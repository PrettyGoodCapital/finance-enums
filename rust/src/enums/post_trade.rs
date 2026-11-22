//! Settlement, clearing, and allocation.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum SettlementType {
    Invalid = 0,
    Physical,
    Cash,
    NonDeliverable,
    ElectAtExercise,
    DeliveryVersusPayment,
    PaymentVersusPayment,
    FreeOfPayment,
    HoldInCustody,
    TriParty,
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

#[abi_safe_enum]
pub enum ClearingModel {
    Invalid = 0,
    Bilateral,
    CentralCounterparty,
    PrimeBroker,
    SponsoredAccess,
    AgentCleared,
}

#[abi_safe_enum]
pub enum ClearingHouse {
    Invalid = 0,
    NationalSecuritiesClearingCorporation,
    FixedIncomeClearingCorporation,
    OptionsClearingCorporation,
    ChicagoMercantileExchange,
    IntercontinentalExchangeClear,
    LondonClearingHouse,
    EurexClearing,
    DepositoryTrustClearingCorporation,
    Euroclear,
    Clearstream,
    Other,
}

#[abi_safe_enum]
pub enum AllocationMethod {
    Invalid = 0,
    AveragePrice,
    SpecificLot,
    ProRata,
    FirstInFirstOut,
    LastInFirstOut,
    Manual,
    Automated,
    StepOut,
}

#[abi_safe_enum]
pub enum GiveUpType {
    Invalid = 0,
    None,
    GiveUp,
    GiveIn,
    AveragePriceGiveUp,
    ClearingGiveUp,
}
