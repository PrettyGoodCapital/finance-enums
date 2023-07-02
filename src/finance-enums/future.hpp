#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {
enum class LIB_EXPORT FutureType {
  Invalid   = 0,
  Financial = 1,
  Commodity = 2,
};

extern const char* FutureTypeNames[];

enum class LIB_EXPORT FutureDeliveryType {
  Invalid  = 0,
  Physical = 1,
  Cash     = 2,
};

extern const char* FutureDeliveryNames[];

const char* FutureTypeToString(const FutureType);
const char* FutureDeliveryTypeToString(const FutureDeliveryType);

FutureType FutureTypeFromString(const char*);
FutureDeliveryType FutureDeliveryTypeFromString(const char*);

}
