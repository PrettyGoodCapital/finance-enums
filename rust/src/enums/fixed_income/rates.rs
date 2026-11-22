//! Rate indices and how rates accrue.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum RateIndex {
    Invalid = 0,
    SecuredOvernightFinancingRate,
    EffectiveFederalFundsRate,
    EuroShortTermRate,
    SterlingOvernightIndexAverage,
    EuroInterbankOfferedRate,
    TokyoOvernightAverageRate,
    SwissAverageRateOvernight,
    ConsumerPriceIndex,
}

/// How a floating leg compounds its spread across reset periods (FpML CompoundingMethodEnum).
#[abi_safe_enum]
pub enum CompoundingMethod {
    Invalid = 0,
    None,
    Straight,
    Flat,
    SpreadExclusive,
}

/// How an overnight-rate leg accrues across a period.
#[abi_safe_enum]
pub enum OvernightAccrualMethod {
    Invalid = 0,
    Compounded,
    OvernightCompoundedAnnualRate,
    Averaged,
    AveragedDaily,
}

/// How an inflation index value is read for a reference date.
#[abi_safe_enum]
pub enum PriceIndexCalculationMethod {
    Invalid = 0,
    Monthly,
    Interpolated,
    InterpolatedJapan,
}
