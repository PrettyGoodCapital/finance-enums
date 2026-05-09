from finance_enums import ExchangeCode


class TestExchange:
    def test_exchange_basic(self):
        assert len(ExchangeCode.__members__) == 147

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
