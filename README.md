# finance enums

Standard financial enumerations

[![Build Status](https://github.com/prettygoodcapital/finance-enums/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/prettygoodcapital/finance-enums/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/prettygoodcapital/finance-enums/branch/main/graph/badge.svg)](https://codecov.io/gh/prettygoodcapital/finance-enums)
[![License](https://img.shields.io/github/license/prettygoodcapital/finance-enums)](https://github.com/prettygoodcapital/finance-enums)
[![PyPI](https://img.shields.io/pypi/v/finance-enums.svg)](https://pypi.python.org/pypi/finance-enums)

## Overview

- `CountryCode` (`ISO 3166-1 alpha-2`)
  - `Country` in Python
- `CountryCode3` (`ISO 3166-1 alpha-3`)
- `CountryCode.name`
- `CountryCode.flag` (`base64` encoded `png` of flag)
- `Currency` (`ISO 4217` plus explicit project-defined extensions marked as non-ISO)
- `Currency.name`
- `Exchange` (`ISO 10383`)
  - Note: NMS US Equities only for now
- `Sector`
- `IndustryGroup`
- `Industry`
- `SubIndustry`
- `SecurityType`
  - `EquityType`
  - `OptionType`
    - `OptionExerciseType`
  - `BondType`
  - `CommodityType`
  - `FundType`
    - `FundSubType`
    - `MutualFundEndedness`
- `OrderType`
- `Side`
- `TimeInForce`
- `OrderFlag`

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).

## Currency Metadata

Currency data is maintained from a structured Rust source of truth.

- Each currency row includes a code, display name, and `is_iso4217` flag.
- Python exposes structured access through `currency_records()` and `currency_alias_records()`.
- Native consumers can re-extract the same immutable dataset through the versioned `finance_enums.currency_export_v1` `PyCapsule` or the exported `finance_enums_currency_export_v1` C ABI symbol.
