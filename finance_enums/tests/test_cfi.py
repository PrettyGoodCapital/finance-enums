from dataclasses import replace

import pytest

from finance_enums import (
    BondType,
    CommodityType,
    ContractStyle,
    DeliveryType,
    FinancingType,
    FundType,
    FutureDeliveryType,
    FutureType,
    InstrumentType,
    MutualFundEndedness,
    OptionExerciseType,
    OptionType,
    PerpetualFutureType,
    SecurityType,
    SettlementType,
    SwapType,
    UnderlyingAssetClass,
    build_cfi,
    build_cfi_from_classification,
    parse_cfi,
    validate_cfi_classification,
)


class TestCFI:
    def test_parse_equity_cfi(self):
        classification = parse_cfi("ESVUFB")

        assert classification.security_type == SecurityType.Equity
        assert classification.equity_type.value == "Shares"
        assert classification.attributes == ("V", "U", "F", "B")

    def test_parse_option_cfi(self):
        classification = parse_cfi("OCAPXS")

        assert classification.security_type == SecurityType.Option
        assert classification.option_type == OptionType.Call
        assert classification.option_exercise_type == OptionExerciseType.American

    def test_build_equity_cfi_defaults_to_common_share(self):
        assert build_cfi(security_type=SecurityType.Equity) == "ESXXXX"

    def test_build_option_cfi_uses_known_exercise_style(self):
        assert (
            build_cfi(
                security_type=SecurityType.Option,
                option_type=OptionType.Put,
                option_exercise_type=OptionExerciseType.European,
            )
            == "OPEXXX"
        )

    def test_build_bond_fund_and_future_cfis(self):
        assert build_cfi(security_type=SecurityType.Bond, bond_type=BondType.Government) == "DBXTXX"
        assert (
            build_cfi(
                security_type=SecurityType.Fund,
                fund_type=FundType.MutualFund,
                mutual_fund_endedness=MutualFundEndedness.Open,
            )
            == "CIOXXX"
        )
        assert (
            build_cfi(
                security_type=SecurityType.Future,
                future_type=FutureType.Commodity,
                future_delivery_type=FutureDeliveryType.Physical,
            )
            == "FCXPXX"
        )

    def test_parse_fund_and_future_cfis(self):
        fund = parse_cfi("CIOIYU")
        future = parse_cfi("FFXCXS")

        assert fund.security_type == SecurityType.Fund
        assert fund.fund_type == FundType.MutualFund
        assert fund.mutual_fund_endedness == MutualFundEndedness.Open
        assert future.security_type == SecurityType.Future
        assert future.future_type == FutureType.Financial
        assert future.future_delivery_type == FutureDeliveryType.Cash

    def test_parse_spot_forward_spread_and_index_cfis(self):
        spot_fx = parse_cfi("IFXXXP")
        spot_commodity = parse_cfi("ITAXXX")
        forward_fx = parse_cfi("JFXXXX")
        commodity_strategy = parse_cfi("KTXXXX")
        index = parse_cfi("TIXXXX")

        assert spot_fx.security_type == SecurityType.Currency
        assert spot_fx.instrument_type == InstrumentType.Spot
        assert spot_commodity.security_type == SecurityType.Commodity
        assert spot_commodity.commodity_type == CommodityType.Agriculture
        assert forward_fx.security_type == SecurityType.Forward
        assert forward_fx.instrument_type == InstrumentType.Forward
        assert forward_fx.underlying_security_type == SecurityType.Currency
        assert commodity_strategy.security_type == SecurityType.Spread
        assert commodity_strategy.instrument_type == InstrumentType.Spread
        assert commodity_strategy.underlying_security_type == SecurityType.Commodity
        assert index.security_type == SecurityType.Index

    def test_build_spot_forward_spread_and_index_cfis(self):
        assert build_cfi(security_type=SecurityType.Currency) == "IFXXXP"
        assert build_cfi(security_type=SecurityType.Commodity, commodity_type=CommodityType.Agriculture) == "ITAXXX"
        assert build_cfi(security_type=SecurityType.Forward, underlying_security_type=SecurityType.Currency) == "JFXXXX"
        assert build_cfi(security_type=SecurityType.Spread, underlying_security_type=SecurityType.Commodity) == "KTXXXX"
        assert build_cfi(security_type=SecurityType.Index) == "TIXXXX"

    def test_parse_derivative_attribute_enums_from_cfi(self):
        listed_option = parse_cfi("OCASPS")
        financial_future = parse_cfi("FFICSX")
        commodity_future = parse_cfi("FCAPSX")
        complex_option = parse_cfi("HRXXXX")
        rates_forward = parse_cfi("JRXXXX")
        mixed_strategy = parse_cfi("KYXXXX")

        assert listed_option.underlying_asset_class == UnderlyingAssetClass.Equity
        assert listed_option.delivery_type == DeliveryType.Physical
        assert listed_option.settlement_type == SettlementType.Physical
        assert listed_option.contract_style == ContractStyle.Standardized

        assert financial_future.future_type == FutureType.Financial
        assert financial_future.underlying_asset_class == UnderlyingAssetClass.Index
        assert financial_future.delivery_type == DeliveryType.Cash
        assert financial_future.settlement_type == SettlementType.Cash
        assert financial_future.contract_style == ContractStyle.Standardized

        assert commodity_future.future_type == FutureType.Commodity
        assert commodity_future.commodity_type == CommodityType.Agriculture
        assert commodity_future.underlying_asset_class == UnderlyingAssetClass.Agriculture

        assert complex_option.security_type == SecurityType.Option
        assert complex_option.underlying_asset_class == UnderlyingAssetClass.InterestRate
        assert rates_forward.security_type == SecurityType.Forward
        assert rates_forward.underlying_asset_class == UnderlyingAssetClass.InterestRate
        assert mixed_strategy.security_type == SecurityType.Spread
        assert mixed_strategy.underlying_asset_class == UnderlyingAssetClass.MixedAssets

    def test_build_derivative_cfis_with_typed_attribute_enums(self):
        assert (
            build_cfi(
                security_type=SecurityType.Option,
                option_type=OptionType.Call,
                option_exercise_type=OptionExerciseType.American,
                underlying_asset_class=UnderlyingAssetClass.Equity,
                settlement_type=SettlementType.Physical,
                contract_style=ContractStyle.Standardized,
            )
            == "OCASPS"
        )
        assert (
            build_cfi(
                security_type=SecurityType.Future,
                future_type=FutureType.Financial,
                underlying_asset_class=UnderlyingAssetClass.Index,
                settlement_type=SettlementType.Cash,
                contract_style=ContractStyle.Standardized,
            )
            == "FFICSX"
        )
        assert (
            build_cfi(
                security_type=SecurityType.Future,
                future_type=FutureType.Commodity,
                commodity_type=CommodityType.Agriculture,
                delivery_type=DeliveryType.Physical,
                contract_style=ContractStyle.Standardized,
            )
            == "FCAPSX"
        )
        assert build_cfi(security_type=SecurityType.Option, underlying_asset_class=UnderlyingAssetClass.InterestRate) == "HRXXXX"
        assert build_cfi(security_type=SecurityType.Forward, underlying_asset_class=UnderlyingAssetClass.InterestRate) == "JRXXXX"
        assert build_cfi(security_type=SecurityType.Spread, underlying_asset_class=UnderlyingAssetClass.MixedAssets) == "KYXXXX"

    def test_build_raw_cfi_for_unmodeled_iso_categories(self):
        assert build_cfi(category="L", group="R", attributes="GDXD") == "LRGDXD"

    def test_parse_swap_and_financing_cfis(self):
        swap = parse_cfi("SFXXXX")
        financing = parse_cfi("LRGDXD")

        assert swap.security_type == SecurityType.Swap
        assert swap.instrument_type == InstrumentType.Swap
        assert swap.swap_type == SwapType.ForeignExchange
        assert financing.security_type == SecurityType.Financing
        assert financing.instrument_type == InstrumentType.Financing
        assert financing.financing_type == FinancingType.RepurchaseAgreement
        assert financing.attributes == ("G", "D", "X", "D")

    def test_build_swap_financing_and_perpetual_future_cfis(self):
        assert build_cfi(security_type=SecurityType.Swap, swap_type=SwapType.ForeignExchange) == "SFXXXX"
        assert build_cfi(security_type=SecurityType.Financing, financing_type=FinancingType.SecuritiesLending) == "LSXXXX"
        assert (
            build_cfi(
                security_type=SecurityType.PerpetualFuture,
                perpetual_future_type=PerpetualFutureType.Commodity,
                future_delivery_type=FutureDeliveryType.Cash,
            )
            == "FCXCXX"
        )

    def test_perpetual_future_cfi_uses_standard_future_envelope(self):
        classification = parse_cfi(
            build_cfi(
                security_type=SecurityType.PerpetualFuture,
                perpetual_future_type=PerpetualFutureType.Financial,
                future_delivery_type=FutureDeliveryType.Cash,
            )
        )

        assert classification.security_type == SecurityType.Future
        assert classification.instrument_type == InstrumentType.Future
        assert classification.future_type == FutureType.Financial

    def test_build_cfi_rejects_unsupported_security_types(self):
        with pytest.raises(NotImplementedError):
            build_cfi(security_type=SecurityType.Pair)

    def test_raw_cfi_inputs_are_normalized_and_validated(self):
        assert build_cfi(category=" t ", group=" i ", attributes=("x", "x", "x", "x")) == "TIXXXX"
        assert parse_cfi(" dnxxxx ").bond_type == BondType.Municipal
        assert parse_cfi("DBXTXX").bond_type == BondType.Government
        assert parse_cfi("CICXXX").mutual_fund_endedness == MutualFundEndedness.Close
        assert parse_cfi("TCXXXX").security_type == SecurityType.Currency
        assert parse_cfi("TTXXXX").security_type == SecurityType.Commodity
        assert parse_cfi("TBXXXX").instrument_type == InstrumentType.Basket
        assert parse_cfi("TDXXXX").security_type == SecurityType.Equity
        assert parse_cfi("RXXXXX").instrument_type == InstrumentType.Right

        with pytest.raises(ValueError, match="exactly 6"):
            parse_cfi("ABC")
        with pytest.raises(ValueError, match="category and group"):
            build_cfi(category="E", attributes="XXXX")
        with pytest.raises(ValueError, match="exactly 4"):
            build_cfi(category="E", group="S", attributes="XXX")
        with pytest.raises(ValueError, match="contain exactly 4"):
            build_cfi(category="E", group="S", attributes=("X", "X"))

    def test_cfi_typed_inputs_are_validated(self):
        with pytest.raises(ValueError, match="invalid security_type"):
            build_cfi(security_type="NotAType")
        with pytest.raises(ValueError, match="listed option"):
            build_cfi(security_type=SecurityType.Option)
        with pytest.raises(ValueError, match="different underliers"):
            build_cfi(
                security_type=SecurityType.Forward,
                underlying_asset_class=UnderlyingAssetClass.Equity,
                underlying_security_type=SecurityType.Currency,
            )
        with pytest.raises(ValueError, match="settlement_type and delivery_type"):
            build_cfi(
                security_type=SecurityType.Future,
                settlement_type=SettlementType.Cash,
                delivery_type=DeliveryType.Physical,
            )
        with pytest.raises(ValueError, match="future_delivery_type"):
            build_cfi(
                security_type=SecurityType.Future,
                settlement_type=SettlementType.Cash,
                future_delivery_type=FutureDeliveryType.Physical,
            )
        with pytest.raises(ValueError, match="swap_type"):
            build_cfi(security_type=SecurityType.Swap)
        with pytest.raises(ValueError, match="financing_type"):
            build_cfi(security_type=SecurityType.Financing)
        with pytest.raises(ValueError, match="forward CFI"):
            build_cfi(security_type=SecurityType.Forward)
        with pytest.raises(ValueError, match="spread CFI"):
            build_cfi(security_type=SecurityType.Spread)

    def test_cfi_unsupported_underliers_and_classification_fallbacks(self):
        with pytest.raises(NotImplementedError, match="complex option"):
            build_cfi(security_type=SecurityType.Option, underlying_asset_class=UnderlyingAssetClass.Index)
        with pytest.raises(NotImplementedError, match="forward"):
            build_cfi(security_type=SecurityType.Forward, underlying_asset_class=UnderlyingAssetClass.Index)
        with pytest.raises(NotImplementedError, match="spread"):
            build_cfi(security_type=SecurityType.Spread, underlying_asset_class=UnderlyingAssetClass.Index)
        with pytest.raises(NotImplementedError, match="asset-class resolution"):
            build_cfi(security_type=SecurityType.Future, underlying_security_type=SecurityType.Pair)

        forward = replace(
            parse_cfi("JRXXXX"),
            code="JIXXXX",
            group="I",
            underlying_asset_class=UnderlyingAssetClass.Index,
            underlying_security_type=SecurityType.Index,
        )
        assert build_cfi_from_classification(forward) == "JIXXXX"

        option = parse_cfi("OCASPS")
        with pytest.raises(TypeError, match="classification"):
            build_cfi_from_classification("OCASPS")
        with pytest.raises(TypeError, match="classification"):
            validate_cfi_classification("OCASPS")
        with pytest.raises(ValueError, match="typed fields"):
            validate_cfi_classification(replace(option, option_type=OptionType.Put))
