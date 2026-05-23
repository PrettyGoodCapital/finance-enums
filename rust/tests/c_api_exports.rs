use finance_enums::{
    finance_enums_currency_export_v1, finance_enums_enum_export_v1,
    finance_enums_exchange_export_v1, CURRENCY_EXPORT_ABI_VERSION, ENUM_EXPORT_ABI_VERSION,
    EXCHANGE_EXPORT_ABI_VERSION,
};
use std::ffi::CStr;

#[test]
fn test_currency_and_exchange_exports_are_available_via_c_api() {
    let currency_export = unsafe { &*finance_enums_currency_export_v1() };
    let exchange_export = unsafe { &*finance_enums_exchange_export_v1() };

    assert_eq!(currency_export.abi_version, CURRENCY_EXPORT_ABI_VERSION);
    assert!(currency_export.records_len > 0);
    assert_eq!(exchange_export.abi_version, EXCHANGE_EXPORT_ABI_VERSION);
    assert!(exchange_export.records_len > 0);
}

#[test]
fn test_enum_export_covers_all_enum_families() {
    let enum_export = unsafe { &*finance_enums_enum_export_v1() };

    assert_eq!(enum_export.abi_version, ENUM_EXPORT_ABI_VERSION);
    assert!(enum_export.family_count > 50);
    assert!(enum_export.records_len > enum_export.family_count);

    let records =
        unsafe { std::slice::from_raw_parts(enum_export.records, enum_export.records_len) };
    let side_buy = records.iter().any(|record| {
        let enum_name = unsafe { CStr::from_ptr(record.enum_name) }
            .to_str()
            .unwrap();
        let variant = unsafe { CStr::from_ptr(record.variant) }.to_str().unwrap();
        enum_name == "Side" && variant == "Buy" && record.ordinal == 1
    });

    assert!(side_buy);
}
