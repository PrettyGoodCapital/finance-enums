import ctypes

from finance_enums import Currency, currency_alias_records, currency_export_capsule, currency_records


class CurrencyRecordRaw(ctypes.Structure):
    _fields_ = [
        ("code", ctypes.c_char_p),
        ("display_name", ctypes.c_char_p),
        ("is_iso4217", ctypes.c_bool),
    ]


class CurrencyAliasRecordRaw(ctypes.Structure):
    _fields_ = [
        ("alias", ctypes.c_char_p),
        ("canonical_code", ctypes.c_char_p),
    ]


class CurrencyExportV1(ctypes.Structure):
    _fields_ = [
        ("abi_version", ctypes.c_uint32),
        ("export_struct_size", ctypes.c_size_t),
        ("currency_record_size", ctypes.c_size_t),
        ("currency_alias_record_size", ctypes.c_size_t),
        ("records", ctypes.POINTER(CurrencyRecordRaw)),
        ("records_len", ctypes.c_size_t),
        ("aliases", ctypes.POINTER(CurrencyAliasRecordRaw)),
        ("aliases_len", ctypes.c_size_t),
    ]


_pycapsule_get_pointer = ctypes.pythonapi.PyCapsule_GetPointer
_pycapsule_get_pointer.restype = ctypes.c_void_p
_pycapsule_get_pointer.argtypes = [ctypes.py_object, ctypes.c_char_p]


class TestCurrency:
    def test_currency_basic(self):
        assert str(Currency.USD) == "USD"
        assert Currency.USD.currency_name() == "United States dollar"
        assert Currency.USD.is_iso4217() is True
        assert Currency.CNH.is_iso4217() is False
        assert Currency.ECNY.is_iso4217() is False

    def test_noniso_currency_pennies(self):
        assert Currency("EUr") == Currency.EUX
        assert Currency("GBp") == Currency.GBX
        assert Currency("USd") == Currency.USX
        assert Currency("e-CNY") == Currency.ECNY

    def test_structured_currency_records(self):
        records = {record.code: record for record in currency_records()}

        assert records["USD"].display_name == "United States dollar"
        assert records["USN"].display_name == "United States dollar (next day)"
        assert records["CNH"].display_name == "Offshore renminbi"
        assert records["ECNY"].display_name == "Digital yuan (e-CNY)"
        assert records["ECNY"].is_iso4217 is False

        alias_records = {record.alias: record.canonical_code for record in currency_alias_records()}
        assert alias_records["EUr"] == "EUX"
        assert alias_records["e-CNY"] == "ECNY"

    def test_currency_export_capsule(self):
        capsule = currency_export_capsule()
        pointer = _pycapsule_get_pointer(capsule, b"finance_enums.currency_export_v1")
        export = ctypes.cast(pointer, ctypes.POINTER(CurrencyExportV1)).contents

        assert export.abi_version == 1
        assert export.records_len == len(currency_records())
        assert export.aliases_len == len(currency_alias_records())
        assert export.records[0].code == b"AED"
        assert export.records[export.records_len - 1].code == b"ECNY"
        assert export.aliases[export.aliases_len - 1].alias == b"e-CNY"
