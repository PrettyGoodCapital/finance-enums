//! Schedule generation: business days, rolls, stubs, and frequencies.

use abi_safe_enum::abi_safe_enum;

/// How a date that falls on a non-business day is adjusted.
#[abi_safe_enum]
pub enum BusinessDayConvention {
    Invalid = 0,
    Unadjusted,
    Following,
    ModifiedFollowing,
    Preceding,
    ModifiedPreceding,
    Nearest,
    FloatingRateNote,
}

/// Day of the month or week on which schedule dates fall, before business day adjustment.
#[abi_safe_enum]
pub enum RollConvention {
    Invalid = 0,
    None,
    EndOfMonth,
    InternationalMoneyMarket,
    InternationalMoneyMarketAustralia,
    InternationalMoneyMarketCanada,
    InternationalMoneyMarketNewZealand,
    SydneyFuturesExchange,
    TreasuryBill,
    FloatingRateNote,
    DayOfMonth1,
    DayOfMonth2,
    DayOfMonth3,
    DayOfMonth4,
    DayOfMonth5,
    DayOfMonth6,
    DayOfMonth7,
    DayOfMonth8,
    DayOfMonth9,
    DayOfMonth10,
    DayOfMonth11,
    DayOfMonth12,
    DayOfMonth13,
    DayOfMonth14,
    DayOfMonth15,
    DayOfMonth16,
    DayOfMonth17,
    DayOfMonth18,
    DayOfMonth19,
    DayOfMonth20,
    DayOfMonth21,
    DayOfMonth22,
    DayOfMonth23,
    DayOfMonth24,
    DayOfMonth25,
    DayOfMonth26,
    DayOfMonth27,
    DayOfMonth28,
    DayOfMonth29,
    DayOfMonth30,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday,
}

#[abi_safe_enum]
pub enum StubType {
    Invalid = 0,
    None,
    ShortFront,
    ShortBack,
    LongFront,
    LongBack,
    SmartFront,
    SmartBack,
    Both,
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
    Biweekly,
    EveryFourWeeks,
    EveryTwoMonths,
    EveryFourMonths,
}

/// Unit of a tenor or period length.
#[abi_safe_enum]
pub enum PeriodUnit {
    Invalid = 0,
    Day,
    Week,
    Month,
    Year,
}

/// Whether a reset or payment happens at the start (in advance) or end (in arrears) of its period.
#[abi_safe_enum]
pub enum PeriodTiming {
    Invalid = 0,
    PeriodStart,
    PeriodEnd,
}
