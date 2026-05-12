import pytest

from finance_enums import (
    AggressorSide,
    AuctionType,
    CountryCode,
    CrossType,
    ExecType,
    ExecutionInstruction,
    LiquidityFlag,
    MarketState,
    MarketStatusReason,
    MarketType,
    OpenClose,
    OrderCapacity,
    OrderStatus,
    PositionEffect,
    PriceType,
    QuoteCondition,
    SegmentType,
    ShortSaleRestriction,
    TradeCondition,
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
        (VenueType, 8, {"Exchange", "AlternativeTradingSystem", "MultilateralTradingFacility"}),
        (MarketType, 8, {"Equities", "FixedIncome", "ForeignExchange"}),
        (TradingSession, 8, {"PreOpen", "Continuous", "AfterHours"}),
        (MarketState, 6, {"PreOpen", "Open", "Halted"}),
        (AuctionType, 6, {"Opening", "Closing", "Volatility"}),
        (SegmentType, 7, {"Primary", "Segment", "Dark"}),
        (MarketStatusReason, 8, {"ScheduledOpen", "Regulatory", "Technical"}),
        (OrderStatus, 9, {"New", "PartiallyFilled", "Canceled"}),
        (ExecType, 8, {"New", "Trade", "Rejected"}),
        (ExecutionInstruction, 8, {"AllOrNone", "ParticipateDoNotInitiate", "MidPricePeg"}),
        (LiquidityFlag, 5, {"Added", "Removed", "Auction"}),
        (PositionEffect, 5, {"Open", "Close", "Rolled"}),
        (OpenClose, 4, {"Open", "Close", "CloseToday"}),
        (OrderCapacity, 5, {"Agency", "Principal", "RisklessPrincipal"}),
        (ShortSaleRestriction, 5, {"None", "LocateRequired", "BorrowRequired"}),
        (QuoteCondition, 6, {"Regular", "Indicative", "Closed"}),
        (TradeCondition, 8, {"Regular", "Auction", "OutOfSequence"}),
        (AggressorSide, 3, {"Buy", "Sell", "Unknown"}),
        (CrossType, 5, {"Internal", "Exchange", "ClosingAuction"}),
        (PriceType, 8, {"PerUnit", "Yield", "Volatility"}),
    ],
)
def test_market_and_trading_enum_surfaces(enum_type, expected_count, expected_members):
    assert len(enum_type.__members__) == expected_count
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

    assert xnys in exchange_records_by_country(CountryCode.US)
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
