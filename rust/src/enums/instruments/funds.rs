//! Funds and fund share classes.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum FundType {
    Invalid = 0,
    ExchangeTradedFund,
    MutualFund,
    RealEstateInvestmentTrust,
    UnitTrust,
    SocieteInvestissementCapitalVariable,
    OpenEndedInvestmentCompany,
    LimitedPartnership,
}

#[abi_safe_enum]
pub enum FundSubType {
    Invalid = 0,
    Index,
    Sector,
    Active,
    Passive,
}

#[abi_safe_enum]
pub enum MutualFundEndedness {
    Invalid = 0,
    OpenEnded,
    ClosedEnded,
}

#[abi_safe_enum]
pub enum DistributionPolicy {
    Invalid = 0,
    Accumulating,
    Distributing,
    Income,
    Growth,
    Mixed,
}

#[abi_safe_enum]
pub enum ShareClassHedging {
    Invalid = 0,
    Unhedged,
    CurrencyHedged,
    DurationHedged,
    CommodityHedged,
    PartialHedged,
}
