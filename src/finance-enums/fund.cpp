#include <cstring>
#include <finance-enums/fund.hpp>

namespace finance_enums {

const char* FundTypeToString(const FundType t) { return FundTypeNames[static_cast<int>(t)]; }
const char* FundSubTypeToString(const FundSubType t) { return FundSubTypeNames[static_cast<int>(t)]; }
const char* MutualFundEndednessToString(const MutualFundEndedness t) {
  return MutualFundEndednessNames[static_cast<int>(t)];
}

FundType FundTypeFromString(const char* s) {
  if(strncmp(s, "ETF", 5) == 0)
    return FundType::ETF;
  if(strncmp(s, "MutualFund", 5) == 0)
    return FundType::MutualFund;
  if(strncmp(s, "REIT", 5) == 0)
    return FundType::REIT;
  return FundType::Invalid;
};

FundSubType FundSubTypeFromString(const char* s) {
  if(strncmp(s, "Index", 6) == 0)
    return FundSubType::Index;
  if(strncmp(s, "Sector", 6) == 0)
    return FundSubType::Sector;
  if(strncmp(s, "Active", 6) == 0)
    return FundSubType::Active;
  if(strncmp(s, "Passive", 6) == 0)
    return FundSubType::Passive;
  return FundSubType::Invalid;
}

MutualFundEndedness MutualFundEndednessFromString(const char* s) {
  if(strncmp(s, "Open", 5) == 0)
    return MutualFundEndedness::Open;
  if(strncmp(s, "Close", 5) == 0)
    return MutualFundEndedness::Close;
  return MutualFundEndedness::Invalid;
}

const char* FundTypeNames[] = {
  "Invalid",    // 0
  "ETF",        // 1
  "MutualFund", // 2
  "REIT",       // 3
};

const char* FundSubTypeNames[] = {
  "Invalid", // 0
  "Index",   // 1
  "Sector",  // 2
  "Active",  // 3
  "Passive", // 4
};

const char* MutualFundEndednessNames[] = {
  "Invalid", // 0
  "Open",    // 1
  "Close",   // 2
};

}