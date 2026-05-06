"""Executable checks for the sqlguard casebook."""

from __future__ import annotations

from collections import Counter

from . import sqlguard_segment_00
from . import sqlguard_segment_01
from . import sqlguard_segment_02
from . import sqlguard_segment_03
from . import sqlguard_segment_04
from . import sqlguard_segment_05
from . import sqlguard_segment_06
from . import sqlguard_segment_07
from . import sqlguard_segment_08
from . import sqlguard_segment_09
from .expected import EXPECTED
from .model import validate_case


def iter_cases():
    yield from sqlguard_segment_00.iter_sqlguard_00()
    yield from sqlguard_segment_01.iter_sqlguard_01()
    yield from sqlguard_segment_02.iter_sqlguard_02()
    yield from sqlguard_segment_03.iter_sqlguard_03()
    yield from sqlguard_segment_04.iter_sqlguard_04()
    yield from sqlguard_segment_05.iter_sqlguard_05()
    yield from sqlguard_segment_06.iter_sqlguard_06()
    yield from sqlguard_segment_07.iter_sqlguard_07()
    yield from sqlguard_segment_08.iter_sqlguard_08()
    yield from sqlguard_segment_09.iter_sqlguard_09()


def summarize_cases() -> dict:
    rows = list(iter_cases())
    for row in rows:
        validate_case(row)
    lanes = Counter(row.expected_lane for row in rows)
    focus = Counter(row.focus for row in rows)
    return {
        "case_count": len(rows),
        "score_min": min(row.expected_score for row in rows),
        "score_max": max(row.expected_score for row in rows),
        "lane_counts": dict(sorted(lanes.items())),
        "focus_counts": dict(sorted(focus.items())),
        "score_checksum": sum((index + 1) * row.expected_score for index, row in enumerate(rows)),
        "pressure_checksum": sum((index % 17 + 1) * row.pressure for index, row in enumerate(rows)),
    }


def assert_expected() -> dict:
    summary = summarize_cases()
    if summary != EXPECTED:
        raise AssertionError(f"casebook summary mismatch: {summary!r} != {EXPECTED!r}")
    return summary


def sqlguard_summary() -> dict:
    return assert_expected()
