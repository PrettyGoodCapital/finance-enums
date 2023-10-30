#include <cstring>
#include <finance-enums/trading.hpp>

namespace finance_enums {

const char* TradingTypeToString(const TradingType t) { return TradingTypeNames[static_cast<int>(t)]; }

const char* SideToString(const Side t) { return SideNames[static_cast<int>(t)]; }

const char* OrderTypeToString(const OrderType t) { return OrderTypeNames[static_cast<int>(t)]; }

const char* OrderFlagToString(const OrderFlag t) { return OrderFlagNames[static_cast<int>(t)]; }

const char* TimeInForceToString(const TimeInForce t) { return TimeInForceNames[static_cast<int>(t)]; }

TradingType TradingTypeFromString(const char* s) {
  if(strncmp(s, "Live", 10) == 0)
    return TradingType::Live;
  if(strncmp(s, "Simulation", 10) == 0)
    return TradingType::Simulation;
  if(strncmp(s, "Sandbox", 10) == 0)
    return TradingType::Sandbox;
  if(strncmp(s, "Backtest", 10) == 0)
    return TradingType::Backtest;
  return TradingType::Invalid;
}

Side SideFromString(const char* s) {
  if(strncmp(s, "Buy", 4) == 0)
    return Side::Buy;
  if(strncmp(s, "Sell", 4) == 0)
    return Side::Sell;
  return Side::None;
}

OrderType OrderTypeFromString(const char* s) {
  if(strncmp(s, "Limit", 6) == 0)
    return OrderType::Limit;
  if(strncmp(s, "Market", 6) == 0)
    return OrderType::Market;
  if(strncmp(s, "Stop", 6) == 0)
    return OrderType::Stop;
  return OrderType::Invalid;
}

OrderFlag OrderFlagFromString(const char* s) {
  if(strncmp(s, "FillOrKill", 10) == 0)
    return OrderFlag::FillOrKill;
  if(strncmp(s, "AllOrNone", 10) == 0)
    return OrderFlag::AllOrNone;
  if(strncmp(s, "ImmediateOrCancel", 10) == 0)
    return OrderFlag::ImmediateOrCancel;
  return OrderFlag::None;
}

TimeInForce TimeInForceFromString(const char* s) {
  if(strncmp(s, "Day", 10) == 0)
    return TimeInForce::Day;
  if(strncmp(s, "GoodTillCanceled", 10) == 0)
    return TimeInForce::GoodTillCanceled;
  return TimeInForce::None;
}

}
