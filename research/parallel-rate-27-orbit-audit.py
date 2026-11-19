"""Independently check the q=61 certified prefix with a dense Arb matrix.

The certificate program uses Arb FFTs. This script constructs the same
operator from direct cosine sums and evolves the actual orbit at 192 bits.
Only this script's stdout is used for the saved audit records.
"""

from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from theta import paley_sign


def actual_norm(vector):
    return sum((entry*entry for entry in vector), arb(0)).sqrt()


def require_lower(label, encoded_bound, actual):
    if not arb(encoded_bound).upper() < actual.lower():
        raise RuntimeError(f"{label} lower bound was not verified")


def require_upper(label, encoded_bound, actual):
    if not arb(encoded_bound).lower() > actual.upper():
        raise RuntimeError(f"{label} upper bound was not verified")


def main():
    prime = 61
    steps = 16
    tau = Fraction(1, 20)
    command = [
        sys.executable, "-B", str(ROOT/"research/harmonic-orbit-27.py"),
        str(prime), "--steps", str(steps), "--tau", str(tau), "--root-budget",
    ]
    certificate_bytes = subprocess.check_output(command, cwd=ROOT)
    certificate_rows = [json.loads(line) for line in certificate_bytes.splitlines()]
    certificates = [row for row in certificate_rows if row["kind"] == "step"]
    prefix = certificate_rows[-1]
    if len(certificates) != steps or prefix["kind"] != "prefix_audit":
        raise RuntimeError("the certificate prefix has an unexpected length")

    ctx.prec = 192
    signs = paley_sign(prime)
    n = len(signs)
    pi = arb.pi()
    coefficients = [
        sum((int(value)*(2*pi*offset*position/n).cos()
             for position, value in enumerate(signs)), arb(0))/n
        for offset in range(n)
    ]
    matrix = [[coefficients[(i-j) % n] for j in range(n)] for i in range(n)]

    def apply(vector):
        return [sum((a*b for a, b in zip(row, vector)), arb(0)) for row in matrix]

    activation_weights = [arb(4)]+[
        arb(4*tau.numerator)/(tau.denominator*n)
    ]*(n-1)

    def activate(vector):
        return [(entry*entry+weight).sqrt()
                for entry, weight in zip(vector, activation_weights)]

    state = [arb(0)]*n
    for step, certificate in enumerate(certificates):
        if certificate["step"] != step:
            raise RuntimeError("the certificate prefix is out of order")
        phi = activate(state)
        next_state = apply(phi)
        next_phi = activate(next_state)
        increment = [b-a for a, b in zip(state, next_state)]
        activation_increment = [b-a for a, b in zip(phi, next_phi)]
        next_increment = apply(activation_increment)
        energy = sum((entry*entry for entry in increment), arb(0))
        bulk_energy = sum((entry*entry for entry in increment[1:]), arb(0))
        bulk_loss = sum(
            (a*a-b*b for a, b in zip(increment[1:], activation_increment[1:])),
            arb(0),
        )/bulk_energy
        root_secant_squared = ((state[0]+next_state[0])/(phi[0]+next_phi[0]))**2
        mean_fraction = sum(activation_increment, arb(0))**2/(n*energy)
        energy_ratio = sum((entry*entry for entry in next_increment), arb(0))/energy

        require_lower("bulk activation loss", certificate["actual_bulk_loss_lower"], bulk_loss)
        require_upper("root secant", certificate["actual_root_secant_squared_upper"],
                      root_secant_squared)
        require_lower("mean reserve", certificate["actual_mean_reserve_fraction_lower"],
                      mean_fraction)
        require_upper("full energy ratio", certificate["actual_full_energy_ratio_upper"],
                      energy_ratio)
        print(json.dumps(dict(
            kind="independent_dense_step", order=prime, tau=str(tau), n=n,
            precision=ctx.prec, step=step,
            bulk_loss_enclosure=str(bulk_loss),
            root_secant_squared_enclosure=str(root_secant_squared),
            mean_reserve_fraction_enclosure=str(mean_fraction),
            energy_ratio_enclosure=str(energy_ratio),
            certified_bulk_loss_lower=certificate["actual_bulk_loss_lower"],
            certified_root_secant_squared_upper=certificate["actual_root_secant_squared_upper"],
            certified_mean_reserve_fraction_lower=certificate["actual_mean_reserve_fraction_lower"],
            certified_full_energy_ratio_upper=certificate["actual_full_energy_ratio_upper"],
        )))
        state = next_state

    residual = actual_norm([a-b for a, b in zip(apply(activate(state)), state)])
    labels = (
        "paired_residual_upper", "one_step_residual_upper",
        "bulk_path_residual_upper", "root_path_residual_upper",
    )
    for label in labels:
        require_upper(label, prefix[label], residual)
    print(json.dumps(dict(
        kind="independent_dense_prefix", order=prime, tau=str(tau),
        n=n, steps=steps, precision=ctx.prec,
        operator_evaluation="direct cosine sums and dense matrix multiplication",
        certified_orbit_integer_sha256=prefix["orbit_integer_sha256"],
        actual_final_residual_enclosure=str(residual),
        verified_residual_upper_bounds={label: prefix[label] for label in labels},
        status="all stepwise and final comparisons passed",
    )))


if __name__ == "__main__":
    main()
