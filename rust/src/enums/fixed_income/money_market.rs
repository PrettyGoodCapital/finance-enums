//! Money market instruments.

use abi_safe_enum::abi_safe_enum;

/// Short-term debt instruments.
#[abi_safe_enum]
pub enum MoneyMarketInstrumentType {
    Invalid = 0,
    TreasuryBill,
    CommercialPaper,
    CertificateOfDeposit,
    BankersAcceptance,
    MediumTermNote,
    TimeDeposit,
    PromissoryNote,
    BankNote,
    EuroCommercialPaper,
}
