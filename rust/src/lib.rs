pub mod currency_data;
pub mod data;
pub mod enum_data;
pub mod exchange_codes;
pub mod exchange_data;

pub use currency_data::{
    CurrencyAliasRecordRaw, CurrencyDataExportV1, CurrencyRecordRaw, CURRENCY_EXPORT_ABI_VERSION,
};
pub use enum_data::{EnumDataExportV1, EnumVariantRecordRaw, ENUM_EXPORT_ABI_VERSION};
pub use exchange_data::{ExchangeDataExportV1, ExchangeRecordRaw, EXCHANGE_EXPORT_ABI_VERSION};

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
