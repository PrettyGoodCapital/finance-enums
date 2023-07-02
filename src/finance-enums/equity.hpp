#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {

enum class LIB_EXPORT EquityType {
  Invalid                    = 0,
  Shares                     = 1,
  PreferredShares            = 2,
  ConvertibleShares          = 3,
  PreferredConvertibleShares = 4,
  DepositoryReceipt          = 5,
};

extern const char* EquityTypeNames[];

const char* EquityTypeToString(const EquityType);
EquityType EquityTypeFromString(const char* s);

}
