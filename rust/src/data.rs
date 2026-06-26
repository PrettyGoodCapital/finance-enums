// Static data tables for finance enums.
// Currency tables are maintained in `currency_data.rs` as structured records.
//
// ABI STABILITY CONTRACT:
// - Variants are append-only. NEVER reorder or remove existing entries.
// - Ordinal values (0-based index) are part of the stable ABI and are
//   persisted in databases, serialized formats, and compiled C/C++ code.
// - New variants MUST be appended at the end of each array.
// - If a variant is deprecated, keep it in place and add a new one at the end.
#![allow(dead_code, non_upper_case_globals, non_camel_case_types)]

pub use crate::currency_data::{
    currency_record, CurrencyAliasRecord, CurrencyAliasRecordRaw, CurrencyDataExportV1,
    CurrencyName_ARRAY, CurrencyRecord, CurrencyRecordRaw, Currency_ALIASES, Currency_CODES_ARRAY,
    Currency_VARIANTS, Currency_names_ARRAY, CURRENCY_ALIAS_RECORDS, CURRENCY_ALIAS_RECORDS_RAW,
    CURRENCY_EXPORT_ABI_VERSION, CURRENCY_EXPORT_V1, CURRENCY_RECORDS, CURRENCY_RECORDS_RAW,
};
pub use crate::exchange_codes::ExchangeCode_VARIANTS;
pub use crate::exchange_data::{exchange_record, exchange_records, ExchangeRecord};

finance_enum!(AgricultureType: Corn, Wheat, Oats, Soybean, Cocoa, Coffee, Sugar, Cotton, OrangeJuice, Cattle, Hogs);
pub static AgricultureType_VARIANTS: &[&str] = AgricultureType::VARIANTS;

finance_enum!(BondType: Corporate, Government, Municipal);
pub static BondType_VARIANTS: &[&str] = BondType::VARIANTS;

finance_enum!(CommodityType: Energy, Metals, Agriculture, Livestock, Softs, Lumber, Freight, Carbon);
pub static CommodityType_VARIANTS: &[&str] = CommodityType::VARIANTS;

finance_enum!(LivestockType: Cattle, Feeder, Hogs);
pub static LivestockType_VARIANTS: &[&str] = LivestockType::VARIANTS;

finance_enum_raw!(CountryCode: XX, AD, AE, AF, AG, AI, AL, AM, AO, AQ, AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD, BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO, BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC, CD, CF, CG, CH, CI, CK, CL, CM, CN, CO, CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK, DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET, FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE, GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR, GS, GT, GU, GW, GY, HK, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JM, JO, JP, KE, KG, KH, KI, KM, KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI, LK, LR, LS, LT, LU, LV, LY, MA, MC, MD, ME, MF, MG, MH, MK, ML, MM, MN, MO, MP, MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NR, NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, QA, RE, RO, RS, RU, RW, SA, SB, SC, SD, SE, SG, SH, SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST, SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ, TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ, UA, UG, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, VU, WF, WS, YE, YT, ZA, ZM, ZW, XK);
pub static CountryCode_VARIANTS: &[&str] = CountryCode::VARIANTS;

finance_enum_raw!(CountryCode3: XXX, AND, ARE, AFG, ATG, AIA, ALB, ARM, AGO, ATA, ARG, ASM, AUT, AUS, ABW, ALA, AZE, BIH, BRB, BGD, BEL, BFA, BGR, BHR, BDI, BEN, BLM, BMU, BRN, BOL, BES, BRA, BHS, BTN, BVT, BWA, BLR, BLZ, CAN, CCK, COD, CAF, COG, CHE, CIV, COK, CHL, CMR, CHN, COL, CRI, CUB, CPV, CUW, CXR, CYP, CZE, DEU, DJI, DNK, DMA, DOM, DZA, ECU, EST, EGY, ESH, ERI, ESP, ETH, FIN, FJI, FLK, FSM, FRO, FRA, GAB, GBR, GRD, GEO, GUF, GGY, GHA, GIB, GRL, GMB, GIN, GLP, GNQ, GRC, SGS, GTM, GUM, GNB, GUY, HKG, HMD, HND, HRV, HTI, HUN, IDN, IRL, ISR, IMN, IND, IOT, IRQ, IRN, ISL, ITA, JEY, JAM, JOR, JPN, KEN, KGZ, KHM, KIR, COM, KNA, PRK, KOR, KWT, CYM, KAZ, LAO, LBN, LCA, LIE, LKA, LBR, LSO, LTU, LUX, LVA, LBY, MAR, MCO, MDA, MNE, MAF, MDG, MHL, MKD, MLI, MMR, MNG, MAC, MNP, MTQ, MRT, MSR, MLT, MUS, MDV, MWI, MEX, MYS, MOZ, NAM, NCL, NER, NFK, NGA, NIC, NLD, NOR, NPL, NRU, NIU, NZL, OMN, PAN, PER, PYF, PNG, PHL, PAK, POL, SPM, PCN, PRI, PSE, PRT, PLW, PRY, QAT, REU, ROU, SRB, RUS, RWA, SAU, SLB, SYC, SDN, SWE, SGP, SHN, SVN, SJM, SVK, SLE, SMR, SEN, SOM, SUR, SSD, STP, SLV, SXM, SYR, SWZ, TCA, TCD, ATF, TGO, THA, TJK, TKL, TLS, TKM, TUN, TON, TUR, TTO, TUV, TWN, TZA, UKR, UGA, UMI, USA, URY, UZB, VAT, VCT, VEN, VGB, VIR, VNM, VUT, WLF, WSM, YEM, MYT, ZAF, ZMB, ZWE, UNK);
pub static CountryCode3_VARIANTS: &[&str] = CountryCode3::VARIANTS;

finance_enum!(EnergyType: Crude, NaturalGas, HeatingOil, Gasoline, Electricity, LiquefiedNaturalGas, Propane, Uranium);
pub static EnergyType_VARIANTS: &[&str] = EnergyType::VARIANTS;

finance_enum!(EquityType: Shares, PreferredShares, ConvertibleShares, PreferredConvertibleShares, DepositoryReceipt, Warrant, Right, Unit);
pub static EquityType_VARIANTS: &[&str] = EquityType::VARIANTS;

finance_enum!(FundSubType: Index, Sector, Active, Passive);
pub static FundSubType_VARIANTS: &[&str] = FundSubType::VARIANTS;

finance_enum!(FundType: ExchangeTradedFund, MutualFund, RealEstateInvestmentTrust);
pub static FundType_VARIANTS: &[&str] = FundType::VARIANTS;

finance_enum!(VenueType: Exchange, AlternativeTradingSystem, MultilateralTradingFacility, OrganizedTradingFacility, DarkPool, ElectronicCommunicationNetwork, Dealer, RequestForQuote);
pub static VenueType_VARIANTS: &[&str] = VenueType::VARIANTS;

finance_enum!(MarketType: Equities, FixedIncome, ForeignExchange, Commodities, Derivatives, Options, Futures, Funds, DigitalAssets, OverTheCounter);
pub static MarketType_VARIANTS: &[&str] = MarketType::VARIANTS;

finance_enum!(TradingSession: PreOpen, OpeningAuction, Continuous, IntradayAuction, ClosingAuction, PostClose, AfterHours, Overnight);
pub static TradingSession_VARIANTS: &[&str] = TradingSession::VARIANTS;

finance_enum!(MarketState: PreOpen, Open, Auction, Closed, Halted, Suspended);
pub static MarketState_VARIANTS: &[&str] = MarketState::VARIANTS;

finance_enum!(AuctionType: Opening, Closing, Intraday, Volatility, Call, Indicative);
pub static AuctionType_VARIANTS: &[&str] = AuctionType::VARIANTS;

finance_enum!(SegmentType: Primary, Secondary, Segment, Composite, Lit, Dark, Retail);
pub static SegmentType_VARIANTS: &[&str] = SegmentType::VARIANTS;

finance_enum!(MarketStatusReason: ScheduledOpen, ScheduledClose, Halt, CircuitBreaker, Regulatory, Technical, Volatility, Holiday);
pub static MarketStatusReason_VARIANTS: &[&str] = MarketStatusReason::VARIANTS;

finance_enum!(IdentifierType: Ticker, InternationalSecuritiesIdentificationNumber, CommitteeOnUniformSecuritiesIdentificationProcedures, StockExchangeDailyOfficialList, FinancialInstrumentGlobalIdentifier, LegalEntityIdentifier, ReutersInstrumentCode, Bloomberg, MarketIdentifierCode, Internal);
pub static IdentifierType_VARIANTS: &[&str] = IdentifierType::VARIANTS;

finance_enum!(TickerNamespace: Exchange, Composite, Bloomberg, Reuters, Vendor, OverTheCounter, Internal, Synthetic);
pub static TickerNamespace_VARIANTS: &[&str] = TickerNamespace::VARIANTS;

finance_enum!(PriceNotation: Decimal, PercentageOfPar, Yield, Spread, BasisPoints, Volatility, IndexPoints, Pips, PerUnit, Percentage, CleanPrice, DirtyPrice);
pub static PriceNotation_VARIANTS: &[&str] = PriceNotation::VARIANTS;

finance_enum!(PriceKind: Bid, Ask, Mid, Last, Settlement, Vwap);
pub static PriceKind_VARIANTS: &[&str] = PriceKind::VARIANTS;

finance_enum!(QuantityUnit: Shares, Contracts, Units, Lots, CurrencyAmount, NotionalAmount, FaceValue, Weight);
pub static QuantityUnit_VARIANTS: &[&str] = QuantityUnit::VARIANTS;

finance_enum!(CurrencyRole: Base, Quote, Settlement, Margin, ProfitAndLoss, Reporting);
pub static CurrencyRole_VARIANTS: &[&str] = CurrencyRole::VARIANTS;

finance_enum!(MICMarketCategory: NotSpecified, MultilateralTradingFacility, SystematicInternaliser, RegulatedMarket, AlternativeTradingSystem, OrganizedTradingFacility, Other, SwapExecutionFacility, RegulatedMarketOffBookSegment, ApprovedPublicationArrangement, CryptoAssetServiceProvider, DesignatedContractMarket, TradeReportingFacility, InterDealerQuotationSystem);
pub static MICMarketCategory_VARIANTS: &[&str] = MICMarketCategory::VARIANTS;

finance_enum!(VenueRegulatoryFlag: Multilateral, OrganizedTrading, TradeReporting, SwapExecution, Publication, SystematicInternaliser, RegulatedMarket, AlternativeTradingSystem, OffBookSegment, CryptoAssetServiceProvider, DesignatedContractMarket, InterDealerQuotation);
pub static VenueRegulatoryFlag_VARIANTS: &[&str] = VenueRegulatoryFlag::VARIANTS;

finance_enum!(ContractStyle: Standardized, NonStandardized);
pub static ContractStyle_VARIANTS: &[&str] = ContractStyle::VARIANTS;

finance_enum!(ContractUnit: Share, Unit, Contract, CurrencyAmount, NotionalAmount, IndexPoint);
pub static ContractUnit_VARIANTS: &[&str] = ContractUnit::VARIANTS;

finance_enum!(DeliveryType: Physical, Cash, NonDeliverable, ElectAtExercise, DeliveryVersusPayment, FreeOfPayment, HoldInCustody, TriParty);
pub static DeliveryType_VARIANTS: &[&str] = DeliveryType::VARIANTS;

finance_enum!(CouponType: Fixed, Floating, Zero, StepUp, InflationLinked, PaymentInKind);
pub static CouponType_VARIANTS: &[&str] = CouponType::VARIANTS;

finance_enum!(CouponFrequency: Monthly, Quarterly, SemiAnnual, Annual, ZeroCoupon, AtMaturity);
pub static CouponFrequency_VARIANTS: &[&str] = CouponFrequency::VARIANTS;

finance_enum!(DayCountConvention: Actual360, Actual365Fixed, ActualActual, Thirty360, ThirtyE360, Business252);
pub static DayCountConvention_VARIANTS: &[&str] = DayCountConvention::VARIANTS;

finance_enum!(AmortizationType: Bullet, Linear, MortgageStyle, NegativeAmortization, SinkingFund, Accreting);
pub static AmortizationType_VARIANTS: &[&str] = AmortizationType::VARIANTS;

finance_enum!(Seniority: SeniorSecured, SeniorUnsecured, SeniorSubordinated, Subordinated, JuniorSubordinated, Preferred);
pub static Seniority_VARIANTS: &[&str] = Seniority::VARIANTS;

finance_enum!(CollateralType: GeneralCollateral, SpecificCollateral, CashCollateral, GovernmentBonds, CorporateBonds, Equities);
pub static CollateralType_VARIANTS: &[&str] = CollateralType::VARIANTS;

finance_enum!(MarginType: Initial, Variation, IndependentAmount, Maintenance, CrossMargin, PortfolioMargin);
pub static MarginType_VARIANTS: &[&str] = MarginType::VARIANTS;

finance_enum!(BorrowType: StockLoan, SecuritiesLending, MarginLoan, RepoBorrow, UnsecuredBorrow);
pub static BorrowType_VARIANTS: &[&str] = BorrowType::VARIANTS;

finance_enum!(RepoType: Bilateral, TriParty, HoldInCustody, Open, Term, Evergreen);
pub static RepoType_VARIANTS: &[&str] = RepoType::VARIANTS;

finance_enum!(AccountType: Cash, Margin, PrimeBrokerage, Custody, Settlement, Omnibus);
pub static AccountType_VARIANTS: &[&str] = AccountType::VARIANTS;

finance_enum!(BookType: Trading, Hedging, Treasury, Financing, Inventory, Custody);
pub static BookType_VARIANTS: &[&str] = BookType::VARIANTS;

finance_enum!(PositionType: Long, Short, Flat, Net, Gross);
pub static PositionType_VARIANTS: &[&str] = PositionType::VARIANTS;

finance_enum!(InventoryType: Available, Reserved, Borrowed, Lent, Encumbered, PendingSettlement);
pub static InventoryType_VARIANTS: &[&str] = InventoryType::VARIANTS;

finance_enum!(StrategyType: MarketMaking, Arbitrage, Hedging, Directional, Execution, RelativeValue);
pub static StrategyType_VARIANTS: &[&str] = StrategyType::VARIANTS;

finance_enum!(NettingType: None, Bilateral, Multilateral, Portfolio, CrossProduct);
pub static NettingType_VARIANTS: &[&str] = NettingType::VARIANTS;

finance_enum!(VehicleWrapper: ExchangeTradedFund, MutualFund, UnitTrust, SocieteInvestissementCapitalVariable, OpenEndedInvestmentCompany, LimitedPartnership);
pub static VehicleWrapper_VARIANTS: &[&str] = VehicleWrapper::VARIANTS;

finance_enum!(DistributionPolicy: Accumulating, Distributing, Income, Growth, Mixed);
pub static DistributionPolicy_VARIANTS: &[&str] = DistributionPolicy::VARIANTS;

finance_enum!(ShareClassHedging: Unhedged, CurrencyHedged, DurationHedged, CommodityHedged, PartialHedged);
pub static ShareClassHedging_VARIANTS: &[&str] = ShareClassHedging::VARIANTS;

finance_enum!(LiquidityTerm: Daily, Weekly, Monthly, Quarterly, SemiAnnual, Annual);
pub static LiquidityTerm_VARIANTS: &[&str] = LiquidityTerm::VARIANTS;

finance_enum!(RedemptionFrequency: Daily, Weekly, Monthly, Quarterly, Annual, AtMaturity);
pub static RedemptionFrequency_VARIANTS: &[&str] = RedemptionFrequency::VARIANTS;

finance_enum!(FinancingType: LoanLease, RepurchaseAgreement, SecuritiesLending);
pub static FinancingType_VARIANTS: &[&str] = FinancingType::VARIANTS;

finance_enum!(FutureAssetClass: Financial, Commodity);
pub static FutureAssetClass_VARIANTS: &[&str] = FutureAssetClass::VARIANTS;

finance_enum!(SwapLegType: Fixed, Floating, Inflation, Credit, Equity, Commodity, ForeignExchange, Basis);
pub static SwapLegType_VARIANTS: &[&str] = SwapLegType::VARIANTS;

finance_enum!(RateIndex: SecuredOvernightFinancingRate, FedFunds, EuroShortTermRate, SterlingOvernightIndexAverage, EuroInterbankOfferedRate, TokyoOvernightAverageRate, SwissAverageRateOvernight, ConsumerPriceIndex);
pub static RateIndex_VARIANTS: &[&str] = RateIndex::VARIANTS;

finance_enum!(ResetFrequency: Daily, Weekly, Monthly, Quarterly, SemiAnnual, Annual);
pub static ResetFrequency_VARIANTS: &[&str] = ResetFrequency::VARIANTS;

finance_enum!(CompoundingMethod: Simple, Compounded, Averaged, Flat, Straight);
pub static CompoundingMethod_VARIANTS: &[&str] = CompoundingMethod::VARIANTS;

finance_enum!(StubType: None, ShortFront, ShortBack, LongFront, LongBack);
pub static StubType_VARIANTS: &[&str] = StubType::VARIANTS;

finance_enum!(BarrierType: UpAndIn, UpAndOut, DownAndIn, DownAndOut, DoubleKnockIn, DoubleKnockOut);
pub static BarrierType_VARIANTS: &[&str] = BarrierType::VARIANTS;

finance_enum!(AveragingMethod: Arithmetic, Geometric, Weighted, VolumeWeighted, SpotAverage);
pub static AveragingMethod_VARIANTS: &[&str] = AveragingMethod::VARIANTS;

finance_enum!(ExoticOptionFeature: Barrier, Digital, Asian, Lookback, Cliquet, Chooser, Compound, Quanto);
pub static ExoticOptionFeature_VARIANTS: &[&str] = ExoticOptionFeature::VARIANTS;

finance_enum!(CorporateActionType: CashDividend, StockDividend, StockSplit, ReverseSplit, RightsIssue, SpinOff, Merger, TenderOffer, Delisting);
pub static CorporateActionType_VARIANTS: &[&str] = CorporateActionType::VARIANTS;

finance_enum!(ListingStatus: Listed, Suspended, Delisted, PendingListing, PendingDelisting, Unlisted);
pub static ListingStatus_VARIANTS: &[&str] = ListingStatus::VARIANTS;

finance_enum!(SecurityStatus: Active, Inactive, Matured, Defaulted, Called, Converted, Expired);
pub static SecurityStatus_VARIANTS: &[&str] = SecurityStatus::VARIANTS;

finance_enum!(ExerciseEventType: Automatic, Voluntary, Assignment, Expiration, EarlyExercise);
pub static ExerciseEventType_VARIANTS: &[&str] = ExerciseEventType::VARIANTS;

finance_enum!(TenderOfferType: Cash, Stock, Mixed, DutchAuction, ExchangeOffer);
pub static TenderOfferType_VARIANTS: &[&str] = TenderOfferType::VARIANTS;

finance_enum!(DelistingReason: Merger, Acquisition, Bankruptcy, Regulatory, Voluntary, FailureToMeetRequirements);
pub static DelistingReason_VARIANTS: &[&str] = DelistingReason::VARIANTS;

finance_enum!(LegRole: Payer, Receiver, Buyer, Seller);
pub static LegRole_VARIANTS: &[&str] = LegRole::VARIANTS;

finance_enum!(PayoffStyle: Linear, Optional, Binary);
pub static PayoffStyle_VARIANTS: &[&str] = PayoffStyle::VARIANTS;

finance_enum!(SettlementType: Physical, Cash, NonDeliverable, ElectAtExercise, DeliveryVersusPayment, PaymentVersusPayment, FreeOfPayment);
pub static SettlementType_VARIANTS: &[&str] = SettlementType::VARIANTS;

finance_enum!(SettlementStatus: Pending, Instructed, Matched, Unmatched, Settled, PartiallySettled, Failed, Canceled);
pub static SettlementStatus_VARIANTS: &[&str] = SettlementStatus::VARIANTS;

finance_enum!(ClearingModel: Bilateral, CentralCounterparty, PrimeBroker, SponsoredAccess, AgentCleared);
pub static ClearingModel_VARIANTS: &[&str] = ClearingModel::VARIANTS;

finance_enum!(ClearingHouse: NationalSecuritiesClearingCorporation, FixedIncomeClearingCorporation, OptionsClearingCorporation, ChicagoMercantileExchange, IntercontinentalExchangeClear, LondonClearingHouse, EurexClearing, DepositoryTrustClearingCorporation, Euroclear, Clearstream, Other);
pub static ClearingHouse_VARIANTS: &[&str] = ClearingHouse::VARIANTS;

finance_enum!(FailsReason: InsufficientSecurities, InsufficientCash, CounterpartyMismatch, InstructionMismatch, RegulatoryHold, MarketDeadlineMissed, CorporateAction, SystemIssue, Other);
pub static FailsReason_VARIANTS: &[&str] = FailsReason::VARIANTS;

finance_enum!(AllocationMethod: AveragePrice, SpecificLot, ProRata, FirstInFirstOut, LastInFirstOut, Manual, Automated, StepOut);
pub static AllocationMethod_VARIANTS: &[&str] = AllocationMethod::VARIANTS;

finance_enum!(GiveUpType: None, GiveUp, GiveIn, AveragePriceGiveUp, ClearingGiveUp);
pub static GiveUpType_VARIANTS: &[&str] = GiveUpType::VARIANTS;

finance_enum!(BenchmarkType: InterestRate, EquityIndex, FixedIncomeIndex, CommodityIndex, ForeignExchangeFixing, InflationIndex, CreditIndex, Custom);
pub static BenchmarkType_VARIANTS: &[&str] = BenchmarkType::VARIANTS;

finance_enum!(IndexWeightingMethod: MarketCap, FloatAdjustedMarketCap, PriceWeighted, EqualWeighted, Fundamental, VolatilityWeighted, RiskParity, ModifiedMarketCap);
pub static IndexWeightingMethod_VARIANTS: &[&str] = IndexWeightingMethod::VARIANTS;

finance_enum!(RebalanceFrequency: Daily, Weekly, Monthly, Quarterly, SemiAnnual, Annual, AdHoc);
pub static RebalanceFrequency_VARIANTS: &[&str] = RebalanceFrequency::VARIANTS;

finance_enum!(CorporateActionAdjustmentType: None, PriceReturn, TotalReturn, NetTotalReturn, GrossTotalReturn, CapitalOnly, DivisorAdjustment);
pub static CorporateActionAdjustmentType_VARIANTS: &[&str] =
    CorporateActionAdjustmentType::VARIANTS;

finance_enum!(CalculationAgentType: Exchange, BenchmarkAdministrator, IndexProvider, CalculationAgent, Dealer, IndependentAgent, Internal);
pub static CalculationAgentType_VARIANTS: &[&str] = CalculationAgentType::VARIANTS;

finance_enum!(UnderlyingAssetClass: Agriculture, Basket, Commodity, Credit, Currency, Debt, Energy, Environmental, Equity, ExtractionResources, Future, GeneratedResources, Index, IndustrialProducts, InterestRate, Metals, MixedAssets, Option, Other, Paper, PolypropyleneProducts, Services, StockDividend, Swap);
pub static UnderlyingAssetClass_VARIANTS: &[&str] = UnderlyingAssetClass::VARIANTS;

finance_enum!(Industry: EnergyEquipmentAndServices, OilGasAndConsumableFuels, Chemicals, ConstructionMaterials, ContainersAndPackaging, MetalsAndMining, PaperAndForestProducts, AerospaceAndDefense, BuildingProducts, ConstructionAndEngineering, ElectricalEquipment, IndustrialConglomerates, Machinery, TradingCompaniesAndDistributors, CommercialServicesAndSupplies, ProfessionalServices, AirFreightAndLogistics, PassengerAirlines, MarineTransportation, GroundTransportation, TransportationInfrastructure, AutomobileComponents, Automobiles, HouseholdDurables, LeisureProducts, TextilesApparelAndLuxuryGoods, HotelsRestaurantsAndLeisure, DiversifiedConsumerServices, Distributors, BroadlineRetail, SpecialtyRetail, ConsumerStaplesDistributionAndRetail, Beverages, FoodProducts, Tobacco, HouseholdProducts, PersonalCareProducts, HealthCareEquipmentAndSupplies, HealthCareProvidersAndServices, HealthCareTechnology, Biotechnology, Pharmaceuticals, LifeSciencesToolsAndServices, Banks, FinancialServices, ConsumerFinance, CapitalMarkets, MortgageRealEstateInvestmentTrusts, Insurance, InformationTechnologyServices, Software, CommunicationsEquipment, TechnologyHardwareStorageAndPeripherals, ElectronicEquipmentInstrumentsAndComponents, SemiconductorsAndSemiconductorEquipment, DiversifiedTelecommunicationServices, WirelessTelecommunicationServices, Media, Entertainment, InteractiveMediaAndServices, ElectricUtilities, GasUtilities, MultiUtilities, WaterUtilities, IndependentPowerAndRenewableElectricityProducers, DiversifiedRealEstateInvestmentTrusts, IndustrialRealEstateInvestmentTrusts, HotelAndResortRealEstateInvestmentTrusts, OfficeRealEstateInvestmentTrusts, HealthCareRealEstateInvestmentTrusts, ResidentialRealEstateInvestmentTrusts, RetailRealEstateInvestmentTrusts, SpecializedRealEstateInvestmentTrusts, RealEstateManagementAndDevelopment);
pub static Industry_VARIANTS: &[&str] = Industry::VARIANTS;

finance_enum!(IndustryGroup: Energy, Materials, CapitalGoods, CommercialAndProfessionalServices, Transportation, AutomobilesAndComponents, ConsumerDurablesAndApparel, ConsumerServices, ConsumerDiscretionaryDistributionAndRetail, ConsumerStaplesDistributionAndRetail, FoodBeverageAndTobacco, HouseholdAndPersonalProducts, HealthCareEquipmentAndServices, PharmaceuticalsBiotechnologyAndLifeSciences, Banks, FinancialServices, Insurance, SoftwareAndServices, TechnologyHardwareAndEquipment, SemiconductorsAndSemiconductorEquipment, TelecommunicationServices, MediaAndEntertainment, Utilities, EquityRealEstateInvestmentTrusts, RealEstateManagementAndDevelopment);
pub static IndustryGroup_VARIANTS: &[&str] = IndustryGroup::VARIANTS;

finance_enum!(InstrumentType: Spot, Option, Forward, Future, Swap, Financing, Right, Warrant, Spread, Pair, Basket);
pub static InstrumentType_VARIANTS: &[&str] = InstrumentType::VARIANTS;

finance_enum!(MetalsType: Gold, Silver, Copper, Platinum, Palladium, Aluminum, Zinc, Nickel, Lead, Tin, Steel, Cobalt, Iron);
pub static MetalsType_VARIANTS: &[&str] = MetalsType::VARIANTS;

finance_enum!(MutualFundEndedness: OpenEnded, ClosedEnded);
pub static MutualFundEndedness_VARIANTS: &[&str] = MutualFundEndedness::VARIANTS;

finance_enum!(OptionExerciseType: American, European, Bermudan);
pub static OptionExerciseType_VARIANTS: &[&str] = OptionExerciseType::VARIANTS;

finance_enum!(OptionType: Call, Put);
pub static OptionType_VARIANTS: &[&str] = OptionType::VARIANTS;

finance_enum!(OrderStatus: New, PendingNew, PartiallyFilled, Filled, Canceled, Rejected, Expired, Suspended, PendingCancel);
pub static OrderStatus_VARIANTS: &[&str] = OrderStatus::VARIANTS;

finance_enum!(ExecutionType: New, Trade, Canceled, Replaced, Rejected, Expired, TradeCorrect, TradeCancel);
pub static ExecutionType_VARIANTS: &[&str] = ExecutionType::VARIANTS;

finance_enum!(ExecutionInstruction: AllOrNone, DoNotIncrease, DoNotReduce, ParticipateDoNotInitiate, StayOnOfferSide, StayOnBidSide, LastPeg, MidPricePeg);
pub static ExecutionInstruction_VARIANTS: &[&str] = ExecutionInstruction::VARIANTS;

finance_enum!(LiquidityFlag: Added, Removed, RoutedOut, Auction, None, Neutral);
pub static LiquidityFlag_VARIANTS: &[&str] = LiquidityFlag::VARIANTS;

finance_enum!(PositionEffect: Open, Close, CloseToday, CloseYesterday, Rolled);
pub static PositionEffect_VARIANTS: &[&str] = PositionEffect::VARIANTS;

finance_enum!(OrderCapacity: Agency, Principal, RisklessPrincipal, Proprietary, MarketMaker);
pub static OrderCapacity_VARIANTS: &[&str] = OrderCapacity::VARIANTS;

finance_enum!(ShortSaleRestriction: None, RegulationShoPriceTest, UptickRule, LocateRequired, BorrowRequired);
pub static ShortSaleRestriction_VARIANTS: &[&str] = ShortSaleRestriction::VARIANTS;

finance_enum!(OrderFlag: None, FillOrKill, AllOrNone, ImmediateOrCancel);
pub static OrderFlag_VARIANTS: &[&str] = OrderFlag::VARIANTS;

finance_enum!(OrderType: Limit, Market, Stop, StopLimit, MarketOnClose, LimitOnClose, Pegged);
pub static OrderType_VARIANTS: &[&str] = OrderType::VARIANTS;

finance_enum!(QuoteCondition: Regular, Indicative, Manual, FastTrading, SlowTrading, Closed);
pub static QuoteCondition_VARIANTS: &[&str] = QuoteCondition::VARIANTS;

finance_enum!(TradeCondition: Regular, Auction, AveragePrice, Block, DerivativelyPriced, PriorReferencePrice, OutOfSequence, Canceled);
pub static TradeCondition_VARIANTS: &[&str] = TradeCondition::VARIANTS;

finance_enum!(AggressorSide: Buy, Sell, Unknown);
pub static AggressorSide_VARIANTS: &[&str] = AggressorSide::VARIANTS;

finance_enum!(CrossType: Internal, Exchange, Broker, OpeningAuction, ClosingAuction);
pub static CrossType_VARIANTS: &[&str] = CrossType::VARIANTS;

finance_enum!(Sector: Energy, Materials, Industrials, ConsumerDiscretionary, ConsumerStaples, HealthCare, Financials, InformationTechnology, CommunicationServices, Utilities, RealEstate);
pub static Sector_VARIANTS: &[&str] = Sector::VARIANTS;

finance_enum!(SecurityType: Equity, Option, Bond, Forward, Future, PerpetualFuture, Swap, Financing, Spread, Fund, Commodity, Currency, Pair, Index, Warrant, Right);
pub static SecurityType_VARIANTS: &[&str] = SecurityType::VARIANTS;

finance_enum!(Side: None, Buy, Sell);
pub static Side_VARIANTS: &[&str] = Side::VARIANTS;

finance_enum!(SwapType: Rates, Commodities, Equity, Credit, ForeignExchange, Other);
pub static SwapType_VARIANTS: &[&str] = SwapType::VARIANTS;

finance_enum!(SubIndustry: OilAndGasDrilling, OilAndGasEquipmentAndServices, IntegratedOilAndGas, OilAndGasExplorationAndProduction, OilAndGasRefiningAndMarketing, OilAndGasStorageAndTransportation, CoalAndConsumableFuels, CommodityChemicals, DiversifiedChemicals, FertilizersAndAgriculturalChemicals, IndustrialGases, SpecialtyChemicals, ConstructionMaterials, MetalGlassAndPlasticContainers, PaperAndPlasticPackagingProductsAndMaterials, Aluminum, DiversifiedMetalsAndMining, Copper, Gold, PreciousMetalsAndMinerals, Silver, Steel, ForestProducts, PaperProducts, AerospaceAndDefense, BuildingProducts, ConstructionAndEngineering, ElectricalComponentsAndEquipment, HeavyElectricalEquipment, IndustrialConglomerates, ConstructionMachineryAndHeavyTransportationEquipment, AgriculturalAndFarmMachinery, IndustrialMachinerySuppliesAndComponents, TradingCompaniesAndDistributors, CommercialPrinting, EnvironmentalAndFacilitiesServices, OfficeServicesAndSupplies, DiversifiedSupportServices, SecurityAndAlarmServices, HumanResourcesAndEmploymentServices, ResearchAndConsultingServices, DataProcessingAndOutsourcedServices, AirFreightAndLogistics, PassengerAirlines, MarineTransportation, RailTransportation, CargoGroundTransportation, PassengerGroundTransportation, AirportServices, HighwaysAndRailtracks, MarinePortsAndServices, AutomotivePartsAndEquipment, TiresAndRubber, AutomobileManufacturers, MotorcycleManufacturers, ConsumerElectronics, HomeFurnishings, Homebuilding, HouseholdAppliances, HousewaresAndSpecialties, LeisureProducts, ApparelAccessoriesAndLuxuryGoods, Footwear, Textiles, CasinosAndGaming, HotelsResortsAndCruiseLines, LeisureFacilities, Restaurants, EducationServices, SpecializedConsumerServices, Distributors, BroadlineRetail, ApparelRetail, ComputerAndElectronicsretail, HomeImprovementRetail, OtherSpecialtyRetail, AutomotiveRetail, HomefurnishingRetail, DrugRetail, FoodDistributors, FoodRetail, ConsumerStaplesMerchandiseRetail, Brewers, DistillersAndVintners, SoftDrinksAndNonAlcoholicBeverages, AgriculturalProductsAndServices, PackagedFoodsAndMeats, Tobacco, HouseholdProducts, PersonalCareProducts, HealthCareEquipment, HealthCareSupplies, HealthCareDistributors, HealthCareServices, HealthCareFacilities, ManagedHealthCare, HealthCareTechnology, Biotechnology, Pharmaceuticals, LifeSciencesToolsAndServices, DiversifiedBanks, RegionalBanks, DiversifiedFinancialServices, MultiSectorHoldings, SpecializedFinance, CommercialAndResidentialMortgageFinance, TransactionAndPaymentProcessingServices, ConsumerFinance, AssetManagementAndCustodyBanks, InvestmentBankingAndBrokerage, DiversifiedCapitalMarkets, FinancialExchangesAndData, MortgageRealEstateInvestmentTrusts, InsuranceBrokers, LifeAndHealthInsurance, MultilineInsurance, PropertyAndCasualtyInsurance, Reinsurance, InformationTechnologyConsultingAndOtherServices, InternetServicesAndInfrastructure, ApplicationSoftware, SystemsSoftware, CommunicationsEquipment, TechnologyHardwareStorageAndPeripherals, ElectronicEquipmentAndInstruments, ElectronicComponents, ElectronicManufacturingServices, TechnologyDistributors, SemiconductorMaterialsAndEquipment, Semiconductors, AlternativeCarriers, IntegratedTelecommunicationServices, WirelessTelecommunicationServices, Advertising, Broadcasting, CableAndSatellite, Publishing, MoviesAndEntertainment, InteractiveHomeEntertainment, InteractiveMediaAndServices, ElectricUtilities, GasUtilities, MultiUtilities, WaterUtilities, IndependentPowerProducersAndEnergyTraders, RenewableElectricity, DiversifiedRealEstateInvestmentTrusts, IndustrialRealEstateInvestmentTrusts, HotelAndResortRealEstateInvestmentTrusts, OfficeRealEstateInvestmentTrusts, HealthCareRealEstateInvestmentTrusts, MultiFamilyResidentialRealEstateInvestmentTrusts, SingleFamilyResidentialRealEstateInvestmentTrusts, RetailRealEstateInvestmentTrusts, OtherSpecializedRealEstateInvestmentTrusts, SelfStorageRealEstateInvestmentTrusts, TelecomTowerRealEstateInvestmentTrusts, TimberRealEstateInvestmentTrusts, DataCenterRealEstateInvestmentTrusts, DiversifiedRealEstateActivities, RealEstateOperatingCompanies, RealEstateDevelopment, RealEstateServices);
pub static SubIndustry_VARIANTS: &[&str] = SubIndustry::VARIANTS;

finance_enum!(TimeInForce: None, Day, GoodTillCanceled, ImmediateOrCancel, FillOrKill, GoodTillDate, AtOpen, AtClose);
pub static TimeInForce_VARIANTS: &[&str] = TimeInForce::VARIANTS;

finance_enum!(ExecutionDisposition: Regular, Bust, Correct);
pub static ExecutionDisposition_VARIANTS: &[&str] = ExecutionDisposition::VARIANTS;

finance_enum!(FXSubType: Spot, Forward, NonDeliverable);
pub static FXSubType_VARIANTS: &[&str] = FXSubType::VARIANTS;

finance_enum!(FXTenor: TOD, TOM, SP, SNX, D2, D3, D4, W1, W2, W3, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M13, M14, M15, M16, M17, M18, M19, M20, M21, M22, M23, BMF1, BMF2, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y15, Y20, Y25, Y30, IM1, IM2, IM3, IM4);
pub static FXTenor_VARIANTS: &[&str] = FXTenor::VARIANTS;

finance_enum!(FactorGroup: Style, Industry, Country, Currency, Market);
pub static FactorGroup_VARIANTS: &[&str] = FactorGroup::VARIANTS;

finance_enum!(FamaFrench3Factor: Market, Size, Value);
pub static FamaFrench3Factor_VARIANTS: &[&str] = FamaFrench3Factor::VARIANTS;

finance_enum!(FamaFrench5Factor: Market, Size, Value, Profitability, Investment);
pub static FamaFrench5Factor_VARIANTS: &[&str] = FamaFrench5Factor::VARIANTS;

finance_enum!(FutureMonthCode: F, G, H, J, K, M, N, Q, U, V, X, Z);
pub static FutureMonthCode_VARIANTS: &[&str] = FutureMonthCode::VARIANTS;

finance_enum!(FutureSpreadLegType: BuyLeg, SellLeg, NearLeg, FarLeg);
pub static FutureSpreadLegType_VARIANTS: &[&str] = FutureSpreadLegType::VARIANTS;

finance_enum!(FutureSpreadSubType: Asset, Calendar);
pub static FutureSpreadSubType_VARIANTS: &[&str] = FutureSpreadSubType::VARIANTS;

finance_enum!(FutureUnderlyingType: Baskets, Equities, Debt, Currency, Indices, Options, Futures, Swaps, InterestRates, StockDividend, Extraction, Agriculture, Industrial, Services, Environmental, Polypropylene, Generated, Others);
pub static FutureUnderlyingType_VARIANTS: &[&str] = FutureUnderlyingType::VARIANTS;

finance_enum!(MsciFactorModel: Value, Momentum, Quality, Size, Volatility, Yield);
pub static MsciFactorModel_VARIANTS: &[&str] = MsciFactorModel::VARIANTS;

finance_enum!(OrderSide: Buy, Sell, SellShort, BuyToCover);
pub static OrderSide_VARIANTS: &[&str] = OrderSide::VARIANTS;

finance_enum!(Symbology: Ticker, RIC, PrimaryRIC, SecCode, MQAID, StableID, PointID, CUSIP, CUSIP9, SEDOL, SEDOL7, ISIN, PanoID, BloombergTicker, RollingFuture, BarraID, OSI, FIGI);
pub static Symbology_VARIANTS: &[&str] = Symbology::VARIANTS;

finance_enum!(TickDirection: Up, Down);
pub static TickDirection_VARIANTS: &[&str] = TickDirection::VARIANTS;

finance_enum!(TradingSessionStatus: NotOpen, PreOpen, Open, Closed, AfterHours, Halted, Suspended, OpeningAuction, IntradayAuction, ClosingAuction, CircuitBreakerAuction, QuotingOnly);
pub static TradingSessionStatus_VARIANTS: &[&str] = TradingSessionStatus::VARIANTS;

pub static CountryNames_ARRAY: &[&str] = &[
    "Uncategorized",
    "Andorra",
    "United Arab Emirates",
    "Afghanistan",
    "Antigua and Barbuda",
    "Anguilla",
    "Albania",
    "Armenia",
    "Angola",
    "Antarctica",
    "Argentina",
    "American Samoa",
    "Austria",
    "Australia",
    "Aruba",
    "Åland Islands",
    "Azerbaijan",
    "Bosnia and Herzegovina",
    "Barbados",
    "Bangladesh",
    "Belgium",
    "Burkina Faso",
    "Bulgaria",
    "Bahrain",
    "Burundi",
    "Benin",
    "Saint Barthélemy",
    "Bermuda",
    "Brunei Darussalam",
    "Bolivia",
    "Bonaire",
    "Brazil",
    "Bahamas",
    "Bhutan",
    "Bouvet Island",
    "Botswana",
    "Belarus",
    "Belize",
    "Canada",
    "Cocos (Keeling) Islands",
    "Democratic Republic of the Congo",
    "Central African Republic",
    "Congo",
    "Switzerland",
    "Côte d'Ivoire",
    "Cook Islands",
    "Chile",
    "Cameroon",
    "China",
    "Colombia",
    "Costa Rica",
    "Cuba",
    "Cabo Verde",
    "Curaçao",
    "Christmas Island",
    "Cyprus",
    "Czechia",
    "Germany",
    "Djibouti",
    "Denmark",
    "Dominica",
    "Dominican Republic",
    "Algeria",
    "Ecuador",
    "Estonia",
    "Egypt",
    "Western Sahara",
    "Eritrea",
    "Spain",
    "Ethiopia",
    "Finland",
    "Fiji",
    "Falkland Islands",
    "Micronesia",
    "Faroe Islands",
    "France",
    "Gabon",
    "United Kingdom of Great Britain and Northern Ireland",
    "Grenada",
    "Georgia",
    "French Guiana",
    "Guernsey",
    "Ghana",
    "Gibraltar",
    "Greenland",
    "Gambia",
    "Guinea",
    "Guadeloupe",
    "Equatorial Guinea",
    "Greece",
    "South Georgia and the South Sandwich Islands",
    "Guatemala",
    "Guam",
    "Guinea-Bissau",
    "Guyana",
    "Hong Kong",
    "Heard Island and McDonald Islands",
    "Honduras",
    "Croatia",
    "Haiti",
    "Hungary",
    "Indonesia",
    "Ireland",
    "Israel",
    "Isle of Man",
    "India",
    "British Indian Ocean Territory",
    "Iraq",
    "Iran",
    "Iceland",
    "Italy",
    "Jersey",
    "Jamaica",
    "Jordan",
    "Japan",
    "Kenya",
    "Kyrgyzstan",
    "Cambodia",
    "Kiribati",
    "Comoros",
    "Saint Kitts and Nevis",
    "North Korea",
    "South Korea",
    "Kuwait",
    "Cayman Islands",
    "Kazakhstan",
    "Laos",
    "Lebanon",
    "Saint Lucia",
    "Liechtenstein",
    "Sri Lanka",
    "Liberia",
    "Lesotho",
    "Lithuania",
    "Luxembourg",
    "Latvia",
    "Libya",
    "Morocco",
    "Monaco",
    "Moldova",
    "Montenegro",
    "Saint Martin",
    "Madagascar",
    "Marshall Islands",
    "North Macedonia",
    "Mali",
    "Myanmar",
    "Mongolia",
    "Macao",
    "Northern Mariana Islands",
    "Martinique",
    "Mauritania",
    "Montserrat",
    "Malta",
    "Mauritius",
    "Maldives",
    "Malawi",
    "Mexico",
    "Malaysia",
    "Mozambique",
    "Namibia",
    "New Caledonia",
    "Niger",
    "Norfolk Island",
    "Nigeria",
    "Nicaragua",
    "Netherlands",
    "Norway",
    "Nepal",
    "Nauru",
    "Niue",
    "New Zealand",
    "Oman",
    "Panama",
    "Peru",
    "French Polynesia",
    "Papua New Guinea",
    "Philippines",
    "Pakistan",
    "Poland",
    "Saint Pierre and Miquelon",
    "Pitcairn",
    "Puerto Rico",
    "Palestine",
    "Portugal",
    "Palau",
    "Paraguay",
    "Qatar",
    "Réunion",
    "Romania",
    "Serbia",
    "Russian Federation",
    "Rwanda",
    "Saudi Arabia",
    "Solomon Islands",
    "Seychelles",
    "Sudan",
    "Sweden",
    "Singapore",
    "Saint Helena, Ascension and Tristan da Cunha",
    "Slovenia",
    "Svalbard and Jan Mayen",
    "Slovakia",
    "Sierra Leone",
    "San Marino",
    "Senegal",
    "Somalia",
    "Suriname",
    "South Sudan",
    "Sao Tome and Principe",
    "El Salvador",
    "Sint Maarten",
    "Syrian Arab Republic",
    "Eswatini",
    "Turks and Caicos Islands",
    "Chad",
    "French Southern Territories",
    "Togo",
    "Thailand",
    "Tajikistan",
    "Tokelau",
    "Timor-Leste",
    "Turkmenistan",
    "Tunisia",
    "Tonga",
    "Türkiye",
    "Trinidad and Tobago",
    "Tuvalu",
    "Taiwan",
    "Tanzania",
    "Ukraine",
    "Uganda",
    "United States Minor Outlying Islands",
    "United States of America",
    "Uruguay",
    "Uzbekistan",
    "Vatican City",
    "Saint Vincent and the Grenadines",
    "Venezuela",
    "British Virgin Islands",
    "U.S. Virgin Islands",
    "Viet Nam",
    "Vanuatu",
    "Wallis and Futuna",
    "Samoa",
    "Yemen",
    "Mayotte",
    "South Africa",
    "Zambia",
    "Zimbabwe",
    "Kosovo",
];
