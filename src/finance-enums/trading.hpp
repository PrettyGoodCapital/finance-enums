#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {

enum class LIB_EXPORT TradingType {
  Invalid    = 0,
  Live       = 1,
  Simulation = 2,
  Sandbox    = 3,
  Backtest   = 4,
};

static const char* TradingTypeNames[] = {
  "Invalid",    // 0
  "Live",       // 1
  "Simulation", // 2
  "Sandbox",    // 3
  "Backtest",   // 4
};

enum class LIB_EXPORT Side {
  None = 0,
  Buy  = 1,
  Sell = 2,
};

static const char* SideNames[] = {
  "None", // 0
  "Buy",  // 1
  "Sell", // 2
};

enum class LIB_EXPORT OrderType {
  Invalid = 0,
  Limit   = 1,
  Market  = 2,
  Stop    = 3,
};

static const char* OrderTypeNames[] = {
  "Invalid", // 0
  "Limit",   // 1
  "Market",  // 2
  "Stop",    // 3
};

enum class LIB_EXPORT OrderFlag {
  None              = 0,
  FillOrKill        = 1,
  AllOrNone         = 2,
  ImmediateOrCancel = 3,
};

static const char* OrderFlagNames[] = {
  "None",              // 0
  "FillOrKill",        // 1
  "AllOrNone",         // 2
  "ImmediateOrCancel", // 3
};

enum class LIB_EXPORT TimeInForce {
  None             = 0,
  Day              = 1,
  GoodTillCanceled = 2,
};

static const char* TimeInForceNames[] = {
  "None",             // 0
  "Day",              // 1
  "GoodTillCanceled", // 2
};

const char* TradingTypeToString(const TradingType);
const char* SideToString(const Side);
const char* OrderTypeToString(const OrderType);
const char* OrderFlagToString(const OrderFlag);
const char* TimeInForceToString(const TimeInForce);

TradingType TradingTypeFromString(const char*);
Side SideFromString(const char*);
OrderType OrderTypeFromString(const char*);
OrderFlag OrderFlagFromString(const char*);
TimeInForce TimeInForceFromString(const char*);

}
