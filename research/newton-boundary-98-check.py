"""Outward arithmetic for the first-activation Newton comparison."""

import json
from pathlib import Path

from flint import arb, ctx


def read_kind(base, filename, predicate):
    with (base / filename).open() as stream:
        return next(record for record in map(json.loads, stream) if predicate(record))


def main():
    ctx.prec = 192
    base = Path(__file__).resolve().parent
    center, half = arb(2031)/128, arb(2)**-17
    floor = center-half
    physical = read_kind(base, "astra-adjoint-82-checks.jsonl",
                         lambda record: record.get("height") == 100)
    disk = read_kind(base, "astra-source-88-checks.jsonl",
                     lambda record: record["kind"] == "uniform_seed_disk_and_true_cold_square")
    time_estimate = read_kind(base, "same-floor-97-checks.jsonl", lambda record: True)

    rate, residual_price = arb("0.984138"), arb("0.001180")
    assert arb(physical["rate_upper"]) < rate
    assert arb(physical["segment_residual_bound"]) < residual_price
    assert arb(physical["first_increment_upper"]) < arb("0.169724")
    derivative = arb(disk["complex_prefix_derivative_upper"])
    residual = arb("0.169724")*derivative**100
    assert derivative < arb("0.514") and residual < arb("3e-30")
    assert arb(time_estimate["predictor_time_derivative_upper"]) < 21

    correction = arb("0.075")
    assert residual_price/(1-rate) < correction
    tail = correction*rate**750
    assert tail < arb("5e-7")
    bulk_curvature = 4*(center+2*half)/(4*floor-9)**arb("1.5")
    mark_curvature = 4*arb("1e30")/(4*arb("1e30")-9)**arb("1.5")
    assert bulk_curvature < arb("0.2") and mark_curvature < arb("0.2")
    assert 462*arb("1.514") < 700
    entry_limsup_bound = arb(2).sqrt()*(2/(1-rate)-1)
    assert entry_limsup_bound < 178
    remainder_constant = 178*700

    height = half/1000
    strip_imaginary = ((21*height+correction*height/(half/2-height))/floor.sqrt()
                       +arb("4.843")*height/(2*floor**arb("1.5")))
    assert strip_imaginary < arb("4e-5")
    first_imaginary = 2*arb("1e-4")/arb(3).sqrt()
    strip_scale = (first_imaginary-arb("4e-5"))*floor.sqrt()/remainder_constant
    assert strip_scale > arb("2.3e-9")
    full_scale = arb("1e-9")
    finite_test_lower = (first_imaginary
                         -(remainder_constant*full_scale+arb("5e-7"))/floor.sqrt())
    assert finite_test_lower > arb("8e-5")
    print(json.dumps(dict(
        kind="actual_first_activation_after_one_newton_correction",
        precision_bits=ctx.prec, pointwise_remainder_coefficient=remainder_constant,
        strip_real_half_width="2^-18", strip_imaginary_half_width="2^-17/1000",
        strip_corrected_imaginary_upper=strip_imaginary.str(14),
        strip_sqrt_n_residual_squared_lower=strip_scale.str(14),
        finite_nominal_neumann_terms=750, nominal_tail_upper=tail.str(14),
        full_square_nominal_imaginary_lower=finite_test_lower.str(14),
    ), sort_keys=True))


if __name__ == "__main__":
    main()
