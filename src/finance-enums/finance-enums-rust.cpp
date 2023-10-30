#include <string>
#include <finance-enums/finance-enums-rust.hpp>

namespace finance_enums {

CountryCode CountryCodeFromString_rust(rust::String st) { return CountryCodeFromString(std::string(st).c_str()); }

rust::String CountryCodeToString_rust(CountryCode cc) { return CountryCodeToString(cc); }

rust::String CountryCodeToName_rust(CountryCode cc) { return CountryCodeToName(cc); }

}