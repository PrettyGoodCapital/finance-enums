//! Settlement method, delivery, and status.

use abi_safe_enum::abi_safe_enum;

/// How a contract settles: by delivering the underlying or by paying cash (FIX SettlMethod, tag 1193).
#[abi_safe_enum]
pub enum SettlementType {
    Invalid = 0,
    Physical,
    Cash,
    NonDeliverable,
    ElectAtExercise,
}

/// How the asset and cash legs of a settlement are exchanged (FIX DeliveryType, tag 919).
#[abi_safe_enum]
pub enum DeliveryType {
    Invalid = 0,
    DeliveryVersusPayment,
    FreeOfPayment,
    PaymentVersusPayment,
    TriParty,
    HoldInCustody,
    DeliverByValue,
}

#[abi_safe_enum]
pub enum SettlementStatus {
    Invalid = 0,
    Pending,
    Instructed,
    Matched,
    Unmatched,
    Settled,
    PartiallySettled,
    Failed,
    Canceled,
}

#[abi_safe_enum]
pub enum SettlementFailReason {
    Invalid = 0,
    InsufficientSecurities,
    InsufficientCash,
    CounterpartyMismatch,
    InstructionMismatch,
    RegulatoryHold,
    MarketDeadlineMissed,
    CorporateAction,
    SystemIssue,
    Other,
}
