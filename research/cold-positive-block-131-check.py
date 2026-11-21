"""Outward lower witness for two retained positive Schur comparison matrices."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import runpy


source = Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):
    old = runpy.run_path(str(source / "cold-combined-height-130-check.py"))

arb = old["arb"]
tilt = old["tilt"]
retained, residual, tail_ratio = old["retained"], old["residual"], old["tail_ratio"]
h = old["h"]
trial = [1000000, 420376, 214684, 114974, 63462, 35702,
         20352, 11711, 6779, 3924, 2235, 1151]
size = len(trial)
lower = arb(1036)/1000

for depth in (601, 602):
    core, norm = residual(h)
    masses = retained(core, 1)
    image = [arb(0)] * (size + 1)
    for k, count in enumerate(trial, 1):
        for j, mass in enumerate(masses):
            if 1 <= j <= size:
                image[j] += (k-1) * count * mass
            for shift in (k+j, abs(k-j)):
                if 1 <= shift <= size:
                    image[shift] += count * mass / 2
    ratios = [entry/count for entry, count in zip(image[1:], trial)]
    assert all(ratio > lower for ratio in ratios)
    print(json.dumps({
        "kind": "positive_comparison_subeigenvector",
        "height": depth, "retained_columns": size,
        "coordinate_ratio_lower": str(min(ratio.lower() for ratio in ratios)),
        "rational_strict_lower": "1.036",
    }, sort_keys=True))
    if depth == 602:
        continue
    _, ratio = tail_ratio(norm)
    activation = retained(core, 0)
    loss = old["old"]["polynomial"](old["norms"], norm)
    loss -= sum(x*w for x, w in zip(activation, tilt))
    loss += 2*abs(old["t"]).sqrt()*abs(old["bn"])*ratio**15/(1-ratio)
    assert 0 <= loss < old["eps"]
    h = [x.upper() for x in activation[1:]]
    h[0] += old["tol"]
    assert old["center_mass"] + sum(k*x for k, x in enumerate(h, 1)) + 4*old["eps"] < arb("4.8")

print(json.dumps({"kind": "positive_comparison_two_step_lower",
                  "heights": [601, 602], "rational_strict_lower": "1.073296"},
                 sort_keys=True))
