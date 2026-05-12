from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from platform import machine as platform_machine
from sys import platform as sys_platform
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class FinanceEnumsCAbiBuildHook(BuildHookInterface):
    PLUGIN_NAME = "finance-enums-c-abi"

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        if self.target_name != "wheel":
            return

        target = self._target_triple()
        destination = Path(self.root, "finance_enums", "lib", self._shared_library_name())
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.unlink(missing_ok=True)

        # Avoid reusing host-built shared objects when cibuildwheel mounts the source into manylinux.
        with tempfile.TemporaryDirectory(prefix="finance-enums-capi-") as target_dir:
            env = os.environ.copy()
            env["CARGO_TARGET_DIR"] = target_dir

            subprocess.run(
                [
                    "cargo",
                    "rustc",
                    "--manifest-path",
                    "rust/Cargo.toml",
                    "--release",
                    "--target",
                    target,
                    "--",
                    "--crate-type",
                    "cdylib",
                ],
                cwd=self.root,
                env=env,
                check=True,
            )

            source = self._find_shared_library(Path(target_dir), target)
            shutil.copy2(source, destination)
        build_data["force_include"][str(destination.relative_to(self.root))] = str(destination.relative_to(self.root))

    def _target_triple(self) -> str:
        platform = os.environ.get("HATCH_RUST_PLATFORM", sys_platform)
        machine = os.environ.get("HATCH_RUST_MACHINE", platform_machine())

        if platform == "win32":
            if machine in ("x86_64", "AMD64"):
                return "x86_64-pc-windows-msvc"
            if machine == "i686":
                return "i686-pc-windows-msvc"
            if machine in ("arm64", "aarch64"):
                return "aarch64-pc-windows-msvc"
        elif platform == "darwin":
            if machine == "x86_64":
                return "x86_64-apple-darwin"
            if machine in ("arm64", "aarch64"):
                return "aarch64-apple-darwin"
        elif platform == "linux":
            if machine == "x86_64":
                return "x86_64-unknown-linux-gnu"
            if machine == "i686":
                return "i686-unknown-linux-gnu"
            if machine in ("arm64", "aarch64"):
                return "aarch64-unknown-linux-gnu"

        raise ValueError(f"Unsupported platform/machine for finance-enums C ABI build: {platform}/{machine}")

    def _find_shared_library(self, target_dir: Path, target: str) -> Path:
        build_dir = target_dir / target / "release"
        candidates = list(build_dir.glob(self._shared_library_pattern()))
        candidates.extend((build_dir / "deps").glob(self._shared_library_pattern()))

        if not candidates:
            raise FileNotFoundError(f"Standalone C ABI library was not produced under '{build_dir}'.")

        return max(candidates, key=lambda path: path.stat().st_mtime)

    def _shared_library_name(self) -> str:
        platform = os.environ.get("HATCH_RUST_PLATFORM", sys_platform)
        if platform == "win32":
            return "finance_enums.dll"
        if platform == "darwin":
            return "libfinance_enums.dylib"
        if platform == "linux":
            return "libfinance_enums.so"
        raise ValueError(f"Unsupported platform: {platform}")

    def _shared_library_pattern(self) -> str:
        platform = os.environ.get("HATCH_RUST_PLATFORM", sys_platform)
        if platform == "win32":
            return "finance_enums*.dll"
        if platform == "darwin":
            return "libfinance_enums*.dylib"
        if platform == "linux":
            return "libfinance_enums*.so"
        raise ValueError(f"Unsupported platform: {platform}")
