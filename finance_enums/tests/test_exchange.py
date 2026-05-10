from finance_enums import CountryCode, ExchangeCode, exchange_record, exchange_records, exchange_records_by_country


class TestExchange:
    def test_exchange_basic(self):
        assert len(ExchangeCode.__members__) == len(exchange_records())
        assert len(ExchangeCode.__members__) > 2000

    def test_exchange_includes_calendar_venues(self):
        expected = {
            "XLON",
            "XAMS",
            "XKRX",
            "XSAU",
            "BVMF",
            "FOREX",
            "CRYPTO",
            "SIFMA_US",
            "ICE_US",
        }
        assert expected.issubset(ExchangeCode.__members__)

    def test_exchange_record_metadata(self):
        xnys = ExchangeCode.XNYS.record()
        forex = ExchangeCode.FOREX.record()

        assert xnys.market_name == "NEW YORK STOCK EXCHANGE, INC."
        assert xnys.iso_country_code == "US"
        assert xnys.is_official is True
        assert forex.status == "PROJECT"
        assert forex.is_official is False

    def test_exchange_lookup_helpers(self):
        xnys = exchange_record("XNYS")
        missing = exchange_record("ZZZZ")
        us_records = exchange_records_by_country(CountryCode.US)

        assert xnys is not None
        assert xnys.market_name == "NEW YORK STOCK EXCHANGE, INC."
        assert missing is None
        assert xnys in us_records
        assert all(record.iso_country_code == "US" for record in us_records)
