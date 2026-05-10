# Enums

`finance-enums` centralizes identifier vocabularies used across the
`finance-*` libraries. Python gets string-valued `Enum` classes; Rust
gets static data arrays under `finance_enums::data`.

All generated Python enum values are strings whose value equals the
member name:

```python
from finance_enums import Currency

str(Currency.USD)  # "USD"
Currency.USD.value # "USD"
```

______________________________________________________________________

## Package naming

Python package:

```bash
pip install finance-enums
```

Rust package:

```toml
[dependencies]
finance_enums = "0.3.0"
```

The Rust package name intentionally uses an underscore. The crate was
first published as `finance_enums`, and crates.io does not allow that
package identity to be renamed to `finance-enums`. Rust import paths also
use underscores:

```rust
use finance_enums::data::ExchangeCode_VARIANTS;
```

______________________________________________________________________

## Country codes

`CountryCode` represents ISO 3166-1 alpha-2 codes and `CountryCode3`
represents ISO 3166-1 alpha-3 codes.

```python
from finance_enums import CountryCode, CountryCode3

CountryCode.US.country_name()  # "United States of America"
CountryCode.US.code3()         # CountryCode3.USA
CountryCode3.USA.country_name()
```

The two country-code tables are kept aligned by Rust tests.

______________________________________________________________________

## Currency metadata

`Currency` covers ISO 4217 currencies plus explicit project-defined
extensions such as offshore or subunit aliases. Each currency has a
structured record:

```python
from finance_enums import Currency, currency_records, currency_alias_records

Currency.USD.currency_name()  # "United States dollar"
Currency.USD.is_iso4217()     # True
Currency.CNH.is_iso4217()     # False
Currency.ECNY.record()
```

Aliases normalize common market spellings into canonical members:

```python
Currency("GBp")   # Currency.GBX
Currency("USd")   # Currency.USX
Currency("e-CNY") # Currency.ECNY
```

`currency_records()` returns immutable dataclass values with:

| Field          | Meaning                                               |
| -------------- | ----------------------------------------------------- |
| `code`         | Canonical currency code                               |
| `display_name` | Human-readable currency name                          |
| `is_iso4217`   | True for ISO 4217 codes, false for project extensions |

`currency_alias_records()` returns alias-to-canonical mappings.

### Native currency and exchange exports

Native consumers that need the immutable metadata tables without
importing Python enum objects can read the same data through either:

- `currency_export_capsule()`, a `PyCapsule` named
  `finance_enums.currency_export_v1`
- the exported C ABI symbols `finance_enums_currency_export_v1` and
  `finance_enums_exchange_export_v1`

The exported struct is versioned so future changes can add a new export
without changing the meaning of version 1.

The Rust build also generates a public header at
`finance_enums/include/finance_enums.h`, and wheel builds install that
header to `include/finance_enums/finance_enums.h` while bundling the
standalone shared library under `finance_enums/lib/`.

______________________________________________________________________

## Exchange codes

`ExchangeCode` contains MIC-style exchange identifiers plus generic
families used by the calendar layer:

```python
from finance_enums import ExchangeCode

ExchangeCode.XNYS
ExchangeCode.XLON
ExchangeCode.FOREX
ExchangeCode.CRYPTO
```

`finance-dates` imports the Rust `ExchangeCode_VARIANTS` table from this
crate and uses it as the source of truth for `finance_dates.EXCHANGE_CODES`.
That keeps exchange discovery consistent between enum and calendar code.

Typed MIC category helpers are also exposed for standards-backed venue
classification:

- `MICMarketCategory` captures the bundled MIC market-category codes as typed enums.
- `VenueRegulatoryFlag` exposes cross-cutting distinctions such as MTF, OTF, TRF, SEF, APA, and systematic internaliser.
- `ExchangeRecord.market_category()` and `ExchangeCode.market_category()` resolve raw MIC codes into typed categories.
- `exchange_records_by_market_category_type()` and `exchange_records_by_regulatory_flag()` provide indexed lookups on the same bundled metadata.

______________________________________________________________________

## Sector taxonomy

The sector taxonomy exports four levels:

| Level          | Symbol          |
| -------------- | --------------- |
| Sector         | `Sector`        |
| Industry group | `IndustryGroup` |
| Industry       | `Industry`      |
| Sub-industry   | `SubIndustry`   |

These values are useful for schema validation, synthetic data
generation, analytics labels, and plotting facets.

______________________________________________________________________

## Security and instrument taxonomy

Security and instrument identifiers cover broad asset classes and nested
subtypes:

- Broad types: `SecurityType`, `InstrumentType`
- Market structure: `VenueType`, `MarketType`, `TradingSession`, `MarketState`, `AuctionType`, `SegmentType`, `MarketStatusReason`
- Identifier and notation: `IdentifierType`, `TickerNamespace`, `PriceNotation`, `QuantityUnit`, `CurrencyRole`
- Equity: `EquityType`
- Options: `OptionType`, `OptionExerciseType`, `SettlementType`, `DeliveryType`, `UnderlyingAssetClass`, `ContractStyle`, `PayoffStyle`
- Bonds: `BondType`
- Commodities: `CommodityType`, `EnergyType`, `MetalsType`, `AgricultureType`
- Funds: `FundType`, `FundSubType`, `MutualFundEndedness`
- Futures: `FutureType`, `FutureDeliveryType`, `ContractUnit`, `LegRole`
- Fixed income and financing: `CouponType`, `CouponFrequency`, `DayCountConvention`, `AmortizationType`, `Seniority`, `CollateralType`, `MarginType`, `BorrowType`, `RepoType`, `FinancingType`
- Swaps and structured products: `SwapType`, `SwapLegType`, `RateIndex`, `ResetFrequency`, `CompoundingMethod`, `StubType`, `BarrierType`, `AveragingMethod`, `ExoticOptionFeature`

The taxonomy is deliberately descriptive rather than behavioral. It does
not attempt to price or model instruments; it standardizes labels.

______________________________________________________________________

## Portfolio and lifecycle enums

Shared post-trade and fund-operation vocabularies now include:

- Portfolio and booking: `AccountType`, `BookType`, `PositionType`, `InventoryType`, `StrategyType`, `NettingType`
- Fund and vehicle structure: `VehicleWrapper`, `DistributionPolicy`, `ShareClassHedging`, `LiquidityTerm`, `RedemptionFrequency`
- Security lifecycle: `CorporateActionType`, `ListingStatus`, `SecurityStatus`, `ExerciseEventType`, `TenderOfferType`, `DelistingReason`

These enums are intended for validation and shared schemas across
execution, risk, portfolio, and reference-data workflows.

______________________________________________________________________

## Structured CFI helpers

`CFIClassification` now supports structured round trips back into ISO
10962 strings:

- `build_cfi_from_classification()` and `CFIClassification.to_code()` rebuild a CFI code from the typed fields on a classification.
- `validate_cfi_classification()` and `CFIClassification.validate()` ensure that the raw category, group, attributes, and stored `code` remain consistent with the typed enum fields.

This keeps downstream systems from having to manually reassemble CFI
strings when they are already working with a parsed classification.

______________________________________________________________________

## Trading enums

Trading workflow identifiers include:

- Order workflow: `OrderType`, `OrderStatus`, `ExecType`, `ExecutionInstruction`, `OrderCapacity`, `PositionEffect`, `OpenClose`, `ShortSaleRestriction`
- Venue and execution flags: `LiquidityFlag`, `OrderFlag`, `TimeInForce`, `TradingType`
- Market-data conditions: `QuoteCondition`, `TradeCondition`, `AggressorSide`, `CrossType`, `PriceType`
- Side: `Side`

These enums are intended for validation and shared API contracts rather than order routing logic.

______________________________________________________________________

## Frequencies

`Frequency` is a small hand-written enum for calendar-aware periods:

```python
from finance_enums import Frequency, to_frequency

to_frequency("D")       # Frequency.Day
to_frequency("weekly")  # Frequency.Week
to_frequency("1mo")     # Frequency.Month

Frequency.Day.periods_per_year      # 252
Frequency.Month.polars_truncate     # "1mo"
```

Use `to_frequency()` at package boundaries when user input may be a
string alias.
