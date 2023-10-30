#pragma once
#include <finance-enums/exports.hpp>
#include <finance-enums/country.hpp>

namespace finance_enums {
// https://www.iso20022.org/market-identifier-codes
extern const char* ExchangeStandard;

enum class LIB_EXPORT ExchangeCode {
  /*################# OTHER #################*/
  XXXX = 0,

  /*################# NON ISO-10383 #################*/
  PYPR = 1,
  SIMU = 2,

  /*################# NYSE #################*/
  XNYS = 3,  // NYSE
  NYSD = 4,  // NYSE Dark
  XCIS = 5,  // NYSE National
  CISD = 6,  // NYSE National Dark
  XCHI = 7,  // NYSE Chicago
  ARCX = 8,  // ARCA
  ARCD = 9,  // ARCA Dark
  ARCO = 10, // ARCA Options
  XASE = 11, // AMEX
  AMXO = 12, // AMEX Options
  // XNLI, // NYSE LIFFE

  /*################# NASDAQ #################*/
  XNAS = 13, // NASDAQ
  XNGS = 14, // NASDAQ Global Select
  XNCM = 15, // NASDAQ Capital Markets
  XNMS = 16, // NASDAQ Global Market
  NASD = 17, // NASDAQ Dark
  XNDQ = 18, // NASDAQ Options
  XBOS = 19, // NASDAQ Boston
  BOSD = 20, // NASDAQ Boston Dark
  XBXO = 21, // NASDAQ Boston Options
  XPHL = 22, // NASDAQ Philly
  XPSX = 23, // NASDAQ PSX (also philly?)
  PSXD = 24, // NASDAQ Philly Dark
  XPHO = 25, // NASDAQ Philly Options
  XPBT = 26, // PBOT
  XPOR = 27, // NASDAQ Portal
  // XBRT, // BRUT ECN
  XNFI = 28, // NASDAQ Fixed Income
  XISE = 29, // ISE Equities (ISE)
  GMNI = 30, // ISE Gemini Options (GEMX)
  MCRY = 31, // ISE Mercury Options (MRX)
  // XISA, // ISE Alternative Markets
  // XISX, // ISE

  /*################# CBOE #################*/
  XCBO = 32, // CBOE
  EDGA = 33, // EDGA
  EDGD = 34, // EDGA DARK
  EDGX = 35, // EDGX
  EDDP = 36, // EDGX DARK
  EDGO = 37, // EDGX Options
  BATS = 38, // BZX
  BZXD = 39, // BZX DARK
  BATO = 40, // BZX Options
  BATY = 41, // BYX
  BYXD = 42, // BYX DARK
  C2OX = 43, // CBOE C2 Options
  // BHSF, // CBOE Swap Execution Facility
  // HSFX, // CBOE Hotspot FX
  // XCBF, // CBOE Futures
  // XCBD, // CBOE Digital
  // CFIM, // CBOE Fixed Income

  /*################# CME #################*/
  XCME = 44, // CME
  FCME = 45, // CME Floor
  // XIMM, // CME IMM (FX / IR)
  GLBX = 46, // Globex
  // XIOM, // CME INDEX AND OPTIONS MARKET
  // CMES, // CME SWAPS MARKETS (CME)
  // CBTS, // CME SWAPS MARKETS (CBOT)
  // NYMS, // CME SWAPS MARKETS (NYMEX)
  // CECS, // CME SWAPS MARKETS (COMEX)
  XCBT = 47, // CBOT
  FCBT = 48, // CBOT Floor
  XKBT = 49, // KANSAS CITY BOARD OF TRADE
  XNYM = 50, // NYMEX
  // XCEC, // NYMEX COMMODITIES EXCHANGE CENTER
  // XNYE, // NYMEX - OTC MARKETS
  // XNYL, // NYMEX - ENERGY MARKETS

  /*################# MIAX #################*/
  MIHI = 51, // MIAX
  MPRL = 52, // MIAX Pearl
  EPRL = 53, // MIAX Pearl
  EPRD = 54, // MIAX Pearl Dark
  XMIO = 55, // MIAX Options
  EMLD = 56, // MIAX Emerald Options

  /*################# OTC Markets #################*/
  OTCM = 57, // OTC Markets
  CAVE = 58, // OTC CAVEAT EMPTOR
  OTCB = 59, // OTCQB MARKETPLACE
  OTCQ = 60, // OTCQX MARKETPLACE
  PINL = 61, // OTC PINK LIMITED
  PINI = 62, // OTC PINK NO INFORMATION
  PINX = 63, // OTC PINK MARKETPLACE
  PSGM = 64, // OTC GREY MARKET
  PINC = 65, // OTC PINK CURRENT

  /*################# FINRA #################*/
  FINR = 66, // FINRA
  FINN = 67, // FINRA NASDAQ TRF (NJ)
  FINC = 68, // FINRA NASDAQ TRF (Chicago)
  FINY = 69, // FINRA NYSE TRF
  XADF = 70, // FINRA ADF
  FINO = 71, // FINRA ORF
  OOTC = 72, // Other OTC

  /*################# OTHER US #################*/
  OPRA = 73, // OPRA
  MEMX = 74, // MEMX
  MEMD = 75, // MEMX Dark
  MXOP = 76, // MEMX Options
  // MEMM,MEMX,SGMT,MEMX LLC RETAIL MIDPOINT,MEMX LLC,254900ZJZM9RSYHE7D79,NSPD,,US
  IEXG = 77, // IEX
  // IEXD, // IEX Dark
  LTSE = 78, // Long Term Stock Exchange

  /*################# Canadian Securities Exchange CSE #################*/
  XCNQ = 79, // CSE
  PURE = 80, // CSE Pure
  CSE2 = 81, // CSE CSE2

  /*################# TMX Group  #################*/
  XTSE = 82, // TSE
  XDRK = 83, // TSX Dark
  VDRK = 84, // TSX Venture Dark
  XTSX = 85, // TSX Venture
  XTNX = 86, // TSX Venture Nex
  XATS = 87, // Alpha Exchange
  XATX = 88, // Alpha X
  ADRK = 89, // Alpha Dark
  XMOD = 90, // Montreal
  XMOC = 91, // Montreal Climate

  /*################# CBOE NEO #################*/
  NEOE = 92, // NEO Exchange
  NEOD = 93, // NEO Exchange Dark
  NEON = 94, // NEO Exchange (MARKET BY
             // PRICE),,549300MILSKTNBLQ1L12,NSPD,NEO-N,CA,TORONTO,WWW.NEOSTOCKEXCHANGE.COM,ACTIVE,20180723,20190624,,,
  NEOC = 95, // NEO Connect

  /*################# Other Canada / Canada ATS #################*/
  // XCX2,CHIC,SGMT,CX2,,,NSPD,,CA,TORONTO,WWW.CHI-X.COM/CA,ACTIVE
  // CHIC,CHIC,OPRT,CHI-X CANADA ATS,,,ATSS,,CA,TORONTO,WWW.CHI-XCANADA.COM,ACTIVE
  // EQCA,EQCA,OPRT,EQUILEND CANADA CORP.,EQUILEND CANADA
  // CORP.,213800MJ9CY4JWO58S26,NSPD,,CA,TORONTO,WWW.EQUILEND.COM,ACTIVE BNSX,BNSX,OPRT,THE BANK OF NOVA
  // SCOTIA,,L3I9ZG2KFGXZ61BMYR72,SINT,,CA,TORONTO,WWW.SCOTIABANK.COM,ACTIVE CAND,CAND,OPRT,CANDEAL.CA
  // INC,,549300QSD4O4FEHPDA44,NSPD,CANDEAL,CA,TORONTO,WWW.CANDEAL.COM,ACTIVE CANX,CANX,OPRT,CANNEX FINANCIAL EXCHANGE
  // LTS,,,NSPD,CANNEX,CA,TORONTO,WWW.CANNEX.COM,ACTIVE COTC,COTC,OPRT,BMO CAPITAL MARKETS - CAD OTC
  // TRADES,,L64HM9LHPDOS1B9HJC68,NSPD,,CA,TORONTO,WWW.BMOCM.COM,ACTIVE IVZX,IVZX,OPRT,INVESCO CANADA PTF
  // TRADES,,9F443AVI6KXI3MYCLS29,NSPD,,CA,TORONTO,WWW.INVESCO.CA,ACTIVE LICA,LICA,OPRT,LIQUIDNET CANADA
  // ATS,,21380031335M4LHQJ436,ATSS,,CA,TORONTO,WWW.LIQUIDNET.COM,ACTIVE MATN,MATN,OPRT,MATCH
  // NOW,,,NSPD,,CA,TORONTO,WWW.TRIACTCANADA.COM,ACTIVE NGXC,NGXC,OPRT,NATURAL GAS
  // EXCHANGE,,549300MZWLT9C8T4VI12,NSPD,NGX,CA,CALGARY,WWW.NGX.COM,ACTIVE OMGA,OMGA,OPRT,OMEGA
  // ATS,,,ATSS,,CA,TORONTO,WWW.OMEGAATS.COM,ACTIVE LYNX,OMGA,SGMT,LYNX ATS,,,ATSS,,CA,TORONTO,WWW.OMEGAATS.COM,ACTIVE
  // XBBK,XBBK,OPRT,PERIMETER FINANCIAL CORP. - BLOCKBOOK ATS,,,ATSS,,CA,TORONTO,WWW.PFIN.CA,ACTIVE
  // XCXD,XCXD,OPRT,NASDAQ CXD,,,NSPD,,CA,TORONTO,HTTP://BUSINESS.NASDAQ.COM/TRADE/CANADIAN-EQUITIES/OVERVIEW,ACTIVE
  // XICX,XICX,OPRT,INSTINET CANADA CROSS,,549300SU730FTQOKTE75,NSPD,,CA,TORONTO,WWW.INSTINET.COM,ACTIVE

  /*################# Other US based Equity ATS #################*/
  // https://www.finra.org/filing-reporting/otc-transparency/ats-equity-firms
  // https://www.sec.gov/foia/docs/atslist
  // ABEX, // 303 Alternatives LLC
  // BIDS, // Bids Trading LP
  // BNPC, // BNP Paribas Cortex
  // OCEA, // Blue Ocean ATS
  // CCMX, // Carta
  // ICBX, // Instinet
  // ONEC, // Citigroup One ATS
  // clearlist
  // CODA, // Coda Markets
  // CAES, // Credit Suisse Crossfinder
  // XSTM, // Fidelity Crossstream
  // dealerweb
  // EQX LLC
  // FNC AG STOCK
  // GOTC, // Global OTC
  // IATS, // Interactive Brokers ATS
  // IEOS, // Interactive Brokers EOS ATS
  // BAML, // BAML Instinct X ATS
  // INCR, // Intelligentcross ATS
  // INVESTX GEM
  // INX SECURITIES, LLC
  // JPBX, // JP Morgan Securities JPB-X
  // JPMX, // JP Morgan Securities JPM-X
  // LEVL, // Level ATS
  // LIUH, // Liquidnet H2O
  // LIQUIDNET NEGOTIATION ATS
  // lodas
  // LMNX, // Luminex ATS
  // MS POOL (ATS-4)	MSPL	MORGAN STANLEY & CO. LLC
  // MS RPOOL (ATS-6)	MSRP	MORGAN STANLEY & CO. LLC
  // MS TRAJECTORY CROSS (ATS-1)	MSTX	MORGAN STANLEY & CO. LLC
  // NFSTX, LLC	NFST	NFSTX, LLC
  // NORTH CAPITAL PRIVATE SECURITIES CORPORATION
  // OASIS PRO MARKETS LLC
  // CGXS, // ONECHRONOS
  // OTC Link
  // OTCN, // OTC Link ECN
  // OTCI, // OTC Link NQB IDQS
  // ITGI, // Virtu Posit
  // PROMETHEUM EMBER ATS INC.
  // STRM, // Purestream
  // SECURITIZE MARKETS ATS
  // SHARENETT ATS
  // SGMT, // Goldman Sigma X2
  // STARTENGINE SECONDARY
  // STFX, // Stifel, Nicolaus and Co STIFEL X ATS
  // TEXTURE ATS
  // BARX, // Barclays ATS
  // TOR ATS
  // UBSA, // UBS ATS
  // VARIABLE INVESTMENT ADVISORS, INC. ATS (VIAATS)
  // VCRS, // Virtu MATCHIT conditional room
  // VFMI, // Virtu Matchit
  // PJCX, // Piper Sandler and Co. ATS

  /*################# Other US based Options/Futures ATS #################*/
  // DASH, // DASH ATS
  // FNFT, // BGC Fenics Futures
  // BGCD, // BGC Derivatives
  // XBOX, // BOX

  /*################# Other US based Fixed Income ATS #################*/
  // https://www.finra.org/filing-reporting/otc-transparency/finra-equity-ats-firms-list
  // SCXA,SCXO,SGMT,SEED DIGITAL SECURITIES MARKET,,5493009JXYKN3NLOUE77,ATSS,,US
  // BNDS, // Bonds.com Bondspro
  // BTEQ, // BrokerTec
  // cboe fixed income (above)
  // CLARITY BIDRATE ALTERNATIVE TRADING SYSTEM
  // clearlist
  // CREDITMATCH
  // DWFI, // Dealerweb
  // FNCS, // BGCF Fenics
  // GSEF, // GFI Swaps Exchange
  // HTD-ATS
  // interactive broker ats (above)
  // ICSU, // ICAP SEF
  // VABD, // ICE Bondpoint
  // TMCC, // ICE TMC
  // IDXM, // IDX Markets
  // Kopen Tech Capital Markets
  // LESI, // LedgerEdge
  // LIFI, // Liquidnet Fixed Income ATS
  // MKAA, // Marketaxess ATS
  // LQED, // LIQUIDITYEDGE
  // MBS Source eTrading, Inc.
  // North Capital Private Securities Corporation
  // OASIS PRO MARKETS LLC
  // OTC Link (above)
  // SECURITIZE MARKETS ATS
  // SHARENETT ATS
  // TEXTURE ATS
  // TP ICAP Global Markets Americas LLC
  // TPCD, // TULLETT PREBON PLC - TP CREDITDEAL
  // BNDD, // TRADEWEB DIRECT
  // TRWB, // TRADEWEB LLC
  // TWSF,TRWB,SGMT,TW SEF LLC,,5493000G5QHJUY9ZWQ91,NSPD,TWSEF,US
  // DWSF,TRWB,SGMT,DW SEF LLC,,5493000G5QHJUY9ZWQ91,NSPD,DWSEF,US
  // TMID, // Trumid

  /*################# Other US based ATS #################*/
  // AATS, // Assent ATS
  // BLUE, // tZero / PRO SECURITIES ATS
  // CLST, // Clear Street
  // FNXB, // BGCF Fenicx Invitations
  // FNFX, // BGC Fenics FX
  // GFAM, // GFI
  // LATG, // GFI LATG
  // PRSE, // Pragma ATS
  // XAQS,XAQS,OPRT,AUTOMATED EQUITY FINANCE MARKETS,,,ATSS,AQS,US
  // XTXD, // XTX Direct

  /*################# US based options #################*/

  /*################# US based futures #################*/
  // SMFE, // Small Exchange

  /*################# US based fx #################*/

  /*################# US based crypto #################*/
  // BKKT, // BAKKT
  // FREX, // COINBASE DERIVATIVES
  // SFOX, // SFOX
  // XTRD, // XTRD

  /*################# OTHER PARENT ORGS #################*/
  // BGCF, // BGC Financial
  // BTEC, // ICAP Electronic Broking
  // GSCO, // Goldman Sachs
  // IBKR, // Interactive Brokers
  // JPMS, // JP Morgan Securities
  // LIUS, // Liquidnet US
  // MTXX, // Marketaxess
  // PIPR, // Piper Sandler and Co.
  // UBSS, // UBS Securities LLC
  // VUSA, // Virtu Americas
  // VFCM, // Virtu Financial Capital Markets
  // XTXM, // XTX Markets
};

static const char* ExchangeCodeNames[] = {
  "XXXX", // 0
  "PYPR", // 1
  "SIMU", // 2
  "XNYS", // 3
  "NYSD", // 4
  "XCIS", // 5
  "CISD", // 6
  "XCHI", // 7
  "ARCX", // 8
  "ARCD", // 9
  "ARCO", // 10
  "XASE", // 11
  "AMXO", // 12
  "XNAS", // 13
  "XNGS", // 14
  "XNCM", // 15
  "XNMS", // 16
  "NASD", // 17
  "XNDQ", // 18
  "XBOS", // 19
  "BOSD", // 20
  "XBXO", // 21
  "XPHL", // 22
  "XPSX", // 23
  "PSXD", // 24
  "XPHO", // 25
  "XPBT", // 26
  "XPOR", // 27
  "XNFI", // 28
  "XISE", // 29
  "GMNI", // 30
  "MCRY", // 31
  "XCBO", // 32
  "EDGA", // 33
  "EDGD", // 34
  "EDGX", // 35
  "EDDP", // 36
  "EDGO", // 37
  "BATS", // 38
  "BZXD", // 39
  "BATO", // 40
  "BATY", // 41
  "BYXD", // 42
  "C2OX", // 43
  "XCME", // 44
  "FCME", // 45
  "GLBX", // 46
  "XCBT", // 47
  "FCBT", // 48
  "XKBT", // 49
  "XNYM", // 50
  "MIHI", // 51
  "MPRL", // 52
  "EPRL", // 53
  "EPRD", // 54
  "XMIO", // 55
  "EMLD", // 56
  "OTCM", // 57
  "CAVE", // 58
  "OTCB", // 59
  "OTCQ", // 60
  "PINL", // 61
  "PINI", // 62
  "PINX", // 63
  "PSGM", // 64
  "PINC", // 65
  "FINR", // 66
  "FINN", // 67
  "FINC", // 68
  "FINY", // 69
  "XADF", // 70
  "FINO", // 71
  "OOTC", // 72
  "OPRA", // 73
  "MEMX", // 74
  "MEMD", // 75
  "MXOP", // 76
  "IEXG", // 77
  "LTSE", // 78
  "XCNQ", // 79
  "PURE", // 80
  "CSE2", // 81
  "XTSE", // 82
  "XDRK", // 83
  "VDRK", // 84
  "XTSX", // 85
  "XTNX", // 86
  "XATS", // 87
  "XATX", // 88
  "ADRK", // 89
  "XMOD", // 90
  "XMOC", // 91
  "NEOE", // 92
  "NEOD", // 93
  "NEON", // 94
  "NEOC", // 95
};

static ExchangeCode _ExchangeCodeToParentExchange[] = {
  ExchangeCode::XXXX, // 0
  ExchangeCode::PYPR, // 1
  ExchangeCode::SIMU, // 2
  ExchangeCode::XNYS, // 3
  ExchangeCode::XNYS, // 4
  ExchangeCode::XNYS, // 5
  ExchangeCode::XNYS, // 6
  ExchangeCode::XNYS, // 7
  ExchangeCode::XNYS, // 8
  ExchangeCode::XNYS, // 9
  ExchangeCode::XNYS, // 10
  ExchangeCode::XNYS, // 11
  ExchangeCode::XNYS, // 12
  ExchangeCode::XNAS, // 13
  ExchangeCode::XNAS, // 14
  ExchangeCode::XNAS, // 15
  ExchangeCode::XNAS, // 16
  ExchangeCode::XNAS, // 17
  ExchangeCode::XNAS, // 18
  ExchangeCode::XNAS, // 19
  ExchangeCode::XNAS, // 20
  ExchangeCode::XNAS, // 21
  ExchangeCode::XNAS, // 22
  ExchangeCode::XNAS, // 23
  ExchangeCode::XNAS, // 24
  ExchangeCode::XNAS, // 25
  ExchangeCode::XNAS, // 26
  ExchangeCode::XNAS, // 27
  ExchangeCode::XNAS, // 28
  ExchangeCode::XNAS, // 29
  ExchangeCode::XNAS, // 30
  ExchangeCode::XNAS, // 31
  ExchangeCode::XCBO, // 32
  ExchangeCode::XCBO, // 33
  ExchangeCode::XCBO, // 34
  ExchangeCode::XCBO, // 35
  ExchangeCode::XCBO, // 36
  ExchangeCode::XCBO, // 37
  ExchangeCode::XCBO, // 38
  ExchangeCode::XCBO, // 39
  ExchangeCode::XCBO, // 40
  ExchangeCode::XCBO, // 41
  ExchangeCode::XCBO, // 42
  ExchangeCode::XCBO, // 43
  ExchangeCode::XCME, // 44
  ExchangeCode::XCME, // 45
  ExchangeCode::XCME, // 46
  ExchangeCode::XCBT, // 47
  ExchangeCode::XCBT, // 48
  ExchangeCode::XCBT, // 49
  ExchangeCode::XNYM, // 50
  ExchangeCode::MIHI, // 51
  ExchangeCode::MIHI, // 52
  ExchangeCode::MIHI, // 53
  ExchangeCode::MIHI, // 54
  ExchangeCode::MIHI, // 55
  ExchangeCode::MIHI, // 56
  ExchangeCode::OTCM, // 57
  ExchangeCode::OTCM, // 58
  ExchangeCode::OTCM, // 59
  ExchangeCode::OTCM, // 60
  ExchangeCode::OTCM, // 61
  ExchangeCode::OTCM, // 62
  ExchangeCode::OTCM, // 63
  ExchangeCode::OTCM, // 64
  ExchangeCode::OTCM, // 65
  ExchangeCode::FINR, // 66
  ExchangeCode::FINR, // 67
  ExchangeCode::FINR, // 68
  ExchangeCode::FINR, // 69
  ExchangeCode::FINR, // 70
  ExchangeCode::FINR, // 71
  ExchangeCode::FINR, // 72
  ExchangeCode::OPRA, // 73
  ExchangeCode::MEMX, // 74
  ExchangeCode::MEMX, // 75
  ExchangeCode::MEMX, // 76
  ExchangeCode::IEXG, // 77
  ExchangeCode::LTSE, // 78
  ExchangeCode::XCNQ, // 79
  ExchangeCode::XCNQ, // 80
  ExchangeCode::XCNQ, // 81
  ExchangeCode::XTSE, // 82
  ExchangeCode::XTSE, // 83
  ExchangeCode::XTSX, // 84
  ExchangeCode::XTSX, // 85
  ExchangeCode::XTSX, // 86
  ExchangeCode::XATS, // 87
  ExchangeCode::XATS, // 88
  ExchangeCode::XATS, // 89
  ExchangeCode::XMOD, // 90
  ExchangeCode::XMOD, // 91
  ExchangeCode::NEOE, // 92
  ExchangeCode::NEOE, // 93
  ExchangeCode::NEOE, // 94
  ExchangeCode::NEOE, // 95
};

static CountryCode _ExchangeCodeToCountryCode[] = {
  CountryCode::XX, // 0
  CountryCode::XX, // 1
  CountryCode::XX, // 2
  CountryCode::US, // 3
  CountryCode::US, // 4
  CountryCode::US, // 5
  CountryCode::US, // 6
  CountryCode::US, // 7
  CountryCode::US, // 8
  CountryCode::US, // 9
  CountryCode::US, // 10
  CountryCode::US, // 11
  CountryCode::US, // 12
  CountryCode::US, // 13
  CountryCode::US, // 14
  CountryCode::US, // 15
  CountryCode::US, // 16
  CountryCode::US, // 17
  CountryCode::US, // 18
  CountryCode::US, // 19
  CountryCode::US, // 20
  CountryCode::US, // 21
  CountryCode::US, // 22
  CountryCode::US, // 23
  CountryCode::US, // 24
  CountryCode::US, // 25
  CountryCode::US, // 26
  CountryCode::US, // 27
  CountryCode::US, // 28
  CountryCode::US, // 29
  CountryCode::US, // 30
  CountryCode::US, // 31
  CountryCode::US, // 32
  CountryCode::US, // 33
  CountryCode::US, // 34
  CountryCode::US, // 35
  CountryCode::US, // 36
  CountryCode::US, // 37
  CountryCode::US, // 38
  CountryCode::US, // 39
  CountryCode::US, // 40
  CountryCode::US, // 41
  CountryCode::US, // 42
  CountryCode::US, // 43
  CountryCode::US, // 44
  CountryCode::US, // 45
  CountryCode::US, // 46
  CountryCode::US, // 47
  CountryCode::US, // 48
  CountryCode::US, // 49
  CountryCode::US, // 50
  CountryCode::US, // 51
  CountryCode::US, // 52
  CountryCode::US, // 53
  CountryCode::US, // 54
  CountryCode::US, // 55
  CountryCode::US, // 56
  CountryCode::US, // 57
  CountryCode::US, // 58
  CountryCode::US, // 59
  CountryCode::US, // 60
  CountryCode::US, // 61
  CountryCode::US, // 62
  CountryCode::US, // 63
  CountryCode::US, // 64
  CountryCode::US, // 65
  CountryCode::US, // 66
  CountryCode::US, // 67
  CountryCode::US, // 68
  CountryCode::US, // 69
  CountryCode::US, // 70
  CountryCode::US, // 71
  CountryCode::US, // 72
  CountryCode::US, // 73
  CountryCode::US, // 74
  CountryCode::US, // 75
  CountryCode::US, // 76
  CountryCode::US, // 77
  CountryCode::US, // 78
  CountryCode::CA, // 79
  CountryCode::CA, // 80
  CountryCode::CA, // 81
  CountryCode::CA, // 82
  CountryCode::CA, // 83
  CountryCode::CA, // 84
  CountryCode::CA, // 85
  CountryCode::CA, // 86
  CountryCode::CA, // 87
  CountryCode::CA, // 88
  CountryCode::CA, // 89
  CountryCode::CA, // 90
  CountryCode::CA, // 91
  CountryCode::CA, // 92
  CountryCode::CA, // 93
  CountryCode::CA, // 94
  CountryCode::CA, // 95
};

static const char* ExchangeNames[] = {
  "Uncategorized",                     // "XXXX", // 0
  "Paper",                             // "PYPR", // 1
  "Simulation",                        // "SIMU", // 2
  "New York Stock Exchange",           // "XNYS", // 3
  "NYSE Dark",                         // "NYSD", // 4
  "NYSE National",                     // "XCIS", // 5
  "NYSE National Dark",                // "CISD", // 6
  "NYSE Chicago",                      // "XCHI", // 7
  "NYSE ARCA",                         // "ARCX", // 8
  "NYSE ARCA Dark",                    // "ARCD", // 9
  "NYSE ARCA Options",                 // "ARCO", // 10
  "NYSE AMEX",                         // "XASE", // 11
  "NYSE AMEX Options",                 // "AMXO", // 12
  "Nasdaq",                            // "XNAS", // 13
  "Nasdaq Global Select",              // "XNGS", // 14
  "Nasdaq Capital Markets",            // "XNCM", // 15
  "Nasdaq Global Markets",             // "XNMS", // 16
  "Nasdaq Dark",                       // "NASD", // 17
  "Nasdaq Options",                    // "XNDQ", // 18
  "Nasdaq BX",                         // "XBOS", // 19
  "Nasdaq BX Dark",                    // "BOSD", // 20
  "Nasdaq BX Options",                 // "XBXO", // 21
  "Nasdaq PHLX",                       // "XPHL", // 22
  "Nasdaq PSX",                        // "XPSX", // 23
  "Nasdaq PSX Dark",                   // "PSXD", // 24
  "Nasdaq PSX Options",                // "XPHO", // 25
  "Philadelphia Board of Trade",       // "XPBT", // 26
  "Nasdaq Portal",                     // "XPOR", // 27
  "Nasdaq Fixed Income",               // "XNFI", // 28
  "ISE Equities",                      // "XISE", // 29
  "ISE Gemini Options",                // "GMNI", // 30
  "ISE Mercury Options",               // "MCRY", // 31
  "CBOE Global Markets",               // "XCBO", // 32
  "CBOE EDGA",                         // "EDGA", // 33
  "CBOE EDGA Dark",                    // "EDGD", // 34
  "CBOE EDGX",                         // "EDGX", // 35
  "CBOE EDGX Dark",                    // "EDDP", // 36
  "CBOE EDGX Options",                 // "EDGO", // 37
  "CBOE BZX",                          // "BATS", // 38
  "CBOE BZX Dark",                     // "BZXD", // 39
  "CBOE BZX Options",                  // "BATO", // 40
  "CBOE BYX",                          // "BATY", // 41
  "CBOE BYX Dark",                     // "BYXD", // 42
  "CBOE C2 Options",                   // "C2OX", // 43
  "Chicago Mercantile Exchange",       // "XCME", // 44
  "CME Floor",                         // "FCME", // 45
  "Globex",                            // "GLBX", // 46
  "Chicago Board of Trade",            // "XCBT", // 47
  "CBOT Floor",                        // "FCBT", // 48
  "Kansas City Board of Trade",        // "XKBT", // 49
  "New York Mercantile Exchange",      // "XNYM", // 50
  "MIAX",                              // "MIHI", // 51
  "MIAX Pearl",                        // "MPRL", // 52
  "MIAX Pearl",                        // "EPRL", // 53
  "MIAX Pearl Dark",                   // "EPRD", // 54
  "MIAX Options",                      // "XMIO", // 55
  "MIAX Emerald",                      // "EMLD", // 56
  "OTC Markets",                       // "OTCM", // 57
  "OTC Caveat Emptor",                 // "CAVE", // 58
  "OTC QB Marketplace",                // "OTCB", // 59
  "OTC QX Marketplace",                // "OTCQ", // 60
  "OTC Pink Limited",                  // "PINL", // 61
  "OTC Pink No Information",           // "PINI", // 62
  "OTC Pink Marketplace",              // "PINX", // 63
  "OTC Grey Market",                   // "PSGM", // 64
  "OTC Pink Current",                  // "PINC", // 65
  "FINRA",                             // "FINR", // 66
  "FINRA NASDAQ TRF (NJ)",             // "FINN", // 67
  "FINRA NASDAQ TRF (Chicago)",        // "FINC", // 68
  "FINRA NYSE TRF",                    // "FINY", // 69
  "FINRA ADF",                         // "XADF", // 70
  "FINRA ORF",                         // "FINO", // 71
  "FINRA Other OTC",                   // "OOTC", // 72
  "Options Price Reporting Authority", // "OPRA", // 73
  "Members Exchange",                  // "MEMX", // 74
  "MEMX Dark",                         // "MEMD", // 75
  "MEMX Options",                      // "MXOP", // 76
  "Investors Exchange",                // "IEXG", // 77
  "Long-Term Stock Exchange",          // "LTSE", // 78
  "Canadian Securities Exchange",      // "XCNQ", // 79
  "CSE Pure",                          // "PURE", // 80
  "CSE CSE2",                          // "CSE2", // 81
  "Toronto Stock Exchange",            // "XTSE", // 82
  "TSE Dark",                          // "XDRK", // 83
  "TRX Venture Exchange",              // "VDRK", // 84
  "TRX Venture Exchange Dark",         // "XTSX", // 85
  "TRX Venture Nex",                   // "XTNX", // 86
  "Alpha Exchange",                    // "XATS", // 87
  "Alpha Exchange X",                  // "XATX", // 88
  "Alpha Exchange Dark",               // "ADRK", // 89
  "Montréal Exchange",                 // "XMOD", // 90
  "Montréal Climate Exchange",         // "XMOC", // 91
  "NEO Exchange",                      // "NEOE", // 92
  "NEO Exchange Dark",                 // "NEOD", // 93
  "NEO Exchange",                      // "NEON", // 94
  "NEO Connect",                       // "NEOC", // 95
};

const char* ExchangeCodeToString(const ExchangeCode);
const char* ExchangeCodeToName(const ExchangeCode);
ExchangeCode ExchangeCodeFromString(const char*);
ExchangeCode ExchangeCodeToParentExchange(const ExchangeCode);
CountryCode ExchangeCodeToCountryCode(const ExchangeCode);

}
