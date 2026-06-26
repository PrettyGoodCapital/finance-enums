"""ISO 3166 country metadata and country <-> currency mappings.

``CountryCode`` is a Rust-generated ``IntEnum`` of ISO 3166-1 alpha-2 codes;
this module attaches the English short name and alpha-3 code, and provides the
bridge to :class:`Currency`.
"""

from __future__ import annotations

from .finance_enums import country_names as _country_names_fn, int_enums as _int_enums

__all__ = [
    "country_currency",
    "currency_countries",
]

Currency = _int_enums.Currency
CountryCode = _int_enums.CountryCode
CountryCode3 = _int_enums.CountryCode3

_country_names = _country_names_fn()

# ``code3()`` maps an alpha-2 member to its alpha-3 counterpart by ordinal, which
# is only correct while the two families are kept position-for-position aligned in
# the Rust source. Guard the invariant at import so a future divergence fails
# loudly instead of silently returning the wrong alpha-3 code.
if len(CountryCode.__members__) != len(CountryCode3.__members__):
    raise RuntimeError("CountryCode and CountryCode3 families are not aligned by ordinal")


def _country_code_country_name(self):
    return _country_names[self.value]


def _country_code_code3(self):
    return CountryCode3(self.value)


CountryCode.country_name = _country_code_country_name  # type: ignore[attr-defined]
CountryCode.code3 = _country_code_code3  # type: ignore[attr-defined]
CountryCode3.country_name = lambda self: _country_names[self.value]  # type: ignore[attr-defined]


# alpha-2 -> currency code (only currencies that are Currency members).
# Best-effort, hand-maintained subset of ISO 3166: covers the major trading
# jurisdictions, not every country code. ``country_currency`` returns ``None`` for
# codes absent here.
_COUNTRY_CURRENCY_CODES: dict[str, str] = {
    "AD": "EUR",
    "AE": "AED",
    "AF": "AFN",
    "AG": "XCD",
    "AI": "XCD",
    "AL": "ALL",
    "AM": "AMD",
    "AO": "AOA",
    "AR": "ARS",
    "AT": "EUR",
    "AU": "AUD",
    "AW": "AWG",
    "AX": "EUR",
    "AZ": "AZN",
    "BA": "BAM",
    "BB": "BBD",
    "BD": "BDT",
    "BE": "EUR",
    "BF": "XOF",
    "BG": "BGN",
    "BH": "BHD",
    "BI": "BIF",
    "BJ": "XOF",
    "BM": "BMD",
    "BN": "BND",
    "BO": "BOB",
    "BR": "BRL",
    "BS": "BSD",
    "BT": "BTN",
    "BW": "BWP",
    "BY": "BYN",
    "BZ": "BZD",
    "CA": "CAD",
    "CD": "CDF",
    "CF": "XAF",
    "CG": "XAF",
    "CH": "CHF",
    "CI": "XOF",
    "CL": "CLP",
    "CM": "XAF",
    "CN": "CNY",
    "CO": "COP",
    "CR": "CRC",
    "CU": "CUP",
    "CV": "CVE",
    "CY": "EUR",
    "CZ": "CZK",
    "DE": "EUR",
    "DK": "DKK",
    "DO": "DOP",
    "DZ": "DZD",
    "EC": "USD",
    "EE": "EUR",
    "EG": "EGP",
    "ES": "EUR",
    "ET": "ETB",
    "FI": "EUR",
    "FJ": "FJD",
    "FR": "EUR",
    "GB": "GBP",
    "GE": "GEL",
    "GH": "GHS",
    "GI": "GIP",
    "GR": "EUR",
    "GT": "GTQ",
    "HK": "HKD",
    "HR": "EUR",
    "HU": "HUF",
    "ID": "IDR",
    "IE": "EUR",
    "IL": "ILS",
    "IN": "INR",
    "IQ": "IQD",
    "IR": "IRR",
    "IS": "ISK",
    "IT": "EUR",
    "JM": "JMD",
    "JO": "JOD",
    "JP": "JPY",
    "KE": "KES",
    "KR": "KRW",
    "KW": "KWD",
    "KY": "KYD",
    "KZ": "KZT",
    "LB": "LBP",
    "LI": "CHF",
    "LK": "LKR",
    "LT": "EUR",
    "LU": "EUR",
    "LV": "EUR",
    "MA": "MAD",
    "MC": "EUR",
    "MT": "EUR",
    "MU": "MUR",
    "MX": "MXN",
    "MY": "MYR",
    "NG": "NGN",
    "NL": "EUR",
    "NO": "NOK",
    "NZ": "NZD",
    "OM": "OMR",
    "PA": "PAB",
    "PE": "PEN",
    "PH": "PHP",
    "PK": "PKR",
    "PL": "PLN",
    "PT": "EUR",
    "QA": "QAR",
    "RO": "RON",
    "RS": "RSD",
    "RU": "RUB",
    "SA": "SAR",
    "SE": "SEK",
    "SG": "SGD",
    "SI": "EUR",
    "SK": "EUR",
    "TH": "THB",
    "TR": "TRY",
    "TW": "TWD",
    "UA": "UAH",
    "US": "USD",
    "VN": "VND",
    "ZA": "ZAR",
}


def country_currency(country_code: CountryCode | str) -> Currency | None:
    normalized = country_code.name if isinstance(country_code, CountryCode) else str(country_code).strip().upper()
    currency_code = _COUNTRY_CURRENCY_CODES.get(normalized)
    return Currency(currency_code) if currency_code is not None else None


def currency_countries(currency: Currency | str) -> list[CountryCode]:
    normalized = currency.name if isinstance(currency, Currency) else str(currency).strip().upper()
    return [
        CountryCode(country_code)
        for country_code, currency_code in _COUNTRY_CURRENCY_CODES.items()
        if currency_code == normalized and country_code in CountryCode.__members__
    ]
