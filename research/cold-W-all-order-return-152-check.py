"""Outward price of the alpha-free W-linear return on the genuine seed."""

from contextlib import redirect_stdout
import io
import json
from math import comb
from pathlib import Path
import runpy


ORDERS = 14


def harmonics(degree):
    for k in range(degree % 2, degree + 1, 2):
        yield k, comb(degree, (degree - k) // 2) * (2 if k else 1)


def cosines(unit, arb, acb):
    d = [acb(0) for _ in range(2 * ORDERS)]
    derivative = [acb(0) for _ in range(2 * ORDERS)]
    for ell in range(ORDERS):
        common = (-1)**ell * arb(comb(2*ell, ell)) * unit**(2*ell) / 4**ell
        for k, count in harmonics(2 * ell + 1):
            d[k] += common * unit * count / 2**(2 * ell + 1)
        for k, count in harmonics(2 * ell):
            derivative[k] += common * (2 * ell + 1) * count / 2**(2 * ell)
    return d, derivative


def times_first(coefficients, acb):
    result = [acb(0) for _ in range(len(coefficients) + 1)]
    for k, coefficient in enumerate(coefficients):
        result[k + 1] += coefficient / 2
        result[abs(k - 1)] += coefficient / 2
    return result


def activation(row, arb):
    output = {k: mass for k, mass in row.items() if k}
    output[0] = sum((abs(k) - 1) * mass for k, mass in output.items()) + arb(0)
    return output


def main():
    source = Path(__file__).with_name("cold-resummed-136-check.py")
    with redirect_stdout(io.StringIO()):
        replay = runpy.run_path(str(source))
    inherited = replay["inherited"]
    multiply = runpy.run_path(str(Path(__file__).with_name("cold-leading-W-square-151-check.py")))["multiply"]
    arb, acb = inherited["arb"], inherited["acb"]
    fields = inherited["fields"]
    kern, prev = fields["kern"], fields["prev"]
    t = inherited["t"]
    _, beta, *_ = kern["p3"]["coefficients"](t, acb(prev["da"]), acb(prev["db"]))
    seed = arb("2.8284275", arb("0.0000005"))
    assert arb("2.828427")**2 < 8 < 8 + arb(4) / 10**30 < arb("2.828428")**2
    root = 2 * t.sqrt()
    unit = seed / root

    d, symmetric_derivative = cosines(unit, arb, acb)
    derivative = [coefficient / root for coefficient in symmetric_derivative]
    odd_inner = times_first(derivative, acb)
    even_inner = times_first(d, acb)
    rank_three = {0: arb(1), -1: arb(3)/4, 1: arb(3)/4, -3: arb(1)/4, 3: arb(1)/4}
    cosine = [{0: arb(1)}] + [{-k: arb(1)/2, k: arb(1)/2} for k in range(1, len(even_inner))]

    def price(row):
        return sum(mass * inherited["price"](k) for k, mass in row.items() if k)

    total = arb(0)
    complement = arb(0)
    for j in range(1, len(odd_inner), 2):
        inner = activation(multiply(rank_three, cosine[j], arb), arb)
        for k in range(1, len(d), 2):
            term = abs(beta * d[k] * odd_inner[j]) * price(multiply(inner, cosine[k], arb))
            total += term
            if (k, j) != (1, 1):
                complement += term
    for j in range(2, len(even_inner), 2):
        inner = multiply(rank_three, activation(cosine[j], arb), arb)
        for k in range(0, len(derivative), 2):
            term = abs(beta * derivative[k] * even_inner[j]) * price(multiply(inner, cosine[k], arb))
            total += term
            if (k, j) != (0, 2):
                complement += term

    bound = arb("0.356")
    inverse_root = 1 / arb("7.96")
    assert abs(unit) < bound and abs(1 / root) < inverse_root
    a = bound**2
    f = 1 / (1 - a)**2
    g = (1 + 3*a) / (1 - a)**3
    tail_f = f - sum((ell + 1) * a**ell for ell in range(ORDERS))
    tail_g = g - sum((ell + 1) * (2*ell + 1) * a**ell for ell in range(ORDERS))
    tail = 48 * abs(beta) * inverse_root * bound * (tail_f * g + f * tail_g)
    assert tail > 0

    folded_multiplier = [arb(0) for _ in range(len(derivative) + 3)]
    for k in range(0, len(derivative), 2):
        for weight, mass in multiply(rank_three, cosine[k], arb).items():
            folded_multiplier[abs(weight)] += abs(beta * derivative[k]).upper() * mass
    translated_step = replay["price_rate"](folded_multiplier) + 12 * abs(beta) * inverse_root * tail_g
    assert translated_step < arb("0.0564")
    translated_square = 2 * arb("0.528") * arb("0.0564")
    assert translated_square < arb("0.05956")

    tail_d = bound * a**ORDERS / (1 - a)
    tail_dprime = inverse_root * a**ORDERS * (
        (2*ORDERS + 1) / (1 - a) + 2*a / (1 - a)**2
    )
    d_err = acb(arb(0, tail_d.upper()), arb(0, tail_d.upper()))
    dprime_err = acb(arb(0, tail_dprime.upper()), arb(0, tail_dprime.upper()))
    first = (d[1] + d_err) * (odd_inner[1] + 3*dprime_err/2)
    second = (derivative[0] + dprime_err) * (even_inner[2] + d_err)
    leading = seed / (4 * t)
    assert total + tail < arb("0.04938")
    assert complement + tail < arb("0.00768")
    assert tail < arb("3.44e-11")
    assert abs(first / leading) < arb("0.837")
    assert abs(2 * second / leading) < arb("0.863")
    print(json.dumps({
        "kind": "all_order_W_linear_alpha_free_square",
        "canonical_eventual_upper": "0.04938",
        "canonical_complement_upper": "0.00768",
        "canonical_analytic_tail_upper": "3.44e-11",
        "rank_four_relative_upper": "0.837",
        "mixed_legendre_relative_upper": "0.863",
        "translated_W_step_upper": "0.0564",
        "translated_mixed_square_upper": "0.05956",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
