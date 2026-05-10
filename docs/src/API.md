# API

`finance-enums` exposes the following public Python symbols:

```python
from finance_enums import (
   AccountType,
   AggressorSide,
   AgricultureType,
   AmortizationType,
   AuctionType,
   AveragingMethod,
   BarrierType,
   BondType,
   BookType,
   BorrowType,
   CollateralType,
   CommodityType,
   CompoundingMethod,
   ContractStyle,
   ContractUnit,
   CorporateActionType,
   CountryCode,
   CountryCode3,
   CouponFrequency,
   CouponType,
   CrossType,
   Currency,
   CurrencyAliasRecord,
   CurrencyRecord,
   CurrencyRole,
   MICMarketCategory,
   DayCountConvention,
   DelistingReason,
   DeliveryType,
   DistributionPolicy,
   EnergyType,
   EquityType,
   ExchangeCode,
   ExecType,
   ExerciseEventType,
   ExoticOptionFeature,
   FinancingType,
   Frequency,
   FundSubType,
   FundType,
   FutureDeliveryType,
   FutureType,
   IdentifierType,
   Industry,
   IndustryGroup,
   InstrumentType,
   InventoryType,
   LegRole,
   LiquidityFlag,
   LiquidityTerm,
   ListingStatus,
   MarginType,
   MarketState,
   MarketStatusReason,
   MarketType,
   MetalsType,
   MutualFundEndedness,
   NettingType,
   OpenClose,
   OptionExerciseType,
   OptionType,
   OrderCapacity,
   OrderFlag,
   OrderStatus,
   OrderType,
   PayoffStyle,
   PerpetualFutureType,
   PositionEffect,
   PositionType,
   PriceNotation,
   PriceType,
   QuantityUnit,
   QuoteCondition,
   RateIndex,
   RedemptionFrequency,
   RepoType,
   ResetFrequency,
   Sector,
   SegmentType,
   Seniority,
   SecurityStatus,
   SecurityType,
   SettlementType,
   ShareClassHedging,
   ShortSaleRestriction,
   Side,
   StrategyType,
   StubType,
   SubIndustry,
   SwapLegType,
   SwapType,
   TenderOfferType,
   TickerNamespace,
   TimeInForce,
   TradeCondition,
   TradingSession,
   TradingType,
   UnderlyingAssetClass,
   VenueRegulatoryFlag,
   VehicleWrapper,
   VenueType,
   build_cfi,
   build_cfi_from_classification,
   currency_alias_records,
   currency_export_capsule,
   currency_records,
   exchange_record,
   exchange_records,
   exchange_records_by_country,
   exchange_records_by_market_category,
   exchange_records_by_market_category_type,
   exchange_records_by_operating_mic,
   exchange_records_by_parent_mic,
   exchange_records_by_region,
   exchange_records_by_regulatory_flag,
   exchange_records_by_status,
   parse_cfi,
   to_frequency,
   validate_cfi_classification,
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

- Countries: `CountryCode`, `CountryCode3`
- Currencies: `Currency`
- Venues: `ExchangeCode`, `MICMarketCategory`, `VenueRegulatoryFlag`
- Market structure: `VenueType`, `MarketType`, `TradingSession`, `MarketState`, `AuctionType`, `SegmentType`, `MarketStatusReason`
- Identifier and notation: `IdentifierType`, `TickerNamespace`, `PriceNotation`, `QuantityUnit`, `CurrencyRole`
- Sectors: `Sector`, `IndustryGroup`, `Industry`, `SubIndustry`
- Instruments: `SecurityType`, `InstrumentType`, `EquityType`, `OptionType`, `OptionExerciseType`, `BondType`, `CommodityType`, `EnergyType`, `MetalsType`, `AgricultureType`, `FundType`, `FundSubType`, `MutualFundEndedness`, `FutureType`, `FutureDeliveryType`, `SettlementType`, `DeliveryType`, `UnderlyingAssetClass`, `ContractStyle`, `PayoffStyle`, `ContractUnit`, `LegRole`
- Fixed income and financing: `CouponType`, `CouponFrequency`, `DayCountConvention`, `AmortizationType`, `Seniority`, `CollateralType`, `MarginType`, `BorrowType`, `RepoType`, `FinancingType`
- Swaps and structured products: `SwapType`, `SwapLegType`, `RateIndex`, `ResetFrequency`, `CompoundingMethod`, `StubType`, `BarrierType`, `AveragingMethod`, `ExoticOptionFeature`
- Portfolio and fund structure: `AccountType`, `BookType`, `PositionType`, `InventoryType`, `StrategyType`, `NettingType`, `VehicleWrapper`, `DistributionPolicy`, `ShareClassHedging`, `LiquidityTerm`, `RedemptionFrequency`
- Corporate actions and lifecycle: `CorporateActionType`, `ListingStatus`, `SecurityStatus`, `ExerciseEventType`, `TenderOfferType`, `DelistingReason`
- Trading: `OrderType`, `OrderStatus`, `ExecType`, `ExecutionInstruction`, `LiquidityFlag`, `PositionEffect`, `OpenClose`, `OrderCapacity`, `ShortSaleRestriction`, `Side`, `OrderFlag`, `TimeInForce`, `TradingType`
- Market data: `QuoteCondition`, `TradeCondition`, `AggressorSide`, `CrossType`, `PriceType`

Exchange helpers now also support typed MIC category access through `ExchangeRecord.market_category()` / `ExchangeCode.market_category()`, standards-backed flags through `.regulatory_flags()`, and indexed lookups through `exchange_records_by_market_category_type()` and `exchange_records_by_regulatory_flag()`.

CFI helpers now support structured round trips through `build_cfi_from_classification()` and validation through `validate_cfi_classification()`, plus the equivalent `CFIClassification.to_code()` and `CFIClassification.validate()` convenience methods.

Inspect available values with `.__members__`:

```python
from finance_enums import ExchangeCode

list(ExchangeCode.__members__)[:10]
"FOREX" in ExchangeCode.__members__
```

______________________________________________________________________

## Country helpers

```python
from finance_enums import CountryCode

CountryCode.US.country_name()
CountryCode.US.code3()
```

`CountryCode3` also exposes `.country_name()`.

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
`finance_enums.finance_enums` are implementation details except for the
documented currency export capsule.
