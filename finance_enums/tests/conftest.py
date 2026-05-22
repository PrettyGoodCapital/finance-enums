import os

import pytest

LIVE_SOURCE_ENV_VAR = "FINANCE_ENUMS_RUN_LIVE_TESTS"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "live_source: requires live upstream network sources and is skipped unless FINANCE_ENUMS_RUN_LIVE_TESTS=1",
    )


def pytest_collection_modifyitems(config, items):
    if os.environ.get(LIVE_SOURCE_ENV_VAR) == "1":
        return

    skip_live = pytest.mark.skip(reason=f"set {LIVE_SOURCE_ENV_VAR}=1 to run live source validation")
    for item in items:
        if "live_source" in item.keywords:
            item.add_marker(skip_live)
