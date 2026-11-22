//! Risk factor groupings.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum FactorGroup {
    Invalid = 0,
    Style,
    Industry,
    Country,
    Currency,
    Market,
}

#[abi_safe_enum]
pub enum FamaFrenchFactor {
    Invalid = 0,
    Market,
    Size,
    Value,
    Profitability,
    Investment,
}

#[abi_safe_enum]
pub enum StyleFactor {
    Invalid = 0,
    Value,
    Momentum,
    Quality,
    Size,
    Volatility,
    Yield,
}
