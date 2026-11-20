"""Outward signed comparison for two actual higher-center Legendre unit returns."""

from contextlib import redirect_stdout
import io
import json
from math import comb
from pathlib import Path
import runpy


def main():
    directory = Path(__file__).parent
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(directory / "cold-resummed-136-check.py"))
    cosines = runpy.run_path(str(directory / "cold-W-all-order-return-152-check.py"))["cosines"]
    arb, acb, t = (replay[key] for key in ("arb", "acb", "t"))
    kern, prev = (replay["fields"][key] for key in ("kern", "prev"))
    alpha, beta, groups, _ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    gamma = arb(499) / 500 * beta * groups[1, 1][0, 0]
    delta = -2 * gamma * kern["linear_scalar"](groups, beta)

    root = 2 * t.sqrt()
    inverse = 1 / arb("7.96")
    unit_bound = arb("0.356")
    unit = replay["seed"] / root
    assert abs(unit) < unit_bound and abs(1/root) < inverse
    square = unit_bound**2
    orders = 14

    def rectangle(radius):
        return acb(arb(0, radius.upper()), arb(0, radius.upper()))

    d, derivative = cosines(unit, arb, acb)
    d_error = rectangle(unit_bound * square**orders / (1-square))
    derivative_error = rectangle(inverse * square**orders *
        ((2*orders + 1)/(1-square) + 2*square/(1-square)**2))
    b0, b2 = (derivative[k]/root + derivative_error for k in (0, 2))
    D = b0*(b0+b2/2)
    v2 = (d[1] + d[3])/2 + d_error

    q0 = acb(0)
    for ell in range(1, orders):
        degree = 2*ell + 1
        cosine_mean = arb(comb(degree-3, (degree-3)//2)) / 2**(degree-3)
        coefficient = (-1)**ell * arb(comb(2*ell, ell)) / 4**ell
        q0 += coefficient * degree*(degree-1)*(degree-2)*unit**(degree-3)*cosine_mean/root**3
    # Bound the derivative tail by a geometric majorant for (2l+1)^3 |unit|^(2l-2).
    ratio = square*(arb(2*orders+3)/(2*orders+1))**3
    assert ratio < arb("0.16")
    q0 += rectangle(inverse**3 * (2*orders+1)**3 * square**(orders-1) / (1-ratio))
    assert q0.real < 0 and v2.real > 0

    old = (D*(alpha*delta-beta*gamma), D*(beta*delta-gamma**2))
    higher = (alpha*beta*delta*q0*v2/2, alpha*gamma*delta*q0*v2/2)
    lower = "0.001"
    upper = "0.002"
    for coefficient, return_coefficient in zip(old, higher):
        assert coefficient.real < 0 and return_coefficient.real > 0
        merged_ratio = abs(1 + return_coefficient/coefficient)
        assert 1-arb(upper) < merged_ratio < 1-arb(lower)
    print(json.dumps({
        "kind": "actual_selected_legendre_unit_returns_on_C1",
        "uniform_relative_saving_lower_per_pair": lower,
        "uniform_relative_saving_upper_per_pair": upper,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
