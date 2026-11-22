import pytest

from finance_enums import (
    AggressorSide,
    BusinessDayConvention,
    CompoundingMethod,
    CreditRatingAgency,
    DayCountConvention,
    DeliveryType,
    FinancingType,
    ForeignExchangeProductType,
    ForeignExchangeTenor,
    MoneyMarketInstrumentType,
    RateIndex,
    RestructuringClause,
    RollConvention,
    SecurityType,
    SettlementType,
    YieldType,
    build_cfi,
    parse_cfi,
)


def _names(enum_type):
    return [member.name for member in enum_type if member.name != "Invalid"]


def test_day_counts_cover_the_isda_and_strata_set():
    # OpenGamma Strata StandardDayCounts, plus Bus/252.
    assert len(_names(DayCountConvention)) == 22
    assert {"ActualActualIsda", "ActualActualIcma", "ActualActualAfb", "Thirty360Isda", "Thirty360European", "Thirty360EuropeanIsda"}.issubset(
        DayCountConvention.__members__
    )
    assert "ActualActual" not in DayCountConvention.__members__
    assert "Thirty360" not in DayCountConvention.__members__


@pytest.mark.parametrize(
    ("written", "member"),
    [
        ("ACT/360", DayCountConvention.Actual360),
        ("ACT/ACT ICMA", DayCountConvention.ActualActualIcma),
        ("30E/360", DayCountConvention.Thirty360European),
        ("30U/360", DayCountConvention.Thirty360UnitedStates),
        ("BUS/252", DayCountConvention.Business252),
    ],
)
def test_day_counts_parse_their_written_form(written, member):
    assert DayCountConvention(written) is member


def test_business_day_and_roll_conventions():
    assert _names(BusinessDayConvention) == [
        "Unadjusted",
        "Following",
        "ModifiedFollowing",
        "Preceding",
        "ModifiedPreceding",
        "Nearest",
        "FloatingRateNote",
    ]
    assert {"EndOfMonth", "InternationalMoneyMarket", "DayOfMonth1", "DayOfMonth30", "Wednesday"}.issubset(RollConvention.__members__)
    assert "DayOfMonth31" not in RollConvention.__members__


def test_compounding_is_separate_from_overnight_accrual():
    assert _names(CompoundingMethod) == ["None", "Straight", "Flat", "SpreadExclusive"]


def test_settlement_method_and_delivery_are_separate_axes():
    # FIX SettlMethod (tag 1193) and DeliveryType (tag 919).
    assert _names(SettlementType) == ["Physical", "Cash", "NonDeliverable", "ElectAtExercise"]
    assert _names(DeliveryType) == ["DeliveryVersusPayment", "FreeOfPayment", "PaymentVersusPayment", "TriParty", "HoldInCustody", "DeliverByValue"]
    assert DeliveryType("DVP") is DeliveryType.DeliveryVersusPayment


@pytest.mark.parametrize(
    ("kwargs", "code"),
    [
        ({"settlement_type": SettlementType.Physical}, "LRXXXP"),
        ({"delivery_type": DeliveryType.TriParty}, "LRXXXT"),
        ({"delivery_type": DeliveryType.HoldInCustody}, "LRXXXH"),
    ],
)
def test_financing_cfi_maps_both_axes(kwargs, code):
    assert build_cfi(security_type=SecurityType.Financing, financing_type=FinancingType.RepurchaseAgreement, **kwargs) == code
    parsed = parse_cfi(code)
    assert parsed.settlement_type == kwargs.get("settlement_type")
    assert parsed.delivery_type == kwargs.get("delivery_type")


def test_aggressor_side_has_an_explicit_no_aggressor():
    assert _names(AggressorSide) == ["Buy", "Sell", "NoAggressor"]


def test_yield_types_follow_fix_tag_235():
    assert len(_names(YieldType)) == 28
    assert {"YieldToMaturity", "YieldToWorst", "YieldToNextCall", "CurrentYield", "TrueYield"}.issubset(YieldType.__members__)


def test_credit_and_money_market_aliases():
    assert RestructuringClause("MM") is RestructuringClause.ModifiedModifiedRestructuring
    assert RestructuringClause("XR") is RestructuringClause.NoRestructuring
    assert CreditRatingAgency("S&P") is CreditRatingAgency.StandardAndPoors
    assert MoneyMarketInstrumentType("CP") is MoneyMarketInstrumentType.CommercialPaper
    assert RateIndex("FedFunds") is RateIndex.EffectiveFederalFundsRate


def test_foreign_exchange_products_and_tenors():
    assert _names(ForeignExchangeProductType) == ["Spot", "OutrightForward", "Swap", "NonDeliverableForward", "NonDeliverableSwap"]
    assert ForeignExchangeProductType("NDF") is ForeignExchangeProductType.NonDeliverableForward
    assert {"TomorrowNext", "BrokenDate"}.issubset(ForeignExchangeTenor.__members__)
    assert "Month12" not in ForeignExchangeTenor.__members__
