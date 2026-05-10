import csv
import io
import json
import subprocess
import xml.etree.ElementTree as ET

import pytest

from finance_enums import CountryCode, CountryCode3, Currency, ExchangeCode

pytestmark = pytest.mark.live_source


def _fetch_text(url: str) -> str:
    result = subprocess.run(
        ["curl", "-fsSL", url],
        capture_output=True,
        check=True,
        text=True,
    )
    return result.stdout


def _fetch_json(url: str):
    return json.loads(_fetch_text(url))


def _active_mics() -> set[str]:
    text = _fetch_text("https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv")
    rows = csv.DictReader(io.StringIO(text))
    return {row["MIC"] for row in rows if row["STATUS"] == "ACTIVE" and row["MIC"]}


def _iso4217_codes() -> set[str]:
    xml_text = _fetch_text("https://www.six-group.com/dam/download/financial-information/data-center/iso-currrency/lists/list-one.xml")
    root = ET.fromstring(xml_text)
    return {entry.findtext("Ccy") for entry in root.findall(".//CcyNtry") if entry.findtext("Ccy")}


def _country_feeds() -> tuple[set[str], set[str]]:
    countries = _fetch_json("https://restcountries.com/v3.1/all?fields=cca2,cca3")
    alpha2 = {entry["cca2"] for entry in countries if "cca2" in entry}
    alpha3 = {entry["cca3"] for entry in countries if "cca3" in entry}
    return alpha2, alpha3


def test_exchange_codes_cover_all_active_iso10383_mics() -> None:
    missing = sorted(_active_mics() - {member.value for member in ExchangeCode})
    assert missing == []


def test_currency_codes_cover_live_iso4217_list() -> None:
    missing = sorted(_iso4217_codes() - {member.value for member in Currency})
    assert missing == []


def test_country_codes_cover_live_country_feed() -> None:
    alpha2, alpha3 = _country_feeds()
    missing_alpha2 = sorted(alpha2 - {member.value for member in CountryCode})
    missing_alpha3 = sorted(alpha3 - {member.value for member in CountryCode3})

    assert missing_alpha2 == []
    assert missing_alpha3 == []
