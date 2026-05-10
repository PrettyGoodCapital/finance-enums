from __future__ import annotations

from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback
    import tomli as tomllib


def test_c_api_build_hook_does_not_import_unbuilt_package():
    pyproject = tomllib.loads(Path("pyproject.toml").read_text())

    build_system = pyproject["build-system"]
    hooks = pyproject["tool"]["hatch"]["build"]["hooks"]
    sdist_packages = pyproject["tool"]["hatch"]["build"]["targets"]["sdist"]["packages"]

    assert "backend-path" not in build_system
    assert "build-plan-class" not in hooks["hatch-rs"]
    assert hooks["custom"]["path"] == "hatch_build.py"
    assert "hatch_build.py" in sdist_packages
