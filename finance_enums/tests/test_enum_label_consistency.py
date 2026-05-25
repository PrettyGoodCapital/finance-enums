import re
from enum import Enum

import finance_enums

_CODE_ENUMS = {"CountryCode", "CountryCode3", "Currency", "ExchangeCode"}
_ACRONYM_RE = re.compile(r"[A-Z]{2,}")


def test_non_code_enum_values_use_expanded_pascal_case_labels():
    offenders: list[str] = []

    for name in finance_enums.__all__:
        enum_type = getattr(finance_enums, name, None)
        if name in _CODE_ENUMS or not isinstance(enum_type, type) or not issubclass(enum_type, Enum):
            continue

        for member in enum_type:
            value = member.value
            if isinstance(value, str) and (_ACRONYM_RE.search(value) or "PnL" in value):
                offenders.append(f"{name}.{member.name}={value}")

    assert offenders == []
