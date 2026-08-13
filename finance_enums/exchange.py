"""ISO 10383 exchange (MIC) reference data for the :class:`ExchangeCode` enum.

``ExchangeCode`` is a Rust-generated ``IntEnum`` whose member names are ISO
10383 Market Identifier Codes. The full record set (market name, operating MIC,
country, regulatory classification, etc.) is sourced from the native extension
via the stable C ABI. Market-category and regulatory-flag mappings are expressed
with the :class:`MICMarketCategory` / :class:`VenueRegulatoryFlag` IntEnums.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from . import _finance_enums as _rust_enums
from ._finance_enums import exchange_records_raw as _exchange_records_raw, int_enums as _int_enums
from .country import country_currency, currency_countries

__all__ = [
    "ExchangeRecord",
    "exchange_currency",
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
]

MICMarketCategory = _int_enums.MICMarketCategory
VenueRegulatoryFlag = _int_enums.VenueRegulatoryFlag
ExchangeCode = _int_enums.ExchangeCode
CountryCode = _int_enums.CountryCode

_exchange_records_typed = getattr(_rust_enums, "exchange_records_typed", None)
_exchange_record_typed = getattr(_rust_enums, "exchange_record_typed", None)


def _coerce_enum(enum_type: Any, value: Any, field_name: str) -> Any:
    if value is None or isinstance(value, enum_type):
        return value
    try:
        return enum_type(value)
    except ValueError as exc:
        raise ValueError(f"invalid {field_name}: {value!r}") from exc


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
    normalized = code.name if isinstance(code, ExchangeCode) else str(code).strip().upper()

    if _exchange_record_typed is not None:
        typed_record = _exchange_record_typed(normalized)
        if typed_record is not None:
            return _exchange_record_from_typed(typed_record)

    return _exchange_by_code.get(normalized)


def exchange_records_by_country(country_code: CountryCode | str) -> list[ExchangeRecord]:
    normalized = country_code.name if isinstance(country_code, CountryCode) else str(country_code).strip().upper()
    return list(_exchange_by_country.get(normalized, []))


def exchange_currency(exchange: ExchangeCode | str):
    record = exchange_record(exchange)
    if record is None:
        return None
    return country_currency(record.iso_country_code)


def exchange_records_by_currency(currency: Any) -> list[ExchangeRecord]:
    countries = currency_countries(currency)
    records: list[ExchangeRecord] = []
    for country in countries:
        records.extend(exchange_records_by_country(country))
    return records


def exchange_records_by_operating_mic(operating_mic: ExchangeCode | str) -> list[ExchangeRecord]:
    normalized = operating_mic.name if isinstance(operating_mic, ExchangeCode) else str(operating_mic).strip().upper()
    return list(_exchange_by_operating_mic.get(normalized, []))


def exchange_records_by_parent_mic(parent_mic: ExchangeCode | str) -> list[ExchangeRecord]:
    normalized = parent_mic.name if isinstance(parent_mic, ExchangeCode) else str(parent_mic).strip().upper()
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


def _exchange_record(self):
    return _exchange_by_code[self.name]


def _exchange_market_name(self):
    return _exchange_by_code[self.name].market_name


def _exchange_market_category(self):
    return _exchange_by_code[self.name].market_category()


def _exchange_regulatory_flags(self):
    return _exchange_by_code[self.name].regulatory_flags()


def _exchange_has_regulatory_flag(self, regulatory_flag):  # type: ignore[no-untyped-def]
    return _exchange_by_code[self.name].has_regulatory_flag(regulatory_flag)


ExchangeCode.record = _exchange_record  # type: ignore[attr-defined]
ExchangeCode.market_name = _exchange_market_name  # type: ignore[attr-defined]
ExchangeCode.market_category = _exchange_market_category  # type: ignore[attr-defined]
ExchangeCode.regulatory_flags = _exchange_regulatory_flags  # type: ignore[attr-defined]
ExchangeCode.has_regulatory_flag = _exchange_has_regulatory_flag  # type: ignore[attr-defined]
