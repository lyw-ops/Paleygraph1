"""Certify a weighted hinge and the leverage cost of deleting one terminal site."""
import json
from pathlib import Path
import runpy

from flint import arb, arb_mat, ctx


root = Path(__file__).resolve().parent
prior = runpy.run_path(str(root / "astra-split-83-check.py"))
terminal = prior["terminal"]
units = terminal["units"]
ctx.prec = 384


def weighted_hinge():
    n, time = 48, 4
    primary, opposite = prior["face"]["faces"]()
    signs = list(map(int, prior["face"]["mask"]))
    height = terminal["terminal_field"](signs, 1, time)
    assert all(h > 0 or h.is_zero() for h in height)
    q = [row[0] for row in primary]
    support = [i for i in range(1, n) if opposite[i].is_zero()]
    mask = [i for i in support if height[i] > 0]
    threshold = (1-q[0])/(5*arb(n).sqrt())
    weight = {i: n*(1+height[i])/time for i in mask}
    assert all(q[i] > threshold or q[i] < threshold for i in mask)
    z = {i: (q[i]-threshold).max(0) for i in mask}
    f = {i: weight[i]*z[i] for i in mask}
    hinge = sum(f[i]*z[i] for i in mask)
    floor = sum(f[i]*q[i] for i in mask)
    assert hinge > 0 and (floor-hinge-threshold*sum(f.values())).contains(0)
    assert primary[10][0].is_zero() and primary[10][2].is_zero() and primary[10][1] > 0
    assert primary[21][0].is_zero() and primary[21][1].is_zero() and primary[21][2] > 0
    assert all(q[i] > 0 or q[i].is_zero() for i in range(n))
    assert all(sum(f[i]*primary[i][k] for i in mask) > 0 for k in (1, 2))
    marked_energy = sum(weight[i]*q[i]**2 for i in mask)
    inverse_metric = {i: weight.get(i, 1/(time*q[0])) for i in support}
    assert all(sum(inverse_metric[i]*q[i]*primary[i][k] for i in support) > 0
               for k in (1, 2))
    inverse = 1+sum(inverse_metric[i]*q[i]**2 for i in support)
    dual_lower = floor**2/hinge
    assert hinge < dual_lower and dual_lower < marked_energy
    high = [i for i in mask if q[i] > 2*threshold]
    assert all(q[i] > 2*threshold or q[i] < 2*threshold for i in mask)
    high_height = sum(q[i]*height[i] for i in high)
    assert hinge > n*threshold*high_height/(2*time)
    return dict(prime=97,time=time,mask_on_exposed_support=mask,high_sites=high,
                weighted_hinge=units(hinge),linear_floor=units(floor),
                weighted_collision_floor=units(dual_lower),masked_energy=units(marked_energy),
                positive_inverse_leverage=units(inverse),high_height=units(high_height),
                precision_bits=ctx.prec,units="1e-9")


def one_site_frontier(p, time, pivot):
    source = terminal["prior"]
    signs = source["paley_sign"](p)
    pair, error = source["solve_prime_pair"](signs)
    assert error is None
    n = len(signs)
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    even = [v/arb(n).sqrt() for v in pair[side]]
    positive = [j for j in range(1, n//2) if even[j] > 0]
    exposed = {j for j in range(1, n) if pair[-side][j].is_zero()}
    assert exposed == set(positive) | {n-j for j in positive}
    forbidden = [j for j in range(1, n//2) if signs[j] == -side]
    columns = [j for j in positive if j != pivot]
    assert len(columns) == len(forbidden) and pivot in positive
    sine = [(arb(2*j)/n).sin_pi() for j in range(n)]
    matrix = arb_mat([[sine[j*k % n] for k in columns] for j in forbidden])
    entries = list(matrix.solve(arb_mat([[-sine[j*pivot % n]] for j in forbidden])))
    odd = [arb(0)]*n
    for j, value in zip([pivot]+columns, [arb(1)]+entries):
        odd[j], odd[-j] = value,-value
    # With unit pivot the true upper endpoint is at most even[pivot].
    candidates = [j for j in positive if abs(odd[j])*even[pivot] > even[j]/2]
    binding = min(candidates,key=lambda j: float((even[j]/abs(odd[j])).mid()))
    end = even[binding]/abs(odd[binding])
    assert end > 0 and all(j == binding or even[j] > end*abs(odd[j]) for j in positive)

    height = terminal["terminal_field"](list(map(int, signs)), side, time)
    assert all(h > 0 or h.is_zero() for h in height)
    total = sum(height[i]*even[i] for i in exposed)
    weights = {i: n*(1+height[i])/time if height[i] > 0 else 1/(time*even[0])
               for i in exposed}
    base = 1+sum(weights[i]*even[i]**2 for i in exposed)
    increase = end**2*sum(weights[i]*odd[i]**2 for i in exposed)
    assert increase > 0
    assert sum(height[i]*odd[i] for i in exposed).contains(0)
    assert sum(weights[i]*even[i]*odd[i] for i in exposed).contains(0)

    def residual(fraction):
        pair_max = {j: height[j]*(even[j]+fraction*end*abs(odd[j])) for j in positive}
        j = max(positive,key=lambda j: float(pair_max[j].mid()))
        assert all(k == j or pair_max[k] < pair_max[j] for k in positive)
        return total-pair_max[j], j

    samples = [residual(s) for s in [arb(0),arb(1)/2,arb(1)]]
    assert samples[0][0] > samples[1][0] and samples[1][0] > samples[2][0]
    return dict(prime=p,time=time,side=side,odd_pivot=pivot,binding_orbit=binding,
                inverse_leverage_even=units(base),inverse_norm_full_increase=units(increase),
                total_height=units(total),best_deleted_orbits=[j for _,j in samples],
                one_site_residuals_at_displacement_0_half_full=[units(v) for v,_ in samples],
                full_erasure_gain=units(samples[0][0]-samples[2][0]),
                precision_bits=ctx.prec,units="1e-9")


if __name__ == "__main__":
    for record in (weighted_hinge(),one_site_frontier(257,5,48),one_site_frontier(409,6,95)):
        print(json.dumps(record,sort_keys=True))
