from finance_enums import CountryCodeAlpha2, CountryCodeAlpha3


class TestCountry:
    def test_country_basic(self):
        assert len(CountryCodeAlpha2) == 251
        assert CountryCodeAlpha2.US.country_name() == "United States of America"
        assert CountryCodeAlpha2.US.alpha3() == CountryCodeAlpha3.USA

    def test_country_includes_kosovo_live_code_pair(self):
        assert CountryCodeAlpha2.XK.country_name() == "Kosovo"
        assert CountryCodeAlpha2.XK.alpha3() == CountryCodeAlpha3.UNK
