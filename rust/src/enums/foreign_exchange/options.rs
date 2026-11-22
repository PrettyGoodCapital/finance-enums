//! FX option quoting conventions.

use abi_safe_enum::abi_safe_enum;

/// Delta conventions for FX option quotes.
#[abi_safe_enum]
pub enum ForeignExchangeDeltaConvention {
    Invalid = 0,
    Spot,
    Forward,
    PremiumAdjustedSpot,
    PremiumAdjustedForward,
}

/// At-the-money strike conventions for FX options.
#[abi_safe_enum]
pub enum ForeignExchangeAtTheMoneyConvention {
    Invalid = 0,
    Spot,
    Forward,
    DeltaNeutral,
    PutCallFiftyDelta,
}

/// Market quotes that define an FX volatility smile.
#[abi_safe_enum]
pub enum ForeignExchangeVolatilityQuoteType {
    Invalid = 0,
    AtTheMoney,
    RiskReversal,
    Butterfly,
}

/// How an option strike in one currency against another is quoted.
#[abi_safe_enum]
pub enum OptionStrikeQuoteBasis {
    Invalid = 0,
    PutCurrencyPerCallCurrency,
    CallCurrencyPerPutCurrency,
}

/// How an option premium is quoted.
#[abi_safe_enum]
pub enum OptionPremiumQuoteBasis {
    Invalid = 0,
    PercentageOfCallCurrencyAmount,
    PercentageOfPutCurrencyAmount,
    CallCurrencyPerPutCurrency,
    PutCurrencyPerCallCurrency,
    Explicit,
}
