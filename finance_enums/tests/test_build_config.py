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
        "name": "finance_enums",
        "manifest": "Cargo.toml",
        "destination": "finance_enums/{python_extension_name}",
    }

    assert c_abi_artifact["name"] == "finance_enums"
    assert c_abi_artifact["destination"] == "finance_enums/lib/{shared_library}"
    assert c_abi_artifact["validate"] is True
    assert c_abi_artifact["outputs"] == [
        {
            "source": "finance_enums/include/finance_enums.h",
            "destination": "include/finance_enums/finance_enums.h",
            "install-scheme": "shared-data",
        }
    ]
    assert all("kind" not in artifact for artifact in artifacts)
    assert all("library" not in artifact for artifact in artifacts)
    assert "hatch_build.py" not in sdist_packages
