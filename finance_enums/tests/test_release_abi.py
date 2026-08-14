from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import finance_enums as fe

ROOT = Path(__file__).resolve().parents[2]
SNAPSHOT_PATH = ROOT / "reference_snapshots" / "abi.json"

NEW_ACTIVE_MICS = (
    "ASPC",
    "ASPV",
    "BTRE",
    "BTRG",
    "BUGI",
    "CODX",
    "CPRM",
    "CXAL",
    "DBAO",
    "GATE",
    "GXIL",
    "HAMX",
    "HAMY",
    "HAMZ",
    "ICOD",
    "IEXO",
    "INCC",
    "JPPM",
    "MSCC",
    "OBGP",
    "OKXE",
    "OMET",
    "OPTM",
    "PAYM",
    "PFSI",
    "PFTO",
    "RMEX",
    "SIG2",
    "SIGB",
    "UBSV",
    "UTST",
    "WBDP",
    "XGPS",
    "XGRW",
    "XLOX",
)


def _snapshot() -> dict:
    return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))


def _sha256_lines(values: list[str]) -> str:
    return hashlib.sha256("\n".join(values).encode()).hexdigest()


def _c_struct_declarations(header: str, name: str) -> list[str]:
    match = re.search(rf"typedef struct {name} \{{(.*?)\}} {name};", header, re.DOTALL)
    assert match is not None
    body = re.sub(r"/\*.*?\*/", "", match.group(1), flags=re.DOTALL)
    return [" ".join(declaration.split()) for declaration in body.split(";") if declaration.strip()]


def test_release_abi_snapshot_matches_runtime() -> None:
    snapshot = _snapshot()

    assert fe.__version__ == snapshot["release"]
    assert list(fe.abi_version()) == snapshot["semantic_abi"]
    assert len(fe.enum_family_schemas()) == snapshot["family_count"]
    assert len(fe.enum_variant_records()) == snapshot["variant_count"]
    assert hashlib.sha256(fe.enum_schema_json().encode()).hexdigest() == snapshot["enum_schema_sha256"]


def test_release_family_prefixes_remain_compatible() -> None:
    prefix = _snapshot()["family_prefix"]
    families = {family.name: family.variants for family in fe.enum_family_schemas()}
    values: list[str] = []

    for name, count in sorted(prefix["counts"].items()):
        assert name in families
        assert len(families[name]) >= count
        values.append(name)
        values.extend(families[name][:count])

    assert _sha256_lines(values) == prefix["sha256"]


def test_beta_c_abi_layout_matches_snapshot() -> None:
    c_abi = _snapshot()["c_abi"]
    header = (ROOT / "finance_enums/include/finance_enums.h").read_text(encoding="utf-8")
    declarations: list[str] = []

    assert c_abi["stability"] == "beta"
    for export, version in c_abi["export_versions"].items():
        macro = f"FINANCE_ENUMS_{export.upper()}_EXPORT_ABI_VERSION {version}u"
        assert macro in header
    for struct, fields in c_abi["struct_fields"].items():
        struct_declarations = _c_struct_declarations(header, struct)
        assert [declaration.split()[-1].lstrip("*") for declaration in struct_declarations] == fields
        declarations.append(struct)
        declarations.extend(struct_declarations)
    assert _sha256_lines(declarations) == c_abi["struct_declarations_sha256"]


def test_release_version_is_synchronized_across_artifacts() -> None:
    version = _snapshot()["release"]

    assert f'version = "{version}"' in (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert f'version = "{version}"' in (ROOT / "Cargo.toml").read_text(encoding="utf-8")
    assert f'version = "{version}"' in (ROOT / "rust" / "Cargo.toml").read_text(encoding="utf-8")
    assert json.loads((ROOT / "vcpkg.json").read_text(encoding="utf-8"))["version"] == version
    assert json.loads((ROOT / "ports" / "finance-enums" / "vcpkg.json").read_text(encoding="utf-8"))["version"] == version
    assert f"version: {version}" in (ROOT / "conda" / "recipe.yaml").read_text(encoding="utf-8")
    cmake = (ROOT / "CMakeLists.txt").read_text(encoding="utf-8")
    assert re.search(rf"project\(finance-enums\s+VERSION {re.escape(version)}", cmake)


def test_beta_cmake_package_requires_same_minor_version() -> None:
    snapshot = _snapshot()
    cmake = (ROOT / "CMakeLists.txt").read_text(encoding="utf-8")

    assert snapshot["semantic_abi"][0] == 0
    assert "COMPATIBILITY SameMinorVersion" in cmake


def test_beta_minor_declares_published_v0_6_ordinal_break() -> None:
    previous = _snapshot()["previous_release"]

    assert fe.abi_compatible(*previous["semantic_abi"][:2]) is False
    assert fe.ordinal_of("Side", "Buy") != previous["representative_ordinals"]["Side.Buy"]
    assert fe.ordinal_of("Currency", "USD") != previous["representative_ordinals"]["Currency.USD"]


def test_new_mics_are_an_append_only_extension() -> None:
    snapshot = _snapshot()["exchange_prefix"]
    variants = [member.name for member in fe.ExchangeCode]

    assert _sha256_lines(variants[: snapshot["count"]]) == snapshot["sha256"]
    assert tuple(variants[snapshot["count"] :]) == NEW_ACTIVE_MICS
    for mic in NEW_ACTIVE_MICS:
        assert fe.exchange_record(mic).is_official is True
