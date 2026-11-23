# API

`finance-enums` exposes the following public Python symbols:

```python
from finance_enums import (
   AccountType,
   AggressorSide,
   AgricultureType,
   AllocationMethod,
   AmortizationType,
   AssetBackedCollateralType,
   AuctionType,
   AveragingMethod,
   BarrierType,
   BenchmarkType,
   BondType,
   BookType,
   BorrowType,
   BusinessDayConvention,
   CFIClassification,
   CalculationAgentType,
   ClearingHouse,
   ClearingModel,
   CollateralType,
   CommodityType,
   CompoundingMethod,
   ContractStyle,
   ContractUnit,
   CorporateActionAdjustmentType,
   CorporateActionType,
   CountryCodeAlpha2,
   CountryCodeAlpha3,
   CouponType,
   CreditDefaultSwapTransactionType,
   CreditEventType,
   CreditQuality,
   CreditRatingAgency,
   CreditRatingOutlook,
   CrossType,
   Currency,
   CurrencyAliasRecord,
   CurrencyRecord,
   CurrencyRole,
   DayCountConvention,
   DebtGuaranteeType,
   DelistingReason,
   DeliveryType,
   DistributionPolicy,
   DurationType,
   EnergyType,
   EnumFamilySchema,
   EnumVariantRecord,
   EquityType,
   ExchangeCode,
   ExchangeRecord,
   ExecutionInstruction,
   ExecutionType,
   ExerciseEventType,
   ExoticOptionFeature,
   FactorGroup,
   FamaFrenchFactor,
   FinancingType,
   ForeignExchangeAtTheMoneyConvention,
   ForeignExchangeBenchmark,
   ForeignExchangeDeltaConvention,
   ForeignExchangeProductType,
   ForeignExchangeQuoteBasis,
   ForeignExchangeTenor,
   ForeignExchangeVolatilityQuoteType,
   Frequency,
   FundSubType,
   FundType,
   FutureAssetClass,
   FutureMonthCode,
   FutureSpreadLegType,
   FutureSpreadSubType,
   GiveUpType,
   IdentifierType,
   IndexWeightingMethod,
   Industry,
   IndustryGroup,
   InstrumentType,
   InterestRateProductType,
   InterestRateSwapType,
   InventoryType,
   IssuerType,
   LegRole,
   LiquidityFlag,
   ListingStatus,
   LivestockType,
   MarginType,
   MarketCategory,
   MarketState,
   MarketStatusReason,
   MarketType,
   MetalType,
   MoneyMarketInstrumentType,
   MutualFundEndedness,
   NettingType,
   ObligationCategory,
   ObligationCharacteristic,
   OptionExerciseType,
   OptionPremiumQuoteBasis,
   OptionStrikeQuoteBasis,
   OptionType,
   OrderCapacity,
   OrderSide,
   OrderStatus,
   OrderType,
   OvernightAccrualMethod,
   PayoffStyle,
   PayoutTiming,
   PeriodTiming,
   PeriodUnit,
   PositionEffect,
   PositionType,
   PriceIndexCalculationMethod,
   PriceKind,
   PriceNotation,
   QuantityUnit,
   QuoteCondition,
   RateIndex,
   RedemptionFeature,
   RepoType,
   RestructuringClause,
   RollConvention,
   ScheduleFrequency,
   Sector,
   SecurityForm,
   SecurityStatus,
   SecurityType,
   SegmentType,
   Seniority,
   SettlementFailReason,
   SettlementStatus,
   SettlementType,
   ShareClassHedging,
   ShortSaleRestriction,
   Side,
   StrategyType,
   StubType,
   StyleFactor,
   SubIndustry,
   SwapLegType,
   SwapType,
   SwaptionCashSettlementMethod,
   Symbology,
   TenderOfferType,
   TickDirection,
   TickerNamespace,
   TimeInForce,
   TouchType,
   TradeCondition,
   TradingPhase,
   TradingSession,
   TransactionIntent,
   UnderlyingAssetClass,
   VenueRegulatoryFlag,
   VenueType,
   YieldType,
   abi_compatible,
   abi_version,
   assert_abi_compatible,
   build_cfi,
   build_cfi_from_classification,
   country_currency,
   currency_alias_records,
   currency_countries,
   currency_export_capsule,
   currency_records,
   enum_export_capsule,
   enum_family_schemas,
   enum_schema,
   enum_schema_json,
   enum_variant_records,
   exchange_currency,
   exchange_export_capsule,
   exchange_record,
   exchange_records,
   exchange_records_by_country,
   exchange_records_by_currency,
   exchange_records_by_market_category,
   exchange_records_by_market_category_type,
   exchange_records_by_operating_mic,
   exchange_records_by_parent_mic,
   exchange_records_by_region,
   exchange_records_by_regulatory_flag,
   exchange_records_by_status,
   family_ordinal_size,
   family_variant_count,
   get_include,
   get_libraries,
   get_library_dirs,
   get_prefix,
   ordinal_of,
   parse_cfi,
   to_frequency,
   transaction_intent,
   transaction_intent_records,
   validate_cfi_classification,
   validate_ordinal,
   variant_name,
)
```

For enum-family descriptions and metadata conventions, see the
[Enums](ENUMS.md) page.

______________________________________________________________________

## Quick start

```python
from finance_enums import Currency, ExchangeCode, Frequency, to_frequency

Currency.USD.currency_name()
Currency("GBp")
ExchangeCode.XNYS.value
to_frequency("quarterly") == Frequency.Quarter
```

______________________________________________________________________

## Reference

```{eval-rst}
.. currentmodule:: finance_enums

.. autoclass:: CurrencyRecord
   :members:

.. autoclass:: CurrencyAliasRecord
   :members:

.. autofunction:: currency_records

.. autofunction:: currency_alias_records

.. autofunction:: currency_export_capsule

.. autoclass:: EnumVariantRecord
   :members:

.. autoclass:: EnumFamilySchema
   :members:

.. autofunction:: enum_variant_records

.. autofunction:: enum_family_schemas

.. autofunction:: enum_schema

.. autofunction:: enum_schema_json

.. autofunction:: enum_export_capsule

.. autoclass:: TransactionIntent
   :members:

.. autofunction:: transaction_intent_records

.. autofunction:: transaction_intent

.. autoclass:: Frequency
   :members:

.. autofunction:: to_frequency
```

______________________________________________________________________

## Generated enum classes

The generated enums are created from Rust variant arrays at import time.
Each is a `str` enum, so members compare naturally with their string
values when needed:

```python
from finance_enums import Side

Side.Buy.value
str(Side.Buy)
```

Generated enum classes:

- Countries: `CountryCodeAlpha2`, `CountryCodeAlpha3`
- Currencies: `Currency`
- Venues: `ExchangeCode`, `MarketCategory`, `VenueRegulatoryFlag`
- Market structure: `VenueType`, `MarketType`, `TradingSession`, `TradingPhase`, `MarketState`, `AuctionType`, `SegmentType`, `MarketStatusReason`
- Identifier and notation: `IdentifierType`, `Symbology`, `TickerNamespace`, `PriceNotation`, `QuantityUnit`, `CurrencyRole`
- Sectors: `Sector`, `IndustryGroup`, `Industry`, `SubIndustry`
- Instruments: `SecurityType`, `InstrumentType`, `EquityType`, `OptionType`, `OptionExerciseType`, `BondType`, `CommodityType`, `EnergyType`, `MetalType`, `AgricultureType`, `FundType`, `FundSubType`, `MutualFundEndedness`, `FutureAssetClass`, `SettlementType`, `UnderlyingAssetClass`, `ContractStyle`, `PayoffStyle`, `ContractUnit`, `LegRole`
- Financing: `CollateralType`, `MarginType`, `BorrowType`, `RepoType`, `FinancingType`
- Swaps and structured products: `SwapType`, `SwapLegType`, `BarrierType`, `AveragingMethod`, `ExoticOptionFeature`
- Post-trade and clearing: `SettlementType`, `DeliveryType`, `SettlementStatus`, `ClearingModel`, `ClearingHouse`, `SettlementFailReason`, `AllocationMethod`, `GiveUpType`
- Rates and schedules: `DayCountConvention`, `BusinessDayConvention`, `RollConvention`, `StubType`, `ScheduleFrequency`, `PeriodUnit`, `PeriodTiming`, `RateIndex`, `CompoundingMethod`, `OvernightAccrualMethod`, `PriceIndexCalculationMethod`, `InterestRateSwapType`, `InterestRateProductType`, `SwaptionCashSettlementMethod`
- Bonds and money markets: `BondType`, `IssuerType`, `CouponType`, `Seniority`, `RedemptionFeature`, `DebtGuaranteeType`, `AmortizationType`, `SecurityForm`, `AssetBackedCollateralType`, `MoneyMarketInstrumentType`, `YieldType`, `DurationType`
- Credit: `RestructuringClause`, `CreditEventType`, `ObligationCategory`, `ObligationCharacteristic`, `CreditDefaultSwapTransactionType`, `CreditRatingAgency`, `CreditRatingOutlook`, `CreditQuality`
- Foreign exchange: `ForeignExchangeProductType`, `ForeignExchangeTenor`, `ForeignExchangeQuoteBasis`, `ForeignExchangeBenchmark`, `ForeignExchangeDeltaConvention`, `ForeignExchangeAtTheMoneyConvention`, `ForeignExchangeVolatilityQuoteType`, `OptionStrikeQuoteBasis`, `OptionPremiumQuoteBasis`, `TouchType`, `PayoutTiming`
- Benchmarks and index administration: `BenchmarkType`, `IndexWeightingMethod`, `CorporateActionAdjustmentType`, `CalculationAgentType`
- Portfolio and fund structure: `AccountType`, `BookType`, `PositionType`, `InventoryType`, `StrategyType`, `NettingType`, `DistributionPolicy`, `ShareClassHedging`
- Corporate actions and lifecycle: `CorporateActionType`, `ListingStatus`, `SecurityStatus`, `ExerciseEventType`, `TenderOfferType`, `DelistingReason`
- Trading: `OrderType`, `OrderStatus`, `ExecutionType`, `ExecutionInstruction`, `LiquidityFlag`, `PositionEffect`, `OrderCapacity`, `ShortSaleRestriction`, `Side`, `OrderSide`, `TimeInForce`
- Market data: `QuoteCondition`, `TradeCondition`, `AggressorSide`, `CrossType`, `PriceKind`, `PriceNotation`

Exchange helpers now also support typed MIC category access through `ExchangeRecord.market_category()` / `ExchangeCode.market_category()`, standards-backed flags through `.regulatory_flags()`, and indexed lookups through `exchange_records_by_market_category_type()` and `exchange_records_by_regulatory_flag()`.

CFI helpers now support structured round trips through `build_cfi_from_classification()` and validation through `validate_cfi_classification()`, plus the equivalent `CFIClassification.to_code()` and `CFIClassification.validate()` convenience methods.

`Side` stays limited to buy/sell direction. Use `transaction_intent()` or `transaction_intent_records()` when a downstream transaction model needs common intent bundles such as opening a long, closing a long, opening a short, or covering a short.

`enum_family_schemas()` and `enum_schema_json()` expose the same Rust-backed enum vocabulary as versioned Python, JSON, Arrow-compatible, and C ABI metadata. The C ABI entry point is `finance_enums_enum_export_v1`.

Inspect available values with `.__members__`:

```python
from finance_enums import ExchangeCode

list(ExchangeCode.__members__)[:10]
"FOREX" in ExchangeCode.__members__
```

______________________________________________________________________

## Country helpers

```python
from finance_enums import CountryCodeAlpha2

CountryCodeAlpha2.US.country_name()
CountryCodeAlpha2.US.alpha3()
```

`CountryCodeAlpha3` also exposes `.country_name()`.

______________________________________________________________________

## Currency helpers

```python
from finance_enums import Currency, currency_records, currency_alias_records

Currency.USD.currency_name()
Currency.USD.is_iso4217()
Currency.USD.record()

records = {record.code: record for record in currency_records()}
aliases = {record.alias: record.canonical_code for record in currency_alias_records()}
```

Aliases are accepted by the enum constructor:

```python
Currency("USd")   # Currency.USX
Currency("EUr")   # Currency.EUX
Currency("e-CNY") # Currency.ECNY
```

______________________________________________________________________

## Frequency helpers

```python
from finance_enums import Frequency, to_frequency

freq = to_frequency("monthly")
freq.periods_per_year
freq.polars_truncate
```

Accepted aliases include common one-letter names (`"D"`, `"W"`,
`"M"`, `"Q"`, `"Y"`), canonical names (`"day"`, `"month"`), and
Polars-style bucket strings (`"1d"`, `"1mo"`, `"1q"`).

______________________________________________________________________

## Rust data access

Rust consumers use the `finance_enums` crate and read static arrays from
`finance_enums::data`:

```rust
use finance_enums::data::{Currency_VARIANTS, ExchangeCode_VARIANTS};

assert!(ExchangeCode_VARIANTS.contains(&"XNYS"));
assert!(Currency_VARIANTS.contains(&"USD"));
```

The Rust crate is intentionally data-only for enum variants. Python enum
classes are built in the Python package layer.

______________________________________________________________________

## Versioning

The current Python package version is exposed at
`finance_enums.__version__`. The public Python API is the symbols listed
at the top of this page. Native functions in
`finance_enums._finance_enums` are implementation details except for the
documented currency export capsule.
