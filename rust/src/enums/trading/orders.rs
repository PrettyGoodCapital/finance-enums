//! Order terms and instructions.

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
    MarketIfTouched,
    MarketToLimit,
    TrailingStop,
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
    PendingReplace,
    DoneForDay,
    Stopped,
}

#[abi_safe_enum]
pub enum OrderSide {
    Invalid = 0,
    Buy,
    Sell,
    SellShort,
    BuyToCover,
    Cross,
    Undisclosed,
}

#[abi_safe_enum]
pub enum Side {
    Invalid = 0,
    Buy,
    Sell,
}

#[abi_safe_enum]
pub enum OrderCapacity {
    Invalid = 0,
    Agency,
    Principal,
    RisklessPrincipal,
    Proprietary,
    MarketMaker,
    Individual,
    MixedCapacity,
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
    GoodForAuction,
    GoodTillCrossing,
    AtCrossing,
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
    Held,
    NotHeld,
    IntermarketSweep,
    CancelOnTradingHalt,
    ReinstateOnTradingHalt,
    CancelOnConnectionLoss,
    NoCross,
    ExternalRoutingNotAllowed,
    ImbalanceOnly,
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
