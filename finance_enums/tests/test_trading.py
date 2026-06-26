import pytest

from finance_enums import (
    OrderFlag,
    OrderType,
    PositionEffect,
    PositionType,
    Side,
    TimeInForce,
    transaction_intent,
    transaction_intent_records,
)


class TestCurrency:
    def test_order_type_basic(self):
        assert len(OrderType) == 8
        assert {"StopLimit", "MarketOnClose", "LimitOnClose", "Pegged"}.issubset(OrderType.__members__)

    def test_side_basic(self):
        assert len(Side) == 4

    def test_time_in_force_basic(self):
        assert len(TimeInForce) == 9
        assert {"ImmediateOrCancel", "FillOrKill", "GoodTillDate", "AtOpen", "AtClose"}.issubset(TimeInForce.__members__)

    def test_order_flag_basic(self):
        assert len(OrderFlag) == 5


def test_side_remains_direction_only_without_position_intent_aliases():
    assert set(Side.__members__) == {"Invalid", "None", "Buy", "Sell"}
    assert "Short" not in Side.__members__
    assert "Cover" not in Side.__members__


@pytest.mark.parametrize(
    ("intent", "side", "position_effect", "position_type"),
    [
        ("open_long", Side.Buy, PositionEffect.Open, PositionType.Long),
        ("close_long", Side.Sell, PositionEffect.Close, PositionType.Long),
        ("open_short", Side.Sell, PositionEffect.Open, PositionType.Short),
        ("cover_short", Side.Buy, PositionEffect.Close, PositionType.Short),
    ],
)
def test_transaction_intent_helper_maps_common_position_intents(intent, side, position_effect, position_type):
    record = transaction_intent(intent)

    assert record.name == intent
    assert record.side == side
    assert record.position_effect == position_effect
    assert record.position_type == position_type


def test_transaction_intent_records_are_stable_and_defensive():
    records = transaction_intent_records()

    assert [record.name for record in records] == ["open_long", "close_long", "open_short", "cover_short"]
    assert transaction_intent("Cover Short") == records[3]
    with pytest.raises(ValueError, match="unknown transaction intent"):
        transaction_intent("sell_short")
