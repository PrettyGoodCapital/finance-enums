#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {

enum class LIB_EXPORT CommodityType {
  Invalid     = 0,
  Energy      = 1,
  Metals      = 2,
  Agriculture = 3,
};

extern const char* CommodityTypeNames[];

enum class LIB_EXPORT EnergyType {
  Invalid    = 0,
  Crude      = 1,
  NaturalGas = 2,
};

extern const char* EnergyTypeNames[];

enum class LIB_EXPORT MetalsType {
  Invalid   = 0,
  Gold      = 1,
  Silver    = 2,
  Copper    = 3,
  Platinum  = 4,
  Palladium = 5,
};

extern const char* MetalsTypeNames[];

enum class LIB_EXPORT AgricultureType {
  Invalid     = 0,
  Corn        = 1,
  Wheat       = 2,
  Oats        = 3,
  Soybean     = 4,
  Cocoa       = 5,
  Coffee      = 6,
  Sugar       = 7,
  Cotten      = 8,
  OrangeJuice = 9,
  Cattle      = 10,
  Hogs        = 11,
};

extern const char* AgricultureTypeNames[];

const char* CommodityTypeToString(const CommodityType);
const char* EnergyTypeToString(const EnergyType);
const char* MetalsTypeToString(const MetalsType);
const char* AgricultureTypeToString(const AgricultureType);

CommodityType CommodityTypeFromString(const char*);
EnergyType EnergyTypeFromString(const char*);
MetalsType MetalsTypeFromString(const char*);
AgricultureType AgricultureTypeFromString(const char*);

}
