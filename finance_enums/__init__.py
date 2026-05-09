"""Standard financial enumerations.

Variant names and structured currency metadata are stored in Rust.
This module reads those tables at import time and constructs Python ``Enum``
classes with attached lookup methods.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from .finance_enums import (
    agriculture_type_variants,
    bond_type_variants,
    commodity_type_variants,
    country_code3_variants,
    country_code_variants,
    country_names,
    currency_alias_records as _currency_alias_records_raw,
    currency_aliases,
    currency_export_capsule,
    currency_names,
    currency_records as _currency_records_raw,
    currency_variants,
    energy_type_variants,
    equity_type_variants,
    exchange_code_variants,
    fund_subtype_variants,
    fund_type_variants,
    future_delivery_type_variants,
    future_type_variants,
    industry_group_variants,
    industry_variants,
    instrument_type_variants,
    metals_type_variants,
    mutual_fund_endedness_variants,
    option_exercise_type_variants,
    option_type_variants,
    order_flag_variants,
    order_type_variants,
    sector_variants,
    security_type_variants,
    side_variants,
    sub_industry_variants,
    time_in_force_variants,
    trading_type_variants,
)
from .frequency import Frequency, to_frequency  # noqa: F401

__version__ = "0.3.0"


@dataclass(frozen=True)
class CurrencyRecord:
    code: str
    display_name: str
    is_iso4217: bool


@dataclass(frozen=True)
class CurrencyAliasRecord:
    alias: str
    canonical_code: str


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

ExchangeCode = _make_str_enum("ExchangeCode", exchange_code_variants())


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
MutualFundEndedness = _make_str_enum("MutualFundEndedness", mutual_fund_endedness_variants())
FutureType = _make_str_enum("FutureType", future_type_variants())
FutureDeliveryType = _make_str_enum("FutureDeliveryType", future_delivery_type_variants())


# --- Trading -----------------------------------------------------------------

OrderType = _make_str_enum("OrderType", order_type_variants())
Side = _make_str_enum("Side", side_variants())
OrderFlag = _make_str_enum("OrderFlag", order_flag_variants())
TimeInForce = _make_str_enum("TimeInForce", time_in_force_variants())
TradingType = _make_str_enum("TradingType", trading_type_variants())


__all__ = [
    "AgricultureType",
    "BondType",
    "CommodityType",
    "CountryCode",
    "CountryCode3",
    "Currency",
    "CurrencyAliasRecord",
    "CurrencyRecord",
    "EnergyType",
    "EquityType",
    "ExchangeCode",
    "Frequency",
    "FundSubType",
    "FundType",
    "FutureDeliveryType",
    "FutureType",
    "Industry",
    "IndustryGroup",
    "InstrumentType",
    "MetalsType",
    "MutualFundEndedness",
    "OptionExerciseType",
    "OptionType",
    "OrderFlag",
    "OrderType",
    "Sector",
    "SecurityType",
    "Side",
    "SubIndustry",
    "TimeInForce",
    "TradingType",
    "currency_alias_records",
    "currency_export_capsule",
    "currency_records",
    "to_frequency",
]
