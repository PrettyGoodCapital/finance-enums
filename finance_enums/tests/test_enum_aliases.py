import pytest

from finance_enums import (
    AllocationMethod,
    BenchmarkType,
    ClearingHouse,
    CurrencyRole,
    EnergyType,
    FundType,
    IdentifierType,
    Industry,
    MarketType,
    PriceKind,
    RateIndex,
    ShortSaleRestriction,
    SubIndustry,
    TickerNamespace,
    VehicleWrapper,
)

ALIAS_CASES = [
    (EnergyType, "LNG", "LiquefiedNaturalGas"),
    (FundType, "ETF", "ExchangeTradedFund"),
    (FundType, "REIT", "RealEstateInvestmentTrust"),
    (MarketType, "OTC", "OverTheCounter"),
    (PriceKind, "VWAP", "Vwap"),
    (IdentifierType, "ISIN", "InternationalSecuritiesIdentificationNumber"),
    (IdentifierType, "CUSIP", "CommitteeOnUniformSecuritiesIdentificationProcedures"),
    (IdentifierType, "SEDOL", "StockExchangeDailyOfficialList"),
    (IdentifierType, "FIGI", "FinancialInstrumentGlobalIdentifier"),
    (IdentifierType, "LEI", "LegalEntityIdentifier"),
    (IdentifierType, "RIC", "ReutersInstrumentCode"),
    (IdentifierType, "MIC", "MarketIdentifierCode"),
    (TickerNamespace, "OTC", "OverTheCounter"),
    (CurrencyRole, "PnL", "ProfitAndLoss"),
    (VehicleWrapper, "ETF", "ExchangeTradedFund"),
    (VehicleWrapper, "SICAV", "SocieteInvestissementCapitalVariable"),
    (VehicleWrapper, "OEIC", "OpenEndedInvestmentCompany"),
    (RateIndex, "SOFR", "SecuredOvernightFinancingRate"),
    (RateIndex, "ESTR", "EuroShortTermRate"),
    (RateIndex, "SONIA", "SterlingOvernightIndexAverage"),
    (RateIndex, "EURIBOR", "EuroInterbankOfferedRate"),
    (RateIndex, "TONAR", "TokyoOvernightAverageRate"),
    (RateIndex, "SARON", "SwissAverageRateOvernight"),
    (RateIndex, "CPI", "ConsumerPriceIndex"),
    (ClearingHouse, "NSCC", "NationalSecuritiesClearingCorporation"),
    (ClearingHouse, "FICC", "FixedIncomeClearingCorporation"),
    (ClearingHouse, "OCC", "OptionsClearingCorporation"),
    (ClearingHouse, "CME", "ChicagoMercantileExchange"),
    (ClearingHouse, "ICEClear", "IntercontinentalExchangeClear"),
    (ClearingHouse, "LCH", "LondonClearingHouse"),
    (ClearingHouse, "DTCC", "DepositoryTrustClearingCorporation"),
    (AllocationMethod, "FIFO", "FirstInFirstOut"),
    (AllocationMethod, "LIFO", "LastInFirstOut"),
    (BenchmarkType, "FXFixing", "ForeignExchangeFixing"),
    (ShortSaleRestriction, "RegSHOPriceTest", "RegulationShoPriceTest"),
    (Industry, "ITServices", "InformationTechnologyServices"),
    (Industry, "DiversifiedREITs", "DiversifiedRealEstateInvestmentTrusts"),
    (Industry, "IndustrialREITs", "IndustrialRealEstateInvestmentTrusts"),
    (Industry, "HotelAndResortREITs", "HotelAndResortRealEstateInvestmentTrusts"),
    (Industry, "OfficeREITs", "OfficeRealEstateInvestmentTrusts"),
    (Industry, "HealthCareREITs", "HealthCareRealEstateInvestmentTrusts"),
    (Industry, "ResidentialREITs", "ResidentialRealEstateInvestmentTrusts"),
    (Industry, "RetailREITs", "RetailRealEstateInvestmentTrusts"),
    (Industry, "SpecializedREITs", "SpecializedRealEstateInvestmentTrusts"),
    (SubIndustry, "ITConsultingAndOtherServices", "InformationTechnologyConsultingAndOtherServices"),
    (SubIndustry, "DiversifiedREITs", "DiversifiedRealEstateInvestmentTrusts"),
    (SubIndustry, "IndustrialREITs", "IndustrialRealEstateInvestmentTrusts"),
    (SubIndustry, "HotelAndResortREITs", "HotelAndResortRealEstateInvestmentTrusts"),
    (SubIndustry, "OfficeREITs", "OfficeRealEstateInvestmentTrusts"),
    (SubIndustry, "HealthCareREITs", "HealthCareRealEstateInvestmentTrusts"),
    (SubIndustry, "MultiFamilyResidentialREITs", "MultiFamilyResidentialRealEstateInvestmentTrusts"),
    (SubIndustry, "SingleFamilyResidentialREITs", "SingleFamilyResidentialRealEstateInvestmentTrusts"),
    (SubIndustry, "RetailREITs", "RetailRealEstateInvestmentTrusts"),
    (SubIndustry, "OtherSpecializedREITs", "OtherSpecializedRealEstateInvestmentTrusts"),
    (SubIndustry, "SelfStorageREITs", "SelfStorageRealEstateInvestmentTrusts"),
    (SubIndustry, "TelecomTowerREITs", "TelecomTowerRealEstateInvestmentTrusts"),
    (SubIndustry, "TimberREITs", "TimberRealEstateInvestmentTrusts"),
    (SubIndustry, "DataCenterREITs", "DataCenterRealEstateInvestmentTrusts"),
]


@pytest.mark.parametrize(("enum_type", "alias", "canonical"), ALIAS_CASES)
def test_acronym_aliases_resolve_to_full_spelled_members(enum_type, alias, canonical):
    canonical_member = enum_type[canonical]

    assert getattr(enum_type, alias) is canonical_member
    assert enum_type[alias] is canonical_member
    assert enum_type(alias) is canonical_member
    assert canonical_member.name == canonical


@pytest.mark.parametrize("enum_type", sorted({case[0] for case in ALIAS_CASES}, key=lambda item: item.__name__))
def test_acronym_aliases_do_not_change_canonical_iteration(enum_type):
    iterated_names = {member.name for member in enum_type}
    alias_names = {alias for candidate, alias, _ in ALIAS_CASES if candidate is enum_type}

    assert iterated_names.isdisjoint(alias_names)
