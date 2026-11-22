//! Corporate actions and security lifecycle.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum CorporateActionType {
    Invalid = 0,
    CashDividend,
    StockDividend,
    StockSplit,
    ReverseSplit,
    RightsIssue,
    SpinOff,
    Merger,
    TenderOffer,
    Delisting,
}

#[abi_safe_enum]
pub enum CorporateActionAdjustmentType {
    Invalid = 0,
    None,
    PriceReturn,
    TotalReturn,
    NetTotalReturn,
    GrossTotalReturn,
    CapitalOnly,
    DivisorAdjustment,
}

#[abi_safe_enum]
pub enum ListingStatus {
    Invalid = 0,
    Listed,
    Suspended,
    Delisted,
    PendingListing,
    PendingDelisting,
    Unlisted,
}

#[abi_safe_enum]
pub enum SecurityStatus {
    Invalid = 0,
    Active,
    Inactive,
    Matured,
    Defaulted,
    Called,
    Converted,
    Expired,
}

#[abi_safe_enum]
pub enum ExerciseEventType {
    Invalid = 0,
    Automatic,
    Voluntary,
    Assignment,
    Expiration,
    EarlyExercise,
}

#[abi_safe_enum]
pub enum TenderOfferType {
    Invalid = 0,
    Cash,
    Stock,
    Mixed,
    DutchAuction,
    ExchangeOffer,
}

#[abi_safe_enum]
pub enum DelistingReason {
    Invalid = 0,
    Merger,
    Acquisition,
    Bankruptcy,
    Regulatory,
    Voluntary,
    FailureToMeetRequirements,
}
