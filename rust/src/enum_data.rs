use std::ffi::{c_char, CString};
use std::sync::OnceLock;

use crate::data::*;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct EnumFamilySpec {
    pub name: &'static str,
    pub variants: &'static [&'static str],
}

impl EnumFamilySpec {
    pub fn variant(&self, variant: &str) -> Option<&'static str> {
        self.variants
            .iter()
            .copied()
            .find(|candidate| *candidate == variant)
    }

    pub fn variant_ordinal(&self, variant: &str) -> Option<usize> {
        self.variants
            .iter()
            .position(|candidate| *candidate == variant)
    }

    pub fn contains_variant(&self, variant: &str) -> bool {
        self.variant(variant).is_some()
    }
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
    /// The highest ordinal value across all families.  Consumers compiled
    /// against an older header can compare their `_COUNT` constants against
    /// this to detect if the library has newer variants they don't know about.
    pub max_ordinal: usize,
}

unsafe impl Sync for EnumDataExportV1 {}
unsafe impl Send for EnumDataExportV1 {}

pub const ENUM_EXPORT_ABI_VERSION: u32 = 1;

/// Semantic version of the *enum data ABI* — the ordinal layout exposed to
/// foreign consumers. This is distinct from the per-export `abi_version` fields
/// (such as [`ENUM_EXPORT_ABI_VERSION`]), which only track the binary layout of
/// each export struct.
///
/// These constants **mirror the package version** in `pyproject.toml` and are
/// kept in sync by `bump-my-version` — do not edit them by hand. The release
/// process follows these ABI-compatibility rules when choosing the bump:
///
/// * **MAJOR** — a backwards-*incompatible* change: reordering, removing, or
///   renaming any existing variant or family, or any change to an export struct
///   layout. Consumers built against a different major MUST NOT use the library.
/// * **MINOR** — a backwards-*compatible* append: new variants added to the end
///   of a family, or entirely new families. Existing ordinals never move, so
///   consumers built against an older minor keep working.
/// * **PATCH** — any other change with no effect on the ordinal layout (docs,
///   metadata, display names, internal refactors).
pub const ENUM_ABI_VERSION_MAJOR: u32 = 0;
/// Minor component of the enum-data ABI version. See [`ENUM_ABI_VERSION_MAJOR`].
pub const ENUM_ABI_VERSION_MINOR: u32 = 6;
/// Patch component of the enum-data ABI version. See [`ENUM_ABI_VERSION_MAJOR`].
pub const ENUM_ABI_VERSION_PATCH: u32 = 0;

/// Returns `true` if a consumer built against `(consumer_major, consumer_minor)`
/// can safely use a library exporting this data.
///
/// Compatible iff the major versions match and the library's minor is at least
/// the consumer's: the library may have *appended* variants the consumer does
/// not know about (safe), but must not have *removed or reordered* any the
/// consumer relies on (that would have bumped the major).
// Guards the case where ENUM_ABI_VERSION_MINOR is 0 (e.g. right after a major
// bump), where `consumer_minor <= 0` would otherwise trip the lint.
#[allow(clippy::absurd_extreme_comparisons)]
pub const fn abi_compatible(consumer_major: u32, consumer_minor: u32) -> bool {
    consumer_major == ENUM_ABI_VERSION_MAJOR && consumer_minor <= ENUM_ABI_VERSION_MINOR
}

/// Like [`abi_compatible`], but panics with a descriptive message when the
/// consumer is incompatible. Intended for Rust consumers that statically embed
/// the version they were built against.
pub fn assert_abi_compatible(consumer_major: u32, consumer_minor: u32) {
    assert!(
        abi_compatible(consumer_major, consumer_minor),
        "finance_enums ABI incompatible: consumer built against {consumer_major}.{consumer_minor}, \
         library exports {ENUM_ABI_VERSION_MAJOR}.{ENUM_ABI_VERSION_MINOR}.{ENUM_ABI_VERSION_PATCH}"
    );
}

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
    "ExecutionType" => ExecutionType_VARIANTS,
    "ExecutionInstruction" => ExecutionInstruction_VARIANTS,
    "ExerciseEventType" => ExerciseEventType_VARIANTS,
    "ExoticOptionFeature" => ExoticOptionFeature_VARIANTS,
    "FailsReason" => FailsReason_VARIANTS,
    "FinancingType" => FinancingType_VARIANTS,
    "FundSubType" => FundSubType_VARIANTS,
    "FundType" => FundType_VARIANTS,
    "FutureAssetClass" => FutureAssetClass_VARIANTS,
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
    "LivestockType" => LivestockType_VARIANTS,
    "MICMarketCategory" => MICMarketCategory_VARIANTS,
    "MarginType" => MarginType_VARIANTS,
    "MarketState" => MarketState_VARIANTS,
    "MarketStatusReason" => MarketStatusReason_VARIANTS,
    "MarketType" => MarketType_VARIANTS,
    "MetalsType" => MetalsType_VARIANTS,
    "MutualFundEndedness" => MutualFundEndedness_VARIANTS,
    "NettingType" => NettingType_VARIANTS,
    "OptionExerciseType" => OptionExerciseType_VARIANTS,
    "OptionType" => OptionType_VARIANTS,
    "OrderCapacity" => OrderCapacity_VARIANTS,
    "OrderFlag" => OrderFlag_VARIANTS,
    "OrderStatus" => OrderStatus_VARIANTS,
    "OrderType" => OrderType_VARIANTS,
    "PayoffStyle" => PayoffStyle_VARIANTS,
    "PositionEffect" => PositionEffect_VARIANTS,
    "PositionType" => PositionType_VARIANTS,
    "PriceKind" => PriceKind_VARIANTS,
    "PriceNotation" => PriceNotation_VARIANTS,
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
    "UnderlyingAssetClass" => UnderlyingAssetClass_VARIANTS,
    "VehicleWrapper" => VehicleWrapper_VARIANTS,
    "VenueRegulatoryFlag" => VenueRegulatoryFlag_VARIANTS,
    "VenueType" => VenueType_VARIANTS,
    // Additional families
    "ExecutionDisposition" => ExecutionDisposition_VARIANTS,
    "FXSubType" => FXSubType_VARIANTS,
    "FXTenor" => FXTenor_VARIANTS,
    "FactorGroup" => FactorGroup_VARIANTS,
    "FamaFrench3Factor" => FamaFrench3Factor_VARIANTS,
    "FamaFrench5Factor" => FamaFrench5Factor_VARIANTS,
    "FutureMonthCode" => FutureMonthCode_VARIANTS,
    "FutureSpreadLegType" => FutureSpreadLegType_VARIANTS,
    "FutureSpreadSubType" => FutureSpreadSubType_VARIANTS,
    "FutureUnderlyingType" => FutureUnderlyingType_VARIANTS,
    "MsciFactorModel" => MsciFactorModel_VARIANTS,
    "OrderSide" => OrderSide_VARIANTS,
    "Symbology" => Symbology_VARIANTS,
    "TickDirection" => TickDirection_VARIANTS,
    "TradingSessionStatus" => TradingSessionStatus_VARIANTS,
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
        max_ordinal: enum_family_specs()
            .iter()
            .map(|f| f.variants.len().saturating_sub(1))
            .max()
            .unwrap_or(0),
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

pub fn enum_family_spec(name: &str) -> Option<&'static EnumFamilySpec> {
    enum_family_specs()
        .iter()
        .find(|family| family.name == name)
}

pub fn enum_variants(name: &str) -> Option<&'static [&'static str]> {
    enum_family_spec(name).map(|family| family.variants)
}

pub fn enum_variant(name: &str, variant: &str) -> Option<&'static str> {
    enum_family_spec(name).and_then(|family| family.variant(variant))
}

pub fn enum_variant_ordinal(name: &str, variant: &str) -> Option<usize> {
    enum_family_spec(name).and_then(|family| family.variant_ordinal(variant))
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn enum_family_lookup_returns_registered_family() {
        let spec = enum_family_spec("MarketType").expect("MarketType should be registered");
        assert_eq!(spec.name, "MarketType");
        assert_eq!(spec.variants, MarketType_VARIANTS);
        assert!(spec.contains_variant("Options"));
        assert!(!spec.contains_variant("Other"));
    }

    #[test]
    fn enum_variant_lookup_uses_names_not_positions() {
        assert_eq!(enum_variant("MarketType", "Options"), Some("Options"));
        assert_eq!(enum_variant("EnergyType", "NaturalGas"), Some("NaturalGas"));
        assert_eq!(enum_variant_ordinal("MarketType", "Options"), Some(6));
        assert_eq!(enum_variant("MarketType", "Other"), None);
        assert_eq!(enum_variant("MissingFamily", "Options"), None);
    }

    #[test]
    fn enum_export_v1_is_consistent() {
        let export = enum_export_v1();
        assert_eq!(export.abi_version, ENUM_EXPORT_ABI_VERSION);
        assert_eq!(export.family_count, ENUM_FAMILY_SPECS.len());
        assert!(export.records_len > 0);
        assert!(export.max_ordinal > 0);
    }

    #[test]
    fn typed_enums_match_string_variants() {
        use crate::data::{CountryCode, SecurityType, Side};

        assert_eq!(Side::Invalid as usize, 0);
        assert_eq!(Side::Buy as usize, 2);
        assert_eq!(Side::Sell as usize, 3);
        assert_eq!(Side::from_ordinal(2), Some(Side::Buy));
        assert_eq!(Side::from_ordinal(99), None);
        assert_eq!(Side::Buy.name(), "Buy");

        assert_eq!(SecurityType::Invalid as usize, 0);
        assert_eq!(SecurityType::Equity as usize, 1);
        assert_eq!(SecurityType::COUNT, 17);

        assert_eq!(CountryCode::US as usize, 233);
        assert_eq!(CountryCode::from_ordinal(233), Some(CountryCode::US));
    }
}
