#include <cstring>
#include <finance-enums/future.hpp>

namespace finance_enums {

const char* FutureTypeToString(const FutureType t) { return FutureTypeNames[static_cast<int>(t)]; }
const char* FutureDeliveryTypeToString(const FutureDeliveryType t) { return FutureDeliveryNames[static_cast<int>(t)]; }

FutureType FutureTypeFromString(const char* s) {
  if(strncmp(s, "Financial", 9) == 0)
    return FutureType::Financial;
  if(strncmp(s, "Commodity", 9) == 0)
    return FutureType::Commodity;
  return FutureType::Invalid;
}

FutureDeliveryType FutureDeliveryTypeFromString(const char* s) {
  if(strncmp(s, "Physical", 8) == 0)
    return FutureDeliveryType::Physical;
  if(strncmp(s, "Cash", 8) == 0)
    return FutureDeliveryType::Cash;
  return FutureDeliveryType::Invalid;
}

const char* FutureTypeNames[] = {
  "Invalid",   // 0
  "Financial", // 1
  "Commodity", // 2
};

const char* FutureDeliveryNames[] = {
  "Invalid",  // 0
  "Physical", // 1
  "Cash",     // 2
};

}
