#include <cstring>
#include <finance-enums/equity.hpp>

namespace finance_enums {

const char* EquityTypeToString(const EquityType t) { return EquityTypeNames[static_cast<int>(t)]; }

EquityType EquityTypeFromString(const char* s) {
  if(strncmp(s, "Shares", 10) == 0)
    return EquityType::Shares;
  if(strncmp(s, "PreferredShares", 10) == 0)
    return EquityType::PreferredShares;
  if(strncmp(s, "ConvertibleShares", 10) == 0)
    return EquityType::ConvertibleShares;
  if(strncmp(s, "PreferredConvertibleShares", 10) == 0)
    return EquityType::PreferredConvertibleShares;
  if(strncmp(s, "DepositoryReceipt", 10) == 0)
    return EquityType::DepositoryReceipt;
  return EquityType::Invalid;
};

const char* EquityTypeNames[] = {
  "Invalid",                    // 0
  "Shares",                     // 1
  "PreferredShares",            // 2
  "ConvertibleShares",          // 3
  "PreferredConvertibleShares", // 4
  "DepositoryReceipt",          // 5
};

}