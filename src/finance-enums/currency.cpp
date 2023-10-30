#include <cstring>
#include <finance-enums/currency.hpp>

namespace finance_enums {

const char* CurrencyToString(const Currency t) { return CurrencyNames[static_cast<int>(t)]; }

const char* CurrencyToName(const Currency t) { return CurrencyCommonNames[static_cast<int>(t)]; }

Currency CurrencyFromString(const char* s) {
  if(strncmp(s, "AED", 3) == 0)
    return Currency::AED;
  if(strncmp(s, "AFN", 3) == 0)
    return Currency::AFN;
  if(strncmp(s, "ALL", 3) == 0)
    return Currency::ALL;
  if(strncmp(s, "AMD", 3) == 0)
    return Currency::AMD;
  if(strncmp(s, "ANG", 3) == 0)
    return Currency::ANG;
  if(strncmp(s, "AOA", 3) == 0)
    return Currency::AOA;
  if(strncmp(s, "ARS", 3) == 0)
    return Currency::ARS;
  if(strncmp(s, "AUD", 3) == 0)
    return Currency::AUD;
  if(strncmp(s, "AWG", 3) == 0)
    return Currency::AWG;
  if(strncmp(s, "AZN", 3) == 0)
    return Currency::AZN;
  if(strncmp(s, "BAM", 3) == 0)
    return Currency::BAM;
  if(strncmp(s, "BBD", 3) == 0)
    return Currency::BBD;
  if(strncmp(s, "BDT", 3) == 0)
    return Currency::BDT;
  if(strncmp(s, "BGN", 3) == 0)
    return Currency::BGN;
  if(strncmp(s, "BHD", 3) == 0)
    return Currency::BHD;
  if(strncmp(s, "BIF", 3) == 0)
    return Currency::BIF;
  if(strncmp(s, "BMD", 3) == 0)
    return Currency::BMD;
  if(strncmp(s, "BND", 3) == 0)
    return Currency::BND;
  if(strncmp(s, "BOB", 3) == 0)
    return Currency::BOB;
  if(strncmp(s, "BOV", 3) == 0)
    return Currency::BOV;
  if(strncmp(s, "BRL", 3) == 0)
    return Currency::BRL;
  if(strncmp(s, "BSD", 3) == 0)
    return Currency::BSD;
  if(strncmp(s, "BTN", 3) == 0)
    return Currency::BTN;
  if(strncmp(s, "BWP", 3) == 0)
    return Currency::BWP;
  if(strncmp(s, "BYN", 3) == 0)
    return Currency::BYN;
  if(strncmp(s, "BZD", 3) == 0)
    return Currency::BZD;
  if(strncmp(s, "CAD", 3) == 0)
    return Currency::CAD;
  if(strncmp(s, "CDF", 3) == 0)
    return Currency::CDF;
  if(strncmp(s, "CHE", 3) == 0)
    return Currency::CHE;
  if(strncmp(s, "CHF", 3) == 0)
    return Currency::CHF;
  if(strncmp(s, "CHW", 3) == 0)
    return Currency::CHW;
  if(strncmp(s, "CLF", 3) == 0)
    return Currency::CLF;
  if(strncmp(s, "CLP", 3) == 0)
    return Currency::CLP;
  if(strncmp(s, "CNY", 3) == 0)
    return Currency::CNY;
  if(strncmp(s, "COP", 3) == 0)
    return Currency::COP;
  if(strncmp(s, "COU", 3) == 0)
    return Currency::COU;
  if(strncmp(s, "CRC", 3) == 0)
    return Currency::CRC;
  if(strncmp(s, "CUC", 3) == 0)
    return Currency::CUC;
  if(strncmp(s, "CUP", 3) == 0)
    return Currency::CUP;
  if(strncmp(s, "CVE", 3) == 0)
    return Currency::CVE;
  if(strncmp(s, "CZK", 3) == 0)
    return Currency::CZK;
  if(strncmp(s, "DJF", 3) == 0)
    return Currency::DJF;
  if(strncmp(s, "DKK", 3) == 0)
    return Currency::DKK;
  if(strncmp(s, "DOP", 3) == 0)
    return Currency::DOP;
  if(strncmp(s, "DZD", 3) == 0)
    return Currency::DZD;
  if(strncmp(s, "EGP", 3) == 0)
    return Currency::EGP;
  if(strncmp(s, "ERN", 3) == 0)
    return Currency::ERN;
  if(strncmp(s, "ETB", 3) == 0)
    return Currency::ETB;
  if(strncmp(s, "EUR", 3) == 0)
    return Currency::EUR;
  if(strncmp(s, "EUX", 3) == 0)
    return Currency::EUX;
  if(strncmp(s, "EUr", 3) == 0)
    return Currency::EUX;
  if(strncmp(s, "FJD", 3) == 0)
    return Currency::FJD;
  if(strncmp(s, "FKP", 3) == 0)
    return Currency::FKP;
  if(strncmp(s, "GBP", 3) == 0)
    return Currency::GBP;
  if(strncmp(s, "GBX", 3) == 0)
    return Currency::GBX;
  if(strncmp(s, "GBp", 3) == 0)
    return Currency::GBX;
  if(strncmp(s, "GEL", 3) == 0)
    return Currency::GEL;
  if(strncmp(s, "GHS", 3) == 0)
    return Currency::GHS;
  if(strncmp(s, "GIP", 3) == 0)
    return Currency::GIP;
  if(strncmp(s, "GMD", 3) == 0)
    return Currency::GMD;
  if(strncmp(s, "GNF", 3) == 0)
    return Currency::GNF;
  if(strncmp(s, "GTQ", 3) == 0)
    return Currency::GTQ;
  if(strncmp(s, "GYD", 3) == 0)
    return Currency::GYD;
  if(strncmp(s, "HKD", 3) == 0)
    return Currency::HKD;
  if(strncmp(s, "HNL", 3) == 0)
    return Currency::HNL;
  if(strncmp(s, "HTG", 3) == 0)
    return Currency::HTG;
  if(strncmp(s, "HUF", 3) == 0)
    return Currency::HUF;
  if(strncmp(s, "IDR", 3) == 0)
    return Currency::IDR;
  if(strncmp(s, "ILS", 3) == 0)
    return Currency::ILS;
  if(strncmp(s, "INR", 3) == 0)
    return Currency::INR;
  if(strncmp(s, "IQD", 3) == 0)
    return Currency::IQD;
  if(strncmp(s, "IRR", 3) == 0)
    return Currency::IRR;
  if(strncmp(s, "ISK", 3) == 0)
    return Currency::ISK;
  if(strncmp(s, "JMD", 3) == 0)
    return Currency::JMD;
  if(strncmp(s, "JOD", 3) == 0)
    return Currency::JOD;
  if(strncmp(s, "JPY", 3) == 0)
    return Currency::JPY;
  if(strncmp(s, "KES", 3) == 0)
    return Currency::KES;
  if(strncmp(s, "KGS", 3) == 0)
    return Currency::KGS;
  if(strncmp(s, "KHR", 3) == 0)
    return Currency::KHR;
  if(strncmp(s, "KMF", 3) == 0)
    return Currency::KMF;
  if(strncmp(s, "KPW", 3) == 0)
    return Currency::KPW;
  if(strncmp(s, "KRW", 3) == 0)
    return Currency::KRW;
  if(strncmp(s, "KWD", 3) == 0)
    return Currency::KWD;
  if(strncmp(s, "KYD", 3) == 0)
    return Currency::KYD;
  if(strncmp(s, "KZT", 3) == 0)
    return Currency::KZT;
  if(strncmp(s, "LAK", 3) == 0)
    return Currency::LAK;
  if(strncmp(s, "LBP", 3) == 0)
    return Currency::LBP;
  if(strncmp(s, "LKR", 3) == 0)
    return Currency::LKR;
  if(strncmp(s, "LRD", 3) == 0)
    return Currency::LRD;
  if(strncmp(s, "LSL", 3) == 0)
    return Currency::LSL;
  if(strncmp(s, "LYD", 3) == 0)
    return Currency::LYD;
  if(strncmp(s, "MAD", 3) == 0)
    return Currency::MAD;
  if(strncmp(s, "MDL", 3) == 0)
    return Currency::MDL;
  if(strncmp(s, "MGA", 3) == 0)
    return Currency::MGA;
  if(strncmp(s, "MKD", 3) == 0)
    return Currency::MKD;
  if(strncmp(s, "MMK", 3) == 0)
    return Currency::MMK;
  if(strncmp(s, "MNT", 3) == 0)
    return Currency::MNT;
  if(strncmp(s, "MOP", 3) == 0)
    return Currency::MOP;
  if(strncmp(s, "MRU", 3) == 0)
    return Currency::MRU;
  if(strncmp(s, "MUR", 3) == 0)
    return Currency::MUR;
  if(strncmp(s, "MVR", 3) == 0)
    return Currency::MVR;
  if(strncmp(s, "MWK", 3) == 0)
    return Currency::MWK;
  if(strncmp(s, "MXN", 3) == 0)
    return Currency::MXN;
  if(strncmp(s, "MXV", 3) == 0)
    return Currency::MXV;
  if(strncmp(s, "MYR", 3) == 0)
    return Currency::MYR;
  if(strncmp(s, "MZN", 3) == 0)
    return Currency::MZN;
  if(strncmp(s, "NAD", 3) == 0)
    return Currency::NAD;
  if(strncmp(s, "NGN", 3) == 0)
    return Currency::NGN;
  if(strncmp(s, "NIO", 3) == 0)
    return Currency::NIO;
  if(strncmp(s, "NOK", 3) == 0)
    return Currency::NOK;
  if(strncmp(s, "NPR", 3) == 0)
    return Currency::NPR;
  if(strncmp(s, "NZD", 3) == 0)
    return Currency::NZD;
  if(strncmp(s, "OMR", 3) == 0)
    return Currency::OMR;
  if(strncmp(s, "PAB", 3) == 0)
    return Currency::PAB;
  if(strncmp(s, "PEN", 3) == 0)
    return Currency::PEN;
  if(strncmp(s, "PGK", 3) == 0)
    return Currency::PGK;
  if(strncmp(s, "PHP", 3) == 0)
    return Currency::PHP;
  if(strncmp(s, "PKR", 3) == 0)
    return Currency::PKR;
  if(strncmp(s, "PLN", 3) == 0)
    return Currency::PLN;
  if(strncmp(s, "PYG", 3) == 0)
    return Currency::PYG;
  if(strncmp(s, "QAR", 3) == 0)
    return Currency::QAR;
  if(strncmp(s, "RON", 3) == 0)
    return Currency::RON;
  if(strncmp(s, "RSD", 3) == 0)
    return Currency::RSD;
  if(strncmp(s, "RUB", 3) == 0)
    return Currency::RUB;
  if(strncmp(s, "RWF", 3) == 0)
    return Currency::RWF;
  if(strncmp(s, "SAR", 3) == 0)
    return Currency::SAR;
  if(strncmp(s, "SBD", 3) == 0)
    return Currency::SBD;
  if(strncmp(s, "SCR", 3) == 0)
    return Currency::SCR;
  if(strncmp(s, "SDG", 3) == 0)
    return Currency::SDG;
  if(strncmp(s, "SEK", 3) == 0)
    return Currency::SEK;
  if(strncmp(s, "SGD", 3) == 0)
    return Currency::SGD;
  if(strncmp(s, "SHP", 3) == 0)
    return Currency::SHP;
  if(strncmp(s, "SLE", 3) == 0)
    return Currency::SLE;
  if(strncmp(s, "SLL", 3) == 0)
    return Currency::SLL;
  if(strncmp(s, "SOS", 3) == 0)
    return Currency::SOS;
  if(strncmp(s, "SRD", 3) == 0)
    return Currency::SRD;
  if(strncmp(s, "SSP", 3) == 0)
    return Currency::SSP;
  if(strncmp(s, "STN", 3) == 0)
    return Currency::STN;
  if(strncmp(s, "SVC", 3) == 0)
    return Currency::SVC;
  if(strncmp(s, "SYP", 3) == 0)
    return Currency::SYP;
  if(strncmp(s, "SZL", 3) == 0)
    return Currency::SZL;
  if(strncmp(s, "THB", 3) == 0)
    return Currency::THB;
  if(strncmp(s, "TJS", 3) == 0)
    return Currency::TJS;
  if(strncmp(s, "TMT", 3) == 0)
    return Currency::TMT;
  if(strncmp(s, "TND", 3) == 0)
    return Currency::TND;
  if(strncmp(s, "TOP", 3) == 0)
    return Currency::TOP;
  if(strncmp(s, "TRY", 3) == 0)
    return Currency::TRY;
  if(strncmp(s, "TTD", 3) == 0)
    return Currency::TTD;
  if(strncmp(s, "TWD", 3) == 0)
    return Currency::TWD;
  if(strncmp(s, "TZS", 3) == 0)
    return Currency::TZS;
  if(strncmp(s, "UAH", 3) == 0)
    return Currency::UAH;
  if(strncmp(s, "UGX", 3) == 0)
    return Currency::UGX;
  if(strncmp(s, "USD", 3) == 0)
    return Currency::USD;
  if(strncmp(s, "USN", 3) == 0)
    return Currency::USN;
  if(strncmp(s, "USX", 3) == 0)
    return Currency::USX;
  if(strncmp(s, "USd", 3) == 0)
    return Currency::USX;
  if(strncmp(s, "UYI", 3) == 0)
    return Currency::UYI;
  if(strncmp(s, "UYU", 3) == 0)
    return Currency::UYU;
  if(strncmp(s, "UYW", 3) == 0)
    return Currency::UYW;
  if(strncmp(s, "UZS", 3) == 0)
    return Currency::UZS;
  if(strncmp(s, "VED", 3) == 0)
    return Currency::VED;
  if(strncmp(s, "VES", 3) == 0)
    return Currency::VES;
  if(strncmp(s, "VND", 3) == 0)
    return Currency::VND;
  if(strncmp(s, "VUV", 3) == 0)
    return Currency::VUV;
  if(strncmp(s, "WST", 3) == 0)
    return Currency::WST;
  if(strncmp(s, "XAF", 3) == 0)
    return Currency::XAF;
  if(strncmp(s, "XAG", 3) == 0)
    return Currency::XAG;
  if(strncmp(s, "XAU", 3) == 0)
    return Currency::XAU;
  if(strncmp(s, "XBA", 3) == 0)
    return Currency::XBA;
  if(strncmp(s, "XBB", 3) == 0)
    return Currency::XBB;
  if(strncmp(s, "XBC", 3) == 0)
    return Currency::XBC;
  if(strncmp(s, "XBD", 3) == 0)
    return Currency::XBD;
  if(strncmp(s, "XCD", 3) == 0)
    return Currency::XCD;
  if(strncmp(s, "XDR", 3) == 0)
    return Currency::XDR;
  if(strncmp(s, "XOF", 3) == 0)
    return Currency::XOF;
  if(strncmp(s, "XPD", 3) == 0)
    return Currency::XPD;
  if(strncmp(s, "XPF", 3) == 0)
    return Currency::XPF;
  if(strncmp(s, "XPT", 3) == 0)
    return Currency::XPT;
  if(strncmp(s, "XSU", 3) == 0)
    return Currency::XSU;
  if(strncmp(s, "XTS", 3) == 0)
    return Currency::XTS;
  if(strncmp(s, "XUA", 3) == 0)
    return Currency::XUA;
  if(strncmp(s, "YER", 3) == 0)
    return Currency::YER;
  if(strncmp(s, "ZAR", 3) == 0)
    return Currency::ZAR;
  if(strncmp(s, "ZMW", 3) == 0)
    return Currency::ZMW;
  if(strncmp(s, "ZWL", 3) == 0)
    return Currency::ZWL;
  return Currency::XXX;
}

}
