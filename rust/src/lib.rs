#[macro_use]
pub mod macros;
pub mod currency_data;
pub mod data;
pub mod enum_data;
pub mod exchange_codes;
pub mod exchange_data;

#[cfg(feature = "polars")]
pub mod polars;

pub use currency_data::{
    CurrencyAliasRecordRaw, CurrencyDataExportV1, CurrencyRecordRaw, CURRENCY_EXPORT_ABI_VERSION,
};
pub use enum_data::{
    abi_compatible, assert_abi_compatible, EnumDataExportV1, EnumVariantRecordRaw,
    ENUM_ABI_VERSION_MAJOR, ENUM_ABI_VERSION_MINOR, ENUM_ABI_VERSION_PATCH,
    ENUM_EXPORT_ABI_VERSION,
};
pub use exchange_data::{ExchangeDataExportV1, ExchangeRecordRaw, EXCHANGE_EXPORT_ABI_VERSION};

use std::ffi::{c_char, CStr};
use std::ptr;

#[no_mangle]
pub extern "C" fn finance_enums_currency_export_v1() -> *const CurrencyDataExportV1 {
    &currency_data::CURRENCY_EXPORT_V1
}

#[no_mangle]
pub extern "C" fn finance_enums_exchange_export_v1() -> *const ExchangeDataExportV1 {
    exchange_data::exchange_export_v1() as *const ExchangeDataExportV1
}

#[no_mangle]
pub extern "C" fn finance_enums_enum_export_v1() -> *const EnumDataExportV1 {
    enum_data::enum_export_v1() as *const EnumDataExportV1
}

/// Writes the library's semantic enum-data ABI version into the provided
/// out-pointers. Any pointer that is null is skipped, so a caller may request
/// only the components it cares about.
#[no_mangle]
#[allow(clippy::not_unsafe_ptr_arg_deref)]
pub extern "C" fn finance_enums_abi_version(major: *mut u32, minor: *mut u32, patch: *mut u32) {
    if !major.is_null() {
        unsafe { *major = ENUM_ABI_VERSION_MAJOR };
    }
    if !minor.is_null() {
        unsafe { *minor = ENUM_ABI_VERSION_MINOR };
    }
    if !patch.is_null() {
        unsafe { *patch = ENUM_ABI_VERSION_PATCH };
    }
}

/// Returns `1` if a consumer built against `(consumer_major, consumer_minor)` is
/// compatible with this library, `0` otherwise. See [`enum_data::abi_compatible`].
#[no_mangle]
pub extern "C" fn finance_enums_abi_compatible(consumer_major: u32, consumer_minor: u32) -> i32 {
    abi_compatible(consumer_major, consumer_minor) as i32
}

/// Borrow a C string pointer as a `&str`, returning `None` for null or non-UTF-8.
///
/// # Safety
/// `ptr` must be null or point to a valid NUL-terminated C string.
unsafe fn borrow_cstr<'a>(ptr: *const c_char) -> Option<&'a str> {
    if ptr.is_null() {
        return None;
    }
    CStr::from_ptr(ptr).to_str().ok()
}

/// Returns the number of variants in `family`, or `-1` if the family is unknown.
#[no_mangle]
#[allow(clippy::not_unsafe_ptr_arg_deref)]
pub extern "C" fn finance_enums_family_variant_count(family: *const c_char) -> isize {
    match unsafe { borrow_cstr(family) }.and_then(enum_data::enum_variants) {
        Some(variants) => variants.len() as isize,
        None => -1,
    }
}

/// Returns `1` if `ordinal` is a valid variant of `family`, `0` if it is out of
/// range, or `-1` if the family is unknown.
#[no_mangle]
#[allow(clippy::not_unsafe_ptr_arg_deref)]
pub extern "C" fn finance_enums_validate_ordinal(family: *const c_char, ordinal: usize) -> i32 {
    match unsafe { borrow_cstr(family) }.and_then(enum_data::enum_variants) {
        Some(variants) if ordinal < variants.len() => 1,
        Some(_) => 0,
        None => -1,
    }
}

/// Returns the ordinal of `variant` within `family`, or `-1` if the variant or
/// family is unknown.
#[no_mangle]
#[allow(clippy::not_unsafe_ptr_arg_deref)]
pub extern "C" fn finance_enums_ordinal_of(family: *const c_char, variant: *const c_char) -> isize {
    let (Some(family), Some(variant)) = (unsafe { borrow_cstr(family) }, unsafe {
        borrow_cstr(variant)
    }) else {
        return -1;
    };
    match enum_data::enum_variant_ordinal(family, variant) {
        Some(ordinal) => ordinal as isize,
        None => -1,
    }
}

/// Returns the NUL-terminated variant name for `(family, ordinal)`, or null if
/// the pair is invalid. The returned pointer is valid for the library's lifetime.
#[no_mangle]
#[allow(clippy::not_unsafe_ptr_arg_deref)]
pub extern "C" fn finance_enums_variant_name(
    family: *const c_char,
    ordinal: usize,
) -> *const c_char {
    let Some(family) = (unsafe { borrow_cstr(family) }) else {
        return ptr::null();
    };
    // Records are laid out family-by-family in registration order (see
    // enum_data::build_enum_export_v1), so the record for (family, ordinal) lives
    // at `family_offset + ordinal`. Walk the family specs (O(families)) to find the
    // offset rather than scanning every record.
    let export = enum_data::enum_export_v1();
    let mut offset = 0usize;
    for spec in enum_data::enum_family_specs() {
        if spec.name == family {
            if ordinal >= spec.variants.len() {
                return ptr::null();
            }
            let records = unsafe { std::slice::from_raw_parts(export.records, export.records_len) };
            return records[offset + ordinal].variant;
        }
        offset += spec.variants.len();
    }
    ptr::null()
}

#[cfg(test)]
mod ffi_tests {
    use super::*;
    use std::ffi::CString;

    #[test]
    fn c_abi_version_and_compat() {
        let (mut major, mut minor, mut patch) = (0u32, 0u32, 0u32);
        finance_enums_abi_version(&mut major, &mut minor, &mut patch);
        assert_eq!(major, ENUM_ABI_VERSION_MAJOR);
        assert_eq!(minor, ENUM_ABI_VERSION_MINOR);
        assert_eq!(patch, ENUM_ABI_VERSION_PATCH);

        finance_enums_abi_version(ptr::null_mut(), ptr::null_mut(), ptr::null_mut());

        assert_eq!(
            finance_enums_abi_compatible(ENUM_ABI_VERSION_MAJOR, ENUM_ABI_VERSION_MINOR),
            1
        );
        assert_eq!(
            finance_enums_abi_compatible(ENUM_ABI_VERSION_MAJOR, ENUM_ABI_VERSION_MINOR + 1),
            0
        );
        assert_eq!(finance_enums_abi_compatible(0, 6), 0);
        assert_eq!(
            finance_enums_abi_compatible(ENUM_ABI_VERSION_MAJOR + 1, ENUM_ABI_VERSION_MINOR),
            0
        );
    }

    #[test]
    fn c_abi_validate_and_lookup() {
        // Pick a family/variant known to exist via the public Rust API.
        let some_family = enum_data::enum_family_specs()[0];
        let family_name = CString::new(some_family.name).unwrap();
        let variant_name_str = some_family.variants[0];
        let variant = CString::new(variant_name_str).unwrap();
        let bogus = CString::new("Bogus__NoSuchFamily").unwrap();

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
        assert!(!name.is_null());
        let name = unsafe { CStr::from_ptr(name) }.to_str().unwrap();
        assert_eq!(name, variant_name_str);
        assert!(finance_enums_variant_name(family_name.as_ptr(), usize::MAX).is_null());
    }
}
