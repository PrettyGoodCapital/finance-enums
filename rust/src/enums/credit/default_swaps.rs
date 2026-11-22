//! Credit default swap terms and credit events.

use abi_safe_enum::abi_safe_enum;

/// Credit default swap restructuring clauses.
#[abi_safe_enum]
pub enum RestructuringClause {
    Invalid = 0,
    NoRestructuring,
    FullRestructuring,
    ModifiedRestructuring,
    ModifiedModifiedRestructuring,
}

/// ISDA credit events.
#[abi_safe_enum]
pub enum CreditEventType {
    Invalid = 0,
    Bankruptcy,
    FailureToPay,
    Restructuring,
    ObligationAcceleration,
    ObligationDefault,
    RepudiationMoratorium,
    GovernmentalIntervention,
    Writedown,
    ImpliedWritedown,
    MaturityExtension,
    DistressedRatingsDowngrade,
}

/// ISDA obligation and deliverable obligation categories.
#[abi_safe_enum]
pub enum ObligationCategory {
    Invalid = 0,
    Payment,
    BorrowedMoney,
    ReferenceObligationsOnly,
    Bond,
    Loan,
    BondOrLoan,
}

/// ISDA obligation and deliverable obligation characteristics.
#[abi_safe_enum]
pub enum ObligationCharacteristic {
    Invalid = 0,
    NotSubordinated,
    SpecifiedCurrency,
    NotSovereignLender,
    NotDomesticCurrency,
    NotDomesticLaw,
    Listed,
    NotDomesticIssuance,
    NotContingent,
    AssignableLoan,
    ConsentRequiredLoan,
    DirectLoanParticipation,
    Transferable,
    MaximumMaturity,
    AcceleratedOrMatured,
    NotBearer,
}

/// ISDA physical settlement matrix transaction types.
#[abi_safe_enum]
pub enum CreditDefaultSwapTransactionType {
    Invalid = 0,
    NorthAmericanCorporate,
    EuropeanCorporate,
    EuropeanFinancialCorporate,
    WesternEuropeanSovereign,
    EmergingEuropeanCorporate,
    AsiaCorporate,
    AsiaSovereign,
    JapanCorporate,
    JapanSovereign,
    AustraliaCorporate,
    LatinAmericaSovereign,
    NewZealandCorporate,
    SingaporeCorporate,
}
