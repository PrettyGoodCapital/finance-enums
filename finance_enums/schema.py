"""Schema / reference-data introspection for the enum families.

These helpers expose the canonical enum families (name, variants, and the
Rust/Python/JSON/Arrow/C-ABI binding metadata) as data. The variant records come
from the native extension, so the schema always matches the compiled enum
families exactly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from .finance_enums import enum_records_raw as _enum_records_raw

__all__ = [
    "EnumFamilySchema",
    "EnumVariantRecord",
    "enum_family_schemas",
    "enum_schema",
    "enum_schema_json",
    "enum_variant_records",
]

_ENUM_SCHEMA_VERSION = 1


@dataclass(frozen=True)
class EnumVariantRecord:
    enum_name: str
    variant: str
    ordinal: int


@dataclass(frozen=True)
class EnumFamilySchema:
    name: str
    rust_static: str
    python_symbol: str
    c_abi_family: str
    json_type: str
    arrow_type: str
    variants: tuple[str, ...]


_ENUM_VARIANT_RECORDS = [EnumVariantRecord(enum_name, variant, ordinal) for enum_name, variant, ordinal in _enum_records_raw()]


def enum_variant_records() -> list[EnumVariantRecord]:
    return list(_ENUM_VARIANT_RECORDS)


def enum_family_schemas() -> list[EnumFamilySchema]:
    families: dict[str, list[str]] = {}
    for record in _ENUM_VARIANT_RECORDS:
        families.setdefault(record.enum_name, []).append(record.variant)

    return [
        EnumFamilySchema(
            name=name,
            rust_static=f"{name}_VARIANTS",
            python_symbol=name,
            c_abi_family=name,
            json_type="string",
            arrow_type="dictionary<utf8>",
            variants=tuple(variants),
        )
        for name, variants in families.items()
    ]


def _enum_family_schema_to_dict(schema: EnumFamilySchema) -> dict[str, Any]:
    return {
        "name": schema.name,
        "rust_static": schema.rust_static,
        "python_symbol": schema.python_symbol,
        "c_abi_family": schema.c_abi_family,
        "json_type": schema.json_type,
        "arrow_type": schema.arrow_type,
        "variants": list(schema.variants),
    }


def enum_schema() -> dict[str, Any]:
    return {
        "schema_version": _ENUM_SCHEMA_VERSION,
        "exports": {
            "rust": "finance_enums::enum_data::enum_family_specs",
            "python": "finance_enums.enum_family_schemas",
            "json": "finance_enums.enum_schema_json",
            "arrow": "dictionary<utf8>",
            "c_abi": "finance_enums_enum_export_v1",
        },
        "families": [_enum_family_schema_to_dict(schema) for schema in enum_family_schemas()],
    }


def enum_schema_json() -> str:
    return json.dumps(enum_schema(), sort_keys=True, separators=(",", ":"))
