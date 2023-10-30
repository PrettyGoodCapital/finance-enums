#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {
enum class LIB_EXPORT OptionType {
  Invalid = 0,
  Call    = 1,
  Put     = 2,
};

extern const char* OptionTypeNames[];

enum class LIB_EXPORT OptionExerciseType {
  Invalid  = 0,
  American = 1,
  European = 2,
  Bermudan = 3,
};

extern const char* OptionExerciseTypeNames[];

const char* OptionTypeToString(const OptionType);
const char* OptionExerciseTypeToString(const OptionExerciseType);
OptionType OptionTypeFromString(const char*);
OptionExerciseType OptionExerciseTypeFromString(const char*);

}
