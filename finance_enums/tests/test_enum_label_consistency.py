import re
from enum import Enum

import finance_enums
from finance_enums import IdentifierType, Symbology

_CODE_ENUMS = {"CountryCodeAlpha2", "CountryCodeAlpha3", "Currency", "ExchangeCode", "Symbology"}
_ACRONYM_RE = re.compile(r"[A-Z]{2,}")


def _enum_families() -> list[tuple[str, type[Enum]]]:
    return [
        (name, enum_type)
        for name in finance_enums.__all__
        if isinstance(enum_type := getattr(finance_enums, name, None), type) and issubclass(enum_type, Enum)
    ]


def test_enum_family_names_use_expanded_pascal_case():
    offenders = [name for name, _ in _enum_families() if _ACRONYM_RE.search(name)]

    assert offenders == []


def test_non_code_enum_values_use_expanded_pascal_case_labels():
    offenders: list[str] = []

    for name, enum_type in _enum_families():
        if name in _CODE_ENUMS:
            continue

        for member in enum_type:
            value = member.name
            if isinstance(value, str) and (_ACRONYM_RE.search(value) or "PnL" in value):
                offenders.append(f"{name}.{member.name}={value}")

    assert offenders == []


def test_symbology_is_one_to_one_with_identifier_type():
    assert len(Symbology) == len(IdentifierType)
    for acronym, full in zip(Symbology, IdentifierType, strict=True):
        assert acronym.value == full.value
        assert IdentifierType(acronym.name) is full
