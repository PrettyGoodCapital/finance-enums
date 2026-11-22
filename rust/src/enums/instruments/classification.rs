//! Broad security, instrument, and underlying classes.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum SecurityType {
    Invalid = 0,
    Equity,
    Option,
    Bond,
    Forward,
    Future,
    PerpetualFuture,
    Swap,
    Financing,
    Spread,
    Fund,
    Commodity,
    Currency,
    Pair,
    Index,
    Warrant,
    Right,
}

#[abi_safe_enum]
pub enum InstrumentType {
    Invalid = 0,
    Spot,
    Option,
    Forward,
    Future,
    Swap,
    Financing,
    Right,
    Warrant,
    Spread,
    Pair,
    Basket,
}

#[abi_safe_enum]
pub enum UnderlyingAssetClass {
    Invalid = 0,
    Agriculture,
    Basket,
    Commodity,
    Credit,
    Currency,
    Debt,
    Energy,
    Environmental,
    Equity,
    ExtractionResources,
    Future,
    GeneratedResources,
    Index,
    IndustrialProducts,
    InterestRate,
    Metals,
    MixedAssets,
    Option,
    Other,
    Paper,
    PolypropyleneProducts,
    Services,
    StockDividend,
    Swap,
}
