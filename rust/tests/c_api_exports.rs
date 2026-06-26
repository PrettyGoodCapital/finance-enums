use finance_enums::{
    enum_data, finance_enums_currency_export_v1, finance_enums_enum_export_v1,
    finance_enums_exchange_export_v1, CURRENCY_EXPORT_ABI_VERSION, ENUM_EXPORT_ABI_VERSION,
    EXCHANGE_EXPORT_ABI_VERSION,
};
use std::collections::{BTreeMap, BTreeSet};
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
    assert_eq!(
        enum_export.family_count,
        enum_data::enum_family_specs().len()
    );
    assert_eq!(
        enum_export.records_len,
        enum_data::enum_family_specs()
            .iter()
            .map(|family| family.variants.len())
            .sum::<usize>()
    );
    assert_eq!(
        enum_export.max_ordinal,
        enum_data::enum_family_specs()
            .iter()
            .map(|family| family.variants.len().saturating_sub(1))
            .max()
            .unwrap_or(0)
    );

    let records =
        unsafe { std::slice::from_raw_parts(enum_export.records, enum_export.records_len) };
    let mut exported = BTreeMap::<String, Vec<(usize, String)>>::new();
    let mut seen_ordinals = BTreeSet::<(String, usize)>::new();
    for record in records {
        let enum_name = unsafe { CStr::from_ptr(record.enum_name) }
            .to_str()
            .unwrap()
            .to_string();
        let variant = unsafe { CStr::from_ptr(record.variant) }
            .to_str()
            .unwrap()
            .to_string();
        assert!(seen_ordinals.insert((enum_name.clone(), record.ordinal)));
        exported
            .entry(enum_name)
            .or_default()
            .push((record.ordinal, variant));
    }

    assert_eq!(exported.len(), enum_data::enum_family_specs().len());
    for family in enum_data::enum_family_specs() {
        let variants = exported
            .get_mut(family.name)
            .unwrap_or_else(|| panic!("missing enum family {}", family.name));
        variants.sort_by_key(|(ordinal, _)| *ordinal);
        let exported_variants = variants
            .iter()
            .map(|(ordinal, variant)| {
                assert_eq!(family.variants[*ordinal], variant);
                variant.as_str()
            })
            .collect::<Vec<_>>();
        assert_eq!(exported_variants, family.variants);
    }

    // Regression guards: these families/variants were intentionally never
    // registered (or removed); assert they do not reappear in the C ABI export.
    assert!(!exported.contains_key("ModelDataScope"));
    assert!(!exported.contains_key("Region"));
    assert!(!exported.contains_key("Urgency"));
    assert!(!exported
        .get("OrderSide")
        .unwrap()
        .iter()
        .any(|(_, variant)| variant == "SellShortExempt"));
}
