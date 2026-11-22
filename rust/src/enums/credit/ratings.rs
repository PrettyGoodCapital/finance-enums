//! Credit ratings.

use abi_safe_enum::abi_safe_enum;

/// Credit rating agencies.
#[abi_safe_enum]
pub enum CreditRatingAgency {
    Invalid = 0,
    StandardAndPoors,
    Moodys,
    Fitch,
    DominionBondRatingService,
    AmBest,
    JapanCreditRatingAgency,
    RatingAndInvestmentInformation,
    KrollBondRatingAgency,
    ScopeRatings,
}

/// Direction a rating agency expects a rating to move.
#[abi_safe_enum]
pub enum CreditRatingOutlook {
    Invalid = 0,
    Positive,
    Negative,
    Stable,
    Developing,
}

/// Broad credit quality bands.
#[abi_safe_enum]
pub enum CreditQuality {
    Invalid = 0,
    InvestmentGrade,
    HighYield,
    Distressed,
    Defaulted,
}
