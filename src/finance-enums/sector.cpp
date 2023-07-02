#include <cstring>
#include <finance-enums/sector.hpp>

namespace finance_enums {

const char* SectorToString(const Sector t) { return SectorNames[static_cast<int>(t)]; }

const char* IndustryGroupToString(const IndustryGroup t) { return IndustryGroupNames[static_cast<int>(t)]; }

const char* IndustryToString(const Industry t) { return IndustryNames[static_cast<int>(t)]; }

const char* SubIndustryToString(const SubIndustry t) { return SubIndustryNames[static_cast<int>(t)]; }

Sector SectorFromString(const char* s) {
  if(strncmp(s, "Energy", 15) == 0)
    return Sector::Energy;
  if(strncmp(s, "Materials", 15) == 0)
    return Sector::Materials;
  if(strncmp(s, "Industrials", 15) == 0)
    return Sector::Industrials;
  if(strncmp(s, "ConsumerDiscretionary", 15) == 0)
    return Sector::ConsumerDiscretionary;
  if(strncmp(s, "ConsumerStaples", 15) == 0)
    return Sector::ConsumerStaples;
  if(strncmp(s, "HealthCare", 15) == 0)
    return Sector::HealthCare;
  if(strncmp(s, "Financials", 15) == 0)
    return Sector::Financials;
  if(strncmp(s, "InformationTechnology", 15) == 0)
    return Sector::InformationTechnology;
  if(strncmp(s, "CommunicationServices", 15) == 0)
    return Sector::CommunicationServices;
  if(strncmp(s, "Utilities", 15) == 0)
    return Sector::Utilities;
  if(strncmp(s, "RealEstate", 15) == 0)
    return Sector::RealEstate;
  return Sector::Invalid;
}

IndustryGroup IndustryGroupFromString(const char* s) {
  if(strncmp(s, "Energy", 20) == 0)
    return IndustryGroup::Energy;
  if(strncmp(s, "Materials", 20) == 0)
    return IndustryGroup::Materials;
  if(strncmp(s, "CapitalGoods", 20) == 0)
    return IndustryGroup::CapitalGoods;
  if(strncmp(s, "CommercialAndProfessionalServices", 20) == 0)
    return IndustryGroup::CommercialAndProfessionalServices;
  if(strncmp(s, "Transportation", 20) == 0)
    return IndustryGroup::Transportation;
  if(strncmp(s, "AutomobilesAndComponents", 20) == 0)
    return IndustryGroup::AutomobilesAndComponents;
  if(strncmp(s, "ConsumerDurablesAndApparel", 20) == 0)
    return IndustryGroup::ConsumerDurablesAndApparel;
  if(strncmp(s, "ConsumerServices", 20) == 0)
    return IndustryGroup::ConsumerServices;
  if(strncmp(s, "ConsumerDiscretionaryDistributionAndRetail", 20) == 0)
    return IndustryGroup::ConsumerDiscretionaryDistributionAndRetail;
  if(strncmp(s, "ConsumerStaplesDistributionAndRetail", 20) == 0)
    return IndustryGroup::ConsumerStaplesDistributionAndRetail;
  if(strncmp(s, "FoodBeverageAndTobacco", 20) == 0)
    return IndustryGroup::FoodBeverageAndTobacco;
  if(strncmp(s, "HouseholdAndPersonalProducts", 20) == 0)
    return IndustryGroup::HouseholdAndPersonalProducts;
  if(strncmp(s, "HealthCareEquipmentAndServices", 20) == 0)
    return IndustryGroup::HealthCareEquipmentAndServices;
  if(strncmp(s, "PharmaceuticalsBiotechnologyAndLifeSciences", 20) == 0)
    return IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences;
  if(strncmp(s, "Banks", 20) == 0)
    return IndustryGroup::Banks;
  if(strncmp(s, "FinancialServices", 20) == 0)
    return IndustryGroup::FinancialServices;
  if(strncmp(s, "Insurance", 20) == 0)
    return IndustryGroup::Insurance;
  if(strncmp(s, "SoftwareAndServices", 20) == 0)
    return IndustryGroup::SoftwareAndServices;
  if(strncmp(s, "TechnologyHardwareAndEquipment", 20) == 0)
    return IndustryGroup::TechnologyHardwareAndEquipment;
  if(strncmp(s, "SemiconductorsAndSemiconductorEquipment", 20) == 0)
    return IndustryGroup::SemiconductorsAndSemiconductorEquipment;
  if(strncmp(s, "TelecommunicationServices", 20) == 0)
    return IndustryGroup::TelecommunicationServices;
  if(strncmp(s, "MediaAndEntertainment", 20) == 0)
    return IndustryGroup::MediaAndEntertainment;
  if(strncmp(s, "Utilities", 20) == 0)
    return IndustryGroup::Utilities;
  if(strncmp(s, "EquityRealEstateInvestmentTrusts", 20) == 0)
    return IndustryGroup::EquityRealEstateInvestmentTrusts;
  if(strncmp(s, "RealEstateManagementAndDevelopment", 20) == 0)
    return IndustryGroup::RealEstateManagementAndDevelopment;
  return IndustryGroup::Invalid;
}

Industry IndustryFromString(const char* s) {
  if(strncmp(s, "EnergyEquipmentAndServices", 25) == 0)
    return Industry::EnergyEquipmentAndServices;
  if(strncmp(s, "OilGasAndConsumeableFules", 25) == 0)
    return Industry::OilGasAndConsumeableFules;
  if(strncmp(s, "Chemicals", 25) == 0)
    return Industry::Chemicals;
  if(strncmp(s, "ConstructionMaterials", 25) == 0)
    return Industry::ConstructionMaterials;
  if(strncmp(s, "ContainersAndPackaging", 25) == 0)
    return Industry::ContainersAndPackaging;
  if(strncmp(s, "MetalsAndMining", 25) == 0)
    return Industry::MetalsAndMining;
  if(strncmp(s, "PaperAndForestProducts", 25) == 0)
    return Industry::PaperAndForestProducts;
  if(strncmp(s, "AerospaceAndDefense", 25) == 0)
    return Industry::AerospaceAndDefense;
  if(strncmp(s, "BuildingProducts", 25) == 0)
    return Industry::BuildingProducts;
  if(strncmp(s, "ConstructionAndEngineering", 25) == 0)
    return Industry::ConstructionAndEngineering;
  if(strncmp(s, "ElectricalEquipment", 25) == 0)
    return Industry::ElectricalEquipment;
  if(strncmp(s, "IndustrialConglomerates", 25) == 0)
    return Industry::IndustrialConglomerates;
  if(strncmp(s, "Machinery", 25) == 0)
    return Industry::Machinery;
  if(strncmp(s, "TradingCompaniesAndDistributors", 25) == 0)
    return Industry::TradingCompaniesAndDistributors;
  if(strncmp(s, "CommercialServicesAndSupplies", 25) == 0)
    return Industry::CommercialServicesAndSupplies;
  if(strncmp(s, "ProfessionalServices", 25) == 0)
    return Industry::ProfessionalServices;
  if(strncmp(s, "AirFreightAndLogistics", 25) == 0)
    return Industry::AirFreightAndLogistics;
  if(strncmp(s, "PassengerAirlines", 25) == 0)
    return Industry::PassengerAirlines;
  if(strncmp(s, "MarineTransportation", 25) == 0)
    return Industry::MarineTransportation;
  if(strncmp(s, "GroundTransportation", 25) == 0)
    return Industry::GroundTransportation;
  if(strncmp(s, "TransportationInfrastructure", 25) == 0)
    return Industry::TransportationInfrastructure;
  if(strncmp(s, "AutomobileComponents", 25) == 0)
    return Industry::AutomobileComponents;
  if(strncmp(s, "Automobiles", 25) == 0)
    return Industry::Automobiles;
  if(strncmp(s, "HouseholdDurables", 25) == 0)
    return Industry::HouseholdDurables;
  if(strncmp(s, "LeisureProducts", 25) == 0)
    return Industry::LeisureProducts;
  if(strncmp(s, "TextilesApparelAndLuxuryGoods", 25) == 0)
    return Industry::TextilesApparelAndLuxuryGoods;
  if(strncmp(s, "HotelsRestaurantsAndLeisure", 25) == 0)
    return Industry::HotelsRestaurantsAndLeisure;
  if(strncmp(s, "DiversifiedConsumerServices", 25) == 0)
    return Industry::DiversifiedConsumerServices;
  if(strncmp(s, "Distributors", 25) == 0)
    return Industry::Distributors;
  if(strncmp(s, "BroadlineRetail", 25) == 0)
    return Industry::BroadlineRetail;
  if(strncmp(s, "SpecialtyRetail", 25) == 0)
    return Industry::SpecialtyRetail;
  if(strncmp(s, "ConsumerStaplesDistributionAndRetail", 25) == 0)
    return Industry::ConsumerStaplesDistributionAndRetail;
  if(strncmp(s, "Beverages", 25) == 0)
    return Industry::Beverages;
  if(strncmp(s, "FoodProducts", 25) == 0)
    return Industry::FoodProducts;
  if(strncmp(s, "Tobacco", 25) == 0)
    return Industry::Tobacco;
  if(strncmp(s, "HouseholdProducts", 25) == 0)
    return Industry::HouseholdProducts;
  if(strncmp(s, "PersonalCareProducts", 25) == 0)
    return Industry::PersonalCareProducts;
  if(strncmp(s, "HealthCareEquipmentAndSupplies", 25) == 0)
    return Industry::HealthCareEquipmentAndSupplies;
  if(strncmp(s, "HealthCareProvidersAndServices", 25) == 0)
    return Industry::HealthCareProvidersAndServices;
  if(strncmp(s, "HealthCareTechnology", 25) == 0)
    return Industry::HealthCareTechnology;
  if(strncmp(s, "Biotechnology", 25) == 0)
    return Industry::Biotechnology;
  if(strncmp(s, "Pharmaceuticals", 25) == 0)
    return Industry::Pharmaceuticals;
  if(strncmp(s, "LifeSciencesToolsAndServices", 25) == 0)
    return Industry::LifeSciencesToolsAndServices;
  if(strncmp(s, "Banks", 25) == 0)
    return Industry::Banks;
  if(strncmp(s, "FinancialServices", 25) == 0)
    return Industry::FinancialServices;
  if(strncmp(s, "ConsumerFinance", 25) == 0)
    return Industry::ConsumerFinance;
  if(strncmp(s, "CapitalMarkets", 25) == 0)
    return Industry::CapitalMarkets;
  if(strncmp(s, "MortgageRealEstateInvestmentTrusts", 25) == 0)
    return Industry::MortgageRealEstateInvestmentTrusts;
  if(strncmp(s, "Insurance", 25) == 0)
    return Industry::Insurance;
  if(strncmp(s, "ITServices", 25) == 0)
    return Industry::ITServices;
  if(strncmp(s, "Software", 25) == 0)
    return Industry::Software;
  if(strncmp(s, "CommunicationsEquipment", 25) == 0)
    return Industry::CommunicationsEquipment;
  if(strncmp(s, "TechnologyHardwareStorageAndPeripherals", 25) == 0)
    return Industry::TechnologyHardwareStorageAndPeripherals;
  if(strncmp(s, "ElectronicEquipmentInstrumentsAndComponents", 25) == 0)
    return Industry::ElectronicEquipmentInstrumentsAndComponents;
  if(strncmp(s, "SemiconductorsAndSemiconductorEquipment", 25) == 0)
    return Industry::SemiconductorsAndSemiconductorEquipment;
  if(strncmp(s, "DiversifiedTelecommunicationServices", 25) == 0)
    return Industry::DiversifiedTelecommunicationServices;
  if(strncmp(s, "WirelessTelecommunicationServices", 25) == 0)
    return Industry::WirelessTelecommunicationServices;
  if(strncmp(s, "Media", 25) == 0)
    return Industry::Media;
  if(strncmp(s, "Entertainment", 25) == 0)
    return Industry::Entertainment;
  if(strncmp(s, "InteractiveMediaAndServices", 25) == 0)
    return Industry::InteractiveMediaAndServices;
  if(strncmp(s, "ElectricUtilities", 25) == 0)
    return Industry::ElectricUtilities;
  if(strncmp(s, "GasUtilities", 25) == 0)
    return Industry::GasUtilities;
  if(strncmp(s, "MultiUtilities", 25) == 0)
    return Industry::MultiUtilities;
  if(strncmp(s, "WaterUtilities", 25) == 0)
    return Industry::WaterUtilities;
  if(strncmp(s, "IndependentPowerAndRenewableElectricityProducers", 25) == 0)
    return Industry::IndependentPowerAndRenewableElectricityProducers;
  if(strncmp(s, "DiversifiedREITs", 25) == 0)
    return Industry::DiversifiedREITs;
  if(strncmp(s, "IndustrialREITs", 25) == 0)
    return Industry::IndustrialREITs;
  if(strncmp(s, "HotelAndResortREITs", 25) == 0)
    return Industry::HotelAndResortREITs;
  if(strncmp(s, "OfficeREITs", 25) == 0)
    return Industry::OfficeREITs;
  if(strncmp(s, "HealthCareREITs", 25) == 0)
    return Industry::HealthCareREITs;
  if(strncmp(s, "ResidentialREITs", 25) == 0)
    return Industry::ResidentialREITs;
  if(strncmp(s, "RetailREITs", 25) == 0)
    return Industry::RetailREITs;
  if(strncmp(s, "SpecializedREITs", 25) == 0)
    return Industry::SpecializedREITs;
  if(strncmp(s, "RealEstateManagementAndDevelopment", 25) == 0)
    return Industry::RealEstateManagementAndDevelopment;
  return Industry::Invalid;
}

SubIndustry SubIndustryFromString(const char* s) {
  if(strncmp(s, "OilAndGasDrilling", 25) == 0)
    return SubIndustry::OilAndGasDrilling;
  if(strncmp(s, "OilAndGasEquipmentAndServices", 25) == 0)
    return SubIndustry::OilAndGasEquipmentAndServices;
  if(strncmp(s, "IntegratedOilAndGas", 25) == 0)
    return SubIndustry::IntegratedOilAndGas;
  if(strncmp(s, "OilAndGasExplorationAndProduction", 25) == 0)
    return SubIndustry::OilAndGasExplorationAndProduction;
  if(strncmp(s, "OilAndGasRefiningAndMarketing", 25) == 0)
    return SubIndustry::OilAndGasRefiningAndMarketing;
  if(strncmp(s, "OilAndGasStorageAndTransportation", 25) == 0)
    return SubIndustry::OilAndGasStorageAndTransportation;
  if(strncmp(s, "CoalAndConsumeableFuels", 25) == 0)
    return SubIndustry::CoalAndConsumeableFuels;
  if(strncmp(s, "CommodityChemicals", 25) == 0)
    return SubIndustry::CommodityChemicals;
  if(strncmp(s, "DiversifiedChemicals", 25) == 0)
    return SubIndustry::DiversifiedChemicals;
  if(strncmp(s, "FertilizersAndAgriculturalChemicals", 25) == 0)
    return SubIndustry::FertilizersAndAgriculturalChemicals;
  if(strncmp(s, "IndustrialGases", 25) == 0)
    return SubIndustry::IndustrialGases;
  if(strncmp(s, "SpecialtyChemicals", 25) == 0)
    return SubIndustry::SpecialtyChemicals;
  if(strncmp(s, "ConstructionMaterials", 25) == 0)
    return SubIndustry::ConstructionMaterials;
  if(strncmp(s, "MetalGlassAndPlasticContainers", 25) == 0)
    return SubIndustry::MetalGlassAndPlasticContainers;
  if(strncmp(s, "PaperAndPlasticPackagingProductsAndMaterials", 25) == 0)
    return SubIndustry::PaperAndPlasticPackagingProductsAndMaterials;
  if(strncmp(s, "Aluminum", 25) == 0)
    return SubIndustry::Aluminum;
  if(strncmp(s, "DiversifiedMetalsAndMining", 25) == 0)
    return SubIndustry::DiversifiedMetalsAndMining;
  if(strncmp(s, "Copper", 25) == 0)
    return SubIndustry::Copper;
  if(strncmp(s, "Gold", 25) == 0)
    return SubIndustry::Gold;
  if(strncmp(s, "PreciousMetalsAndMinerals", 25) == 0)
    return SubIndustry::PreciousMetalsAndMinerals;
  if(strncmp(s, "Silver", 25) == 0)
    return SubIndustry::Silver;
  if(strncmp(s, "Steel", 25) == 0)
    return SubIndustry::Steel;
  if(strncmp(s, "ForestProducts", 25) == 0)
    return SubIndustry::ForestProducts;
  if(strncmp(s, "PaperProducts", 25) == 0)
    return SubIndustry::PaperProducts;
  if(strncmp(s, "AerospaceAndDefense", 25) == 0)
    return SubIndustry::AerospaceAndDefense;
  if(strncmp(s, "BuildingProducts", 25) == 0)
    return SubIndustry::BuildingProducts;
  if(strncmp(s, "ConstructionAndEngineering", 25) == 0)
    return SubIndustry::ConstructionAndEngineering;
  if(strncmp(s, "ElectricalComponentsAndEquipment", 25) == 0)
    return SubIndustry::ElectricalComponentsAndEquipment;
  if(strncmp(s, "HeavyElectricalEquipment", 25) == 0)
    return SubIndustry::HeavyElectricalEquipment;
  if(strncmp(s, "IndustrialConglomerates", 25) == 0)
    return SubIndustry::IndustrialConglomerates;
  if(strncmp(s, "ConstructionMachineryAndHeavyTransportationEquipment", 25) == 0)
    return SubIndustry::ConstructionMachineryAndHeavyTransportationEquipment;
  if(strncmp(s, "AgriculturalAndFarmMachinery", 25) == 0)
    return SubIndustry::AgriculturalAndFarmMachinery;
  if(strncmp(s, "IndustrialMachinerySuppliesAndComponents", 25) == 0)
    return SubIndustry::IndustrialMachinerySuppliesAndComponents;
  if(strncmp(s, "TradingCompaniesAndDistributors", 25) == 0)
    return SubIndustry::TradingCompaniesAndDistributors;
  if(strncmp(s, "CommercialPrinting", 25) == 0)
    return SubIndustry::CommercialPrinting;
  if(strncmp(s, "EnvironmentalAndFacilitiesServices", 25) == 0)
    return SubIndustry::EnvironmentalAndFacilitiesServices;
  if(strncmp(s, "OfficeServicesAndSupplies", 25) == 0)
    return SubIndustry::OfficeServicesAndSupplies;
  if(strncmp(s, "DiviersifiedSupportServices", 25) == 0)
    return SubIndustry::DiviersifiedSupportServices;
  if(strncmp(s, "SecurityAndAlarmServices", 25) == 0)
    return SubIndustry::SecurityAndAlarmServices;
  if(strncmp(s, "HumanResourcesAndEmploymentServices", 25) == 0)
    return SubIndustry::HumanResourcesAndEmploymentServices;
  if(strncmp(s, "ResearchAndConsultingServices", 25) == 0)
    return SubIndustry::ResearchAndConsultingServices;
  if(strncmp(s, "DataProcessingAndOutsourcedServices", 25) == 0)
    return SubIndustry::DataProcessingAndOutsourcedServices;
  if(strncmp(s, "AirFreightAndLogistics", 25) == 0)
    return SubIndustry::AirFreightAndLogistics;
  if(strncmp(s, "PassengerAirlines", 25) == 0)
    return SubIndustry::PassengerAirlines;
  if(strncmp(s, "MarineTransportation", 25) == 0)
    return SubIndustry::MarineTransportation;
  if(strncmp(s, "RailTransportation", 25) == 0)
    return SubIndustry::RailTransportation;
  if(strncmp(s, "CargoGroundTransportation", 25) == 0)
    return SubIndustry::CargoGroundTransportation;
  if(strncmp(s, "PassengerGroundTransportation", 25) == 0)
    return SubIndustry::PassengerGroundTransportation;
  if(strncmp(s, "AirportServices", 25) == 0)
    return SubIndustry::AirportServices;
  if(strncmp(s, "HighwaysAndRailtracks", 25) == 0)
    return SubIndustry::HighwaysAndRailtracks;
  if(strncmp(s, "MarinePortsAndServices", 25) == 0)
    return SubIndustry::MarinePortsAndServices;
  if(strncmp(s, "AutomotivePartsAndEquipment", 25) == 0)
    return SubIndustry::AutomotivePartsAndEquipment;
  if(strncmp(s, "TiresAndRubber", 25) == 0)
    return SubIndustry::TiresAndRubber;
  if(strncmp(s, "AutomobileManufacturers", 25) == 0)
    return SubIndustry::AutomobileManufacturers;
  if(strncmp(s, "MotorcycleManufacturers", 25) == 0)
    return SubIndustry::MotorcycleManufacturers;
  if(strncmp(s, "ConsumerElectronics", 25) == 0)
    return SubIndustry::ConsumerElectronics;
  if(strncmp(s, "HomeFurnishings", 25) == 0)
    return SubIndustry::HomeFurnishings;
  if(strncmp(s, "Homebuilding", 25) == 0)
    return SubIndustry::Homebuilding;
  if(strncmp(s, "HouseholdAppliances", 25) == 0)
    return SubIndustry::HouseholdAppliances;
  if(strncmp(s, "HousewaresAndSpecialties", 25) == 0)
    return SubIndustry::HousewaresAndSpecialties;
  if(strncmp(s, "LeisureProducts", 25) == 0)
    return SubIndustry::LeisureProducts;
  if(strncmp(s, "ApparelAccessoriesAndLuxuryGoods", 25) == 0)
    return SubIndustry::ApparelAccessoriesAndLuxuryGoods;
  if(strncmp(s, "Footwear", 25) == 0)
    return SubIndustry::Footwear;
  if(strncmp(s, "Textiles", 25) == 0)
    return SubIndustry::Textiles;
  if(strncmp(s, "CasinosAndGaming", 25) == 0)
    return SubIndustry::CasinosAndGaming;
  if(strncmp(s, "HotelsResortsAndCruiseLines", 25) == 0)
    return SubIndustry::HotelsResortsAndCruiseLines;
  if(strncmp(s, "LeisureFacilities", 25) == 0)
    return SubIndustry::LeisureFacilities;
  if(strncmp(s, "Restaurants", 25) == 0)
    return SubIndustry::Restaurants;
  if(strncmp(s, "EducationServices", 25) == 0)
    return SubIndustry::EducationServices;
  if(strncmp(s, "SpecializedConsumerServices", 25) == 0)
    return SubIndustry::SpecializedConsumerServices;
  if(strncmp(s, "Distributors", 25) == 0)
    return SubIndustry::Distributors;
  if(strncmp(s, "BroadlineRetail", 25) == 0)
    return SubIndustry::BroadlineRetail;
  if(strncmp(s, "ApparelRetail", 25) == 0)
    return SubIndustry::ApparelRetail;
  if(strncmp(s, "ComputerAndElectronicsretail", 25) == 0)
    return SubIndustry::ComputerAndElectronicsretail;
  if(strncmp(s, "HomeImprovementRetail", 25) == 0)
    return SubIndustry::HomeImprovementRetail;
  if(strncmp(s, "OtherSpecialtyRetail", 25) == 0)
    return SubIndustry::OtherSpecialtyRetail;
  if(strncmp(s, "AutomotiveRetail", 25) == 0)
    return SubIndustry::AutomotiveRetail;
  if(strncmp(s, "HomefurnishingRetail", 25) == 0)
    return SubIndustry::HomefurnishingRetail;
  if(strncmp(s, "DrugRetail", 25) == 0)
    return SubIndustry::DrugRetail;
  if(strncmp(s, "FoodDistributors", 25) == 0)
    return SubIndustry::FoodDistributors;
  if(strncmp(s, "FoodRetail", 25) == 0)
    return SubIndustry::FoodRetail;
  if(strncmp(s, "ConsumerStaplesMerchandiseRetail", 25) == 0)
    return SubIndustry::ConsumerStaplesMerchandiseRetail;
  if(strncmp(s, "Brewers", 25) == 0)
    return SubIndustry::Brewers;
  if(strncmp(s, "DistillersAndVintners", 25) == 0)
    return SubIndustry::DistillersAndVintners;
  if(strncmp(s, "SoftDrinksAndNonAlcoholicBeverages", 25) == 0)
    return SubIndustry::SoftDrinksAndNonAlcoholicBeverages;
  if(strncmp(s, "AgriculturalProductsAndServices", 25) == 0)
    return SubIndustry::AgriculturalProductsAndServices;
  if(strncmp(s, "PackagedFoodsAndMeats", 25) == 0)
    return SubIndustry::PackagedFoodsAndMeats;
  if(strncmp(s, "Tobacco", 25) == 0)
    return SubIndustry::Tobacco;
  if(strncmp(s, "HouseholdProducts", 25) == 0)
    return SubIndustry::HouseholdProducts;
  if(strncmp(s, "PersonalCareProducts", 25) == 0)
    return SubIndustry::PersonalCareProducts;
  if(strncmp(s, "HealthCareEquipment", 25) == 0)
    return SubIndustry::HealthCareEquipment;
  if(strncmp(s, "HealthCareSupplies", 25) == 0)
    return SubIndustry::HealthCareSupplies;
  if(strncmp(s, "HealthCareDistributors", 25) == 0)
    return SubIndustry::HealthCareDistributors;
  if(strncmp(s, "HealthCareServices", 25) == 0)
    return SubIndustry::HealthCareServices;
  if(strncmp(s, "HealthCareFacilities", 25) == 0)
    return SubIndustry::HealthCareFacilities;
  if(strncmp(s, "ManagedHealthCare", 25) == 0)
    return SubIndustry::ManagedHealthCare;
  if(strncmp(s, "HealthCareTechnology", 25) == 0)
    return SubIndustry::HealthCareTechnology;
  if(strncmp(s, "Biotechnology", 25) == 0)
    return SubIndustry::Biotechnology;
  if(strncmp(s, "Pharmaceuticals", 25) == 0)
    return SubIndustry::Pharmaceuticals;
  if(strncmp(s, "LifeSciencesToolsAndServices", 25) == 0)
    return SubIndustry::LifeSciencesToolsAndServices;
  if(strncmp(s, "DiversifiedBanks", 25) == 0)
    return SubIndustry::DiversifiedBanks;
  if(strncmp(s, "RegionalBanks", 25) == 0)
    return SubIndustry::RegionalBanks;
  if(strncmp(s, "DiversifiedFinancialServices", 25) == 0)
    return SubIndustry::DiversifiedFinancialServices;
  if(strncmp(s, "MultiSectorHoldings", 25) == 0)
    return SubIndustry::MultiSectorHoldings;
  if(strncmp(s, "SpecializedFinance", 25) == 0)
    return SubIndustry::SpecializedFinance;
  if(strncmp(s, "CommercialAndResidentialMortgageFinance", 25) == 0)
    return SubIndustry::CommercialAndResidentialMortgageFinance;
  if(strncmp(s, "TransactionAndPaymentProcessingServices", 25) == 0)
    return SubIndustry::TransactionAndPaymentProcessingServices;
  if(strncmp(s, "ConsumerFinance", 25) == 0)
    return SubIndustry::ConsumerFinance;
  if(strncmp(s, "AssetManagementAndCustodyBanks", 25) == 0)
    return SubIndustry::AssetManagementAndCustodyBanks;
  if(strncmp(s, "InvestmentBankingAndBrokerage", 25) == 0)
    return SubIndustry::InvestmentBankingAndBrokerage;
  if(strncmp(s, "DiversifiedCapitalMarkets", 25) == 0)
    return SubIndustry::DiversifiedCapitalMarkets;
  if(strncmp(s, "FinancialExchangesAndData", 25) == 0)
    return SubIndustry::FinancialExchangesAndData;
  if(strncmp(s, "MortgageRealEstateInvestmentTrusts", 25) == 0)
    return SubIndustry::MortgageRealEstateInvestmentTrusts;
  if(strncmp(s, "InsuranceBrokers", 25) == 0)
    return SubIndustry::InsuranceBrokers;
  if(strncmp(s, "LifeAndHealthInsurance", 25) == 0)
    return SubIndustry::LifeAndHealthInsurance;
  if(strncmp(s, "MultilineInsurance", 25) == 0)
    return SubIndustry::MultilineInsurance;
  if(strncmp(s, "PropertyAndCasualtyInsurance", 25) == 0)
    return SubIndustry::PropertyAndCasualtyInsurance;
  if(strncmp(s, "Reinsurance", 25) == 0)
    return SubIndustry::Reinsurance;
  if(strncmp(s, "ITConsultingAndOtherServices", 25) == 0)
    return SubIndustry::ITConsultingAndOtherServices;
  if(strncmp(s, "InternetServicesAndInfrastructure", 25) == 0)
    return SubIndustry::InternetServicesAndInfrastructure;
  if(strncmp(s, "ApplicationSoftware", 25) == 0)
    return SubIndustry::ApplicationSoftware;
  if(strncmp(s, "SystemsSoftware", 25) == 0)
    return SubIndustry::SystemsSoftware;
  if(strncmp(s, "CommunicationsEquipment", 25) == 0)
    return SubIndustry::CommunicationsEquipment;
  if(strncmp(s, "TechnologyHardwareStorageAndPeripherals", 25) == 0)
    return SubIndustry::TechnologyHardwareStorageAndPeripherals;
  if(strncmp(s, "ElectronicEquipmentAndInstruments", 25) == 0)
    return SubIndustry::ElectronicEquipmentAndInstruments;
  if(strncmp(s, "ElectronicComponents", 25) == 0)
    return SubIndustry::ElectronicComponents;
  if(strncmp(s, "ElectronicManufacturingServices", 25) == 0)
    return SubIndustry::ElectronicManufacturingServices;
  if(strncmp(s, "TechnologyDistributors", 25) == 0)
    return SubIndustry::TechnologyDistributors;
  if(strncmp(s, "SemiconductorMaterialsAndEquipment", 25) == 0)
    return SubIndustry::SemiconductorMaterialsAndEquipment;
  if(strncmp(s, "Semiconductors", 25) == 0)
    return SubIndustry::Semiconductors;
  if(strncmp(s, "AlternativeCarriers", 25) == 0)
    return SubIndustry::AlternativeCarriers;
  if(strncmp(s, "IntegratedTelecommunicationServices", 25) == 0)
    return SubIndustry::IntegratedTelecommunicationServices;
  if(strncmp(s, "WirelessTelecommunicationServices", 25) == 0)
    return SubIndustry::WirelessTelecommunicationServices;
  if(strncmp(s, "Advertising", 25) == 0)
    return SubIndustry::Advertising;
  if(strncmp(s, "Broadcasting", 25) == 0)
    return SubIndustry::Broadcasting;
  if(strncmp(s, "CableAndSatellite", 25) == 0)
    return SubIndustry::CableAndSatellite;
  if(strncmp(s, "Publishing", 25) == 0)
    return SubIndustry::Publishing;
  if(strncmp(s, "MoviesAndEntertainment", 25) == 0)
    return SubIndustry::MoviesAndEntertainment;
  if(strncmp(s, "InteractiveHomeEntertainment", 25) == 0)
    return SubIndustry::InteractiveHomeEntertainment;
  if(strncmp(s, "InteractiveMediaAndServices", 25) == 0)
    return SubIndustry::InteractiveMediaAndServices;
  if(strncmp(s, "ElectricUtilities", 25) == 0)
    return SubIndustry::ElectricUtilities;
  if(strncmp(s, "GasUtilities", 25) == 0)
    return SubIndustry::GasUtilities;
  if(strncmp(s, "MultiUtilities", 25) == 0)
    return SubIndustry::MultiUtilities;
  if(strncmp(s, "WaterUtilities", 25) == 0)
    return SubIndustry::WaterUtilities;
  if(strncmp(s, "IndependentPowerProducersAndEnergyTraders", 25) == 0)
    return SubIndustry::IndependentPowerProducersAndEnergyTraders;
  if(strncmp(s, "RenewableElectricity", 25) == 0)
    return SubIndustry::RenewableElectricity;
  if(strncmp(s, "DiversifiedREITs", 25) == 0)
    return SubIndustry::DiversifiedREITs;
  if(strncmp(s, "IndustrialREITs", 25) == 0)
    return SubIndustry::IndustrialREITs;
  if(strncmp(s, "HotelAndResortREITs", 25) == 0)
    return SubIndustry::HotelAndResortREITs;
  if(strncmp(s, "OfficeREITs", 25) == 0)
    return SubIndustry::OfficeREITs;
  if(strncmp(s, "HealthCareREITs", 25) == 0)
    return SubIndustry::HealthCareREITs;
  if(strncmp(s, "MultiFamilyResidentialREITs", 25) == 0)
    return SubIndustry::MultiFamilyResidentialREITs;
  if(strncmp(s, "SingleFamilyResidentialREITs", 25) == 0)
    return SubIndustry::SingleFamilyResidentialREITs;
  if(strncmp(s, "RetailREITs", 25) == 0)
    return SubIndustry::RetailREITs;
  if(strncmp(s, "OtherSpecializedREITs", 25) == 0)
    return SubIndustry::OtherSpecializedREITs;
  if(strncmp(s, "SelfStorageREITs", 25) == 0)
    return SubIndustry::SelfStorageREITs;
  if(strncmp(s, "TelecomTowerREITs", 25) == 0)
    return SubIndustry::TelecomTowerREITs;
  if(strncmp(s, "TimberREITs", 25) == 0)
    return SubIndustry::TimberREITs;
  if(strncmp(s, "DataCenterREITs", 25) == 0)
    return SubIndustry::DataCenterREITs;
  if(strncmp(s, "DiversifiedRealEstateActivities", 25) == 0)
    return SubIndustry::DiversifiedRealEstateActivities;
  if(strncmp(s, "RealEstateOperatingCompanies", 25) == 0)
    return SubIndustry::RealEstateOperatingCompanies;
  if(strncmp(s, "RealEstateDevelopment", 25) == 0)
    return SubIndustry::RealEstateDevelopment;
  if(strncmp(s, "RealEstateServices", 25) == 0)
    return SubIndustry::RealEstateServices;
  return SubIndustry::Invalid;
}

static std::vector<IndustryGroup> _InvalidIndustryGroups     = {};
static std::vector<IndustryGroup> _EnergyIndustryGroups      = {IndustryGroup::Energy};
static std::vector<IndustryGroup> _MaterialsIndustryGroups   = {IndustryGroup::Materials};
static std::vector<IndustryGroup> _IndustrialsIndustryGroups = {
  IndustryGroup::CapitalGoods,
  IndustryGroup::CommercialAndProfessionalServices,
  IndustryGroup::Transportation,
};

static std::vector<IndustryGroup> _ConsumerDiscretionaryIndustryGroups = {
  IndustryGroup::AutomobilesAndComponents,
  IndustryGroup::ConsumerDurablesAndApparel,
  IndustryGroup::ConsumerServices,
  IndustryGroup::ConsumerDiscretionaryDistributionAndRetail,
};

static std::vector<IndustryGroup> _ConsumerStaplesIndustryGroups = {
  IndustryGroup::ConsumerStaplesDistributionAndRetail,
  IndustryGroup::FoodBeverageAndTobacco,
  IndustryGroup::HouseholdAndPersonalProducts,
};

static std::vector<IndustryGroup> _HealthCareIndustryGroups = {
  IndustryGroup::HealthCareEquipmentAndServices,
  IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences,
};

static std::vector<IndustryGroup> _FinancialsIndustryGroups = {
  IndustryGroup::Banks,
  IndustryGroup::FinancialServices,
  IndustryGroup::Insurance,
};
static std::vector<IndustryGroup> _InformationTechnologyIndustryGroups = {
  IndustryGroup::SoftwareAndServices,
  IndustryGroup::TechnologyHardwareAndEquipment,
  IndustryGroup::SemiconductorsAndSemiconductorEquipment,
};

static std::vector<IndustryGroup> _CommunicationServicesIndustryGroups = {
  IndustryGroup::TelecommunicationServices,
  IndustryGroup::MediaAndEntertainment,
};
static std::vector<IndustryGroup> _UtilitiesIndustryGroups  = {IndustryGroup::Utilities};
static std::vector<IndustryGroup> _RealEstateIndustryGroups = {
  IndustryGroup::EquityRealEstateInvestmentTrusts,
  IndustryGroup::RealEstateManagementAndDevelopment,
};

static std::vector<Industry> _InvalidIndustries = {};
static std::vector<Industry> _EnergyIndustries  = {
  Industry::EnergyEquipmentAndServices, Industry::OilGasAndConsumeableFules};
static std::vector<Industry> _MaterialsIndustries = {
  Industry::Chemicals,       Industry::ConstructionMaterials,  Industry::ContainersAndPackaging,
  Industry::MetalsAndMining, Industry::PaperAndForestProducts,
};
static std::vector<Industry> _CapitalGoodsIndustries = {
  Industry::AerospaceAndDefense,
  Industry::BuildingProducts,
  Industry::ConstructionAndEngineering,
  Industry::ElectricalEquipment,
  Industry::IndustrialConglomerates,
  Industry::Machinery,
  Industry::TradingCompaniesAndDistributors,
};
static std::vector<Industry> _CommercialAndProfessionalServicesIndustries = {
  Industry::CommercialServicesAndSupplies,
  Industry::ProfessionalServices,
};
static std::vector<Industry> _TransportationIndustries = {
  Industry::AirFreightAndLogistics,       Industry::PassengerAirlines,
  Industry::MarineTransportation,         Industry::GroundTransportation,
  Industry::TransportationInfrastructure,
};
static std::vector<Industry> _AutomobilesAndComponentsIndustries = {
  Industry::AutomobileComponents, Industry::Automobiles};
static std::vector<Industry> _ConsumerDurablesAndApparelIndustries = {
  Industry::HouseholdDurables,
  Industry::LeisureProducts,
  Industry::TextilesApparelAndLuxuryGoods,
};
static std::vector<Industry> _ConsumerServicesIndustries = {
  Industry::HotelsRestaurantsAndLeisure,
  Industry::DiversifiedConsumerServices,
};
static std::vector<Industry> _ConsumerDiscretionaryDistributionAndRetailIndustries = {
  Industry::Distributors,
  Industry::BroadlineRetail,
  Industry::SpecialtyRetail,
};
static std::vector<Industry> _ConsumerStaplesDistributionAndRetailIndustries = {
  Industry::ConsumerStaplesDistributionAndRetail};
static std::vector<Industry> _FoodBeverageAndTobaccoIndustries = {
  Industry::Beverages,
  Industry::FoodProducts,
  Industry::Tobacco,
};
static std::vector<Industry> _HouseholdAndPersonalProductsIndustries = {
  Industry::HouseholdProducts, Industry::PersonalCareProducts};
static std::vector<Industry> _HealthCareEquipmentAndServicesIndustries = {
  Industry::HealthCareEquipmentAndSupplies,
  Industry::HealthCareProvidersAndServices,
  Industry::HealthCareTechnology,
};
static std::vector<Industry> _PharmaceuticalsBiotechnologyAndLifeSciencesIndustries = {
  Industry::Biotechnology,
  Industry::Pharmaceuticals,
  Industry::LifeSciencesToolsAndServices,
};
static std::vector<Industry> _BanksIndustries             = {Industry::Banks};
static std::vector<Industry> _FinancialServicesIndustries = {
  Industry::FinancialServices,
  Industry::ConsumerFinance,
  Industry::CapitalMarkets,
  Industry::MortgageRealEstateInvestmentTrusts,
};
static std::vector<Industry> _InsuranceIndustries                      = {Industry::Insurance};
static std::vector<Industry> _SoftwareAndServicesIndustries            = {Industry::ITServices, Industry::Software};
static std::vector<Industry> _TechnologyHardwareAndEquipmentIndustries = {
  Industry::CommunicationsEquipment,
  Industry::TechnologyHardwareStorageAndPeripherals,
  Industry::ElectronicEquipmentInstrumentsAndComponents,
};
static std::vector<Industry> _SemiconductorsAndSemiconductorEquipmentIndustries = {
  Industry::SemiconductorsAndSemiconductorEquipment};
static std::vector<Industry> _TelecommunicationServicesIndustries = {
  Industry::DiversifiedTelecommunicationServices,
  Industry::WirelessTelecommunicationServices,
};
static std::vector<Industry> _MediaAndEntertainmentIndustries = {
  Industry::Media,
  Industry::Entertainment,
  Industry::InteractiveMediaAndServices,
};
static std::vector<Industry> _UtilitiesIndustries = {
  Industry::ElectricUtilities,
  Industry::GasUtilities,
  Industry::MultiUtilities,
  Industry::WaterUtilities,
  Industry::IndependentPowerAndRenewableElectricityProducers,
};
static std::vector<Industry> _EquityRealEstateInvestmentTrustsIndustries = {
  Industry::DiversifiedREITs, Industry::IndustrialREITs,  Industry::HotelAndResortREITs, Industry::OfficeREITs,
  Industry::HealthCareREITs,  Industry::ResidentialREITs, Industry::RetailREITs,         Industry::SpecializedREITs,
};
static std::vector<Industry> _RealEstateManagementAndDevelopmentIndustries = {
  Industry::RealEstateManagementAndDevelopment};

static std::vector<SubIndustry> _InvalidSubIndustries                    = {};
static std::vector<SubIndustry> _EnergyEquipmentAndServicesSubIndustries = {
  SubIndustry::OilAndGasDrilling, SubIndustry::OilAndGasEquipmentAndServices};
static std::vector<SubIndustry> _OilGasAndConsumeableFulesSubIndustries = {
  SubIndustry::IntegratedOilAndGas, SubIndustry::OilAndGasExplorationAndProduction,
  SubIndustry::OilAndGasRefiningAndMarketing, SubIndustry::OilAndGasStorageAndTransportation,
  SubIndustry::CoalAndConsumeableFuels};
static std::vector<SubIndustry> _ChemicalsSubIndustries = {
  SubIndustry::CommodityChemicals, SubIndustry::DiversifiedChemicals, SubIndustry::FertilizersAndAgriculturalChemicals,
  SubIndustry::IndustrialGases, SubIndustry::SpecialtyChemicals};
static std::vector<SubIndustry> _ConstructionMaterialsSubIndustries  = {SubIndustry::ConstructionMaterials};
static std::vector<SubIndustry> _ContainersAndPackagingSubIndustries = {
  SubIndustry::MetalGlassAndPlasticContainers, SubIndustry::PaperAndPlasticPackagingProductsAndMaterials};
static std::vector<SubIndustry> _MetalsAndMiningSubIndustries = {
  SubIndustry::Aluminum, SubIndustry::DiversifiedMetalsAndMining, SubIndustry::Copper,
  SubIndustry::Gold,     SubIndustry::PreciousMetalsAndMinerals,  SubIndustry::Silver,
  SubIndustry::Steel};
static std::vector<SubIndustry> _PaperAndForestProductsSubIndustries = {
  SubIndustry::ForestProducts, SubIndustry::PaperProducts};
static std::vector<SubIndustry> _AerospaceAndDefenseSubIndustries        = {SubIndustry::AerospaceAndDefense};
static std::vector<SubIndustry> _BuildingProductsSubIndustries           = {SubIndustry::BuildingProducts};
static std::vector<SubIndustry> _ConstructionAndEngineeringSubIndustries = {SubIndustry::ConstructionAndEngineering};
static std::vector<SubIndustry> _ElectricalEquipmentSubIndustries        = {
  SubIndustry::ElectricalComponentsAndEquipment, SubIndustry::HeavyElectricalEquipment};
static std::vector<SubIndustry> _IndustrialConglomeratesSubIndustries = {SubIndustry::IndustrialConglomerates};
static std::vector<SubIndustry> _MachinerySubIndustries               = {
  SubIndustry::ConstructionMachineryAndHeavyTransportationEquipment, SubIndustry::AgriculturalAndFarmMachinery,
  SubIndustry::IndustrialMachinerySuppliesAndComponents};
static std::vector<SubIndustry> _TradingCompaniesAndDistributorsSubIndustries = {
  SubIndustry::TradingCompaniesAndDistributors};
static std::vector<SubIndustry> _CommercialServicesAndSuppliesSubIndustries = {
  SubIndustry::CommercialPrinting, SubIndustry::EnvironmentalAndFacilitiesServices,
  SubIndustry::OfficeServicesAndSupplies, SubIndustry::DiviersifiedSupportServices,
  SubIndustry::SecurityAndAlarmServices};
static std::vector<SubIndustry> _ProfessionalServicesSubIndustries = {
  SubIndustry::HumanResourcesAndEmploymentServices, SubIndustry::ResearchAndConsultingServices,
  SubIndustry::DataProcessingAndOutsourcedServices};
static std::vector<SubIndustry> _AirFreightAndLogisticsSubIndustries = {SubIndustry::AirFreightAndLogistics};
static std::vector<SubIndustry> _PassengerAirlinesSubIndustries      = {SubIndustry::PassengerAirlines};
static std::vector<SubIndustry> _MarineTransportationSubIndustries   = {SubIndustry::MarineTransportation};
static std::vector<SubIndustry> _GroundTransportationSubIndustries   = {
  SubIndustry::RailTransportation, SubIndustry::CargoGroundTransportation, SubIndustry::PassengerGroundTransportation};
static std::vector<SubIndustry> _TransportationInfrastructureSubIndustries = {
  SubIndustry::AirportServices, SubIndustry::HighwaysAndRailtracks, SubIndustry::MarinePortsAndServices};
static std::vector<SubIndustry> _AutomobileComponentsSubIndustries = {
  SubIndustry::AutomotivePartsAndEquipment, SubIndustry::TiresAndRubber};
static std::vector<SubIndustry> _AutomobilesSubIndustries = {
  SubIndustry::AutomobileManufacturers, SubIndustry::MotorcycleManufacturers};
static std::vector<SubIndustry> _HouseholdDurablesSubIndustries = {
  SubIndustry::ConsumerElectronics, SubIndustry::HomeFurnishings, SubIndustry::Homebuilding,
  SubIndustry::HouseholdAppliances, SubIndustry::HousewaresAndSpecialties};
static std::vector<SubIndustry> _LeisureProductsSubIndustries               = {SubIndustry::LeisureProducts};
static std::vector<SubIndustry> _TextilesApparelAndLuxuryGoodsSubIndustries = {
  SubIndustry::ApparelAccessoriesAndLuxuryGoods, SubIndustry::Footwear, SubIndustry::Textiles};
static std::vector<SubIndustry> _HotelsRestaurantsAndLeisureSubIndustries = {
  SubIndustry::CasinosAndGaming, SubIndustry::HotelsResortsAndCruiseLines, SubIndustry::LeisureFacilities,
  SubIndustry::Restaurants};
static std::vector<SubIndustry> _DiversifiedConsumerServicesSubIndustries = {
  SubIndustry::EducationServices, SubIndustry::SpecializedConsumerServices};
static std::vector<SubIndustry> _DistributorsSubIndustries    = {SubIndustry::Distributors};
static std::vector<SubIndustry> _BroadlineRetailSubIndustries = {SubIndustry::BroadlineRetail};
static std::vector<SubIndustry> _SpecialtyRetailSubIndustries = {
  SubIndustry::ApparelRetail,         SubIndustry::ComputerAndElectronicsretail,
  SubIndustry::HomeImprovementRetail, SubIndustry::OtherSpecialtyRetail,
  SubIndustry::AutomotiveRetail,      SubIndustry::HomefurnishingRetail};
static std::vector<SubIndustry> _ConsumerStaplesDistributionAndRetailSubIndustries = {
  SubIndustry::DrugRetail, SubIndustry::FoodDistributors, SubIndustry::FoodRetail,
  SubIndustry::ConsumerStaplesMerchandiseRetail};
static std::vector<SubIndustry> _BeveragesSubIndustries = {
  SubIndustry::Brewers, SubIndustry::DistillersAndVintners, SubIndustry::SoftDrinksAndNonAlcoholicBeverages};
static std::vector<SubIndustry> _FoodProductsSubIndustries = {
  SubIndustry::AgriculturalProductsAndServices, SubIndustry::PackagedFoodsAndMeats};
static std::vector<SubIndustry> _TobaccoSubIndustries                        = {SubIndustry::Tobacco};
static std::vector<SubIndustry> _HouseholdProductsSubIndustries              = {SubIndustry::HouseholdProducts};
static std::vector<SubIndustry> _PersonalCareProductsSubIndustries           = {SubIndustry::PersonalCareProducts};
static std::vector<SubIndustry> _HealthCareEquipmentAndSuppliesSubIndustries = {
  SubIndustry::HealthCareEquipment, SubIndustry::HealthCareSupplies};
static std::vector<SubIndustry> _HealthCareProvidersAndServicesSubIndustries = {
  SubIndustry::HealthCareDistributors, SubIndustry::HealthCareServices, SubIndustry::HealthCareFacilities,
  SubIndustry::ManagedHealthCare};
static std::vector<SubIndustry> _HealthCareTechnologySubIndustries         = {SubIndustry::HealthCareTechnology};
static std::vector<SubIndustry> _BiotechnologySubIndustries                = {SubIndustry::Biotechnology};
static std::vector<SubIndustry> _PharmaceuticalsSubIndustries              = {SubIndustry::Pharmaceuticals};
static std::vector<SubIndustry> _LifeSciencesToolsAndServicesSubIndustries = {
  SubIndustry::LifeSciencesToolsAndServices};
static std::vector<SubIndustry> _BanksSubIndustries = {SubIndustry::DiversifiedBanks, SubIndustry::RegionalBanks};
static std::vector<SubIndustry> _FinancialServicesSubIndustries = {
  SubIndustry::DiversifiedFinancialServices, SubIndustry::MultiSectorHoldings, SubIndustry::SpecializedFinance,
  SubIndustry::CommercialAndResidentialMortgageFinance, SubIndustry::TransactionAndPaymentProcessingServices};
static std::vector<SubIndustry> _ConsumerFinanceSubIndustries = {SubIndustry::ConsumerFinance};
static std::vector<SubIndustry> _CapitalMarketsSubIndustries  = {
  SubIndustry::AssetManagementAndCustodyBanks, SubIndustry::InvestmentBankingAndBrokerage,
  SubIndustry::DiversifiedCapitalMarkets, SubIndustry::FinancialExchangesAndData};
static std::vector<SubIndustry> _MortgageRealEstateInvestmentTrustsSubIndustries = {
  SubIndustry::MortgageRealEstateInvestmentTrusts};
static std::vector<SubIndustry> _InsuranceSubIndustries = {
  SubIndustry::InsuranceBrokers, SubIndustry::LifeAndHealthInsurance, SubIndustry::MultilineInsurance,
  SubIndustry::PropertyAndCasualtyInsurance, SubIndustry::Reinsurance};
static std::vector<SubIndustry> _ITServicesSubIndustries = {
  SubIndustry::ITConsultingAndOtherServices, SubIndustry::InternetServicesAndInfrastructure};
static std::vector<SubIndustry> _SoftwareSubIndustries = {
  SubIndustry::ApplicationSoftware, SubIndustry::SystemsSoftware};
static std::vector<SubIndustry> _CommunicationsEquipmentSubIndustries = {SubIndustry::CommunicationsEquipment};
static std::vector<SubIndustry> _TechnologyHardwareStorageAndPeripheralsSubIndustries = {
  SubIndustry::TechnologyHardwareStorageAndPeripherals};
static std::vector<SubIndustry> _ElectronicEquipmentInstrumentsAndComponentsSubIndustries = {
  SubIndustry::ElectronicEquipmentAndInstruments,
  SubIndustry::ElectronicComponents,
  SubIndustry::ElectronicManufacturingServices,
  SubIndustry::TechnologyDistributors,
};
static std::vector<SubIndustry> _SemiconductorsAndSemiconductorEquipmentSubIndustries = {
  SubIndustry::SemiconductorMaterialsAndEquipment, SubIndustry::Semiconductors};
static std::vector<SubIndustry> _DiversifiedTelecommunicationServicesSubIndustries = {
  SubIndustry::AlternativeCarriers, SubIndustry::IntegratedTelecommunicationServices};
static std::vector<SubIndustry> _WirelessTelecommunicationServicesSubIndustries = {
  SubIndustry::WirelessTelecommunicationServices};
static std::vector<SubIndustry> _MediaSubIndustries = {
  SubIndustry::Advertising, SubIndustry::Broadcasting, SubIndustry::CableAndSatellite, SubIndustry::Publishing};
static std::vector<SubIndustry> _EntertainmentSubIndustries = {
  SubIndustry::MoviesAndEntertainment, SubIndustry::InteractiveHomeEntertainment};
static std::vector<SubIndustry> _InteractiveMediaAndServicesSubIndustries = {SubIndustry::InteractiveMediaAndServices};
static std::vector<SubIndustry> _ElectricUtilitiesSubIndustries           = {SubIndustry::ElectricUtilities};
static std::vector<SubIndustry> _GasUtilitiesSubIndustries                = {SubIndustry::GasUtilities};
static std::vector<SubIndustry> _MultiUtilitiesSubIndustries              = {SubIndustry::MultiUtilities};
static std::vector<SubIndustry> _WaterUtilitiesSubIndustries              = {SubIndustry::WaterUtilities};
static std::vector<SubIndustry> _IndependentPowerAndRenewableElectricityProducersSubIndustries = {
  SubIndustry::IndependentPowerProducersAndEnergyTraders,
  SubIndustry::RenewableElectricity,
};
static std::vector<SubIndustry> _DiversifiedREITsSubIndustries    = {SubIndustry::DiversifiedREITs};
static std::vector<SubIndustry> _IndustrialREITsSubIndustries     = {SubIndustry::IndustrialREITs};
static std::vector<SubIndustry> _HotelAndResortREITsSubIndustries = {SubIndustry::HotelAndResortREITs};
static std::vector<SubIndustry> _OfficeREITsSubIndustries         = {SubIndustry::OfficeREITs};
static std::vector<SubIndustry> _HealthCareREITsSubIndustries     = {SubIndustry::HealthCareREITs};
static std::vector<SubIndustry> _ResidentialREITsSubIndustries    = {
  SubIndustry::MultiFamilyResidentialREITs,
  SubIndustry::SingleFamilyResidentialREITs,
};
static std::vector<SubIndustry> _RetailREITsSubIndustries      = {SubIndustry::RetailREITs};
static std::vector<SubIndustry> _SpecializedREITsSubIndustries = {
  SubIndustry::OtherSpecializedREITs, SubIndustry::SelfStorageREITs, SubIndustry::TelecomTowerREITs,
  SubIndustry::TimberREITs,           SubIndustry::DataCenterREITs,
};
static std::vector<SubIndustry> _RealEstateManagementAndDevelopmentSubIndustries = {
  SubIndustry::DiversifiedRealEstateActivities,
  SubIndustry::RealEstateOperatingCompanies,
  SubIndustry::RealEstateDevelopment,
  SubIndustry::RealEstateServices,
};

const std::vector<IndustryGroup> SectorToIndustryGroups(const Sector s) {
  switch(s) {
    case Sector::Energy:
      return _EnergyIndustryGroups;
    case Sector::Materials:
      return _MaterialsIndustryGroups;
    case Sector::Industrials:
      return _IndustrialsIndustryGroups;
    case Sector::ConsumerDiscretionary:
      return _ConsumerDiscretionaryIndustryGroups;
    case Sector::ConsumerStaples:
      return _ConsumerStaplesIndustryGroups;
    case Sector::HealthCare:
      return _HealthCareIndustryGroups;
    case Sector::Financials:
      return _FinancialsIndustryGroups;
    case Sector::InformationTechnology:
      return _InformationTechnologyIndustryGroups;
    case Sector::CommunicationServices:
      return _CommunicationServicesIndustryGroups;
    case Sector::Utilities:
      return _UtilitiesIndustryGroups;
    case Sector::RealEstate:
      return _RealEstateIndustryGroups;
    default:
      return _InvalidIndustryGroups;
  }
}

const std::vector<Industry> IndustryGroupToIndustries(const IndustryGroup ig) {
  switch(ig) {
    case IndustryGroup::Energy:
      return _EnergyIndustries;
    case IndustryGroup::Materials:
      return _MaterialsIndustries;
    case IndustryGroup::CapitalGoods:
      return _CapitalGoodsIndustries;
    case IndustryGroup::CommercialAndProfessionalServices:
      return _CommercialAndProfessionalServicesIndustries;
    case IndustryGroup::Transportation:
      return _TransportationIndustries;
    case IndustryGroup::AutomobilesAndComponents:
      return _AutomobilesAndComponentsIndustries;
    case IndustryGroup::ConsumerDurablesAndApparel:
      return _ConsumerDurablesAndApparelIndustries;
    case IndustryGroup::ConsumerServices:
      return _ConsumerServicesIndustries;
    case IndustryGroup::ConsumerDiscretionaryDistributionAndRetail:
      return _ConsumerDiscretionaryDistributionAndRetailIndustries;
    case IndustryGroup::ConsumerStaplesDistributionAndRetail:
      return _ConsumerStaplesDistributionAndRetailIndustries;
    case IndustryGroup::FoodBeverageAndTobacco:
      return _FoodBeverageAndTobaccoIndustries;
    case IndustryGroup::HouseholdAndPersonalProducts:
      return _HouseholdAndPersonalProductsIndustries;
    case IndustryGroup::HealthCareEquipmentAndServices:
      return _HealthCareEquipmentAndServicesIndustries;
    case IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences:
      return _PharmaceuticalsBiotechnologyAndLifeSciencesIndustries;
    case IndustryGroup::Banks:
      return _BanksIndustries;
    case IndustryGroup::FinancialServices:
      return _FinancialServicesIndustries;
    case IndustryGroup::Insurance:
      return _InsuranceIndustries;
    case IndustryGroup::SoftwareAndServices:
      return _SoftwareAndServicesIndustries;
    case IndustryGroup::TechnologyHardwareAndEquipment:
      return _TechnologyHardwareAndEquipmentIndustries;
    case IndustryGroup::SemiconductorsAndSemiconductorEquipment:
      return _SemiconductorsAndSemiconductorEquipmentIndustries;
    case IndustryGroup::TelecommunicationServices:
      return _TelecommunicationServicesIndustries;
    case IndustryGroup::MediaAndEntertainment:
      return _MediaAndEntertainmentIndustries;
    case IndustryGroup::Utilities:
      return _UtilitiesIndustries;
    case IndustryGroup::EquityRealEstateInvestmentTrusts:
      return _EquityRealEstateInvestmentTrustsIndustries;
    case IndustryGroup::RealEstateManagementAndDevelopment:
      return _RealEstateManagementAndDevelopmentIndustries;
    default:
      return _InvalidIndustries;
  }
}

const std::vector<SubIndustry> IndustryToSubIndustries(const Industry i) {
  switch(i) {
    case Industry::EnergyEquipmentAndServices:
      return _EnergyEquipmentAndServicesSubIndustries;
    case Industry::OilGasAndConsumeableFules:
      return _OilGasAndConsumeableFulesSubIndustries;
    case Industry::Chemicals:
      return _ChemicalsSubIndustries;
    case Industry::ConstructionMaterials:
      return _ConstructionMaterialsSubIndustries;
    case Industry::ContainersAndPackaging:
      return _ContainersAndPackagingSubIndustries;
    case Industry::MetalsAndMining:
      return _MetalsAndMiningSubIndustries;
    case Industry::PaperAndForestProducts:
      return _PaperAndForestProductsSubIndustries;
    case Industry::AerospaceAndDefense:
      return _AerospaceAndDefenseSubIndustries;
    case Industry::BuildingProducts:
      return _BuildingProductsSubIndustries;
    case Industry::ConstructionAndEngineering:
      return _ConstructionAndEngineeringSubIndustries;
    case Industry::ElectricalEquipment:
      return _ElectricalEquipmentSubIndustries;
    case Industry::IndustrialConglomerates:
      return _IndustrialConglomeratesSubIndustries;
    case Industry::Machinery:
      return _MachinerySubIndustries;
    case Industry::TradingCompaniesAndDistributors:
      return _TradingCompaniesAndDistributorsSubIndustries;
    case Industry::CommercialServicesAndSupplies:
      return _CommercialServicesAndSuppliesSubIndustries;
    case Industry::ProfessionalServices:
      return _ProfessionalServicesSubIndustries;
    case Industry::AirFreightAndLogistics:
      return _AirFreightAndLogisticsSubIndustries;
    case Industry::PassengerAirlines:
      return _PassengerAirlinesSubIndustries;
    case Industry::MarineTransportation:
      return _MarineTransportationSubIndustries;
    case Industry::GroundTransportation:
      return _GroundTransportationSubIndustries;
    case Industry::TransportationInfrastructure:
      return _TransportationInfrastructureSubIndustries;
    case Industry::AutomobileComponents:
      return _AutomobileComponentsSubIndustries;
    case Industry::Automobiles:
      return _AutomobilesSubIndustries;
    case Industry::HouseholdDurables:
      return _HouseholdDurablesSubIndustries;
    case Industry::LeisureProducts:
      return _LeisureProductsSubIndustries;
    case Industry::TextilesApparelAndLuxuryGoods:
      return _TextilesApparelAndLuxuryGoodsSubIndustries;
    case Industry::HotelsRestaurantsAndLeisure:
      return _HotelsRestaurantsAndLeisureSubIndustries;
    case Industry::DiversifiedConsumerServices:
      return _DiversifiedConsumerServicesSubIndustries;
    case Industry::Distributors:
      return _DistributorsSubIndustries;
    case Industry::BroadlineRetail:
      return _BroadlineRetailSubIndustries;
    case Industry::SpecialtyRetail:
      return _SpecialtyRetailSubIndustries;
    case Industry::ConsumerStaplesDistributionAndRetail:
      return _ConsumerStaplesDistributionAndRetailSubIndustries;
    case Industry::Beverages:
      return _BeveragesSubIndustries;
    case Industry::FoodProducts:
      return _FoodProductsSubIndustries;
    case Industry::Tobacco:
      return _TobaccoSubIndustries;
    case Industry::HouseholdProducts:
      return _HouseholdProductsSubIndustries;
    case Industry::PersonalCareProducts:
      return _PersonalCareProductsSubIndustries;
    case Industry::HealthCareEquipmentAndSupplies:
      return _HealthCareEquipmentAndSuppliesSubIndustries;
    case Industry::HealthCareProvidersAndServices:
      return _HealthCareProvidersAndServicesSubIndustries;
    case Industry::HealthCareTechnology:
      return _HealthCareTechnologySubIndustries;
    case Industry::Biotechnology:
      return _BiotechnologySubIndustries;
    case Industry::Pharmaceuticals:
      return _PharmaceuticalsSubIndustries;
    case Industry::LifeSciencesToolsAndServices:
      return _LifeSciencesToolsAndServicesSubIndustries;
    case Industry::Banks:
      return _BanksSubIndustries;
    case Industry::FinancialServices:
      return _FinancialServicesSubIndustries;
    case Industry::ConsumerFinance:
      return _ConsumerFinanceSubIndustries;
    case Industry::CapitalMarkets:
      return _CapitalMarketsSubIndustries;
    case Industry::MortgageRealEstateInvestmentTrusts:
      return _MortgageRealEstateInvestmentTrustsSubIndustries;
    case Industry::Insurance:
      return _InsuranceSubIndustries;
    case Industry::ITServices:
      return _ITServicesSubIndustries;
    case Industry::Software:
      return _SoftwareSubIndustries;
    case Industry::CommunicationsEquipment:
      return _CommunicationsEquipmentSubIndustries;
    case Industry::TechnologyHardwareStorageAndPeripherals:
      return _TechnologyHardwareStorageAndPeripheralsSubIndustries;
    case Industry::ElectronicEquipmentInstrumentsAndComponents:
      return _ElectronicEquipmentInstrumentsAndComponentsSubIndustries;
    case Industry::SemiconductorsAndSemiconductorEquipment:
      return _SemiconductorsAndSemiconductorEquipmentSubIndustries;
    case Industry::DiversifiedTelecommunicationServices:
      return _DiversifiedTelecommunicationServicesSubIndustries;
    case Industry::WirelessTelecommunicationServices:
      return _WirelessTelecommunicationServicesSubIndustries;
    case Industry::Media:
      return _MediaSubIndustries;
    case Industry::Entertainment:
      return _EntertainmentSubIndustries;
    case Industry::InteractiveMediaAndServices:
      return _InteractiveMediaAndServicesSubIndustries;
    case Industry::ElectricUtilities:
      return _ElectricUtilitiesSubIndustries;
    case Industry::GasUtilities:
      return _GasUtilitiesSubIndustries;
    case Industry::MultiUtilities:
      return _MultiUtilitiesSubIndustries;
    case Industry::WaterUtilities:
      return _WaterUtilitiesSubIndustries;
    case Industry::IndependentPowerAndRenewableElectricityProducers:
      return _IndependentPowerAndRenewableElectricityProducersSubIndustries;
    case Industry::DiversifiedREITs:
      return _DiversifiedREITsSubIndustries;
    case Industry::IndustrialREITs:
      return _IndustrialREITsSubIndustries;
    case Industry::HotelAndResortREITs:
      return _HotelAndResortREITsSubIndustries;
    case Industry::OfficeREITs:
      return _OfficeREITsSubIndustries;
    case Industry::HealthCareREITs:
      return _HealthCareREITsSubIndustries;
    case Industry::ResidentialREITs:
      return _ResidentialREITsSubIndustries;
    case Industry::RetailREITs:
      return _RetailREITsSubIndustries;
    case Industry::SpecializedREITs:
      return _SpecializedREITsSubIndustries;
    case Industry::RealEstateManagementAndDevelopment:
      return _RealEstateManagementAndDevelopmentSubIndustries;
    default:
      return _InvalidSubIndustries;
  }
}

Sector IndustryGroupToSector(const IndustryGroup ig) {
  switch(ig) {
    case IndustryGroup::Energy:
      return Sector::Energy;
    case IndustryGroup::Materials:
      return Sector::Materials;
    case IndustryGroup::CapitalGoods:
      return Sector::Industrials;
    case IndustryGroup::CommercialAndProfessionalServices:
      return Sector::Industrials;
    case IndustryGroup::Transportation:
      return Sector::Industrials;
    case IndustryGroup::AutomobilesAndComponents:
      return Sector::ConsumerDiscretionary;
    case IndustryGroup::ConsumerDurablesAndApparel:
      return Sector::ConsumerDiscretionary;
    case IndustryGroup::ConsumerServices:
      return Sector::ConsumerDiscretionary;
    case IndustryGroup::ConsumerDiscretionaryDistributionAndRetail:
      return Sector::ConsumerDiscretionary;
    case IndustryGroup::ConsumerStaplesDistributionAndRetail:
      return Sector::ConsumerStaples;
    case IndustryGroup::FoodBeverageAndTobacco:
      return Sector::ConsumerStaples;
    case IndustryGroup::HouseholdAndPersonalProducts:
      return Sector::ConsumerStaples;
    case IndustryGroup::HealthCareEquipmentAndServices:
      return Sector::HealthCare;
    case IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences:
      return Sector::HealthCare;
    case IndustryGroup::Banks:
      return Sector::Financials;
    case IndustryGroup::FinancialServices:
      return Sector::Financials;
    case IndustryGroup::Insurance:
      return Sector::Financials;
    case IndustryGroup::SoftwareAndServices:
      return Sector::InformationTechnology;
    case IndustryGroup::TechnologyHardwareAndEquipment:
      return Sector::InformationTechnology;
    case IndustryGroup::SemiconductorsAndSemiconductorEquipment:
      return Sector::InformationTechnology;
    case IndustryGroup::TelecommunicationServices:
      return Sector::CommunicationServices;
    case IndustryGroup::MediaAndEntertainment:
      return Sector::CommunicationServices;
    case IndustryGroup::Utilities:
      return Sector::Utilities;
    case IndustryGroup::EquityRealEstateInvestmentTrusts:
      return Sector::RealEstate;
    case IndustryGroup::RealEstateManagementAndDevelopment:
      return Sector::RealEstate;
    default:
      return Sector::Invalid;
  }
}

IndustryGroup IndustryToIndustryGroup(const Industry i) {
  switch(i) {
    case Industry::EnergyEquipmentAndServices:
      return IndustryGroup::Energy;
    case Industry::OilGasAndConsumeableFules:
      return IndustryGroup::Energy;
    case Industry::Chemicals:
      return IndustryGroup::Materials;
    case Industry::ConstructionMaterials:
      return IndustryGroup::Materials;
    case Industry::ContainersAndPackaging:
      return IndustryGroup::Materials;
    case Industry::MetalsAndMining:
      return IndustryGroup::Materials;
    case Industry::PaperAndForestProducts:
      return IndustryGroup::Materials;
    case Industry::AerospaceAndDefense:
      return IndustryGroup::CapitalGoods;
    case Industry::BuildingProducts:
      return IndustryGroup::CapitalGoods;
    case Industry::ConstructionAndEngineering:
      return IndustryGroup::CapitalGoods;
    case Industry::ElectricalEquipment:
      return IndustryGroup::CapitalGoods;
    case Industry::IndustrialConglomerates:
      return IndustryGroup::CapitalGoods;
    case Industry::Machinery:
      return IndustryGroup::CapitalGoods;
    case Industry::TradingCompaniesAndDistributors:
      return IndustryGroup::CapitalGoods;
    case Industry::CommercialServicesAndSupplies:
      return IndustryGroup::CommercialAndProfessionalServices;
    case Industry::ProfessionalServices:
      return IndustryGroup::CommercialAndProfessionalServices;
    case Industry::AirFreightAndLogistics:
      return IndustryGroup::Transportation;
    case Industry::PassengerAirlines:
      return IndustryGroup::Transportation;
    case Industry::MarineTransportation:
      return IndustryGroup::Transportation;
    case Industry::GroundTransportation:
      return IndustryGroup::Transportation;
    case Industry::TransportationInfrastructure:
      return IndustryGroup::Transportation;
    case Industry::AutomobileComponents:
      return IndustryGroup::AutomobilesAndComponents;
    case Industry::Automobiles:
      return IndustryGroup::AutomobilesAndComponents;
    case Industry::HouseholdDurables:
      return IndustryGroup::ConsumerDurablesAndApparel;
    case Industry::LeisureProducts:
      return IndustryGroup::ConsumerDurablesAndApparel;
    case Industry::TextilesApparelAndLuxuryGoods:
      return IndustryGroup::ConsumerDurablesAndApparel;
    case Industry::HotelsRestaurantsAndLeisure:
      return IndustryGroup::ConsumerServices;
    case Industry::DiversifiedConsumerServices:
      return IndustryGroup::ConsumerServices;
    case Industry::Distributors:
      return IndustryGroup::ConsumerDiscretionaryDistributionAndRetail;
    case Industry::BroadlineRetail:
      return IndustryGroup::ConsumerDiscretionaryDistributionAndRetail;
    case Industry::SpecialtyRetail:
      return IndustryGroup::ConsumerDiscretionaryDistributionAndRetail;
    case Industry::ConsumerStaplesDistributionAndRetail:
      return IndustryGroup::ConsumerStaplesDistributionAndRetail;
    case Industry::Beverages:
      return IndustryGroup::FoodBeverageAndTobacco;
    case Industry::FoodProducts:
      return IndustryGroup::FoodBeverageAndTobacco;
    case Industry::Tobacco:
      return IndustryGroup::FoodBeverageAndTobacco;
    case Industry::HouseholdProducts:
      return IndustryGroup::HouseholdAndPersonalProducts;
    case Industry::PersonalCareProducts:
      return IndustryGroup::HouseholdAndPersonalProducts;
    case Industry::HealthCareEquipmentAndSupplies:
      return IndustryGroup::HealthCareEquipmentAndServices;
    case Industry::HealthCareProvidersAndServices:
      return IndustryGroup::HealthCareEquipmentAndServices;
    case Industry::HealthCareTechnology:
      return IndustryGroup::HealthCareEquipmentAndServices;
    case Industry::Biotechnology:
      return IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences;
    case Industry::Pharmaceuticals:
      return IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences;
    case Industry::LifeSciencesToolsAndServices:
      return IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences;
    case Industry::Banks:
      return IndustryGroup::Banks;
    case Industry::FinancialServices:
      return IndustryGroup::FinancialServices;
    case Industry::ConsumerFinance:
      return IndustryGroup::FinancialServices;
    case Industry::CapitalMarkets:
      return IndustryGroup::FinancialServices;
    case Industry::MortgageRealEstateInvestmentTrusts:
      return IndustryGroup::FinancialServices;
    case Industry::Insurance:
      return IndustryGroup::Insurance;
    case Industry::ITServices:
      return IndustryGroup::SoftwareAndServices;
    case Industry::Software:
      return IndustryGroup::SoftwareAndServices;
    case Industry::CommunicationsEquipment:
      return IndustryGroup::TechnologyHardwareAndEquipment;
    case Industry::TechnologyHardwareStorageAndPeripherals:
      return IndustryGroup::TechnologyHardwareAndEquipment;
    case Industry::ElectronicEquipmentInstrumentsAndComponents:
      return IndustryGroup::TechnologyHardwareAndEquipment;
    case Industry::SemiconductorsAndSemiconductorEquipment:
      return IndustryGroup::SemiconductorsAndSemiconductorEquipment;
    case Industry::DiversifiedTelecommunicationServices:
      return IndustryGroup::TelecommunicationServices;
    case Industry::WirelessTelecommunicationServices:
      return IndustryGroup::TelecommunicationServices;
    case Industry::Media:
      return IndustryGroup::MediaAndEntertainment;
    case Industry::Entertainment:
      return IndustryGroup::MediaAndEntertainment;
    case Industry::InteractiveMediaAndServices:
      return IndustryGroup::MediaAndEntertainment;
    case Industry::ElectricUtilities:
      return IndustryGroup::Utilities;
    case Industry::GasUtilities:
      return IndustryGroup::Utilities;
    case Industry::MultiUtilities:
      return IndustryGroup::Utilities;
    case Industry::WaterUtilities:
      return IndustryGroup::Utilities;
    case Industry::IndependentPowerAndRenewableElectricityProducers:
      return IndustryGroup::Utilities;
    case Industry::DiversifiedREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::IndustrialREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::HotelAndResortREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::OfficeREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::HealthCareREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::ResidentialREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::RetailREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::SpecializedREITs:
      return IndustryGroup::EquityRealEstateInvestmentTrusts;
    case Industry::RealEstateManagementAndDevelopment:
      return IndustryGroup::RealEstateManagementAndDevelopment;
    default:
      return IndustryGroup::Invalid;
  }
}

Industry SubIndustryToIndustry(const SubIndustry si) {
  switch(si) {
    case SubIndustry::OilAndGasDrilling:
      return Industry::EnergyEquipmentAndServices;
    case SubIndustry::OilAndGasEquipmentAndServices:
      return Industry::EnergyEquipmentAndServices;
    case SubIndustry::IntegratedOilAndGas:
      return Industry::OilGasAndConsumeableFules;
    case SubIndustry::OilAndGasExplorationAndProduction:
      return Industry::OilGasAndConsumeableFules;
    case SubIndustry::OilAndGasRefiningAndMarketing:
      return Industry::OilGasAndConsumeableFules;
    case SubIndustry::OilAndGasStorageAndTransportation:
      return Industry::OilGasAndConsumeableFules;
    case SubIndustry::CoalAndConsumeableFuels:
      return Industry::OilGasAndConsumeableFules;
    case SubIndustry::CommodityChemicals:
      return Industry::Chemicals;
    case SubIndustry::DiversifiedChemicals:
      return Industry::Chemicals;
    case SubIndustry::FertilizersAndAgriculturalChemicals:
      return Industry::Chemicals;
    case SubIndustry::IndustrialGases:
      return Industry::Chemicals;
    case SubIndustry::SpecialtyChemicals:
      return Industry::Chemicals;
    case SubIndustry::ConstructionMaterials:
      return Industry::ConstructionMaterials;
    case SubIndustry::MetalGlassAndPlasticContainers:
      return Industry::ContainersAndPackaging;
    case SubIndustry::PaperAndPlasticPackagingProductsAndMaterials:
      return Industry::ContainersAndPackaging;
    case SubIndustry::Aluminum:
      return Industry::MetalsAndMining;
    case SubIndustry::DiversifiedMetalsAndMining:
      return Industry::MetalsAndMining;
    case SubIndustry::Copper:
      return Industry::MetalsAndMining;
    case SubIndustry::Gold:
      return Industry::MetalsAndMining;
    case SubIndustry::PreciousMetalsAndMinerals:
      return Industry::MetalsAndMining;
    case SubIndustry::Silver:
      return Industry::MetalsAndMining;
    case SubIndustry::Steel:
      return Industry::MetalsAndMining;
    case SubIndustry::ForestProducts:
      return Industry::PaperAndForestProducts;
    case SubIndustry::PaperProducts:
      return Industry::PaperAndForestProducts;
    case SubIndustry::AerospaceAndDefense:
      return Industry::AerospaceAndDefense;
    case SubIndustry::BuildingProducts:
      return Industry::BuildingProducts;
    case SubIndustry::ConstructionAndEngineering:
      return Industry::ConstructionAndEngineering;
    case SubIndustry::ElectricalComponentsAndEquipment:
      return Industry::ElectricalEquipment;
    case SubIndustry::HeavyElectricalEquipment:
      return Industry::ElectricalEquipment;
    case SubIndustry::IndustrialConglomerates:
      return Industry::IndustrialConglomerates;
    case SubIndustry::ConstructionMachineryAndHeavyTransportationEquipment:
      return Industry::Machinery;
    case SubIndustry::AgriculturalAndFarmMachinery:
      return Industry::Machinery;
    case SubIndustry::IndustrialMachinerySuppliesAndComponents:
      return Industry::Machinery;
    case SubIndustry::TradingCompaniesAndDistributors:
      return Industry::TradingCompaniesAndDistributors;
    case SubIndustry::CommercialPrinting:
      return Industry::CommercialServicesAndSupplies;
    case SubIndustry::EnvironmentalAndFacilitiesServices:
      return Industry::CommercialServicesAndSupplies;
    case SubIndustry::OfficeServicesAndSupplies:
      return Industry::CommercialServicesAndSupplies;
    case SubIndustry::DiviersifiedSupportServices:
      return Industry::CommercialServicesAndSupplies;
    case SubIndustry::SecurityAndAlarmServices:
      return Industry::CommercialServicesAndSupplies;
    case SubIndustry::HumanResourcesAndEmploymentServices:
      return Industry::ProfessionalServices;
    case SubIndustry::ResearchAndConsultingServices:
      return Industry::ProfessionalServices;
    case SubIndustry::DataProcessingAndOutsourcedServices:
      return Industry::ProfessionalServices;
    case SubIndustry::AirFreightAndLogistics:
      return Industry::AirFreightAndLogistics;
    case SubIndustry::PassengerAirlines:
      return Industry::PassengerAirlines;
    case SubIndustry::MarineTransportation:
      return Industry::MarineTransportation;
    case SubIndustry::RailTransportation:
      return Industry::GroundTransportation;
    case SubIndustry::CargoGroundTransportation:
      return Industry::GroundTransportation;
    case SubIndustry::PassengerGroundTransportation:
      return Industry::GroundTransportation;
    case SubIndustry::AirportServices:
      return Industry::TransportationInfrastructure;
    case SubIndustry::HighwaysAndRailtracks:
      return Industry::TransportationInfrastructure;
    case SubIndustry::MarinePortsAndServices:
      return Industry::TransportationInfrastructure;
    case SubIndustry::AutomotivePartsAndEquipment:
      return Industry::AutomobileComponents;
    case SubIndustry::TiresAndRubber:
      return Industry::AutomobileComponents;
    case SubIndustry::AutomobileManufacturers:
      return Industry::Automobiles;
    case SubIndustry::MotorcycleManufacturers:
      return Industry::Automobiles;
    case SubIndustry::ConsumerElectronics:
      return Industry::HouseholdDurables;
    case SubIndustry::HomeFurnishings:
      return Industry::HouseholdDurables;
    case SubIndustry::Homebuilding:
      return Industry::HouseholdDurables;
    case SubIndustry::HouseholdAppliances:
      return Industry::HouseholdDurables;
    case SubIndustry::HousewaresAndSpecialties:
      return Industry::HouseholdDurables;
    case SubIndustry::LeisureProducts:
      return Industry::LeisureProducts;
    case SubIndustry::ApparelAccessoriesAndLuxuryGoods:
      return Industry::TextilesApparelAndLuxuryGoods;
    case SubIndustry::Footwear:
      return Industry::TextilesApparelAndLuxuryGoods;
    case SubIndustry::Textiles:
      return Industry::TextilesApparelAndLuxuryGoods;
    case SubIndustry::CasinosAndGaming:
      return Industry::HotelsRestaurantsAndLeisure;
    case SubIndustry::HotelsResortsAndCruiseLines:
      return Industry::HotelsRestaurantsAndLeisure;
    case SubIndustry::LeisureFacilities:
      return Industry::HotelsRestaurantsAndLeisure;
    case SubIndustry::Restaurants:
      return Industry::HotelsRestaurantsAndLeisure;
    case SubIndustry::EducationServices:
      return Industry::DiversifiedConsumerServices;
    case SubIndustry::SpecializedConsumerServices:
      return Industry::DiversifiedConsumerServices;
    case SubIndustry::Distributors:
      return Industry::Distributors;
    case SubIndustry::BroadlineRetail:
      return Industry::BroadlineRetail;
    case SubIndustry::ApparelRetail:
      return Industry::SpecialtyRetail;
    case SubIndustry::ComputerAndElectronicsretail:
      return Industry::SpecialtyRetail;
    case SubIndustry::HomeImprovementRetail:
      return Industry::SpecialtyRetail;
    case SubIndustry::OtherSpecialtyRetail:
      return Industry::SpecialtyRetail;
    case SubIndustry::AutomotiveRetail:
      return Industry::SpecialtyRetail;
    case SubIndustry::HomefurnishingRetail:
      return Industry::SpecialtyRetail;
    case SubIndustry::DrugRetail:
      return Industry::ConsumerStaplesDistributionAndRetail;
    case SubIndustry::FoodDistributors:
      return Industry::ConsumerStaplesDistributionAndRetail;
    case SubIndustry::FoodRetail:
      return Industry::ConsumerStaplesDistributionAndRetail;
    case SubIndustry::ConsumerStaplesMerchandiseRetail:
      return Industry::ConsumerStaplesDistributionAndRetail;
    case SubIndustry::Brewers:
      return Industry::Beverages;
    case SubIndustry::DistillersAndVintners:
      return Industry::Beverages;
    case SubIndustry::SoftDrinksAndNonAlcoholicBeverages:
      return Industry::Beverages;
    case SubIndustry::AgriculturalProductsAndServices:
      return Industry::FoodProducts;
    case SubIndustry::PackagedFoodsAndMeats:
      return Industry::FoodProducts;
    case SubIndustry::Tobacco:
      return Industry::Tobacco;
    case SubIndustry::HouseholdProducts:
      return Industry::HouseholdProducts;
    case SubIndustry::PersonalCareProducts:
      return Industry::PersonalCareProducts;
    case SubIndustry::HealthCareEquipment:
      return Industry::HealthCareEquipmentAndSupplies;
    case SubIndustry::HealthCareSupplies:
      return Industry::HealthCareEquipmentAndSupplies;
    case SubIndustry::HealthCareDistributors:
      return Industry::HealthCareProvidersAndServices;
    case SubIndustry::HealthCareServices:
      return Industry::HealthCareProvidersAndServices;
    case SubIndustry::HealthCareFacilities:
      return Industry::HealthCareProvidersAndServices;
    case SubIndustry::ManagedHealthCare:
      return Industry::HealthCareProvidersAndServices;
    case SubIndustry::HealthCareTechnology:
      return Industry::HealthCareTechnology;
    case SubIndustry::Biotechnology:
      return Industry::Biotechnology;
    case SubIndustry::Pharmaceuticals:
      return Industry::Pharmaceuticals;
    case SubIndustry::LifeSciencesToolsAndServices:
      return Industry::LifeSciencesToolsAndServices;
    case SubIndustry::DiversifiedBanks:
      return Industry::Banks;
    case SubIndustry::RegionalBanks:
      return Industry::Banks;
    case SubIndustry::DiversifiedFinancialServices:
      return Industry::FinancialServices;
    case SubIndustry::MultiSectorHoldings:
      return Industry::FinancialServices;
    case SubIndustry::SpecializedFinance:
      return Industry::FinancialServices;
    case SubIndustry::CommercialAndResidentialMortgageFinance:
      return Industry::FinancialServices;
    case SubIndustry::TransactionAndPaymentProcessingServices:
      return Industry::FinancialServices;
    case SubIndustry::ConsumerFinance:
      return Industry::ConsumerFinance;
    case SubIndustry::AssetManagementAndCustodyBanks:
      return Industry::CapitalMarkets;
    case SubIndustry::InvestmentBankingAndBrokerage:
      return Industry::CapitalMarkets;
    case SubIndustry::DiversifiedCapitalMarkets:
      return Industry::CapitalMarkets;
    case SubIndustry::FinancialExchangesAndData:
      return Industry::CapitalMarkets;
    case SubIndustry::MortgageRealEstateInvestmentTrusts:
      return Industry::MortgageRealEstateInvestmentTrusts;
    case SubIndustry::InsuranceBrokers:
      return Industry::Insurance;
    case SubIndustry::LifeAndHealthInsurance:
      return Industry::Insurance;
    case SubIndustry::MultilineInsurance:
      return Industry::Insurance;
    case SubIndustry::PropertyAndCasualtyInsurance:
      return Industry::Insurance;
    case SubIndustry::Reinsurance:
      return Industry::Insurance;
    case SubIndustry::ITConsultingAndOtherServices:
      return Industry::ITServices;
    case SubIndustry::InternetServicesAndInfrastructure:
      return Industry::ITServices;
    case SubIndustry::ApplicationSoftware:
      return Industry::Software;
    case SubIndustry::SystemsSoftware:
      return Industry::Software;
    case SubIndustry::CommunicationsEquipment:
      return Industry::CommunicationsEquipment;
    case SubIndustry::TechnologyHardwareStorageAndPeripherals:
      return Industry::TechnologyHardwareStorageAndPeripherals;
    case SubIndustry::ElectronicEquipmentAndInstruments:
      return Industry::ElectronicEquipmentInstrumentsAndComponents;
    case SubIndustry::ElectronicComponents:
      return Industry::ElectronicEquipmentInstrumentsAndComponents;
    case SubIndustry::ElectronicManufacturingServices:
      return Industry::ElectronicEquipmentInstrumentsAndComponents;
    case SubIndustry::TechnologyDistributors:
      return Industry::ElectronicEquipmentInstrumentsAndComponents;
    case SubIndustry::SemiconductorMaterialsAndEquipment:
      return Industry::SemiconductorsAndSemiconductorEquipment;
    case SubIndustry::Semiconductors:
      return Industry::SemiconductorsAndSemiconductorEquipment;
    case SubIndustry::AlternativeCarriers:
      return Industry::DiversifiedTelecommunicationServices;
    case SubIndustry::IntegratedTelecommunicationServices:
      return Industry::DiversifiedTelecommunicationServices;
    case SubIndustry::WirelessTelecommunicationServices:
      return Industry::WirelessTelecommunicationServices;
    case SubIndustry::Advertising:
      return Industry::Media;
    case SubIndustry::Broadcasting:
      return Industry::Media;
    case SubIndustry::CableAndSatellite:
      return Industry::Media;
    case SubIndustry::Publishing:
      return Industry::Media;
    case SubIndustry::MoviesAndEntertainment:
      return Industry::Entertainment;
    case SubIndustry::InteractiveHomeEntertainment:
      return Industry::Entertainment;
    case SubIndustry::InteractiveMediaAndServices:
      return Industry::InteractiveMediaAndServices;
    case SubIndustry::ElectricUtilities:
      return Industry::ElectricUtilities;
    case SubIndustry::GasUtilities:
      return Industry::GasUtilities;
    case SubIndustry::MultiUtilities:
      return Industry::MultiUtilities;
    case SubIndustry::WaterUtilities:
      return Industry::WaterUtilities;
    case SubIndustry::IndependentPowerProducersAndEnergyTraders:
      return Industry::IndependentPowerAndRenewableElectricityProducers;
    case SubIndustry::RenewableElectricity:
      return Industry::IndependentPowerAndRenewableElectricityProducers;
    case SubIndustry::DiversifiedREITs:
      return Industry::DiversifiedREITs;
    case SubIndustry::IndustrialREITs:
      return Industry::IndustrialREITs;
    case SubIndustry::HotelAndResortREITs:
      return Industry::HotelAndResortREITs;
    case SubIndustry::OfficeREITs:
      return Industry::OfficeREITs;
    case SubIndustry::HealthCareREITs:
      return Industry::HealthCareREITs;
    case SubIndustry::MultiFamilyResidentialREITs:
      return Industry::ResidentialREITs;
    case SubIndustry::SingleFamilyResidentialREITs:
      return Industry::ResidentialREITs;
    case SubIndustry::RetailREITs:
      return Industry::RetailREITs;
    case SubIndustry::OtherSpecializedREITs:
      return Industry::SpecializedREITs;
    case SubIndustry::SelfStorageREITs:
      return Industry::SpecializedREITs;
    case SubIndustry::TelecomTowerREITs:
      return Industry::SpecializedREITs;
    case SubIndustry::TimberREITs:
      return Industry::SpecializedREITs;
    case SubIndustry::DataCenterREITs:
      return Industry::SpecializedREITs;
    case SubIndustry::DiversifiedRealEstateActivities:
      return Industry::RealEstateManagementAndDevelopment;
    case SubIndustry::RealEstateOperatingCompanies:
      return Industry::RealEstateManagementAndDevelopment;
    case SubIndustry::RealEstateDevelopment:
      return Industry::RealEstateManagementAndDevelopment;
    case SubIndustry::RealEstateServices:
      return Industry::RealEstateManagementAndDevelopment;
    default:
      return Industry::Invalid;
  }
}

}
