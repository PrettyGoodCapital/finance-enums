//! Swaps and other rate derivatives.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum SwapType {
    Invalid = 0,
    InterestRate,
    Commodity,
    Equity,
    Credit,
    ForeignExchange,
    Other,
}

#[abi_safe_enum]
pub enum SwapLegType {
    Invalid = 0,
    Fixed,
    Floating,
    Inflation,
    Credit,
    Equity,
    Commodity,
    ForeignExchange,
    Basis,
    Overnight,
}

/// Interest rate swap structures.
#[abi_safe_enum]
pub enum InterestRateSwapType {
    Invalid = 0,
    FixedForFloating,
    Basis,
    OvernightIndex,
    CrossCurrency,
    ZeroCouponInflation,
    YearOnYearInflation,
    Amortizing,
}

/// Interest rate derivative products.
#[abi_safe_enum]
pub enum InterestRateProductType {
    Invalid = 0,
    Swap,
    ForwardRateAgreement,
    Cap,
    Floor,
    Collar,
    Swaption,
    Future,
}

/// Cash settlement methods for swaptions (ISDA 2006, section 18.3).
#[abi_safe_enum]
pub enum SwaptionCashSettlementMethod {
    Invalid = 0,
    CashPrice,
    ParYield,
    ZeroCouponYield,
    CollateralizedCashPrice,
}
