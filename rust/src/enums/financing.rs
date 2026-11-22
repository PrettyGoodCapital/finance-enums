//! Collateral, margin, borrowing, and repo.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum CollateralType {
    Invalid = 0,
    GeneralCollateral,
    SpecificCollateral,
    CashCollateral,
    GovernmentBonds,
    CorporateBonds,
    Equities,
}

#[abi_safe_enum]
pub enum MarginType {
    Invalid = 0,
    Initial,
    Variation,
    IndependentAmount,
    Maintenance,
    CrossMargin,
    PortfolioMargin,
}

#[abi_safe_enum]
pub enum BorrowType {
    Invalid = 0,
    StockLoan,
    SecuritiesLending,
    MarginLoan,
    RepoBorrow,
    UnsecuredBorrow,
}

#[abi_safe_enum]
pub enum RepoType {
    Invalid = 0,
    Bilateral,
    TriParty,
    HoldInCustody,
    Open,
    Term,
    Evergreen,
}

#[abi_safe_enum]
pub enum FinancingType {
    Invalid = 0,
    LoanLease,
    RepurchaseAgreement,
    SecuritiesLending,
}
