//! General contract terms.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum ContractStyle {
    Invalid = 0,
    Standardized,
    NonStandardized,
}

#[abi_safe_enum]
pub enum ContractUnit {
    Invalid = 0,
    Share,
    Unit,
    Contract,
    CurrencyAmount,
    NotionalAmount,
    IndexPoint,
}

#[abi_safe_enum]
pub enum PayoffStyle {
    Invalid = 0,
    Linear,
    Optional,
    Binary,
}

#[abi_safe_enum]
pub enum LegRole {
    Invalid = 0,
    Payer,
    Receiver,
    Buyer,
    Seller,
}
