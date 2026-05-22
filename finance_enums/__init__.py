"""Standard financial enumerations.

Variant names and structured currency metadata are stored in Rust.
This module reads those tables at import time and constructs Python ``Enum``
classes with attached lookup methods.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum
from typing import Any

from . import finance_enums as _rust_enums
from .finance_enums import (
    account_type_variants,
    aggressor_side_variants,
    agriculture_type_variants,
    amortization_type_variants,
    auction_type_variants,
    averaging_method_variants,
    barrier_type_variants,
    bond_type_variants,
    book_type_variants,
    borrow_type_variants,
    collateral_type_variants,
    commodity_type_variants,
    compounding_method_variants,
    contract_style_variants,
    contract_unit_variants,
    corporate_action_type_variants,
    country_code3_variants,
    country_code_variants,
    country_names,
    coupon_frequency_variants,
    coupon_type_variants,
    cross_type_variants,
    currency_alias_records as _currency_alias_records_raw,
    currency_aliases,
    currency_export_capsule,
    currency_names,
    currency_records as _currency_records_raw,
    currency_role_variants,
    currency_variants,
    day_count_convention_variants,
    delisting_reason_variants,
    delivery_type_variants,
    distribution_policy_variants,
    energy_type_variants,
    equity_type_variants,
    exchange_code_variants,
    exchange_records_raw as _exchange_records_raw,
    exec_type_variants,
    execution_instruction_variants,
    exercise_event_type_variants,
    exotic_option_feature_variants,
    financing_type_variants,
    fund_subtype_variants,
    fund_type_variants,
    future_delivery_type_variants,
    future_type_variants,
    identifier_type_variants,
    industry_group_variants,
    industry_variants,
    instrument_type_variants,
    inventory_type_variants,
    leg_role_variants,
    liquidity_flag_variants,
    liquidity_term_variants,
    listing_status_variants,
    margin_type_variants,
    market_state_variants,
    market_status_reason_variants,
    market_type_variants,
    metals_type_variants,
    mic_market_category_variants,
    mutual_fund_endedness_variants,
    netting_type_variants,
    open_close_variants,
    option_exercise_type_variants,
    option_type_variants,
    order_capacity_variants,
    order_flag_variants,
    order_status_variants,
    order_type_variants,
    payoff_style_variants,
    perpetual_future_type_variants,
    position_effect_variants,
    position_type_variants,
    price_notation_variants,
    price_type_variants,
    quantity_unit_variants,
    quote_condition_variants,
    rate_index_variants,
    redemption_frequency_variants,
    repo_type_variants,
    reset_frequency_variants,
    sector_variants,
    security_status_variants,
    security_type_variants,
    segment_type_variants,
    seniority_variants,
    settlement_type_variants,
    share_class_hedging_variants,
    short_sale_restriction_variants,
    side_variants,
    strategy_type_variants,
    stub_type_variants,
    sub_industry_variants,
    swap_leg_type_variants,
    swap_type_variants,
    tender_offer_type_variants,
    ticker_namespace_variants,
    time_in_force_variants,
    trade_condition_variants,
    trading_session_variants,
    trading_type_variants,
    underlying_asset_class_variants,
    vehicle_wrapper_variants,
    venue_regulatory_flag_variants,
    venue_type_variants,
)
from .frequency import Frequency, to_frequency  # noqa: F401

__version__ = "0.4.0"

_exchange_records_typed = getattr(_rust_enums, "exchange_records_typed", None)
_exchange_record_typed = getattr(_rust_enums, "exchange_record_typed", None)


@dataclass(frozen=True)
class CurrencyRecord:
    code: str
    display_name: str
    is_iso4217: bool


@dataclass(frozen=True)
class CurrencyAliasRecord:
    alias: str
    canonical_code: str


@dataclass(frozen=True)
class ExchangeRecord:
    mic: str
    market_name: str
    legal_entity_name: str
    operating_mic: str
    parent_mic: str
    market_category_code: str
    acronym: str
    iso_country_code: str
    city: str
    website: str
    status: str
    region: str
    subregion: str
    is_segment: bool
    is_official: bool

    def market_category(self) -> MICMarketCategory | None:
        return _MARKET_CATEGORY_CODE_TO_TYPE.get(self.market_category_code)

    def regulatory_flags(self) -> tuple[VenueRegulatoryFlag, ...]:
        market_category = self.market_category()
        if market_category is None:
            return ()
        return _MARKET_CATEGORY_TYPE_TO_FLAGS.get(market_category, ())

    def has_regulatory_flag(self, regulatory_flag: VenueRegulatoryFlag | str) -> bool:
        resolved_flag = _coerce_enum(VenueRegulatoryFlag, regulatory_flag, "regulatory_flag")
        return resolved_flag in self.regulatory_flags()


def _exchange_record_from_raw(record: list[str]) -> ExchangeRecord:
    return ExchangeRecord(
        mic=record[0],
        market_name=record[1],
        legal_entity_name=record[2],
        operating_mic=record[3],
        parent_mic=record[4],
        market_category_code=record[5],
        acronym=record[6],
        iso_country_code=record[7],
        city=record[8],
        website=record[9],
        status=record[10],
        region=record[11],
        subregion=record[12],
        is_segment=record[13] == "1",
        is_official=record[14] == "1",
    )


def _exchange_record_from_typed(record: Any) -> ExchangeRecord:
    return ExchangeRecord(
        mic=record.mic,
        market_name=record.market_name,
        legal_entity_name=record.legal_entity_name,
        operating_mic=record.operating_mic,
        parent_mic=record.parent_mic,
        market_category_code=record.market_category_code,
        acronym=record.acronym,
        iso_country_code=record.iso_country_code,
        city=record.city,
        website=record.website,
        status=record.status,
        region=record.region,
        subregion=record.subregion,
        is_segment=record.is_segment,
        is_official=record.is_official,
    )


def _make_str_enum(name: str, members: list[str], aliases: dict[str, str] | None = None) -> Any:
    """Build a string-valued ``Enum`` whose value equals its name."""

    cls = Enum(name, {m: m for m in members}, type=str)

    if aliases:
        # Override _missing_ to support the alias map.
        def _missing_(value):  # type: ignore[no-untyped-def]
            if isinstance(value, str) and value in aliases:
                return cls[aliases[value]]
            return None

        cls._missing_ = classmethod(lambda c, v: _missing_(v))  # type: ignore[assignment]

    cls.__str__ = lambda self: self.value  # type: ignore[assignment]
    return cls


MICMarketCategory = _make_str_enum("MICMarketCategory", mic_market_category_variants())
VenueRegulatoryFlag = _make_str_enum("VenueRegulatoryFlag", venue_regulatory_flag_variants())

_MARKET_CATEGORY_CODE_TO_TYPE = {
    "NSPD": MICMarketCategory.NotSpecified,
    "MLTF": MICMarketCategory.MultilateralTradingFacility,
    "SINT": MICMarketCategory.SystematicInternaliser,
    "RMKT": MICMarketCategory.RegulatedMarket,
    "ATSS": MICMarketCategory.AlternativeTradingSystem,
    "OTFS": MICMarketCategory.OrganizedTradingFacility,
    "OTHR": MICMarketCategory.Other,
    "SEFS": MICMarketCategory.SwapExecutionFacility,
    "RMOS": MICMarketCategory.RegulatedMarketOffBookSegment,
    "APPA": MICMarketCategory.ApprovedPublicationArrangement,
    "CASP": MICMarketCategory.CryptoAssetServiceProvider,
    "DCMS": MICMarketCategory.DesignatedContractMarket,
    "TRFS": MICMarketCategory.TradeReportingFacility,
    "IDQS": MICMarketCategory.InterDealerQuotationSystem,
}
_MARKET_CATEGORY_TYPE_TO_FLAGS = {
    MICMarketCategory.NotSpecified: (),
    MICMarketCategory.MultilateralTradingFacility: (VenueRegulatoryFlag.Multilateral,),
    MICMarketCategory.SystematicInternaliser: (VenueRegulatoryFlag.SystematicInternaliser,),
    MICMarketCategory.RegulatedMarket: (VenueRegulatoryFlag.RegulatedMarket,),
    MICMarketCategory.AlternativeTradingSystem: (VenueRegulatoryFlag.AlternativeTradingSystem,),
    MICMarketCategory.OrganizedTradingFacility: (VenueRegulatoryFlag.OrganizedTrading,),
    MICMarketCategory.Other: (),
    MICMarketCategory.SwapExecutionFacility: (VenueRegulatoryFlag.SwapExecution,),
    MICMarketCategory.RegulatedMarketOffBookSegment: (
        VenueRegulatoryFlag.RegulatedMarket,
        VenueRegulatoryFlag.OffBookSegment,
    ),
    MICMarketCategory.ApprovedPublicationArrangement: (VenueRegulatoryFlag.Publication,),
    MICMarketCategory.CryptoAssetServiceProvider: (VenueRegulatoryFlag.CryptoAssetServiceProvider,),
    MICMarketCategory.DesignatedContractMarket: (VenueRegulatoryFlag.DesignatedContractMarket,),
    MICMarketCategory.TradeReportingFacility: (VenueRegulatoryFlag.TradeReporting,),
    MICMarketCategory.InterDealerQuotationSystem: (VenueRegulatoryFlag.InterDealerQuotation,),
}


# --- Country -----------------------------------------------------------------

_country_codes = country_code_variants()
_country_codes3 = country_code3_variants()
_country_names = country_names()

CountryCode3 = _make_str_enum("CountryCode3", _country_codes3)
CountryCode = _make_str_enum("CountryCode", _country_codes)


def _country_code_country_name(self):
    return _country_names[_country_codes.index(self.value)]


def _country_code_code3(self):
    return CountryCode3[_country_codes3[_country_codes.index(self.value)]]


CountryCode.country_name = _country_code_country_name  # type: ignore[attr-defined]
CountryCode.code3 = _country_code_code3  # type: ignore[attr-defined]
CountryCode3.country_name = lambda self: _country_names[_country_codes3.index(self.value)]  # type: ignore[attr-defined]


# --- Currency ----------------------------------------------------------------

_currency_record_data = [CurrencyRecord(code, display_name, is_iso4217) for code, display_name, is_iso4217 in _currency_records_raw()]
_currency_alias_record_data = [CurrencyAliasRecord(alias, canonical_code) for alias, canonical_code in _currency_alias_records_raw()]
_currency_codes = [record.code for record in _currency_record_data]
_currency_by_code = {record.code: record for record in _currency_record_data}
_currency_aliases = {record.alias: record.canonical_code for record in _currency_alias_record_data if record.canonical_code in _currency_by_code}

Currency = _make_str_enum("Currency", _currency_codes, aliases=_currency_aliases)


def currency_records() -> list[CurrencyRecord]:
    return list(_currency_record_data)


def currency_alias_records() -> list[CurrencyAliasRecord]:
    return list(_currency_alias_record_data)


def _currency_currency_name(self):
    return _currency_by_code[self.value].display_name


def _currency_is_iso4217(self):
    return _currency_by_code[self.value].is_iso4217


def _currency_record(self):
    return _currency_by_code[self.value]


Currency.currency_name = _currency_currency_name  # type: ignore[attr-defined]
Currency.is_iso4217 = _currency_is_iso4217  # type: ignore[attr-defined]
Currency.record = _currency_record  # type: ignore[attr-defined]


# --- Exchange ----------------------------------------------------------------

if _exchange_records_typed is not None:
    _exchange_record_data = [_exchange_record_from_typed(record) for record in _exchange_records_typed()]
else:
    _exchange_record_data = [_exchange_record_from_raw(record) for record in _exchange_records_raw()]

_exchange_by_code = {record.mic: record for record in _exchange_record_data}
_exchange_by_country: dict[str, list[ExchangeRecord]] = {}
_exchange_by_operating_mic: dict[str, list[ExchangeRecord]] = {}
_exchange_by_parent_mic: dict[str, list[ExchangeRecord]] = {}
_exchange_by_status: dict[str, list[ExchangeRecord]] = {}
_exchange_by_region: dict[str, list[ExchangeRecord]] = {}
_exchange_by_market_category: dict[str, list[ExchangeRecord]] = {}
_exchange_by_market_category_type: dict[MICMarketCategory, list[ExchangeRecord]] = {}
_exchange_by_regulatory_flag: dict[VenueRegulatoryFlag, list[ExchangeRecord]] = {}

for record in _exchange_record_data:
    _exchange_by_country.setdefault(record.iso_country_code, []).append(record)
    if record.operating_mic:
        _exchange_by_operating_mic.setdefault(record.operating_mic, []).append(record)
    if record.parent_mic:
        _exchange_by_parent_mic.setdefault(record.parent_mic, []).append(record)
    if record.status:
        _exchange_by_status.setdefault(record.status, []).append(record)
    if record.region:
        _exchange_by_region.setdefault(record.region, []).append(record)
    if record.market_category_code:
        _exchange_by_market_category.setdefault(record.market_category_code, []).append(record)
        market_category = _MARKET_CATEGORY_CODE_TO_TYPE.get(record.market_category_code)
        if market_category is not None:
            _exchange_by_market_category_type.setdefault(market_category, []).append(record)
            for regulatory_flag in _MARKET_CATEGORY_TYPE_TO_FLAGS.get(market_category, ()):
                _exchange_by_regulatory_flag.setdefault(regulatory_flag, []).append(record)


def exchange_records() -> list[ExchangeRecord]:
    return list(_exchange_record_data)


def exchange_record(code: ExchangeCode | str) -> ExchangeRecord | None:
    normalized = code.value if isinstance(code, ExchangeCode) else str(code).strip().upper()

    if _exchange_record_typed is not None:
        typed_record = _exchange_record_typed(normalized)
        if typed_record is not None:
            return _exchange_record_from_typed(typed_record)

    return _exchange_by_code.get(normalized)


def exchange_records_by_country(country_code: CountryCode | str) -> list[ExchangeRecord]:
    normalized = country_code.value if isinstance(country_code, CountryCode) else str(country_code).strip().upper()
    return list(_exchange_by_country.get(normalized, []))


def exchange_records_by_operating_mic(operating_mic: ExchangeCode | str) -> list[ExchangeRecord]:
    normalized = operating_mic.value if isinstance(operating_mic, ExchangeCode) else str(operating_mic).strip().upper()
    return list(_exchange_by_operating_mic.get(normalized, []))


def exchange_records_by_parent_mic(parent_mic: ExchangeCode | str) -> list[ExchangeRecord]:
    normalized = parent_mic.value if isinstance(parent_mic, ExchangeCode) else str(parent_mic).strip().upper()
    return list(_exchange_by_parent_mic.get(normalized, []))


def exchange_records_by_status(status: str) -> list[ExchangeRecord]:
    normalized = str(status).strip().upper()
    return list(_exchange_by_status.get(normalized, []))


def exchange_records_by_region(region: str) -> list[ExchangeRecord]:
    normalized = str(region).strip()
    return list(_exchange_by_region.get(normalized, []))


def exchange_records_by_market_category(market_category_code: str) -> list[ExchangeRecord]:
    normalized = str(market_category_code).strip().upper()
    return list(_exchange_by_market_category.get(normalized, []))


def exchange_records_by_market_category_type(market_category: MICMarketCategory | str) -> list[ExchangeRecord]:
    resolved_market_category = _coerce_enum(MICMarketCategory, market_category, "market_category")
    return list(_exchange_by_market_category_type.get(resolved_market_category, []))


def exchange_records_by_regulatory_flag(regulatory_flag: VenueRegulatoryFlag | str) -> list[ExchangeRecord]:
    resolved_regulatory_flag = _coerce_enum(VenueRegulatoryFlag, regulatory_flag, "regulatory_flag")
    return list(_exchange_by_regulatory_flag.get(resolved_regulatory_flag, []))


ExchangeCode = _make_str_enum("ExchangeCode", exchange_code_variants())


def _exchange_record(self):
    return _exchange_by_code[self.value]


def _exchange_market_name(self):
    return _exchange_by_code[self.value].market_name


def _exchange_market_category(self):
    return _exchange_by_code[self.value].market_category()


def _exchange_regulatory_flags(self):
    return _exchange_by_code[self.value].regulatory_flags()


def _exchange_has_regulatory_flag(self, regulatory_flag):  # type: ignore[no-untyped-def]
    return _exchange_by_code[self.value].has_regulatory_flag(regulatory_flag)


ExchangeCode.record = _exchange_record  # type: ignore[attr-defined]
ExchangeCode.market_name = _exchange_market_name  # type: ignore[attr-defined]
ExchangeCode.market_category = _exchange_market_category  # type: ignore[attr-defined]
ExchangeCode.regulatory_flags = _exchange_regulatory_flags  # type: ignore[attr-defined]
ExchangeCode.has_regulatory_flag = _exchange_has_regulatory_flag  # type: ignore[attr-defined]


# --- Sector taxonomy ---------------------------------------------------------

Sector = _make_str_enum("Sector", sector_variants())
IndustryGroup = _make_str_enum("IndustryGroup", industry_group_variants())
Industry = _make_str_enum("Industry", industry_variants())
SubIndustry = _make_str_enum("SubIndustry", sub_industry_variants())


# --- Security & instrument ---------------------------------------------------

SecurityType = _make_str_enum("SecurityType", security_type_variants())
InstrumentType = _make_str_enum("InstrumentType", instrument_type_variants())
EquityType = _make_str_enum("EquityType", equity_type_variants())
OptionType = _make_str_enum("OptionType", option_type_variants())
OptionExerciseType = _make_str_enum("OptionExerciseType", option_exercise_type_variants())
BondType = _make_str_enum("BondType", bond_type_variants())
CommodityType = _make_str_enum("CommodityType", commodity_type_variants())
EnergyType = _make_str_enum("EnergyType", energy_type_variants())
MetalsType = _make_str_enum("MetalsType", metals_type_variants())
AgricultureType = _make_str_enum("AgricultureType", agriculture_type_variants())
FundType = _make_str_enum("FundType", fund_type_variants())
FundSubType = _make_str_enum("FundSubType", fund_subtype_variants())
VenueType = _make_str_enum("VenueType", venue_type_variants())
MarketType = _make_str_enum("MarketType", market_type_variants())
TradingSession = _make_str_enum("TradingSession", trading_session_variants())
MarketState = _make_str_enum("MarketState", market_state_variants())
AuctionType = _make_str_enum("AuctionType", auction_type_variants())
SegmentType = _make_str_enum("SegmentType", segment_type_variants())
MarketStatusReason = _make_str_enum("MarketStatusReason", market_status_reason_variants())
IdentifierType = _make_str_enum("IdentifierType", identifier_type_variants())
TickerNamespace = _make_str_enum("TickerNamespace", ticker_namespace_variants())
PriceNotation = _make_str_enum("PriceNotation", price_notation_variants())
QuantityUnit = _make_str_enum("QuantityUnit", quantity_unit_variants())
CurrencyRole = _make_str_enum("CurrencyRole", currency_role_variants())
CouponType = _make_str_enum("CouponType", coupon_type_variants())
CouponFrequency = _make_str_enum("CouponFrequency", coupon_frequency_variants())
DayCountConvention = _make_str_enum("DayCountConvention", day_count_convention_variants())
AmortizationType = _make_str_enum("AmortizationType", amortization_type_variants())
Seniority = _make_str_enum("Seniority", seniority_variants())
CollateralType = _make_str_enum("CollateralType", collateral_type_variants())
MarginType = _make_str_enum("MarginType", margin_type_variants())
BorrowType = _make_str_enum("BorrowType", borrow_type_variants())
RepoType = _make_str_enum("RepoType", repo_type_variants())
AccountType = _make_str_enum("AccountType", account_type_variants())
BookType = _make_str_enum("BookType", book_type_variants())
PositionType = _make_str_enum("PositionType", position_type_variants())
InventoryType = _make_str_enum("InventoryType", inventory_type_variants())
StrategyType = _make_str_enum("StrategyType", strategy_type_variants())
NettingType = _make_str_enum("NettingType", netting_type_variants())
VehicleWrapper = _make_str_enum("VehicleWrapper", vehicle_wrapper_variants())
DistributionPolicy = _make_str_enum("DistributionPolicy", distribution_policy_variants())
ShareClassHedging = _make_str_enum("ShareClassHedging", share_class_hedging_variants())
LiquidityTerm = _make_str_enum("LiquidityTerm", liquidity_term_variants())
RedemptionFrequency = _make_str_enum("RedemptionFrequency", redemption_frequency_variants())
FinancingType = _make_str_enum("FinancingType", financing_type_variants())
MutualFundEndedness = _make_str_enum("MutualFundEndedness", mutual_fund_endedness_variants())
FutureType = _make_str_enum("FutureType", future_type_variants())
FutureDeliveryType = _make_str_enum("FutureDeliveryType", future_delivery_type_variants())
SettlementType = _make_str_enum("SettlementType", settlement_type_variants())
DeliveryType = _make_str_enum("DeliveryType", delivery_type_variants())
UnderlyingAssetClass = _make_str_enum("UnderlyingAssetClass", underlying_asset_class_variants())
ContractStyle = _make_str_enum("ContractStyle", contract_style_variants())
PayoffStyle = _make_str_enum("PayoffStyle", payoff_style_variants())
ContractUnit = _make_str_enum("ContractUnit", contract_unit_variants())
SwapLegType = _make_str_enum("SwapLegType", swap_leg_type_variants())
RateIndex = _make_str_enum("RateIndex", rate_index_variants())
ResetFrequency = _make_str_enum("ResetFrequency", reset_frequency_variants())
CompoundingMethod = _make_str_enum("CompoundingMethod", compounding_method_variants())
StubType = _make_str_enum("StubType", stub_type_variants())
BarrierType = _make_str_enum("BarrierType", barrier_type_variants())
AveragingMethod = _make_str_enum("AveragingMethod", averaging_method_variants())
ExoticOptionFeature = _make_str_enum("ExoticOptionFeature", exotic_option_feature_variants())
CorporateActionType = _make_str_enum("CorporateActionType", corporate_action_type_variants())
ListingStatus = _make_str_enum("ListingStatus", listing_status_variants())
SecurityStatus = _make_str_enum("SecurityStatus", security_status_variants())
ExerciseEventType = _make_str_enum("ExerciseEventType", exercise_event_type_variants())
TenderOfferType = _make_str_enum("TenderOfferType", tender_offer_type_variants())
DelistingReason = _make_str_enum("DelistingReason", delisting_reason_variants())
LegRole = _make_str_enum("LegRole", leg_role_variants())
PerpetualFutureType = _make_str_enum("PerpetualFutureType", perpetual_future_type_variants())
SwapType = _make_str_enum("SwapType", swap_type_variants())


# --- Trading -----------------------------------------------------------------

OrderType = _make_str_enum("OrderType", order_type_variants())
OrderStatus = _make_str_enum("OrderStatus", order_status_variants())
ExecType = _make_str_enum("ExecType", exec_type_variants())
ExecutionInstruction = _make_str_enum("ExecutionInstruction", execution_instruction_variants())
LiquidityFlag = _make_str_enum("LiquidityFlag", liquidity_flag_variants())
PositionEffect = _make_str_enum("PositionEffect", position_effect_variants())
OpenClose = _make_str_enum("OpenClose", open_close_variants())
OrderCapacity = _make_str_enum("OrderCapacity", order_capacity_variants())
ShortSaleRestriction = _make_str_enum("ShortSaleRestriction", short_sale_restriction_variants())
QuoteCondition = _make_str_enum("QuoteCondition", quote_condition_variants())
TradeCondition = _make_str_enum("TradeCondition", trade_condition_variants())
AggressorSide = _make_str_enum("AggressorSide", aggressor_side_variants())
CrossType = _make_str_enum("CrossType", cross_type_variants())
PriceType = _make_str_enum("PriceType", price_type_variants())
Side = _make_str_enum("Side", side_variants())
OrderFlag = _make_str_enum("OrderFlag", order_flag_variants())
TimeInForce = _make_str_enum("TimeInForce", time_in_force_variants())
TradingType = _make_str_enum("TradingType", trading_type_variants())


# --- CFI ---------------------------------------------------------------------


@dataclass(frozen=True)
class CFIClassification:
    code: str
    category: str
    group: str
    attributes: tuple[str, str, str, str]
    security_type: SecurityType | None
    instrument_type: InstrumentType | None
    equity_type: EquityType | None = None
    option_type: OptionType | None = None
    option_exercise_type: OptionExerciseType | None = None
    bond_type: BondType | None = None
    fund_type: FundType | None = None
    mutual_fund_endedness: MutualFundEndedness | None = None
    future_type: FutureType | None = None
    future_delivery_type: FutureDeliveryType | None = None
    settlement_type: SettlementType | None = None
    delivery_type: DeliveryType | None = None
    underlying_asset_class: UnderlyingAssetClass | None = None
    contract_style: ContractStyle | None = None
    perpetual_future_type: PerpetualFutureType | None = None
    swap_type: SwapType | None = None
    financing_type: FinancingType | None = None
    commodity_type: CommodityType | None = None
    underlying_security_type: SecurityType | None = None


_EQUITY_GROUP_TO_TYPE = {
    "S": EquityType.Shares,
    "P": EquityType.PreferredShares,
    "R": EquityType.PreferredShares,
    "C": EquityType.ConvertibleShares,
    "F": EquityType.PreferredConvertibleShares,
    "V": EquityType.PreferredConvertibleShares,
    "D": EquityType.DepositoryReceipt,
}
_EQUITY_TYPE_TO_GROUP = {
    EquityType.Shares: "S",
    EquityType.PreferredShares: "P",
    EquityType.ConvertibleShares: "C",
    EquityType.PreferredConvertibleShares: "F",
    EquityType.DepositoryReceipt: "D",
}
_OPTION_GROUP_TO_TYPE = {"C": OptionType.Call, "P": OptionType.Put}
_OPTION_TYPE_TO_GROUP = {value: key for key, value in _OPTION_GROUP_TO_TYPE.items()}
_OPTION_EXERCISE_TO_ATTR = {
    OptionExerciseType.American: "A",
    OptionExerciseType.European: "E",
    OptionExerciseType.Bermudan: "B",
}
_OPTION_ATTR_TO_EXERCISE = {value: key for key, value in _OPTION_EXERCISE_TO_ATTR.items()}
_SETTLEMENT_TYPE_TO_DELIVERY_TYPE = {
    SettlementType.Physical: DeliveryType.Physical,
    SettlementType.Cash: DeliveryType.Cash,
    SettlementType.NonDeliverable: DeliveryType.NonDeliverable,
    SettlementType.ElectAtExercise: DeliveryType.ElectAtExercise,
}
_DELIVERY_TYPE_TO_SETTLEMENT_TYPE = {value: key for key, value in _SETTLEMENT_TYPE_TO_DELIVERY_TYPE.items()}
_FUTURE_DELIVERY_TYPE_TO_DELIVERY_TYPE = {
    FutureDeliveryType.Physical: DeliveryType.Physical,
    FutureDeliveryType.Cash: DeliveryType.Cash,
}
_DELIVERY_TYPE_TO_FUTURE_DELIVERY_TYPE = {value: key for key, value in _FUTURE_DELIVERY_TYPE_TO_DELIVERY_TYPE.items()}
_DERIVATIVE_DELIVERY_ATTR_TO_TYPE = {
    "P": DeliveryType.Physical,
    "C": DeliveryType.Cash,
    "N": DeliveryType.NonDeliverable,
    "E": DeliveryType.ElectAtExercise,
}
_DERIVATIVE_DELIVERY_TYPE_TO_ATTR = {value: key for key, value in _DERIVATIVE_DELIVERY_ATTR_TO_TYPE.items()}
_FINANCING_DELIVERY_ATTR_TO_TYPE = {
    "P": DeliveryType.Physical,
    "C": DeliveryType.Cash,
    "N": DeliveryType.NonDeliverable,
    "D": DeliveryType.DeliveryVersusPayment,
    "F": DeliveryType.FreeOfPayment,
    "H": DeliveryType.HoldInCustody,
    "T": DeliveryType.TriParty,
}
_FINANCING_DELIVERY_TYPE_TO_ATTR = {value: key for key, value in _FINANCING_DELIVERY_ATTR_TO_TYPE.items()}
_CONTRACT_STYLE_TO_ATTR = {
    ContractStyle.Standardized: "S",
    ContractStyle.NonStandardized: "N",
}
_CONTRACT_STYLE_ATTR_TO_STYLE = {value: key for key, value in _CONTRACT_STYLE_TO_ATTR.items()}
_OPTION_ASSET_ATTR_TO_CLASS = {
    "B": UnderlyingAssetClass.Basket,
    "S": UnderlyingAssetClass.Equity,
    "D": UnderlyingAssetClass.Debt,
    "T": UnderlyingAssetClass.Commodity,
    "C": UnderlyingAssetClass.Currency,
    "I": UnderlyingAssetClass.Index,
    "O": UnderlyingAssetClass.Option,
    "F": UnderlyingAssetClass.Future,
    "W": UnderlyingAssetClass.Swap,
    "N": UnderlyingAssetClass.InterestRate,
    "M": UnderlyingAssetClass.Other,
}
_OPTION_CLASS_TO_ASSET_ATTR = {value: key for key, value in _OPTION_ASSET_ATTR_TO_CLASS.items()}
_FUND_GROUP_TO_TYPE = {
    "E": FundType.ETF,
    "B": FundType.REIT,
    "I": FundType.MutualFund,
}
_FUTURE_GROUP_TO_TYPE = {"F": FutureType.Financial, "C": FutureType.Commodity}
_FUTURE_TYPE_TO_GROUP = {value: key for key, value in _FUTURE_GROUP_TO_TYPE.items()}
_FINANCIAL_FUTURE_ATTR_TO_CLASS = {
    "B": UnderlyingAssetClass.Basket,
    "S": UnderlyingAssetClass.Equity,
    "D": UnderlyingAssetClass.Debt,
    "C": UnderlyingAssetClass.Currency,
    "I": UnderlyingAssetClass.Index,
    "O": UnderlyingAssetClass.Option,
    "F": UnderlyingAssetClass.Future,
    "W": UnderlyingAssetClass.Swap,
    "N": UnderlyingAssetClass.InterestRate,
    "V": UnderlyingAssetClass.StockDividend,
    "M": UnderlyingAssetClass.Other,
}
_FINANCIAL_FUTURE_CLASS_TO_ATTR = {value: key for key, value in _FINANCIAL_FUTURE_ATTR_TO_CLASS.items()}
_COMMODITY_FUTURE_ATTR_TO_CLASS = {
    "E": UnderlyingAssetClass.ExtractionResources,
    "A": UnderlyingAssetClass.Agriculture,
    "I": UnderlyingAssetClass.IndustrialProducts,
    "S": UnderlyingAssetClass.Services,
    "N": UnderlyingAssetClass.Environmental,
    "P": UnderlyingAssetClass.PolypropyleneProducts,
    "H": UnderlyingAssetClass.GeneratedResources,
    "M": UnderlyingAssetClass.Other,
}
_COMMODITY_FUTURE_CLASS_TO_ATTR = {value: key for key, value in _COMMODITY_FUTURE_ATTR_TO_CLASS.items()}
_COMMODITY_FUTURE_CLASS_TO_TYPE = {
    UnderlyingAssetClass.Agriculture: CommodityType.Agriculture,
}
_PERPETUAL_FUTURE_GROUP_TO_TYPE = {"F": PerpetualFutureType.Financial, "C": PerpetualFutureType.Commodity}
_PERPETUAL_FUTURE_TYPE_TO_GROUP = {value: key for key, value in _PERPETUAL_FUTURE_GROUP_TO_TYPE.items()}
_FUTURE_DELIVERY_TO_ATTR = {
    FutureDeliveryType.Physical: "P",
    FutureDeliveryType.Cash: "C",
}
_FUTURE_ATTR_TO_DELIVERY = {value: key for key, value in _FUTURE_DELIVERY_TO_ATTR.items()}
_SWAP_GROUP_TO_TYPE = {
    "R": SwapType.Rates,
    "T": SwapType.Commodities,
    "E": SwapType.Equity,
    "C": SwapType.Credit,
    "F": SwapType.ForeignExchange,
    "M": SwapType.Other,
}
_SWAP_TYPE_TO_GROUP = {value: key for key, value in _SWAP_GROUP_TO_TYPE.items()}
_SPOT_COMMODITY_ATTR_TO_TYPE = {
    "A": CommodityType.Agriculture,
    "J": CommodityType.Energy,
    "K": CommodityType.Metals,
}
_COMMODITY_TYPE_TO_SPOT_ATTR = {value: key for key, value in _SPOT_COMMODITY_ATTR_TO_TYPE.items()}
_FINANCING_GROUP_TO_TYPE = {
    "L": FinancingType.LoanLease,
    "R": FinancingType.RepurchaseAgreement,
    "S": FinancingType.SecuritiesLending,
}
_FINANCING_TYPE_TO_GROUP = {value: key for key, value in _FINANCING_GROUP_TO_TYPE.items()}
_COMPLEX_OPTION_GROUP_TO_ASSET_CLASS = {
    "R": UnderlyingAssetClass.InterestRate,
    "T": UnderlyingAssetClass.Commodity,
    "E": UnderlyingAssetClass.Equity,
    "C": UnderlyingAssetClass.Credit,
    "F": UnderlyingAssetClass.Currency,
    "M": UnderlyingAssetClass.Other,
}
_ASSET_CLASS_TO_COMPLEX_OPTION_GROUP = {value: key for key, value in _COMPLEX_OPTION_GROUP_TO_ASSET_CLASS.items()}
_FORWARD_GROUP_TO_ASSET_CLASS = {
    "E": UnderlyingAssetClass.Equity,
    "F": UnderlyingAssetClass.Currency,
    "C": UnderlyingAssetClass.Credit,
    "R": UnderlyingAssetClass.InterestRate,
    "T": UnderlyingAssetClass.Commodity,
}
_ASSET_CLASS_TO_FORWARD_GROUP = {value: key for key, value in _FORWARD_GROUP_TO_ASSET_CLASS.items()}
_STRATEGY_GROUP_TO_ASSET_CLASS = {
    "R": UnderlyingAssetClass.InterestRate,
    "T": UnderlyingAssetClass.Commodity,
    "E": UnderlyingAssetClass.Equity,
    "C": UnderlyingAssetClass.Credit,
    "F": UnderlyingAssetClass.Currency,
    "Y": UnderlyingAssetClass.MixedAssets,
    "M": UnderlyingAssetClass.Other,
}
_ASSET_CLASS_TO_STRATEGY_GROUP = {value: key for key, value in _STRATEGY_GROUP_TO_ASSET_CLASS.items()}
_ASSET_CLASS_TO_SECURITY_TYPE = {
    UnderlyingAssetClass.Equity: SecurityType.Equity,
    UnderlyingAssetClass.Currency: SecurityType.Currency,
    UnderlyingAssetClass.Commodity: SecurityType.Commodity,
    UnderlyingAssetClass.Debt: SecurityType.Bond,
    UnderlyingAssetClass.Index: SecurityType.Index,
    UnderlyingAssetClass.Option: SecurityType.Option,
    UnderlyingAssetClass.Future: SecurityType.Future,
    UnderlyingAssetClass.Swap: SecurityType.Swap,
}
_SECURITY_TYPE_TO_ASSET_CLASS = {value: key for key, value in _ASSET_CLASS_TO_SECURITY_TYPE.items()}


def _coerce_enum(enum_type, value, field_name: str):  # type: ignore[no-untyped-def]
    if value is None or isinstance(value, enum_type):
        return value
    try:
        return enum_type(value)
    except ValueError as exc:
        raise ValueError(f"invalid {field_name}: {value!r}") from exc


def _normalize_cfi_attributes(attributes: str | tuple[str, str, str, str] | None) -> tuple[str, str, str, str]:
    if attributes is None:
        return ("X", "X", "X", "X")
    if isinstance(attributes, str):
        normalized = attributes.strip().upper()
        if len(normalized) != 4:
            raise ValueError("CFI attributes must be exactly 4 characters")
        return tuple(normalized)  # type: ignore[return-value]
    if len(attributes) != 4:
        raise ValueError("CFI attributes must contain exactly 4 characters")
    return tuple(str(value).strip().upper() for value in attributes)


def _resolve_underlying_asset_class(
    underlying_asset_class: UnderlyingAssetClass | None,
    underlying_security_type: SecurityType | None,
) -> UnderlyingAssetClass | None:
    if underlying_security_type is None:
        return underlying_asset_class

    mapped_asset_class = _SECURITY_TYPE_TO_ASSET_CLASS.get(underlying_security_type)
    if mapped_asset_class is None:
        raise NotImplementedError(
            f"derivative underlying asset-class resolution is not implemented for security type {underlying_security_type.value}"
        )
    if underlying_asset_class is not None and underlying_asset_class != mapped_asset_class:
        raise ValueError("underlying_asset_class and underlying_security_type refer to different underliers")
    return mapped_asset_class


def _resolve_delivery_fields(
    settlement_type: SettlementType | None,
    delivery_type: DeliveryType | None,
    future_delivery_type: FutureDeliveryType | None,
) -> tuple[SettlementType | None, DeliveryType | None, FutureDeliveryType | None]:
    resolved_delivery_type = delivery_type

    if settlement_type is not None:
        settlement_delivery_type = _SETTLEMENT_TYPE_TO_DELIVERY_TYPE[settlement_type]
        if resolved_delivery_type is not None and resolved_delivery_type != settlement_delivery_type:
            raise ValueError("settlement_type and delivery_type refer to different delivery semantics")
        resolved_delivery_type = settlement_delivery_type

    if future_delivery_type is not None:
        future_delivery = _FUTURE_DELIVERY_TYPE_TO_DELIVERY_TYPE[future_delivery_type]
        if resolved_delivery_type is not None and resolved_delivery_type != future_delivery:
            raise ValueError("future_delivery_type and settlement_type or delivery_type refer to different delivery semantics")
        resolved_delivery_type = future_delivery

    if resolved_delivery_type is None:
        return settlement_type, None, future_delivery_type

    return (
        _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(resolved_delivery_type),
        resolved_delivery_type,
        _DELIVERY_TYPE_TO_FUTURE_DELIVERY_TYPE.get(resolved_delivery_type),
    )


def parse_cfi(code: str) -> CFIClassification:
    normalized = code.strip().upper()
    if len(normalized) != 6:
        raise ValueError("CFI codes must be exactly 6 characters")

    category = normalized[0]
    group = normalized[1]
    attributes = (normalized[2], normalized[3], normalized[4], normalized[5])

    security_type = None
    instrument_type = None
    equity_type = None
    option_type = None
    option_exercise_type = None
    bond_type = None
    fund_type = None
    mutual_fund_endedness = None
    future_type = None
    future_delivery_type = None
    settlement_type = None
    delivery_type = None
    underlying_asset_class = None
    contract_style = None
    perpetual_future_type = None
    swap_type = None
    financing_type = None
    commodity_type = None
    underlying_security_type = None

    if category == "E":
        security_type = SecurityType.Equity
        instrument_type = InstrumentType.Spot
        equity_type = _EQUITY_GROUP_TO_TYPE.get(group)
    elif category == "D":
        security_type = SecurityType.Bond
        instrument_type = InstrumentType.Spot
        if group == "N":
            bond_type = BondType.Municipal
        elif group in {"B", "C", "W", "T", "S", "E", "G", "A", "H"}:
            bond_type = BondType.Government if attributes[1] == "T" else BondType.Corporate
    elif category == "C":
        security_type = SecurityType.Fund
        instrument_type = InstrumentType.Spot
        fund_type = _FUND_GROUP_TO_TYPE.get(group)
        if group == "I":
            if attributes[0] == "O":
                mutual_fund_endedness = MutualFundEndedness.Open
            elif attributes[0] == "C":
                mutual_fund_endedness = MutualFundEndedness.Close
    elif category == "O":
        security_type = SecurityType.Option
        instrument_type = InstrumentType.Option
        option_type = _OPTION_GROUP_TO_TYPE.get(group)
        option_exercise_type = _OPTION_ATTR_TO_EXERCISE.get(attributes[0])
        underlying_asset_class = _OPTION_ASSET_ATTR_TO_CLASS.get(attributes[1])
        delivery_type = _DERIVATIVE_DELIVERY_ATTR_TO_TYPE.get(attributes[2])
        settlement_type = _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(delivery_type)
        contract_style = _CONTRACT_STYLE_ATTR_TO_STYLE.get(attributes[3])
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "F":
        security_type = SecurityType.Future
        instrument_type = InstrumentType.Future
        future_type = _FUTURE_GROUP_TO_TYPE.get(group)
        if group == "F":
            underlying_asset_class = _FINANCIAL_FUTURE_ATTR_TO_CLASS.get(attributes[0])
        elif group == "C":
            underlying_asset_class = _COMMODITY_FUTURE_ATTR_TO_CLASS.get(attributes[0])
            commodity_type = _COMMODITY_FUTURE_CLASS_TO_TYPE.get(underlying_asset_class)
        delivery_type = _DERIVATIVE_DELIVERY_ATTR_TO_TYPE.get(attributes[1])
        settlement_type = _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(delivery_type)
        future_delivery_type = _DELIVERY_TYPE_TO_FUTURE_DELIVERY_TYPE.get(delivery_type)
        contract_style = _CONTRACT_STYLE_ATTR_TO_STYLE.get(attributes[2])
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "S":
        security_type = SecurityType.Swap
        instrument_type = InstrumentType.Swap
        swap_type = _SWAP_GROUP_TO_TYPE.get(group)
    elif category == "H":
        security_type = SecurityType.Option
        instrument_type = InstrumentType.Option
        underlying_asset_class = _COMPLEX_OPTION_GROUP_TO_ASSET_CLASS.get(group)
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "I":
        instrument_type = InstrumentType.Spot
        if group == "F":
            security_type = SecurityType.Currency
        elif group == "T":
            security_type = SecurityType.Commodity
            commodity_type = _SPOT_COMMODITY_ATTR_TO_TYPE.get(attributes[0])
    elif category == "J":
        security_type = SecurityType.Forward
        instrument_type = InstrumentType.Forward
        underlying_asset_class = _FORWARD_GROUP_TO_ASSET_CLASS.get(group)
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "L":
        security_type = SecurityType.Financing
        instrument_type = InstrumentType.Financing
        financing_type = _FINANCING_GROUP_TO_TYPE.get(group)
        delivery_type = _FINANCING_DELIVERY_ATTR_TO_TYPE.get(attributes[3])
        settlement_type = _DELIVERY_TYPE_TO_SETTLEMENT_TYPE.get(delivery_type)
    elif category == "K":
        security_type = SecurityType.Spread
        instrument_type = InstrumentType.Spread
        underlying_asset_class = _STRATEGY_GROUP_TO_ASSET_CLASS.get(group)
        underlying_security_type = _ASSET_CLASS_TO_SECURITY_TYPE.get(underlying_asset_class)
    elif category == "R":
        instrument_type = InstrumentType.Right
    elif category == "T":
        if group == "C":
            security_type = SecurityType.Currency
            instrument_type = InstrumentType.Spot
        elif group == "T":
            security_type = SecurityType.Commodity
            instrument_type = InstrumentType.Spot
        elif group == "I":
            security_type = SecurityType.Index
            instrument_type = InstrumentType.Spot
        elif group == "B":
            instrument_type = InstrumentType.Basket
        elif group == "D":
            security_type = SecurityType.Equity
            instrument_type = InstrumentType.Spot

    return CFIClassification(
        code=normalized,
        category=category,
        group=group,
        attributes=attributes,
        security_type=security_type,
        instrument_type=instrument_type,
        equity_type=equity_type,
        option_type=option_type,
        option_exercise_type=option_exercise_type,
        bond_type=bond_type,
        fund_type=fund_type,
        mutual_fund_endedness=mutual_fund_endedness,
        future_type=future_type,
        future_delivery_type=future_delivery_type,
        settlement_type=settlement_type,
        delivery_type=delivery_type,
        underlying_asset_class=underlying_asset_class,
        contract_style=contract_style,
        perpetual_future_type=perpetual_future_type,
        swap_type=swap_type,
        financing_type=financing_type,
        commodity_type=commodity_type,
        underlying_security_type=underlying_security_type,
    )


def build_cfi(
    *,
    security_type: SecurityType | str | None = None,
    equity_type: EquityType | str | None = None,
    option_type: OptionType | str | None = None,
    option_exercise_type: OptionExerciseType | str | None = None,
    bond_type: BondType | str | None = None,
    commodity_type: CommodityType | str | None = None,
    fund_type: FundType | str | None = None,
    financing_type: FinancingType | str | None = None,
    mutual_fund_endedness: MutualFundEndedness | str | None = None,
    future_type: FutureType | str | None = None,
    future_delivery_type: FutureDeliveryType | str | None = None,
    settlement_type: SettlementType | str | None = None,
    delivery_type: DeliveryType | str | None = None,
    underlying_asset_class: UnderlyingAssetClass | str | None = None,
    contract_style: ContractStyle | str | None = None,
    perpetual_future_type: PerpetualFutureType | str | None = None,
    swap_type: SwapType | str | None = None,
    underlying_security_type: SecurityType | str | None = None,
    category: str | None = None,
    group: str | None = None,
    attributes: str | tuple[str, str, str, str] | None = None,
) -> str:
    security_type = _coerce_enum(SecurityType, security_type, "security_type")
    equity_type = _coerce_enum(EquityType, equity_type, "equity_type")
    option_type = _coerce_enum(OptionType, option_type, "option_type")
    option_exercise_type = _coerce_enum(OptionExerciseType, option_exercise_type, "option_exercise_type")
    bond_type = _coerce_enum(BondType, bond_type, "bond_type")
    commodity_type = _coerce_enum(CommodityType, commodity_type, "commodity_type")
    fund_type = _coerce_enum(FundType, fund_type, "fund_type")
    financing_type = _coerce_enum(FinancingType, financing_type, "financing_type")
    mutual_fund_endedness = _coerce_enum(MutualFundEndedness, mutual_fund_endedness, "mutual_fund_endedness")
    future_type = _coerce_enum(FutureType, future_type, "future_type")
    future_delivery_type = _coerce_enum(FutureDeliveryType, future_delivery_type, "future_delivery_type")
    settlement_type = _coerce_enum(SettlementType, settlement_type, "settlement_type")
    delivery_type = _coerce_enum(DeliveryType, delivery_type, "delivery_type")
    underlying_asset_class = _coerce_enum(UnderlyingAssetClass, underlying_asset_class, "underlying_asset_class")
    contract_style = _coerce_enum(ContractStyle, contract_style, "contract_style")
    perpetual_future_type = _coerce_enum(PerpetualFutureType, perpetual_future_type, "perpetual_future_type")
    swap_type = _coerce_enum(SwapType, swap_type, "swap_type")
    underlying_security_type = _coerce_enum(SecurityType, underlying_security_type, "underlying_security_type")

    underlying_asset_class = _resolve_underlying_asset_class(underlying_asset_class, underlying_security_type)
    settlement_type, delivery_type, future_delivery_type = _resolve_delivery_fields(
        settlement_type,
        delivery_type,
        future_delivery_type,
    )

    if category is not None or group is not None or attributes is not None:
        if category is None or group is None:
            raise ValueError("category and group are required when building a raw CFI code")
        return f"{category.strip().upper()}{group.strip().upper()}{''.join(_normalize_cfi_attributes(attributes))}"

    if security_type is None:
        raise ValueError("security_type is required when category and group are not provided")

    if security_type == SecurityType.Equity:
        resolved_equity_type = equity_type or EquityType.Shares
        return f"E{_EQUITY_TYPE_TO_GROUP[resolved_equity_type]}XXXX"

    if security_type == SecurityType.Bond:
        resolved_bond_type = bond_type or BondType.Corporate
        if resolved_bond_type == BondType.Municipal:
            return "DNXXXX"
        if resolved_bond_type == BondType.Government:
            return "DBXTXX"
        return "DBXXXX"

    if security_type == SecurityType.Currency:
        return "IFXXXP"

    if security_type == SecurityType.Commodity:
        commodity_attr = _COMMODITY_TYPE_TO_SPOT_ATTR.get(commodity_type, "X")
        return f"IT{commodity_attr}XXX"

    if security_type == SecurityType.Fund:
        resolved_fund_type = fund_type or FundType.MutualFund
        if resolved_fund_type == FundType.ETF:
            return "CEXXXX"
        if resolved_fund_type == FundType.REIT:
            return "CBXXXX"
        endedness_attr = "X"
        if mutual_fund_endedness == MutualFundEndedness.Open:
            endedness_attr = "O"
        elif mutual_fund_endedness == MutualFundEndedness.Close:
            endedness_attr = "C"
        return f"CI{endedness_attr}XXX"

    if security_type == SecurityType.Option:
        if option_type is None:
            if underlying_asset_class is None:
                raise ValueError("option_type is required when building a listed option CFI")
            complex_group = _ASSET_CLASS_TO_COMPLEX_OPTION_GROUP.get(underlying_asset_class)
            if complex_group is None:
                raise NotImplementedError(
                    f"CFI complex option generation is not implemented for underlying asset class {underlying_asset_class.value}"
                )
            return f"H{complex_group}XXXX"
        exercise_attr = _OPTION_EXERCISE_TO_ATTR.get(option_exercise_type, "X")
        underlying_attr = _OPTION_CLASS_TO_ASSET_ATTR.get(underlying_asset_class, "X")
        delivery_attr = _DERIVATIVE_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        style_attr = _CONTRACT_STYLE_TO_ATTR.get(contract_style, "X")
        return f"O{_OPTION_TYPE_TO_GROUP[option_type]}{exercise_attr}{underlying_attr}{delivery_attr}{style_attr}"

    if security_type == SecurityType.Future:
        resolved_future_type = future_type or FutureType.Financial
        resolved_underlying_asset_class = underlying_asset_class
        if resolved_future_type == FutureType.Commodity and resolved_underlying_asset_class is None:
            resolved_underlying_asset_class = {
                CommodityType.Agriculture: UnderlyingAssetClass.Agriculture,
            }.get(commodity_type)
        if resolved_future_type == FutureType.Financial:
            underlying_attr = _FINANCIAL_FUTURE_CLASS_TO_ATTR.get(resolved_underlying_asset_class, "X")
        else:
            underlying_attr = _COMMODITY_FUTURE_CLASS_TO_ATTR.get(resolved_underlying_asset_class, "X")
        delivery_attr = _DERIVATIVE_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        style_attr = _CONTRACT_STYLE_TO_ATTR.get(contract_style, "X")
        return f"F{_FUTURE_TYPE_TO_GROUP[resolved_future_type]}{underlying_attr}{delivery_attr}{style_attr}X"

    if security_type == SecurityType.PerpetualFuture:
        resolved_perpetual_future_type = perpetual_future_type or PerpetualFutureType.Financial
        resolved_underlying_asset_class = underlying_asset_class
        if resolved_perpetual_future_type == PerpetualFutureType.Commodity and resolved_underlying_asset_class is None:
            resolved_underlying_asset_class = {
                CommodityType.Agriculture: UnderlyingAssetClass.Agriculture,
            }.get(commodity_type)
        if resolved_perpetual_future_type == PerpetualFutureType.Financial:
            underlying_attr = _FINANCIAL_FUTURE_CLASS_TO_ATTR.get(resolved_underlying_asset_class, "X")
        else:
            underlying_attr = _COMMODITY_FUTURE_CLASS_TO_ATTR.get(resolved_underlying_asset_class, "X")
        delivery_attr = _DERIVATIVE_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        style_attr = _CONTRACT_STYLE_TO_ATTR.get(contract_style, "X")
        return f"F{_PERPETUAL_FUTURE_TYPE_TO_GROUP[resolved_perpetual_future_type]}{underlying_attr}{delivery_attr}{style_attr}X"

    if security_type == SecurityType.Swap:
        if swap_type is None:
            raise ValueError("swap_type is required when building a swap CFI")
        return f"S{_SWAP_TYPE_TO_GROUP[swap_type]}XXXX"

    if security_type == SecurityType.Financing:
        if financing_type is None:
            raise ValueError("financing_type is required when building a financing CFI")
        delivery_attr = _FINANCING_DELIVERY_TYPE_TO_ATTR.get(delivery_type, "X")
        return f"L{_FINANCING_TYPE_TO_GROUP[financing_type]}XXX{delivery_attr}"

    if security_type == SecurityType.Forward:
        if underlying_asset_class is None:
            raise ValueError("underlying_asset_class or underlying_security_type is required when building a forward CFI")
        forward_group = _ASSET_CLASS_TO_FORWARD_GROUP.get(underlying_asset_class)
        if forward_group is None:
            raise NotImplementedError(f"CFI forward generation is not implemented for underlying asset class {underlying_asset_class.value}")
        return f"J{forward_group}XXXX"

    if security_type == SecurityType.Spread:
        if underlying_asset_class is None:
            raise ValueError("underlying_asset_class or underlying_security_type is required when building a spread CFI")
        strategy_group = _ASSET_CLASS_TO_STRATEGY_GROUP.get(underlying_asset_class)
        if strategy_group is None:
            raise NotImplementedError(f"CFI spread generation is not implemented for underlying asset class {underlying_asset_class.value}")
        return f"K{strategy_group}XXXX"

    if security_type == SecurityType.Index:
        return "TIXXXX"

    raise NotImplementedError(f"CFI generation is not implemented for security type {security_type.value}")


def build_cfi_from_classification(classification: CFIClassification) -> str:
    if not isinstance(classification, CFIClassification):
        raise TypeError("classification must be a CFIClassification")

    try:
        if classification.security_type is not None:
            return build_cfi(
                security_type=classification.security_type,
                equity_type=classification.equity_type,
                option_type=classification.option_type,
                option_exercise_type=classification.option_exercise_type,
                bond_type=classification.bond_type,
                commodity_type=classification.commodity_type,
                fund_type=classification.fund_type,
                financing_type=classification.financing_type,
                mutual_fund_endedness=classification.mutual_fund_endedness,
                future_type=classification.future_type,
                future_delivery_type=classification.future_delivery_type,
                settlement_type=classification.settlement_type,
                delivery_type=classification.delivery_type,
                underlying_asset_class=classification.underlying_asset_class,
                contract_style=classification.contract_style,
                perpetual_future_type=classification.perpetual_future_type,
                swap_type=classification.swap_type,
                underlying_security_type=classification.underlying_security_type,
            )
    except NotImplementedError:
        pass

    return build_cfi(
        category=classification.category,
        group=classification.group,
        attributes=classification.attributes,
    )


def validate_cfi_classification(classification: CFIClassification) -> CFIClassification:
    if not isinstance(classification, CFIClassification):
        raise TypeError("classification must be a CFIClassification")

    raw_code = build_cfi(
        category=classification.category,
        group=classification.group,
        attributes=classification.attributes,
    )
    structured_code = build_cfi_from_classification(classification)
    normalized_code = classification.code.strip().upper()

    if normalized_code != raw_code:
        raise ValueError(f"CFI classification code does not match derived code {raw_code}")
    if structured_code != raw_code:
        raise ValueError("CFI classification typed fields do not match category/group/attributes")

    return replace(
        classification,
        code=raw_code,
        category=raw_code[0],
        group=raw_code[1],
        attributes=tuple(raw_code[2:]),
    )


def _cfi_classification_to_code(self):
    return build_cfi_from_classification(self)


def _cfi_classification_validate(self):
    return validate_cfi_classification(self)


CFIClassification.to_code = _cfi_classification_to_code  # type: ignore[attr-defined]
CFIClassification.validate = _cfi_classification_validate  # type: ignore[attr-defined]


__all__ = [
    "AggressorSide",
    "AgricultureType",
    "AmortizationType",
    "AuctionType",
    "AveragingMethod",
    "BarrierType",
    "BondType",
    "BookType",
    "BorrowType",
    "AccountType",
    "CollateralType",
    "CommodityType",
    "CompoundingMethod",
    "ContractStyle",
    "ContractUnit",
    "CorporateActionType",
    "CFIClassification",
    "CouponFrequency",
    "CouponType",
    "CountryCode",
    "CountryCode3",
    "CrossType",
    "Currency",
    "CurrencyAliasRecord",
    "CurrencyRecord",
    "CurrencyRole",
    "MICMarketCategory",
    "DayCountConvention",
    "DelistingReason",
    "DeliveryType",
    "DistributionPolicy",
    "EnergyType",
    "EquityType",
    "ExchangeCode",
    "ExchangeRecord",
    "ExecType",
    "ExecutionInstruction",
    "ExerciseEventType",
    "ExoticOptionFeature",
    "Frequency",
    "FinancingType",
    "FundSubType",
    "FundType",
    "FutureDeliveryType",
    "FutureType",
    "IdentifierType",
    "Industry",
    "IndustryGroup",
    "InventoryType",
    "InstrumentType",
    "LegRole",
    "LiquidityTerm",
    "LiquidityFlag",
    "ListingStatus",
    "MarginType",
    "MarketState",
    "MarketStatusReason",
    "MarketType",
    "MetalsType",
    "MutualFundEndedness",
    "NettingType",
    "OpenClose",
    "OptionExerciseType",
    "OptionType",
    "OrderCapacity",
    "OrderFlag",
    "OrderStatus",
    "OrderType",
    "PayoffStyle",
    "PerpetualFutureType",
    "PositionType",
    "PositionEffect",
    "PriceNotation",
    "PriceType",
    "QuantityUnit",
    "QuoteCondition",
    "RateIndex",
    "RedemptionFrequency",
    "RepoType",
    "ResetFrequency",
    "Sector",
    "SegmentType",
    "Seniority",
    "SecurityStatus",
    "SecurityType",
    "SettlementType",
    "ShareClassHedging",
    "ShortSaleRestriction",
    "Side",
    "StrategyType",
    "StubType",
    "SubIndustry",
    "SwapLegType",
    "SwapType",
    "TenderOfferType",
    "TickerNamespace",
    "TimeInForce",
    "TradeCondition",
    "TradingSession",
    "TradingType",
    "UnderlyingAssetClass",
    "VenueRegulatoryFlag",
    "VenueType",
    "VehicleWrapper",
    "build_cfi_from_classification",
    "currency_alias_records",
    "currency_export_capsule",
    "currency_records",
    "build_cfi",
    "exchange_record",
    "exchange_records",
    "exchange_records_by_country",
    "exchange_records_by_market_category",
    "exchange_records_by_market_category_type",
    "exchange_records_by_operating_mic",
    "exchange_records_by_parent_mic",
    "exchange_records_by_region",
    "exchange_records_by_regulatory_flag",
    "exchange_records_by_status",
    "parse_cfi",
    "to_frequency",
    "validate_cfi_classification",
]
