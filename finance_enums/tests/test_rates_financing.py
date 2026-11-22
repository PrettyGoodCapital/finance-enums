import pytest

from finance_enums import (
    AmortizationType,
    AveragingMethod,
    BarrierType,
    BorrowType,
    CollateralType,
    CompoundingMethod,
    CouponType,
    DayCountConvention,
    ExoticOptionFeature,
    MarginType,
    RateIndex,
    RepoType,
    Seniority,
    StubType,
    SwapLegType,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_count", "expected_members"),
    [
        (CouponType, 12, {"Fixed", "Floating", "Zero"}),
        (DayCountConvention, 23, {"Actual360", "ActualActualIsda", "Thirty360Isda", "Thirty360UnitedStates"}),
        (AmortizationType, 7, {"Bullet", "Linear", "Accreting"}),
        (Seniority, 11, {"SeniorSecured", "Subordinated", "Preferred"}),
        (CollateralType, 7, {"GeneralCollateral", "CashCollateral", "Equities"}),
        (MarginType, 7, {"Initial", "Variation", "PortfolioMargin"}),
        (BorrowType, 6, {"StockLoan", "RepoBorrow", "UnsecuredBorrow"}),
        (RepoType, 7, {"Bilateral", "TriParty", "Evergreen"}),
        (SwapLegType, 10, {"Fixed", "Floating", "Basis"}),
        (
            RateIndex,
            9,
            {
                "SecuredOvernightFinancingRate",
                "SterlingOvernightIndexAverage",
                "EuroInterbankOfferedRate",
            },
        ),
        (CompoundingMethod, 5, {"None", "Straight", "Flat", "SpreadExclusive"}),
        (StubType, 9, {"None", "ShortFront", "LongBack"}),
        (BarrierType, 7, {"UpAndIn", "DownAndOut", "DoubleKnockOut"}),
        (AveragingMethod, 6, {"Arithmetic", "Geometric", "VolumeWeighted"}),
        (ExoticOptionFeature, 9, {"Barrier", "Asian", "Quanto"}),
    ],
)
def test_fixed_income_financing_and_structured_product_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type) == expected_count
    assert expected_members.issubset(enum_type.__members__)
