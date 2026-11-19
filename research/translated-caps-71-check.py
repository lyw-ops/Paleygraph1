"""Outward comparison of three translated covers on actual prime-97 defects."""

from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx


def main():
    face = runpy.run_path(str(Path(__file__).with_name("astra-face-54-check.py")))
    ctx.prec = 320
    plus, minus = face["faces"]()
    n = len(minus)
    assert plus[0][0] > minus[0]
    reps = face["active"][1] + face["free"]
    support = sorted({i for j in reps for i in {j, -j % n}})
    signs = list(map(int, face["mask"]))
    root = arb(n).sqrt()

    def kernel(x):
        return [z.real for z in acb.dft([s*z for s, z in zip(signs, acb.dft(x))],
                                       inverse=True)]

    col = kernel([arb(1)] + [arb(0)] * (n-1))
    pin = [1 + x + arb(1)/n for x in col]
    state = [arb(0)] * n
    profiles = []
    for _ in range(22):
        phi = [(state[0]**2 + 4).sqrt()] + [abs(x) for x in state[1:]]
        raw = [root * (x-y) / 2 for x, y in zip(phi, state)]
        mean = sum(raw) / n
        projected = [(x + mean - y) / 2 for x, y in zip(raw, kernel(raw))]
        assert projected[0] > 0
        shift = (1 + arb(1)/1000) * projected[0]/root - mean
        profiles.append([projected[i] + shift * pin[i] for i in support])
        state = kernel(phi)

    counts = []
    for i in range(len(support)):
        levels = [sum(profiles[j][i] for j in range(a, a + 3)) / 3 + arb(1)/20
                  for a in range(1, 20)]
        assert all(x < 0 or x > 0 for x in levels)
        counts.append(sum(x < 0 for x in levels))
    demand = [arb(k)/19 for k in counts]

    w = [x/minus[0] for x in minus]
    masks = []
    for h in range(1, n):
        budget = 1-w[-h]
        assert budget > 0
        masks.append([w[(i-h) % n]/budget for i in support])

    inverse_cap = []
    for column in zip(*masks):
        cap = arb(1)
        for value in column:
            cap = cap.max(value)
        inverse_cap.append(cap)

    # These rational prices are frozen proposals, checked directly below.
    nonnegative = {
        1: 54416, 4: 214218, 5: 149799, 19: 69896, 23: 29347,
        24: 220620, 25: 57333, 28: 24766, 29: 40232,
        43: 120135, 44: 238983, 47: 66904,
    }
    signed = {
        1: 74533568, 9: -10839930, 10: 746141833, 12: 19545938,
        15: -178675161, 16: 12738985, 20: 239363451, 21: -230078718,
        26: -472268335, 28: 263374148, 32: -22547125, 35: -151113276,
        38: 138574654, 42: -117425788, 43: -248073933, 44: -31414389,
        45: -156470333, 47: 242582778,
    }
    old_dual = {
        2: 489792, 5: 795244, 7: 79716, 8: 621292, 13: 849131,
        22: 746644, 26: 678046, 35: 850149, 40: 282365, 41: 249180,
        43: 814613, 46: 487781,
    }
    cap_dual = {2: 368170, 5: 717395, 6: 386220, 8: 491339, 13: 717395,
                22: 112879, 35: 706789, 40: 508659, 42: 506388, 43: 706789,
                46: 362871}
    signed = [signed.get(h, 0) + 100 for h in range(1, n)]
    nonnegative = [nonnegative.get(h, 0) for h in range(1, n)]
    dual = [arb(old_dual.get(i, 0))/10**6 for i in support]
    assert all(sum(t * a**2 for t, a in zip(dual, row)) < 1 for row in masks)
    lower = sum(Fraction(old_dual.get(i, 0)*k, 19*10**6) for i, k in zip(support, counts))
    dual_cap = [arb(cap_dual.get(i, 0)) / 10**6 for i in support]
    assert all(sum(t * a * s for t, a, s in zip(dual_cap, row, inverse_cap)) < 1
               for row in masks)
    lower_cap = sum(Fraction(cap_dual.get(i, 0)*k, 19*10**6)
                    for i, k in zip(support, counts))
    for prices, denominator in ((nonnegative, 10**6), (signed, 10**8)):
        for needed, column, cap in zip(demand, zip(*masks), inverse_cap):
            coverage = sum(arb(c)*a for c, a in zip(prices, column)) * cap / denominator
            assert coverage > needed
    upper_nonnegative = Fraction(sum(nonnegative), 10**6)
    upper_signed = Fraction(sum(signed), 10**8)
    assert upper_signed < lower_cap <= upper_nonnegative < lower
    print(json.dumps(dict(p=97, precision=ctx.prec, candidate_sign=-1,
                          starts=[1, 19], window_length=3, allowance="1/1000",
                          cutoff="1/20", nonzero_site_counts=[[i,k] for i,k in zip(support,counts) if k],
                          unscaled_square_cover_lower=str(lower),
                          unscaled_cap_cover_lower=str(lower_cap),
                          unscaled_cap_cover_upper=str(upper_nonnegative),
                          unscaled_signed_cap_cover_upper=str(upper_signed)), sort_keys=True))


if __name__ == "__main__":
    main()
