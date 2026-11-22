//! Benchmarks and index administration.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum BenchmarkType {
    Invalid = 0,
    InterestRate,
    EquityIndex,
    FixedIncomeIndex,
    CommodityIndex,
    ForeignExchangeFixing,
    InflationIndex,
    CreditIndex,
    Custom,
}

#[abi_safe_enum]
pub enum IndexWeightingMethod {
    Invalid = 0,
    MarketCapitalization,
    FloatAdjustedMarketCapitalization,
    PriceWeighted,
    EqualWeighted,
    Fundamental,
    VolatilityWeighted,
    RiskParity,
    ModifiedMarketCapitalization,
}

#[abi_safe_enum]
pub enum CalculationAgentType {
    Invalid = 0,
    Exchange,
    BenchmarkAdministrator,
    IndexProvider,
    CalculationAgent,
    Dealer,
    IndependentAgent,
    Internal,
}
