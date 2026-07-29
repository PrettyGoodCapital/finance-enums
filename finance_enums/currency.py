"""Currency metadata for the :class:`Currency` enum (ISO 4217 + extensions).

``Currency`` is a Rust-generated ``IntEnum``; the display-name / ISO-4217
metadata, record accessors and aliases all come from the native extension via
the stable C ABI.
"""

from __future__ import annotations

from dataclasses import dataclass

from .finance_enums import (
    currency_alias_records as _currency_alias_records_raw,
    currency_records as _currency_records_raw,
    int_enums as _int_enums,
)

__all__ = [
    "CurrencyAliasRecord",
    "CurrencyRecord",
    "currency_alias_records",
    "currency_records",
]


@dataclass(frozen=True)
class CurrencyRecord:
    code: str
    display_name: str
    is_iso4217: bool


@dataclass(frozen=True)
class CurrencyAliasRecord:
    alias: str
    canonical_code: str


Currency = _int_enums.Currency

_currency_record_data = [CurrencyRecord(code, display_name, is_iso4217) for code, display_name, is_iso4217 in _currency_records_raw()]
_currency_alias_record_data = [CurrencyAliasRecord(alias, canonical_code) for alias, canonical_code in _currency_alias_records_raw()]
_currency_codes = [record.code for record in _currency_record_data]
_currency_by_code = {record.code: record for record in _currency_record_data}

#: Alias -> canonical code map, restricted to aliases whose canonical code is a
#: known ``Currency`` member. Consumed by the package-level enum-behaviour
#: installer to resolve string aliases on the ``Currency`` family.
currency_aliases = {record.alias: record.canonical_code for record in _currency_alias_record_data if record.canonical_code in _currency_by_code}


def currency_records() -> list[CurrencyRecord]:
    return list(_currency_record_data)


def currency_alias_records() -> list[CurrencyAliasRecord]:
    return list(_currency_alias_record_data)


def _currency_currency_name(self):
    return _currency_by_code[self.name].display_name


def _currency_is_iso4217(self):
    return _currency_by_code[self.name].is_iso4217


def _currency_record(self):
    return _currency_by_code[self.name]


Currency.currency_name = _currency_currency_name  # type: ignore[attr-defined]
Currency.is_iso4217 = _currency_is_iso4217  # type: ignore[attr-defined]
Currency.record = _currency_record  # type: ignore[attr-defined]
