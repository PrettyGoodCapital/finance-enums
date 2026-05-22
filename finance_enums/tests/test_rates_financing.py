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
        (CouponType, 6, {"Fixed", "Floating", "Zero"}),
        (CouponFrequency, 6, {"Monthly", "SemiAnnual", "AtMaturity"}),
        (DayCountConvention, 6, {"Actual360", "ActualActual", "Thirty360"}),
        (AmortizationType, 6, {"Bullet", "Linear", "Accreting"}),
        (Seniority, 6, {"SeniorSecured", "Subordinated", "Preferred"}),
        (CollateralType, 6, {"GeneralCollateral", "CashCollateral", "Equities"}),
        (MarginType, 6, {"Initial", "Variation", "PortfolioMargin"}),
        (BorrowType, 5, {"StockLoan", "RepoBorrow", "UnsecuredBorrow"}),
        (RepoType, 6, {"Bilateral", "TriParty", "Evergreen"}),
        (SwapLegType, 8, {"Fixed", "Floating", "Basis"}),
        (RateIndex, 8, {"SOFR", "SONIA", "EURIBOR"}),
        (ResetFrequency, 6, {"Daily", "Quarterly", "Annual"}),
        (CompoundingMethod, 5, {"Simple", "Compounded", "Flat"}),
        (StubType, 5, {"None", "ShortFront", "LongBack"}),
        (BarrierType, 6, {"UpAndIn", "DownAndOut", "DoubleKnockOut"}),
        (AveragingMethod, 5, {"Arithmetic", "Geometric", "VolumeWeighted"}),
        (ExoticOptionFeature, 8, {"Barrier", "Asian", "Quanto"}),
    ],
)
def test_fixed_income_financing_and_structured_product_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type.__members__) == expected_count
    assert expected_members.issubset(enum_type.__members__)
