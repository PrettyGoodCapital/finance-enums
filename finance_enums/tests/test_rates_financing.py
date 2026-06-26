import pytest

from finance_enums import (
    AmortizationType,
    AveragingMethod,
    BarrierType,
    BorrowType,
    CollateralType,
    CompoundingMethod,
    CouponFrequency,
    CouponType,
    DayCountConvention,
    ExoticOptionFeature,
    MarginType,
    RateIndex,
    RepoType,
    ResetFrequency,
    Seniority,
    StubType,
    SwapLegType,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_count", "expected_members"),
    [
        (CouponType, 7, {"Fixed", "Floating", "Zero"}),
        (CouponFrequency, 7, {"Monthly", "SemiAnnual", "AtMaturity"}),
        (DayCountConvention, 7, {"Actual360", "ActualActual", "Thirty360"}),
        (AmortizationType, 7, {"Bullet", "Linear", "Accreting"}),
        (Seniority, 7, {"SeniorSecured", "Subordinated", "Preferred"}),
        (CollateralType, 7, {"GeneralCollateral", "CashCollateral", "Equities"}),
        (MarginType, 7, {"Initial", "Variation", "PortfolioMargin"}),
        (BorrowType, 6, {"StockLoan", "RepoBorrow", "UnsecuredBorrow"}),
        (RepoType, 7, {"Bilateral", "TriParty", "Evergreen"}),
        (SwapLegType, 9, {"Fixed", "Floating", "Basis"}),
        (
            RateIndex,
            9,
            {
                "SecuredOvernightFinancingRate",
                "SterlingOvernightIndexAverage",
                "EuroInterbankOfferedRate",
            },
        ),
        (ResetFrequency, 7, {"Daily", "Quarterly", "Annual"}),
        (CompoundingMethod, 6, {"Simple", "Compounded", "Flat"}),
        (StubType, 6, {"None", "ShortFront", "LongBack"}),
        (BarrierType, 7, {"UpAndIn", "DownAndOut", "DoubleKnockOut"}),
        (AveragingMethod, 6, {"Arithmetic", "Geometric", "VolumeWeighted"}),
        (ExoticOptionFeature, 9, {"Barrier", "Asian", "Quanto"}),
    ],
)
def test_fixed_income_financing_and_structured_product_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type) == expected_count
    assert expected_members.issubset(enum_type.__members__)
