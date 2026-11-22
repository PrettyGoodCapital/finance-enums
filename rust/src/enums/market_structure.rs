//! Venues, market categories, sessions, and market state.

use abi_safe_enum::abi_safe_enum;

#[abi_safe_enum]
pub enum VenueType {
    Invalid = 0,
    Exchange,
    AlternativeTradingSystem,
    MultilateralTradingFacility,
    OrganizedTradingFacility,
    DarkPool,
    ElectronicCommunicationNetwork,
    Dealer,
    RequestForQuote,
}

#[abi_safe_enum]
pub enum MarketType {
    Invalid = 0,
    Equities,
    FixedIncome,
    ForeignExchange,
    Commodities,
    Derivatives,
    Options,
    Futures,
    Funds,
    DigitalAssets,
    OverTheCounter,
}

#[abi_safe_enum]
pub enum MarketCategory {
    Invalid = 0,
    NotSpecified,
    MultilateralTradingFacility,
    SystematicInternalizer,
    RegulatedMarket,
    AlternativeTradingSystem,
    OrganizedTradingFacility,
    Other,
    SwapExecutionFacility,
    RegulatedMarketOffBookSegment,
    ApprovedPublicationArrangement,
    CryptoAssetServiceProvider,
    DesignatedContractMarket,
    TradeReportingFacility,
    InterDealerQuotationSystem,
}

#[abi_safe_enum]
pub enum VenueRegulatoryFlag {
    Invalid = 0,
    Multilateral,
    OrganizedTrading,
    TradeReporting,
    SwapExecution,
    Publication,
    SystematicInternalizer,
    RegulatedMarket,
    AlternativeTradingSystem,
    OffBookSegment,
    CryptoAssetServiceProvider,
    DesignatedContractMarket,
    InterDealerQuotation,
}

#[abi_safe_enum]
pub enum TradingSession {
    Invalid = 0,
    Day,
    HalfDay,
    Morning,
    Afternoon,
    Evening,
    PreMarket,
    AfterHours,
    Overnight,
}

#[abi_safe_enum]
pub enum TradingPhase {
    Invalid = 0,
    PreTrading,
    OpeningAuction,
    Continuous,
    IntradayAuction,
    VolatilityAuction,
    ClosingAuction,
    TradingAtLast,
    PostTrading,
    Closed,
    Break,
    PreCross,
    Cross,
    Quiescent,
    QuotingOnly,
}

#[abi_safe_enum]
pub enum MarketState {
    Invalid = 0,
    Open,
    Closed,
    Halted,
    Suspended,
}

#[abi_safe_enum]
pub enum AuctionType {
    Invalid = 0,
    Opening,
    Closing,
    Intraday,
    Volatility,
    Call,
    Indicative,
}

#[abi_safe_enum]
pub enum SegmentType {
    Invalid = 0,
    Primary,
    Secondary,
    Segment,
    Composite,
    Lit,
    Dark,
    Retail,
}

#[abi_safe_enum]
pub enum MarketStatusReason {
    Invalid = 0,
    ScheduledOpen,
    ScheduledClose,
    Halt,
    CircuitBreaker,
    Regulatory,
    Technical,
    Volatility,
    Holiday,
}
