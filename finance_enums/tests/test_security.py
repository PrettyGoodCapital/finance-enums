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
        assert len(SecurityType.__members__) == 14

    def test_instrument_type_basic(self):
        assert len(InstrumentType.__members__) == 10

    def test_equity_type_basic(self):
        assert len(EquityType.__members__) == 5

    def test_option_type_basic(self):
        assert len(OptionType.__members__) == 2

    def test_bond_type_basic(self):
        assert len(BondType.__members__) == 3

    def test_commodity_type_basic(self):
        assert len(CommodityType.__members__) == 3

    def test_fund_type_basic(self):
        assert len(FundType.__members__) == 3

    def test_swap_type_basic(self):
        assert len(SwapType.__members__) == 6

    def test_financing_type_basic(self):
        assert len(FinancingType.__members__) == 3

    def test_perpetual_future_type_basic(self):
        assert len(PerpetualFutureType.__members__) == 2

    def test_option_exercise_type_basic(self):
        assert len(OptionExerciseType.__members__) == 3

    def test_settlement_type_basic(self):
        assert len(SettlementType.__members__) == 4

    def test_delivery_type_basic(self):
        assert len(DeliveryType.__members__) == 8

    def test_underlying_asset_class_basic(self):
        assert len(UnderlyingAssetClass.__members__) == 24

    def test_contract_style_basic(self):
        assert len(ContractStyle.__members__) == 2

    def test_payoff_style_basic(self):
        assert len(PayoffStyle.__members__) == 3

    def test_contract_unit_basic(self):
        assert len(ContractUnit.__members__) == 6

    def test_leg_role_basic(self):
        assert len(LegRole.__members__) == 4

    def test_fund_subtype_basic(self):
        assert len(FundSubType.__members__) == 4

    def test_mutual_fund_endedness_basic(self):
        assert len(MutualFundEndedness.__members__) == 2
