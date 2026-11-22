//! Day count conventions.

use abi_safe_enum::abi_safe_enum;

/// Day count fraction conventions, as defined by ISDA and implemented by OpenGamma Strata.
#[abi_safe_enum]
pub enum DayCountConvention {
    Invalid = 0,
    /// Act/360
    Actual360,
    /// Act/365F
    Actual365Fixed,
    /// Act/Act ISDA
    ActualActualIsda,
    /// 30/360 ISDA (Bond Basis)
    Thirty360Isda,
    /// 30E/360 (Eurobond Basis)
    Thirty360European,
    /// Bus/252
    Business252,
    /// Act/Act ICMA
    ActualActualIcma,
    /// Act/Act AFB
    ActualActualAfb,
    /// Act/Act Year
    ActualActualYear,
    /// Act/365A
    Actual365Actual,
    /// Act/365L
    Actual365Leap,
    /// Act/364
    Actual364,
    /// Act/365.25
    Actual36525,
    /// NL/360
    NoLeap360,
    /// NL/365
    NoLeap365,
    /// 30U/360
    Thirty360UnitedStates,
    /// 30U/360 EOM
    Thirty360UnitedStatesEndOfMonth,
    /// 30/360 PSA
    Thirty360PublicSecuritiesAssociation,
    /// 30E/360 ISDA
    Thirty360EuropeanIsda,
    /// 30E+/360
    Thirty360EuropeanPlus,
    /// 30E/365
    Thirty365European,
    /// 1/1
    OneOne,
}
