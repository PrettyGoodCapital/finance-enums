#pragma once
#include <deque>
#include <iostream>
#include <memory>
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <string>
#include <vector>
// #include <pybind11_json/pybind11_json.hpp>

#include <finance-enums/common.hpp>
#include <finance-enums/bond.hpp>
#include <finance-enums/commodity.hpp>
#include <finance-enums/country.hpp>
#include <finance-enums/currency.hpp>
#include <finance-enums/equity.hpp>
#include <finance-enums/exchange.hpp>
#include <finance-enums/exports.hpp>
#include <finance-enums/fund.hpp>
#include <finance-enums/future.hpp>
#include <finance-enums/instrument.hpp>
#include <finance-enums/option.hpp>
#include <finance-enums/sector.hpp>
#include <finance-enums/security.hpp>
#include <finance-enums/trading.hpp>

namespace py = pybind11;
using namespace finance_enums;

PYBIND11_MODULE(extension, m) {
  m.doc() = "C++ bindings to finance-enums library";

  // Bond
  py::enum_<BondType>(m, "BondType", py::arithmetic())
    .value("Invalid", BondType::Invalid)
    .value("Corporate", BondType::Corporate)
    .value("Government", BondType::Government)
    .value("Municipal", BondType::Municipal)
    .def("__str__", &BondTypeToString, py::prepend())
    .def("__repr__", &BondTypeToString, py::prepend())
    .def(py::init(&BondTypeFromString));

  // Commodity
  py::enum_<CommodityType>(m, "CommodityType", py::arithmetic())
    .value("Invalid", CommodityType::Invalid)
    .value("Energy", CommodityType::Energy)
    .value("Metals", CommodityType::Metals)
    .value("Agriculture", CommodityType::Agriculture)
    .def("__str__", &CommodityTypeToString, py::prepend())
    .def("__repr__", &CommodityTypeToString, py::prepend())
    .def(py::init(&CommodityTypeFromString));
  py::enum_<EnergyType>(m, "EnergyType", py::arithmetic())
    .value("Invalid", EnergyType::Invalid)
    .value("Crude", EnergyType::Crude)
    .value("NaturalGas", EnergyType::NaturalGas)
    .def("__str__", &EnergyTypeToString, py::prepend())
    .def("__repr__", &EnergyTypeToString, py::prepend())
    .def(py::init(&EnergyTypeFromString));
  py::enum_<MetalsType>(m, "MetalsType", py::arithmetic())
    .value("Invalid", MetalsType::Invalid)
    .value("Gold", MetalsType::Gold)
    .value("Silver", MetalsType::Silver)
    .value("Copper", MetalsType::Copper)
    .value("Platinum", MetalsType::Platinum)
    .value("Palladium", MetalsType::Palladium)
    .def("__str__", &MetalsTypeToString, py::prepend())
    .def("__repr__", &MetalsTypeToString, py::prepend())
    .def(py::init(&MetalsTypeFromString));
  py::enum_<AgricultureType>(m, "AgricultureType", py::arithmetic())
    .value("Invalid", AgricultureType::Invalid)
    .value("Corn", AgricultureType::Corn)
    .value("Wheat", AgricultureType::Wheat)
    .value("Oats", AgricultureType::Oats)
    .value("Soybean", AgricultureType::Soybean)
    .value("Cocoa", AgricultureType::Cocoa)
    .value("Coffee", AgricultureType::Coffee)
    .value("Sugar", AgricultureType::Sugar)
    .value("Cotten", AgricultureType::Cotten)
    .value("OrangeJuice", AgricultureType::OrangeJuice)
    .value("Cattle", AgricultureType::Cattle)
    .value("Hogs", AgricultureType::Hogs)
    .def("__str__", &AgricultureTypeToString, py::prepend())
    .def("__repr__", &AgricultureTypeToString, py::prepend())
    .def(py::init(&AgricultureTypeFromString));

  // Country in long enums

  // Currency in long enums

  // Equity
  py::enum_<EquityType>(m, "EquityType", py::arithmetic())
    .value("Invalid", EquityType::Invalid)
    .value("Shares", EquityType::Shares)
    .value("PreferredShares", EquityType::PreferredShares)
    .value("ConvertibleShares", EquityType::ConvertibleShares)
    .value("PreferredConvertibleShares", EquityType::PreferredConvertibleShares)
    .value("DepositoryReceipt", EquityType::DepositoryReceipt)
    .def("__str__", &EquityTypeToString, py::prepend())
    .def("__repr__", &EquityTypeToString, py::prepend())
    .def(py::init(&EquityTypeFromString));

  // Exchange
  py::enum_<ExchangeCode>(m, "ExchangeCode", py::arithmetic())
    .value("XXXX", ExchangeCode::XXXX)
    .value("PYPR", ExchangeCode::PYPR)
    .value("SIMU", ExchangeCode::SIMU)
    .value("XNYS", ExchangeCode::XNYS)
    .value("NYSD", ExchangeCode::NYSD)
    .value("XCIS", ExchangeCode::XCIS)
    .value("CISD", ExchangeCode::CISD)
    .value("XCHI", ExchangeCode::XCHI)
    .value("ARCX", ExchangeCode::ARCX)
    .value("ARCD", ExchangeCode::ARCD)
    .value("ARCO", ExchangeCode::ARCO)
    .value("XASE", ExchangeCode::XASE)
    .value("AMXO", ExchangeCode::AMXO)
    .value("XNAS", ExchangeCode::XNAS)
    .value("XNGS", ExchangeCode::XNGS)
    .value("XNCM", ExchangeCode::XNCM)
    .value("XNMS", ExchangeCode::XNMS)
    .value("NASD", ExchangeCode::NASD)
    .value("XNDQ", ExchangeCode::XNDQ)
    .value("XBOS", ExchangeCode::XBOS)
    .value("BOSD", ExchangeCode::BOSD)
    .value("XBXO", ExchangeCode::XBXO)
    .value("XPHL", ExchangeCode::XPHL)
    .value("XPSX", ExchangeCode::XPSX)
    .value("PSXD", ExchangeCode::PSXD)
    .value("XPHO", ExchangeCode::XPHO)
    .value("XPBT", ExchangeCode::XPBT)
    .value("XPOR", ExchangeCode::XPOR)
    .value("XNFI", ExchangeCode::XNFI)
    .value("XISE", ExchangeCode::XISE)
    .value("GMNI", ExchangeCode::GMNI)
    .value("MCRY", ExchangeCode::MCRY)
    .value("XCBO", ExchangeCode::XCBO)
    .value("EDGA", ExchangeCode::EDGA)
    .value("EDGD", ExchangeCode::EDGD)
    .value("EDGX", ExchangeCode::EDGX)
    .value("EDDP", ExchangeCode::EDDP)
    .value("EDGO", ExchangeCode::EDGO)
    .value("BATS", ExchangeCode::BATS)
    .value("BZXD", ExchangeCode::BZXD)
    .value("BATO", ExchangeCode::BATO)
    .value("BATY", ExchangeCode::BATY)
    .value("BYXD", ExchangeCode::BYXD)
    .value("C2OX", ExchangeCode::C2OX)
    .value("XCME", ExchangeCode::XCME)
    .value("FCME", ExchangeCode::FCME)
    .value("GLBX", ExchangeCode::GLBX)
    .value("XCBT", ExchangeCode::XCBT)
    .value("FCBT", ExchangeCode::FCBT)
    .value("XKBT", ExchangeCode::XKBT)
    .value("XNYM", ExchangeCode::XNYM)
    .value("MIHI", ExchangeCode::MIHI)
    .value("MPRL", ExchangeCode::MPRL)
    .value("EPRL", ExchangeCode::EPRL)
    .value("EPRD", ExchangeCode::EPRD)
    .value("XMIO", ExchangeCode::XMIO)
    .value("EMLD", ExchangeCode::EMLD)
    .value("OTCM", ExchangeCode::OTCM)
    .value("CAVE", ExchangeCode::CAVE)
    .value("OTCB", ExchangeCode::OTCB)
    .value("OTCQ", ExchangeCode::OTCQ)
    .value("PINL", ExchangeCode::PINL)
    .value("PINI", ExchangeCode::PINI)
    .value("PINX", ExchangeCode::PINX)
    .value("PSGM", ExchangeCode::PSGM)
    .value("PINC", ExchangeCode::PINC)
    .value("FINR", ExchangeCode::FINR)
    .value("FINN", ExchangeCode::FINN)
    .value("FINC", ExchangeCode::FINC)
    .value("FINY", ExchangeCode::FINY)
    .value("XADF", ExchangeCode::XADF)
    .value("FINO", ExchangeCode::FINO)
    .value("OOTC", ExchangeCode::OOTC)
    .value("OPRA", ExchangeCode::OPRA)
    .value("MEMX", ExchangeCode::MEMX)
    .value("MEMD", ExchangeCode::MEMD)
    .value("MXOP", ExchangeCode::MXOP)
    .value("IEXG", ExchangeCode::IEXG)
    .value("LTSE", ExchangeCode::LTSE)
    .value("XCNQ", ExchangeCode::XCNQ)
    .value("PURE", ExchangeCode::PURE)
    .value("CSE2", ExchangeCode::CSE2)
    .value("XTSE", ExchangeCode::XTSE)
    .value("XDRK", ExchangeCode::XDRK)
    .value("VDRK", ExchangeCode::VDRK)
    .value("XTSX", ExchangeCode::XTSX)
    .value("XTNX", ExchangeCode::XTNX)
    .value("XATS", ExchangeCode::XATS)
    .value("XATX", ExchangeCode::XATX)
    .value("ADRK", ExchangeCode::ADRK)
    .value("XMOD", ExchangeCode::XMOD)
    .value("XMOC", ExchangeCode::XMOC)
    .value("NEOE", ExchangeCode::NEOE)
    .value("NEOD", ExchangeCode::NEOD)
    .value("NEON", ExchangeCode::NEON)
    .value("NEOC", ExchangeCode::NEOC)
    .def("__str__", &ExchangeCodeToString, py::prepend())
    .def("__repr__", &ExchangeCodeToString, py::prepend())
    .def(py::init(&ExchangeCodeFromString))
    .def("parent", &ExchangeCodeToParentExchange)
    .def("country", &ExchangeCodeToCountryCode)
    .def("exchange_name", &ExchangeCodeToName)
    .def_property_readonly_static("standard", []() { return ExchangeStandard; });

  // Fund
  py::enum_<FundType>(m, "FundType", py::arithmetic())
    .value("Invalid", FundType::Invalid)
    .value("ETF", FundType::ETF)
    .value("MutualFund", FundType::MutualFund)
    .value("REIT", FundType::REIT)
    .def("__str__", &FundTypeToString, py::prepend())
    .def("__repr__", &FundTypeToString, py::prepend())
    .def(py::init(&FundTypeFromString));
  py::enum_<FundSubType>(m, "FundSubType", py::arithmetic())
    .value("Invalid", FundSubType::Invalid)
    .value("Index", FundSubType::Index)
    .value("Sector", FundSubType::Sector)
    .value("Active", FundSubType::Active)
    .value("Passive", FundSubType::Passive)
    .def("__str__", &FundSubTypeToString, py::prepend())
    .def("__repr__", &FundSubTypeToString, py::prepend())
    .def(py::init(&FundSubTypeFromString));
  py::enum_<MutualFundEndedness>(m, "MutualFundEndedness", py::arithmetic())
    .value("Invalid", MutualFundEndedness::Invalid)
    .value("Open", MutualFundEndedness::Open)
    .value("Close", MutualFundEndedness::Close)
    .def("__str__", &MutualFundEndednessToString, py::prepend())
    .def("__repr__", &MutualFundEndednessToString, py::prepend())
    .def(py::init(&MutualFundEndednessFromString));

  // Future
  py::enum_<FutureType>(m, "FutureType", py::arithmetic())
    .value("Invalid", FutureType::Invalid)
    .value("Financial", FutureType::Financial)
    .value("Commodity", FutureType::Commodity)
    .def("__str__", &FutureTypeToString, py::prepend())
    .def("__repr__", &FutureTypeToString, py::prepend())
    .def(py::init(&FutureTypeFromString));
  py::enum_<FutureDeliveryType>(m, "FutureDeliveryType", py::arithmetic())
    .value("Invalid", FutureDeliveryType::Invalid)
    .value("Physical", FutureDeliveryType::Physical)
    .value("Cash", FutureDeliveryType::Cash)
    .def("__str__", &FutureDeliveryTypeToString, py::prepend())
    .def("__repr__", &FutureDeliveryTypeToString, py::prepend())
    .def(py::init(&FutureDeliveryTypeFromString));

  // Instrument
  py::enum_<InstrumentType>(m, "InstrumentType", py::arithmetic())
    .value("Invalid", InstrumentType::Invalid)
    .value("Spot", InstrumentType::Spot)
    .value("Option", InstrumentType::Option)
    .value("Forward", InstrumentType::Forward)
    .value("Future", InstrumentType::Future)
    .value("Right", InstrumentType::Right)
    .value("Spread", InstrumentType::Spread)
    .value("Pair", InstrumentType::Pair)
    .value("Basket", InstrumentType::Basket)
    .def("__str__", &InstrumentTypeToString, py::prepend())
    .def("__repr__", &InstrumentTypeToString, py::prepend())
    .def(py::init(&InstrumentTypeFromString));

  // Option
  py::enum_<OptionType>(m, "OptionType", py::arithmetic())
    .value("Invalid", OptionType::Invalid)
    .value("Call", OptionType::Call)
    .value("Put", OptionType::Put)
    .def("__str__", &OptionTypeToString, py::prepend())
    .def("__repr__", &OptionTypeToString, py::prepend())
    .def(py::init(&OptionTypeFromString));
  py::enum_<OptionExerciseType>(m, "OptionExerciseType", py::arithmetic())
    .value("Invalid", OptionExerciseType::Invalid)
    .value("American", OptionExerciseType::American)
    .value("European", OptionExerciseType::European)
    .value("Bermudan", OptionExerciseType::Bermudan)
    .def("__str__", &OptionExerciseTypeToString, py::prepend())
    .def("__repr__", &OptionExerciseTypeToString, py::prepend())
    .def(py::init(&OptionExerciseTypeFromString));

  // Sector
  py::enum_<Sector>(m, "Sector", py::arithmetic())
    .value("Invalid", Sector::Invalid)
    .value("Energy", Sector::Energy)
    .value("Materials", Sector::Materials)
    .value("Industrials", Sector::Industrials)
    .value("ConsumerDiscretionary", Sector::ConsumerDiscretionary)
    .value("ConsumerStaples", Sector::ConsumerStaples)
    .value("HealthCare", Sector::HealthCare)
    .value("Financials", Sector::Financials)
    .value("InformationTechnology", Sector::InformationTechnology)
    .value("CommunicationServices", Sector::CommunicationServices)
    .value("Utilities", Sector::Utilities)
    .value("RealEstate", Sector::RealEstate)
    .def("__str__", &SectorToString, py::prepend())
    .def("__repr__", &SectorToString, py::prepend())
    .def(py::init(&SectorFromString))
    .def("industry_groups", &SectorToIndustryGroups);

  py::enum_<IndustryGroup>(m, "IndustryGroup", py::arithmetic())
    .value("Invalid", IndustryGroup::Invalid)
    .value("Energy", IndustryGroup::Energy)
    .value("Materials", IndustryGroup::Materials)
    .value("CapitalGoods", IndustryGroup::CapitalGoods)
    .value("CommercialAndProfessionalServices", IndustryGroup::CommercialAndProfessionalServices)
    .value("Transportation", IndustryGroup::Transportation)
    .value("AutomobilesAndComponents", IndustryGroup::AutomobilesAndComponents)
    .value("ConsumerDurablesAndApparel", IndustryGroup::ConsumerDurablesAndApparel)
    .value("ConsumerServices", IndustryGroup::ConsumerServices)
    .value("ConsumerDiscretionaryDistributionAndRetail", IndustryGroup::ConsumerDiscretionaryDistributionAndRetail)
    .value("ConsumerStaplesDistributionAndRetail", IndustryGroup::ConsumerStaplesDistributionAndRetail)
    .value("FoodBeverageAndTobacco", IndustryGroup::FoodBeverageAndTobacco)
    .value("HouseholdAndPersonalProducts", IndustryGroup::HouseholdAndPersonalProducts)
    .value("HealthCareEquipmentAndServices", IndustryGroup::HealthCareEquipmentAndServices)
    .value("PharmaceuticalsBiotechnologyAndLifeSciences", IndustryGroup::PharmaceuticalsBiotechnologyAndLifeSciences)
    .value("Banks", IndustryGroup::Banks)
    .value("FinancialServices", IndustryGroup::FinancialServices)
    .value("Insurance", IndustryGroup::Insurance)
    .value("SoftwareAndServices", IndustryGroup::SoftwareAndServices)
    .value("TechnologyHardwareAndEquipment", IndustryGroup::TechnologyHardwareAndEquipment)
    .value("SemiconductorsAndSemiconductorEquipment", IndustryGroup::SemiconductorsAndSemiconductorEquipment)
    .value("TelecommunicationServices", IndustryGroup::TelecommunicationServices)
    .value("MediaAndEntertainment", IndustryGroup::MediaAndEntertainment)
    .value("Utilities", IndustryGroup::Utilities)
    .value("EquityRealEstateInvestmentTrusts", IndustryGroup::EquityRealEstateInvestmentTrusts)
    .value("RealEstateManagementAndDevelopment", IndustryGroup::RealEstateManagementAndDevelopment)
    .def("__str__", &IndustryGroupToString, py::prepend())
    .def("__repr__", &IndustryGroupToString, py::prepend())
    .def(py::init(&IndustryGroupFromString))
    .def("sector", &IndustryGroupToSector)
    .def("industries", &IndustryGroupToIndustries);

  py::enum_<Industry>(m, "Industry", py::arithmetic())
    .value("Invalid", Industry::Invalid)
    .value("EnergyEquipmentAndServices", Industry::EnergyEquipmentAndServices)
    .value("OilGasAndConsumeableFules", Industry::OilGasAndConsumeableFules)
    .value("Chemicals", Industry::Chemicals)
    .value("ConstructionMaterials", Industry::ConstructionMaterials)
    .value("ContainersAndPackaging", Industry::ContainersAndPackaging)
    .value("MetalsAndMining", Industry::MetalsAndMining)
    .value("PaperAndForestProducts", Industry::PaperAndForestProducts)
    .value("AerospaceAndDefense", Industry::AerospaceAndDefense)
    .value("BuildingProducts", Industry::BuildingProducts)
    .value("ConstructionAndEngineering", Industry::ConstructionAndEngineering)
    .value("ElectricalEquipment", Industry::ElectricalEquipment)
    .value("IndustrialConglomerates", Industry::IndustrialConglomerates)
    .value("Machinery", Industry::Machinery)
    .value("TradingCompaniesAndDistributors", Industry::TradingCompaniesAndDistributors)
    .value("CommercialServicesAndSupplies", Industry::CommercialServicesAndSupplies)
    .value("ProfessionalServices", Industry::ProfessionalServices)
    .value("AirFreightAndLogistics", Industry::AirFreightAndLogistics)
    .value("PassengerAirlines", Industry::PassengerAirlines)
    .value("MarineTransportation", Industry::MarineTransportation)
    .value("GroundTransportation", Industry::GroundTransportation)
    .value("TransportationInfrastructure", Industry::TransportationInfrastructure)
    .value("AutomobileComponents", Industry::AutomobileComponents)
    .value("Automobiles", Industry::Automobiles)
    .value("HouseholdDurables", Industry::HouseholdDurables)
    .value("LeisureProducts", Industry::LeisureProducts)
    .value("TextilesApparelAndLuxuryGoods", Industry::TextilesApparelAndLuxuryGoods)
    .value("HotelsRestaurantsAndLeisure", Industry::HotelsRestaurantsAndLeisure)
    .value("DiversifiedConsumerServices", Industry::DiversifiedConsumerServices)
    .value("Distributors", Industry::Distributors)
    .value("BroadlineRetail", Industry::BroadlineRetail)
    .value("SpecialtyRetail", Industry::SpecialtyRetail)
    .value("ConsumerStaplesDistributionAndRetail", Industry::ConsumerStaplesDistributionAndRetail)
    .value("Beverages", Industry::Beverages)
    .value("FoodProducts", Industry::FoodProducts)
    .value("Tobacco", Industry::Tobacco)
    .value("HouseholdProducts", Industry::HouseholdProducts)
    .value("PersonalCareProducts", Industry::PersonalCareProducts)
    .value("HealthCareEquipmentAndSupplies", Industry::HealthCareEquipmentAndSupplies)
    .value("HealthCareProvidersAndServices", Industry::HealthCareProvidersAndServices)
    .value("HealthCareTechnology", Industry::HealthCareTechnology)
    .value("Biotechnology", Industry::Biotechnology)
    .value("Pharmaceuticals", Industry::Pharmaceuticals)
    .value("LifeSciencesToolsAndServices", Industry::LifeSciencesToolsAndServices)
    .value("Banks", Industry::Banks)
    .value("FinancialServices", Industry::FinancialServices)
    .value("ConsumerFinance", Industry::ConsumerFinance)
    .value("CapitalMarkets", Industry::CapitalMarkets)
    .value("MortgageRealEstateInvestmentTrusts", Industry::MortgageRealEstateInvestmentTrusts)
    .value("Insurance", Industry::Insurance)
    .value("ITServices", Industry::ITServices)
    .value("Software", Industry::Software)
    .value("CommunicationsEquipment", Industry::CommunicationsEquipment)
    .value("TechnologyHardwareStorageAndPeripherals", Industry::TechnologyHardwareStorageAndPeripherals)
    .value("ElectronicEquipmentInstrumentsAndComponents", Industry::ElectronicEquipmentInstrumentsAndComponents)
    .value("SemiconductorsAndSemiconductorEquipment", Industry::SemiconductorsAndSemiconductorEquipment)
    .value("DiversifiedTelecommunicationServices", Industry::DiversifiedTelecommunicationServices)
    .value("WirelessTelecommunicationServices", Industry::WirelessTelecommunicationServices)
    .value("Media", Industry::Media)
    .value("Entertainment", Industry::Entertainment)
    .value("InteractiveMediaAndServices", Industry::InteractiveMediaAndServices)
    .value("ElectricUtilities", Industry::ElectricUtilities)
    .value("GasUtilities", Industry::GasUtilities)
    .value("MultiUtilities", Industry::MultiUtilities)
    .value("WaterUtilities", Industry::WaterUtilities)
    .value(
      "IndependentPowerAndRenewableElectricityProducers", Industry::IndependentPowerAndRenewableElectricityProducers
    )
    .value("DiversifiedREITs", Industry::DiversifiedREITs)
    .value("IndustrialREITs", Industry::IndustrialREITs)
    .value("HotelAndResortREITs", Industry::HotelAndResortREITs)
    .value("OfficeREITs", Industry::OfficeREITs)
    .value("HealthCareREITs", Industry::HealthCareREITs)
    .value("ResidentialREITs", Industry::ResidentialREITs)
    .value("RetailREITs", Industry::RetailREITs)
    .value("SpecializedREITs", Industry::SpecializedREITs)
    .value("RealEstateManagementAndDevelopment", Industry::RealEstateManagementAndDevelopment)
    .def("__str__", &IndustryToString, py::prepend())
    .def("__repr__", &IndustryToString, py::prepend())
    .def(py::init(&IndustryFromString))
    .def("industry_group", &IndustryToIndustryGroup)
    .def("subindustries", &IndustryToSubIndustries);

  // Subindustry in long enums

  // Security
  py::enum_<SecurityType>(m, "SecurityType", py::arithmetic())
    .value("Invalid", SecurityType::Invalid)
    .value("Equity", SecurityType::Equity)
    .value("Option", SecurityType::Option)
    .value("Bond", SecurityType::Bond)
    .value("Forward", SecurityType::Forward)
    .value("Future", SecurityType::Future)
    .value("PerpetualFuture", SecurityType::PerpetualFuture)
    .value("Spread", SecurityType::Spread)
    .value("Fund", SecurityType::Fund)
    .value("Commodity", SecurityType::Commodity)
    .value("Currency", SecurityType::Currency)
    .value("Pair", SecurityType::Pair)
    .value("Index", SecurityType::Index)
    .def("__str__", &SecurityTypeToString, py::prepend())
    .def("__repr__", &SecurityTypeToString, py::prepend())
    .def(py::init(&SecurityTypeFromString));

  // Trading
  py::enum_<TradingType>(m, "TradingType", py::arithmetic())
    .value("Invalid", TradingType::Invalid)
    .value("Live", TradingType::Live)
    .value("Simulation", TradingType::Simulation)
    .value("Sandbox", TradingType::Sandbox)
    .value("Backtest", TradingType::Backtest)
    .def("__str__", &TradingTypeToString, py::prepend())
    .def("__repr__", &TradingTypeToString, py::prepend())
    .def(py::init(&TradingTypeFromString));
  py::enum_<Side>(m, "Side", py::arithmetic())
    .value("None", Side::None)
    .value("Buy", Side::Buy)
    .value("Sell", Side::Sell)
    .def("__str__", &SideToString, py::prepend())
    .def("__repr__", &SideToString, py::prepend())
    .def(py::init(&SideFromString));
  py::enum_<OrderType>(m, "OrderType", py::arithmetic())
    .value("Invalid", OrderType::Invalid)
    .value("Limit", OrderType::Limit)
    .value("Market", OrderType::Market)
    .value("Stop", OrderType::Stop)
    .def("__str__", &OrderTypeToString, py::prepend())
    .def("__repr__", &OrderTypeToString, py::prepend())
    .def(py::init(&OrderTypeFromString));
  py::enum_<OrderFlag>(m, "OrderFlag", py::arithmetic())
    .value("None", OrderFlag::None)
    .value("FillOrKill", OrderFlag::FillOrKill)
    .value("AllOrNone", OrderFlag::AllOrNone)
    .value("ImmediateOrCancel", OrderFlag::ImmediateOrCancel)
    .def("__str__", &OrderFlagToString, py::prepend())
    .def("__repr__", &OrderFlagToString, py::prepend())
    .def(py::init(&OrderFlagFromString));
  py::enum_<TimeInForce>(m, "TimeInForce", py::arithmetic())
    .value("None", TimeInForce::None)
    .value("Day", TimeInForce::Day)
    .value("GoodTillCanceled", TimeInForce::GoodTillCanceled)
    .def("__str__", &TimeInForceToString, py::prepend())
    .def("__repr__", &TimeInForceToString, py::prepend())
    .def(py::init(&TimeInForceFromString));

// Long Enums
#include <finance-enums/python/long-enums.hpp>
  /*******************************
   * Helpers
   ******************************/
  // NONE
};
