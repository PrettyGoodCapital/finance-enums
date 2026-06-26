from finance_enums import Industry, IndustryGroup, Sector, SubIndustry


class TestSector:
    def test_sector_basic(self):
        assert len(Sector) == 12

    def test_industry_group_basic(self):
        assert len(IndustryGroup) == 26

    def test_industry_basic(self):
        assert len(Industry) == 75

    def test_subindustry_basic(self):
        assert len(SubIndustry) == 164
