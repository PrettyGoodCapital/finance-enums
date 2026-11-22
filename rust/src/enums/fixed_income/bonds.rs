//! Bond classification, coupons, ranking, and redemption.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum BondType {
    Invalid = 0,
    Corporate,
    Government,
    Municipal,
    Agency,
    Supranational,
    CoveredBond,
    AssetBacked,
    MortgageBacked,
    Convertible,
    StructuredNote,
    CollateralizedDebtObligation,
}

/// Kind of entity that issues a debt security.
#[abi_safe_enum]
pub enum IssuerType {
    Invalid = 0,
    Sovereign,
    CentralBank,
    QuasiGovernment,
    RegionalGovernment,
    LocalGovernment,
    Supranational,
    Corporate,
    FinancialInstitution,
    SpecialPurposeVehicle,
    Fund,
}

#[abi_safe_enum]
pub enum CouponType {
    Invalid = 0,
    Fixed,
    Floating,
    Zero,
    StepUp,
    InflationLinked,
    PaymentInKind,
    InverseFloating,
    IndexLinked,
    Structured,
    StepDown,
    InterestOnly,
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
    SeniorNonPreferred,
    LowerTierTwoSubordinated,
    UpperTierTwoSubordinated,
    TierOneSubordinated,
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

/// Embedded options and redemption features of a debt security.
#[abi_safe_enum]
pub enum RedemptionFeature {
    Invalid = 0,
    Callable,
    Puttable,
    Convertible,
    Exchangeable,
    ContingentConvertible,
    Sinkable,
    Extendible,
    Perpetual,
    MakeWholeCallable,
}

/// Guarantee or security backing a debt security (ISO 10962 guarantee attribute).
#[abi_safe_enum]
pub enum DebtGuaranteeType {
    Invalid = 0,
    GovernmentGuaranteed,
    JointlyGuaranteed,
    Secured,
    Unsecured,
    NegativePledge,
}

/// Legal form in which a security is held.
#[abi_safe_enum]
pub enum SecurityForm {
    Invalid = 0,
    Bearer,
    Registered,
    BearerOrRegistered,
}

/// Collateral pools behind asset-backed securities.
#[abi_safe_enum]
pub enum AssetBackedCollateralType {
    Invalid = 0,
    HomeEquityLoan,
    AutoLoan,
    StudentLoan,
    CreditCardReceivable,
    Mortgage,
    Other,
}
