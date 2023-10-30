#pragma once

#include <exception>
#include <string>
#include <finance-enums/exports.hpp>

// #include <nlohmann/json.hpp>
// #include <date.h>

// using json = nlohmann::json;

namespace finance_enums {
class LIB_EXPORT FinanceEnumsCPPException : public std::exception {
private:
  std::string msg = "";

public:
  explicit FinanceEnumsCPPException(std::string msg)
    : msg(msg) {}

  const char* what() const noexcept override { return msg.c_str(); }
};
}
