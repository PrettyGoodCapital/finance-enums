//! Orders, executions, and market-data conditions.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum OrderType {
    Invalid = 0,
    Limit,
    Market,
    Stop,
    StopLimit,
    MarketOnClose,
    LimitOnClose,
    Pegged,
}

#[abi_safe_enum]
pub enum OrderStatus {
    Invalid = 0,
    New,
    PendingNew,
    PartiallyFilled,
    Filled,
    Canceled,
    Rejected,
    Expired,
    Suspended,
    PendingCancel,
}

#[abi_safe_enum]
pub enum OrderSide {
    Invalid = 0,
    Buy,
    Sell,
    SellShort,
    BuyToCover,
}

#[abi_safe_enum]
pub enum Side {
    Invalid = 0,
    Buy,
    Sell,
}

#[abi_safe_enum]
pub enum OrderFlag {
    Invalid = 0,
    None,
    FillOrKill,
    AllOrNone,
    ImmediateOrCancel,
}

#[abi_safe_enum]
pub enum OrderCapacity {
    Invalid = 0,
    Agency,
    Principal,
    RisklessPrincipal,
    Proprietary,
    MarketMaker,
}

#[abi_safe_enum]
pub enum TimeInForce {
    Invalid = 0,
    None,
    Day,
    GoodTillCanceled,
    ImmediateOrCancel,
    FillOrKill,
    GoodTillDate,
    AtOpen,
    AtClose,
}

#[abi_safe_enum]
pub enum ExecutionType {
    Invalid = 0,
    New,
    Trade,
    Canceled,
    Replaced,
    Rejected,
    Expired,
    TradeCorrect,
    TradeCancel,
}

#[abi_safe_enum]
pub enum ExecutionInstruction {
    Invalid = 0,
    AllOrNone,
    DoNotIncrease,
    DoNotReduce,
    ParticipateDoNotInitiate,
    StayOnOfferSide,
    StayOnBidSide,
    LastPeg,
    MidPricePeg,
}

#[abi_safe_enum]
pub enum ExecutionDisposition {
    Invalid = 0,
    Regular,
    Bust,
    Correct,
}

#[abi_safe_enum]
pub enum LiquidityFlag {
    Invalid = 0,
    Added,
    Removed,
    RoutedOut,
    Auction,
    None,
    Neutral,
}

#[abi_safe_enum]
pub enum PositionEffect {
    Invalid = 0,
    Open,
    Close,
    CloseToday,
    CloseYesterday,
    Rolled,
}

#[abi_safe_enum]
pub enum ShortSaleRestriction {
    Invalid = 0,
    None,
    AlternativeUptickRule,
    UptickRule,
    LocateRequired,
    BorrowRequired,
}

#[abi_safe_enum]
pub enum QuoteCondition {
    Invalid = 0,
    Regular,
    Indicative,
    Manual,
    FastTrading,
    SlowTrading,
    Closed,
}

#[abi_safe_enum]
pub enum TradeCondition {
    Invalid = 0,
    Regular,
    Auction,
    AveragePrice,
    Block,
    DerivativelyPriced,
    PriorReferencePrice,
    OutOfSequence,
    Canceled,
}

#[abi_safe_enum]
pub enum CrossType {
    Invalid = 0,
    Internal,
    Exchange,
    Broker,
    OpeningAuction,
    ClosingAuction,
}

#[abi_safe_enum]
pub enum TickDirection {
    Invalid = 0,
    Up,
    Down,
}
