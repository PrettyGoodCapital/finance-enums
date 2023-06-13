# finance-enums
Standard Financial Enumerations

[![Build Status](https://github.com/timkpaine/finance_enums/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/timkpaine/finance_enums/actions?query=workflow%3A%22Build+Status%22)
[![Coverage](https://codecov.io/gh/timkpaine/finance_enums/branch/main/graph/badge.svg?token=ag2j2TV2wE)](https://codecov.io/gh/timkpaine/finance_enums)
[![License](https://img.shields.io/github/license/timkpaine/finance_enums.svg)](https://pypi.python.org/pypi/finance_enums/)
[![PyPI](https://img.shields.io/pypi/v/finance_enums.svg)](https://pypi.python.org/pypi/finance_enums/)


## Categories

- `CountryCode` (`ISO 3166-1 alpha-2`)
    - `Country` in Python
- `CountryCode3` (`ISO 3166-1 alpha-3`)
- `CountryCode.name`
- `CountryCode.flag` (`base64` encoded `png` of flag)
- `Currency` (`ISO 4217`)
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
