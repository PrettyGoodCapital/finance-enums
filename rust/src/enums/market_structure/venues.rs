//! Venue and market categories.

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
