import pytest

from finance_enums import (
    OpenClose,
    OrderFlag,
    OrderType,
    PositionEffect,
    PositionType,
    Side,
    TimeInForce,
    TradingType,
    transaction_intent,
    transaction_intent_records,
)


class TestCurrency:
    def test_order_type_basic(self):
        assert len(OrderType.__members__) == 3

    def test_side_basic(self):
        assert len(Side.__members__) == 3

    def test_time_in_force_basic(self):
        assert len(TimeInForce.__members__) == 3

    def test_order_flag_basic(self):
        assert len(OrderFlag.__members__) == 4

    def test_trading_type_basic(self):
        assert len(TradingType.__members__) == 4


def test_side_remains_direction_only_without_position_intent_aliases():
    assert set(Side.__members__) == {"None", "Buy", "Sell"}
    assert "Short" not in Side.__members__
    assert "Cover" not in Side.__members__


@pytest.mark.parametrize(
    ("intent", "side", "position_effect", "open_close", "position_type"),
    [
        ("open_long", Side.Buy, PositionEffect.Open, OpenClose.Open, PositionType.Long),
        ("close_long", Side.Sell, PositionEffect.Close, OpenClose.Close, PositionType.Long),
        ("open_short", Side.Sell, PositionEffect.Open, OpenClose.Open, PositionType.Short),
        ("cover_short", Side.Buy, PositionEffect.Close, OpenClose.Close, PositionType.Short),
    ],
)
def test_transaction_intent_helper_maps_common_position_intents(intent, side, position_effect, open_close, position_type):
    record = transaction_intent(intent)

    assert record.name == intent
    assert record.side == side
    assert record.position_effect == position_effect
    assert record.open_close == open_close
    assert record.position_type == position_type


def test_transaction_intent_records_are_stable_and_defensive():
    records = transaction_intent_records()

    assert [record.name for record in records] == ["open_long", "close_long", "open_short", "cover_short"]
    assert transaction_intent("Cover Short") == records[3]
    with pytest.raises(ValueError, match="unknown transaction intent"):
        transaction_intent("sell_short")
