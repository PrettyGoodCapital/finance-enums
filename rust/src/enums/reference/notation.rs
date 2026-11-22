//! How prices, quantities, and currency amounts are expressed.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum PriceNotation {
    Invalid = 0,
    Decimal,
    PercentageOfPar,
    Yield,
    Spread,
    BasisPoints,
    Volatility,
    IndexPoints,
    Pips,
    PerUnit,
    Percentage,
    CleanPrice,
    DirtyPrice,
    Discount,
    Premium,
    UpfrontPoints,
    PercentageOfNotional,
}

#[abi_safe_enum]
pub enum PriceKind {
    Invalid = 0,
    Bid,
    Ask,
    Mid,
    Last,
    Settlement,
    VolumeWeightedAveragePrice,
}

#[abi_safe_enum]
pub enum QuantityUnit {
    Invalid = 0,
    Shares,
    Contracts,
    Units,
    Lots,
    CurrencyAmount,
    NotionalAmount,
    FaceValue,
    Weight,
}

#[abi_safe_enum]
pub enum CurrencyRole {
    Invalid = 0,
    Base,
    Quote,
    Settlement,
    Margin,
    ProfitAndLoss,
    Reporting,
    Dealt,
    Call,
    Put,
    Premium,
}
