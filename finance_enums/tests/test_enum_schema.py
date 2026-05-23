import json
from enum import Enum

import finance_enums as fe
from finance_enums import (
    EnumFamilySchema,
    EnumVariantRecord,
    enum_family_schemas,
    enum_schema,
    enum_schema_json,
    enum_variant_records,
)


def test_enum_variant_records_cover_rust_backed_enum_families():
    records = enum_variant_records()

    assert EnumVariantRecord(enum_name="Side", variant="Buy", ordinal=1) in records
    assert EnumVariantRecord(enum_name="SettlementStatus", variant="Settled", ordinal=4) in records
    assert EnumVariantRecord(enum_name="BenchmarkType", variant="InterestRate", ordinal=0) in records


def test_enum_family_schemas_describe_python_rust_json_arrow_and_c_abi_exports():
    schemas = {schema.name: schema for schema in enum_family_schemas()}

    assert isinstance(schemas["Side"], EnumFamilySchema)
    assert schemas["Side"].python_symbol == "Side"
    assert schemas["Side"].rust_static == "Side_VARIANTS"
    assert schemas["Side"].json_type == "string"
    assert schemas["Side"].arrow_type == "dictionary<utf8>"
    assert schemas["Side"].c_abi_family == "Side"
    assert schemas["Side"].variants == ("None", "Buy", "Sell")

    assert "BenchmarkType" in schemas
    assert "ClearingModel" in schemas


def test_enum_schema_json_is_stable_and_versioned():
    schema = enum_schema()
    payload = json.loads(enum_schema_json())

    assert schema["schema_version"] == 1
    assert schema["exports"]["c_abi"] == "finance_enums_enum_export_v1"
    assert payload["schema_version"] == schema["schema_version"]
    assert payload["families"] == schema["families"]


def test_enum_family_schemas_cover_public_python_enum_surface():
    c_abi_families = {schema.name for schema in enum_family_schemas()}
    public_python_enums = {name for name, symbol in vars(fe).items() if name in fe.__all__ and isinstance(symbol, type) and issubclass(symbol, Enum)}

    # Frequency is maintained as a Python helper enum and is not sourced from the Rust C ABI table.
    public_python_enums.discard("Frequency")

    missing_in_c_abi = public_python_enums - c_abi_families
    unexpected_c_abi_families = c_abi_families - public_python_enums

    assert missing_in_c_abi == set()
    assert unexpected_c_abi_families == set()
