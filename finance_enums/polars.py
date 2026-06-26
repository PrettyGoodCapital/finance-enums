"""Polars Enum dtype integration for finance_enums.

Provides pre-built ``pl.Enum(...)`` dtypes for every enum family, so you can use
them directly as column types in Polars DataFrames:

    >>> import polars as pl
    >>> from finance_enums.polars import CurrencyDtype, SideDtype
    >>> df = pl.DataFrame({"ccy": ["USD", "EUR"]}, schema={"ccy": CurrencyDtype})

Each dtype is a ``pl.Enum`` whose categories match the variant list (and ordinal
positions) from the canonical Rust source.
"""

from __future__ import annotations

import polars as pl

from .finance_enums import __all_families__, enums

# Build a pl.Enum dtype for every family
# e.g. CurrencyDtype = pl.Enum(["AED", "AFN", ..., "ZWL"])
for _name in __all_families__:
    _variants = list(getattr(enums, _name))
    globals()[f"{_name}Dtype"] = pl.Enum(_variants)

del _name, _variants

__all__ = [f"{name}Dtype" for name in __all_families__]
