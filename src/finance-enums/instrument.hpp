#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {
// TODO
// https://en.wikipedia.org/wiki/ISO_10962

enum class LIB_EXPORT InstrumentType {
  Invalid = 0, // single instrument
  Spot    = 1, // single instrument
  Option  = 2, // underlying + date
  Forward = 3, // underlying + date
  Future  = 4, // underlying + date
  Right   = 5, // underlying
  Spread  = 6, // left / right legs
  Pair    = 7, // left / right legs
  Basket  = 8, // components
};

extern const char* InstrumentTypeNames[];

const char* InstrumentTypeToString(const InstrumentType);
InstrumentType InstrumentTypeFromString(const char*);

}
