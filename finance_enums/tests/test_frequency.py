import pytest

from finance_enums import Frequency, to_frequency


def test_frequency_aliases_and_properties():
    assert to_frequency(Frequency.Day) is Frequency.Day
    assert to_frequency("D") is Frequency.Day
    assert to_frequency(" weekly ") is Frequency.Week
    assert to_frequency("1mo") is Frequency.Month
    assert to_frequency("quarterly") is Frequency.Quarter
    assert to_frequency("annually") is Frequency.Year

    assert Frequency.Day.periods_per_year == 252
    assert Frequency.Week.periods_per_year == 52
    assert Frequency.Month.periods_per_year == 12
    assert Frequency.Quarter.periods_per_year == 4
    assert Frequency.Year.periods_per_year == 1

    assert Frequency.Day.polars_truncate == "1d"
    assert Frequency.Week.polars_truncate == "1w"
    assert Frequency.Month.polars_truncate == "1mo"
    assert Frequency.Quarter.polars_truncate == "1q"
    assert Frequency.Year.polars_truncate == "1y"

    with pytest.raises(ValueError, match="Unknown frequency"):
        to_frequency("fortnight")
