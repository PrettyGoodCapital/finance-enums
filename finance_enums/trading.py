"""Trading-intent helpers built from the order/position enum families.

A :class:`TransactionIntent` bundles the canonical (side, position effect,
position type) tuple for the four basic equity transactions.
"""

from __future__ import annotations

from dataclasses import dataclass

from ._finance_enums import int_enums as _int_enums

__all__ = [
    "TransactionIntent",
    "transaction_intent",
    "transaction_intent_records",
]

Side = _int_enums.Side
PositionEffect = _int_enums.PositionEffect
PositionType = _int_enums.PositionType


@dataclass(frozen=True)
class TransactionIntent:
    name: str
    side: Side
    position_effect: PositionEffect
    position_type: PositionType


_TRANSACTION_INTENT_RECORDS = (
    TransactionIntent("open_long", Side.Buy, PositionEffect.Open, PositionType.Long),
    TransactionIntent("close_long", Side.Sell, PositionEffect.Close, PositionType.Long),
    TransactionIntent("open_short", Side.Sell, PositionEffect.Open, PositionType.Short),
    TransactionIntent("cover_short", Side.Buy, PositionEffect.Close, PositionType.Short),
)
_TRANSACTION_INTENT_BY_NAME = {record.name: record for record in _TRANSACTION_INTENT_RECORDS}


def _normalize_transaction_intent_name(value: str) -> str:
    return str(value).strip().lower().replace("-", "_").replace(" ", "_")


def transaction_intent_records() -> list[TransactionIntent]:
    return list(_TRANSACTION_INTENT_RECORDS)


def transaction_intent(intent: TransactionIntent | str) -> TransactionIntent:
    if isinstance(intent, TransactionIntent):
        return intent

    normalized = _normalize_transaction_intent_name(intent)
    try:
        return _TRANSACTION_INTENT_BY_NAME[normalized]
    except KeyError as exc:
        raise ValueError(f"unknown transaction intent: {intent!r}") from exc
