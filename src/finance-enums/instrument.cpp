#include <cstring>
#include <finance-enums/instrument.hpp>

namespace finance_enums {

const char* InstrumentTypeToString(const InstrumentType t) { return InstrumentTypeNames[static_cast<int>(t)]; }

InstrumentType InstrumentTypeFromString(const char* s) {
  if(strncmp(s, "Spot", 8) == 0)
    return InstrumentType::Spot;
  if(strncmp(s, "Option", 8) == 0)
    return InstrumentType::Option;
  if(strncmp(s, "Forward", 8) == 0)
    return InstrumentType::Forward;
  if(strncmp(s, "Future", 8) == 0)
    return InstrumentType::Future;
  if(strncmp(s, "Right", 8) == 0)
    return InstrumentType::Right;
  if(strncmp(s, "Spread", 8) == 0)
    return InstrumentType::Spread;
  if(strncmp(s, "Pair", 8) == 0)
    return InstrumentType::Pair;
  if(strncmp(s, "Basket", 8) == 0)
    return InstrumentType::Basket;
  return InstrumentType::Invalid;
}

const char* InstrumentTypeNames[] = {
  "Invalid", // 0,
  "Spot",    // 1,
  "Option",  // 2,
  "Forward", // 3,
  "Future",  // 4,
  "Right",   // 5,
  "Spread",  // 6,
  "Pair",    // 7,
  "Basket",  // 8,
};

}
