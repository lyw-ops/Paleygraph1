"""Audit saved round-34 records and replay the exact incidence arithmetic.

This does not recompute all large stationary solves or Arb transforms.
Run with -B; only stdout is written.
"""

import contextlib
import importlib.util
import io
import json
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parent
ctx.prec = 192
PREFIX = "parallel-schur-response-34"


def rows(suffix):
    return [json.loads(line) for line in (ROOT/(PREFIX+suffix)).read_text().splitlines()]


def audit():
    diagnostic = rows(".jsonl")
    assert len(diagnostic) == 130 and diagnostic[-1]["kind"] == "all_checks_passed"
    assert diagnostic[-1]["actual_rows_are_floating"] is True
    assert diagnostic[-1]["cases"] == 7
    exact_saved = [r for r in diagnostic if r["kind"] == "exact_prime_incidence"]
    spec = importlib.util.spec_from_file_location("round34_diagnostic", ROOT/(PREFIX+".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        for p in (13, 101, 401):
            module.exact_incidence(p)
    exact_replayed = [json.loads(line) for line in captured.getvalue().splitlines()]
    assert exact_saved == exact_replayed
    assert sum(r["checks"] for r in exact_saved) == 506

    file_rows = {PREFIX+".jsonl": len(diagnostic)}
    intervals = 0
    distinct = set()
    certificate_sides = 0
    summaries = []
    for suffix, count in (("-certified-trial.jsonl", 5), ("-certified.jsonl", 9),
                          ("-certified-large.jsonl", 5), ("-certified-half.jsonl", 5)):
        data = rows(suffix)
        file_rows[PREFIX+suffix] = len(data)
        assert len(data) == count
        assert data[-1]["kind"] == "all_checks_passed" and data[-1]["all_thresholds"] is True
        for r in data:
            if r["kind"] == "rigorous_stationary_enclosure":
                epsilon = arb(r["residual_norm_upper"])
                L = arb(r["L_upper"])
                radius = arb(r["radius_l2"])
                assert r["certified"] is True and L < 1
                assert epsilon < (1-L)*radius
                assert arb(r["banach_margin_lower"]) > 0
            elif r["kind"] == "rigorous_continuous_all_threshold_HR":
                assert r["all_R_ge_zero_certified"] is True
                C = arb(r["C"])
                cover = arb(r["maximum_cover_ratio_upper"])
                terminal = arb(r["terminal_ratio_upper"])
                combined = arb(r["all_threshold_ratio_upper"])
                assert cover < C and terminal < C and combined < C
                expected = max(cover, terminal)
                assert combined.overlaps(expected)
                assert arb(r["minimum_physical_interval_width_lower"]) > 0
                assert arb(r["coordinate_and_l2_radius_upper"]) > 0
                assert arb(r["certified_dmax_upper"]) > 0
                intervals += r["certified_intervals"]
                certificate_sides += 1
                distinct.add((r["p"], r["side"], r["tau"]))
                summaries.append(dict(p=r["p"], side=r["side"], C=r["C"],
                                      intervals=r["certified_intervals"],
                                      ratio_upper=r["all_threshold_ratio_upper"]))

    assert sum(file_rows.values()) == 154
    assert intervals == 754 and certificate_sides == 10 and len(distinct) == 8
    return dict(all_checks_passed=True, primary_records=154,
                exact_incidence_checks_replayed=506,
                distinct_exact_stationary_sides=8,
                total_cover_intervals=754, file_rows=file_rows,
                certificate_summary=summaries,
                scope="saved-record consistency and exact-incidence replay; large Arb transforms not rerun",
                prime_uniform_cold_HR_proved=False,
                source_UI_assumed=False, ETH26_proved=False)


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
