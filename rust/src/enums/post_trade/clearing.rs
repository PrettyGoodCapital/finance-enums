//! Clearing and allocation.

use abi_safe_enum::abi_safe_enum;

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
