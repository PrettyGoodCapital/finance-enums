#pragma once
#include <finance-enums/finance-enums.hpp>
#include "rust/cxx.h"

namespace finance_enums {

CountryCode CountryCodeFromString_rust(rust::String st);
rust::String CountryCodeToString_rust(CountryCode cc);
rust::String CountryCodeToName_rust(CountryCode cc);

}