"""Outward replay of full-face descent for the same physical height and root."""
import json
import runpy
from pathlib import Path

from flint import arb, arb_mat, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-split-83-check.py")))
ctx.prec = 384
units = prior["interval"]


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), arb(0))


def model():
    n = 48
    face = prior["face"]
    full, opposite = face["faces"]()
    row = [j for j in range(1, n) if opposite[j].is_zero()]
    assert row == [j for j in range(1, n) if any(not v.is_zero() for v in full[j])]
    signs = list(map(int, face["mask"]))
    # Reconstruct, including the hinge minimizer, fixed head, and terminal mask.
    receipt = prior["check"]()
    heads = set(receipt["common_head"])
    h = prior["terminal"]["terminal_field"](signs, 1, 4)
    g = [int(i in heads)+v/4 for i, v in enumerate(h)]
    apply = prior["terminal"]["prior"]["apply_multiplier"]
    state = [arb(0)]*n
    energy = [arb(1)/n]*n
    for _ in range(4):
        phi = [(4+state[0]**2).sqrt()] + [abs(v) for v in state[1:]]
        state = apply(phi, signs)
        energy = [v+y*y for v, y in zip(energy, state)]

    A = arb_mat([list(full[j][1:])+[-energy[j] if j != 19 else arb(0)]
                 for j in (3,22,19)])
    base = list(A.solve(arb_mat([[-full[j][0]] for j in (3,22,19)])))[:2]
    return row, full, h, g, energy, base


def run(scale_num, scale_den):
    row, full, h, g, energy, base = model()
    n = 48
    cap = [v*scale_num/scale_den for v in energy]
    for j in row:
        if h[j] > 0:
            cap[j] = cap[j].min(arb(4)/(n*(1+h[j])))
        else:
            assert h[j].is_zero()
        assert cap[j] > 0

    def point(t):
        return [v + dot([x,z], t) for v,x,z in full]

    def validate(q, zeros):
        assert (sum(q)-1).contains(0) and (q[0]-full[0][0]).contains(0)
        for j in row:
            if j in zeros:
                assert q[j].contains(0)
                q[j] = arb(0)
            else:
                assert q[j] > 0
        assert all(j == 0 or j in row or q[j].is_zero() for j in range(n))

    def cost(q):
        return sum(g[j]*(q[j]-cap[j]).max(0) for j in row)

    def gradient(q):
        assert all(q[j] < cap[j] or q[j] > cap[j] for j in row)
        return [sum(g[j]*full[j][l] for j in row if q[j] > cap[j]) for l in (1, 2)]

    gram = [[sum(full[j][k]*full[j][l]/cap[j] for j in row)
             for l in (1, 2)] for k in (1, 2)]
    assert gram[0][0] > 0 and arb_mat(gram).det() > 0
    t = base
    records = []
    for k in range(2 if scale_num*5 == scale_den else 1):
        q = point(t)
        validate(q, {19,29} if k == 0 else {10,38})
        grad = gradient(q)
        if k == 0:
            dt = prior["solve"](gram, [-v for v in grad])
        else:
            # At this boundary the first anchored variable must increase or stay zero.
            dt = [arb(0), -grad[1]/gram[1][1]]
            assert grad[0]+gram[0][1]*dt[1] > 0
        d = [dot(v[1:],dt) for v in full]
        descent = sum(d[j]**2/cap[j] for j in row)
        assert descent > 0 and (descent+dot(dt, grad)).contains(0)
        assert d[19] > 0
        end = -t[k]/dt[k]
        assert end > 0
        newt = [v+end*u for v,u in zip(t,dt)]
        assert newt[k].contains(0)
        newt[k] = arb(0)  # exactly zero by choice of end
        other = point(newt)
        validate(other, {10,38} if k == 0 else {10,21,27,38})
        assert d[10 if k == 0 else 21] < 0
        final_grad = gradient(other)
        assert dot(final_grad,dt) < 0
        crossed = [j for j in row if (q[j] > cap[j]) != (other[j] > cap[j])]
        charged = [j for j in crossed if g[j] > 0]
        loss = sum((g[j]*abs(other[j]-cap[j]) for j in crossed), arb(0))
        assert (cost(other)-cost(q)+end*descent-loss).contains(0)
        if scale_num*5 == scale_den:
            assert not charged
        else:
            assert charged == [21,27] and loss > arb(12)/10000
        records.append(dict(start=units(cost(q)),end=units(cost(other)),
                            squared_slope=units(descent),length=units(end),
                            reenter_19_velocity=units(d[19]),charge_crossings=charged,
                            crossing_loss=units(loss) if charged else [0,0]))
        t = newt

    out = dict(prime=97,time=4,capacity_scale=[scale_num,scale_den],
               metric="joint coordinate capacities",precision=ctx.prec,units="1e-9",
               steps=records)
    if scale_num*5 == scale_den:
        q = point([arb(0),arb(0)])
        validate(q, {10,21,27,38})
        assert all(v > 0 for v in gradient(q))
        # Keeping site 19 zero leaves one affine coordinate, parametrized by
        # the second nonnegative anchor. Convexity and the strict right
        # derivative at zero certify its exact constrained minimum.
        v = full[19]
        locked = point([-v[0]/v[1],arb(0)])
        validate(locked,{19,21,27,29})
        right = dot(gradient(locked), [-v[2]/v[1],arb(1)])
        assert right > 0 and cost(locked)-cost(q) > arb(14)/1000
        # A genuine opposite field attains the one-sided quadratic trace
        # quotient. Interpolation is only on the exact complementary zero set.
        charge = [j for j in row if g[j] > 0]
        excess = [(q[j]-cap[j]).max(0)/cap[j] if j in charge else arb(0)
                  for j in range(n)]
        slopes = [sum(full[j][l]*excess[j] for j in row) for l in (1,2)]
        assert all(v > 0 for v in slopes)
        sq = sum(cap[j]*excess[j]**2 for j in charge)
        metric = sum(cap[j]*g[j]**2 for j in charge)
        sites = [j for j in range(1,n//2+1) if q[j] > 0]
        signs = prior["face"]["mask"]
        modes = [j for j in range(1,n//2+1) if signs[j] == -1]
        cos = [(arb(2*j)/n).cos_pi() for j in range(n)]
        coeff = prior["solve"]([[cos[i*j % n] for j in modes] for i in sites],
                               [excess[i] for i in sites])
        field = [dot(coeff,[cos[i*j % n] for j in modes]) for i in range(n)]
        assert all(field[j]<0 for j in (10,21,27,38))
        assert all((field[j]-excess[j]).contains(0) for j in row if q[j] > 0)
        revenue = sum(field)/n-q[0]*field[0]
        debit = sum(cap[j]*field[j].max(0) for j in charge)
        denominator_sq = sum(cap[j]*field[j].max(0)**2 for j in charge)
        assert (sq-denominator_sq).contains(0) and (revenue-debit-sq).contains(0)
        # For finite A=1/5 retain the actual below-cap norm rather than the
        # asymptotic O(d^-1/2) bound, which assumes A>=2.
        _, opposite = prior["face"]["faces"]()
        outside = [j for j in range(1,n) if opposite[j] > 0]
        neutral = [u-field[0]*r/opposite[0] for u,r in zip(field,opposite)]
        assert neutral[0].contains(0)
        masked = [neutral[j] if j in outside else arb(0) for j in range(n)]
        apply = prior["terminal"]["prior"]["apply_multiplier"]
        projector = [int(s == 1) for s in signs]
        cols = [arb(n).sqrt()*v for v in apply(masked,projector)]
        jstar = max([0]+outside, key=lambda j:float(abs(cols[j]).mid()))
        jstar = min(jstar,(-jstar) % n)
        assert all(abs(cols[jstar]) > abs(cols[j]) for j in [0]+outside
                   if j not in {jstar,(-jstar)%n})
        assert (cols[jstar]-cols[(-jstar)%n]).contains(0)
        ej = [arb(int(j == jstar)) for j in range(n)]
        col = apply(ej,projector)
        assert cols[jstar] > 0 or cols[jstar] < 0
        sign = -1 if cols[jstar] > 0 else 1
        wt = [(1+sign*arb(n).sqrt()*u)/n for u in col]
        assert all(wt[j] > 0 and wt[j] < arb(2)/n for j in row)
        exterior = sum(masked)/n
        saved = abs(cols[jstar])/n
        actual_debit = sum((wt[j]-cap[j]).max(0)**2/cap[j] for j in charge).sqrt()
        assert (dot(wt,neutral)-sum(neutral)/n).contains(0)
        assert (sum(wt[j]*neutral[j] for j in outside)-exterior+saved).contains(0)
        assert revenue-debit < exterior-saved+actual_debit*sq.sqrt()
        out.update(jacobi_response_center=jstar, signed_exterior=units(exterior),
                   signed_exterior_saving=units(saved), selected_cap_error_norm=units(actual_debit),
                   quadratic_trace_squared=units(sq),weighted_squared_demand=units(metric),
                   joint_trace_upper=units((sq*metric).sqrt()),
                   global_minimum=units(cost(q)),locked_19_minimum=units(cost(locked)),
                   locked_price_gap=units(cost(locked)-cost(q)),locked_right_slope=units(right))
    return out


if __name__ == "__main__":
    for scale in ((1,5),(3,20)):
        print(json.dumps(run(*scale),sort_keys=True))
