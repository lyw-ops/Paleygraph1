"""Outward-rounded transport and root-orthogonal cold histories on true endpoints."""
import importlib.util
import json
from pathlib import Path

from flint import arb, ctx

source = Path(__file__).with_name("astra-late-51-check.py")
spec = importlib.util.spec_from_file_location("late", source)
late = importlib.util.module_from_spec(spec)
spec.loader.exec_module(late)
ep = late.endpoint
ctx.prec = 384


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def run(q, root=0):
    signs = late.square_field_sign(root) if root else late.paley_sign(q)
    n = len(signs)
    rn = arb(n).sqrt()
    if root:
        side = 1
        large = [arb(root-1)/rn if i % (root-1) == 0 else arb(0) for i in range(n)]
    else:
        pair, err = ep.solve_prime_pair(signs)
        assert not err, err
        side = 1 if pair[1][0] > pair[-1][0] else -1
        large = pair[side]
    tau = -side
    e = [arb(1)] + [arb(0)]*(n-1)
    p = ep.apply_multiplier(e, [int(v == tau) for v in signs])
    h = p[0]
    small = [1/rn+large[0]*x for x in p] if root else pair[tau]
    alpha, beta = large[0], small[0]
    c = (beta-1/rn)/h
    rep = [1/rn+c*x for x in p]
    residual = [v-w for v, w in zip(small, rep)]
    assert sum(residual).contains(0) and residual[0].contains(0)
    if root:
        assert all(x.contains(0) for x in residual)
    v = [arb(0)]*n
    B = A = H = neg_sum = arb(0)
    records = []
    seed = {}
    for t in range(1, 17):
        activation = [abs(x) for x in v]
        activation[0] = (4+v[0]**2).sqrt()
        bump = activation[0]-abs(v[0])
        g = sum(activation)/(2*rn)
        old_rep = tau*dot(rep, v)
        old_hinge = dot(rep, [ep.positive_part(-tau*x) for x in v])
        B += 2-bump
        A += (1-g)**2
        H += 2*dot(large, [ep.positive_part(-side*x) for x in v])
        neg_sum += dot(residual, [ep.positive_part(-tau*x) for x in v])
        v = ep.apply_multiplier(activation, signs)
        pv = ep.apply_multiplier(v, [int(s == tau) for s in signs])
        mark = (activation[0]-2*g/rn+tau*v[0])/2
        projected = [tau*x-mark*y/h for x, y in zip(pv, p)]
        assert (mark-tau*pv[0]).contains(0) and projected[0].contains(0)
        m = side*dot(large, v)
        other = tau*dot(small, v)
        assert (other-c*mark-2*neg_sum).contains(0)
        assert (2*old_hinge-c*mark+old_rep+beta*bump-2*g).contains(0)
        E = dot(v,v)
        C = dot(v, ep.apply_multiplier(v, signs))
        assert (m-2*t*(alpha-1)+alpha*B-E/4-A-H).contains(0)
        assert (dot(residual, projected)-2*neg_sum).contains(0)
        z = [side*rn*x for x in v]
        dist = late.cross_distance(z, [rn*x for x in large], [rn*x for x in small])
        one_sided = (dist+m-other)/2
        # Full squared residual version, using signed mean gap as equality.
        sq_mismatch = sum((r-y)**2 for r,y in zip(residual, projected))
        rhs = 4*t*(alpha-1)-2*alpha*B+2*(A+H)-2*c*mark+mark**2/h+side*C/2
        assert (dot(residual, residual)+2*(m-other)-rhs-sq_mismatch).contains(0)
        if t == 1:
            for name, label, row in (("larger", side, large), ("smaller", tau, small)):
                proj = ep.apply_multiplier(e, [int(x == label) for x in signs])
                coeff = (row[0]-1/rn)/proj[0]
                trial_density = [1+rn*coeff*x for x in proj]
                hinge = [ep.positive_part(-2-label*rn*x) for x in v]
                signed = dot(trial_density, hinge)/n
                actual = dot(row, hinge)/rn
                seed[name] = dict(representer=str(signed), correction=str(actual-signed))
        if t in (4,8,16):
            assert one_sided.upper() >= (m-other).lower()
            records.append(dict(t=t, transport=str(dist), upward=str(one_sided),
                                mark_pairing=str(c*mark), residual_tail_sum=str(neg_sum),
                                square_cost_lower=str(m-c*mark) if root else None))
    print(json.dumps(dict(q=q, side=side, alpha=str(alpha), beta=str(beta),
                          residual_norm2=str(dot(residual, residual)), rows=records, seed=seed),
                     sort_keys=True), flush=True)


if __name__ == "__main__":
    for q, root in [(101,0),(173,0),(401,0),(121,11),(961,31)]:
        run(q,root)
