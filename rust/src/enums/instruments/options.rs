//! Option terms and exotic features.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum OptionType {
    Invalid = 0,
    Call,
    Put,
}

#[abi_safe_enum]
pub enum OptionExerciseType {
    Invalid = 0,
    American,
    European,
    Bermudan,
}

#[abi_safe_enum]
pub enum ExoticOptionFeature {
    Invalid = 0,
    Barrier,
    Digital,
    Asian,
    Lookback,
    Cliquet,
    Chooser,
    Compound,
    Quanto,
}

#[abi_safe_enum]
pub enum BarrierType {
    Invalid = 0,
    UpAndIn,
    UpAndOut,
    DownAndIn,
    DownAndOut,
    DoubleKnockIn,
    DoubleKnockOut,
}

#[abi_safe_enum]
pub enum AveragingMethod {
    Invalid = 0,
    Arithmetic,
    Geometric,
    Weighted,
    VolumeWeighted,
    SpotAverage,
}

/// Touch and no-touch digital option styles.
#[abi_safe_enum]
pub enum TouchType {
    Invalid = 0,
    OneTouch,
    NoTouch,
    DoubleOneTouch,
    DoubleNoTouch,
}

/// When a digital or touch option pays out.
#[abi_safe_enum]
pub enum PayoutTiming {
    Invalid = 0,
    Immediate,
    Deferred,
}
