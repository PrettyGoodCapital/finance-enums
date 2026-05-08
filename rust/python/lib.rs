//! pyo3 bindings exposing the static enum tables to Python.

use pyo3::prelude::*;

use ::finance_enums::data::*;

macro_rules! variant_fn {
    ($name:ident, $arr:ident) => {
        #[pyfunction]
        fn $name() -> Vec<&'static str> { $arr.to_vec() }
    };
}

variant_fn!(country_code_variants, CountryCode_VARIANTS);
variant_fn!(country_code3_variants, CountryCode3_VARIANTS);
variant_fn!(country_names, CountryNames_ARRAY);
variant_fn!(currency_variants, Currency_VARIANTS);
variant_fn!(currency_names, CurrencyName_ARRAY);
variant_fn!(exchange_code_variants, ExchangeCode_VARIANTS);
variant_fn!(sector_variants, Sector_VARIANTS);
variant_fn!(industry_group_variants, IndustryGroup_VARIANTS);
variant_fn!(industry_variants, Industry_VARIANTS);
variant_fn!(sub_industry_variants, SubIndustry_VARIANTS);
variant_fn!(security_type_variants, SecurityType_VARIANTS);
variant_fn!(instrument_type_variants, InstrumentType_VARIANTS);
variant_fn!(equity_type_variants, EquityType_VARIANTS);
variant_fn!(option_type_variants, OptionType_VARIANTS);
variant_fn!(option_exercise_type_variants, OptionExerciseType_VARIANTS);
variant_fn!(bond_type_variants, BondType_VARIANTS);
variant_fn!(commodity_type_variants, CommodityType_VARIANTS);
variant_fn!(energy_type_variants, EnergyType_VARIANTS);
variant_fn!(metals_type_variants, MetalsType_VARIANTS);
variant_fn!(agriculture_type_variants, AgricultureType_VARIANTS);
variant_fn!(fund_type_variants, FundType_VARIANTS);
variant_fn!(fund_subtype_variants, FundSubType_VARIANTS);
variant_fn!(mutual_fund_endedness_variants, MutualFundEndedness_VARIANTS);
variant_fn!(future_type_variants, FutureType_VARIANTS);
variant_fn!(future_delivery_type_variants, FutureDeliveryType_VARIANTS);
variant_fn!(order_type_variants, OrderType_VARIANTS);
variant_fn!(side_variants, Side_VARIANTS);
variant_fn!(order_flag_variants, OrderFlag_VARIANTS);
variant_fn!(time_in_force_variants, TimeInForce_VARIANTS);
variant_fn!(trading_type_variants, TradingType_VARIANTS);

#[pyfunction]
fn currency_aliases() -> Vec<(&'static str, &'static str)> {
    Currency_ALIASES.to_vec()
}

#[pymodule]
fn finance_enums(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    macro_rules! reg {
        ($f:ident) => { m.add_function(wrap_pyfunction!($f, m)?)?; };
    }
    reg!(country_code_variants);
    reg!(country_code3_variants);
    reg!(country_names);
    reg!(currency_variants);
    reg!(currency_names);
    reg!(currency_aliases);
    reg!(exchange_code_variants);
    reg!(sector_variants);
    reg!(industry_group_variants);
    reg!(industry_variants);
    reg!(sub_industry_variants);
    reg!(security_type_variants);
    reg!(instrument_type_variants);
    reg!(equity_type_variants);
    reg!(option_type_variants);
    reg!(option_exercise_type_variants);
    reg!(bond_type_variants);
    reg!(commodity_type_variants);
    reg!(energy_type_variants);
    reg!(metals_type_variants);
    reg!(agriculture_type_variants);
    reg!(fund_type_variants);
    reg!(fund_subtype_variants);
    reg!(mutual_fund_endedness_variants);
    reg!(future_type_variants);
    reg!(future_delivery_type_variants);
    reg!(order_type_variants);
    reg!(side_variants);
    reg!(order_flag_variants);
    reg!(time_in_force_variants);
    reg!(trading_type_variants);
    Ok(())
}
