"""Standard financial enumerations.

Variant names and structured currency metadata are stored in Rust. This module
reads those tables at import time, constructs Python ``IntEnum`` classes with
attached lookup methods, and re-exports the domain helpers from the cfi /
country / currency / exchange / schema / trading submodules.
"""

from __future__ import annotations

from typing import Any

from . import _finance_enums as _rust_enums
from ._finance_enums import (
    __all_families__,
    abi_compatible,
    abi_version,
    assert_abi_compatible,
    currency_export_capsule,
    enum_export_capsule,
    family_variant_count,
    ordinal_of,
    validate_ordinal,
    variant_name,
)
from .frequency import Frequency, to_frequency

__version__ = "0.7.0"

#: Semantic enum-data ABI version of the loaded native extension, as
#: ``(major, minor, patch)``. See the "ABI compatibility" section of the README.
__abi_version__ = abi_version()


def exchange_export_capsule():
    """Return the exchange C ABI export capsule when provided by the native extension."""
    capsule_fn = getattr(_rust_enums, "exchange_export_capsule", None)
    if capsule_fn is None:
        raise ImportError("finance_enums native extension does not expose exchange_export_capsule")
    return capsule_fn()


_ENUM_ACRONYM_ALIASES: dict[str, dict[str, str]] = {
    "AllocationMethod": {
        "FIFO": "FirstInFirstOut",
        "LIFO": "LastInFirstOut",
    },
    "BenchmarkType": {"FXFixing": "ForeignExchangeFixing"},
    "ClearingHouse": {
        "NSCC": "NationalSecuritiesClearingCorporation",
        "FICC": "FixedIncomeClearingCorporation",
        "OCC": "OptionsClearingCorporation",
        "CME": "ChicagoMercantileExchange",
        "ICEClear": "IntercontinentalExchangeClear",
        "LCH": "LondonClearingHouse",
        "DTCC": "DepositoryTrustClearingCorporation",
    },
    "CurrencyRole": {"PnL": "ProfitAndLoss"},
    "EnergyType": {"LNG": "LiquefiedNaturalGas"},
    "FundType": {
        "ETF": "ExchangeTradedFund",
        "REIT": "RealEstateInvestmentTrust",
    },
    "IdentifierType": {
        "ISIN": "InternationalSecuritiesIdentificationNumber",
        "CUSIP": "CommitteeOnUniformSecuritiesIdentificationProcedures",
        "SEDOL": "StockExchangeDailyOfficialList",
        "FIGI": "FinancialInstrumentGlobalIdentifier",
        "LEI": "LegalEntityIdentifier",
        "RIC": "ReutersInstrumentCode",
        "MIC": "MarketIdentifierCode",
    },
    "Industry": {
        "ITServices": "InformationTechnologyServices",
        "DiversifiedREITs": "DiversifiedRealEstateInvestmentTrusts",
        "IndustrialREITs": "IndustrialRealEstateInvestmentTrusts",
        "HotelAndResortREITs": "HotelAndResortRealEstateInvestmentTrusts",
        "OfficeREITs": "OfficeRealEstateInvestmentTrusts",
        "HealthCareREITs": "HealthCareRealEstateInvestmentTrusts",
        "ResidentialREITs": "ResidentialRealEstateInvestmentTrusts",
        "RetailREITs": "RetailRealEstateInvestmentTrusts",
        "SpecializedREITs": "SpecializedRealEstateInvestmentTrusts",
    },
    "MarketType": {"OTC": "OverTheCounter"},
    "PriceKind": {"VWAP": "Vwap"},
    "RateIndex": {
        "SOFR": "SecuredOvernightFinancingRate",
        "ESTR": "EuroShortTermRate",
        "SONIA": "SterlingOvernightIndexAverage",
        "EURIBOR": "EuroInterbankOfferedRate",
        "TONAR": "TokyoOvernightAverageRate",
        "SARON": "SwissAverageRateOvernight",
        "CPI": "ConsumerPriceIndex",
    },
    "ShortSaleRestriction": {"RegSHOPriceTest": "RegulationShoPriceTest"},
    "SubIndustry": {
        "ITConsultingAndOtherServices": "InformationTechnologyConsultingAndOtherServices",
        "DiversifiedREITs": "DiversifiedRealEstateInvestmentTrusts",
        "IndustrialREITs": "IndustrialRealEstateInvestmentTrusts",
        "HotelAndResortREITs": "HotelAndResortRealEstateInvestmentTrusts",
        "OfficeREITs": "OfficeRealEstateInvestmentTrusts",
        "HealthCareREITs": "HealthCareRealEstateInvestmentTrusts",
        "MultiFamilyResidentialREITs": "MultiFamilyResidentialRealEstateInvestmentTrusts",
        "SingleFamilyResidentialREITs": "SingleFamilyResidentialRealEstateInvestmentTrusts",
        "RetailREITs": "RetailRealEstateInvestmentTrusts",
        "OtherSpecializedREITs": "OtherSpecializedRealEstateInvestmentTrusts",
        "SelfStorageREITs": "SelfStorageRealEstateInvestmentTrusts",
        "TelecomTowerREITs": "TelecomTowerRealEstateInvestmentTrusts",
        "TimberREITs": "TimberRealEstateInvestmentTrusts",
        "DataCenterREITs": "DataCenterRealEstateInvestmentTrusts",
    },
    "TickerNamespace": {"OTC": "OverTheCounter"},
    "VehicleWrapper": {
        "ETF": "ExchangeTradedFund",
        "SICAV": "SocieteInvestissementCapitalVariable",
        "OEIC": "OpenEndedInvestmentCompany",
    },
}


#: Native ``IntEnum`` classes generated in Rust, keyed by family name.
_int_enums = _rust_enums.int_enums


def _install_enum_behaviour(cls: Any, alias_map: dict[str, str] | None, *, expose_aliases: bool) -> None:
    """Attach acronym/alias resolution and ``str`` formatting to a native IntEnum.

    The native classes are plain ``IntEnum`` families whose ``value`` is the
    variant ordinal. This restores the package's ergonomics:

    * ``str(member)`` returns the variant name (e.g. ``"USD"``);
    * ``EnumType("Name")`` and ``EnumType("Alias")`` resolve to the member; and
    * acronym aliases are exposed as members (e.g. ``FundType.ETF``).
    """

    member_map = cls._member_map_
    if alias_map:
        unknown = sorted({canonical for canonical in alias_map.values() if canonical not in member_map})
        if unknown:
            raise ValueError(f"aliases for {cls.__name__} reference unknown members: {unknown}")
        if expose_aliases:
            for alias, canonical in alias_map.items():
                if alias.isidentifier() and alias not in member_map:
                    member = member_map[canonical]
                    setattr(cls, alias, member)
                    member_map[alias] = member

    def _missing_(c: Any, value: Any) -> Any:
        if isinstance(value, str):
            member = c._member_map_.get(value)
            if member is not None:
                return member
            if alias_map is not None:
                canonical = alias_map.get(value)
                if canonical is not None:
                    return c._member_map_[canonical]
        return None

    cls._missing_ = classmethod(_missing_)
    cls.__str__ = lambda self: self.name


# Currency aliases are derived in the currency submodule; the install loop needs
# them to resolve string aliases on the ``Currency`` family.
from .currency import currency_aliases as _currency_aliases

# Install alias resolution and string formatting on every native IntEnum family,
# and expose each family as a module-level attribute.
for _family_name in __all_families__:
    _family_cls = getattr(_int_enums, _family_name)
    if _family_name == "Currency":
        _install_enum_behaviour(_family_cls, _currency_aliases, expose_aliases=False)
    else:
        _install_enum_behaviour(_family_cls, _ENUM_ACRONYM_ALIASES.get(_family_name), expose_aliases=True)
    globals()[_family_name] = _family_cls
del _family_name, _family_cls


# Domain helpers. Imported after the install loop so the families carry their
# string/alias resolution behaviour before the helpers attach methods to them.
from .cfi import (
    CFIClassification,
    build_cfi,
    build_cfi_from_classification,
    parse_cfi,
    validate_cfi_classification,
)
from .country import country_currency, currency_countries
from .currency import (
    CurrencyAliasRecord,
    CurrencyRecord,
    currency_alias_records,
    currency_records,
)
from .exchange import (
    ExchangeRecord,
    exchange_currency,
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
)
from .schema import (
    EnumFamilySchema,
    EnumVariantRecord,
    enum_family_schemas,
    enum_schema,
    enum_schema_json,
    enum_variant_records,
)
from .trading import (
    TransactionIntent,
    transaction_intent,
    transaction_intent_records,
)

__all__ = [
    "AccountType",
    "AggressorSide",
    "AgricultureType",
    "AllocationMethod",
    "AmortizationType",
    "AuctionType",
    "AveragingMethod",
    "BarrierType",
    "BenchmarkType",
    "BondType",
    "BookType",
    "BorrowType",
    "CFIClassification",
    "CalculationAgentType",
    "ClearingHouse",
    "ClearingModel",
    "CollateralType",
    "CommodityType",
    "CompoundingMethod",
    "ContractStyle",
    "ContractUnit",
    "CorporateActionAdjustmentType",
    "CorporateActionType",
    "CountryCode",
    "CountryCode3",
    "CouponFrequency",
    "CouponType",
    "CrossType",
    "Currency",
    "CurrencyAliasRecord",
    "CurrencyRecord",
    "CurrencyRole",
    "DayCountConvention",
    "DelistingReason",
    "DeliveryType",
    "DistributionPolicy",
    "EnergyType",
    "EnumFamilySchema",
    "EnumVariantRecord",
    "EquityType",
    "ExchangeCode",
    "ExchangeRecord",
    "ExecutionDisposition",
    "ExecutionInstruction",
    "ExecutionType",
    "ExerciseEventType",
    "ExoticOptionFeature",
    "FXSubType",
    "FXTenor",
    "FactorGroup",
    "FailsReason",
    "FamaFrench3Factor",
    "FamaFrench5Factor",
    "FinancingType",
    "Frequency",
    "FundSubType",
    "FundType",
    "FutureAssetClass",
    "FutureMonthCode",
    "FutureSpreadLegType",
    "FutureSpreadSubType",
    "FutureUnderlyingType",
    "GiveUpType",
    "IdentifierType",
    "IndexWeightingMethod",
    "Industry",
    "IndustryGroup",
    "InstrumentType",
    "InventoryType",
    "LegRole",
    "LiquidityFlag",
    "LiquidityTerm",
    "ListingStatus",
    "LivestockType",
    "MICMarketCategory",
    "MarginType",
    "MarketState",
    "MarketStatusReason",
    "MarketType",
    "MetalsType",
    "MsciFactorModel",
    "MutualFundEndedness",
    "NettingType",
    "OptionExerciseType",
    "OptionType",
    "OrderCapacity",
    "OrderFlag",
    "OrderSide",
    "OrderStatus",
    "OrderType",
    "PayoffStyle",
    "PositionEffect",
    "PositionType",
    "PriceKind",
    "PriceNotation",
    "QuantityUnit",
    "QuoteCondition",
    "RateIndex",
    "RebalanceFrequency",
    "RedemptionFrequency",
    "RepoType",
    "ResetFrequency",
    "Sector",
    "SecurityStatus",
    "SecurityType",
    "SegmentType",
    "Seniority",
    "SettlementStatus",
    "SettlementType",
    "ShareClassHedging",
    "ShortSaleRestriction",
    "Side",
    "StrategyType",
    "StubType",
    "SubIndustry",
    "SwapLegType",
    "SwapType",
    "Symbology",
    "TenderOfferType",
    "TickDirection",
    "TickerNamespace",
    "TimeInForce",
    "TradeCondition",
    "TradingSession",
    "TradingSessionStatus",
    "TransactionIntent",
    "UnderlyingAssetClass",
    "VehicleWrapper",
    "VenueRegulatoryFlag",
    "VenueType",
    "__abi_version__",
    "abi_compatible",
    "abi_version",
    "assert_abi_compatible",
    "build_cfi",
    "build_cfi_from_classification",
    "country_currency",
    "currency_alias_records",
    "currency_countries",
    "currency_export_capsule",
    "currency_records",
    "enum_export_capsule",
    "enum_family_schemas",
    "enum_schema",
    "enum_schema_json",
    "enum_variant_records",
    "exchange_currency",
    "exchange_export_capsule",
    "exchange_record",
    "exchange_records",
    "exchange_records_by_country",
    "exchange_records_by_currency",
    "exchange_records_by_market_category",
    "exchange_records_by_market_category_type",
    "exchange_records_by_operating_mic",
    "exchange_records_by_parent_mic",
    "exchange_records_by_region",
    "exchange_records_by_regulatory_flag",
    "exchange_records_by_status",
    "family_variant_count",
    "ordinal_of",
    "parse_cfi",
    "to_frequency",
    "transaction_intent",
    "transaction_intent_records",
    "validate_cfi_classification",
    "validate_ordinal",
    "variant_name",
]
