"""Build and run the C and C++ FFI integration programs against the cdylib."""

import platform
import shutil
import subprocess
from pathlib import Path

import pytest

TESTS_FFI_DIR = Path(__file__).parent
PROJECT_ROOT = TESTS_FFI_DIR.parents[2]
INCLUDE_DIR = PROJECT_ROOT / "finance_enums" / "include"
C_SOURCE = TESTS_FFI_DIR / "test.c"
CPP_SOURCE = TESTS_FFI_DIR / "test.cpp"


def _find_shared_library() -> Path | None:
    if platform.system() == "Darwin":
        lib_name = "libfinance_enums.dylib"
    elif platform.system() == "Linux":
        lib_name = "libfinance_enums.so"
    else:
        return None

    candidates = [
        PROJECT_ROOT / "finance_enums" / "lib" / lib_name,
        PROJECT_ROOT / "rust" / "target" / "release" / lib_name,
        PROJECT_ROOT / "rust" / "target" / "debug" / lib_name,
        PROJECT_ROOT / "target" / "release" / lib_name,
        PROJECT_ROOT / "target" / "debug" / lib_name,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _build_library() -> Path:
    lib_path = _find_shared_library()
    if lib_path is not None:
        return lib_path

    if shutil.which("cargo") is None:
        pytest.skip("cargo not available and shared library not built")

    result = subprocess.run(
        ["cargo", "rustc", "--release", "--crate-type=cdylib"],
        cwd=PROJECT_ROOT / "rust",
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        pytest.fail(f"cargo rustc --crate-type=cdylib failed:\n{result.stderr}")

    lib_path = _find_shared_library()
    if lib_path is None:
        pytest.skip("Could not build or locate shared library")
    return lib_path


def _compile(source: Path, compiler: str, std: str) -> Path:
    output = TESTS_FFI_DIR / source.stem
    cmd = [compiler, std, "-O2", f"-I{INCLUDE_DIR}", "-o", str(output), str(source)]
    if platform.system() == "Linux":
        cmd.append("-ldl")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        pytest.fail(f"{compiler} compilation failed:\n{result.stderr}")
    return output


def _run(binary: Path, lib_path: Path) -> None:
    result = subprocess.run(
        [str(binary), str(lib_path)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.skipif(not C_SOURCE.exists(), reason="C test source not found")
def test_c_ffi():
    compiler = "clang" if platform.system() == "Darwin" else "gcc"
    if shutil.which(compiler) is None:
        pytest.skip(f"{compiler} not available")
    lib_path = _build_library()
    binary = _compile(C_SOURCE, compiler, "-std=c11")
    try:
        _run(binary, lib_path)
    finally:
        binary.unlink(missing_ok=True)


@pytest.mark.skipif(not CPP_SOURCE.exists(), reason="C++ test source not found")
def test_cpp_ffi():
    compiler = "clang++" if platform.system() == "Darwin" else "g++"
    if shutil.which(compiler) is None:
        pytest.skip(f"{compiler} not available")
    lib_path = _build_library()
    binary = _compile(CPP_SOURCE, compiler, "-std=c++20")
    try:
        _run(binary, lib_path)
    finally:
        binary.unlink(missing_ok=True)
