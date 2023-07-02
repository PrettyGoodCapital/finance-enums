#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {

enum class LIB_EXPORT BondType {
  Invalid    = 0,
  Corporate  = 1,
  Government = 2,
  Municipal  = 3,
};

static const char* BondTypeNames[] = {
  "Invalid",    // 0
  "Corporate",  // 1
  "Government", // 2
  "Municipal",  // 3
};

const char* BondTypeToString(const BondType);
BondType BondTypeFromString(const char*);

}
