"""Custom integrations read translations/<lang>.json, not strings.json."""

import json
from pathlib import Path

COMPONENT = Path(__file__).resolve().parents[1] / "custom_components" / "bru"


def _keys(data, prefix=""):
    if isinstance(data, dict):
        out = set()
        for key, value in data.items():
            out |= _keys(value, f"{prefix}{key}.")
        return out
    return {prefix.rstrip(".")}


def test_english_matches_strings():
    strings = json.loads((COMPONENT / "strings.json").read_text())
    english = json.loads((COMPONENT / "translations" / "en.json").read_text())
    assert english == strings


def test_german_has_every_key():
    strings = json.loads((COMPONENT / "strings.json").read_text())
    german = json.loads((COMPONENT / "translations" / "de.json").read_text())
    assert _keys(german) == _keys(strings)
