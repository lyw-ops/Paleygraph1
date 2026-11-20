"""Outward price for the leading W-linear square term on the Jacobi column."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


def multiply(left, right, arb):
    result = {}
    for a, mass_a in left.items():
        for b, mass_b in right.items():
            result[a + b] = result.get(a + b, arb(0)) + mass_a * mass_b
    return result


def main():
    source = Path(__file__).with_name("cold-combined-height-130-check.py")
    with redirect_stdout(io.StringIO()):
        inherited = runpy.run_path(str(source))
    arb, acb = inherited["arb"], inherited["acb"]
    fields = inherited["fields"]
    kern, prev = fields["kern"], fields["prev"]
    alpha, beta, *_ = kern["p3"]["coefficients"](
        inherited["t"], acb(prev["da"]), acb(prev["db"])
    )
    field = {k: kern["F"][4 + k] for k in range(-4, 5)}
    jacobi = {-1: arb(1) / 2, 1: arb(1) / 2}
    legendre = {-2: arb(1) / 2, 0: arb(1), 2: arb(1) / 2}
    rank_three = {0: arb(1), -1: arb(3) / 4, 1: arb(3) / 4,
                  -3: arb(1) / 4, 3: arb(1) / 4}

    def price(left, right):
        pre_activation = multiply(left, right, arb)
        return sum(mass * inherited["price"](weight)
                   for weight, mass in pre_activation.items() if weight)

    term_jacobi = price(jacobi, field) + price(rank_three, legendre) / 2
    term_legendre = price(legendre, field) + price(rank_three, rank_three)
    seed_cap = arb("2.828428")
    assert seed_cap**2 > 8 + arb(4) / 10**30
    square = inherited["floor"] - inherited["half"]
    bound = abs(beta) * (seed_cap * term_jacobi + abs(alpha) * term_legendre) / (4 * square)
    assert bound < arb("0.061")
    seed_square = arb("8.0000005", arb("0.0000005"))
    kappa = seed_square / (8 * inherited["t"])
    factor_four = abs(1 - 3 * kappa)
    factor_mixed = abs(1 - 5 * kappa / 2)
    assert factor_four < arb("0.812")
    assert factor_mixed < arb("0.844")
    merged = abs(beta) * seed_cap / (4 * square) * (
        factor_four * price(jacobi, field)
        + factor_mixed * price(rank_three, legendre) / 2
    )
    assert merged < arb("0.051")
    print(json.dumps({
        "kind": "actual_leading_W_linear_square_on_C1",
        "canonical_eventual_upper": "0.061",
        "alpha_free_merged_labels_upper": "0.051",
        "rank_four_relative_coefficient_upper": "0.812",
        "mixed_legendre_relative_coefficient_upper": "0.844",
        "bits": inherited["ctx"].prec,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
