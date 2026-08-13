from __future__ import annotations

from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib


def test_c_api_build_uses_declarative_hatch_rs_artifacts():
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    pyproject = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

    build_system = pyproject["build-system"]
    hooks = pyproject["tool"]["hatch"]["build"]["hooks"]
    hatch_rs = hooks["hatch-rs"]
    sdist_packages = pyproject["tool"]["hatch"]["build"]["targets"]["sdist"]["packages"]
    artifacts = hatch_rs["artifacts"]
    python_artifact = next(artifact for artifact in artifacts if artifact["manifest"] == "Cargo.toml")
    c_abi_artifact = next(artifact for artifact in artifacts if artifact["manifest"] == "rust/Cargo.toml")

    assert "backend-path" not in build_system
    assert "custom" not in hooks
    assert "build-plan-class" not in hatch_rs
    assert hatch_rs["target-dir"] == "isolated"
    assert python_artifact == {
        "name": "_finance_enums",
        "manifest": "Cargo.toml",
        "destination": "finance_enums/{python_extension_name}",
    }

    assert c_abi_artifact["name"] == "finance_enums"
    assert c_abi_artifact["destination"] == "finance_enums/lib/{shared_library}"
    assert c_abi_artifact["skip-if-env"] == "FINANCE_ENUMS_SKIP_SHARED_LIBRARY"
    assert c_abi_artifact["validate"] is True
    expected_headers = {
        "finance_enums.h",
        "finance_enums.hpp",
        "finance_enums_convert.hpp",
        "finance_enums_generated.h",
    }
    assert {Path(header).name for header in c_abi_artifact["expected-headers"]} == expected_headers
    assert {Path(output["source"]).name for output in c_abi_artifact["outputs"]} == expected_headers
    assert {Path(output["destination"]).name for output in c_abi_artifact["outputs"]} == expected_headers
    assert all(output["install-scheme"] == "shared-data" for output in c_abi_artifact["outputs"])
    assert all("kind" not in artifact for artifact in artifacts)
    assert all("library" not in artifact for artifact in artifacts)
    assert "hatch_build.py" not in sdist_packages

    wheel = pyproject["tool"]["hatch"]["build"]["targets"]["wheel"]
    assert "finance_enums/include" in wheel["exclude"]
    assert "finance_enums/lib" in wheel["exclude"]
    assert "shared-data" not in wheel

    cargo = tomllib.loads((pyproject_path.parent / "Cargo.toml").read_text(encoding="utf-8"))
    rust_cargo = tomllib.loads((pyproject_path.parent / "rust" / "Cargo.toml").read_text(encoding="utf-8"))
    assert cargo["lib"]["name"] == "_finance_enums"
    assert rust_cargo["lib"]["name"] == "finance_enums"


def test_native_package_include_paths_match_documented_header_names():
    root = Path(__file__).resolve().parents[2]
    cmake_config = (root / "rust/cmake/config/finance-enumsConfig.cmake.in").read_text(encoding="utf-8")
    pkg_config = (root / "rust/cmake/config/finance-enums.pc.in").read_text(encoding="utf-8")

    assert '@PACKAGE_CMAKE_INSTALL_INCLUDEDIR@/finance_enums"' in cmake_config
    assert '@CMAKE_INSTALL_FULL_INCLUDEDIR@/finance_enums"' in pkg_config
