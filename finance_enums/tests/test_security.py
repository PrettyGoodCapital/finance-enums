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
    InstrumentType,
    LegRole,
    MutualFundEndedness,
    OptionExerciseType,
    OptionType,
    PayoffStyle,
    PerpetualFutureType,
    SecurityType,
    SettlementType,
    SwapType,
    UnderlyingAssetClass,
)


class TestSecurityType:
    def test_security_type_basic(self):
        assert len(SecurityType) == 16

    def test_instrument_type_basic(self):
        assert len(InstrumentType) == 11

    def test_equity_type_basic(self):
        assert len(EquityType) == 8

    def test_option_type_basic(self):
        assert len(OptionType) == 2

    def test_bond_type_basic(self):
        assert len(BondType) == 3

    def test_commodity_type_basic(self):
        assert len(CommodityType) == 8

    def test_fund_type_basic(self):
        assert len(FundType) == 3

    def test_swap_type_basic(self):
        assert len(SwapType) == 6

    def test_financing_type_basic(self):
        assert len(FinancingType) == 3

    def test_perpetual_future_type_basic(self):
        assert len(PerpetualFutureType) == 2

    def test_option_exercise_type_basic(self):
        assert len(OptionExerciseType) == 3

    def test_settlement_type_basic(self):
        assert len(SettlementType) == 7

    def test_delivery_type_basic(self):
        assert len(DeliveryType) == 8

    def test_underlying_asset_class_basic(self):
        assert len(UnderlyingAssetClass) == 24

    def test_contract_style_basic(self):
        assert len(ContractStyle) == 2

    def test_payoff_style_basic(self):
        assert len(PayoffStyle) == 3

    def test_contract_unit_basic(self):
        assert len(ContractUnit) == 6

    def test_leg_role_basic(self):
        assert len(LegRole) == 4

    def test_fund_subtype_basic(self):
        assert len(FundSubType) == 4

    def test_mutual_fund_endedness_basic(self):
        assert len(MutualFundEndedness) == 2
