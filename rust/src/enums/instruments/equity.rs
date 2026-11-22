//! Equity securities.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum EquityType {
    Invalid = 0,
    Shares,
    PreferredShares,
    ConvertibleShares,
    PreferredConvertibleShares,
    DepositoryReceipt,
    Warrant,
    Right,
    Unit,
}
