# finance enums

Standard financial enumerations

[![Build Status](https://github.com/prettygoodcapital/finance-enums/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/prettygoodcapital/finance-enums/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/prettygoodcapital/finance-enums/branch/main/graph/badge.svg)](https://codecov.io/gh/prettygoodcapital/finance-enums)
[![License](https://img.shields.io/github/license/prettygoodcapital/finance-enums)](https://github.com/prettygoodcapital/finance-enums)
[![PyPI](https://img.shields.io/pypi/v/finance-enums.svg)](https://pypi.python.org/pypi/finance-enums)

## Overview

`finance-enums` is the shared vocabulary layer for the `finance-*`
stack. It exposes string-valued Python enums backed by Rust static data
tables, plus structured currency metadata and a small frequency enum used
by calendar-aware libraries.

The goal is to make identifiers boring and consistent: country codes,
currencies, exchange codes, GICS-like sector taxonomy, security types,
instrument types, portfolio labels, lifecycle states, order flags,
trade sides, and time-in-force values all come from one package.

### Quick start

```python
from finance_enums import (
    CommodityType,
    ContractStyle,
    Currency,
    ExchangeCode,
    OptionExerciseType,
    OptionType,
    SecurityType,
    SettlementType,
    Sector,
    UnderlyingAssetClass,
    exchange_record,
    exchange_records_by_country,
    build_cfi,
    parse_cfi,
    Frequency,
    to_frequency,
)

str(Currency.USD)                    # "USD"
Currency.USD.currency_name()         # "United States dollar"
Currency.USD.is_iso4217()            # True
Currency("e-CNY")                    # Currency.ECNY

ExchangeCode.XNYS.value              # "XNYS"
ExchangeCode.XNYS.record().region    # "Americas"
exchange_record("XNYS").market_name  # "NEW YORK STOCK EXCHANGE, INC."
len(exchange_records_by_country("US")) > 0

parse_cfi("ESVUFB").equity_type.value   # "Shares"
build_cfi(security_type=SecurityType.Option, option_type=OptionType.Call)  # "OCXXXX"
build_cfi(
    security_type=SecurityType.Option,
    option_type=OptionType.Call,
    option_exercise_type=OptionExerciseType.American,
    underlying_asset_class=UnderlyingAssetClass.Equity,
    settlement_type=SettlementType.Physical,
    contract_style=ContractStyle.Standardized,
)  # "OCASPS"
build_cfi(security_type=SecurityType.Currency)                              # "IFXXXP"
build_cfi(security_type=SecurityType.Commodity, commodity_type=CommodityType.Agriculture)  # "ITAXXX"
build_cfi(category="S", group="F")                                        # "SFXXXX"

Sector.InformationTechnology.value   # "InformationTechnology"

to_frequency("monthly")             # Frequency.Month
Frequency.Month.periods_per_year     # 12
Frequency.Month.polars_truncate      # "1mo"
```

### Enum families

The public Python API includes:

- Countries: `CountryCode`, `CountryCode3`
- Currencies: `Currency`, `CurrencyRecord`, `CurrencyAliasRecord`, `currency_records`, `currency_alias_records`
- Venues: `ExchangeCode`, `ExchangeRecord`, `exchange_record`, `exchange_records`, `exchange_records_by_country`, `exchange_records_by_operating_mic`, `exchange_records_by_parent_mic`, `exchange_records_by_status`, `exchange_records_by_region`, `exchange_records_by_market_category`, `MICMarketCategory`, `VenueRegulatoryFlag`, `exchange_records_by_market_category_type`, `exchange_records_by_regulatory_flag`
- Sector taxonomy: `Sector`, `IndustryGroup`, `Industry`, `SubIndustry`
- Market structure: `VenueType`, `MarketType`, `TradingSession`, `MarketState`, `AuctionType`, `SegmentType`, `MarketStatusReason`
- Identifier and notation: `IdentifierType`, `TickerNamespace`, `PriceNotation`, `QuantityUnit`, `CurrencyRole`
- Instruments: `SecurityType`, `InstrumentType`, `EquityType`, `OptionType`, `OptionExerciseType`, `BondType`, `CommodityType`, `EnergyType`, `MetalsType`, `AgricultureType`, `FundType`, `FundSubType`, `MutualFundEndedness`, `FutureType`, `FutureDeliveryType`, `SettlementType`, `DeliveryType`, `UnderlyingAssetClass`, `ContractStyle`, `PayoffStyle`, `ContractUnit`, `LegRole`
- Fixed income and financing: `CouponType`, `CouponFrequency`, `DayCountConvention`, `AmortizationType`, `Seniority`, `CollateralType`, `MarginType`, `BorrowType`, `RepoType`, `FinancingType`
- Swaps and structured products: `SwapType`, `SwapLegType`, `RateIndex`, `ResetFrequency`, `CompoundingMethod`, `StubType`, `BarrierType`, `AveragingMethod`, `ExoticOptionFeature`
- Portfolio and fund structure: `AccountType`, `BookType`, `PositionType`, `InventoryType`, `StrategyType`, `NettingType`, `VehicleWrapper`, `DistributionPolicy`, `ShareClassHedging`, `LiquidityTerm`, `RedemptionFrequency`
- Corporate actions and lifecycle: `CorporateActionType`, `ListingStatus`, `SecurityStatus`, `ExerciseEventType`, `TenderOfferType`, `DelistingReason`
- CFI helpers: `CFIClassification`, `parse_cfi`, `build_cfi`, `build_cfi_from_classification`, `validate_cfi_classification`
- Trading: `OrderType`, `OrderStatus`, `ExecType`, `ExecutionInstruction`, `LiquidityFlag`, `PositionEffect`, `OpenClose`, `OrderCapacity`, `ShortSaleRestriction`, `Side`, `OrderFlag`, `TimeInForce`, `TradingType`
- Market data: `QuoteCondition`, `TradeCondition`, `AggressorSide`, `CrossType`, `PriceType`
- Frequencies: `Frequency`, `to_frequency`

### Documentation

See the [Enums](docs/src/ENUMS.md) page for the enum families,
metadata conventions, exchange-code relationship with `finance-dates`,
and Rust/Python naming notes. See the [API](docs/src/API.md) page for a
reference and recipes.

### Rust crate

The Rust crate is published as `finance_enums` on crates.io and imported
as `finance_enums` in Rust code:

```toml
[dependencies]
finance_enums = "0.3.0"
```

```rust
use finance_enums::data::ExchangeCode_VARIANTS;
```

The Python package name is `finance-enums`; the Rust package uses an
underscore because the original crates.io name cannot be renamed to the
hyphenated spelling.

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).

## Currency Metadata

Currency data is maintained from a structured Rust source of truth.

- Each currency row includes a code, display name, and `is_iso4217` flag.
- Python exposes structured access through `currency_records()` and `currency_alias_records()`.
- Native consumers can re-extract the same immutable dataset through the versioned `finance_enums.currency_export_v1` `PyCapsule` or the exported `finance_enums_currency_export_v1` C ABI symbol.

## Exchange Metadata

Exchange coverage is now backed by bundled ISO 10383 MIC records plus a small set of project-defined calendar families.

- Python exposes structured exchange access through `exchange_records()` and `ExchangeCode.record()`.
- Python also exposes direct venue lookups through `exchange_record()` and indexed filters through `exchange_records_by_country()`, `exchange_records_by_operating_mic()`, `exchange_records_by_parent_mic()`, `exchange_records_by_status()`, `exchange_records_by_region()`, `exchange_records_by_market_category()`, `exchange_records_by_market_category_type()`, and `exchange_records_by_regulatory_flag()`.
- Each `ExchangeRecord` and `ExchangeCode` can derive a typed MIC market category through `.market_category()` and standards-backed regulatory flags through `.regulatory_flags()` / `.has_regulatory_flag()`.
- Bundled exchange metadata includes market name, legal entity, operating and parent MICs, market category, acronym, ISO country code, city, website, status, region, subregion, segment flag, and official/project provenance.
- Project-defined non-ISO venue families remain available for downstream calendar consumers: `PYPR`, `SIMU`, `FOREX`, `CRYPTO`, `SIFMA_US`, `ICE_US`, and `CFE`.

## Native C ABI

`finance-enums` now ships a minimal versioned C ABI for immutable currency and exchange metadata.

- The core Rust crate exports `finance_enums_currency_export_v1` and `finance_enums_exchange_export_v1`.
- The Rust build generates `finance_enums/include/finance_enums.h`, and wheel builds install that header to `include/finance_enums/finance_enums.h`.
- Wheels also bundle a standalone shared library inside `finance_enums/lib/` so downstream C or C++ code can link against the same versioned export surface.

## CFI Helpers

`finance-enums` now includes a broader ISO 10962 / CFI parser and builder.

- `parse_cfi()` maps supported families into the existing enum surface for equities, bonds, funds, options, futures, swaps, financing, spot FX, spot commodities, forwards, spreads, and indices, while preserving the raw category, group, and attribute characters.
- `build_cfi()` emits category/group-correct codes for the supported enum-backed families and also accepts raw `category`, `group`, and `attributes` inputs for ISO categories that the library does not model with dedicated enums yet.
- `build_cfi_from_classification()` and `CFIClassification.to_code()` provide a structured round-trip path from typed enum-backed classifications back into ISO 10962 strings.
- `validate_cfi_classification()` and `CFIClassification.validate()` check that the typed fields, raw CFI positions, and stored `code` all agree before downstream code persists or republishes a classification.
- Listed options and futures now expose typed derivative attributes for underlier asset class, settlement or delivery semantics, and contract standardization instead of leaving those positions opaque.
- Non-listed options, forwards, and strategies now support rate, credit, mixed-asset, and other high-value CFI underlier groups through `UnderlyingAssetClass`.
- `SecurityType.PerpetualFuture` is available as a standalone library type and builds through the ISO futures CFI envelope, because ISO 10962 does not encode a dedicated perpetual-future category.
- Remaining unsupported enum families still raise `NotImplementedError` during generation rather than guessing invalid codes.

## Live Reference Tests

Live standards coverage tests are part of the normal pytest suite and are marked `live_source`.

- Default local test runs skip them automatically.
- Enable them by running `FINANCE_ENUMS_RUN_LIVE_TESTS=1 /opt/homebrew/bin/python -m pytest -q finance_enums/tests`.
