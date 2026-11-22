import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_reference_data_generator_is_reproducible():
    result = subprocess.run(
        [sys.executable, "scripts/generate_reference_data.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_reference_snapshot_diff_is_clean_for_checked_in_data():
    result = subprocess.run(
        [sys.executable, "scripts/snapshot_reference_diffs.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_generated_enum_stub_is_up_to_date():
    """The committed type stub must match a fresh regeneration from the native families."""
    from finance_enums.gen_enum_stubs import generate_stub, stub_path

    assert stub_path.read_text(encoding="utf-8") == generate_stub(), "run: python finance_enums/gen_enum_stubs.py"
