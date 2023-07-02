#pragma once
#include <vector>
#include <finance-enums/exports.hpp>

namespace finance_enums {

enum class LIB_EXPORT Sector {
  Invalid               = 0,
  Energy                = 1,
  Materials             = 2,
  Industrials           = 3,
  ConsumerDiscretionary = 4,
  ConsumerStaples       = 5,
  HealthCare            = 6,
  Financials            = 7,
  InformationTechnology = 8,
  CommunicationServices = 9,
  Utilities             = 10,
  RealEstate            = 11,
};

static const char* SectorNames[] = {
  "Invalid",               // 0,
  "Energy",                // 1,
  "Materials",             // 2,
  "Industrials",           // 3,
  "ConsumerDiscretionary", // 4,
  "ConsumerStaples",       // 5,
  "HealthCare",            // 6,
  "Financials",            // 7,
  "InformationTechnology", // 8,
  "CommunicationServices", // 9,
  "Utilities",             // 10,
  "RealEstate",            // 11,
};

enum class LIB_EXPORT IndustryGroup {
  Invalid = 0,
  // Energy
  Energy = 1,
  // Materials
  Materials = 2,
  // Industrials
  CapitalGoods                      = 3,
  CommercialAndProfessionalServices = 4,
  Transportation                    = 5,
  // Consumer Discretionary
  AutomobilesAndComponents                   = 6,
  ConsumerDurablesAndApparel                 = 7,
  ConsumerServices                           = 8,
  ConsumerDiscretionaryDistributionAndRetail = 9,
  // Consumer Staples
  ConsumerStaplesDistributionAndRetail = 10,
  FoodBeverageAndTobacco               = 11,
  HouseholdAndPersonalProducts         = 12,
  // Health Care
  HealthCareEquipmentAndServices              = 13,
  PharmaceuticalsBiotechnologyAndLifeSciences = 14,
  // Financials
  Banks             = 15,
  FinancialServices = 16,
  Insurance         = 17,
  // Information Technology
  SoftwareAndServices                     = 18,
  TechnologyHardwareAndEquipment          = 19,
  SemiconductorsAndSemiconductorEquipment = 20,
  // Communication Services
  TelecommunicationServices = 21,
  MediaAndEntertainment     = 22,
  // Utilities
  Utilities = 23,
  // Real Estate
  EquityRealEstateInvestmentTrusts   = 24,
  RealEstateManagementAndDevelopment = 25,
};

static const char* IndustryGroupNames[] = {
  "Invalid",                                     // 0,
  "Energy",                                      // 1,
  "Materials",                                   // 2,
  "CapitalGoods",                                // 3,
  "CommercialAndProfessionalServices",           // 4,
  "Transportation",                              // 5,
  "AutomobilesAndComponents",                    // 6,
  "ConsumerDurablesAndApparel",                  // 7,
  "ConsumerServices",                            // 8,
  "ConsumerDiscretionaryDistributionAndRetail",  // 9,
  "ConsumerStaplesDistributionAndRetail",        // 10,
  "FoodBeverageAndTobacco",                      // 11,
  "HouseholdAndPersonalProducts",                // 12,
  "HealthCareEquipmentAndServices",              // 13,
  "PharmaceuticalsBiotechnologyAndLifeSciences", // 14,
  "Banks",                                       // 15,
  "FinancialServices",                           // 16,
  "Insurance",                                   // 17,
  "SoftwareAndServices",                         // 18,
  "TechnologyHardwareAndEquipment",              // 19,
  "SemiconductorsAndSemiconductorEquipment",     // 20,
  "TelecommunicationServices",                   // 21,
  "MediaAndEntertainment",                       // 22,
  "Utilities",                                   // 23,
  "EquityRealEstateInvestmentTrusts",            // 24,
  "RealEstateManagementAndDevelopment",          // 25,
};

enum class LIB_EXPORT Industry {
  Invalid = 0,
  // Energy
  EnergyEquipmentAndServices = 1,
  OilGasAndConsumeableFules  = 2,
  // Materials,
  Chemicals              = 3,
  ConstructionMaterials  = 4,
  ContainersAndPackaging = 5,
  MetalsAndMining        = 6,
  PaperAndForestProducts = 7,
  // Industrials -> Capital Goods
  AerospaceAndDefense             = 8,
  BuildingProducts                = 9,
  ConstructionAndEngineering      = 10,
  ElectricalEquipment             = 11,
  IndustrialConglomerates         = 12,
  Machinery                       = 13,
  TradingCompaniesAndDistributors = 14,
  // Industrials -> Commercial and Professional Services
  CommercialServicesAndSupplies = 15,
  ProfessionalServices          = 16,
  // Industrials -> Transportation
  AirFreightAndLogistics       = 17,
  PassengerAirlines            = 18,
  MarineTransportation         = 19,
  GroundTransportation         = 20,
  TransportationInfrastructure = 21,
  // Consumer Discretionary -> Automobiles and Components
  AutomobileComponents = 22,
  Automobiles          = 23,
  // Consumer Discretionary -> Consumer Durables and Apparel
  HouseholdDurables             = 24,
  LeisureProducts               = 25,
  TextilesApparelAndLuxuryGoods = 26,
  // Consumer Discretionary -> Consumer Services
  HotelsRestaurantsAndLeisure = 27,
  DiversifiedConsumerServices = 28,
  // Consumer Discretionary -> Consumer Discretionary Distribution and Retail
  Distributors    = 29,
  BroadlineRetail = 30,
  SpecialtyRetail = 31,
  // Consumer Staples -> Consumer Staples Distribution And Retail
  ConsumerStaplesDistributionAndRetail = 32,
  // Consumer Staples -> Food, Beverage, and Tobacco
  Beverages    = 33,
  FoodProducts = 34,
  Tobacco      = 35,
  // Consumer Staples -> Household and Personal Products
  HouseholdProducts    = 36,
  PersonalCareProducts = 37,
  // Health Care -> Health Care Equipment and Services
  HealthCareEquipmentAndSupplies = 38,
  HealthCareProvidersAndServices = 39,
  HealthCareTechnology           = 40,
  // Health Care -> Pharmaceuticals, Biotechnology, and Life Sciences
  Biotechnology                = 41,
  Pharmaceuticals              = 42,
  LifeSciencesToolsAndServices = 43,
  // Financials -> Banks
  Banks = 44,
  // Financials -> Financial Services
  FinancialServices                  = 45,
  ConsumerFinance                    = 46,
  CapitalMarkets                     = 47,
  MortgageRealEstateInvestmentTrusts = 48,
  // Financials -> Insurance
  Insurance = 49,
  // Information Technology -> Software and Services
  ITServices = 50,
  Software   = 51,
  // Information Technology -> Technology Equipment and Hardware
  CommunicationsEquipment                     = 52,
  TechnologyHardwareStorageAndPeripherals     = 53,
  ElectronicEquipmentInstrumentsAndComponents = 54,
  // Information Technology -> Semiconductors and Semiconductor Equipment
  SemiconductorsAndSemiconductorEquipment = 55,
  // Communication Services -> Telecommunication Services
  DiversifiedTelecommunicationServices = 56,
  WirelessTelecommunicationServices    = 57,
  // Communication Services -> Media and Entertainment
  Media                       = 58,
  Entertainment               = 59,
  InteractiveMediaAndServices = 60,
  // Utilities
  ElectricUtilities                                = 61,
  GasUtilities                                     = 62,
  MultiUtilities                                   = 63,
  WaterUtilities                                   = 64,
  IndependentPowerAndRenewableElectricityProducers = 65,
  // Real Estate -> Equity REITs
  DiversifiedREITs    = 66,
  IndustrialREITs     = 67,
  HotelAndResortREITs = 68,
  OfficeREITs         = 69,
  HealthCareREITs     = 70,
  ResidentialREITs    = 71,
  RetailREITs         = 72,
  SpecializedREITs    = 73,
  // Real Estate -> Real Estate Management and Development
  RealEstateManagementAndDevelopment = 74,
};

static const char* IndustryNames[] = {
  "Invalid",                                          // 0
  "EnergyEquipmentAndServices",                       // 1
  "OilGasAndConsumeableFules",                        // 2
  "Chemicals",                                        // 3
  "ConstructionMaterials",                            // 4
  "ContainersAndPackaging",                           // 5
  "MetalsAndMining",                                  // 6
  "PaperAndForestProducts",                           // 7
  "AerospaceAndDefense",                              // 8
  "BuildingProducts",                                 // 9
  "ConstructionAndEngineering",                       // 10
  "ElectricalEquipment",                              // 11
  "IndustrialConglomerates",                          // 12
  "Machinery",                                        // 13
  "TradingCompaniesAndDistributors",                  // 14
  "CommercialServicesAndSupplies",                    // 15
  "ProfessionalServices",                             // 16
  "AirFreightAndLogistics",                           // 17
  "PassengerAirlines",                                // 18
  "MarineTransportation",                             // 19
  "GroundTransportation",                             // 20
  "TransportationInfrastructure",                     // 21
  "AutomobileComponents",                             // 22
  "Automobiles",                                      // 23
  "HouseholdDurables",                                // 24
  "LeisureProducts",                                  // 25
  "TextilesApparelAndLuxuryGoods",                    // 26
  "HotelsRestaurantsAndLeisure",                      // 27
  "DiversifiedConsumerServices",                      // 28
  "Distributors",                                     // 29
  "BroadlineRetail",                                  // 30
  "SpecialtyRetail",                                  // 31
  "ConsumerStaplesDistributionAndRetail",             // 32
  "Beverages",                                        // 33
  "FoodProducts",                                     // 34
  "Tobacco",                                          // 35
  "HouseholdProducts",                                // 36
  "PersonalCareProducts",                             // 37
  "HealthCareEquipmentAndSupplies",                   // 38
  "HealthCareProvidersAndServices",                   // 39
  "HealthCareTechnology",                             // 40
  "Biotechnology",                                    // 41
  "Pharmaceuticals",                                  // 42
  "LifeSciencesToolsAndServices",                     // 43
  "Banks",                                            // 44
  "FinancialServices",                                // 45
  "ConsumerFinance",                                  // 46
  "CapitalMarkets",                                   // 47
  "MortgageRealEstateInvestmentTrusts",               // 48
  "Insurance",                                        // 49
  "ITServices",                                       // 50
  "Software",                                         // 51
  "CommunicationsEquipment",                          // 52
  "TechnologyHardwareStorageAndPeripherals",          // 53
  "ElectronicEquipmentInstrumentsAndComponents",      // 54
  "SemiconductorsAndSemiconductorEquipment",          // 55
  "DiversifiedTelecommunicationServices",             // 56
  "WirelessTelecommunicationServices",                // 57
  "Media",                                            // 58
  "Entertainment",                                    // 59
  "InteractiveMediaAndServices",                      // 60
  "ElectricUtilities",                                // 61
  "GasUtilities",                                     // 62
  "MultiUtilities",                                   // 63
  "WaterUtilities",                                   // 64
  "IndependentPowerAndRenewableElectricityProducers", // 65
  "DiversifiedREITs",                                 // 66
  "IndustrialREITs",                                  // 67
  "HotelAndResortREITs",                              // 68
  "OfficeREITs",                                      // 69
  "HealthCareREITs",                                  // 70
  "ResidentialREITs",                                 // 71
  "RetailREITs",                                      // 72
  "SpecializedREITs",                                 // 73
  "RealEstateManagementAndDevelopment",               // 74
};

enum class LIB_EXPORT SubIndustry {
  Invalid = 0,
  // Energy -> Energy Equipment and Services
  OilAndGasDrilling             = 1,
  OilAndGasEquipmentAndServices = 2,
  // Energy -> Oil, Gas, and Consumeable Fuels
  IntegratedOilAndGas               = 3,
  OilAndGasExplorationAndProduction = 4,
  OilAndGasRefiningAndMarketing     = 5,
  OilAndGasStorageAndTransportation = 6,
  CoalAndConsumeableFuels           = 7,
  // Materials -> Chemicals
  CommodityChemicals                  = 8,
  DiversifiedChemicals                = 9,
  FertilizersAndAgriculturalChemicals = 10,
  IndustrialGases                     = 11,
  SpecialtyChemicals                  = 12,
  // Materials -> Construction Materials
  ConstructionMaterials = 13,
  // Materials -> Containers and Packaging
  MetalGlassAndPlasticContainers               = 14,
  PaperAndPlasticPackagingProductsAndMaterials = 15,
  // Materials -> Metals and Mining
  Aluminum                   = 16,
  DiversifiedMetalsAndMining = 17,
  Copper                     = 18,
  Gold                       = 19,
  PreciousMetalsAndMinerals  = 20,
  Silver                     = 21,
  Steel                      = 22,
  // Materials -> Paper and Forest Products
  ForestProducts = 23,
  PaperProducts  = 24,
  // Industrials -> Capital Goods -> AerospaceAndDefense
  AerospaceAndDefense = 25,
  // Industrials -> Capital Goods -> BuildingProducts
  BuildingProducts = 26,
  // Industrials -> Capital Goods -> ConstructionAndEngineering
  ConstructionAndEngineering = 27,
  // Industrials -> Capital Goods -> ElectricalEquipment
  ElectricalComponentsAndEquipment = 28,
  HeavyElectricalEquipment         = 29,
  // Industrials -> Capital Goods -> IndustrialConglomerates
  IndustrialConglomerates = 30,
  // Industrials -> Capital Goods -> Machinery
  ConstructionMachineryAndHeavyTransportationEquipment = 31,
  AgriculturalAndFarmMachinery                         = 32,
  IndustrialMachinerySuppliesAndComponents             = 33,
  // Industrials -> Capital Goods -> TradingCompaniesAndDistributors
  TradingCompaniesAndDistributors = 34,
  // Industrials -> Commercial and Professional Services -> CommercialServicesAndSupplies
  CommercialPrinting                 = 35,
  EnvironmentalAndFacilitiesServices = 36,
  OfficeServicesAndSupplies          = 37,
  DiviersifiedSupportServices        = 38,
  SecurityAndAlarmServices           = 39,
  // Industrials -> Commercial and Professional Services -> ProfessionalServices
  HumanResourcesAndEmploymentServices = 40,
  ResearchAndConsultingServices       = 41,
  DataProcessingAndOutsourcedServices = 42,
  // Industrials -> Transportation -> AirFreightAndLogistics
  AirFreightAndLogistics = 43,
  // Industrials -> Transportation -> PassengerAirlines
  PassengerAirlines = 44,
  // Industrials -> Transportation -> MarineTransportation
  MarineTransportation = 45,
  // Industrials -> Transportation -> GroundTransportation
  RailTransportation            = 46,
  CargoGroundTransportation     = 47,
  PassengerGroundTransportation = 48,
  // Industrials -> Transportation -> TransportationInfrastructure
  AirportServices        = 49,
  HighwaysAndRailtracks  = 50,
  MarinePortsAndServices = 51,
  // Consumer Discretionary -> Automobiles and Components -> AutomobileComponents
  AutomotivePartsAndEquipment = 52,
  TiresAndRubber              = 53,
  // Consumer Discretionary -> Automobiles and Components -> Automobiles
  AutomobileManufacturers = 54,
  MotorcycleManufacturers = 55,
  // Consumer Discretionary -> Consumer Durables and Apparel -> Household Durables
  ConsumerElectronics      = 56,
  HomeFurnishings          = 57,
  Homebuilding             = 58,
  HouseholdAppliances      = 59,
  HousewaresAndSpecialties = 60,
  // Consumer Discretionary -> Consumer Durables and Apparel -> Leisure Products
  LeisureProducts = 61,
  // Consumer Discretionary -> Consumer Durables and Apparel -> Textiles, Apprael, and Luxury Goods
  ApparelAccessoriesAndLuxuryGoods = 62,
  Footwear                         = 63,
  Textiles                         = 64,
  // Consumer Discretionary -> Consumer Services -> Hotels, Restaurants, and Leisure
  CasinosAndGaming            = 65,
  HotelsResortsAndCruiseLines = 66,
  LeisureFacilities           = 67,
  Restaurants                 = 68,
  // Consumer Discretionary -> Consumer Services -> Diversified Consumer Services
  EducationServices           = 69,
  SpecializedConsumerServices = 70,
  // Consumer Discretionary -> Consumer Discretionary Distribution and Retail -> Distributors
  Distributors = 71,
  // Consumer Discretionary -> Consumer Discretionary Distribution and Retail -> Broadline Retail
  BroadlineRetail = 72,
  // Consumer Discretionary -> Consumer Discretionary Distribution and Retail -> Specialty Retail
  ApparelRetail                = 73,
  ComputerAndElectronicsretail = 74,
  HomeImprovementRetail        = 75,
  OtherSpecialtyRetail         = 76,
  AutomotiveRetail             = 77,
  HomefurnishingRetail         = 78,
  // Consumer Staples -> Consumer Staples Distribution And Retail -> Consumer Staples, Distribution, and Retail
  DrugRetail                       = 79,
  FoodDistributors                 = 80,
  FoodRetail                       = 81,
  ConsumerStaplesMerchandiseRetail = 82,
  // Consumer Staples -> Food, Beverage, and Tobacco -> Beverages
  Brewers                            = 83,
  DistillersAndVintners              = 84,
  SoftDrinksAndNonAlcoholicBeverages = 85,
  // Consumer Staples -> Food, Beverage, and Tobacco -> Food Products
  AgriculturalProductsAndServices = 86,
  PackagedFoodsAndMeats           = 87,
  // Consumer Staples -> Food, Beverage, and Tobacco -> Tobacco
  Tobacco = 88,
  // Consumer Staples -> Household and Personal Products -> Household Products
  HouseholdProducts = 89,
  // Consumer Staples -> Household and Personal Products -> Personal Care Products
  PersonalCareProducts = 90,
  // Health Care -> Health Care Equipment and Services -> Health Care Equipment and Supplies
  HealthCareEquipment = 91,
  HealthCareSupplies  = 92,
  // Health Care -> Health Care Equipment and Services -> Health Care Providers and Services
  HealthCareDistributors = 93,
  HealthCareServices     = 94,
  HealthCareFacilities   = 95,
  ManagedHealthCare      = 96,
  // Health Care -> Health Care Equipment and Services -> Health Care Technology
  HealthCareTechnology = 97,
  // Health Care -> Pharmaceuticals, Biotechnology, and Life Sciences -> Biotechnology
  Biotechnology = 98,
  // Health Care -> Pharmaceuticals, Biotechnology, and Life Sciences -> Pharmaceuticals
  Pharmaceuticals = 99,
  // Health Care -> Pharmaceuticals, Biotechnology, and Life Sciences -> Life Sciences Tools and Services
  LifeSciencesToolsAndServices = 100,
  // Financials -> Banks -> Banks
  DiversifiedBanks = 101,
  RegionalBanks    = 102,
  // Financials -> Financial Services -> Financial Services
  DiversifiedFinancialServices            = 103,
  MultiSectorHoldings                     = 104,
  SpecializedFinance                      = 105,
  CommercialAndResidentialMortgageFinance = 106,
  TransactionAndPaymentProcessingServices = 107,
  // Financials -> Financial Services -> Consumer Finance
  ConsumerFinance = 108,
  // Financials -> Financial Services -> Capital Markets
  AssetManagementAndCustodyBanks = 109,
  InvestmentBankingAndBrokerage  = 110,
  DiversifiedCapitalMarkets      = 111,
  FinancialExchangesAndData      = 112,
  // Financials -> Financial Services -> Mortgage REITs,
  MortgageRealEstateInvestmentTrusts = 113,
  // Financials -> Insurance -> Insurance
  InsuranceBrokers             = 114,
  LifeAndHealthInsurance       = 115,
  MultilineInsurance           = 116,
  PropertyAndCasualtyInsurance = 117,
  Reinsurance                  = 118,
  // Information Technology -> Software and Services -> ITServices
  ITConsultingAndOtherServices      = 119,
  InternetServicesAndInfrastructure = 120,
  // Information Technology -> Software and Services -> Software
  ApplicationSoftware = 121,
  SystemsSoftware     = 122,
  // Information Technology -> Technology Equipment and Hardware -> CommunicationsEquipment
  CommunicationsEquipment = 123,
  // Information Technology -> Technology Equipment and Hardware -> TechnologyHardwareStorageAndPeripherals
  TechnologyHardwareStorageAndPeripherals = 124,
  // Information Technology -> Technology Equipment and Hardware -> ElectronicEquipmentInstrumentsAndComponents
  ElectronicEquipmentAndInstruments = 125,
  ElectronicComponents              = 126,
  ElectronicManufacturingServices   = 127,
  TechnologyDistributors            = 128,
  // Information Technology -> Semiconductors and Semiconductor Equipment -> SemiconductorsAndSemiconductorEquipmen
  SemiconductorMaterialsAndEquipment = 129,
  Semiconductors                     = 130,
  // Communication Services -> Telecommunication Services -> DiversifiedTelecommunicationServices
  AlternativeCarriers                 = 131,
  IntegratedTelecommunicationServices = 132,
  // Communication Services -> Telecommunication Services -> WirelessTelecommunicationServices
  WirelessTelecommunicationServices = 133,
  // Communication Services -> Media and Entertainment -> Media
  Advertising       = 134,
  Broadcasting      = 135,
  CableAndSatellite = 136,
  Publishing        = 137,
  // Communication Services -> Media and Entertainment -> Entertainment
  MoviesAndEntertainment       = 138,
  InteractiveHomeEntertainment = 139,
  // Communication Services -> Media and Entertainment -> InteractiveMediaAndServices
  InteractiveMediaAndServices = 140,
  // Utilities -> ElectricUtilities
  ElectricUtilities = 141,
  // Utilities -> GasUtilities
  GasUtilities = 142,
  // Utilities -> MultiUtilities
  MultiUtilities = 143,
  // Utilities -> WaterUtilities
  WaterUtilities = 144,
  // Utilities -> IndependentPowerAndRenewableElectricityProducers
  IndependentPowerProducersAndEnergyTraders = 145,
  RenewableElectricity                      = 146,
  // Real Estate -> Equity REITs -> DiversifiedREITs
  DiversifiedREITs = 147,
  // Real Estate -> Equity REITs -> IndustrialREITs
  IndustrialREITs = 148,
  // Real Estate -> Equity REITs -> HotelAndResortREITs
  HotelAndResortREITs = 149,
  // Real Estate -> Equity REITs -> OfficeREITs
  OfficeREITs = 150,
  // Real Estate -> Equity REITs -> HealthCareREITs
  HealthCareREITs = 151,
  // Real Estate -> Equity REITs -> ResidentialREITs
  MultiFamilyResidentialREITs  = 152,
  SingleFamilyResidentialREITs = 153,
  // Real Estate -> Equity REITs -> RetailREITs
  RetailREITs = 154,
  // Real Estate -> Equity REITs -> SpecializedREITs
  OtherSpecializedREITs = 155,
  SelfStorageREITs      = 156,
  TelecomTowerREITs     = 157,
  TimberREITs           = 158,
  DataCenterREITs       = 159,
  // Real Estate -> Real Estate Management and Development -> RealEstateManagementAndDevelopment
  DiversifiedRealEstateActivities = 160,
  RealEstateOperatingCompanies    = 161,
  RealEstateDevelopment           = 162,
  RealEstateServices              = 163,
};

static const char* SubIndustryNames[] = {
  "Invalid",                                              // 0,
  "OilAndGasDrilling",                                    // 1,
  "OilAndGasEquipmentAndServices",                        // 2,
  "IntegratedOilAndGas",                                  // 3,
  "OilAndGasExplorationAndProduction",                    // 4,
  "OilAndGasRefiningAndMarketing",                        // 5,
  "OilAndGasStorageAndTransportation",                    // 6,
  "CoalAndConsumeableFuels",                              // 7,
  "CommodityChemicals",                                   // 8,
  "DiversifiedChemicals",                                 // 9,
  "FertilizersAndAgriculturalChemicals",                  // 10,
  "IndustrialGases",                                      // 11,
  "SpecialtyChemicals",                                   // 12,
  "ConstructionMaterials",                                // 13,
  "MetalGlassAndPlasticContainers",                       // 14,
  "PaperAndPlasticPackagingProductsAndMaterials",         // 15,
  "Aluminum",                                             // 16,
  "DiversifiedMetalsAndMining",                           // 17,
  "Copper",                                               // 18,
  "Gold",                                                 // 19,
  "PreciousMetalsAndMinerals",                            // 20,
  "Silver",                                               // 21,
  "Steel",                                                // 22,
  "ForestProducts",                                       // 23,
  "PaperProducts",                                        // 24,
  "AerospaceAndDefense",                                  // 25,
  "BuildingProducts",                                     // 26,
  "ConstructionAndEngineering",                           // 27,
  "ElectricalComponentsAndEquipment",                     // 28,
  "HeavyElectricalEquipment",                             // 29,
  "IndustrialConglomerates",                              // 30,
  "ConstructionMachineryAndHeavyTransportationEquipment", // 31,
  "AgriculturalAndFarmMachinery",                         // 32,
  "IndustrialMachinerySuppliesAndComponents",             // 33,
  "TradingCompaniesAndDistributors",                      // 34,
  "CommercialPrinting",                                   // 35,
  "EnvironmentalAndFacilitiesServices",                   // 36,
  "OfficeServicesAndSupplies",                            // 37,
  "DiviersifiedSupportServices",                          // 38,
  "SecurityAndAlarmServices",                             // 39,
  "HumanResourcesAndEmploymentServices",                  // 40,
  "ResearchAndConsultingServices",                        // 41,
  "DataProcessingAndOutsourcedServices",                  // 42,
  "AirFreightAndLogistics",                               // 43,
  "PassengerAirlines",                                    // 44,
  "MarineTransportation",                                 // 45,
  "RailTransportation",                                   // 46,
  "CargoGroundTransportation",                            // 47,
  "PassengerGroundTransportation",                        // 48,
  "AirportServices",                                      // 49,
  "HighwaysAndRailtracks",                                // 50,
  "MarinePortsAndServices",                               // 51,
  "AutomotivePartsAndEquipment",                          // 52,
  "TiresAndRubber",                                       // 53,
  "AutomobileManufacturers",                              // 54,
  "MotorcycleManufacturers",                              // 55,
  "ConsumerElectronics",                                  // 56,
  "HomeFurnishings",                                      // 57,
  "Homebuilding",                                         // 58,
  "HouseholdAppliances",                                  // 59,
  "HousewaresAndSpecialties",                             // 60,
  "LeisureProducts",                                      // 61,
  "ApparelAccessoriesAndLuxuryGoods",                     // 62,
  "Footwear",                                             // 63,
  "Textiles",                                             // 64,
  "CasinosAndGaming",                                     // 65,
  "HotelsResortsAndCruiseLines",                          // 66,
  "LeisureFacilities",                                    // 67,
  "Restaurants",                                          // 68,
  "EducationServices",                                    // 69,
  "SpecializedConsumerServices",                          // 70,
  "Distributors",                                         // 71,
  "BroadlineRetail",                                      // 72,
  "ApparelRetail",                                        // 73,
  "ComputerAndElectronicsretail",                         // 74,
  "HomeImprovementRetail",                                // 75,
  "OtherSpecialtyRetail",                                 // 76,
  "AutomotiveRetail",                                     // 77,
  "HomefurnishingRetail",                                 // 78,
  "DrugRetail",                                           // 79,
  "FoodDistributors",                                     // 80,
  "FoodRetail",                                           // 81,
  "ConsumerStaplesMerchandiseRetail",                     // 82,
  "Brewers",                                              // 83,
  "DistillersAndVintners",                                // 84,
  "SoftDrinksAndNonAlcoholicBeverages",                   // 85,
  "AgriculturalProductsAndServices",                      // 86,
  "PackagedFoodsAndMeats",                                // 87,
  "Tobacco",                                              // 88,
  "HouseholdProducts",                                    // 89,
  "PersonalCareProducts",                                 // 90,
  "HealthCareEquipment",                                  // 91,
  "HealthCareSupplies",                                   // 92,
  "HealthCareDistributors",                               // 93,
  "HealthCareServices",                                   // 94,
  "HealthCareFacilities",                                 // 95,
  "ManagedHealthCare",                                    // 96,
  "HealthCareTechnology",                                 // 97,
  "Biotechnology",                                        // 98,
  "Pharmaceuticals",                                      // 99,
  "LifeSciencesToolsAndServices",                         // 100,
  "DiversifiedBanks",                                     // 101,
  "RegionalBanks",                                        // 102,
  "DiversifiedFinancialServices",                         // 103,
  "MultiSectorHoldings",                                  // 104,
  "SpecializedFinance",                                   // 105,
  "CommercialAndResidentialMortgageFinance",              // 106,
  "TransactionAndPaymentProcessingServices",              // 107,
  "ConsumerFinance",                                      // 108,
  "AssetManagementAndCustodyBanks",                       // 109,
  "InvestmentBankingAndBrokerage",                        // 110,
  "DiversifiedCapitalMarkets",                            // 111,
  "FinancialExchangesAndData",                            // 112,
  "MortgageRealEstateInvestmentTrusts",                   // 113,
  "InsuranceBrokers",                                     // 114,
  "LifeAndHealthInsurance",                               // 115,
  "MultilineInsurance",                                   // 116,
  "PropertyAndCasualtyInsurance",                         // 117,
  "Reinsurance",                                          // 118,
  "ITConsultingAndOtherServices",                         // 119,
  "InternetServicesAndInfrastructure",                    // 120,
  "ApplicationSoftware",                                  // 121,
  "SystemsSoftware",                                      // 122,
  "CommunicationsEquipment",                              // 123,
  "TechnologyHardwareStorageAndPeripherals",              // 124,
  "ElectronicEquipmentAndInstruments",                    // 125,
  "ElectronicComponents",                                 // 126,
  "ElectronicManufacturingServices",                      // 127,
  "TechnologyDistributors",                               // 128,
  "SemiconductorMaterialsAndEquipment",                   // 129,
  "Semiconductors",                                       // 130,
  "AlternativeCarriers",                                  // 131,
  "IntegratedTelecommunicationServices",                  // 132,
  "WirelessTelecommunicationServices",                    // 133,
  "Advertising",                                          // 134,
  "Broadcasting",                                         // 135,
  "CableAndSatellite",                                    // 136,
  "Publishing",                                           // 137,
  "MoviesAndEntertainment",                               // 138,
  "InteractiveHomeEntertainment",                         // 139,
  "InteractiveMediaAndServices",                          // 140,
  "ElectricUtilities",                                    // 141,
  "GasUtilities",                                         // 142,
  "MultiUtilities",                                       // 143,
  "WaterUtilities",                                       // 144,
  "IndependentPowerProducersAndEnergyTraders",            // 145,
  "RenewableElectricity",                                 // 146,
  "DiversifiedREITs",                                     // 147,
  "IndustrialREITs",                                      // 148,
  "HotelAndResortREITs",                                  // 149,
  "OfficeREITs",                                          // 150,
  "HealthCareREITs",                                      // 151,
  "MultiFamilyResidentialREITs",                          // 152,
  "SingleFamilyResidentialREITs",                         // 153,
  "RetailREITs",                                          // 154,
  "OtherSpecializedREITs",                                // 155,
  "SelfStorageREITs",                                     // 156,
  "TelecomTowerREITs",                                    // 157,
  "TimberREITs",                                          // 158,
  "DataCenterREITs",                                      // 159,
  "DiversifiedRealEstateActivities",                      // 160,
  "RealEstateOperatingCompanies",                         // 161,
  "RealEstateDevelopment",                                // 162,
  "RealEstateServices",                                   // 163,
};

const char* SectorToString(const Sector);
const char* IndustryGroupToString(const IndustryGroup);
const char* IndustryToString(const Industry);
const char* SubIndustryToString(const SubIndustry);

Sector SectorFromString(const char*);
IndustryGroup IndustryGroupFromString(const char*);
Industry IndustryFromString(const char*);
SubIndustry SubIndustryFromString(const char*);

// Mappings
const std::vector<IndustryGroup> SectorToIndustryGroups(const Sector);
const std::vector<Industry> IndustryGroupToIndustries(const IndustryGroup);
const std::vector<SubIndustry> IndustryToSubIndustries(const Industry);
Sector IndustryGroupToSector(const IndustryGroup);
IndustryGroup IndustryToIndustryGroup(const Industry);
Industry SubIndustryToIndustry(const SubIndustry);
}
