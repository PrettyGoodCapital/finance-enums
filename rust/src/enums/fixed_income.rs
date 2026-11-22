//! Bond, rate, and swap conventions.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum CouponType {
    Invalid = 0,
    Fixed,
    Floating,
    Zero,
    StepUp,
    InflationLinked,
    PaymentInKind,
}

#[abi_safe_enum]
pub enum DayCountConvention {
    Invalid = 0,
    Actual360,
    Actual365Fixed,
    ActualActual,
    Thirty360,
    Thirty360European,
    Business252,
}

#[abi_safe_enum]
pub enum AmortizationType {
    Invalid = 0,
    Bullet,
    Linear,
    MortgageStyle,
    NegativeAmortization,
    SinkingFund,
    Accreting,
}

#[abi_safe_enum]
pub enum Seniority {
    Invalid = 0,
    SeniorSecured,
    SeniorUnsecured,
    SeniorSubordinated,
    Subordinated,
    JuniorSubordinated,
    Preferred,
}

#[abi_safe_enum]
pub enum ScheduleFrequency {
    Invalid = 0,
    Daily,
    Weekly,
    Monthly,
    Quarterly,
    SemiAnnual,
    Annual,
    AtMaturity,
    AdHoc,
}

#[abi_safe_enum]
pub enum RateIndex {
    Invalid = 0,
    SecuredOvernightFinancingRate,
    FedFunds,
    EuroShortTermRate,
    SterlingOvernightIndexAverage,
    EuroInterbankOfferedRate,
    TokyoOvernightAverageRate,
    SwissAverageRateOvernight,
    ConsumerPriceIndex,
}

#[abi_safe_enum]
pub enum CompoundingMethod {
    Invalid = 0,
    Simple,
    Compounded,
    Averaged,
    Flat,
    Straight,
}

#[abi_safe_enum]
pub enum StubType {
    Invalid = 0,
    None,
    ShortFront,
    ShortBack,
    LongFront,
    LongBack,
}

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
}
