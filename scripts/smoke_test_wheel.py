from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

HEADERS = {
    "finance_enums.h",
    "finance_enums.hpp",
    "finance_enums_convert.hpp",
    "finance_enums_generated.h",
}


def _wheel(path: Path) -> Path:
    if path.is_file():
        return path
    wheels = sorted(path.glob("*.whl"))
    if len(wheels) != 1:
        raise AssertionError(f"expected one wheel in {path}, found {wheels}")
    return wheels[0]


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate finance-enums wheel layout and importability")
    parser.add_argument("wheel", type=Path)
    parser.add_argument("--split", action="store_true", help="expect a Python-only split-package wheel")
    args = parser.parse_args()

    wheel = _wheel(args.wheel)
    with zipfile.ZipFile(wheel) as archive:
        names = archive.namelist()
        extensions = [name for name in names if name.startswith("finance_enums/_finance_enums.") and name.endswith((".so", ".pyd"))]
        libraries = [name for name in names if name.startswith("finance_enums/lib/") and name.endswith((".so", ".dylib", ".dll"))]
        headers = {Path(name).name for name in names if ".data/data/include/finance_enums/" in name and name.endswith((".h", ".hpp"))}

        assert len(extensions) == 1, extensions
        assert not any(name.startswith("finance_enums/finance_enums.") for name in names)
        assert not any(name.startswith("finance_enums/include/") for name in names)
        if args.split:
            assert not libraries, libraries
            assert not headers, headers
        else:
            assert len(libraries) == 1, libraries
            assert headers == HEADERS, headers

        with tempfile.TemporaryDirectory() as directory:
            archive.extractall(directory)
            env = os.environ.copy()
            env.pop("PYTHONPATH", None)
            subprocess.run(
                [
                    sys.executable,
                    "-c",
                    "import finance_enums as fe; assert fe.abi_version() == tuple(map(int, fe.__version__.split('.')))",
                ],
                cwd=directory,
                env=env,
                check=True,
            )


if __name__ == "__main__":
    main()
