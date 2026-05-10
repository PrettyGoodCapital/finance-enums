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
        (IdentifierType, 10, {"Ticker", "ISIN", "FIGI"}),
        (TickerNamespace, 8, {"Exchange", "Composite", "Bloomberg"}),
        (PriceNotation, 8, {"Decimal", "Yield", "BasisPoints"}),
        (QuantityUnit, 8, {"Shares", "Contracts", "NotionalAmount"}),
        (CurrencyRole, 6, {"Base", "Quote", "Settlement"}),
        (AccountType, 6, {"Cash", "Margin", "Custody"}),
        (BookType, 6, {"Trading", "Treasury", "Custody"}),
        (PositionType, 5, {"Long", "Short", "Net"}),
        (InventoryType, 6, {"Available", "Borrowed", "PendingSettlement"}),
        (StrategyType, 6, {"MarketMaking", "Arbitrage", "Execution"}),
        (NettingType, 5, {"None", "Bilateral", "Portfolio"}),
        (VehicleWrapper, 6, {"ETF", "SICAV", "LimitedPartnership"}),
        (DistributionPolicy, 5, {"Accumulating", "Distributing", "Mixed"}),
        (ShareClassHedging, 5, {"Unhedged", "CurrencyHedged", "PartialHedged"}),
        (LiquidityTerm, 6, {"Daily", "Monthly", "Annual"}),
        (RedemptionFrequency, 6, {"Daily", "Quarterly", "AtMaturity"}),
        (CorporateActionType, 9, {"CashDividend", "Merger", "Delisting"}),
        (ListingStatus, 6, {"Listed", "Suspended", "PendingDelisting"}),
        (SecurityStatus, 7, {"Active", "Matured", "Expired"}),
        (ExerciseEventType, 5, {"Automatic", "Assignment", "EarlyExercise"}),
        (TenderOfferType, 5, {"Cash", "Mixed", "ExchangeOffer"}),
        (DelistingReason, 6, {"Merger", "Regulatory", "FailureToMeetRequirements"}),
    ],
)
def test_identifier_portfolio_fund_and_lifecycle_enum_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type.__members__) == expected_count
    assert expected_members.issubset(enum_type.__members__)
