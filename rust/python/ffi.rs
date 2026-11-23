//! The C ABI of `libfinance_enums`, and safe views over it.
//!
//! With the `direct` feature the `finance_enums` crate (with `capi`) is linked
//! statically.
//! Otherwise (`capi`) the declarations below resolve against the shared
//! library, which hatch-rs links and adds to the rpath.

#![allow(unused_unsafe)]

use std::ffi::{c_char, CStr, CString};
use std::mem::size_of;
use std::sync::OnceLock;

#[cfg(feature = "direct")]
pub use finance_enums::capi::{
    finance_enums_abi_compatible, finance_enums_abi_version, finance_enums_country_name,
    finance_enums_currency_export_v1, finance_enums_enum_export_v1,
    finance_enums_exchange_export_v1, finance_enums_family_ordinal_size,
    finance_enums_family_variant_count, finance_enums_ordinal_of, finance_enums_validate_ordinal,
    finance_enums_variant_name, CurrencyAliasRecordRaw, CurrencyDataExportV1, CurrencyRecordRaw,
    EnumDataExportV1, EnumVariantRecordRaw, ExchangeDataExportV1, ExchangeRecordRaw,
};

#[cfg(not(any(feature = "direct", feature = "capi")))]
compile_error!("enable either the `capi` or the `direct` feature");

#[cfg(not(feature = "direct"))]
mod linked {
    use std::ffi::c_char;

    #[repr(C)]
    pub struct CurrencyRecordRaw {
        pub code: *const c_char,
        pub display_name: *const c_char,
        pub is_iso4217: bool,
    }

    #[repr(C)]
    pub struct CurrencyAliasRecordRaw {
        pub alias: *const c_char,
        pub canonical_code: *const c_char,
    }

    #[repr(C)]
    pub struct CurrencyDataExportV1 {
        pub abi_version: u32,
        pub export_struct_size: usize,
        pub currency_record_size: usize,
        pub currency_alias_record_size: usize,
        pub records: *const CurrencyRecordRaw,
        pub records_len: usize,
        pub aliases: *const CurrencyAliasRecordRaw,
        pub aliases_len: usize,
    }

    #[repr(C)]
    pub struct ExchangeRecordRaw {
        pub mic: *const c_char,
        pub market_name: *const c_char,
        pub legal_entity_name: *const c_char,
        pub operating_mic: *const c_char,
        pub parent_mic: *const c_char,
        pub market_category_code: *const c_char,
        pub acronym: *const c_char,
        pub iso_country_code: *const c_char,
        pub city: *const c_char,
        pub website: *const c_char,
        pub status: *const c_char,
        pub region: *const c_char,
        pub subregion: *const c_char,
        pub is_segment: bool,
        pub is_official: bool,
    }

    #[repr(C)]
    pub struct ExchangeDataExportV1 {
        pub abi_version: u32,
        pub export_struct_size: usize,
        pub exchange_record_size: usize,
        pub records: *const ExchangeRecordRaw,
        pub records_len: usize,
    }

    #[repr(C)]
    pub struct EnumVariantRecordRaw {
        pub enum_name: *const c_char,
        pub variant: *const c_char,
        pub ordinal: usize,
    }

    #[repr(C)]
    pub struct EnumDataExportV1 {
        pub abi_version: u32,
        pub export_struct_size: usize,
        pub enum_variant_record_size: usize,
        pub records: *const EnumVariantRecordRaw,
        pub records_len: usize,
        pub family_count: usize,
        pub max_ordinal: usize,
    }

    extern "C" {
        pub fn finance_enums_currency_export_v1() -> *const CurrencyDataExportV1;
        pub fn finance_enums_exchange_export_v1() -> *const ExchangeDataExportV1;
        pub fn finance_enums_enum_export_v1() -> *const EnumDataExportV1;
        pub fn finance_enums_abi_version(major: *mut u32, minor: *mut u32, patch: *mut u32);
        pub fn finance_enums_abi_compatible(consumer_major: u32, consumer_minor: u32) -> i32;
        pub fn finance_enums_family_variant_count(family: *const c_char) -> isize;
        pub fn finance_enums_family_ordinal_size(family: *const c_char) -> isize;
        pub fn finance_enums_validate_ordinal(family: *const c_char, ordinal: usize) -> i32;
        pub fn finance_enums_ordinal_of(family: *const c_char, variant: *const c_char) -> isize;
        pub fn finance_enums_variant_name(family: *const c_char, ordinal: usize) -> *const c_char;
        pub fn finance_enums_country_name(ordinal: usize) -> *const c_char;
    }
}

#[cfg(not(feature = "direct"))]
pub use linked::*;

/// Export-struct layout version this extension was built against.
const EXPORT_ABI_VERSION: u32 = 1;

/// Borrows a string owned by the library, which never frees it.
pub fn library_str(value: *const c_char) -> &'static str {
    unsafe { CStr::from_ptr(value) }
        .to_str()
        .expect("libfinance_enums returned non-UTF-8 text")
}

pub fn currency_export() -> &'static CurrencyDataExportV1 {
    unsafe { &*finance_enums_currency_export_v1() }
}

pub fn exchange_export() -> &'static ExchangeDataExportV1 {
    unsafe { &*finance_enums_exchange_export_v1() }
}

pub fn enum_export() -> &'static EnumDataExportV1 {
    unsafe { &*finance_enums_enum_export_v1() }
}

/// Fails when the loaded library's export structs do not match the layout
/// declared here, for example after linking a library from another release.
pub fn check_layout() -> Result<(), String> {
    let currency = currency_export();
    let exchange = exchange_export();
    let enums = enum_export();
    let checks = [
        (
            "currency",
            currency.abi_version,
            currency.export_struct_size,
            size_of::<CurrencyDataExportV1>(),
        ),
        (
            "currency record",
            currency.abi_version,
            currency.currency_record_size,
            size_of::<CurrencyRecordRaw>(),
        ),
        (
            "currency alias record",
            currency.abi_version,
            currency.currency_alias_record_size,
            size_of::<CurrencyAliasRecordRaw>(),
        ),
        (
            "exchange",
            exchange.abi_version,
            exchange.export_struct_size,
            size_of::<ExchangeDataExportV1>(),
        ),
        (
            "exchange record",
            exchange.abi_version,
            exchange.exchange_record_size,
            size_of::<ExchangeRecordRaw>(),
        ),
        (
            "enum",
            enums.abi_version,
            enums.export_struct_size,
            size_of::<EnumDataExportV1>(),
        ),
        (
            "enum record",
            enums.abi_version,
            enums.enum_variant_record_size,
            size_of::<EnumVariantRecordRaw>(),
        ),
    ];
    for (name, version, library_size, extension_size) in checks {
        if version != EXPORT_ABI_VERSION || library_size != extension_size {
            return Err(format!(
                "libfinance_enums {name} export does not match this extension: \
                 version {version} (expected {EXPORT_ABI_VERSION}), size {library_size} (expected {extension_size})"
            ));
        }
    }
    Ok(())
}

pub fn currency_records() -> &'static [CurrencyRecordRaw] {
    let export = currency_export();
    unsafe { std::slice::from_raw_parts(export.records, export.records_len) }
}

pub fn currency_alias_records() -> &'static [CurrencyAliasRecordRaw] {
    let export = currency_export();
    unsafe { std::slice::from_raw_parts(export.aliases, export.aliases_len) }
}

pub fn exchange_records() -> &'static [ExchangeRecordRaw] {
    let export = exchange_export();
    unsafe { std::slice::from_raw_parts(export.records, export.records_len) }
}

pub struct Family {
    pub name: &'static str,
    /// `(variant, ordinal)` in declaration order.
    pub variants: Vec<(&'static str, usize)>,
}

/// Enum families in export order, rebuilt from the flat variant records.
pub fn families() -> &'static [Family] {
    static FAMILIES: OnceLock<Vec<Family>> = OnceLock::new();
    FAMILIES.get_or_init(|| {
        let export = enum_export();
        let records = unsafe { std::slice::from_raw_parts(export.records, export.records_len) };
        let mut families: Vec<Family> = Vec::with_capacity(export.family_count);
        for record in records {
            let name = library_str(record.enum_name);
            if families.last().map(|family| family.name) != Some(name) {
                families.push(Family {
                    name,
                    variants: Vec::new(),
                });
            }
            families
                .last_mut()
                .unwrap()
                .variants
                .push((library_str(record.variant), record.ordinal));
        }
        families
    })
}

pub fn country_names() -> Vec<&'static str> {
    (0..)
        .map(|ordinal| unsafe { finance_enums_country_name(ordinal) })
        .take_while(|name| !name.is_null())
        .map(library_str)
        .collect()
}

pub fn abi_version() -> (u32, u32, u32) {
    let (mut major, mut minor, mut patch) = (0, 0, 0);
    unsafe { finance_enums_abi_version(&mut major, &mut minor, &mut patch) };
    (major, minor, patch)
}

pub fn abi_compatible(consumer_major: u32, consumer_minor: u32) -> bool {
    unsafe { finance_enums_abi_compatible(consumer_major, consumer_minor) == 1 }
}

pub fn family_variant_count(family: &str) -> Option<usize> {
    let family = CString::new(family).ok()?;
    usize::try_from(unsafe { finance_enums_family_variant_count(family.as_ptr()) }).ok()
}

pub fn family_ordinal_size(family: &str) -> Option<usize> {
    let family = CString::new(family).ok()?;
    usize::try_from(unsafe { finance_enums_family_ordinal_size(family.as_ptr()) }).ok()
}

pub fn validate_ordinal(family: &str, ordinal: usize) -> Option<bool> {
    let family = CString::new(family).ok()?;
    match unsafe { finance_enums_validate_ordinal(family.as_ptr(), ordinal) } {
        1 => Some(true),
        0 => Some(false),
        _ => None,
    }
}

pub fn ordinal_of(family: &str, variant: &str) -> Option<usize> {
    let family = CString::new(family).ok()?;
    let variant = CString::new(variant).ok()?;
    usize::try_from(unsafe { finance_enums_ordinal_of(family.as_ptr(), variant.as_ptr()) }).ok()
}

pub fn variant_name(family: &str, ordinal: usize) -> Option<&'static str> {
    let family = CString::new(family).ok()?;
    let name = unsafe { finance_enums_variant_name(family.as_ptr(), ordinal) };
    (!name.is_null()).then(|| library_str(name))
}
