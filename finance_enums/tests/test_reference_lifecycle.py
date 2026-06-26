import pytest

from finance_enums import (
    AccountType,
    BookType,
    CorporateActionType,
    CurrencyRole,
    DelistingReason,
    DistributionPolicy,
    ExerciseEventType,
    IdentifierType,
    InventoryType,
    LiquidityTerm,
    ListingStatus,
    NettingType,
    PositionType,
    PriceNotation,
    QuantityUnit,
    RedemptionFrequency,
    SecurityStatus,
    ShareClassHedging,
    StrategyType,
    TenderOfferType,
    TickerNamespace,
    VehicleWrapper,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_count", "expected_members"),
    [
        (
            IdentifierType,
            11,
            {
                "Ticker",
                "InternationalSecuritiesIdentificationNumber",
                "FinancialInstrumentGlobalIdentifier",
            },
        ),
        (TickerNamespace, 9, {"Exchange", "Composite", "Bloomberg"}),
        (PriceNotation, 13, {"Decimal", "Yield", "BasisPoints", "PerUnit", "CleanPrice", "DirtyPrice"}),
        (QuantityUnit, 9, {"Shares", "Contracts", "NotionalAmount"}),
        (CurrencyRole, 7, {"Base", "Quote", "Settlement"}),
        (AccountType, 7, {"Cash", "Margin", "Custody"}),
        (BookType, 7, {"Trading", "Treasury", "Custody"}),
        (PositionType, 6, {"Long", "Short", "Net"}),
        (InventoryType, 7, {"Available", "Borrowed", "PendingSettlement"}),
        (StrategyType, 7, {"MarketMaking", "Arbitrage", "Execution"}),
        (NettingType, 6, {"None", "Bilateral", "Portfolio"}),
        (
            VehicleWrapper,
            7,
            {"ExchangeTradedFund", "SocieteInvestissementCapitalVariable", "LimitedPartnership"},
        ),
        (DistributionPolicy, 6, {"Accumulating", "Distributing", "Mixed"}),
        (ShareClassHedging, 6, {"Unhedged", "CurrencyHedged", "PartialHedged"}),
        (LiquidityTerm, 7, {"Daily", "Monthly", "Annual"}),
        (RedemptionFrequency, 7, {"Daily", "Quarterly", "AtMaturity"}),
        (CorporateActionType, 10, {"CashDividend", "Merger", "Delisting"}),
        (ListingStatus, 7, {"Listed", "Suspended", "PendingDelisting"}),
        (SecurityStatus, 8, {"Active", "Matured", "Expired"}),
        (ExerciseEventType, 6, {"Automatic", "Assignment", "EarlyExercise"}),
        (TenderOfferType, 6, {"Cash", "Mixed", "ExchangeOffer"}),
        (DelistingReason, 7, {"Merger", "Regulatory", "FailureToMeetRequirements"}),
    ],
)
def test_identifier_portfolio_fund_and_lifecycle_enum_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type) == expected_count
    assert expected_members.issubset(enum_type.__members__)
