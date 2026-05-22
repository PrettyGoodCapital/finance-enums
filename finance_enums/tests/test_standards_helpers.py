from dataclasses import replace

import pytest

from finance_enums import (
    MICMarketCategory,
    VenueRegulatoryFlag,
    build_cfi_from_classification,
    exchange_record,
    exchange_records_by_market_category_type,
    exchange_records_by_regulatory_flag,
    parse_cfi,
    validate_cfi_classification,
)


def test_exchange_records_expose_typed_market_category_and_regulatory_flags():
    bmtf = exchange_record("BMTF")
    afsa = exchange_record("AFSA")
    finn = exchange_record("FINN")
    asef = exchange_record("ASEF")
    aapa = exchange_record("AAPA")
    xlgt = exchange_record("XLGT")

    assert bmtf is not None
    assert afsa is not None
    assert finn is not None
    assert asef is not None
    assert aapa is not None
    assert xlgt is not None

    assert bmtf.market_category() == MICMarketCategory.MultilateralTradingFacility
    assert afsa.market_category() == MICMarketCategory.OrganizedTradingFacility
    assert finn.market_category() == MICMarketCategory.TradeReportingFacility
    assert asef.market_category() == MICMarketCategory.SwapExecutionFacility
    assert aapa.market_category() == MICMarketCategory.ApprovedPublicationArrangement
    assert xlgt.market_category() == MICMarketCategory.SystematicInternaliser

    assert VenueRegulatoryFlag.Multilateral in bmtf.regulatory_flags()
    assert VenueRegulatoryFlag.OrganizedTrading in afsa.regulatory_flags()
    assert VenueRegulatoryFlag.TradeReporting in finn.regulatory_flags()
    assert VenueRegulatoryFlag.SwapExecution in asef.regulatory_flags()
    assert VenueRegulatoryFlag.Publication in aapa.regulatory_flags()
    assert VenueRegulatoryFlag.SystematicInternaliser in xlgt.regulatory_flags()

    assert bmtf in exchange_records_by_market_category_type(MICMarketCategory.MultilateralTradingFacility)
    assert afsa in exchange_records_by_regulatory_flag(VenueRegulatoryFlag.OrganizedTrading)
    assert finn in exchange_records_by_regulatory_flag(VenueRegulatoryFlag.TradeReporting)
    assert asef in exchange_records_by_regulatory_flag(VenueRegulatoryFlag.SwapExecution)
    assert aapa in exchange_records_by_regulatory_flag(VenueRegulatoryFlag.Publication)
    assert xlgt in exchange_records_by_regulatory_flag(VenueRegulatoryFlag.SystematicInternaliser)


def test_cfi_classification_supports_structured_round_trip_and_validation():
    listed_option = parse_cfi("OCASPS")

    assert build_cfi_from_classification(listed_option) == "OCASPS"
    assert listed_option.to_code() == "OCASPS"
    assert validate_cfi_classification(listed_option) == listed_option
    assert listed_option.validate() == listed_option

    invalid = replace(listed_option, code="OPESCS")

    with pytest.raises(ValueError, match="does not match"):
        validate_cfi_classification(invalid)
