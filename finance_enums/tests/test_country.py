from finance_enums import CountryCode, CountryCode3


class TestCountry:
    def test_country_basic(self):
        assert len(CountryCode.__members__) == 251
        assert CountryCode.US.country_name() == "United States of America"
        assert CountryCode.US.code3() == CountryCode3.USA

    def test_country_includes_kosovo_live_code_pair(self):
        assert CountryCode.XK.country_name() == "Kosovo"
        assert CountryCode.XK.code3() == CountryCode3.UNK
