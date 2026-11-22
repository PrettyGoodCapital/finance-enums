//! Futures contracts and calendar spreads.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum FutureAssetClass {
    Invalid = 0,
    Financial,
    Commodity,
}

#[abi_safe_enum]
pub enum FutureMonthCode {
    Invalid = 0,
    F,
    G,
    H,
    J,
    K,
    M,
    N,
    Q,
    U,
    V,
    X,
    Z,
}

#[abi_safe_enum]
pub enum FutureSpreadLegType {
    Invalid = 0,
    BuyLeg,
    SellLeg,
    NearLeg,
    FarLeg,
}

#[abi_safe_enum]
pub enum FutureSpreadSubType {
    Invalid = 0,
    Asset,
    Calendar,
}
