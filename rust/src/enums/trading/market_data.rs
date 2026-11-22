//! Quote and trade conditions.

use abi_safe_enum::abi_safe_enum;

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
pub enum TickDirection {
    Invalid = 0,
    Up,
    Down,
}

/// Side of the order that removed liquidity in a trade. `NoAggressor` marks trades with none, such as implied or opening trades.
#[abi_safe_enum]
pub enum AggressorSide {
    Invalid = 0,
    Buy,
    Sell,
    NoAggressor,
}
