//! Security and instrument classification, including the CFI attribute families.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum SecurityType {
    Invalid = 0,
    Equity,
    Option,
    Bond,
    Forward,
    Future,
    PerpetualFuture,
    Swap,
    Financing,
    Spread,
    Fund,
    Commodity,
    Currency,
    Pair,
    Index,
    Warrant,
    Right,
}

#[abi_safe_enum]
pub enum InstrumentType {
    Invalid = 0,
    Spot,
    Option,
    Forward,
    Future,
    Swap,
    Financing,
    Right,
    Warrant,
    Spread,
    Pair,
    Basket,
}

#[abi_safe_enum]
pub enum EquityType {
    Invalid = 0,
    Shares,
    PreferredShares,
    ConvertibleShares,
    PreferredConvertibleShares,
    DepositoryReceipt,
    Warrant,
    Right,
    Unit,
}

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
pub enum BondType {
    Invalid = 0,
    Corporate,
    Government,
    Municipal,
}

#[abi_safe_enum]
pub enum FundType {
    Invalid = 0,
    ExchangeTradedFund,
    MutualFund,
    RealEstateInvestmentTrust,
    UnitTrust,
    SocieteInvestissementCapitalVariable,
    OpenEndedInvestmentCompany,
    LimitedPartnership,
}

#[abi_safe_enum]
pub enum FundSubType {
    Invalid = 0,
    Index,
    Sector,
    Active,
    Passive,
}

#[abi_safe_enum]
pub enum MutualFundEndedness {
    Invalid = 0,
    OpenEnded,
    ClosedEnded,
}

#[abi_safe_enum]
pub enum FutureAssetClass {
    Invalid = 0,
    Financial,
    Commodity,
}

#[abi_safe_enum]
pub enum FutureMonthCode {
    Invalid = 0,
    F,
    G,
    H,
    J,
    K,
    M,
    N,
    Q,
    U,
    V,
    X,
    Z,
}

#[abi_safe_enum]
pub enum FutureSpreadLegType {
    Invalid = 0,
    BuyLeg,
    SellLeg,
    NearLeg,
    FarLeg,
}

#[abi_safe_enum]
pub enum FutureSpreadSubType {
    Invalid = 0,
    Asset,
    Calendar,
}

#[abi_safe_enum]
pub enum ContractStyle {
    Invalid = 0,
    Standardized,
    NonStandardized,
}

#[abi_safe_enum]
pub enum ContractUnit {
    Invalid = 0,
    Share,
    Unit,
    Contract,
    CurrencyAmount,
    NotionalAmount,
    IndexPoint,
}

#[abi_safe_enum]
pub enum PayoffStyle {
    Invalid = 0,
    Linear,
    Optional,
    Binary,
}

#[abi_safe_enum]
pub enum LegRole {
    Invalid = 0,
    Payer,
    Receiver,
    Buyer,
    Seller,
}

#[abi_safe_enum]
pub enum UnderlyingAssetClass {
    Invalid = 0,
    Agriculture,
    Basket,
    Commodity,
    Credit,
    Currency,
    Debt,
    Energy,
    Environmental,
    Equity,
    ExtractionResources,
    Future,
    GeneratedResources,
    Index,
    IndustrialProducts,
    InterestRate,
    Metals,
    MixedAssets,
    Option,
    Other,
    Paper,
    PolypropyleneProducts,
    Services,
    StockDividend,
    Swap,
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
