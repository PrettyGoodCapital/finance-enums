import pytest

from finance_enums import (
    AccountType,
    BookType,
    CorporateActionType,
    CurrencyRole,
    DelistingReason,
    DistributionPolicy,
    ExerciseEventType,
    FundType,
    IdentifierType,
    InventoryType,
    ListingStatus,
    NettingType,
    PositionType,
    PriceNotation,
    QuantityUnit,
    SecurityStatus,
    ShareClassHedging,
    StrategyType,
    TenderOfferType,
    TickerNamespace,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_count", "expected_members"),
    [
        (
            IdentifierType,
            13,
            {
                "Ticker",
                "InternationalSecuritiesIdentificationNumber",
                "FinancialInstrumentGlobalIdentifier",
            },
        ),
        (TickerNamespace, 9, {"Exchange", "Composite", "Bloomberg"}),
        (PriceNotation, 17, {"Decimal", "Yield", "BasisPoints", "PerUnit", "CleanPrice", "DirtyPrice"}),
        (QuantityUnit, 9, {"Shares", "Contracts", "NotionalAmount"}),
        (CurrencyRole, 11, {"Base", "Quote", "Settlement"}),
        (AccountType, 7, {"Cash", "Margin", "Custody"}),
        (BookType, 7, {"Trading", "Treasury", "Custody"}),
        (PositionType, 6, {"Long", "Short", "Net"}),
        (InventoryType, 7, {"Available", "Borrowed", "PendingSettlement"}),
        (StrategyType, 7, {"MarketMaking", "Arbitrage", "Execution"}),
        (NettingType, 6, {"None", "Bilateral", "Portfolio"}),
        (
            FundType,
            8,
            {"ExchangeTradedFund", "SocieteInvestissementCapitalVariable", "LimitedPartnership"},
        ),
        (DistributionPolicy, 6, {"Accumulating", "Distributing", "Mixed"}),
        (ShareClassHedging, 6, {"Unhedged", "CurrencyHedged", "PartialHedged"}),
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
