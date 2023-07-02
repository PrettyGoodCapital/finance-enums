#include <cstring>
#include <finance-enums/security.hpp>

namespace finance_enums {

const char* SecurityTypeToString(const SecurityType t) { return SecurityTypeNames[static_cast<int>(t)]; }

SecurityType SecurityTypeFromString(const char* s) {
  if(strncmp(s, "Equity", 10) == 0)
    return SecurityType::Equity;
  if(strncmp(s, "Option", 10) == 0)
    return SecurityType::Option;
  if(strncmp(s, "Bond", 10) == 0)
    return SecurityType::Bond;
  if(strncmp(s, "Forward", 10) == 0)
    return SecurityType::Forward;
  if(strncmp(s, "Future", 10) == 0)
    return SecurityType::Future;
  if(strncmp(s, "PerpetualFuture", 10) == 0)
    return SecurityType::PerpetualFuture;
  if(strncmp(s, "Spread", 10) == 0)
    return SecurityType::Spread;
  if(strncmp(s, "Fund", 10) == 0)
    return SecurityType::Fund;
  if(strncmp(s, "Commodity", 10) == 0)
    return SecurityType::Commodity;
  if(strncmp(s, "Currency", 10) == 0)
    return SecurityType::Currency;
  if(strncmp(s, "Pair", 10) == 0)
    return SecurityType::Pair;
  if(strncmp(s, "Index", 10) == 0)
    return SecurityType::Index;
  return SecurityType::Invalid;
}

}