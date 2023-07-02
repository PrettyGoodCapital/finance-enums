#include <cstring>
#include <finance-enums/bond.hpp>

namespace finance_enums {

const char* BondTypeToString(const BondType t) { return BondTypeNames[static_cast<int>(t)]; }

BondType BondTypeFromString(const char* s) {
  if(strncmp(s, "Corporate", 10) == 0)
    return BondType::Corporate;
  if(strncmp(s, "Government", 10) == 0)
    return BondType::Government;
  if(strncmp(s, "Municipal", 10) == 0)
    return BondType::Municipal;
  return BondType::Invalid;
}

}
