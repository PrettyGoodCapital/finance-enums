import pytest

from finance_enums import (
    AuctionType,
    CountryCodeAlpha2,
    CrossType,
    ExecutionInstruction,
    ExecutionType,
    LiquidityFlag,
    MarketState,
    MarketStatusReason,
    MarketType,
    OrderCapacity,
    OrderStatus,
    PositionEffect,
    PriceKind,
    QuoteCondition,
    SegmentType,
    ShortSaleRestriction,
    TradeCondition,
    TradingPhase,
    TradingSession,
    VenueType,
    exchange_record,
    exchange_records_by_country,
    exchange_records_by_market_category,
    exchange_records_by_operating_mic,
    exchange_records_by_parent_mic,
    exchange_records_by_region,
    exchange_records_by_status,
)


@pytest.mark.parametrize(
    ("enum_type", "expected_count", "expected_members"),
    [
        (VenueType, 9, {"Exchange", "AlternativeTradingSystem", "MultilateralTradingFacility"}),
        (MarketType, 11, {"Equities", "FixedIncome", "ForeignExchange", "Options", "Futures"}),
        (TradingSession, 9, {"Day", "PreMarket", "AfterHours", "Overnight"}),
        (TradingPhase, 15, {"PreTrading", "Continuous", "VolatilityAuction", "TradingAtLast", "QuotingOnly"}),
        (MarketState, 8, {"Open", "Closed", "Halted", "Suspended"}),
        (AuctionType, 7, {"Opening", "Closing", "Volatility"}),
        (SegmentType, 8, {"Primary", "Segment", "Dark"}),
        (MarketStatusReason, 9, {"ScheduledOpen", "Regulatory", "Technical"}),
        (OrderStatus, 13, {"New", "PartiallyFilled", "Canceled"}),
        (ExecutionType, 18, {"New", "Trade", "Rejected"}),
        (ExecutionInstruction, 18, {"AllOrNone", "ParticipateDoNotInitiate", "MidPricePeg"}),
        (LiquidityFlag, 8, {"Added", "Removed", "Auction", "Neutral"}),
        (PositionEffect, 6, {"Open", "Close", "CloseToday", "CloseYesterday", "Rolled"}),
        (OrderCapacity, 8, {"Agency", "Principal", "RisklessPrincipal"}),
        (ShortSaleRestriction, 6, {"None", "LocateRequired", "BorrowRequired"}),
        (QuoteCondition, 7, {"Regular", "Indicative", "Closed"}),
        (TradeCondition, 9, {"Regular", "Auction", "OutOfSequence"}),
        (CrossType, 9, {"AllOrNone", "SamePrice", "CustomerToCustomer"}),
        (PriceKind, 7, {"Bid", "Ask", "Mid", "Last", "Settlement", "VolumeWeightedAveragePrice"}),
    ],
)
def test_market_and_trading_enum_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type) == expected_count
    assert expected_members.issubset(enum_type.__members__)


def test_exchange_lookup_helpers_cover_additional_filters():
    xnys = exchange_record("XNYS")
    arcx = exchange_record("ARCX")
    xngs = exchange_record("XNGS")
    forex = exchange_record("FOREX")

    assert xnys is not None
    assert arcx is not None
    assert xngs is not None
    assert forex is not None

    assert xnys in exchange_records_by_country(CountryCodeAlpha2.US)
    assert arcx in exchange_records_by_operating_mic("XNYS")
    assert arcx in exchange_records_by_parent_mic("XNYS")
    assert xngs in exchange_records_by_status("UPDATED")
    assert forex in exchange_records_by_status("PROJECT")
    assert xnys in exchange_records_by_region("Americas")
    assert forex in exchange_records_by_region("Global")
    assert xnys in exchange_records_by_market_category("NSPD")
    assert arcx in exchange_records_by_market_category("RMKT")

    assert all(record.operating_mic == "XNYS" for record in exchange_records_by_operating_mic("XNYS"))
    assert all(record.parent_mic == "XNYS" for record in exchange_records_by_parent_mic("XNYS"))
    assert all(record.status == "UPDATED" for record in exchange_records_by_status("UPDATED"))
    assert all(record.region == "Global" for record in exchange_records_by_region("Global"))
    assert all(record.market_category_code == "RMKT" for record in exchange_records_by_market_category("RMKT"))

    assert exchange_records_by_operating_mic("ZZZZ") == []
    assert exchange_records_by_parent_mic("ZZZZ") == []
    assert exchange_records_by_status("MISSING") == []
    assert exchange_records_by_region("Atlantis") == []
    assert exchange_records_by_market_category("NONE") == []
