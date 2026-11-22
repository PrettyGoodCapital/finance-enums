//! FX products, tenors, quoting, and fixings.

use abi_safe_enum::abi_safe_enum;

/// Foreign exchange products (FIX SecurityType FXSPOT, FXFWD, FXSWAP, FXNDF, FXNDS).
#[abi_safe_enum]
pub enum ForeignExchangeProductType {
    Invalid = 0,
    Spot,
    OutrightForward,
    Swap,
    NonDeliverableForward,
    NonDeliverableSwap,
}

/// Standard FX settlement tenors. There is no `Month12`: use `Year1`.
#[abi_safe_enum]
pub enum ForeignExchangeTenor {
    Invalid = 0,
    Today,
    Tomorrow,
    Spot,
    SpotNext,
    Day2,
    Day3,
    Day4,
    Week1,
    Week2,
    Week3,
    Month1,
    Month2,
    Month3,
    Month4,
    Month5,
    Month6,
    Month7,
    Month8,
    Month9,
    Month10,
    Month11,
    Month13,
    Month14,
    Month15,
    Month16,
    Month17,
    Month18,
    Month19,
    Month20,
    Month21,
    Month22,
    Month23,
    BrazilianFuturesRoll1,
    BrazilianFuturesRoll2,
    Year1,
    Year2,
    Year3,
    Year4,
    Year5,
    Year6,
    Year7,
    Year8,
    Year9,
    Year10,
    Year15,
    Year20,
    Year25,
    Year30,
    InternationalMonetaryMarket1,
    InternationalMonetaryMarket2,
    InternationalMonetaryMarket3,
    InternationalMonetaryMarket4,
    TomorrowNext,
    BrokenDate,
}

/// How an exchange rate is quoted.
#[abi_safe_enum]
pub enum ForeignExchangeQuoteBasis {
    Invalid = 0,
    BaseCurrencyPerQuoteCurrency,
    QuoteCurrencyPerBaseCurrency,
}

/// FX fixing benchmarks (FIX FXBenchmark).
#[abi_safe_enum]
pub enum ForeignExchangeBenchmark {
    Invalid = 0,
    WorldMarketsReuters,
    Bloomberg,
    EuropeanCentralBank,
    CentralBank,
    MitsubishiUfj,
    Other,
}
