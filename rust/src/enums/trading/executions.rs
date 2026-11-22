//! Execution reports and crosses.

use abi_safe_enum::abi_safe_enum;

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
    PendingNew,
    PendingCancel,
    PendingReplace,
    Restated,
    DoneForDay,
    Suspended,
    Stopped,
    OrderStatus,
    TriggeredOrActivatedBySystem,
}

#[abi_safe_enum]
pub enum LiquidityFlag {
    Invalid = 0,
    Added,
    Removed,
    RoutedOut,
    Auction,
    Neutral,
    TriggeredStopOrder,
    TriggeredMarketOrder,
}

/// Cross order types (FIX CrossType, tag 549).
#[abi_safe_enum]
pub enum CrossType {
    Invalid = 0,
    AllOrNone,
    ImmediateOrCancel,
    OneSide,
    SamePrice,
    Basis,
    Contingent,
    VolumeWeightedAveragePrice,
    CustomerToCustomer,
}
