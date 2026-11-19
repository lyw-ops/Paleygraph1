"""Outward checks for conditional Fourier modulation and centered affine transport."""
import json
from itertools import permutations
from pathlib import Path
import runpy
import sys

from flint import acb, arb, ctx

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
old = runpy.run_path(str(here / "astra-matched-88-check.py"))
prior = old["prior"]
equal, units, positions = (old[name] for name in ("equal", "units", "positions"))
from theta import prime_field_generator

ctx.prec = 384


def audit(p, pivot):
    signs = prior["paley_sign"](p)
    pair, error = prior["solve_prime_pair"](signs)
    assert error is None
    n = len(signs)
    q, r = [[a/arb(n).sqrt() for a in pair[s]] for s in (1, -1)]
    if pivot is not None:
        old["add_odd"](r, -1, pivot, signs)
    F, R = positions(q), positions(r)
    for row, spec, side in ((q, F, 1), (r, R, -1)):
        equal(sum(row), 1)
        assert all(a.is_zero() or a > 0 for a in row)
        for k in range(1, n):
            if signs[k] != side:
                equal(spec[k], 0)
    equal(n*q[0]*r[0], 1)
    g = prime_field_generator(p)
    log = {pow(g, 2*i, p): i for i in range(n)}
    phases = [acb(0, arb.pi()*2*i/n).exp() for i in range(n)]
    root = arb(p).sqrt()
    u, v = (11, 2) if p == 53 else (2, 3)
    d = 3 if n % 3 == 0 else 2
    bins = [[] for _ in range(d)]
    for z in range(p):
        x, y, w = (log.get(k % p) for k in (u*u*z, v*v*(z+1), z+2))
        if (x is not None and y is not None and w is not None
                and signs[x] == 1 and signs[y] == -1):
            bins[w % d].append((x, y))
    assert all(bins)
    j = pivot if pivot is not None else max(range(1, n), key=lambda k: float(q[k]))
    source_is_minus = pivot is not None
    t = j if source_is_minus else -j
    atom = 0 if source_is_minus else j
    mu = [n*q[i]*r[(i+t) % n] for i in range(n)]
    mu_spec = positions(mu)
    equal(sum(mu), 1)
    equal(mu[atom], r[j]/r[0] if source_is_minus else q[j]/q[0])
    equal(mu[-t % n] if source_is_minus else mu[0], 0)
    if source_is_minus:
        equal(q[j]+q[-j], 0)
        assert r[j] > r[-j]
    else:
        equal(r[j]+r[-j], 0)
    unmod, recentered, charges, real_lower, complex_lower = [], [], [], [], []
    scalar_transport = arb(0)
    for entries in bins:
        measured = [acb(0), acb(0)]
        prices = [R[y].real-F[x].real for x, y in entries]
        charges.append(sum(prices)/root)
        for (x, y), price in zip(entries, prices):
            raw = sum(m*phases[(i*x-(i+t)*y) % n] for i, m in enumerate(mu))
            moved = raw*phases[(-atom*x+(atom+t)*y) % n]
            equal(raw, phases[-t*y % n]*mu_spec[(x-y) % n])
            equal(moved, phases[-atom*(x-y) % n]*mu_spec[(x-y) % n])
            measured[0] += price*raw/root
            measured[1] += price*moved/root
        unmod.append(measured[0])
        recentered.append(measured[1])
        for real_scores, target in ((True, real_lower), (False, complex_lower)):
            columns = [([R[y] for x, y in entries], [y for x, y in entries]),
                       ([F[x] for x, y in entries], [x for x, y in entries])]
            if not source_is_minus:
                columns.reverse()
            centered, angles = [], []
            for values, logs in columns:
                if real_scores:
                    values = [value.real for value in values]
                mean = sum(values)/len(values)
                centered.append([value-mean for value in values])
                angles.append([phases[-j*k % n] for k in logs])
                equal(sum(centered[-1]), 0)
            X, Y = centered
            hx, hy = angles
            left = abs(sum(a*h for a,h in zip(X,hx)))
            right = [abs(sum(a*(h if sign == 1 else h.conjugate())
                             for a,h in zip(Y,hy))) for sign in (1,-1)]
            lower = min(abs(left-w) for w in right)
            target.append(lower/root)
            if real_scores:
                costs = [sum(abs(a-b) for a,b in zip(X,ys)) for ys in permutations(Y)]
                low = min(cost.lower() for cost in costs)
                high = min(cost.upper() for cost in costs)
                scalar_transport += low.union(high)/root
            # Check pointwise decomposition, allowing reversals of order,
            # conjugation of phase and a free additional rotation in the bin.
            for reverse, sign, rotation in ((False, 1, 0), (True, -1, 3)):
                lhs = rhs = arb(0)
                for i in range(len(X)):
                    k = len(X)-1-i if reverse else i
                    l, m = hx[i], hy[k] if sign == 1 else hy[k].conjugate()
                    m *= phases[rotation]
                    lhs += abs(X[i]*l-Y[k]*m)
                    rhs += abs(X[i]-Y[k])+min(abs(X[i]),abs(Y[k]))*abs(l-m)
                assert lhs.upper() >= lower.lower() and rhs.upper() >= lhs.lower()

    # Multiple genuine modes against every possible scalar third-coset fit.
    cloud = []
    for side, row in enumerate((q,r)):
        ids = sorted(range(1,n), key=lambda i: float(row[i]+row[-i]), reverse=True)[:3]
        cloud.extend((side, i, (row[i]+row[-i])/2) for i in ids)
    mass_norm = sum(w*w for _,_,w in cloud).sqrt()
    assert mass_norm > 0
    correlation = acb(0)
    gram = residual_sq = arb(0)
    for entries in bins:
        scores = [R[y].real-F[x].real for x,y in entries]
        tests = [sum((1 if side == 0 else -1)*w*phases[-i*(x,y)[side] % n]
                     for side,i,w in cloud)/mass_norm for x,y in entries]
        centered_tests = [val-sum(tests)/len(tests) for val in tests]
        centered_scores = [val-sum(scores)/len(scores) for val in scores]
        equal(sum(centered_tests),0)
        equal(sum(centered_scores),0)
        for D,T in zip(centered_scores,centered_tests):
            correlation += D*T
            residual_sq += D*D
            gram += abs(T)**2
    assert gram > 0
    cloud_lower = abs(correlation)/gram.sqrt()
    assert cloud_lower > 0
    assert cloud_lower.lower() <= residual_sq.sqrt().upper()
    # Quotient Fourier/total-variation identity for the real unweighted price.
    expected = n*(r[0]-q[0])/(8*d*root)
    delta = [a-expected for a in charges]
    spec = acb.dft(delta)
    equal(sum(a*a for a in delta), sum(abs(b)**2 for b in spec)/d)
    assert sum(real_lower) > 0 and sum(complex_lower) > 0
    return dict(prime=p, bits=ctx.prec, units="1e-9", probes=[u,v], index=d,
                bin_counts=list(map(len,bins)), character=j, displacement=t % n,
                six_mode_cloud_norm=units(mass_norm), least_squares_norm=units(residual_sq.sqrt()),
                six_mode_finite_lower=units(cloud_lower),
                atom=atom, conditional_atom=units(mu[atom]),
                raw_conditional_price=[[units(z.real),units(z.imag)] for z in unmod],
                centered_conditional_price=[[units(z.real),units(z.imag)] for z in recentered],
                signed_price=units(sum(charges)), centered_signed_price=[0,0],
                real_all_rotation_coupling_lower=units(sum(real_lower)),
                complex_all_rotation_coupling_lower=units(sum(complex_lower)),
                scalar_only_optimal_centered_transport=units(scalar_transport),
                root_atoms=[units(q[j]),units(q[-j]),units(r[j]),units(r[-j])])


if __name__ == "__main__":
    for values in ((53, None), (257, 48), (409, 95)):
        print(json.dumps(audit(*values), sort_keys=True), flush=True)
