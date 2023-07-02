#include <cstring>
#include <finance-enums/exchange.hpp>

namespace finance_enums {

const char* ExchangeStandard = "ISO10383";

const char* ExchangeCodeToString(const ExchangeCode t) { return ExchangeCodeNames[static_cast<int>(t)]; }
const char* ExchangeCodeToName(const ExchangeCode t) { return ExchangeNames[static_cast<int>(t)]; }

ExchangeCode ExchangeCodeFromString(const char* s) {
  if(strncmp(s, "XXXX", 4) == 0)
    return ExchangeCode::XXXX;
  if(strncmp(s, "PYPR", 4) == 0)
    return ExchangeCode::PYPR;
  if(strncmp(s, "SIMU", 4) == 0)
    return ExchangeCode::SIMU;
  if(strncmp(s, "XNYS", 4) == 0)
    return ExchangeCode::XNYS;
  if(strncmp(s, "NYSD", 4) == 0)
    return ExchangeCode::NYSD;
  if(strncmp(s, "XCIS", 4) == 0)
    return ExchangeCode::XCIS;
  if(strncmp(s, "CISD", 4) == 0)
    return ExchangeCode::CISD;
  if(strncmp(s, "XCHI", 4) == 0)
    return ExchangeCode::XCHI;
  if(strncmp(s, "ARCX", 4) == 0)
    return ExchangeCode::ARCX;
  if(strncmp(s, "ARCD", 4) == 0)
    return ExchangeCode::ARCD;
  if(strncmp(s, "ARCO", 4) == 0)
    return ExchangeCode::ARCO;
  if(strncmp(s, "XASE", 4) == 0)
    return ExchangeCode::XASE;
  if(strncmp(s, "AMXO", 4) == 0)
    return ExchangeCode::AMXO;
  if(strncmp(s, "XNAS", 4) == 0)
    return ExchangeCode::XNAS;
  if(strncmp(s, "XNGS", 4) == 0)
    return ExchangeCode::XNGS;
  if(strncmp(s, "XNCM", 4) == 0)
    return ExchangeCode::XNCM;
  if(strncmp(s, "XNMS", 4) == 0)
    return ExchangeCode::XNMS;
  if(strncmp(s, "NASD", 4) == 0)
    return ExchangeCode::NASD;
  if(strncmp(s, "XNDQ", 4) == 0)
    return ExchangeCode::XNDQ;
  if(strncmp(s, "XBOS", 4) == 0)
    return ExchangeCode::XBOS;
  if(strncmp(s, "BOSD", 4) == 0)
    return ExchangeCode::BOSD;
  if(strncmp(s, "XBXO", 4) == 0)
    return ExchangeCode::XBXO;
  if(strncmp(s, "XPHL", 4) == 0)
    return ExchangeCode::XPHL;
  if(strncmp(s, "XPSX", 4) == 0)
    return ExchangeCode::XPSX;
  if(strncmp(s, "PSXD", 4) == 0)
    return ExchangeCode::PSXD;
  if(strncmp(s, "XPHO", 4) == 0)
    return ExchangeCode::XPHO;
  if(strncmp(s, "XPBT", 4) == 0)
    return ExchangeCode::XPBT;
  if(strncmp(s, "XPOR", 4) == 0)
    return ExchangeCode::XPOR;
  if(strncmp(s, "XNFI", 4) == 0)
    return ExchangeCode::XNFI;
  if(strncmp(s, "XISE", 4) == 0)
    return ExchangeCode::XISE;
  if(strncmp(s, "GMNI", 4) == 0)
    return ExchangeCode::GMNI;
  if(strncmp(s, "MCRY", 4) == 0)
    return ExchangeCode::MCRY;
  if(strncmp(s, "XCBO", 4) == 0)
    return ExchangeCode::XCBO;
  if(strncmp(s, "EDGA", 4) == 0)
    return ExchangeCode::EDGA;
  if(strncmp(s, "EDGD", 4) == 0)
    return ExchangeCode::EDGD;
  if(strncmp(s, "EDGX", 4) == 0)
    return ExchangeCode::EDGX;
  if(strncmp(s, "EDDP", 4) == 0)
    return ExchangeCode::EDDP;
  if(strncmp(s, "EDGO", 4) == 0)
    return ExchangeCode::EDGO;
  if(strncmp(s, "BATS", 4) == 0)
    return ExchangeCode::BATS;
  if(strncmp(s, "BZXD", 4) == 0)
    return ExchangeCode::BZXD;
  if(strncmp(s, "BATO", 4) == 0)
    return ExchangeCode::BATO;
  if(strncmp(s, "BATY", 4) == 0)
    return ExchangeCode::BATY;
  if(strncmp(s, "BYXD", 4) == 0)
    return ExchangeCode::BYXD;
  if(strncmp(s, "C2OX", 4) == 0)
    return ExchangeCode::C2OX;
  if(strncmp(s, "XCME", 4) == 0)
    return ExchangeCode::XCME;
  if(strncmp(s, "FCME", 4) == 0)
    return ExchangeCode::FCME;
  if(strncmp(s, "GLBX", 4) == 0)
    return ExchangeCode::GLBX;
  if(strncmp(s, "XCBT", 4) == 0)
    return ExchangeCode::XCBT;
  if(strncmp(s, "FCBT", 4) == 0)
    return ExchangeCode::FCBT;
  if(strncmp(s, "XKBT", 4) == 0)
    return ExchangeCode::XKBT;
  if(strncmp(s, "XNYM", 4) == 0)
    return ExchangeCode::XNYM;
  if(strncmp(s, "MIHI", 4) == 0)
    return ExchangeCode::MIHI;
  if(strncmp(s, "MPRL", 4) == 0)
    return ExchangeCode::MPRL;
  if(strncmp(s, "EPRL", 4) == 0)
    return ExchangeCode::EPRL;
  if(strncmp(s, "EPRD", 4) == 0)
    return ExchangeCode::EPRD;
  if(strncmp(s, "XMIO", 4) == 0)
    return ExchangeCode::XMIO;
  if(strncmp(s, "EMLD", 4) == 0)
    return ExchangeCode::EMLD;
  if(strncmp(s, "OTCM", 4) == 0)
    return ExchangeCode::OTCM;
  if(strncmp(s, "CAVE", 4) == 0)
    return ExchangeCode::CAVE;
  if(strncmp(s, "OTCB", 4) == 0)
    return ExchangeCode::OTCB;
  if(strncmp(s, "OTCQ", 4) == 0)
    return ExchangeCode::OTCQ;
  if(strncmp(s, "PINL", 4) == 0)
    return ExchangeCode::PINL;
  if(strncmp(s, "PINI", 4) == 0)
    return ExchangeCode::PINI;
  if(strncmp(s, "PINX", 4) == 0)
    return ExchangeCode::PINX;
  if(strncmp(s, "PSGM", 4) == 0)
    return ExchangeCode::PSGM;
  if(strncmp(s, "PINC", 4) == 0)
    return ExchangeCode::PINC;
  if(strncmp(s, "FINR", 4) == 0)
    return ExchangeCode::FINR;
  if(strncmp(s, "FINN", 4) == 0)
    return ExchangeCode::FINN;
  if(strncmp(s, "FINC", 4) == 0)
    return ExchangeCode::FINC;
  if(strncmp(s, "FINY", 4) == 0)
    return ExchangeCode::FINY;
  if(strncmp(s, "XADF", 4) == 0)
    return ExchangeCode::XADF;
  if(strncmp(s, "FINO", 4) == 0)
    return ExchangeCode::FINO;
  if(strncmp(s, "OOTC", 4) == 0)
    return ExchangeCode::OOTC;
  if(strncmp(s, "OPRA", 4) == 0)
    return ExchangeCode::OPRA;
  if(strncmp(s, "MEMX", 4) == 0)
    return ExchangeCode::MEMX;
  if(strncmp(s, "MEMD", 4) == 0)
    return ExchangeCode::MEMD;
  if(strncmp(s, "MXOP", 4) == 0)
    return ExchangeCode::MXOP;
  if(strncmp(s, "IEXG", 4) == 0)
    return ExchangeCode::IEXG;
  if(strncmp(s, "LTSE", 4) == 0)
    return ExchangeCode::LTSE;
  if(strncmp(s, "XCNQ", 4) == 0)
    return ExchangeCode::XCNQ;
  if(strncmp(s, "PURE", 4) == 0)
    return ExchangeCode::PURE;
  if(strncmp(s, "CSE2", 4) == 0)
    return ExchangeCode::CSE2;
  if(strncmp(s, "XTSE", 4) == 0)
    return ExchangeCode::XTSE;
  if(strncmp(s, "XDRK", 4) == 0)
    return ExchangeCode::XDRK;
  if(strncmp(s, "VDRK", 4) == 0)
    return ExchangeCode::VDRK;
  if(strncmp(s, "XTSX", 4) == 0)
    return ExchangeCode::XTSX;
  if(strncmp(s, "XTNX", 4) == 0)
    return ExchangeCode::XTNX;
  if(strncmp(s, "XATS", 4) == 0)
    return ExchangeCode::XATS;
  if(strncmp(s, "XATX", 4) == 0)
    return ExchangeCode::XATX;
  if(strncmp(s, "ADRK", 4) == 0)
    return ExchangeCode::ADRK;
  if(strncmp(s, "XMOD", 4) == 0)
    return ExchangeCode::XMOD;
  if(strncmp(s, "XMOC", 4) == 0)
    return ExchangeCode::XMOC;
  if(strncmp(s, "NEOE", 4) == 0)
    return ExchangeCode::NEOE;
  if(strncmp(s, "NEOD", 4) == 0)
    return ExchangeCode::NEOD;
  if(strncmp(s, "NEON", 4) == 0)
    return ExchangeCode::NEON;
  if(strncmp(s, "NEOC", 4) == 0)
    return ExchangeCode::NEOC;
  return ExchangeCode::XXXX;
}

ExchangeCode ExchangeCodeToParentExchange(const ExchangeCode t) {
  return _ExchangeCodeToParentExchange[static_cast<int>(t)];
}
CountryCode ExchangeCodeToCountryCode(const ExchangeCode t) { return _ExchangeCodeToCountryCode[static_cast<int>(t)]; }

}