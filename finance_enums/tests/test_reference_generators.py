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
