from __future__ import annotations

import sys
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib

ROOT = Path(__file__).resolve().parents[2]
HEADERS = {
    "finance_enums.h",
    "finance_enums.hpp",
    "finance_enums_convert.hpp",
    "finance_enums_generated.h",
}


def _toml(path: str) -> dict:
    return tomllib.loads((ROOT / path).read_text(encoding="utf-8"))


def test_c_abi_library_is_built_before_the_extension_that_links_it():
    pyproject = _toml("pyproject.toml")
    hooks = pyproject["tool"]["hatch"]["build"]["hooks"]
    hatch_rs = hooks["hatch-rs"]
    artifacts = hatch_rs["artifacts"]

    assert "backend-path" not in pyproject["build-system"]
    assert "custom" not in hooks
    assert hatch_rs["target-dir"] == "isolated"
    assert [artifact["name"] for artifact in artifacts] == ["finance_enums", "_finance_enums"]

    library, extension = artifacts
    assert library["manifest"] == "rust/capi/Cargo.toml"
    assert library["destination"] == "finance_enums/lib/{shared_library}"
    assert library["header-symbol-prefix"] == "finance_enums_"
    assert library["validate"] is True
    assert {Path(header).name for header in library["expected-headers"]} == HEADERS
    for output in library["outputs"]:
        name = Path(output["source"]).name
        assert output["source"] == f"rust/capi/include/{name}"
        assert output["destination"] == f"finance_enums/include/finance_enums/{name}"
        assert output["install-scheme"] == "package"
    assert {Path(output["source"]).name for output in library["outputs"]} == HEADERS

    assert extension["manifest"] == "Cargo.toml"
    assert extension["destination"] == "finance_enums/{python_extension_name}"
    assert extension["links"] == ["finance_enums"]
    assert extension["library-source-features"] == {
        "bundled": ["capi"],
        "external": ["capi"],
        "static": ["direct"],
        "direct": ["direct"],
    }

    wheel = pyproject["tool"]["hatch"]["build"]["targets"]["wheel"]
    assert "finance_enums/lib/*" in wheel["artifacts"]
    assert "finance_enums/include/**/*.h" in wheel["artifacts"]


def test_cargo_crates_split_core_c_abi_and_extension():
    extension = _toml("Cargo.toml")
    core = _toml("rust/Cargo.toml")
    capi = _toml("rust/capi/Cargo.toml")

    assert extension["lib"]["name"] == "_finance_enums"
    assert extension["features"] == {"default": ["direct"], "capi": [], "direct": ["dep:finance_enums"]}
    assert extension["dependencies"]["finance_enums"]["package"] == "finance_enums_capi"

    assert core["package"]["name"] == "finance_enums_core"
    assert core["lib"]["crate-type"] == ["rlib"]
    assert core["workspace"]["members"] == [".", "abi_safe_enum", "abi_safe_enum_macros", "capi"]
    assert core["dependencies"]["abi_safe_enum"]["path"] == "abi_safe_enum"

    assert capi["lib"]["name"] == "finance_enums"
    assert "cdylib" in capi["lib"]["crate-type"]
    assert capi["dependencies"]["finance_enums_core"]["path"] == ".."
    for crate in (extension, core, capi):
        assert crate["package"]["version"] == core["package"]["version"]


def test_native_package_include_paths_match_documented_header_names():
    cmake_config = (ROOT / "rust/cmake/config/finance-enumsConfig.cmake.in").read_text(encoding="utf-8")
    pkg_config = (ROOT / "rust/cmake/config/finance-enums.pc.in").read_text(encoding="utf-8")

    assert '@PACKAGE_CMAKE_INSTALL_INCLUDEDIR@/finance_enums"' in cmake_config
    assert '@CMAKE_INSTALL_FULL_INCLUDEDIR@/finance_enums"' in pkg_config
