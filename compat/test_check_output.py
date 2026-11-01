"""Checks the checker itself. `pytest compat`."""

import json
from pathlib import Path

from check_output import compare

FIXTURE = Path(__file__).parent.parent / "fixtures/official/b-compare5-us.items.json"
OFFICIAL = json.loads(FIXTURE.read_text())[0]


def test_identical_passes() -> None:
    assert compare(OFFICIAL, OFFICIAL) == []


def test_missing_key_fails() -> None:
    ours = {k: v for k, v in OFFICIAL.items() if k != "relatedQueries_top"}
    assert compare(ours, OFFICIAL) == ["$.relatedQueries_top: missing"]


def test_wrong_type_fails() -> None:
    assert compare({**OFFICIAL, "searchTerm": 1}, OFFICIAL) == ["$.searchTerm: number instead of str"]


def test_key_order_fails() -> None:
    ours = dict(reversed(list(OFFICIAL.items())))
    assert any("key order differs" in p for p in compare(ours, OFFICIAL))


def test_empty_list_matches_any_list() -> None:
    assert compare({**OFFICIAL, "relatedQueries_top": []}, OFFICIAL) == []
