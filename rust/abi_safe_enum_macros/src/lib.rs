//! Implementation of `#[abi_safe_enum]`. Use it through the `abi_safe_enum`
//! crate, which re-exports the attribute alongside the trait it implements.

use proc_macro::TokenStream;
use proc_macro2::Span;
use quote::{format_ident, quote};
use syn::spanned::Spanned;
use syn::{parse_macro_input, Error, Expr, ExprLit, Fields, Ident, ItemEnum, Lit, Result};

#[derive(Clone, Copy, PartialEq, PartialOrd)]
enum Width {
    U8,
    U16,
    U32,
}

impl Width {
    fn smallest_for(max: u64) -> Option<Self> {
        if max <= u64::from(u8::MAX) {
            Some(Self::U8)
        } else if max <= u64::from(u16::MAX) {
            Some(Self::U16)
        } else if max <= u64::from(u32::MAX) {
            Some(Self::U32)
        } else {
            None
        }
    }

    fn parse(ident: &Ident) -> Result<Self> {
        match ident.to_string().as_str() {
            "u8" => Ok(Self::U8),
            "u16" => Ok(Self::U16),
            "u32" => Ok(Self::U32),
            _ => Err(Error::new(ident.span(), "repr must be one of u8, u16, u32")),
        }
    }

    fn ident(self) -> Ident {
        let name = match self {
            Self::U8 => "u8",
            Self::U16 => "u16",
            Self::U32 => "u32",
        };
        Ident::new(name, Span::call_site())
    }

    fn bytes(self) -> usize {
        match self {
            Self::U8 => 1,
            Self::U16 => 2,
            Self::U32 => 4,
        }
    }
}

/// Declares a fieldless enum whose ordinals are part of an ABI.
///
/// See the `abi_safe_enum` crate for the full contract.
#[proc_macro_attribute]
pub fn abi_safe_enum(args: TokenStream, input: TokenStream) -> TokenStream {
    let mut pinned: Option<(Width, Span)> = None;
    let parser = syn::meta::parser(|meta| {
        if meta.path.is_ident("repr") {
            let ident: Ident = meta.value()?.parse()?;
            pinned = Some((Width::parse(&ident)?, ident.span()));
            Ok(())
        } else {
            Err(meta.error("unsupported abi_safe_enum argument; expected `repr = u8|u16|u32`"))
        }
    });
    parse_macro_input!(args with parser);
    let item = parse_macro_input!(input as ItemEnum);
    expand(item, pinned)
        .unwrap_or_else(Error::into_compile_error)
        .into()
}

fn literal_ordinal(expr: &Expr) -> Result<u64> {
    match expr {
        Expr::Lit(ExprLit {
            lit: Lit::Int(int), ..
        }) => int.base10_parse::<u64>(),
        _ => Err(Error::new(
            expr.span(),
            "abi_safe_enum ordinals must be integer literals",
        )),
    }
}

fn expand(mut item: ItemEnum, pinned: Option<(Width, Span)>) -> Result<proc_macro2::TokenStream> {
    if !item.generics.params.is_empty() {
        return Err(Error::new(
            item.generics.span(),
            "abi_safe_enum does not support generic enums",
        ));
    }
    if let Some(repr) = item.attrs.iter().find(|attr| attr.path().is_ident("repr")) {
        return Err(Error::new(
            repr.span(),
            "abi_safe_enum chooses the #[repr]; use #[abi_safe_enum(repr = u16)] to pin a width",
        ));
    }
    if item.variants.is_empty() {
        return Err(Error::new(
            item.ident.span(),
            "abi_safe_enum needs at least one variant",
        ));
    }

    let mut ordinals: Vec<u64> = Vec::with_capacity(item.variants.len());
    let mut next = 0u64;
    for variant in &item.variants {
        if !matches!(variant.fields, Fields::Unit) {
            return Err(Error::new(
                variant.span(),
                "abi_safe_enum variants cannot carry data",
            ));
        }
        let ordinal = match &variant.discriminant {
            Some((_, expr)) => literal_ordinal(expr)?,
            None => next,
        };
        if let Some(position) = ordinals.iter().position(|seen| *seen == ordinal) {
            let first = &item.variants[position].ident;
            return Err(Error::new(
                variant.span(),
                format!(
                    "ordinal {ordinal} of `{}` is already used by `{first}`",
                    variant.ident
                ),
            ));
        }
        ordinals.push(ordinal);
        next = ordinal + 1;
    }
    if !ordinals.contains(&0) {
        return Err(Error::new(
            item.ident.span(),
            "abi_safe_enum needs a variant with ordinal 0 to act as the invalid/unknown sentinel",
        ));
    }

    let max = *ordinals.iter().max().unwrap();
    let needed = Width::smallest_for(max).ok_or_else(|| {
        Error::new(
            item.ident.span(),
            format!("ordinal {max} does not fit in u32"),
        )
    })?;
    let width = match pinned {
        Some((width, span)) if width < needed => {
            return Err(Error::new(
                span,
                format!("ordinal {max} does not fit in the pinned repr"),
            ));
        }
        Some((width, _)) => width,
        None => needed,
    };

    let repr = width.ident();
    for (variant, ordinal) in item.variants.iter_mut().zip(&ordinals) {
        let literal = syn::LitInt::new(&format!("{ordinal}{repr}"), variant.ident.span());
        variant.discriminant = Some((Default::default(), syn::parse_quote!(#literal)));
    }

    let name = &item.ident;
    let name_text = name.to_string();
    let idents: Vec<&Ident> = item.variants.iter().map(|variant| &variant.ident).collect();
    let names: Vec<String> = idents.iter().map(|ident| ident.to_string()).collect();
    let ordinals_u32: Vec<u32> = ordinals.iter().map(|ordinal| *ordinal as u32).collect();
    let count = idents.len();
    let bytes = width.bytes();
    let runtime = format_ident!("abi_safe_enum");

    Ok(quote! {
        #[repr(#repr)]
        #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord)]
        #[allow(non_camel_case_types)]
        #item

        impl #name {
            /// The enum's name.
            pub const NAME: &'static str = #name_text;
            /// Variant names in declaration order.
            pub const VARIANTS: &'static [&'static str] = &[#(#names),*];
            /// Ordinal of each variant, parallel to `VARIANTS`.
            pub const ORDINALS: &'static [u32] = &[#(#ordinals_u32),*];
            /// Number of variants, including the ordinal-0 sentinel.
            pub const COUNT: usize = #count;
            /// Size in bytes of the enum's representation.
            pub const ORDINAL_SIZE: usize = #bytes;

            /// The variant's ordinal.
            #[inline]
            pub const fn ordinal(self) -> u32 {
                self as #repr as u32
            }

            /// The variant with `ordinal`, or `None` if no variant uses it.
            #[inline]
            pub const fn from_ordinal(ordinal: u32) -> Option<Self> {
                match ordinal {
                    #(#ordinals_u32 => Some(Self::#idents),)*
                    _ => None,
                }
            }

            /// The variant's name.
            #[inline]
            pub const fn name(self) -> &'static str {
                match self {
                    #(Self::#idents => #names,)*
                }
            }

            /// Alias for [`Self::name`].
            #[inline]
            pub const fn as_str(self) -> &'static str {
                self.name()
            }

            /// The variant named `name`, or `None` if no variant has that name.
            #[inline]
            pub fn from_name(name: &str) -> Option<Self> {
                match name {
                    #(#names => Some(Self::#idents),)*
                    _ => None,
                }
            }
        }

        impl ::#runtime::AbiSafeEnum for #name {
            const NAME: &'static str = #name::NAME;
            const VARIANTS: &'static [&'static str] = #name::VARIANTS;
            const ORDINALS: &'static [u32] = #name::ORDINALS;
            const ORDINAL_SIZE: usize = #name::ORDINAL_SIZE;

            fn ordinal(self) -> u32 {
                #name::ordinal(self)
            }

            fn from_ordinal(ordinal: u32) -> Option<Self> {
                #name::from_ordinal(ordinal)
            }

            fn name(self) -> &'static str {
                #name::name(self)
            }

            fn from_name(name: &str) -> Option<Self> {
                #name::from_name(name)
            }
        }

        impl ::core::convert::From<#name> for u32 {
            #[inline]
            fn from(value: #name) -> u32 {
                value.ordinal()
            }
        }

        impl ::core::convert::TryFrom<u32> for #name {
            type Error = ::#runtime::UnknownOrdinal;

            #[inline]
            fn try_from(ordinal: u32) -> ::core::result::Result<Self, Self::Error> {
                Self::from_ordinal(ordinal).ok_or(::#runtime::UnknownOrdinal(ordinal))
            }
        }

        impl ::core::str::FromStr for #name {
            type Err = ::#runtime::UnknownName;

            #[inline]
            fn from_str(name: &str) -> ::core::result::Result<Self, Self::Err> {
                Self::from_name(name).ok_or(::#runtime::UnknownName)
            }
        }

        impl ::core::fmt::Display for #name {
            fn fmt(&self, f: &mut ::core::fmt::Formatter<'_>) -> ::core::fmt::Result {
                f.write_str(self.name())
            }
        }
    })
}
