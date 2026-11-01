#!/usr/bin/env python3
"""Compare an Actor's output with a saved official output. Values are ignored; keys, key order
and types are compared. An empty list matches any list, because Google may return no data.

    python compat/check_output.py <our-items.json> <official-items.json>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def kind(value: Any) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int | float):
        return "number"
    if value is None:
        return "null"
    return type(value).__name__


def compare(ours: Any, official: Any, path: str = "$") -> list[str]:
    if kind(ours) != kind(official):
        return [f"{path}: {kind(ours)} instead of {kind(official)}"]
    if isinstance(official, dict):
        problems: list[str] = []
        problems += [f"{path}.{k}: missing" for k in official if k not in ours]
        problems += [f"{path}.{k}: extra key" for k in ours if k not in official]
        shared_ours = [k for k in ours if k in official]
        shared_official = [k for k in official if k in ours]
        if shared_ours != shared_official:
            problems.append(f"{path}: key order differs: {shared_ours} vs {shared_official}")
        for key in shared_official:
            problems += compare(ours[key], official[key], f"{path}.{key}")
        return problems
    if isinstance(official, list) and ours and official:
        return compare(ours[0], official[0], f"{path}[0]")
    return []


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 2
    ours, official = (json.loads(Path(p).read_text()) for p in argv[1:])
    if not ours or not official:
        print("FAIL: an input file has no items")
        return 1
    problems = compare(ours[0], official[0])
    print("\n".join(problems) if problems else "OK: same keys, key order and types")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
