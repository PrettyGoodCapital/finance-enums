from __future__ import annotations

from finance_enums import CountryCode, Currency, ExchangeCode, country_currency, currency_countries, exchange_currency, exchange_records_by_currency


def test_country_and_exchange_currency_mappings() -> None:
    assert country_currency(CountryCode.US) is Currency.USD
    assert country_currency("GB") is Currency.GBP
    assert exchange_currency(ExchangeCode.XNYS) is Currency.USD
    assert exchange_currency("XLON") is Currency.GBP


def test_reverse_currency_mappings() -> None:
    countries = currency_countries(Currency.EUR)
    exchanges = exchange_records_by_currency("USD")

    assert CountryCode.DE in countries
    assert CountryCode.FR in countries
    assert any(record.mic == "XNYS" for record in exchanges)
