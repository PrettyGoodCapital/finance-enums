//! C ABI for finance-enums: `libfinance_enums`.
//!
//! Every pointer returned by this library points into data the library owns
//! and stays valid for the lifetime of the process; callers never free it.

#![allow(clippy::missing_safety_doc)]

use std::ffi::{c_char, CStr, CString};
use std::ptr;
use std::sync::OnceLock;

use finance_enums_core::data::{
    exchange_records, CountryCodeAlpha2_NAMES, CURRENCY_ALIAS_RECORDS, CURRENCY_RECORDS,
};
use finance_enums_core::enum_data::{enum_family_spec, enum_family_specs, EnumFamilySpec};

/// Layout version of `CurrencyDataExportV1` and its record structs.
pub const FINANCE_ENUMS_CURRENCY_EXPORT_ABI_VERSION: u32 = 1;
/// Layout version of `ExchangeDataExportV1` and its record struct.
pub const FINANCE_ENUMS_EXCHANGE_EXPORT_ABI_VERSION: u32 = 1;
/// Layout version of `EnumDataExportV1` and its record struct.
pub const FINANCE_ENUMS_ENUM_EXPORT_ABI_VERSION: u32 = 1;

/// Major component of the semantic enum-data ABI version: the ordinal layout
/// exposed to foreign consumers. This is distinct from the per-export
/// `*_EXPORT_ABI_VERSION` constants, which only track the binary layout of each
/// export struct.
///
/// The three components mirror the package version and are kept in sync by
/// bump-my-version. While major is zero, every minor is an independent beta
/// ABI. Starting with 1.0:
/// - MAJOR: a variant or family was reordered, removed, or renamed, or an
///   export struct layout changed. Consumers built against a different major
///   must not use the library.
/// - MINOR: new variants appended to a family, or new families. Existing
///   ordinals never move.
/// - PATCH: any other change that does not affect the ordinal layout.
///
/// A consumer bakes these constants into its binary and calls
/// `finance_enums_abi_compatible()` (or `finance_enums_abi_header_compatible()`)
/// against the loaded library.
pub const FINANCE_ENUMS_ABI_VERSION_MAJOR: u32 = 0;
/// Minor component of the semantic enum-data ABI version.
pub const FINANCE_ENUMS_ABI_VERSION_MINOR: u32 = 8;
/// Patch component of the semantic enum-data ABI version.
pub const FINANCE_ENUMS_ABI_VERSION_PATCH: u32 = 0;

/// One currency: ISO 4217 code (or project extension), display name, and
/// whether the code is official ISO 4217.
#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct CurrencyRecordRaw {
    pub code: *const c_char,
    pub display_name: *const c_char,
    pub is_iso4217: bool,
}

/// An alternate spelling of a currency code and the code it resolves to.
#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct CurrencyAliasRecordRaw {
    pub alias: *const c_char,
    pub canonical_code: *const c_char,
}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
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

/// One ISO 10383 market identifier code record.
#[repr(C)]
#[derive(Clone, Copy, Debug)]
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
#[derive(Clone, Copy, Debug)]
pub struct ExchangeDataExportV1 {
    pub abi_version: u32,
    pub export_struct_size: usize,
    pub exchange_record_size: usize,
    pub records: *const ExchangeRecordRaw,
    pub records_len: usize,
}

/// One `(family, variant, ordinal)` triple. Records are laid out family by
/// family, each family in ordinal order.
#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct EnumVariantRecordRaw {
    pub enum_name: *const c_char,
    pub variant: *const c_char,
    pub ordinal: usize,
}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct EnumDataExportV1 {
    pub abi_version: u32,
    pub export_struct_size: usize,
    pub enum_variant_record_size: usize,
    pub records: *const EnumVariantRecordRaw,
    pub records_len: usize,
    pub family_count: usize,
    /// Highest ordinal across all families. Ordinals can have gaps, so this is
    /// an upper bound, not a variant count.
    pub max_ordinal: usize,
}

unsafe impl Sync for CurrencyDataExportV1 {}
unsafe impl Send for CurrencyDataExportV1 {}
unsafe impl Sync for ExchangeDataExportV1 {}
unsafe impl Send for ExchangeDataExportV1 {}
unsafe impl Sync for EnumDataExportV1 {}
unsafe impl Send for EnumDataExportV1 {}

/// Keeps the record arrays alive behind an export struct that points into them.
struct Backing<T> {
    _arrays: Vec<Box<dyn std::any::Any>>,
    export: T,
}

unsafe impl<T> Sync for Backing<T> {}
unsafe impl<T> Send for Backing<T> {}

fn leak_c_string(value: &str) -> *const c_char {
    CString::new(value)
        .expect("finance_enums string contained interior NUL")
        .into_raw()
        .cast_const()
}

fn build_currency_export() -> Backing<CurrencyDataExportV1> {
    let records: Box<[CurrencyRecordRaw]> = CURRENCY_RECORDS
        .iter()
        .map(|record| CurrencyRecordRaw {
            code: leak_c_string(record.code),
            display_name: leak_c_string(record.display_name),
            is_iso4217: record.is_iso4217,
        })
        .collect();
    let aliases: Box<[CurrencyAliasRecordRaw]> = CURRENCY_ALIAS_RECORDS
        .iter()
        .map(|record| CurrencyAliasRecordRaw {
            alias: leak_c_string(record.alias),
            canonical_code: leak_c_string(record.canonical_code),
        })
        .collect();
    let export = CurrencyDataExportV1 {
        abi_version: FINANCE_ENUMS_CURRENCY_EXPORT_ABI_VERSION,
        export_struct_size: std::mem::size_of::<CurrencyDataExportV1>(),
        currency_record_size: std::mem::size_of::<CurrencyRecordRaw>(),
        currency_alias_record_size: std::mem::size_of::<CurrencyAliasRecordRaw>(),
        records: records.as_ptr(),
        records_len: records.len(),
        aliases: aliases.as_ptr(),
        aliases_len: aliases.len(),
    };
    Backing {
        _arrays: vec![Box::new(records), Box::new(aliases)],
        export,
    }
}

fn build_exchange_export() -> Backing<ExchangeDataExportV1> {
    let records: Box<[ExchangeRecordRaw]> = exchange_records()
        .iter()
        .map(|record| ExchangeRecordRaw {
            mic: leak_c_string(record.mic),
            market_name: leak_c_string(record.market_name),
            legal_entity_name: leak_c_string(record.legal_entity_name),
            operating_mic: leak_c_string(record.operating_mic),
            parent_mic: leak_c_string(record.parent_mic),
            market_category_code: leak_c_string(record.market_category_code),
            acronym: leak_c_string(record.acronym),
            iso_country_code: leak_c_string(record.iso_country_code),
            city: leak_c_string(record.city),
            website: leak_c_string(record.website),
            status: leak_c_string(record.status),
            region: leak_c_string(record.region),
            subregion: leak_c_string(record.subregion),
            is_segment: record.is_segment,
            is_official: record.is_official,
        })
        .collect();
    let export = ExchangeDataExportV1 {
        abi_version: FINANCE_ENUMS_EXCHANGE_EXPORT_ABI_VERSION,
        export_struct_size: std::mem::size_of::<ExchangeDataExportV1>(),
        exchange_record_size: std::mem::size_of::<ExchangeRecordRaw>(),
        records: records.as_ptr(),
        records_len: records.len(),
    };
    Backing {
        _arrays: vec![Box::new(records)],
        export,
    }
}

fn build_enum_export() -> Backing<EnumDataExportV1> {
    let records: Box<[EnumVariantRecordRaw]> = enum_family_specs()
        .iter()
        .flat_map(|family| {
            family
                .iter()
                .map(move |(variant, ordinal)| EnumVariantRecordRaw {
                    enum_name: leak_c_string(family.name),
                    variant: leak_c_string(variant),
                    ordinal: ordinal as usize,
                })
        })
        .collect();
    let export = EnumDataExportV1 {
        abi_version: FINANCE_ENUMS_ENUM_EXPORT_ABI_VERSION,
        export_struct_size: std::mem::size_of::<EnumDataExportV1>(),
        enum_variant_record_size: std::mem::size_of::<EnumVariantRecordRaw>(),
        records: records.as_ptr(),
        records_len: records.len(),
        family_count: enum_family_specs().len(),
        max_ordinal: enum_family_specs()
            .iter()
            .map(|family| family.max_ordinal() as usize)
            .max()
            .unwrap_or(0),
    };
    Backing {
        _arrays: vec![Box::new(records)],
        export,
    }
}

struct CountryNames(Box<[*const c_char]>);

unsafe impl Sync for CountryNames {}
unsafe impl Send for CountryNames {}

static CURRENCY_EXPORT: OnceLock<Backing<CurrencyDataExportV1>> = OnceLock::new();
static EXCHANGE_EXPORT: OnceLock<Backing<ExchangeDataExportV1>> = OnceLock::new();
static ENUM_EXPORT: OnceLock<Backing<EnumDataExportV1>> = OnceLock::new();
static COUNTRY_NAMES: OnceLock<CountryNames> = OnceLock::new();

/// Currency records and aliases.
#[no_mangle]
pub extern "C" fn finance_enums_currency_export_v1() -> *const CurrencyDataExportV1 {
    &CURRENCY_EXPORT.get_or_init(build_currency_export).export
}

/// ISO 10383 exchange records, including project-defined calendar families.
#[no_mangle]
pub extern "C" fn finance_enums_exchange_export_v1() -> *const ExchangeDataExportV1 {
    &EXCHANGE_EXPORT.get_or_init(build_exchange_export).export
}

/// Every enum family and variant with its ordinal.
#[no_mangle]
pub extern "C" fn finance_enums_enum_export_v1() -> *const EnumDataExportV1 {
    &ENUM_EXPORT.get_or_init(build_enum_export).export
}

/// Writes the library's runtime enum-data ABI version into the out-pointers.
/// Any pointer that is null is skipped.
#[no_mangle]
pub unsafe extern "C" fn finance_enums_abi_version(
    major: *mut u32,
    minor: *mut u32,
    patch: *mut u32,
) {
    if !major.is_null() {
        *major = FINANCE_ENUMS_ABI_VERSION_MAJOR;
    }
    if !minor.is_null() {
        *minor = FINANCE_ENUMS_ABI_VERSION_MINOR;
    }
    if !patch.is_null() {
        *patch = FINANCE_ENUMS_ABI_VERSION_PATCH;
    }
}

/// Returns 1 if a consumer built against `(consumer_major, consumer_minor)` is
/// compatible with the loaded library, 0 otherwise. While major is zero, minor
/// must also match because the ABI is beta. Starting with 1.0, the library's
/// minor may be newer than the consumer's.
#[no_mangle]
pub extern "C" fn finance_enums_abi_compatible(consumer_major: u32, consumer_minor: u32) -> i32 {
    finance_enums_core::abi_compatible(consumer_major, consumer_minor) as i32
}

/// Borrows a C string as `&str`, returning `None` for null or non-UTF-8.
///
/// # Safety
/// `value` must be null or point to a valid NUL-terminated C string.
unsafe fn borrow_cstr<'a>(value: *const c_char) -> Option<&'a str> {
    if value.is_null() {
        return None;
    }
    CStr::from_ptr(value).to_str().ok()
}

/// The family named by the C string `family`.
///
/// # Safety
/// `family` must be null or point to a valid NUL-terminated C string.
unsafe fn family_spec(family: *const c_char) -> Option<&'static EnumFamilySpec> {
    borrow_cstr(family).and_then(enum_family_spec)
}

/// Number of variants in `family`, or -1 if the family is unknown.
#[no_mangle]
pub unsafe extern "C" fn finance_enums_family_variant_count(family: *const c_char) -> isize {
    match family_spec(family) {
        Some(spec) => spec.variants.len() as isize,
        None => -1,
    }
}

/// Size in bytes (1, 2, or 4) of `family`'s ordinal type, or -1 if the family
/// is unknown. A C or C++ enum mirroring the family should use an unsigned
/// integer of this size.
#[no_mangle]
pub unsafe extern "C" fn finance_enums_family_ordinal_size(family: *const c_char) -> isize {
    match family_spec(family) {
        Some(spec) => spec.ordinal_size as isize,
        None => -1,
    }
}

/// Returns 1 if some variant of `family` has `ordinal`, 0 if none does, or -1
/// if the family is unknown. Ordinals can have gaps, so this is a membership
/// test, not a range check.
#[no_mangle]
pub unsafe extern "C" fn finance_enums_validate_ordinal(
    family: *const c_char,
    ordinal: usize,
) -> i32 {
    match family_spec(family) {
        Some(spec) => {
            u32::try_from(ordinal).is_ok_and(|ordinal| spec.contains_ordinal(ordinal)) as i32
        }
        None => -1,
    }
}

/// Ordinal of `variant` within `family`, or -1 if either is unknown.
#[no_mangle]
pub unsafe extern "C" fn finance_enums_ordinal_of(
    family: *const c_char,
    variant: *const c_char,
) -> isize {
    let (Some(family), Some(variant)) = (borrow_cstr(family), borrow_cstr(variant)) else {
        return -1;
    };
    match enum_family_spec(family).and_then(|spec| spec.variant_ordinal(variant)) {
        Some(ordinal) => ordinal as isize,
        None => -1,
    }
}

/// NUL-terminated variant name for `(family, ordinal)`, or null if the pair is
/// invalid.
#[no_mangle]
pub unsafe extern "C" fn finance_enums_variant_name(
    family: *const c_char,
    ordinal: usize,
) -> *const c_char {
    let Some(family) = borrow_cstr(family) else {
        return ptr::null();
    };
    // Records are laid out family by family in registration order, each family
    // in declaration order, so the record for a variant is at the family's
    // offset plus the variant's declaration index.
    let export = &*finance_enums_enum_export_v1();
    let mut offset = 0usize;
    for spec in enum_family_specs() {
        if spec.name == family {
            let Some(index) = u32::try_from(ordinal)
                .ok()
                .and_then(|ordinal| spec.index_of_ordinal(ordinal))
            else {
                return ptr::null();
            };
            let records = std::slice::from_raw_parts(export.records, export.records_len);
            return records[offset + index].variant;
        }
        offset += spec.variants.len();
    }
    ptr::null()
}

/// English short name of the country at `ordinal` in `CountryCodeAlpha2` (the
/// same ordinal in `CountryCodeAlpha3`), or null if out of range.
#[no_mangle]
pub extern "C" fn finance_enums_country_name(ordinal: usize) -> *const c_char {
    let names = COUNTRY_NAMES.get_or_init(|| {
        CountryNames(
            CountryCodeAlpha2_NAMES
                .iter()
                .map(|name| leak_c_string(name))
                .collect(),
        )
    });
    names.0.get(ordinal).copied().unwrap_or(ptr::null())
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::ffi::CString;

    #[test]
    fn abi_version_matches_core() {
        assert_eq!(
            FINANCE_ENUMS_ABI_VERSION_MAJOR,
            finance_enums_core::ENUM_ABI_VERSION_MAJOR
        );
        assert_eq!(
            FINANCE_ENUMS_ABI_VERSION_MINOR,
            finance_enums_core::ENUM_ABI_VERSION_MINOR
        );
        assert_eq!(
            FINANCE_ENUMS_ABI_VERSION_PATCH,
            finance_enums_core::ENUM_ABI_VERSION_PATCH
        );
    }

    #[test]
    fn abi_version_and_compat() {
        let (mut major, mut minor, mut patch) = (0u32, 0u32, 0u32);
        unsafe { finance_enums_abi_version(&mut major, &mut minor, &mut patch) };
        assert_eq!(
            (major, minor, patch),
            (
                FINANCE_ENUMS_ABI_VERSION_MAJOR,
                FINANCE_ENUMS_ABI_VERSION_MINOR,
                FINANCE_ENUMS_ABI_VERSION_PATCH
            )
        );

        unsafe { finance_enums_abi_version(ptr::null_mut(), ptr::null_mut(), ptr::null_mut()) };

        assert_eq!(finance_enums_abi_compatible(major, minor), 1);
        assert_eq!(finance_enums_abi_compatible(major, minor + 1), 0);
        assert_eq!(finance_enums_abi_compatible(0, 6), 0);
        assert_eq!(finance_enums_abi_compatible(major + 1, minor), 0);
    }

    #[test]
    fn validate_and_lookup() {
        let some_family = enum_family_specs()[0];
        let family_name = CString::new(some_family.name).unwrap();
        let variant = CString::new(some_family.variants[0]).unwrap();
        let bogus = CString::new("Bogus__NoSuchFamily").unwrap();

        unsafe {
            assert_eq!(finance_enums_validate_ordinal(family_name.as_ptr(), 0), 1);
            assert_eq!(
                finance_enums_validate_ordinal(family_name.as_ptr(), usize::MAX),
                0
            );
            assert_eq!(finance_enums_validate_ordinal(bogus.as_ptr(), 0), -1);
            assert_eq!(
                finance_enums_ordinal_of(family_name.as_ptr(), variant.as_ptr()),
                0
            );
            assert_eq!(finance_enums_family_variant_count(bogus.as_ptr()), -1);
            assert_eq!(
                finance_enums_family_variant_count(family_name.as_ptr()) as usize,
                some_family.variants.len()
            );

            let name = finance_enums_variant_name(family_name.as_ptr(), 0);
            assert_eq!(
                CStr::from_ptr(name).to_str().unwrap(),
                some_family.variants[0]
            );
            assert!(finance_enums_variant_name(family_name.as_ptr(), usize::MAX).is_null());
        }
    }

    #[test]
    fn country_names_cover_alpha2_ordinals() {
        let us = finance_enums_core::data::CountryCodeAlpha2::US as usize;
        let name = unsafe { CStr::from_ptr(finance_enums_country_name(us)) };
        assert_eq!(name.to_str().unwrap(), "United States of America");
        assert!(finance_enums_country_name(CountryCodeAlpha2_NAMES.len()).is_null());
    }
}
