import pytest

from finance_enums import (
    AllocationMethod,
    BenchmarkType,
    CalculationAgentType,
    ClearingHouse,
    ClearingModel,
    CorporateActionAdjustmentType,
    FailsReason,
    GiveUpType,
    IndexWeightingMethod,
    RebalanceFrequency,
    SettlementStatus,
    SettlementType,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_members"),
    [
        (SettlementType, {"Physical", "Cash", "NonDeliverable", "ElectAtExercise", "DeliveryVersusPayment", "PaymentVersusPayment", "FreeOfPayment"}),
        (SettlementStatus, {"Pending", "Matched", "Settled", "Failed", "PartiallySettled", "Canceled"}),
        (ClearingModel, {"Bilateral", "CentralCounterparty", "PrimeBroker", "AgentCleared"}),
        (
            ClearingHouse,
            {
                "NationalSecuritiesClearingCorporation",
                "FixedIncomeClearingCorporation",
                "OptionsClearingCorporation",
                "ChicagoMercantileExchange",
                "IntercontinentalExchangeClear",
                "LondonClearingHouse",
                "EurexClearing",
                "DepositoryTrustClearingCorporation",
            },
        ),
        (FailsReason, {"InsufficientSecurities", "InsufficientCash", "InstructionMismatch", "RegulatoryHold", "SystemIssue"}),
        (AllocationMethod, {"AveragePrice", "SpecificLot", "ProRata", "FirstInFirstOut", "LastInFirstOut", "StepOut"}),
        (GiveUpType, {"None", "GiveUp", "GiveIn", "AveragePriceGiveUp", "ClearingGiveUp"}),
        (
            BenchmarkType,
            {"InterestRate", "EquityIndex", "FixedIncomeIndex", "CommodityIndex", "ForeignExchangeFixing", "InflationIndex", "CreditIndex"},
        ),
        (IndexWeightingMethod, {"MarketCap", "FloatAdjustedMarketCap", "PriceWeighted", "EqualWeighted", "Fundamental", "RiskParity"}),
        (RebalanceFrequency, {"Daily", "Weekly", "Monthly", "Quarterly", "SemiAnnual", "Annual", "AdHoc"}),
        (CorporateActionAdjustmentType, {"None", "PriceReturn", "TotalReturn", "NetTotalReturn", "GrossTotalReturn", "DivisorAdjustment"}),
        (CalculationAgentType, {"Exchange", "BenchmarkAdministrator", "IndexProvider", "CalculationAgent", "Dealer", "IndependentAgent"}),
    ],
)
def test_post_trade_and_benchmark_enum_surfaces(enum_type, expected_members):
    assert expected_members.issubset(enum_type.__members__)


def test_extended_settlement_type_keeps_cfi_compatible_members():
    assert SettlementType.Physical.value == "Physical"
    assert SettlementType.Cash.value == "Cash"
    assert SettlementType.NonDeliverable.value == "NonDeliverable"
    assert SettlementType.ElectAtExercise.value == "ElectAtExercise"
