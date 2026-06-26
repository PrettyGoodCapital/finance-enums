"""Tests for the native ABI version/compat helpers and runtime enum helpers.

Covers the in-process PyO3 functions and the C ABI exported from the cdylib (via
ctypes). The C/C++ headers are exercised by the compile-and-run test in
``finance_enums/tests/ffi/test_ffi_build.py``.
"""

import ctypes
import platform
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parents[2]


@pytest.fixture
def fe():
    import finance_enums

    if not hasattr(finance_enums, "abi_version"):
        pytest.skip("finance_enums native extension predates ABI helpers")
    return finance_enums


class TestPyO3Helpers:
    def test_abi_version(self, fe):
        major, minor, patch = fe.abi_version()
        assert (major, minor, patch) == fe.__abi_version__
        assert all(isinstance(x, int) for x in (major, minor, patch))

    def test_abi_compatible(self, fe):
        major, minor, _patch = fe.abi_version()
        assert fe.abi_compatible(major, minor) is True
        assert fe.abi_compatible(major, minor + 1) is False
        assert fe.abi_compatible(major + 1, minor) is False

    def test_assert_abi_compatible(self, fe):
        major, minor, _patch = fe.abi_version()
        fe.assert_abi_compatible(major, minor)  # must not raise
        with pytest.raises(RuntimeError):
            fe.assert_abi_compatible(major + 1, minor)

    def test_family_variant_count(self, fe):
        assert fe.family_variant_count("Side") == 4
        assert fe.family_variant_count("Bogus") is None

    def test_validate_ordinal(self, fe):
        assert fe.validate_ordinal("Side", 0) is True
        assert fe.validate_ordinal("Side", 99_999) is False
        assert fe.validate_ordinal("Bogus", 0) is None

    def test_variant_name(self, fe):
        assert fe.variant_name("Side", 2) == "Buy"
        assert fe.variant_name("Side", 99_999) is None
        assert fe.variant_name("Bogus", 0) is None

    def test_ordinal_of(self, fe):
        assert fe.ordinal_of("Side", "Buy") == 2
        assert fe.ordinal_of("Side", "NOPE") is None
        assert fe.ordinal_of("Bogus", "Buy") is None

    def test_round_trip(self, fe):
        for name in ("Side", "OptionType"):
            count = fe.family_variant_count(name)
            assert count is not None
            for ordinal in range(count):
                variant = fe.variant_name(name, ordinal)
                assert variant is not None
                assert fe.ordinal_of(name, variant) == ordinal


def _find_cdylib() -> Path | None:
    lib_name = {
        "Darwin": "libfinance_enums.dylib",
        "Linux": "libfinance_enums.so",
        "Windows": "finance_enums.dll",
    }.get(platform.system())
    if lib_name is None:
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


@pytest.fixture
def cdylib():
    lib_path = _find_cdylib()
    if lib_path is None:
        pytest.skip("cdylib not built")
    lib = ctypes.CDLL(str(lib_path))
    lib.finance_enums_abi_version.argtypes = [
        ctypes.POINTER(ctypes.c_uint32),
        ctypes.POINTER(ctypes.c_uint32),
        ctypes.POINTER(ctypes.c_uint32),
    ]
    lib.finance_enums_abi_version.restype = None
    lib.finance_enums_abi_compatible.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
    lib.finance_enums_abi_compatible.restype = ctypes.c_int32
    lib.finance_enums_validate_ordinal.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
    lib.finance_enums_validate_ordinal.restype = ctypes.c_int32
    lib.finance_enums_variant_name.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
    lib.finance_enums_variant_name.restype = ctypes.c_char_p
    lib.finance_enums_ordinal_of.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lib.finance_enums_ordinal_of.restype = ctypes.c_ssize_t
    lib.finance_enums_family_variant_count.argtypes = [ctypes.c_char_p]
    lib.finance_enums_family_variant_count.restype = ctypes.c_ssize_t
    return lib


class TestCAbiViaCtypes:
    def test_abi_version(self, cdylib):
        major = ctypes.c_uint32()
        minor = ctypes.c_uint32()
        patch = ctypes.c_uint32()
        cdylib.finance_enums_abi_version(ctypes.byref(major), ctypes.byref(minor), ctypes.byref(patch))
        # The ABI version mirrors the package version, so it is only guaranteed
        # to be non-zero, not >= 1 on the major component.
        assert (major.value, minor.value, patch.value) != (0, 0, 0)

    def test_abi_compatible(self, cdylib):
        major = ctypes.c_uint32()
        minor = ctypes.c_uint32()
        cdylib.finance_enums_abi_version(ctypes.byref(major), ctypes.byref(minor), None)
        assert cdylib.finance_enums_abi_compatible(major.value, minor.value) == 1
        assert cdylib.finance_enums_abi_compatible(major.value, minor.value + 1) == 0
        assert cdylib.finance_enums_abi_compatible(major.value + 1, minor.value) == 0

    def test_validate_ordinal(self, cdylib):
        assert cdylib.finance_enums_validate_ordinal(b"Side", 0) == 1
        assert cdylib.finance_enums_validate_ordinal(b"Side", 99_999) == 0
        assert cdylib.finance_enums_validate_ordinal(b"Bogus", 0) == -1

    def test_variant_name(self, cdylib):
        assert cdylib.finance_enums_variant_name(b"Side", 2) == b"Buy"
        assert cdylib.finance_enums_variant_name(b"Side", 99) is None

    def test_ordinal_of(self, cdylib):
        assert cdylib.finance_enums_ordinal_of(b"Side", b"Buy") == 2
        assert cdylib.finance_enums_ordinal_of(b"Side", b"NOPE") == -1

    def test_family_variant_count(self, cdylib):
        assert cdylib.finance_enums_family_variant_count(b"Side") == 4
        assert cdylib.finance_enums_family_variant_count(b"Bogus") == -1
