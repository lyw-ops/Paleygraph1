"""Certify the effect of erasing the true signed quotient-cost heads at p=769."""
import json
from pathlib import Path
import runpy

from flint import arb, ctx, fmpq
import numpy as np
from scipy.optimize import linprog

base = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
ctx.prec = 384


def replay():
    p, n, m, b, J = 769, 384, 8, 48, 16
    signs = list(map(int, base["paley_sign"](p)))
    state = [arb(0)] * n
    costs = [arb(0)] * b
    for j in range(J):
        erase = 2+2*j
        assert erase % b
        for r in range(1, b):
            numerator = sum(state[r::b])
            if erase % b == r:
                numerator -= state[erase]
            costs[r] += numerator / (m*J)
        source = list(map(abs, state))
        source[0] = (4*n+state[0]**2).sqrt()
        state = base["apply"](source, signs)
    heads = []
    for threshold, expected in [(arb(13)/10, {10, 38}), (arb(6)/5, {10, 12, 36, 38})]:
        head = {r for r, cost in enumerate(costs) if cost > threshold}
        assert head == expected
        assert all(costs[r] < threshold for r in range(b) if r not in head)
        heads.append(head)
    # The order-six positional subgroup is an allowed clique. Its Fourier-square
    # law is exactly uniform on the eight characters divisible by six.
    assert all(signs[8*j] == 1 for j in range(8, b, 8))
    assert not heads[0].intersection(range(0, b, 6))
    trial_charge = sum(costs[::6])/8
    # An opposite-sector trigonometric majorant off the four deleted blocks
    # gives the all-law root upper by taking expectations against any trial.
    forbidden = [j for j in range(1, b//2+1) if signs[8*j] == -1]
    keep = [r for r in range(b) if r not in heads[1]]
    rows = [[arb(1)] + [arb.cos_pi_fmpq(fmpq(2*r*j,b)) for j in forbidden] for r in keep]
    fitted = linprog([1]+[0]*len(forbidden), A_ub=-np.asarray(rows, dtype=float),
                     b_ub=[-int(r == 0) for r in keep], bounds=(None, None),
                     method="highs")
    assert fitted.success
    coeff = [arb(round(float(x)*10**10))/10**10 for x in fitted.x]
    coeff[0] += arb(1)/10**8
    for r, row in zip(keep, rows):
        assert sum(a*z for a, z in zip(coeff, row)) > int(r == 0)
    assert coeff[0] < arb(76456)/10**6
    return dict(prime=p, group_order=n, horizon=J, block_order=m, sign=1,
                precision_bits=ctx.prec, physical_erasure="2+2j",
                hot_above_13_over_10=sorted(heads[0]), hot_above_6_over_5=sorted(heads[1]),
                two_head_trial_root="1/8", two_head_trial_support=list(range(0,b,6)),
                eroded_signed_trial_charge_before_root_division_units_1e_minus_9=base["enclose"](trial_charge),
                four_head_all_law_root_strict_upper="0.076456",
                four_head_majorant_mean_units_1e_minus_9=base["enclose"](coeff[0]))


if __name__ == "__main__":
    print(json.dumps(replay(), sort_keys=True))
