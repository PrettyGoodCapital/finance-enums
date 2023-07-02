#include <cstring>
#include <finance-enums/commodity.hpp>

namespace finance_enums {

const char* CommodityTypeToString(const CommodityType t) { return CommodityTypeNames[static_cast<int>(t)]; }
const char* EnergyTypeToString(const EnergyType t) { return EnergyTypeNames[static_cast<int>(t)]; }
const char* MetalsTypeToString(const MetalsType t) { return MetalsTypeNames[static_cast<int>(t)]; }
const char* AgricultureTypeToString(const AgricultureType t) { return AgricultureTypeNames[static_cast<int>(t)]; }

CommodityType CommodityTypeFromString(const char* s) {
  if(strncmp(s, "Energy", 6) == 0)
    return CommodityType::Energy;
  if(strncmp(s, "Metals", 6) == 0)
    return CommodityType::Metals;
  if(strncmp(s, "Agriculture", 6) == 0)
    return CommodityType::Agriculture;
  return CommodityType::Invalid;
}

EnergyType EnergyTypeFromString(const char* s) {
  if(strncmp(s, "Crude", 5) == 0)
    return EnergyType::Crude;
  if(strncmp(s, "NaturalGas", 5) == 0)
    return EnergyType::NaturalGas;
  return EnergyType::Invalid;
}

MetalsType MetalsTypeFromString(const char* s) {
  if(strncmp(s, "Gold", 7) == 0)
    return MetalsType::Gold;
  if(strncmp(s, "Silver", 7) == 0)
    return MetalsType::Silver;
  if(strncmp(s, "Copper", 7) == 0)
    return MetalsType::Copper;
  if(strncmp(s, "Platinum", 7) == 0)
    return MetalsType::Platinum;
  if(strncmp(s, "Palladium", 7) == 0)
    return MetalsType::Palladium;
  return MetalsType::Invalid;
}

AgricultureType AgricultureTypeFromString(const char* s) {
  if(strncmp(s, "Corn", 8) == 0)
    return AgricultureType::Corn;
  if(strncmp(s, "Wheat", 8) == 0)
    return AgricultureType::Wheat;
  if(strncmp(s, "Oats", 8) == 0)
    return AgricultureType::Oats;
  if(strncmp(s, "Soybean", 8) == 0)
    return AgricultureType::Soybean;
  if(strncmp(s, "Cocoa", 8) == 0)
    return AgricultureType::Cocoa;
  if(strncmp(s, "Coffee", 8) == 0)
    return AgricultureType::Coffee;
  if(strncmp(s, "Sugar", 8) == 0)
    return AgricultureType::Sugar;
  if(strncmp(s, "Cotten", 8) == 0)
    return AgricultureType::Cotten;
  if(strncmp(s, "OrangeJuice", 8) == 0)
    return AgricultureType::OrangeJuice;
  if(strncmp(s, "Cattle", 8) == 0)
    return AgricultureType::Cattle;
  if(strncmp(s, "Hogs", 8) == 0)
    return AgricultureType::Hogs;
  return AgricultureType::Invalid;
}

const char* CommodityTypeNames[] = {
  "Invalid",     // 0
  "Energy",      // 1
  "Metals",      // 2
  "Agriculture", // 3
};

const char* EnergyTypeNames[] = {
  "Invalid",    // 0
  "Crude",      // 1
  "NaturalGas", // 2
};

const char* MetalsTypeNames[] = {
  "Invalid",   // 0
  "Gold",      // 1
  "Silver",    // 2
  "Copper",    // 3
  "Platinum",  // 4
  "Palladium", // 5
};

const char* AgricultureTypeNames[] = {
  "Invalid",     // 0
  "Corn",        // 1
  "Wheat",       // 2
  "Oats",        // 3
  "Soybean",     // 4
  "Cocoa",       // 5
  "Coffee",      // 6
  "Sugar",       // 7
  "Cotten",      // 8
  "OrangeJuice", // 9
  "Cattle",      // 10
  "Hogs",        // 11
};

}