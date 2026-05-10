import sys
from pathlib import Path


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
    assert "CurrencyDataExportV1" in header
    assert "ExchangeDataExportV1" in header
