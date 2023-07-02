from finance_enums import Sector, IndustryGroup, Industry, SubIndustry


class TestSector:
    def test_sector_basic(self):
        assert len(Sector.__members__) == 12

    def test_industry_group_basic(self):
        assert len(IndustryGroup.__members__) == 26

    def test_industry_basic(self):
        assert len(Industry.__members__) == 75

    def test_subindustry_basic(self):
        assert len(SubIndustry.__members__) == 164
