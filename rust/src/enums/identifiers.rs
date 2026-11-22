//! Instrument identifiers, symbology, and price and quantity notation.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum IdentifierType {
    Invalid = 0,
    Ticker,
    InternationalSecuritiesIdentificationNumber,
    CommitteeOnUniformSecuritiesIdentificationProcedures,
    StockExchangeDailyOfficialList,
    FinancialInstrumentGlobalIdentifier,
    LegalEntityIdentifier,
    ReutersInstrumentCode,
    PrimaryReutersInstrumentCode,
    BloombergTicker,
    MarketIdentifierCode,
    OptionsSymbologyInitiative,
    Internal,
}

/// Acronym spelling of [`IdentifierType`](super::IdentifierType); the two stay ordinal-for-ordinal aligned.
#[abi_safe_enum]
pub enum Symbology {
    Invalid = 0,
    Ticker,
    ISIN,
    CUSIP,
    SEDOL,
    FIGI,
    LEI,
    RIC,
    PrimaryRIC,
    BBGTicker,
    MIC,
    OSI,
    Internal,
}

#[abi_safe_enum]
pub enum TickerNamespace {
    Invalid = 0,
    Exchange,
    Composite,
    Bloomberg,
    Reuters,
    Vendor,
    OverTheCounter,
    Internal,
    Synthetic,
}

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
}
