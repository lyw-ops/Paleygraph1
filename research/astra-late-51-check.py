"""Check two-endpoint coverage and consecutive true cold scores using Arb."""
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from flint import arb, ctx
from scipy.optimize import linear_sum_assignment

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from square_control import square_field_sign
from theta import paley_sign

spec = importlib.util.spec_from_file_location("endpoint", ROOT / "research/endpoint-direction-45-check.py")
endpoint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(endpoint)
ctx.prec = 320


def lower_min(x, y):
    return min(x.lower(), y.lower()).union(min(x.upper(), y.upper()))


def cross_distance(z, rho, other):
    """Integrate the empirical CDF difference after rounding the support."""
    n = len(z)
    atoms = [(v.mid(), x/n) for v,x in zip(z,rho)] + [(-v.mid(), -x/n) for v,x in zip(z,other)]
    atoms.sort(key=lambda item: item[0])
    prefix = distance = arb(0)
    last = atoms[0][0]
    for point, weight in atoms:
        distance += (point-last)*abs(prefix)
        prefix += weight
        last = point
    error = sum(v.rad()*(x+y) for v,x,y in zip(z,rho,other))/n
    return distance + arb(0, error.upper())


def verify(q, square_root=0):
    sign = square_field_sign(square_root) if square_root else paley_sign(q)
    n = len(sign)
    root_n = arb(n).sqrt()
    if square_root:
        side = 1
        rho = [arb(square_root - 1 if i % (square_root - 1) == 0 else 0) for i in range(n)]
        kernel = endpoint.apply_multiplier([arb(1)] + [arb(0)]*(n-1), [int(s == -1) for s in sign])
        # The zero tail of the true square optimum follows from complementarity.
        other = [arb(0) if i and rho[i] > 0 else 1 + rho[0]*k for i, k in enumerate(kernel)]
    else:
        pair, error = endpoint.solve_prime_pair(sign)
        assert error is None
        side = 1 if pair[1][0] > pair[-1][0] else -1
        rho = [root_n*v for v in pair[side]]
        other = [root_n*v for v in pair[-side]]
    alpha, beta = rho[0]/root_n, other[0]/root_n
    assert alpha > beta and (alpha*beta-1).contains(0)
    assert (sum(other)-n).contains(0)
    r = (sum(x*x for x in rho)/n).sqrt()
    history = [[arb(0)]*n]
    bumps, gvals = [], []
    for t in range(8):
        v = [y/root_n for y in history[-1]]
        phi = [abs(x) for x in v]
        phi[0] = (4+v[0]*v[0]).sqrt()
        bumps.append(phi[0]-abs(v[0]))
        gvals.append(sum(phi)/(2*root_n))
        history.append([root_n*x for x in endpoint.apply_multiplier(phi, sign)])
    h = np.array([[float(x) for x in ys] for ys in history]).T
    costs = np.max(abs(h[:,None,:]+h[None,:,:]), axis=2)**2
    _, perm = linear_sum_assignment(np.rint(costs*1e8).astype(np.int64))
    assert sorted(perm) == list(range(n))
    directed_edges = [(i,int(j)) for i,j in enumerate(perm)]
    edges = directed_edges + [(j,i) for i,j in directed_edges]
    L = len(edges)
    budget = (sum(max(abs(y[i]+y[j]).upper() for y in history)**2 for i,j in edges)/L).sqrt()
    H = A = B = arb(0)
    previous_distance = cross_distance(history[0], rho, other)
    rows = []
    for t in range(8):
        z = [side*y for y in history[t]]
        znew = [side*y for y in history[t+1]]
        a = sum(x*abs(y) for x,y in zip(rho,z))/n
        other_a = sum(x*abs(y) for x,y in zip(other,z))/n
        other_m = -sum(x*y for x,y in zip(other,z))/n
        next_m = sum(x*y for x,y in zip(rho,znew))/n
        other_next = -sum(x*y for x,y in zip(other,znew))/n
        b, g = bumps[t], gvals[t]
        assert (next_m-a-alpha*b+2*g).contains(0)
        assert (next_m-other_next-a+other_a-b*(alpha-beta)).contains(0)
        distance = cross_distance(znew, rho, other)
        distance_slack = previous_distance+distance-b*(alpha-beta)
        assert distance_slack.lower() >= 0 or distance_slack.contains(0)
        previous_distance = distance
        H += other_a-other_m
        B += 2-b
        A += (1-g)**2
        energy_next = sum(y*y for y in znew)/n
        assert (other_next-(2*(beta-1)*(t+1)-beta*B+energy_next/4+A+H)).contains(0)
        if t < 2:
            continue
        assert distance_slack > 0
        c = sum(lower_min(rho[i],rho[j])*abs(z[i]) for i,j in edges)/(L*a)
        union = sum(lower_min(rho[i],rho[j]+other[j])*abs(z[i]) for i,j in edges)/(L*a)
        # Only the fresh coverage beyond what was already supplied by rho_j.
        extra = sum((lower_min(rho[i],rho[j]+other[j])-lower_min(rho[i],rho[j]))
                    *abs(z[i]+z[j]) for i,j in edges)/L
        gap = other_next-(a*(union-c)-extra+beta*b-2*g)
        assert gap > 0 and extra < r*budget
        assert (other_next-other_a-beta*b+2*g).contains(0)
        if square_root:
            h = square_root
            assert union-c < arb(2*h)/(h*h-1)
            independent_gain = sum(other[j] for j in range(n) if rho[j] == 0)/((h-1)*n)
            assert (independent_gain-arb(h-2)/(h-1)**2).contains(0)
        rows.append(dict(t=t,same=str(c),combined=str(union),extra_pair_error=str(extra),
                         cross_wasserstein_next=str(distance), cross_pair_slack=str(distance_slack),
                         opposite_next=str(other_next),coverage_slack=str(gap)))
    print(json.dumps(dict(q=q, side=side, alpha=str(alpha), beta=str(beta), checks=rows), sort_keys=True))


if __name__ == "__main__":
    for q, root in ((101,0),(173,0),(121,11),(961,31)):
        verify(q,root)
