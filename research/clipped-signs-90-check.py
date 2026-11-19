"""Check the actual unforced angle data in the clipped-defect lower bound."""

from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, arb
import numpy as np


phase = runpy.run_path(str(Path(__file__).with_name("astra-phase-86-check.py")))
branch = phase["src"]
n, size = branch["n"], branch["N"]
x, rat = phase["x"], branch["rat"]


def main():
    weights = [arb(4)] + [4 * rat(x) / n] * (size - 1)
    u = branch["base"]["real_root"](branch["Kr"], branch["sign"], rat(x), weights)
    spectrum = [(entry * entry + weight).sqrt() for entry, weight in zip(u, weights)]
    seed = np.array([complex(float(a), 0) for a in spectrum])
    left = branch["anchor"](seed, (x, Fraction(0)))
    assert branch["vmax"]([acb(a) - b for a, b in zip(spectrum, left[0])]) < arb(2)**-40
    first, last = phase["first"], phase["last"]
    seed, left, _ = phase["walk"](Fraction(0), first, seed, left, "before")
    seed, left, _ = phase["walk"](first, last, seed, left, "crossing")
    seed, left, radius = phase["walk"](last, last, seed, left, "crossing")
    _, _, angles = phase["tube_data"](last, last, left, left, radius)

    cap = (1 / arb(2).sqrt()).atan()
    overshoot = rat("0.28")
    assert angles[phase["upper_site"]] > cap + overshoot
    spread = max(a.upper() for a in angles) - min(a.lower() for a in angles)
    assert spread < arb.pi()/2 + rat("65") * rat("0.00003")
    assert all(abs(a) < phase["outer"] for a in angles)
    theta = abs(acb(rat(x), rat(last)).arg())
    assert theta / 2 < cap
    assert abs(angles[0]) + theta / 2 < rat("0.85")
    assert phase["outer"] + cap < rat("1.6")
    assert (rat("0.85") + rat("1.6")) / 2 < arb.pi()/2

    common_cosine = ((spread + 2 * cap) / 2).cos()
    assert common_cosine > arb(1)/7
    bound = 4 * (overshoot / 2).sin() / (7 * arb(20).sqrt())
    assert bound > arb(1)/60
    print(json.dumps(dict(
        kind="actual_phase_witness_for_clipped_total_defect", prime=173, real=str(x),
        imag=str(last), kappa=2, upper_phase_lower_bound=angles[phase["upper_site"]].lower().str(9),
        common_cosine_lower="1/7", overshoot_lower="0.28",
        total_bulk_correction_strict_lower="1/60", precision=branch["ctx"].prec,
    ), sort_keys=True))


if __name__ == "__main__":
    main()
