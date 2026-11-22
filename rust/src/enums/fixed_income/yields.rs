//! Yield and duration measures.

use abi_safe_enum::abi_safe_enum;

/// Yield measures (FIX YieldType, tag 235).
#[abi_safe_enum]
pub enum YieldType {
    Invalid = 0,
    AfterTaxYield,
    AnnualYield,
    YieldAtIssue,
    YieldToAverageMaturity,
    BookYield,
    YieldToNextCall,
    YieldChangeSinceClose,
    CompoundYield,
    CurrentYield,
    TrueGrossYield,
    YieldWithInflationAssumption,
    InverseFloaterBondYield,
    MostRecentClosingYield,
    YieldToLongestAverageLife,
    MarkToMarketYield,
    YieldToMaturity,
    YieldToNextRefund,
    OpenAverageYield,
    PreviousCloseYield,
    ProceedsYield,
    YieldToNextPut,
    SemiAnnualYield,
    YieldToShortestAverageLife,
    SimpleYield,
    TaxEquivalentYield,
    YieldToTenderDate,
    TrueYield,
    YieldToWorst,
}

/// Bond duration measures.
#[abi_safe_enum]
pub enum DurationType {
    Invalid = 0,
    Simple,
    Macaulay,
    Modified,
}
