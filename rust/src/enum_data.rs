use std::ffi::{c_char, CString};
use std::sync::OnceLock;

use crate::data::*;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct EnumFamilySpec {
    pub name: &'static str,
    pub variants: &'static [&'static str],
}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct EnumVariantRecordRaw {
    pub enum_name: *const c_char,
    pub variant: *const c_char,
    pub ordinal: usize,
}

unsafe impl Sync for EnumVariantRecordRaw {}
unsafe impl Send for EnumVariantRecordRaw {}

#[repr(C)]
#[derive(Clone, Copy, Debug)]
pub struct EnumDataExportV1 {
    pub abi_version: u32,
    pub export_struct_size: usize,
    pub enum_variant_record_size: usize,
    pub records: *const EnumVariantRecordRaw,
    pub records_len: usize,
    pub family_count: usize,
}

unsafe impl Sync for EnumDataExportV1 {}
unsafe impl Send for EnumDataExportV1 {}

pub const ENUM_EXPORT_ABI_VERSION: u32 = 1;

macro_rules! enum_family_specs {
    ($($name:literal => $variants:ident),* $(,)?) => {
        pub static ENUM_FAMILY_SPECS: &[EnumFamilySpec] = &[
            $(EnumFamilySpec { name: $name, variants: $variants },)*
        ];
    };
}

enum_family_specs!(
    "AccountType" => AccountType_VARIANTS,
    "AggressorSide" => AggressorSide_VARIANTS,
    "AgricultureType" => AgricultureType_VARIANTS,
    "AllocationMethod" => AllocationMethod_VARIANTS,
    "AmortizationType" => AmortizationType_VARIANTS,
    "AuctionType" => AuctionType_VARIANTS,
    "AveragingMethod" => AveragingMethod_VARIANTS,
    "BarrierType" => BarrierType_VARIANTS,
    "BenchmarkType" => BenchmarkType_VARIANTS,
    "BondType" => BondType_VARIANTS,
    "BookType" => BookType_VARIANTS,
    "BorrowType" => BorrowType_VARIANTS,
    "CalculationAgentType" => CalculationAgentType_VARIANTS,
    "ClearingHouse" => ClearingHouse_VARIANTS,
    "ClearingModel" => ClearingModel_VARIANTS,
    "CollateralType" => CollateralType_VARIANTS,
    "CommodityType" => CommodityType_VARIANTS,
    "CompoundingMethod" => CompoundingMethod_VARIANTS,
    "ContractStyle" => ContractStyle_VARIANTS,
    "ContractUnit" => ContractUnit_VARIANTS,
    "CorporateActionAdjustmentType" => CorporateActionAdjustmentType_VARIANTS,
    "CorporateActionType" => CorporateActionType_VARIANTS,
    "CouponFrequency" => CouponFrequency_VARIANTS,
    "CouponType" => CouponType_VARIANTS,
    "CountryCode" => CountryCode_VARIANTS,
    "CountryCode3" => CountryCode3_VARIANTS,
    "CrossType" => CrossType_VARIANTS,
    "Currency" => Currency_VARIANTS,
    "CurrencyRole" => CurrencyRole_VARIANTS,
    "DayCountConvention" => DayCountConvention_VARIANTS,
    "DelistingReason" => DelistingReason_VARIANTS,
    "DeliveryType" => DeliveryType_VARIANTS,
    "DistributionPolicy" => DistributionPolicy_VARIANTS,
    "EnergyType" => EnergyType_VARIANTS,
    "EquityType" => EquityType_VARIANTS,
    "ExchangeCode" => ExchangeCode_VARIANTS,
    "ExecType" => ExecType_VARIANTS,
    "ExecutionInstruction" => ExecutionInstruction_VARIANTS,
    "ExerciseEventType" => ExerciseEventType_VARIANTS,
    "ExoticOptionFeature" => ExoticOptionFeature_VARIANTS,
    "FailsReason" => FailsReason_VARIANTS,
    "FinancingType" => FinancingType_VARIANTS,
    "FundSubType" => FundSubType_VARIANTS,
    "FundType" => FundType_VARIANTS,
    "FutureDeliveryType" => FutureDeliveryType_VARIANTS,
    "FutureType" => FutureType_VARIANTS,
    "GiveUpType" => GiveUpType_VARIANTS,
    "IdentifierType" => IdentifierType_VARIANTS,
    "IndexWeightingMethod" => IndexWeightingMethod_VARIANTS,
    "Industry" => Industry_VARIANTS,
    "IndustryGroup" => IndustryGroup_VARIANTS,
    "InstrumentType" => InstrumentType_VARIANTS,
    "InventoryType" => InventoryType_VARIANTS,
    "LegRole" => LegRole_VARIANTS,
    "LiquidityFlag" => LiquidityFlag_VARIANTS,
    "LiquidityTerm" => LiquidityTerm_VARIANTS,
    "ListingStatus" => ListingStatus_VARIANTS,
    "MICMarketCategory" => MICMarketCategory_VARIANTS,
    "MarginType" => MarginType_VARIANTS,
    "MarketState" => MarketState_VARIANTS,
    "MarketStatusReason" => MarketStatusReason_VARIANTS,
    "MarketType" => MarketType_VARIANTS,
    "MetalsType" => MetalsType_VARIANTS,
    "MutualFundEndedness" => MutualFundEndedness_VARIANTS,
    "NettingType" => NettingType_VARIANTS,
    "OpenClose" => OpenClose_VARIANTS,
    "OptionExerciseType" => OptionExerciseType_VARIANTS,
    "OptionType" => OptionType_VARIANTS,
    "OrderCapacity" => OrderCapacity_VARIANTS,
    "OrderFlag" => OrderFlag_VARIANTS,
    "OrderStatus" => OrderStatus_VARIANTS,
    "OrderType" => OrderType_VARIANTS,
    "PayoffStyle" => PayoffStyle_VARIANTS,
    "PerpetualFutureType" => PerpetualFutureType_VARIANTS,
    "PositionEffect" => PositionEffect_VARIANTS,
    "PositionType" => PositionType_VARIANTS,
    "PriceNotation" => PriceNotation_VARIANTS,
    "PriceType" => PriceType_VARIANTS,
    "QuantityUnit" => QuantityUnit_VARIANTS,
    "QuoteCondition" => QuoteCondition_VARIANTS,
    "RateIndex" => RateIndex_VARIANTS,
    "RebalanceFrequency" => RebalanceFrequency_VARIANTS,
    "RedemptionFrequency" => RedemptionFrequency_VARIANTS,
    "RepoType" => RepoType_VARIANTS,
    "ResetFrequency" => ResetFrequency_VARIANTS,
    "Sector" => Sector_VARIANTS,
    "SecurityStatus" => SecurityStatus_VARIANTS,
    "SecurityType" => SecurityType_VARIANTS,
    "SegmentType" => SegmentType_VARIANTS,
    "Seniority" => Seniority_VARIANTS,
    "SettlementStatus" => SettlementStatus_VARIANTS,
    "SettlementType" => SettlementType_VARIANTS,
    "ShareClassHedging" => ShareClassHedging_VARIANTS,
    "ShortSaleRestriction" => ShortSaleRestriction_VARIANTS,
    "Side" => Side_VARIANTS,
    "StrategyType" => StrategyType_VARIANTS,
    "StubType" => StubType_VARIANTS,
    "SubIndustry" => SubIndustry_VARIANTS,
    "SwapLegType" => SwapLegType_VARIANTS,
    "SwapType" => SwapType_VARIANTS,
    "TenderOfferType" => TenderOfferType_VARIANTS,
    "TickerNamespace" => TickerNamespace_VARIANTS,
    "TimeInForce" => TimeInForce_VARIANTS,
    "TradeCondition" => TradeCondition_VARIANTS,
    "TradingSession" => TradingSession_VARIANTS,
    "TradingType" => TradingType_VARIANTS,
    "UnderlyingAssetClass" => UnderlyingAssetClass_VARIANTS,
    "VehicleWrapper" => VehicleWrapper_VARIANTS,
    "VenueRegulatoryFlag" => VenueRegulatoryFlag_VARIANTS,
    "VenueType" => VenueType_VARIANTS,
);

struct EnumDataExportBacking {
    _records: Box<[EnumVariantRecordRaw]>,
    export: EnumDataExportV1,
}

unsafe impl Sync for EnumDataExportBacking {}
unsafe impl Send for EnumDataExportBacking {}

fn leak_c_string(value: &'static str) -> *const c_char {
    CString::new(value)
        .expect("enum value contained interior NUL")
        .into_raw()
        .cast_const()
}

fn build_enum_export_v1() -> EnumDataExportBacking {
    let records = enum_family_specs()
        .iter()
        .flat_map(|family| {
            family
                .variants
                .iter()
                .enumerate()
                .map(move |(ordinal, variant)| EnumVariantRecordRaw {
                    enum_name: leak_c_string(family.name),
                    variant: leak_c_string(variant),
                    ordinal,
                })
        })
        .collect::<Vec<_>>()
        .into_boxed_slice();

    let export = EnumDataExportV1 {
        abi_version: ENUM_EXPORT_ABI_VERSION,
        export_struct_size: std::mem::size_of::<EnumDataExportV1>(),
        enum_variant_record_size: std::mem::size_of::<EnumVariantRecordRaw>(),
        records: records.as_ptr(),
        records_len: records.len(),
        family_count: enum_family_specs().len(),
    };

    EnumDataExportBacking {
        _records: records,
        export,
    }
}

static ENUM_EXPORT_V1_INNER: OnceLock<EnumDataExportBacking> = OnceLock::new();

pub fn enum_family_specs() -> &'static [EnumFamilySpec] {
    ENUM_FAMILY_SPECS
}

pub fn enum_variant_records() -> Vec<(&'static str, &'static str, usize)> {
    enum_family_specs()
        .iter()
        .flat_map(|family| {
            family
                .variants
                .iter()
                .enumerate()
                .map(move |(ordinal, variant)| (family.name, *variant, ordinal))
        })
        .collect()
}

pub fn enum_export_v1() -> &'static EnumDataExportV1 {
    &ENUM_EXPORT_V1_INNER
        .get_or_init(build_enum_export_v1)
        .export
}
