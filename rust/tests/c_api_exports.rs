use finance_enums::{
    finance_enums_currency_export_v1, finance_enums_exchange_export_v1,
    CURRENCY_EXPORT_ABI_VERSION, EXCHANGE_EXPORT_ABI_VERSION,
};

#[test]
fn test_currency_and_exchange_exports_are_available_via_c_api() {
    let currency_export = unsafe { &*finance_enums_currency_export_v1() };
    let exchange_export = unsafe { &*finance_enums_exchange_export_v1() };

    assert_eq!(currency_export.abi_version, CURRENCY_EXPORT_ABI_VERSION);
    assert!(currency_export.records_len > 0);
    assert_eq!(exchange_export.abi_version, EXCHANGE_EXPORT_ABI_VERSION);
    assert!(exchange_export.records_len > 0);
}
