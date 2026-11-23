use abi_safe_enum::AbiSafeEnum;

use crate::data::*;

/// One enum family: its variant names and the ordinal of each.
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub struct EnumFamilySpec {
    pub name: &'static str,
    /// Variant names in declaration order.
    pub variants: &'static [&'static str],
    /// Ordinal of each variant, parallel to `variants`. `None` for the
    /// table-backed families (`Currency`, `ExchangeCode`), whose ordinal is
    /// their position.
    pub ordinals: Option<&'static [u32]>,
    /// Size in bytes of the family's ordinal representation.
    pub ordinal_size: usize,
}

/// Smallest of 1, 2, or 4 bytes that holds ordinals `0..count`.
const fn ordinal_size_for(count: usize) -> usize {
    if count <= 1 << 8 {
        1
    } else if count <= 1 << 16 {
        2
    } else {
        4
    }
}

impl EnumFamilySpec {
    /// The spec of an `#[abi_safe_enum]` enum.
    pub const fn of<E: AbiSafeEnum>() -> Self {
        Self {
            name: E::NAME,
            variants: E::VARIANTS,
            ordinals: Some(E::ORDINALS),
            ordinal_size: E::ORDINAL_SIZE,
        }
    }

    /// The spec of a family backed by a name table, with positional ordinals.
    pub const fn table(name: &'static str, variants: &'static [&'static str]) -> Self {
        Self {
            name,
            variants,
            ordinals: None,
            ordinal_size: ordinal_size_for(variants.len()),
        }
    }

    /// Ordinal of the variant at `index` in declaration order.
    pub fn ordinal_at(&self, index: usize) -> u32 {
        match self.ordinals {
            Some(ordinals) => ordinals[index],
            None => index as u32,
        }
    }

    /// `(variant, ordinal)` pairs in declaration order.
    pub fn iter(&self) -> impl Iterator<Item = (&'static str, u32)> + '_ {
        self.variants
            .iter()
            .enumerate()
            .map(|(index, variant)| (*variant, self.ordinal_at(index)))
    }

    pub fn variant(&self, variant: &str) -> Option<&'static str> {
        self.variants
            .iter()
            .copied()
            .find(|candidate| *candidate == variant)
    }

    pub fn contains_variant(&self, variant: &str) -> bool {
        self.variant(variant).is_some()
    }

    /// Ordinal of the variant named `variant`.
    pub fn variant_ordinal(&self, variant: &str) -> Option<u32> {
        self.variants
            .iter()
            .position(|candidate| *candidate == variant)
            .map(|index| self.ordinal_at(index))
    }

    /// Declaration-order index of the variant with `ordinal`.
    pub fn index_of_ordinal(&self, ordinal: u32) -> Option<usize> {
        match self.ordinals {
            Some(ordinals) => ordinals.iter().position(|candidate| *candidate == ordinal),
            None => ((ordinal as usize) < self.variants.len()).then_some(ordinal as usize),
        }
    }

    /// Name of the variant with `ordinal`.
    pub fn variant_name(&self, ordinal: u32) -> Option<&'static str> {
        self.index_of_ordinal(ordinal)
            .map(|index| self.variants[index])
    }

    pub fn contains_ordinal(&self, ordinal: u32) -> bool {
        self.index_of_ordinal(ordinal).is_some()
    }

    pub fn max_ordinal(&self) -> u32 {
        match self.ordinals {
            Some(ordinals) => ordinals.iter().copied().max().unwrap_or(0),
            None => self.variants.len().saturating_sub(1) as u32,
        }
    }
}

/// Semantic version of the *enum data ABI* — the ordinal layout exposed to
/// foreign consumers. This is distinct from the per-export `abi_version` fields
/// in the C ABI crate, which only track the binary layout of each export struct.
///
/// These constants **mirror the package version** in `pyproject.toml` and are
/// kept in sync by `bump-my-version` — do not edit them by hand.
///
/// While the major version is zero, each minor version is an independent beta
/// ABI and consumers must match it exactly. After 1.0, the release process
/// follows these ABI-compatibility rules when choosing the bump:
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
pub const ENUM_ABI_VERSION_MINOR: u32 = 9;
/// Patch component of the enum-data ABI version. See [`ENUM_ABI_VERSION_MAJOR`].
pub const ENUM_ABI_VERSION_PATCH: u32 = 1;

/// Returns `true` if a consumer built against `(consumer_major, consumer_minor)`
/// can safely use a library exporting this data.
///
/// During the 0.x beta, major and minor must both match. Starting with 1.0,
/// compatible libraries have the same major and a minor at least as new as the
/// consumer's.
pub const fn abi_compatible(consumer_major: u32, consumer_minor: u32) -> bool {
    consumer_major == ENUM_ABI_VERSION_MAJOR
        && if ENUM_ABI_VERSION_MAJOR == 0 {
            consumer_minor == ENUM_ABI_VERSION_MINOR
        } else {
            consumer_minor <= ENUM_ABI_VERSION_MINOR
        }
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

/// Every enum family, in C ABI export order.
pub static ENUM_FAMILY_SPECS: &[EnumFamilySpec] = &[
    EnumFamilySpec::of::<AccountType>(),
    EnumFamilySpec::of::<AggressorSide>(),
    EnumFamilySpec::of::<AgricultureType>(),
    EnumFamilySpec::of::<AllocationMethod>(),
    EnumFamilySpec::of::<AmortizationType>(),
    EnumFamilySpec::of::<AssetBackedCollateralType>(),
    EnumFamilySpec::of::<AuctionType>(),
    EnumFamilySpec::of::<AveragingMethod>(),
    EnumFamilySpec::of::<BarrierType>(),
    EnumFamilySpec::of::<BenchmarkType>(),
    EnumFamilySpec::of::<BondType>(),
    EnumFamilySpec::of::<BookType>(),
    EnumFamilySpec::of::<BorrowType>(),
    EnumFamilySpec::of::<BusinessDayConvention>(),
    EnumFamilySpec::of::<CalculationAgentType>(),
    EnumFamilySpec::of::<ClearingHouse>(),
    EnumFamilySpec::of::<ClearingModel>(),
    EnumFamilySpec::of::<CollateralType>(),
    EnumFamilySpec::of::<CommodityType>(),
    EnumFamilySpec::of::<CompoundingMethod>(),
    EnumFamilySpec::of::<ContractStyle>(),
    EnumFamilySpec::of::<ContractUnit>(),
    EnumFamilySpec::of::<CorporateActionAdjustmentType>(),
    EnumFamilySpec::of::<CorporateActionType>(),
    EnumFamilySpec::of::<CountryCodeAlpha2>(),
    EnumFamilySpec::of::<CountryCodeAlpha3>(),
    EnumFamilySpec::of::<CouponType>(),
    EnumFamilySpec::of::<CreditDefaultSwapTransactionType>(),
    EnumFamilySpec::of::<CreditEventType>(),
    EnumFamilySpec::of::<CreditQuality>(),
    EnumFamilySpec::of::<CreditRatingAgency>(),
    EnumFamilySpec::of::<CreditRatingOutlook>(),
    EnumFamilySpec::of::<CrossType>(),
    EnumFamilySpec::table("Currency", Currency_VARIANTS),
    EnumFamilySpec::of::<CurrencyRole>(),
    EnumFamilySpec::of::<DayCountConvention>(),
    EnumFamilySpec::of::<DebtGuaranteeType>(),
    EnumFamilySpec::of::<DelistingReason>(),
    EnumFamilySpec::of::<DeliveryType>(),
    EnumFamilySpec::of::<DistributionPolicy>(),
    EnumFamilySpec::of::<DurationType>(),
    EnumFamilySpec::of::<EnergyType>(),
    EnumFamilySpec::of::<EquityType>(),
    EnumFamilySpec::table("ExchangeCode", ExchangeCode_VARIANTS),
    EnumFamilySpec::of::<ExecutionInstruction>(),
    EnumFamilySpec::of::<ExecutionType>(),
    EnumFamilySpec::of::<ExerciseEventType>(),
    EnumFamilySpec::of::<ExoticOptionFeature>(),
    EnumFamilySpec::of::<FactorGroup>(),
    EnumFamilySpec::of::<FamaFrenchFactor>(),
    EnumFamilySpec::of::<FinancingType>(),
    EnumFamilySpec::of::<ForeignExchangeAtTheMoneyConvention>(),
    EnumFamilySpec::of::<ForeignExchangeBenchmark>(),
    EnumFamilySpec::of::<ForeignExchangeDeltaConvention>(),
    EnumFamilySpec::of::<ForeignExchangeProductType>(),
    EnumFamilySpec::of::<ForeignExchangeQuoteBasis>(),
    EnumFamilySpec::of::<ForeignExchangeTenor>(),
    EnumFamilySpec::of::<ForeignExchangeVolatilityQuoteType>(),
    EnumFamilySpec::of::<FundSubType>(),
    EnumFamilySpec::of::<FundType>(),
    EnumFamilySpec::of::<FutureAssetClass>(),
    EnumFamilySpec::of::<FutureMonthCode>(),
    EnumFamilySpec::of::<FutureSpreadLegType>(),
    EnumFamilySpec::of::<FutureSpreadSubType>(),
    EnumFamilySpec::of::<GiveUpType>(),
    EnumFamilySpec::of::<IdentifierType>(),
    EnumFamilySpec::of::<IndexWeightingMethod>(),
    EnumFamilySpec::of::<Industry>(),
    EnumFamilySpec::of::<IndustryGroup>(),
    EnumFamilySpec::of::<InstrumentType>(),
    EnumFamilySpec::of::<InterestRateProductType>(),
    EnumFamilySpec::of::<InterestRateSwapType>(),
    EnumFamilySpec::of::<InventoryType>(),
    EnumFamilySpec::of::<IssuerType>(),
    EnumFamilySpec::of::<LegRole>(),
    EnumFamilySpec::of::<LiquidityFlag>(),
    EnumFamilySpec::of::<ListingStatus>(),
    EnumFamilySpec::of::<LivestockType>(),
    EnumFamilySpec::of::<MarginType>(),
    EnumFamilySpec::of::<MarketCategory>(),
    EnumFamilySpec::of::<MarketState>(),
    EnumFamilySpec::of::<MarketStatusReason>(),
    EnumFamilySpec::of::<MarketType>(),
    EnumFamilySpec::of::<MetalType>(),
    EnumFamilySpec::of::<MoneyMarketInstrumentType>(),
    EnumFamilySpec::of::<MutualFundEndedness>(),
    EnumFamilySpec::of::<NettingType>(),
    EnumFamilySpec::of::<ObligationCategory>(),
    EnumFamilySpec::of::<ObligationCharacteristic>(),
    EnumFamilySpec::of::<OptionExerciseType>(),
    EnumFamilySpec::of::<OptionPremiumQuoteBasis>(),
    EnumFamilySpec::of::<OptionStrikeQuoteBasis>(),
    EnumFamilySpec::of::<OptionType>(),
    EnumFamilySpec::of::<OrderCapacity>(),
    EnumFamilySpec::of::<OrderSide>(),
    EnumFamilySpec::of::<OrderStatus>(),
    EnumFamilySpec::of::<OrderType>(),
    EnumFamilySpec::of::<OvernightAccrualMethod>(),
    EnumFamilySpec::of::<PayoffStyle>(),
    EnumFamilySpec::of::<PayoutTiming>(),
    EnumFamilySpec::of::<PeriodTiming>(),
    EnumFamilySpec::of::<PeriodUnit>(),
    EnumFamilySpec::of::<PositionEffect>(),
    EnumFamilySpec::of::<PositionType>(),
    EnumFamilySpec::of::<PriceIndexCalculationMethod>(),
    EnumFamilySpec::of::<PriceKind>(),
    EnumFamilySpec::of::<PriceNotation>(),
    EnumFamilySpec::of::<QuantityUnit>(),
    EnumFamilySpec::of::<QuoteCondition>(),
    EnumFamilySpec::of::<RateIndex>(),
    EnumFamilySpec::of::<RedemptionFeature>(),
    EnumFamilySpec::of::<RepoType>(),
    EnumFamilySpec::of::<RestructuringClause>(),
    EnumFamilySpec::of::<RollConvention>(),
    EnumFamilySpec::of::<ScheduleFrequency>(),
    EnumFamilySpec::of::<Sector>(),
    EnumFamilySpec::of::<SecurityForm>(),
    EnumFamilySpec::of::<SecurityStatus>(),
    EnumFamilySpec::of::<SecurityType>(),
    EnumFamilySpec::of::<SegmentType>(),
    EnumFamilySpec::of::<Seniority>(),
    EnumFamilySpec::of::<SettlementFailReason>(),
    EnumFamilySpec::of::<SettlementStatus>(),
    EnumFamilySpec::of::<SettlementType>(),
    EnumFamilySpec::of::<ShareClassHedging>(),
    EnumFamilySpec::of::<ShortSaleRestriction>(),
    EnumFamilySpec::of::<Side>(),
    EnumFamilySpec::of::<StrategyType>(),
    EnumFamilySpec::of::<StubType>(),
    EnumFamilySpec::of::<StyleFactor>(),
    EnumFamilySpec::of::<SubIndustry>(),
    EnumFamilySpec::of::<SwapLegType>(),
    EnumFamilySpec::of::<SwapType>(),
    EnumFamilySpec::of::<SwaptionCashSettlementMethod>(),
    EnumFamilySpec::of::<Symbology>(),
    EnumFamilySpec::of::<TenderOfferType>(),
    EnumFamilySpec::of::<TickDirection>(),
    EnumFamilySpec::of::<TickerNamespace>(),
    EnumFamilySpec::of::<TimeInForce>(),
    EnumFamilySpec::of::<TouchType>(),
    EnumFamilySpec::of::<TradeCondition>(),
    EnumFamilySpec::of::<TradingPhase>(),
    EnumFamilySpec::of::<TradingSession>(),
    EnumFamilySpec::of::<UnderlyingAssetClass>(),
    EnumFamilySpec::of::<VenueRegulatoryFlag>(),
    EnumFamilySpec::of::<VenueType>(),
    EnumFamilySpec::of::<YieldType>(),
];

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

pub fn enum_variant_ordinal(name: &str, variant: &str) -> Option<u32> {
    enum_family_spec(name).and_then(|family| family.variant_ordinal(variant))
}

/// `(family, variant, ordinal)` for every variant of every family.
pub fn enum_variant_records() -> Vec<(&'static str, &'static str, u32)> {
    enum_family_specs()
        .iter()
        .flat_map(|family| {
            family
                .iter()
                .map(move |(variant, ordinal)| (family.name, variant, ordinal))
        })
        .collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn enum_family_lookup_returns_registered_family() {
        let spec = enum_family_spec("MarketType").expect("MarketType should be registered");
        assert_eq!(spec.name, "MarketType");
        assert_eq!(spec.variants, MarketType::VARIANTS);
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
    fn typed_enums_match_string_variants() {
        use crate::data::{CountryCodeAlpha2, SecurityType, Side};

        assert_eq!(Side::Invalid as usize, 0);
        assert_eq!(Side::Buy as usize, 1);
        assert_eq!(Side::Sell as usize, 2);
        assert_eq!(Side::from_ordinal(1), Some(Side::Buy));
        assert_eq!(Side::from_ordinal(99), None);
        assert_eq!(Side::Buy.name(), "Buy");

        assert_eq!(SecurityType::Invalid as usize, 0);
        assert_eq!(SecurityType::Equity as usize, 1);
        assert_eq!(SecurityType::COUNT, 17);

        assert_eq!(CountryCodeAlpha2::US as usize, 233);
        assert_eq!(
            CountryCodeAlpha2::from_ordinal(233),
            Some(CountryCodeAlpha2::US)
        );
    }

    #[test]
    fn specs_carry_each_enums_ordinals_and_width() {
        let side = enum_family_spec("Side").unwrap();
        assert_eq!(side.ordinals, Some(Side::ORDINALS));
        assert_eq!(side.ordinal_size, 1);
        assert_eq!(
            enum_family_spec("CountryCodeAlpha2").unwrap().ordinal_size,
            2
        );
        assert_eq!(enum_family_spec("Currency").unwrap().ordinal_size, 1);
        assert_eq!(enum_family_spec("ExchangeCode").unwrap().ordinal_size, 2);
        for spec in enum_family_specs() {
            assert_eq!(
                spec.ordinal_at(0),
                0,
                "{} must start with its sentinel",
                spec.name
            );
            assert!(spec.variant_name(spec.max_ordinal()).is_some());
        }
    }

    #[test]
    fn sparse_specs_look_up_by_declared_ordinal() {
        let spec = EnumFamilySpec {
            name: "Sparse",
            variants: &["Invalid", "First", "Tenth"],
            ordinals: Some(&[0, 1, 10]),
            ordinal_size: 1,
        };
        assert_eq!(spec.variant_ordinal("Tenth"), Some(10));
        assert_eq!(spec.variant_name(10), Some("Tenth"));
        assert_eq!(spec.variant_name(2), None);
        assert_eq!(spec.index_of_ordinal(10), Some(2));
        assert!(!spec.contains_ordinal(2));
        assert_eq!(spec.max_ordinal(), 10);
        assert_eq!(
            spec.iter().collect::<Vec<_>>(),
            [("Invalid", 0), ("First", 1), ("Tenth", 10)]
        );
    }

    #[test]
    fn country_names_follow_alpha2_ordinals() {
        assert_eq!(CountryCodeAlpha2_NAMES.len(), CountryCodeAlpha2::COUNT);
        assert_eq!(CountryCodeAlpha2::ORDINALS, CountryCodeAlpha3::ORDINALS);
        assert!(CountryCodeAlpha2::ORDINALS
            .iter()
            .enumerate()
            .all(|(index, ordinal)| *ordinal as usize == index));
    }

    #[test]
    fn symbology_is_ordinal_aligned_with_identifier_type() {
        let pairs: Vec<_> = Symbology::VARIANTS
            .iter()
            .copied()
            .zip(IdentifierType::VARIANTS.iter().copied())
            .collect();
        assert_eq!(Symbology::COUNT, IdentifierType::COUNT);
        assert_eq!(
            pairs,
            [
                ("Invalid", "Invalid"),
                ("Ticker", "Ticker"),
                ("ISIN", "InternationalSecuritiesIdentificationNumber"),
                (
                    "CUSIP",
                    "CommitteeOnUniformSecuritiesIdentificationProcedures"
                ),
                ("SEDOL", "StockExchangeDailyOfficialList"),
                ("FIGI", "FinancialInstrumentGlobalIdentifier"),
                ("LEI", "LegalEntityIdentifier"),
                ("RIC", "ReutersInstrumentCode"),
                ("PrimaryRIC", "PrimaryReutersInstrumentCode"),
                ("BBGTicker", "BloombergTicker"),
                ("MIC", "MarketIdentifierCode"),
                ("OSI", "OptionsSymbologyInitiative"),
                ("Internal", "Internal"),
            ]
        );
    }
}
