"""Verify endpoint-weighted antipodal cancellation on genuine cold histories."""
import importlib.util
import json
from pathlib import Path
import sys

from flint import arb, ctx
import numpy as np
from scipy.optimize import linear_sum_assignment

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from theta import paley_sign
from square_control import square_field_sign

spec = importlib.util.spec_from_file_location("endpoint", ROOT / "research/endpoint-direction-45-check.py")
endpoint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(endpoint)
ctx.prec = 320


def sorted_balls(values):
    lower = sorted(x.lower() for x in values)
    upper = sorted(x.upper() for x in values)
    return [a.union(b) for a, b in zip(lower, upper)]


def verify(q, root, start=2, terminal=8):
    sign = square_field_sign(root) if root else paley_sign(q)
    n = len(sign)
    if root:
        side = 1
        rho = [arb(root-1 if i % (root-1) == 0 else 0) for i in range(n)]
    else:
        pair, err = endpoint.solve_prime_pair(sign)
        assert err is None
        side = 1 if pair[1][0] > pair[-1][0] else -1
        assert pair[side][0] > pair[-side][0]
        rho = [arb(n).sqrt()*x for x in pair[side]]
    alpha = rho[0]/arb(n).sqrt()
    delta = alpha-1
    Y = [arb(0)]*n
    H = A = B = arb(0)
    histories, weights = [], []
    wrong, baselines, means = [], [], []
    for t in range(terminal+1):
        w = [side*r*y for r, y in zip(rho, Y)]
        mass = sum(w)/n
        energy = sum(y*y for y in Y)/n
        F = 2*delta*t-alpha*B+energy/4+A
        assert (mass-(F+H)).contains(0)
        histories.append(Y)
        weights.append(w)
        wrong.append(H)
        baselines.append(F)
        means.append(mass)
        signal = [abs(y)/arb(n).sqrt() for y in Y]
        old = signal[0]
        signal[0] = (4+old*old).sqrt()
        B += 2-(signal[0]-old)
        A += (1-sum(signal)/(2*arb(n).sqrt()))**2
        H += sum(abs(v)-v for v in w)/n
        Y = [arb(n).sqrt()*z for z in endpoint.apply_multiplier(signal, sign)]

    # Bistochastic cost minimization for the entire unweighted history.
    # Only the proposed permutation and its verified cost are used below.
    approx = np.array([[float(x) for x in row] for row in histories]).T
    costs = np.max(abs(approx[:,None,:]+approx[None,:,:]), axis=2)**2
    _, perm = linear_sum_assignment(np.rint(costs*1e8).astype(np.int64))
    assert sorted(perm) == list(range(n))
    rms = (sum(max(abs(row[i]+row[j]).upper() for row in histories)**2
               for i,j in enumerate(perm))/n).sqrt()
    constant = min(F.lower() for F in baselines[start:terminal+1])
    assert constant+wrong[start] > 0
    product = arb(1)
    details = []
    for t in range(start, terminal):
        w = weights[t]
        H0 = constant+wrong[t]
        H1 = constant+wrong[t+1]
        a = sum(abs(v) for v in w)/n
        ordered = sorted_balls(w)
        antitone_sums = [x+y for x,y in zip(ordered, reversed(ordered))]
        assert all(z == 0 or z > 0 for z in antitone_sums)
        best = sum(abs(z) for z in antitone_sums)/(2*n*a)
        proposed = sum(abs(w[i]+w[j]) for i,j in enumerate(perm))/(2*n*a)
        assert (best-means[t]/a).upper() >= 0
        assert (proposed-best).upper() >= 0
        assert (H1*best-H0).upper() >= 0
        if q == 101:
            assert best > arb(9975)/10000
        if q == 173 and t == 2:
            assert best < arb(9674)/10000
            assert proposed > arb(9967)/10000
        if q == 121:
            assert all(v == 0 or v > 0 for v in w)
        product /= best
        details.append(dict(time=t, all_antitone_pairs_nonnegative=True, best_unrestricted_defect=str(best), history_plan_defect=str(proposed),
                            signed_fraction=str(means[t]/a)))
    bound = (constant+wrong[terminal])/(constant+wrong[start])
    if q == 121:
        assert (bound-1).contains(0) and (product-1).contains(0)
    else:
        assert bound > product
    print(json.dumps(dict(order=q, sign=side, start=start, terminal=terminal, mark=str(alpha),
                          history_rms_upper=str(rms.upper()), inverse_defect_product=str(product),
                          available_growth=str(bound), checkpoints=details), sort_keys=True))


if __name__ == "__main__":
    for q, root in [(101,0),(173,0),(121,11),(961,31)]:
        verify(q, root)
