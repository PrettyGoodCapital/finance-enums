#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {

enum class LIB_EXPORT SecurityType {
  Invalid         = 0,
  Equity          = 1,
  Option          = 2,
  Bond            = 3,
  Forward         = 4,
  Future          = 5,
  PerpetualFuture = 6,
  Spread          = 7,
  Fund            = 8,
  Commodity       = 9,
  Currency        = 10,
  Pair            = 11,
  Index           = 12,
};

static const char* SecurityTypeNames[] = {
  "Invalid",         // 0
  "Equity",          // 1
  "Option",          // 2
  "Bond",            // 3
  "Forward",         // 4
  "Future",          // 5
  "PerpetualFuture", // 6
  "Spread",          // 7
  "Fund",            // 8
  "Commodity",       // 9
  "Currency",        // 10
  "Pair",            // 11
  "Index",           // 12
};

const char* SecurityTypeToString(const SecurityType);
SecurityType SecurityTypeFromString(const char*);

}
