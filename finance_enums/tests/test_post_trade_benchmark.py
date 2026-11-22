import pytest

from finance_enums import (
    AllocationMethod,
    BenchmarkType,
    CalculationAgentType,
    ClearingHouse,
    ClearingModel,
    CorporateActionAdjustmentType,
    GiveUpType,
    IndexWeightingMethod,
    ScheduleFrequency,
    SettlementFailReason,
    SettlementStatus,
    SettlementType,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_members"),
    [
        (
            SettlementType,
            {
                "Physical",
                "Cash",
                "NonDeliverable",
                "ElectAtExercise",
                "DeliveryVersusPayment",
                "PaymentVersusPayment",
                "FreeOfPayment",
                "HoldInCustody",
                "TriParty",
            },
        ),
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
        (SettlementFailReason, {"InsufficientSecurities", "InsufficientCash", "InstructionMismatch", "RegulatoryHold", "SystemIssue"}),
        (AllocationMethod, {"AveragePrice", "SpecificLot", "ProRata", "FirstInFirstOut", "LastInFirstOut", "StepOut"}),
        (GiveUpType, {"None", "GiveUp", "GiveIn", "AveragePriceGiveUp", "ClearingGiveUp"}),
        (
            BenchmarkType,
            {"InterestRate", "EquityIndex", "FixedIncomeIndex", "CommodityIndex", "ForeignExchangeFixing", "InflationIndex", "CreditIndex"},
        ),
        (
            IndexWeightingMethod,
            {"MarketCapitalization", "FloatAdjustedMarketCapitalization", "PriceWeighted", "EqualWeighted", "Fundamental", "RiskParity"},
        ),
        (ScheduleFrequency, {"Daily", "Weekly", "Monthly", "Quarterly", "SemiAnnual", "Annual", "AtMaturity", "AdHoc"}),
        (CorporateActionAdjustmentType, {"None", "PriceReturn", "TotalReturn", "NetTotalReturn", "GrossTotalReturn", "DivisorAdjustment"}),
        (CalculationAgentType, {"Exchange", "BenchmarkAdministrator", "IndexProvider", "CalculationAgent", "Dealer", "IndependentAgent"}),
    ],
)
def test_post_trade_and_benchmark_enum_surfaces(enum_type, expected_members):
    assert expected_members.issubset(enum_type.__members__)


def test_extended_settlement_type_keeps_cfi_compatible_members():
    assert SettlementType.Physical.name == "Physical"
    assert SettlementType.Cash.name == "Cash"
    assert SettlementType.NonDeliverable.name == "NonDeliverable"
    assert SettlementType.ElectAtExercise.name == "ElectAtExercise"
