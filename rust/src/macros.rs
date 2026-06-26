/// Declares a typed `#[repr(usize)]` enum from a list of variant identifiers,
/// injecting an `Invalid` sentinel at ordinal 0 so every real variant has a
/// non-zero ordinal.
///
/// Use [`finance_enum_raw!`] instead when the family already supplies its own
/// ordinal-0 sentinel (e.g. ISO code families whose "unknown" code lives at 0).
///
/// The macro produces:
/// - A `#[repr(usize)]` enum with `Debug`, `Clone`, `Copy`, `PartialEq`, `Eq`, `Hash`
/// - `VARIANTS: &[&str]` and `COUNT: usize` associated constants
/// - `from_ordinal(usize) -> Option<Self>` constructor
/// - `name(self) -> &'static str` / `as_str(self) -> &'static str` accessors (to-string)
/// - `from_name(&str) -> Option<Self>` plus a `std::str::FromStr` impl (from-string)
/// - `From<E> for usize`, `TryFrom<usize> for E`, `Display`
///
/// Usage:
///
/// ```rust,ignore
/// finance_enum!(Side: None, Buy, Sell);
///
/// assert_eq!(Side::Invalid as usize, 0);
/// assert_eq!(Side::Buy as usize, 2);
/// assert_eq!(Side::from_name("Sell"), Some(Side::Sell));
/// assert_eq!(Side::VARIANTS, &["Invalid", "None", "Buy", "Sell"]);
/// ```
#[macro_export]
macro_rules! finance_enum {
    ($name:ident : $($variant:ident),+ $(,)?) => {
        $crate::finance_enum_raw!($name : Invalid, $($variant),+);
    };
}

/// Like [`finance_enum!`] but does **not** inject an `Invalid` sentinel; the
/// caller is responsible for placing an ordinal-0 sentinel (e.g. an ISO
/// "unknown" code) at the front of the variant list.
#[macro_export]
macro_rules! finance_enum_raw {
    ($name:ident : $($variant:ident),+ $(,)?) => {
        #[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
        #[repr(usize)]
        #[allow(non_camel_case_types)]
        pub enum $name {
            $($variant),+
        }

        impl $name {
            pub const VARIANTS: &[&str] = &[$(stringify!($variant)),+];
            pub const COUNT: usize = Self::VARIANTS.len();

            #[inline]
            pub fn from_ordinal(ordinal: usize) -> Option<Self> {
                if ordinal < Self::COUNT {
                    // SAFETY: repr(usize) with contiguous values 0..COUNT
                    Some(unsafe { std::mem::transmute::<usize, Self>(ordinal) })
                } else {
                    None
                }
            }

            #[inline]
            pub fn name(self) -> &'static str {
                Self::VARIANTS[self as usize]
            }

            /// Returns the canonical string name of the variant (to-string).
            /// Alias for [`Self::name`].
            #[inline]
            pub fn as_str(self) -> &'static str {
                self.name()
            }

            /// Parses a variant from its canonical string name (from-string).
            /// Returns `None` for unknown names.
            ///
            /// Named `from_name` (not `from_str`) so it does not shadow the
            /// `std::str::FromStr::from_str` trait method, which returns `Result`.
            #[inline]
            pub fn from_name(value: &str) -> Option<Self> {
                let mut ordinal = 0usize;
                while ordinal < Self::COUNT {
                    if Self::VARIANTS[ordinal] == value {
                        return Self::from_ordinal(ordinal);
                    }
                    ordinal += 1;
                }
                None
            }
        }

        impl From<$name> for usize {
            #[inline]
            fn from(v: $name) -> usize { v as usize }
        }

        impl TryFrom<usize> for $name {
            type Error = ();
            #[inline]
            fn try_from(v: usize) -> Result<Self, ()> {
                Self::from_ordinal(v).ok_or(())
            }
        }

        impl std::str::FromStr for $name {
            type Err = ();
            #[inline]
            fn from_str(value: &str) -> Result<Self, ()> {
                $name::from_name(value).ok_or(())
            }
        }

        impl std::fmt::Display for $name {
            fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                f.write_str(self.name())
            }
        }
    };
}
