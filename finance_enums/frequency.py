"""Calendar-frequency enum shared by all finance-* libraries.

This is the canonical location for the ``period`` / ``window`` argument
values used across ``finance-calcs``, ``finance-plots``, ``finance-etl``,
and ``finance-dates``. Any function that takes a calendar-aware
``period=`` or ``window=`` argument should accept either a
:class:`Frequency` member or one of the string aliases below.
"""

from __future__ import annotations

from enum import Enum

__all__ = ["Frequency", "to_frequency"]


class Frequency(str, Enum):
    """Canonical calendar frequency.

    The string value is the lower-case canonical alias; additional
    aliases are accepted by :func:`to_frequency` (e.g. ``"D"``,
    ``"daily"``, ``"M"``, ``"monthly"``, ``"yearly"``).
    """

    Day = "day"
    Week = "week"
    Month = "month"
    Quarter = "quarter"
    Year = "year"

    @property
    def periods_per_year(self) -> int:
        """Approximate number of periods per year for annualisation."""
        return {
            Frequency.Day: 252,
            Frequency.Week: 52,
            Frequency.Month: 12,
            Frequency.Quarter: 4,
            Frequency.Year: 1,
        }[self]

    @property
    def polars_truncate(self) -> str:
        """Polars ``dt.truncate`` rule string for bucketing dates."""
        return {
            Frequency.Day: "1d",
            Frequency.Week: "1w",
            Frequency.Month: "1mo",
            Frequency.Quarter: "1q",
            Frequency.Year: "1y",
        }[self]


_ALIASES: dict[str, Frequency] = {
    # Day
    "d": Frequency.Day, "day": Frequency.Day, "daily": Frequency.Day,
    "1d": Frequency.Day,
    # Week
    "w": Frequency.Week, "week": Frequency.Week, "weekly": Frequency.Week,
    "1w": Frequency.Week,
    # Month
    "m": Frequency.Month, "mo": Frequency.Month, "month": Frequency.Month,
    "monthly": Frequency.Month, "1mo": Frequency.Month,
    # Quarter
    "q": Frequency.Quarter, "quarter": Frequency.Quarter,
    "quarterly": Frequency.Quarter, "1q": Frequency.Quarter,
    # Year
    "y": Frequency.Year, "year": Frequency.Year, "yearly": Frequency.Year,
    "annual": Frequency.Year, "annually": Frequency.Year, "1y": Frequency.Year,
}


def to_frequency(value: Frequency | str) -> Frequency:
    """Coerce ``value`` to a :class:`Frequency` member.

    Accepts a :class:`Frequency` instance directly, the canonical
    lower-case name, or any of the common aliases listed above.

    Raises:
        ValueError: If ``value`` is not a recognised frequency.
    """
    if isinstance(value, Frequency):
        return value
    if isinstance(value, str):
        key = value.strip().lower()
        if key in _ALIASES:
            return _ALIASES[key]
    raise ValueError(f"Unknown frequency: {value!r}")
