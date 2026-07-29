import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _abi_families():
    """``{family: ((variant, ordinal), ...)}`` straight from the runtime C ABI."""
    import finance_enums

    families: dict[str, list[tuple[str, int]]] = {}
    for record in finance_enums.enum_variant_records():
        families.setdefault(record.enum_name, []).append((record.variant, record.ordinal))
    return {name: tuple(sorted(items, key=lambda pair: pair[1])) for name, items in families.items()}


def _generated_header_families(header):
    """Parse the C ``typedef enum`` blocks into ``{family: ((variant, ordinal), ...)}``."""
    families = {}
    for match in re.finditer(r"typedef enum \{(.*?)\}\s*FE_(\w+);", header, re.DOTALL):
        body = match.group(1)
        name = match.group(2)
        pairs = re.findall(rf"\bFE_{name}_(\S+?)\s*=\s*(\d+)", body)
        families[name] = tuple((variant, int(ordinal)) for variant, ordinal in pairs)
    return families


def _generated_cpp_families(header):
    """Parse the C++ ``enum class`` blocks into ``{family: ((enumerator, ordinal), ...)}``."""
    families = {}
    for match in re.finditer(r"enum class (\w+) : size_t \{(.*?)\};", header, re.DOTALL):
        name = match.group(1)
        body = match.group(2)
        pairs = re.findall(r"\b([A-Za-z_]\w*)\s*=\s*(\d+)", body)
        families[name] = tuple((enumerator, int(ordinal)) for enumerator, ordinal in pairs)
    return families


def test_generated_c_header_exists_and_exposes_versioned_exports():
    header_path = Path(__file__).resolve().parents[1] / "include" / "finance_enums.h"
    library_name = {
        "darwin": "libfinance_enums.dylib",
        "linux": "libfinance_enums.so",
        "win32": "finance_enums.dll",
    }[sys.platform]
    library_path = Path(__file__).resolve().parents[1] / "lib" / library_name

    assert header_path.exists()
    assert library_path.exists()

    header = header_path.read_text()

    assert "finance_enums_currency_export_v1" in header
    assert "finance_enums_exchange_export_v1" in header
    assert "finance_enums_enum_export_v1" in header
    assert "CurrencyDataExportV1" in header
    assert "ExchangeDataExportV1" in header
    assert "EnumDataExportV1" in header
    assert "EnumVariantRecordRaw" in header

    # Semantic ABI version macros + compatibility helpers.
    assert "FINANCE_ENUMS_ABI_VERSION_MAJOR" in header
    assert "FINANCE_ENUMS_ABI_VERSION_MINOR" in header
    assert "FINANCE_ENUMS_ABI_VERSION_PATCH" in header
    assert "finance_enums_abi_version" in header
    assert "finance_enums_abi_compatible" in header
    assert "finance_enums_abi_header_compatible" in header

    # Runtime enum helpers.
    assert "finance_enums_family_variant_count" in header
    assert "finance_enums_validate_ordinal" in header
    assert "finance_enums_ordinal_of" in header
    assert "finance_enums_variant_name" in header

    # The export struct must expose max_ordinal (matches the Rust layout).
    assert "max_ordinal" in header


def test_generated_enum_header_matches_runtime_abi():
    header_path = ROOT / "finance_enums" / "include" / "finance_enums_generated.h"
    header = header_path.read_text()
    abi_families = _abi_families()

    # The C macros mirror the ABI (variant name + ordinal) exactly, including the
    # Currency and ExchangeCode families that live outside data.rs.
    assert _generated_header_families(header) == abi_families

    # The C++ enum class carries the same ordinals; enumerators are the variant
    # names, sanitized to be valid identifiers (digit-leading MICs get an "_").
    from finance_enums.gen_enums_header import _cpp_enumerator

    expected_cpp = {name: tuple((_cpp_enumerator(variant), ordinal) for variant, ordinal in items) for name, items in abi_families.items()}
    assert _generated_cpp_families(header) == expected_cpp

    assert {name: int(count) for name, count in re.findall(r"#define FE_(\w+)_COUNT (\d+)u", header)} == {
        name: len(items) for name, items in abi_families.items()
    }


def test_generated_enum_header_is_up_to_date():
    """The committed header must match a fresh regeneration from the ABI."""
    sys.path.insert(0, str(ROOT))
    from finance_enums.gen_enums_header import generate_header, parse_families

    header_path = ROOT / "finance_enums" / "include" / "finance_enums_generated.h"
    expected = generate_header(parse_families())
    assert header_path.read_text(encoding="utf-8") == expected, "run: python finance_enums/gen_enums_header.py"
