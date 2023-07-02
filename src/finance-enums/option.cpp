#include <cstring>
#include <finance-enums/option.hpp>

namespace finance_enums {

const char* OptionTypeToString(const OptionType t) { return OptionTypeNames[static_cast<int>(t)]; }
const char* OptionExerciseTypeToString(const OptionExerciseType t) {
  return OptionExerciseTypeNames[static_cast<int>(t)];
}

OptionType OptionTypeFromString(const char* s) {
  if(strncmp(s, "Call", 4) == 0)
    return OptionType::Call;
  if(strncmp(s, "Put", 4) == 0)
    return OptionType::Put;
  return OptionType::Invalid;
}

OptionExerciseType OptionExerciseTypeFromString(const char* s) {
  if(strncmp(s, "American", 8) == 0)
    return OptionExerciseType::American;
  if(strncmp(s, "European", 8) == 0)
    return OptionExerciseType::European;
  if(strncmp(s, "Bermudan", 8) == 0)
    return OptionExerciseType::Bermudan;
  return OptionExerciseType::Invalid;
}

const char* OptionTypeNames[] = {
  "Invalid", // 0,
  "Call",    // 1,
  "Put",     // 2,
};

const char* OptionExerciseTypeNames[] = {
  "Invalid",  // 0,
  "American", // 1
  "European", // 2
  "Bermudan", // 3
};

}
