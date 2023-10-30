#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {
enum class LIB_EXPORT FundType {
  Invalid    = 0,
  ETF        = 1,
  MutualFund = 2,
  REIT       = 3,
};

extern const char* FundTypeNames[];

enum class LIB_EXPORT FundSubType {
  Invalid = 0,
  Index   = 1,
  Sector  = 2,
  Active  = 3,
  Passive = 4,
};

extern const char* FundSubTypeNames[];

enum class LIB_EXPORT MutualFundEndedness {
  Invalid = 0,
  Open    = 1,
  Close   = 2,
};

extern const char* MutualFundEndednessNames[];

const char* FundTypeToString(const FundType);
const char* FundSubTypeToString(const FundSubType);
const char* MutualFundEndednessToString(const MutualFundEndedness);

FundType FundTypeFromString(const char*);
FundSubType FundSubTypeFromString(const char*);
MutualFundEndedness MutualFundEndednessFromString(const char*);

}
