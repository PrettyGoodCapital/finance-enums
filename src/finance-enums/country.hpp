#pragma once
#include <finance-enums/exports.hpp>

using namespace std;

namespace finance_enums {

// https://en.wikipedia.org/wiki/ISO_3166-1
extern const char* CountryStandard;

enum class LIB_EXPORT CountryCode {
  XX = 0, // INVALID
  AD = 1,
  AE = 2,
  AF = 3,
  AG = 4,
  AI = 5,
  AL = 6,
  AM = 7,
  AO = 8,
  AQ = 9,
  AR = 10,
  AS = 11,
  AT = 12,
  AU = 13,
  AW = 14,
  AX = 15,
  AZ = 16,
  BA = 17,
  BB = 18,
  BD = 19,
  BE = 20,
  BF = 21,
  BG = 22,
  BH = 23,
  BI = 24,
  BJ = 25,
  BL = 26,
  BM = 27,
  BN = 28,
  BO = 29,
  BQ = 30,
  BR = 31,
  BS = 32,
  BT = 33,
  BV = 34,
  BW = 35,
  BY = 36,
  BZ = 37,
  CA = 38,
  CC = 39,
  CD = 40,
  CF = 41,
  CG = 42,
  CH = 43,
  CI = 44,
  CK = 45,
  CL = 46,
  CM = 47,
  CN = 48,
  CO = 49,
  CR = 50,
  CU = 51,
  CV = 52,
  CW = 53,
  CX = 54,
  CY = 55,
  CZ = 56,
  DE = 57,
  DJ = 58,
  DK = 59,
  DM = 60,
  DO = 61,
  DZ = 62,
  EC = 63,
  EE = 64,
  EG = 65,
  EH = 66,
  ER = 67,
  ES = 68,
  ET = 69,
  FI = 70,
  FJ = 71,
  FK = 72,
  FM = 73,
  FO = 74,
  FR = 75,
  GA = 76,
  GB = 77,
  GD = 78,
  GE = 79,
  GF = 80,
  GG = 81,
  GH = 82,
  GI = 83,
  GL = 84,
  GM = 85,
  GN = 86,
  GP = 87,
  GQ = 88,
  GR = 89,
  GS = 90,
  GT = 91,
  GU = 92,
  GW = 93,
  GY = 94,
  HK = 95,
  HM = 96,
  HN = 97,
  HR = 98,
  HT = 99,
  HU = 100,
  ID = 101,
  IE = 102,
  IL = 103,
  IM = 104,
  IN = 105,
  IO = 106,
  IQ = 107,
  IR = 108,
  IS = 109,
  IT = 110,
  JE = 111,
  JM = 112,
  JO = 113,
  JP = 114,
  KE = 115,
  KG = 116,
  KH = 117,
  KI = 118,
  KM = 119,
  KN = 120,
  KP = 121,
  KR = 122,
  KW = 123,
  KY = 124,
  KZ = 125,
  LA = 126,
  LB = 127,
  LC = 128,
  LI = 129,
  LK = 130,
  LR = 131,
  LS = 132,
  LT = 133,
  LU = 134,
  LV = 135,
  LY = 136,
  MA = 137,
  MC = 138,
  MD = 139,
  ME = 140,
  MF = 141,
  MG = 142,
  MH = 143,
  MK = 144,
  ML = 145,
  MM = 146,
  MN = 147,
  MO = 148,
  MP = 149,
  MQ = 150,
  MR = 151,
  MS = 152,
  MT = 153,
  MU = 154,
  MV = 155,
  MW = 156,
  MX = 157,
  MY = 158,
  MZ = 159,
  NA = 160,
  NC = 161,
  NE = 162,
  NF = 163,
  NG = 164,
  NI = 165,
  NL = 166,
  NO = 167,
  NP = 168,
  NR = 169,
  NU = 170,
  NZ = 171,
  OM = 172,
  PA = 173,
  PE = 174,
  PF = 175,
  PG = 176,
  PH = 177,
  PK = 178,
  PL = 179,
  PM = 180,
  PN = 181,
  PR = 182,
  PS = 183,
  PT = 184,
  PW = 185,
  PY = 186,
  QA = 187,
  RE = 188,
  RO = 189,
  RS = 190,
  RU = 191,
  RW = 192,
  SA = 193,
  SB = 194,
  SC = 195,
  SD = 196,
  SE = 197,
  SG = 198,
  SH = 199,
  SI = 200,
  SJ = 201,
  SK = 202,
  SL = 203,
  SM = 204,
  SN = 205,
  SO = 206,
  SR = 207,
  SS = 208,
  ST = 209,
  SV = 210,
  SX = 211,
  SY = 212,
  SZ = 213,
  TC = 214,
  TD = 215,
  TF = 216,
  TG = 217,
  TH = 218,
  TJ = 219,
  TK = 220,
  TL = 221,
  TM = 222,
  TN = 223,
  TO = 224,
  TR = 225,
  TT = 226,
  TV = 227,
  TW = 228,
  TZ = 229,
  UA = 230,
  UG = 231,
  UM = 232,
  US = 233,
  UY = 234,
  UZ = 235,
  VA = 236,
  VC = 237,
  VE = 238,
  VG = 239,
  VI = 240,
  VN = 241,
  VU = 242,
  WF = 243,
  WS = 244,
  YE = 245,
  YT = 246,
  ZA = 247,
  ZM = 248,
  ZW = 249,
};

extern const char* CountryCodeNames[];

enum class LIB_EXPORT CountryCode3 {
  XXX = 0,
  AND = 1,
  ARE = 2,
  AFG = 3,
  ATG = 4,
  AIA = 5,
  ALB = 6,
  ARM = 7,
  AGO = 8,
  ATA = 9,
  ARG = 10,
  ASM = 11,
  AUT = 12,
  AUS = 13,
  ABW = 14,
  ALA = 15,
  AZE = 16,
  BIH = 17,
  BRB = 18,
  BGD = 19,
  BEL = 20,
  BFA = 21,
  BGR = 22,
  BHR = 23,
  BDI = 24,
  BEN = 25,
  BLM = 26,
  BMU = 27,
  BRN = 28,
  BOL = 29,
  BES = 30,
  BRA = 31,
  BHS = 32,
  BTN = 33,
  BVT = 34,
  BWA = 35,
  BLR = 36,
  BLZ = 37,
  CAN = 38,
  CCK = 39,
  COD = 40,
  CAF = 41,
  COG = 42,
  CHE = 43,
  CIV = 44,
  COK = 45,
  CHL = 46,
  CMR = 47,
  CHN = 48,
  COL = 49,
  CRI = 50,
  CUB = 51,
  CPV = 52,
  CUW = 53,
  CXR = 54,
  CYP = 55,
  CZE = 56,
  DEU = 57,
  DJI = 58,
  DNK = 59,
  DMA = 60,
  DOM = 61,
  DZA = 62,
  ECU = 63,
  EST = 64,
  EGY = 65,
  ESH = 66,
  ERI = 67,
  ESP = 68,
  ETH = 69,
  FIN = 70,
  FJI = 71,
  FLK = 72,
  FSM = 73,
  FRO = 74,
  FRA = 75,
  GAB = 76,
  GBR = 77,
  GRD = 78,
  GEO = 79,
  GUF = 80,
  GGY = 81,
  GHA = 82,
  GIB = 83,
  GRL = 84,
  GMB = 85,
  GIN = 86,
  GLP = 87,
  GNQ = 88,
  GRC = 89,
  SGS = 90,
  GTM = 91,
  GUM = 92,
  GNB = 93,
  GUY = 94,
  HKG = 95,
  HMD = 96,
  HND = 97,
  HRV = 98,
  HTI = 99,
  HUN = 100,
  IDN = 101,
  IRL = 102,
  ISR = 103,
  IMN = 104,
  IND = 105,
  IOT = 106,
  IRQ = 107,
  IRN = 108,
  ISL = 109,
  ITA = 110,
  JEY = 111,
  JAM = 112,
  JOR = 113,
  JPN = 114,
  KEN = 115,
  KGZ = 116,
  KHM = 117,
  KIR = 118,
  COM = 119,
  KNA = 120,
  PRK = 121,
  KOR = 122,
  KWT = 123,
  CYM = 124,
  KAZ = 125,
  LAO = 126,
  LBN = 127,
  LCA = 128,
  LIE = 129,
  LKA = 130,
  LBR = 131,
  LSO = 132,
  LTU = 133,
  LUX = 134,
  LVA = 135,
  LBY = 136,
  MAR = 137,
  MCO = 138,
  MDA = 139,
  MNE = 140,
  MAF = 141,
  MDG = 142,
  MHL = 143,
  MKD = 144,
  MLI = 145,
  MMR = 146,
  MNG = 147,
  MAC = 148,
  MNP = 149,
  MTQ = 150,
  MRT = 151,
  MSR = 152,
  MLT = 153,
  MUS = 154,
  MDV = 155,
  MWI = 156,
  MEX = 157,
  MYS = 158,
  MOZ = 159,
  NAM = 160,
  NCL = 161,
  NER = 162,
  NFK = 163,
  NGA = 164,
  NIC = 165,
  NLD = 166,
  NOR = 167,
  NPL = 168,
  NRU = 169,
  NIU = 170,
  NZL = 171,
  OMN = 172,
  PAN = 173,
  PER = 174,
  PYF = 175,
  PNG = 176,
  PHL = 177,
  PAK = 178,
  POL = 179,
  SPM = 180,
  PCN = 181,
  PRI = 182,
  PSE = 183,
  PRT = 184,
  PLW = 185,
  PRY = 186,
  QAT = 187,
  REU = 188,
  ROU = 189,
  SRB = 190,
  RUS = 191,
  RWA = 192,
  SAU = 193,
  SLB = 194,
  SYC = 195,
  SDN = 196,
  SWE = 197,
  SGP = 198,
  SHN = 199,
  SVN = 200,
  SJM = 201,
  SVK = 202,
  SLE = 203,
  SMR = 204,
  SEN = 205,
  SOM = 206,
  SUR = 207,
  SSD = 208,
  STP = 209,
  SLV = 210,
  SXM = 211,
  SYR = 212,
  SWZ = 213,
  TCA = 214,
  TCD = 215,
  ATF = 216,
  TGO = 217,
  THA = 218,
  TJK = 219,
  TKL = 220,
  TLS = 221,
  TKM = 222,
  TUN = 223,
  TON = 224,
  TUR = 225,
  TTO = 226,
  TUV = 227,
  TWN = 228,
  TZA = 229,
  UKR = 230,
  UGA = 231,
  UMI = 232,
  USA = 233,
  URY = 234,
  UZB = 235,
  VAT = 236,
  VCT = 237,
  VEN = 238,
  VGB = 239,
  VIR = 240,
  VNM = 241,
  VUT = 242,
  WLF = 243,
  WSM = 244,
  YEM = 245,
  MYT = 246,
  ZAF = 247,
  ZMB = 248,
  ZWE = 249,
};

extern const char* CountryCode3Names[];
extern const char* CountryFlags[];
extern const char* CountryCommonNames[];

const char* CountryCodeToString(const CountryCode);
const char* CountryCodeToName(const CountryCode);
const char* CountryCode3ToString(const CountryCode3);
const char* CountryCode3ToName(const CountryCode3);

CountryCode CountryCodeFromString(const char*);
CountryCode3 CountryCode3FromString(const char*);

const char* CountryCodeToFlag(const CountryCode);
const char* CountryCode3ToFlag(const CountryCode3);
CountryCode3 CountryCodeToCountryCode3(const CountryCode);
CountryCode CountryCode3ToCountryCode(const CountryCode3);

}

// AD,AND,Andorra,AD,AND
// AE,ARE,United Arab Emirates,AE,ARE
// AF,AFG,Afghanistan,AF,AFG
// AG,ATG,Antigua and Barbuda,AG,ATG
// AI,AIA,Anguilla,AI,AIA
// AL,ALB,Albania,AL,ALB
// AM,ARM,Armenia,AM,ARM
// AO,AGO,Angola,AO,AGO
// AQ,ATA,Antarctica,AQ,ATA
// AR,ARG,Argentina,AR,ARG
// AS,ASM,American Samoa,AS,ASM
// AT,AUT,Austria,AT,AUT
// AU,AUS,Australia,AU,AUS
// AW,ABW,Aruba,AW,ABW
// AX,ALA,Åland Islands,AX,ALA
// AZ,AZE,Azerbaijan,AZ,AZE
// BA,BIH,Bosnia and Herzegovina,BA,BIH
// BB,BRB,Barbados,BB,BRB
// BD,BGD,Bangladesh,BD,BGD
// BE,BEL,Belgium,BE,BEL
// BF,BFA,Burkina Faso,BF,BFA
// BG,BGR,Bulgaria,BG,BGR
// BH,BHR,Bahrain,BH,BHR
// BI,BDI,Burundi,BI,BDI
// BJ,BEN,Benin,BJ,BEN
// BL,BLM,Saint Barthélemy,BL,BLM
// BM,BMU,Bermuda,BM,BMU
// BN,BRN,Brunei Darussalam,BN,BRN
// BO,BOL,Bolivia,BO,BOL
// BQ,BES,Bonaire,BQ,BES
// BR,BRA,Brazil,BR,BRA
// BS,BHS,Bahamas,BS,BHS
// BT,BTN,Bhutan,BT,BTN
// BV,BVT,Bouvet Island,BV,BVT
// BW,BWA,Botswana,BW,BWA
// BY,BLR,Belarus,BY,BLR
// BZ,BLZ,Belize,BZ,BLZ
// CA,CAN,Canada,CA,CAN
// CC,CCK,Cocos (Keeling) Islands,CC,CCK
// CD,COD,Democratic Republic of the Congo,CD,COD
// CF,CAF,Central African Republic,CF,CAF
// CG,COG,Congo,CG,COG
// CH,CHE,Switzerland,CH,CHE
// CI,CIV,Côte d'Ivoire,CI,CIV
// CK,COK,Cook Islands,CK,COK
// CL,CHL,Chile,CL,CHL
// CM,CMR,Cameroon,CM,CMR
// CN,CHN,China,CN,CHN
// CO,COL,Colombia,CO,COL
// CR,CRI,Costa Rica,CR,CRI
// CU,CUB,Cuba,CU,CUB
// CV,CPV,Cabo Verde,CV,CPV
// CW,CUW,Curaçao,CW,CUW
// CX,CXR,Christmas Island,CX,CXR
// CY,CYP,Cyprus,CY,CYP
// CZ,CZE,Czechia,CZ,CZE
// DE,DEU,Germany,DE,DEU
// DJ,DJI,Djibouti,DJ,DJI
// DK,DNK,Denmark,DK,DNK
// DM,DMA,Dominica,DM,DMA
// DO,DOM,Dominican Republic,DO,DOM
// DZ,DZA,Algeria,DZ,DZA
// EC,ECU,Ecuador,EC,ECU
// EE,EST,Estonia,EE,EST
// EG,EGY,Egypt,EG,EGY
// EH,ESH,Western Sahara,EH,ESH
// ER,ERI,Eritrea,ER,ERI
// ES,ESP,Spain,ES,ESP
// ET,ETH,Ethiopia,ET,ETH
// FI,FIN,Finland,FI,FIN
// FJ,FJI,Fiji,FJ,FJI
// FK,FLK,Falkland Islands,FK,FLK
// FM,FSM,Micronesia,FM,FSM
// FO,FRO,Faroe Islands,FO,FRO
// FR,FRA,France,FR,FRA
// GA,GAB,Gabon,GA,GAB
// GB,GBR,United Kingdom of Great Britain and Northern Ireland,GB,GBR
// GD,GRD,Grenada,GD,GRD
// GE,GEO,Georgia,GE,GEO
// GF,GUF,French Guiana,GF,GUF
// GG,GGY,Guernsey,GG,GGY
// GH,GHA,Ghana,GH,GHA
// GI,GIB,Gibraltar,GI,GIB
// GL,GRL,Greenland,GL,GRL
// GM,GMB,Gambia,GM,GMB
// GN,GIN,Guinea,GN,GIN
// GP,GLP,Guadeloupe,GP,GLP
// GQ,GNQ,Equatorial Guinea,GQ,GNQ
// GR,GRC,Greece,GR,GRC
// GS,SGS,South Georgia and the South Sandwich Islands,GS,SGS
// GT,GTM,Guatemala,GT,GTM
// GU,GUM,Guam,GU,GUM
// GW,GNB,Guinea-Bissau,GW,GNB
// GY,GUY,Guyana,GY,GUY
// HK,HKG,Hong Kong,HK,HKG
// HM,HMD,Heard Island and McDonald Islands,HM,HMD
// HN,HND,Honduras,HN,HND
// HR,HRV,Croatia,HR,HRV
// HT,HTI,Haiti,HT,HTI
// HU,HUN,Hungary,HU,HUN
// ID,IDN,Indonesia,ID,IDN
// IE,IRL,Ireland,IE,IRL
// IL,ISR,Israel,IL,ISR
// IM,IMN,Isle of Man,IM,IMN
// IN,IND,India,IN,IND
// IO,IOT,British Indian Ocean Territory,IO,IOT
// IQ,IRQ,Iraq,IQ,IRQ
// IR,IRN,Iran,IR,IRN
// IS,ISL,Iceland,IS,ISL
// IT,ITA,Italy,IT,ITA
// JE,JEY,Jersey,JE,JEY
// JM,JAM,Jamaica,JM,JAM
// JO,JOR,Jordan,JO,JOR
// JP,JPN,Japan,JP,JPN
// KE,KEN,Kenya,KE,KEN
// KG,KGZ,Kyrgyzstan,KG,KGZ
// KH,KHM,Cambodia,KH,KHM
// KI,KIR,Kiribati,KI,KIR
// KM,COM,Comoros,KM,COM
// KN,KNA,Saint Kitts and Nevis,KN,KNA
// KP,PRK,North Korea,KP,PRK
// KR,KOR,South Korea,KR,KOR
// KW,KWT,Kuwait,KW,KWT
// KY,CYM,Cayman Islands,KY,CYM
// KZ,KAZ,Kazakhstan,KZ,KAZ
// LA,LAO,Laos,LA,LAO
// LB,LBN,Lebanon,LB,LBN
// LC,LCA,Saint Lucia,LC,LCA
// LI,LIE,Liechtenstein,LI,LIE
// LK,LKA,Sri Lanka,LK,LKA
// LR,LBR,Liberia,LR,LBR
// LS,LSO,Lesotho,LS,LSO
// LT,LTU,Lithuania,LT,LTU
// LU,LUX,Luxembourg,LU,LUX
// LV,LVA,Latvia,LV,LVA
// LY,LBY,Libya,LY,LBY
// MA,MAR,Morocco,MA,MAR
// MC,MCO,Monaco,MC,MCO
// MD,MDA,Moldova,MD,MDA
// ME,MNE,Montenegro,ME,MNE
// MF,MAF,Saint Martin,MF,MAF
// MG,MDG,Madagascar,MG,MDG
// MH,MHL,Marshall Islands,MH,MHL
// MK,MKD,North Macedonia,MK,MKD
// ML,MLI,Mali,ML,MLI
// MM,MMR,Myanmar,MM,MMR
// MN,MNG,Mongolia,MN,MNG
// MO,MAC,Macao,MO,MAC
// MP,MNP,Northern Mariana Islands,MP,MNP
// MQ,MTQ,Martinique,MQ,MTQ
// MR,MRT,Mauritania,MR,MRT
// MS,MSR,Montserrat,MS,MSR
// MT,MLT,Malta,MT,MLT
// MU,MUS,Mauritius,MU,MUS
// MV,MDV,Maldives,MV,MDV
// MW,MWI,Malawi,MW,MWI
// MX,MEX,Mexico,MX,MEX
// MY,MYS,Malaysia,MY,MYS
// MZ,MOZ,Mozambique,MZ,MOZ
// NA,NAM,Namibia,NA,NAM
// NC,NCL,New Caledonia,NC,NCL
// NE,NER,Niger,NE,NER
// NF,NFK,Norfolk Island,NF,NFK
// NG,NGA,Nigeria,NG,NGA
// NI,NIC,Nicaragua,NI,NIC
// NL,NLD,Netherlands,NL,NLD
// NO,NOR,Norway,NO,NOR
// NP,NPL,Nepal,NP,NPL
// NR,NRU,Nauru,NR,NRU
// NU,NIU,Niue,NU,NIU
// NZ,NZL,New Zealand,NZ,NZL
// OM,OMN,Oman,OM,OMN
// PA,PAN,Panama,PA,PAN
// PE,PER,Peru,PE,PER
// PF,PYF,French Polynesia,PF,PYF
// PG,PNG,Papua New Guinea,PG,PNG
// PH,PHL,Philippines,PH,PHL
// PK,PAK,Pakistan,PK,PAK
// PL,POL,Poland,PL,POL
// PM,SPM,Saint Pierre and Miquelon,PM,SPM
// PN,PCN,Pitcairn,PN,PCN
// PR,PRI,Puerto Rico,PR,PRI
// PS,PSE,Palestine,PS,PSE
// PT,PRT,Portugal,PT,PRT
// PW,PLW,Palau,PW,PLW
// PY,PRY,Paraguay,PY,PRY
// QA,QAT,Qatar,QA,QAT
// RE,REU,Réunion,RE,REU
// RO,ROU,Romania,RO,ROU
// RS,SRB,Serbia,RS,SRB
// RU,RUS,Russian Federation,RU,RUS
// RW,RWA,Rwanda,RW,RWA
// SA,SAU,Saudi Arabia,SA,SAU
// SB,SLB,Solomon Islands,SB,SLB
// SC,SYC,Seychelles,SC,SYC
// SD,SDN,Sudan,SD,SDN
// SE,SWE,Sweden,SE,SWE
// SG,SGP,Singapore,SG,SGP
// SH,SHN,Saint Helena, Ascension and Tristan da Cunha,SH,SHN
// SI,SVN,Slovenia,SI,SVN
// SJ,SJM,Svalbard and Jan Mayen,SJ,SJM
// SK,SVK,Slovakia,SK,SVK
// SL,SLE,Sierra Leone,SL,SLE
// SM,SMR,San Marino,SM,SMR
// SN,SEN,Senegal,SN,SEN
// SO,SOM,Somalia,SO,SOM
// SR,SUR,Suriname,SR,SUR
// SS,SSD,South Sudan,SS,SSD
// ST,STP,Sao Tome and Principe,ST,STP
// SV,SLV,El Salvador,SV,SLV
// SX,SXM,Sint Maarten,SX,SXM
// SY,SYR,Syrian Arab Republic,SY,SYR
// SZ,SWZ,Eswatini,SZ,SWZ
// TC,TCA,Turks and Caicos Islands,TC,TCA
// TD,TCD,Chad,TD,TCD
// TF,ATF,French Southern Territories,TF,ATF
// TG,TGO,Togo,TG,TGO
// TH,THA,Thailand,TH,THA
// TJ,TJK,Tajikistan,TJ,TJK
// TK,TKL,Tokelau,TK,TKL
// TL,TLS,Timor-Leste,TL,TLS
// TM,TKM,Turkmenistan,TM,TKM
// TN,TUN,Tunisia,TN,TUN
// TO,TON,Tonga,TO,TON
// TR,TUR,Türkiye,TR,TUR
// TT,TTO,Trinidad and Tobago,TT,TTO
// TV,TUV,Tuvalu,TV,TUV
// TW,TWN,Taiwan,TW,TWN
// TZ,TZA,Tanzania,TZ,TZA
// UA,UKR,Ukraine,UA,UKR
// UG,UGA,Uganda,UG,UGA
// UM,UMI,United States Minor Outlying Islands,UM,UMI
// US,USA,United States of America,US,USA
// UY,URY,Uruguay,UY,URY
// UZ,UZB,Uzbekistan,UZ,UZB
// VA,VAT,Vatican City,VA,VAT
// VC,VCT,Saint Vincent and the Grenadines,VC,VCT
// VE,VEN,Venezuela,VE,VEN
// VG,VGB,British Virgin Islands,VG,VGB
// VI,VIR,U.S. Virgin Islands,VI,VIR
// VN,VNM,Viet Nam,VN,VNM
// VU,VUT,Vanuatu,VU,VUT
// WF,WLF,Wallis and Futuna,WF,WLF
// WS,WSM,Samoa,WS,WSM
// YE,YEM,Yemen,YE,YEM
// YT,MYT,Mayotte,YT,MYT
// ZA,ZAF,South Africa,ZA,ZAF
// ZM,ZMB,Zambia,ZM,ZMB
// ZW,ZWE,Zimbabwe,ZW,ZWE
