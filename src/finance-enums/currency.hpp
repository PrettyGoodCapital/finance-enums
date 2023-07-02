#pragma once
#include <finance-enums/exports.hpp>

namespace finance_enums {

// https://en.wikipedia.org/wiki/ISO_4217
const char* CurrencyStandard = "ISO4217";

enum class LIB_EXPORT Currency {
  XXX = 0,
  AED = 1,
  AFN = 2,
  ALL = 3,
  AMD = 4,
  ANG = 5,
  AOA = 6,
  ARS = 7,
  AUD = 8,
  AWG = 9,
  AZN = 10,
  BAM = 11,
  BBD = 12,
  BDT = 13,
  BGN = 14,
  BHD = 15,
  BIF = 16,
  BMD = 17,
  BND = 18,
  BOB = 19,
  BOV = 20,
  BRL = 21,
  BSD = 22,
  BTN = 23,
  BWP = 24,
  BYN = 25,
  BZD = 26,
  CAD = 27,
  CDF = 28,
  CHE = 29,
  CHF = 30,
  CHW = 31,
  CLF = 32,
  CLP = 33,
  CNY = 34,
  COP = 35,
  COU = 36,
  CRC = 37,
  CUC = 38,
  CUP = 39,
  CVE = 40,
  CZK = 41,
  DJF = 42,
  DKK = 43,
  DOP = 44,
  DZD = 45,
  EGP = 46,
  ERN = 47,
  ETB = 48,
  EUR = 49,
  EUX = 50, // NOTE: non iso
  FJD = 51,
  FKP = 52,
  GBP = 53,
  GBX = 54, // NOTE: non iso
  GEL = 55,
  GHS = 56,
  GIP = 57,
  GMD = 58,
  GNF = 59,
  GTQ = 60,
  GYD = 61,
  HKD = 62,
  HNL = 63,
  HTG = 64,
  HUF = 65,
  IDR = 66,
  ILS = 67,
  INR = 68,
  IQD = 69,
  IRR = 70,
  ISK = 71,
  JMD = 72,
  JOD = 73,
  JPY = 74,
  KES = 75,
  KGS = 76,
  KHR = 77,
  KMF = 78,
  KPW = 79,
  KRW = 80,
  KWD = 81,
  KYD = 82,
  KZT = 83,
  LAK = 84,
  LBP = 85,
  LKR = 86,
  LRD = 87,
  LSL = 88,
  LYD = 89,
  MAD = 90,
  MDL = 91,
  MGA = 92,
  MKD = 93,
  MMK = 94,
  MNT = 95,
  MOP = 96,
  MRU = 97,
  MUR = 98,
  MVR = 99,
  MWK = 100,
  MXN = 101,
  MXV = 102,
  MYR = 103,
  MZN = 104,
  NAD = 105,
  NGN = 106,
  NIO = 107,
  NOK = 108,
  NPR = 109,
  NZD = 110,
  OMR = 111,
  PAB = 112,
  PEN = 113,
  PGK = 114,
  PHP = 115,
  PKR = 116,
  PLN = 117,
  PYG = 118,
  QAR = 119,
  RON = 120,
  RSD = 121,
  RUB = 122,
  RWF = 123,
  SAR = 124,
  SBD = 125,
  SCR = 126,
  SDG = 127,
  SEK = 128,
  SGD = 129,
  SHP = 130,
  SLE = 131,
  SLL = 132,
  SOS = 133,
  SRD = 134,
  SSP = 135,
  STN = 136,
  SVC = 137,
  SYP = 138,
  SZL = 139,
  THB = 140,
  TJS = 141,
  TMT = 142,
  TND = 143,
  TOP = 144,
  TRY = 145,
  TTD = 146,
  TWD = 147,
  TZS = 148,
  UAH = 149,
  UGX = 150,
  USD = 151,
  USN = 152,
  USX = 153, // NOTE: non iso
  UYI = 154,
  UYU = 155,
  UYW = 156,
  UZS = 157,
  VED = 158,
  VES = 159,
  VND = 160,
  VUV = 161,
  WST = 162,
  XAF = 163,
  XAG = 164,
  XAU = 165,
  XBA = 166,
  XBB = 167,
  XBC = 168,
  XBD = 169,
  XCD = 170,
  XDR = 171,
  XOF = 172,
  XPD = 173,
  XPF = 174,
  XPT = 175,
  XSU = 176,
  XTS = 177,
  XUA = 178,
  YER = 179,
  ZAR = 180,
  ZMW = 181,
  ZWL = 182,
};

const char* CurrencyNames[] = {
  "XXX", // 0
  "AED", // 1
  "AFN", // 2
  "ALL", // 3
  "AMD", // 4
  "ANG", // 5
  "AOA", // 6
  "ARS", // 7
  "AUD", // 8
  "AWG", // 9
  "AZN", // 10
  "BAM", // 11
  "BBD", // 12
  "BDT", // 13
  "BGN", // 14
  "BHD", // 15
  "BIF", // 16
  "BMD", // 17
  "BND", // 18
  "BOB", // 19
  "BOV", // 20
  "BRL", // 21
  "BSD", // 22
  "BTN", // 23
  "BWP", // 24
  "BYN", // 25
  "BZD", // 26
  "CAD", // 27
  "CDF", // 28
  "CHE", // 29
  "CHF", // 30
  "CHW", // 31
  "CLF", // 32
  "CLP", // 33
  "CNY", // 34
  "COP", // 35
  "COU", // 36
  "CRC", // 37
  "CUC", // 38
  "CUP", // 39
  "CVE", // 40
  "CZK", // 41
  "DJF", // 42
  "DKK", // 43
  "DOP", // 44
  "DZD", // 45
  "EGP", // 46
  "ERN", // 47
  "ETB", // 48
  "EUR", // 49
  "EUX", // 50
  "FJD", // 51
  "FKP", // 52
  "GBP", // 53
  "GBX", // 54
  "GEL", // 55
  "GHS", // 56
  "GIP", // 57
  "GMD", // 58
  "GNF", // 59
  "GTQ", // 60
  "GYD", // 61
  "HKD", // 62
  "HNL", // 63
  "HTG", // 64
  "HUF", // 65
  "IDR", // 66
  "ILS", // 67
  "INR", // 68
  "IQD", // 69
  "IRR", // 70
  "ISK", // 71
  "JMD", // 72
  "JOD", // 73
  "JPY", // 74
  "KES", // 75
  "KGS", // 76
  "KHR", // 77
  "KMF", // 78
  "KPW", // 79
  "KRW", // 80
  "KWD", // 81
  "KYD", // 82
  "KZT", // 83
  "LAK", // 84
  "LBP", // 85
  "LKR", // 86
  "LRD", // 87
  "LSL", // 88
  "LYD", // 89
  "MAD", // 90
  "MDL", // 91
  "MGA", // 92
  "MKD", // 93
  "MMK", // 94
  "MNT", // 95
  "MOP", // 96
  "MRU", // 97
  "MUR", // 98
  "MVR", // 99
  "MWK", // 100
  "MXN", // 101
  "MXV", // 102
  "MYR", // 103
  "MZN", // 104
  "NAD", // 105
  "NGN", // 106
  "NIO", // 107
  "NOK", // 108
  "NPR", // 109
  "NZD", // 110
  "OMR", // 111
  "PAB", // 112
  "PEN", // 113
  "PGK", // 114
  "PHP", // 115
  "PKR", // 116
  "PLN", // 117
  "PYG", // 118
  "QAR", // 119
  "RON", // 120
  "RSD", // 121
  "RUB", // 122
  "RWF", // 123
  "SAR", // 124
  "SBD", // 125
  "SCR", // 126
  "SDG", // 127
  "SEK", // 128
  "SGD", // 129
  "SHP", // 130
  "SLE", // 131
  "SLL", // 132
  "SOS", // 133
  "SRD", // 134
  "SSP", // 135
  "STN", // 136
  "SVC", // 137
  "SYP", // 138
  "SZL", // 139
  "THB", // 140
  "TJS", // 141
  "TMT", // 142
  "TND", // 143
  "TOP", // 144
  "TRY", // 145
  "TTD", // 146
  "TWD", // 147
  "TZS", // 148
  "UAH", // 149
  "UGX", // 150
  "USD", // 151
  "USN", // 152
  "USX", // 153
  "UYI", // 154
  "UYU", // 155
  "UYW", // 156
  "UZS", // 157
  "VED", // 158
  "VES", // 159
  "VND", // 160
  "VUV", // 161
  "WST", // 162
  "XAF", // 163
  "XAG", // 164
  "XAU", // 165
  "XBA", // 166
  "XBB", // 167
  "XBC", // 168
  "XBD", // 169
  "XCD", // 170
  "XDR", // 171
  "XOF", // 172
  "XPD", // 173
  "XPF", // 174
  "XPT", // 175
  "XSU", // 176
  "XTS", // 177
  "XUA", // 178
  "YER", // 179
  "ZAR", // 180
  "ZMW", // 181
  "ZWL", // 182
};

const char* CurrencyCommonNames[] = {
  "Invalid",                                        // XXX = 0
  "United Arab Emirates dirham",                    // AED = 1
  "Afghan afghani",                                 // AFN = 2
  "Albanian lek",                                   // ALL = 3
  "Armenian dram",                                  // AMD = 4
  "Netherlands Antillean guilder",                  // ANG = 5
  "Angolan kwanza",                                 // AOA = 6
  "Argentine peso",                                 // ARS = 7
  "Australian dollar",                              // AUD = 8
  "Aruban florin",                                  // AWG = 9
  "Azerbaijani manat",                              // AZN = 10
  "Bosnia and Herzegovina convertible mark",        // BAM = 11
  "Barbados dollar",                                // BBD = 12
  "Bangladeshi taka",                               // BDT = 13
  "Bulgarian lev",                                  // BGN = 14
  "Bahraini dinar",                                 // BHD = 15
  "Burundian franc",                                // BIF = 16
  "Bermudian dollar",                               // BMD = 17
  "Brunei dollar",                                  // BND = 18
  "Boliviano",                                      // BOB = 19
  "Bolivian Mvdol",                                 // BOV = 20
  "Brazilian real",                                 // BRL = 21
  "Bahamian dollar",                                // BSD = 22
  "Bhutanese ngultrum",                             // BTN = 23
  "Botswana pula",                                  // BWP = 24
  "Belarusian ruble",                               // BYN = 25
  "Belize dollar",                                  // BZD = 26
  "Canadian dollar",                                // CAD = 27
  "Congolese franc",                                // CDF = 28
  "WIR euro",                                       // CHE = 29
  "Swiss franc",                                    // CHF = 30
  "WIR franc",                                      // CHW = 31
  "Unidad de Fomento",                              // CLF = 32
  "Chilean peso",                                   // CLP = 33
  "Renminbi",                                       // CNY = 34
  "Colombian peso",                                 // COP = 35
  "Unidad de Valor Real (UVR)",                     // COU = 36
  "Costa Rican colon",                              // CRC = 37
  "Cuban convertible peso",                         // CUC = 38
  "Cuban peso",                                     // CUP = 39
  "Cape Verdean escudo",                            // CVE = 40
  "Czech koruna",                                   // CZK = 41
  "Djiboutian franc",                               // DJF = 42
  "Danish krone",                                   // DKK = 43
  "Dominican peso",                                 // DOP = 44
  "Algerian dinar",                                 // DZD = 45
  "Egyptian pound",                                 // EGP = 46
  "Eritrean nakfa",                                 // ERN = 47
  "Ethiopian birr",                                 // ETB = 48
  "Euro",                                           // EUR = 49
  "Euro (cents)",                                   // EUX = 50, // NOTE: non is
  "Fiji dollar",                                    // FJD = 51
  "Falkland Islands pound",                         // FKP = 52
  "Pound sterling",                                 // GBP = 53
  "Penny sterling",                                 // GBX = 54, // NOTE: non is
  "Georgian lari",                                  // GEL = 55
  "Ghanaian cedi",                                  // GHS = 56
  "Gibraltar pound",                                // GIP = 57
  "Gambian dalasi",                                 // GMD = 58
  "Guinean franc",                                  // GNF = 59
  "Guatemalan quetzal",                             // GTQ = 60
  "Guyanese dollar",                                // GYD = 61
  "Hong Kong dollar",                               // HKD = 62
  "Honduran lempira",                               // HNL = 63
  "Haitian gourde",                                 // HTG = 64
  "Hungarian forint",                               // HUF = 65
  "Indonesian rupiah",                              // IDR = 66
  "Israeli new shekel",                             // ILS = 67
  "Indian rupee",                                   // INR = 68
  "Iraqi dinar",                                    // IQD = 69
  "Iranian rial",                                   // IRR = 70
  "Icelandic króna",                                // ISK = 71
  "Jamaican dollar",                                // JMD = 72
  "Jordanian dinar",                                // JOD = 73
  "Japanese yen",                                   // JPY = 74
  "Kenyan shilling",                                // KES = 75
  "Kyrgyzstani som",                                // KGS = 76
  "Cambodian riel",                                 // KHR = 77
  "Comoro franc",                                   // KMF = 78
  "North Korean won",                               // KPW = 79
  "South Korean won",                               // KRW = 80
  "Kuwaiti dinar",                                  // KWD = 81
  "Cayman Islands dollar",                          // KYD = 82
  "Kazakhstani tenge",                              // KZT = 83
  "Lao kip",                                        // LAK = 84
  "Lebanese pound",                                 // LBP = 85
  "Sri Lankan rupee",                               // LKR = 86
  "Liberian dollar",                                // LRD = 87
  "Lesotho loti",                                   // LSL = 88
  "Libyan dinar",                                   // LYD = 89
  "Moroccan dirham",                                // MAD = 90
  "Moldovan leu",                                   // MDL = 91
  "Malagasy ariary",                                // MGA = 92
  "Macedonian denar",                               // MKD = 93
  "Myanmar kyat",                                   // MMK = 94
  "Mongolian tögrög",                               // MNT = 95
  "Macanese pataca",                                // MOP = 96
  "Mauritanian ouguiya",                            // MRU = 97
  "Mauritian rupee",                                // MUR = 98
  "Maldivian rufiyaa",                              // MVR = 99
  "Malawian kwacha",                                // MWK = 100
  "Mexican peso",                                   // MXN = 101
  "Mexican Unidad de Inversion",                    // MXV = 102
  "Malaysian ringgit",                              // MYR = 103
  "Mozambican metical",                             // MZN = 104
  "Namibian dollar",                                // NAD = 105
  "Nigerian naira",                                 // NGN = 106
  "Nicaraguan córdoba",                             // NIO = 107
  "Norwegian krone",                                // NOK = 108
  "Nepalese rupee",                                 // NPR = 109
  "New Zealand dollar",                             // NZD = 110
  "Omani rial",                                     // OMR = 111
  "Panamanian balboa",                              // PAB = 112
  "Peruvian sol",                                   // PEN = 113
  "Papua New Guinean kina",                         // PGK = 114
  "Philippine peso",                                // PHP = 115
  "Pakistani rupee",                                // PKR = 116
  "Polish złoty",                                   // PLN = 117
  "Paraguayan guaraní",                             // PYG = 118
  "Qatari riyal",                                   // QAR = 119
  "Romanian leu",                                   // RON = 120
  "Serbian dinar",                                  // RSD = 121
  "Russian ruble",                                  // RUB = 122
  "Rwandan franc",                                  // RWF = 123
  "Saudi riyal",                                    // SAR = 124
  "Solomon Islands dollar",                         // SBD = 125
  "Seychelles rupee",                               // SCR = 126
  "Sudanese pound",                                 // SDG = 127
  "Swedish krona",                                  // SEK = 128
  "Singapore dollar",                               // SGD = 129
  "Saint Helena pound",                             // SHP = 130
  "Sierra Leonean leone",                           // SLE = 131
  "Sierra Leonean leone",                           // SLL = 132
  "Somali shilling",                                // SOS = 133
  "Surinamese dollar",                              // SRD = 134
  "South Sudanese pound",                           // SSP = 135
  "São Tomé and Príncipe dobra",                    // STN = 136
  "Salvadoran colón",                               // SVC = 137
  "Syrian pound",                                   // SYP = 138
  "Swazi lilangeni",                                // SZL = 139
  "Thai baht",                                      // THB = 140
  "Tajikistani somoni",                             // TJS = 141
  "Turkmenistan manat",                             // TMT = 142
  "Tunisian dinar",                                 // TND = 143
  "Tongan paʻanga",                                 // TOP = 144
  "Turkish lira",                                   // TRY = 145
  "Trinidad and Tobago dollar",                     // TTD = 146
  "New Taiwan dollar",                              // TWD = 147
  "Tanzanian shilling",                             // TZS = 148
  "Ukrainian hryvnia",                              // UAH = 149
  "Ugandan shilling",                               // UGX = 150
  "United States dollar",                           // USD = 151
  "United States dollar",                           // USN = 152
  "United States penny",                            // USX = 153, // NOTE: non is
  "Uruguay Peso en Unidades Indexadas",             // UYI = 154
  "Uruguayan peso",                                 // UYU = 155
  "Unidad previsional",                             // UYW = 156
  "Uzbekistan sum",                                 // UZS = 157
  "Venezuelan digital bolívar",                     // VED = 158
  "Venezuelan sovereign bolívar",                   // VES = 159
  "Vietnamese đồng",                                // VND = 160
  "Vanuatu vatu",                                   // VUV = 161
  "Samoan tala",                                    // WST = 162
  "CFA franc BEAC",                                 // XAF = 163
  "Silver",                                         // XAG = 164
  "Gold",                                           // XAU = 165
  "European Composite Unit",                        // XBA = 166
  "European Monetary Unit",                         // XBB = 167
  "European Unit of Account 9",                     // XBC = 168
  "European Unit of Account 17",                    // XBD = 169
  "East Caribbean dollar",                          // XCD = 170
  "Special drawing rights",                         // XDR = 171
  "CFA franc BCEAO",                                // XOF = 172
  "Palladium",                                      // XPD = 173
  "CFP franc",                                      // XPF = 174
  "Platinum",                                       // XPT = 175
  "SUCRE Unified System for Regional Compensation", // XSU = 176
  "Code reserved for testing",                      // XTS = 177
  "ADB Unit of Account",                            // XUA = 178
  "Yemeni rial",                                    // YER = 179
  "South African rand",                             // ZAR = 180
  "Zambian kwacha",                                 // ZMW = 181
  "Zimbabwean dollar",                              // ZWL = 182
};

const char* CurrencyToString(const Currency);
const char* CurrencyToName(const Currency);
Currency CurrencyFromString(const char*);

}
