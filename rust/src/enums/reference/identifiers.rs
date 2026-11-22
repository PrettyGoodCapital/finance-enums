//! Instrument identifier schemes and ticker namespaces.

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

/// Acronym spelling of [`IdentifierType`]; the two stay ordinal-for-ordinal aligned.
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
