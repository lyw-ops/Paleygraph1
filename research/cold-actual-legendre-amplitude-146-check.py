"""Replay a cold amplitude bound and a positive-comparison obstruction."""

from collections import defaultdict
from contextlib import redirect_stdout
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


DIRECTORY = Path(__file__).resolve().parent
AMPLITUDE = Fraction("0.244")
TRIAL = (
    8973227569, 3772133028, 1926411861, 1031686615,
    569461640, 320358146, 182624039, 105087972,
    60826244, 35210557, 20055269, 10331046,
)


def check_selected_rate(prices):
    folded = defaultdict(Fraction, prices["retained_coefficients"](legendre=False))
    linear = prices["legendre_fibers"](prices["retained_coefficients"](legendre=True))
    for weight, value in linear.items():
        folded[weight] += AMPLITUDE * value
    rho = prices["RHO"]
    cut = prices["ORDERS"]
    pure_tail = 4 * prices["JACOBI_PREFACTOR"] * rho**cut * (
        (cut + 1) / (1 - rho) + rho / (1 - rho)**2
    )
    linear_tail = 8 * prices["LEGENDRE_PREFACTOR"] * rho**cut * (
        2 * rho * (1 + rho) / (1 - rho)**3
        + (4 * cut + 3) * rho / (1 - rho)**2
        + (cut + 1) * (2 * cut + 1) / (1 - rho)
    )
    upper = prices["column_bound"](folded) + pure_tail + AMPLITUDE * linear_tail
    assert upper < Fraction("0.6333")
    assert Fraction("0.487") * AMPLITUDE < Fraction("0.119")
    assert 2 * Fraction("0.528") * Fraction("0.119") < Fraction("0.126")
    assert Fraction("0.634")**2 < Fraction("0.402")
    assert Fraction("0.402") + Fraction("0.598") == 1
    assert Fraction("0.634") + Fraction("0.366") == 1
    assert Fraction("0.580184") + Fraction("0.017") * Fraction("1.048") == Fraction("0.598")


def positive_witness(folded, arb):
    def signed_mass(weight):
        return folded[abs(weight)] / (2 if weight else 1)

    for output, target in enumerate(TRIAL, 1):
        image = sum(
            count * ((source - 1) * folded[output]
                     + signed_mass(output - source) + signed_mass(output + source))
            for source, count in enumerate(TRIAL, 1)
        )
        assert image > arb("1.035") * target, output


def main():
    prices = runpy.run_path(str(DIRECTORY / "cold-jacobi-linear-legendre-145-check.py"))
    with redirect_stdout(io.StringIO()):
        prices["main"]()
        prior = runpy.run_path(str(DIRECTORY / "cold-combined-height-130-check.py"))
    arb = prior["arb"]
    assert prior["pars"][0] < arb("0.244")
    check_selected_rate(prices)

    h = prior["h"]
    core, norm = prior["residual"](h)
    positive_witness(prior["retained"](core, 1), arb)

    activation = prior["retained"](core, 0)
    _, ratio = prior["tail_ratio"](norm)
    leak = prior["old"]["polynomial"](prior["norms"], norm)
    leak -= sum(value * weight for value, weight in zip(activation, prior["tilt"]))
    leak += 2 * abs(prior["t"]).sqrt() * abs(prior["bn"]) * ratio**15 / (1 - ratio)
    assert 0 <= leak < prior["eps"]
    next_h = [value.upper() for value in activation[1:]]
    next_h[0] += prior["tol"]
    assert prior["center_mass"] + sum(
        weight * value for weight, value in enumerate(next_h, 1)
    ) + 4 * prior["eps"] < arb("4.8")
    next_core, _ = prior["residual"](next_h)
    positive_witness(prior["retained"](next_core, 1), arb)

    assert Fraction("1.035")**2 == Fraction("1.071225")
    print(json.dumps({
        "kind": "actual_legendre_amplitude_selected_block",
        "amplitude_upper": "0.244",
        "geometric_joint_upper": "0.6333",
        "eventual_joint_upper": "0.634",
        "eventual_linear_upper": "0.119",
        "eventual_mixed_two_step_upper": "0.126",
        "eventual_joint_square_upper": "0.402",
    }, sort_keys=True))
    print(json.dumps({
        "kind": "retained_direct_positive_repricing_obstruction",
        "heights": [601, 602],
        "principal_weights": len(TRIAL),
        "single_step_lower": "1.035",
        "two_step_lower": "1.071225",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
