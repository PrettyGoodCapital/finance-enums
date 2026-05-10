use pyo3::prelude::*;
use pyo3::types::PyCapsule;
use std::ffi::c_void;
use std::ptr::NonNull;

use ::finance_enums::data::*;

#[pyclass(frozen, name = "_ExchangeRecordRaw")]
#[derive(Clone)]
struct PyExchangeRecord {
    #[pyo3(get)]
    mic: String,
    #[pyo3(get)]
    market_name: String,
    #[pyo3(get)]
    legal_entity_name: String,
    #[pyo3(get)]
    operating_mic: String,
    #[pyo3(get)]
    parent_mic: String,
    #[pyo3(get)]
    market_category_code: String,
    #[pyo3(get)]
    acronym: String,
    #[pyo3(get)]
    iso_country_code: String,
    #[pyo3(get)]
    city: String,
    #[pyo3(get)]
    website: String,
    #[pyo3(get)]
    status: String,
    #[pyo3(get)]
    region: String,
    #[pyo3(get)]
    subregion: String,
    #[pyo3(get)]
    is_segment: bool,
    #[pyo3(get)]
    is_official: bool,
}

impl From<&ExchangeRecord> for PyExchangeRecord {
    fn from(record: &ExchangeRecord) -> Self {
        Self {
            mic: record.mic.to_string(),
            market_name: record.market_name.to_string(),
            legal_entity_name: record.legal_entity_name.to_string(),
            operating_mic: record.operating_mic.to_string(),
            parent_mic: record.parent_mic.to_string(),
            market_category_code: record.market_category_code.to_string(),
            acronym: record.acronym.to_string(),
            iso_country_code: record.iso_country_code.to_string(),
            city: record.city.to_string(),
            website: record.website.to_string(),
            status: record.status.to_string(),
            region: record.region.to_string(),
            subregion: record.subregion.to_string(),
            is_segment: record.is_segment,
            is_official: record.is_official,
        }
    }
}

macro_rules! variant_fn {
    ($name:ident, $arr:ident) => {
        #[pyfunction]
        fn $name() -> Vec<&'static str> {
            $arr.to_vec()
        }
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
variant_fn!(venue_type_variants, VenueType_VARIANTS);
variant_fn!(market_type_variants, MarketType_VARIANTS);
variant_fn!(trading_session_variants, TradingSession_VARIANTS);
variant_fn!(market_state_variants, MarketState_VARIANTS);
variant_fn!(auction_type_variants, AuctionType_VARIANTS);
variant_fn!(segment_type_variants, SegmentType_VARIANTS);
variant_fn!(market_status_reason_variants, MarketStatusReason_VARIANTS);
variant_fn!(identifier_type_variants, IdentifierType_VARIANTS);
variant_fn!(ticker_namespace_variants, TickerNamespace_VARIANTS);
variant_fn!(price_notation_variants, PriceNotation_VARIANTS);
variant_fn!(quantity_unit_variants, QuantityUnit_VARIANTS);
variant_fn!(currency_role_variants, CurrencyRole_VARIANTS);
variant_fn!(mic_market_category_variants, MICMarketCategory_VARIANTS);
variant_fn!(venue_regulatory_flag_variants, VenueRegulatoryFlag_VARIANTS);
variant_fn!(contract_style_variants, ContractStyle_VARIANTS);
variant_fn!(contract_unit_variants, ContractUnit_VARIANTS);
variant_fn!(delivery_type_variants, DeliveryType_VARIANTS);
variant_fn!(coupon_type_variants, CouponType_VARIANTS);
variant_fn!(coupon_frequency_variants, CouponFrequency_VARIANTS);
variant_fn!(day_count_convention_variants, DayCountConvention_VARIANTS);
variant_fn!(amortization_type_variants, AmortizationType_VARIANTS);
variant_fn!(seniority_variants, Seniority_VARIANTS);
variant_fn!(collateral_type_variants, CollateralType_VARIANTS);
variant_fn!(margin_type_variants, MarginType_VARIANTS);
variant_fn!(borrow_type_variants, BorrowType_VARIANTS);
variant_fn!(repo_type_variants, RepoType_VARIANTS);
variant_fn!(account_type_variants, AccountType_VARIANTS);
variant_fn!(book_type_variants, BookType_VARIANTS);
variant_fn!(position_type_variants, PositionType_VARIANTS);
variant_fn!(inventory_type_variants, InventoryType_VARIANTS);
variant_fn!(strategy_type_variants, StrategyType_VARIANTS);
variant_fn!(netting_type_variants, NettingType_VARIANTS);
variant_fn!(vehicle_wrapper_variants, VehicleWrapper_VARIANTS);
variant_fn!(distribution_policy_variants, DistributionPolicy_VARIANTS);
variant_fn!(share_class_hedging_variants, ShareClassHedging_VARIANTS);
variant_fn!(liquidity_term_variants, LiquidityTerm_VARIANTS);
variant_fn!(redemption_frequency_variants, RedemptionFrequency_VARIANTS);
variant_fn!(financing_type_variants, FinancingType_VARIANTS);
variant_fn!(mutual_fund_endedness_variants, MutualFundEndedness_VARIANTS);
variant_fn!(future_type_variants, FutureType_VARIANTS);
variant_fn!(future_delivery_type_variants, FutureDeliveryType_VARIANTS);
variant_fn!(swap_leg_type_variants, SwapLegType_VARIANTS);
variant_fn!(rate_index_variants, RateIndex_VARIANTS);
variant_fn!(reset_frequency_variants, ResetFrequency_VARIANTS);
variant_fn!(compounding_method_variants, CompoundingMethod_VARIANTS);
variant_fn!(stub_type_variants, StubType_VARIANTS);
variant_fn!(barrier_type_variants, BarrierType_VARIANTS);
variant_fn!(averaging_method_variants, AveragingMethod_VARIANTS);
variant_fn!(exotic_option_feature_variants, ExoticOptionFeature_VARIANTS);
variant_fn!(corporate_action_type_variants, CorporateActionType_VARIANTS);
variant_fn!(listing_status_variants, ListingStatus_VARIANTS);
variant_fn!(security_status_variants, SecurityStatus_VARIANTS);
variant_fn!(exercise_event_type_variants, ExerciseEventType_VARIANTS);
variant_fn!(tender_offer_type_variants, TenderOfferType_VARIANTS);
variant_fn!(delisting_reason_variants, DelistingReason_VARIANTS);
variant_fn!(leg_role_variants, LegRole_VARIANTS);
variant_fn!(payoff_style_variants, PayoffStyle_VARIANTS);
variant_fn!(perpetual_future_type_variants, PerpetualFutureType_VARIANTS);
variant_fn!(settlement_type_variants, SettlementType_VARIANTS);
variant_fn!(swap_type_variants, SwapType_VARIANTS);
variant_fn!(order_status_variants, OrderStatus_VARIANTS);
variant_fn!(exec_type_variants, ExecType_VARIANTS);
variant_fn!(execution_instruction_variants, ExecutionInstruction_VARIANTS);
variant_fn!(liquidity_flag_variants, LiquidityFlag_VARIANTS);
variant_fn!(position_effect_variants, PositionEffect_VARIANTS);
variant_fn!(open_close_variants, OpenClose_VARIANTS);
variant_fn!(order_capacity_variants, OrderCapacity_VARIANTS);
variant_fn!(short_sale_restriction_variants, ShortSaleRestriction_VARIANTS);
variant_fn!(order_type_variants, OrderType_VARIANTS);
variant_fn!(quote_condition_variants, QuoteCondition_VARIANTS);
variant_fn!(trade_condition_variants, TradeCondition_VARIANTS);
variant_fn!(aggressor_side_variants, AggressorSide_VARIANTS);
variant_fn!(cross_type_variants, CrossType_VARIANTS);
variant_fn!(price_type_variants, PriceType_VARIANTS);
variant_fn!(side_variants, Side_VARIANTS);
variant_fn!(order_flag_variants, OrderFlag_VARIANTS);
variant_fn!(time_in_force_variants, TimeInForce_VARIANTS);
variant_fn!(trading_type_variants, TradingType_VARIANTS);
variant_fn!(underlying_asset_class_variants, UnderlyingAssetClass_VARIANTS);

#[pyfunction]
fn currency_aliases() -> Vec<(&'static str, &'static str)> {
    Currency_ALIASES.to_vec()
}

#[pyfunction]
fn currency_records() -> Vec<(&'static str, &'static str, bool)> {
    CURRENCY_RECORDS
        .iter()
        .map(|record| (record.code, record.display_name, record.is_iso4217))
        .collect()
}

#[pyfunction]
fn currency_alias_records() -> Vec<(&'static str, &'static str)> {
    CURRENCY_ALIAS_RECORDS
        .iter()
        .map(|record| (record.alias, record.canonical_code))
        .collect()
}

#[pyfunction]
fn exchange_records_raw() -> Vec<Vec<&'static str>> {
    exchange_records()
        .iter()
        .map(|record| {
            vec![
                record.mic,
                record.market_name,
                record.legal_entity_name,
                record.operating_mic,
                record.parent_mic,
                record.market_category_code,
                record.acronym,
                record.iso_country_code,
                record.city,
                record.website,
                record.status,
                record.region,
                record.subregion,
                if record.is_segment { "1" } else { "0" },
                if record.is_official { "1" } else { "0" },
            ]
        })
        .collect()
}

#[pyfunction]
fn exchange_records_typed() -> Vec<PyExchangeRecord> {
    exchange_records().iter().map(PyExchangeRecord::from).collect()
}

#[pyfunction]
fn exchange_record_typed(mic: &str) -> Option<PyExchangeRecord> {
    exchange_record(mic).map(PyExchangeRecord::from)
}

#[pyfunction]
fn currency_export_capsule(py: Python<'_>) -> PyResult<Bound<'_, PyCapsule>> {
    let pointer = NonNull::from(&CURRENCY_EXPORT_V1).cast::<c_void>();

    unsafe { PyCapsule::new_with_pointer(py, pointer, c"finance_enums.currency_export_v1") }
}

#[no_mangle]
pub extern "C" fn finance_enums_currency_export_v1() -> *const CurrencyDataExportV1 {
    &CURRENCY_EXPORT_V1
}

#[pymodule]
fn finance_enums(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    macro_rules! reg {
        ($f:ident) => {
            m.add_function(wrap_pyfunction!($f, m)?)?;
        };
    }
    reg!(country_code_variants);
    reg!(country_code3_variants);
    reg!(country_names);
    reg!(currency_variants);
    reg!(currency_names);
    reg!(currency_aliases);
    reg!(currency_records);
    reg!(currency_alias_records);
    reg!(currency_export_capsule);
    reg!(exchange_records_raw);
    reg!(exchange_records_typed);
    reg!(exchange_record_typed);
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
    reg!(venue_type_variants);
    reg!(market_type_variants);
    reg!(trading_session_variants);
    reg!(market_state_variants);
    reg!(auction_type_variants);
    reg!(segment_type_variants);
    reg!(market_status_reason_variants);
    reg!(identifier_type_variants);
    reg!(ticker_namespace_variants);
    reg!(price_notation_variants);
    reg!(quantity_unit_variants);
    reg!(currency_role_variants);
    reg!(mic_market_category_variants);
    reg!(venue_regulatory_flag_variants);
    reg!(contract_style_variants);
    reg!(contract_unit_variants);
    reg!(delivery_type_variants);
    reg!(coupon_type_variants);
    reg!(coupon_frequency_variants);
    reg!(day_count_convention_variants);
    reg!(amortization_type_variants);
    reg!(seniority_variants);
    reg!(collateral_type_variants);
    reg!(margin_type_variants);
    reg!(borrow_type_variants);
    reg!(repo_type_variants);
    reg!(account_type_variants);
    reg!(book_type_variants);
    reg!(position_type_variants);
    reg!(inventory_type_variants);
    reg!(strategy_type_variants);
    reg!(netting_type_variants);
    reg!(vehicle_wrapper_variants);
    reg!(distribution_policy_variants);
    reg!(share_class_hedging_variants);
    reg!(liquidity_term_variants);
    reg!(redemption_frequency_variants);
    reg!(financing_type_variants);
    reg!(mutual_fund_endedness_variants);
    reg!(future_type_variants);
    reg!(future_delivery_type_variants);
    reg!(swap_leg_type_variants);
    reg!(rate_index_variants);
    reg!(reset_frequency_variants);
    reg!(compounding_method_variants);
    reg!(stub_type_variants);
    reg!(barrier_type_variants);
    reg!(averaging_method_variants);
    reg!(exotic_option_feature_variants);
    reg!(corporate_action_type_variants);
    reg!(listing_status_variants);
    reg!(security_status_variants);
    reg!(exercise_event_type_variants);
    reg!(tender_offer_type_variants);
    reg!(delisting_reason_variants);
    reg!(leg_role_variants);
    reg!(payoff_style_variants);
    reg!(perpetual_future_type_variants);
    reg!(settlement_type_variants);
    reg!(swap_type_variants);
    reg!(order_status_variants);
    reg!(exec_type_variants);
    reg!(execution_instruction_variants);
    reg!(liquidity_flag_variants);
    reg!(position_effect_variants);
    reg!(open_close_variants);
    reg!(order_capacity_variants);
    reg!(short_sale_restriction_variants);
    reg!(order_type_variants);
    reg!(quote_condition_variants);
    reg!(trade_condition_variants);
    reg!(aggressor_side_variants);
    reg!(cross_type_variants);
    reg!(price_type_variants);
    reg!(side_variants);
    reg!(order_flag_variants);
    reg!(time_in_force_variants);
    reg!(trading_type_variants);
    reg!(underlying_asset_class_variants);
    m.add_class::<PyExchangeRecord>()?;
    Ok(())
}
