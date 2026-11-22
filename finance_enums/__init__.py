"""Standard financial enumerations.

Variant names and structured currency metadata are stored in Rust. This module
reads those tables at import time, constructs Python ``IntEnum`` classes with
attached lookup methods, and re-exports the domain helpers from the cfi /
country / currency / exchange / schema / trading submodules.
"""

from __future__ import annotations

import os as _os
from pathlib import Path as _Path
from typing import TYPE_CHECKING, Any

_PREFIX = _Path(__file__).resolve().parent
# The extension links libfinance_enums from lib/; Windows does not search there by default.
if _os.name == "nt" and (_PREFIX / "lib").is_dir():
    _DLL_DIRECTORY = _os.add_dll_directory(str(_PREFIX / "lib"))

from . import _finance_enums as _rust_enums
from ._finance_enums import (
    __all_families__,
    abi_compatible,
    abi_version,
    assert_abi_compatible,
    currency_export_capsule,
    enum_export_capsule,
    family_ordinal_size,
    family_variant_count,
    ordinal_of,
    validate_ordinal,
    variant_name,
)
from .frequency import Frequency, to_frequency

if TYPE_CHECKING:
    # The families are built in Rust and installed below; the stub declares them for type checkers.
    from ._enum_types import *

__version__ = "0.8.0"

#: Semantic enum-data ABI version of the loaded native extension, as
#: ``(major, minor, patch)``. See the "ABI compatibility" section of the README.
__abi_version__ = abi_version()


def get_prefix() -> str:
    """The installed package directory, usable as a CMake prefix for libfinance_enums."""
    return str(_PREFIX)


def get_include() -> str:
    """The directory holding ``finance_enums/finance_enums.h``."""
    return str(_PREFIX / "include")


def get_library_dirs() -> list[str]:
    """Directories holding the bundled libfinance_enums shared library."""
    return [str(_PREFIX / "lib")]


def get_libraries() -> list[str]:
    """Link names for libfinance_enums, for ``-l`` or ``target_link_libraries``."""
    return ["finance_enums"]


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
    "BondType": {
        "ABS": "AssetBacked",
        "MBS": "MortgageBacked",
        "CDO": "CollateralizedDebtObligation",
    },
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
    "CreditRatingAgency": {
        "SP": "StandardAndPoors",
        "S&P": "StandardAndPoors",
        "DBRS": "DominionBondRatingService",
        "JCR": "JapanCreditRatingAgency",
        "KBRA": "KrollBondRatingAgency",
    },
    "DayCountConvention": {
        "ACT/360": "Actual360",
        "ACT/365F": "Actual365Fixed",
        "ACT/ACT ISDA": "ActualActualIsda",
        "ACT/ACT ICMA": "ActualActualIcma",
        "ACT/ACT AFB": "ActualActualAfb",
        "ACT/365L": "Actual365Leap",
        "ACT/364": "Actual364",
        "ACT/365.25": "Actual36525",
        "NL/360": "NoLeap360",
        "NL/365": "NoLeap365",
        "30E/360": "Thirty360European",
        "30E/360 ISDA": "Thirty360EuropeanIsda",
        "30E+/360": "Thirty360EuropeanPlus",
        "30U/360": "Thirty360UnitedStates",
        "30/360 PSA": "Thirty360PublicSecuritiesAssociation",
        "BUS/252": "Business252",
        "1/1": "OneOne",
    },
    "DeliveryType": {
        "DVP": "DeliveryVersusPayment",
        "FOP": "FreeOfPayment",
        "PVP": "PaymentVersusPayment",
    },
    "EnergyType": {"LNG": "LiquefiedNaturalGas"},
    "ForeignExchangeBenchmark": {
        "WMR": "WorldMarketsReuters",
        "BFIX": "Bloomberg",
        "ECB": "EuropeanCentralBank",
    },
    "ForeignExchangeProductType": {
        "NDF": "NonDeliverableForward",
        "NDS": "NonDeliverableSwap",
    },
    "FundType": {
        "ETF": "ExchangeTradedFund",
        "REIT": "RealEstateInvestmentTrust",
        "SICAV": "SocieteInvestissementCapitalVariable",
        "OEIC": "OpenEndedInvestmentCompany",
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
    "MoneyMarketInstrumentType": {
        "CP": "CommercialPaper",
        "CD": "CertificateOfDeposit",
        "ECP": "EuroCommercialPaper",
        "MTN": "MediumTermNote",
    },
    "PriceKind": {"VWAP": "VolumeWeightedAveragePrice"},
    "RateIndex": {
        "SOFR": "SecuredOvernightFinancingRate",
        "FedFunds": "EffectiveFederalFundsRate",
        "EFFR": "EffectiveFederalFundsRate",
        "ESTR": "EuroShortTermRate",
        "SONIA": "SterlingOvernightIndexAverage",
        "EURIBOR": "EuroInterbankOfferedRate",
        "TONAR": "TokyoOvernightAverageRate",
        "SARON": "SwissAverageRateOvernight",
        "CPI": "ConsumerPriceIndex",
    },
    "RestructuringClause": {
        "XR": "NoRestructuring",
        "CR": "FullRestructuring",
        "MR": "ModifiedRestructuring",
        "MM": "ModifiedModifiedRestructuring",
    },
    "ShortSaleRestriction": {"RegSHOPriceTest": "AlternativeUptickRule"},
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
}


#: Native ``IntEnum`` classes generated in Rust, keyed by family name.
_int_enums = _rust_enums.int_enums

# ``Symbology`` is the acronym spelling of ``IdentifierType``, aligned by ordinal.
_ENUM_ACRONYM_ALIASES["IdentifierType"] = {
    acronym.name: full.name for acronym, full in zip(_int_enums.Symbology, _int_enums.IdentifierType, strict=True) if acronym.name != full.name
}


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
    "AssetBackedCollateralType",
    "AuctionType",
    "AveragingMethod",
    "BarrierType",
    "BenchmarkType",
    "BondType",
    "BookType",
    "BorrowType",
    "BusinessDayConvention",
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
    "CountryCodeAlpha2",
    "CountryCodeAlpha3",
    "CouponType",
    "CreditDefaultSwapTransactionType",
    "CreditEventType",
    "CreditQuality",
    "CreditRatingAgency",
    "CreditRatingOutlook",
    "CrossType",
    "Currency",
    "CurrencyAliasRecord",
    "CurrencyRecord",
    "CurrencyRole",
    "DayCountConvention",
    "DebtGuaranteeType",
    "DelistingReason",
    "DeliveryType",
    "DistributionPolicy",
    "DurationType",
    "EnergyType",
    "EnumFamilySchema",
    "EnumVariantRecord",
    "EquityType",
    "ExchangeCode",
    "ExchangeRecord",
    "ExecutionInstruction",
    "ExecutionType",
    "ExerciseEventType",
    "ExoticOptionFeature",
    "FactorGroup",
    "FamaFrenchFactor",
    "FinancingType",
    "ForeignExchangeAtTheMoneyConvention",
    "ForeignExchangeBenchmark",
    "ForeignExchangeDeltaConvention",
    "ForeignExchangeProductType",
    "ForeignExchangeQuoteBasis",
    "ForeignExchangeTenor",
    "ForeignExchangeVolatilityQuoteType",
    "Frequency",
    "FundSubType",
    "FundType",
    "FutureAssetClass",
    "FutureMonthCode",
    "FutureSpreadLegType",
    "FutureSpreadSubType",
    "GiveUpType",
    "IdentifierType",
    "IndexWeightingMethod",
    "Industry",
    "IndustryGroup",
    "InstrumentType",
    "InterestRateProductType",
    "InterestRateSwapType",
    "InventoryType",
    "IssuerType",
    "LegRole",
    "LiquidityFlag",
    "ListingStatus",
    "LivestockType",
    "MarginType",
    "MarketCategory",
    "MarketState",
    "MarketStatusReason",
    "MarketType",
    "MetalType",
    "MoneyMarketInstrumentType",
    "MutualFundEndedness",
    "NettingType",
    "ObligationCategory",
    "ObligationCharacteristic",
    "OptionExerciseType",
    "OptionPremiumQuoteBasis",
    "OptionStrikeQuoteBasis",
    "OptionType",
    "OrderCapacity",
    "OrderSide",
    "OrderStatus",
    "OrderType",
    "OvernightAccrualMethod",
    "PayoffStyle",
    "PayoutTiming",
    "PeriodTiming",
    "PeriodUnit",
    "PositionEffect",
    "PositionType",
    "PriceIndexCalculationMethod",
    "PriceKind",
    "PriceNotation",
    "QuantityUnit",
    "QuoteCondition",
    "RateIndex",
    "RedemptionFeature",
    "RepoType",
    "RestructuringClause",
    "RollConvention",
    "ScheduleFrequency",
    "Sector",
    "SecurityForm",
    "SecurityStatus",
    "SecurityType",
    "SegmentType",
    "Seniority",
    "SettlementFailReason",
    "SettlementStatus",
    "SettlementType",
    "ShareClassHedging",
    "ShortSaleRestriction",
    "Side",
    "StrategyType",
    "StubType",
    "StyleFactor",
    "SubIndustry",
    "SwapLegType",
    "SwapType",
    "SwaptionCashSettlementMethod",
    "Symbology",
    "TenderOfferType",
    "TickDirection",
    "TickerNamespace",
    "TimeInForce",
    "TouchType",
    "TradeCondition",
    "TradingPhase",
    "TradingSession",
    "TransactionIntent",
    "UnderlyingAssetClass",
    "VenueRegulatoryFlag",
    "VenueType",
    "YieldType",
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
    "family_ordinal_size",
    "family_variant_count",
    "get_include",
    "get_libraries",
    "get_library_dirs",
    "get_prefix",
    "ordinal_of",
    "parse_cfi",
    "to_frequency",
    "transaction_intent",
    "transaction_intent_records",
    "validate_cfi_classification",
    "validate_ordinal",
    "variant_name",
]
