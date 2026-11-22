//! Trading sessions, phases, and market state.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum TradingSession {
    Invalid = 0,
    Day,
    HalfDay,
    Morning,
    Afternoon,
    Evening,
    PreMarket,
    AfterHours,
    Overnight,
}

#[abi_safe_enum]
pub enum TradingPhase {
    Invalid = 0,
    PreTrading,
    OpeningAuction,
    Continuous,
    IntradayAuction,
    VolatilityAuction,
    ClosingAuction,
    TradingAtLast,
    PostTrading,
    Closed,
    Break,
    PreCross,
    Cross,
    Quiescent,
    QuotingOnly,
}

#[abi_safe_enum]
pub enum MarketState {
    Invalid = 0,
    Open,
    Closed,
    Halted,
    Suspended,
    Outage,
    PartialOutage,
    Delayed,
}

#[abi_safe_enum]
pub enum AuctionType {
    Invalid = 0,
    Opening,
    Closing,
    Intraday,
    Volatility,
    Call,
    Indicative,
}

#[abi_safe_enum]
pub enum MarketStatusReason {
    Invalid = 0,
    ScheduledOpen,
    ScheduledClose,
    Halt,
    CircuitBreaker,
    Regulatory,
    Technical,
    Volatility,
    Holiday,
}
