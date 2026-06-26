from finance_enums import (
    BondType,
    CommodityType,
    ContractStyle,
    ContractUnit,
    DeliveryType,
    EquityType,
    FinancingType,
    FundSubType,
    FundType,
    FutureAssetClass,
    InstrumentType,
    LegRole,
    MutualFundEndedness,
    OptionExerciseType,
    OptionType,
    PayoffStyle,
    SecurityType,
    SettlementType,
    SwapType,
    UnderlyingAssetClass,
)


class TestSecurityType:
    def test_security_type_basic(self):
        assert len(SecurityType) == 17

    def test_instrument_type_basic(self):
        assert len(InstrumentType) == 12

    def test_equity_type_basic(self):
        assert len(EquityType) == 9

    def test_option_type_basic(self):
        assert len(OptionType) == 3

    def test_bond_type_basic(self):
        assert len(BondType) == 4

    def test_commodity_type_basic(self):
        assert len(CommodityType) == 9

    def test_fund_type_basic(self):
        assert len(FundType) == 4

    def test_swap_type_basic(self):
        assert len(SwapType) == 7

    def test_financing_type_basic(self):
        assert len(FinancingType) == 4

    def test_future_asset_class_basic(self):
        assert len(FutureAssetClass) == 3

    def test_option_exercise_type_basic(self):
        assert len(OptionExerciseType) == 4

    def test_settlement_type_basic(self):
        assert len(SettlementType) == 8

    def test_delivery_type_basic(self):
        assert len(DeliveryType) == 9

    def test_underlying_asset_class_basic(self):
        assert len(UnderlyingAssetClass) == 25

    def test_contract_style_basic(self):
        assert len(ContractStyle) == 3

    def test_payoff_style_basic(self):
        assert len(PayoffStyle) == 4

    def test_contract_unit_basic(self):
        assert len(ContractUnit) == 7

    def test_leg_role_basic(self):
        assert len(LegRole) == 5

    def test_fund_subtype_basic(self):
        assert len(FundSubType) == 5

    def test_mutual_fund_endedness_basic(self):
        assert len(MutualFundEndedness) == 3
