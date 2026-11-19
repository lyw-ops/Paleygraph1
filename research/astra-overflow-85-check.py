"""Interval checks for positive and signed marked projections at prime 97."""
import json
import runpy
from pathlib import Path

from flint import acb, arb, arb_mat, ctx

base = Path(__file__).resolve().parent
previous = runpy.run_path(str(base / "astra-capacity-84-check.py"))
ctx.prec = 384
interval = previous["units"]
dot = previous["dot"]


def true_pin(signs, n):
    apply = previous["prior"]["terminal"]["prior"]["apply_multiplier"]
    state = [arb(0)]*n
    raw = [arb(0)]*n
    root = arb(n).sqrt()
    for time in range(5):
        phi = [(4+state[0]**2).sqrt()] + [abs(v) for v in state[1:]]
        if time:
            weight = arb(1 if time == 4 else 2)/7
            raw = [v+weight*root*(g-y)/2 for v,g,y in zip(raw,phi,state)]
        if time < 4:
            state = apply(phi, signs)
    projected = apply(raw, [int(s <= 0) for s in signs])
    column = [v.real for v in acb.dft([int(s == -1) for s in signs], inverse=True)]
    increment = (projected[0]/root-sum(raw)/n).max(0)
    return [v+increment*(1-c/column[0]) for v,c in zip(projected,column)]


def check():
    n = 48
    sites, full, h, g, energy, _ = previous["model"]()
    a = full[0][0]
    marks = [0]+sites
    w = [4*a]*n
    w[0] = a**2
    charge = [i for i in sites if g[i] > 0]
    for i in charge:
        w[i] = energy[i]/5
        if h[i] > 0:
            w[i] = w[i].min(arb(4)/(n*(1+h[i])))
    # Columns parameterize the whole reflected signed space after scaling.
    basis = arb_mat([[v/w[i].sqrt() for v in full[i]] for i in marks])
    gram = basis.transpose()*basis
    assert gram.det() > 0
    project = lambda v: basis * gram.solve(basis.transpose()*v)
    unit = arb_mat([[arb(int(i == 0))] for i in marks])
    rootcol = list(project(unit))
    lev = rootcol[0]
    signed = [w[i].sqrt()*z/lev for i,z in zip(marks,rootcol)]
    negative = {i for i,q in zip(marks,signed) if q < 0}
    assert negative == {2,10,21,27,38,46}
    assert all(q < 0 if i in negative else q > 0 for i,q in zip(marks,signed))
    assert (sum(signed)-1).contains(0) and (signed[0]-a).contains(0)

    # Positive minimum at the origin of the two nonnegative anchor parameters.
    assert all(full[i][0].is_zero() if i in {10,21,27,38} else full[i][0] > 0
               for i in marks)
    assert full[10][2].is_zero() and full[21][1].is_zero()
    assert full[10][1] > 0 and full[21][2] > 0
    assert gram[0,1] > 0 and gram[0,2] > 0
    pos_lev = 1/gram[0,0]
    pos_col = arb_mat([[pos_lev*full[i][0]/w[i].sqrt()] for i in marks])
    # Exterior nonnegative multipliers on the two binding reflected pairs.
    multiplier = [arb(0)]*n
    for i,k in ((10,1),(21,2)):
        multiplier[i] = multiplier[n-i] = pos_lev*gram[0,k]*w[i].sqrt()/(2*full[i][k])
        assert multiplier[i] > 0
    z = arb_mat([[multiplier[i]] for i in marks])
    assert all(t.contains(0) for t in (project(unit+z)-pos_col))
    assert (sum(t*t for t in pos_col)-pos_lev).contains(0)
    pz = list(project(z))
    rho_sq = dot(rootcol,pz)**2/(dot(rootcol,rootcol)*dot(pz,pz))
    assert dot(rootcol,pz) < 0 and (lev*(1-rho_sq)-pos_lev).contains(0)

    # Positive-price lower bound on reflection pair {2,46}, with equality.
    # q2 = floor + c*q3 + k*q10 identically on the even signed slice.
    coeff = list(arb_mat([[full[i][j] for i in (3,10)] for j in (1,2)])
                 .solve(arb_mat([[full[2][j]] for j in (1,2)])))
    assert all(v > 0 for v in coeff)
    floor = full[2][0]-dot(coeff, [full[3][0], full[10][0]])
    right = -full[3][0]/full[3][2]
    assert right > 0
    for i in marks:
        candidate = full[i][0]+right*full[i][2]
        if i in {3,10,38,45}:
            assert candidate.contains(0)
        else:
            assert candidate > 0
    assert (full[2][0]+right*full[2][2]-floor).contains(0)

    # The unnormalized physical identity holds with either sign of D.
    pin = true_pin(list(map(int,previous["prior"]["face"]["mask"])), n)
    u = arb(1)/100
    D = a*pin[0]-sum(pin)/n-u*(1-a)
    assert D < 0
    assert all((pin[i]+u < 0) == (h[i] > 0) for i in sites)
    pos = arb_mat([[arb(0) if i == 0 else w[i].sqrt()*(pin[i]+u).max(0)] for i in marks])
    neg = arb_mat([[arb(0) if i == 0 else w[i].sqrt()*(-pin[i]-u).max(0)] for i in marks])
    assert all(t.contains(0) for t in project(D*unit+pos-neg))

    return dict(prime=97, time=4, precision=ctx.prec, units="1e-9",
                capacity_scale=[1,5], uncharged_weight="4a", signed_leverage=interval(lev),
                positive_leverage=interval(pos_lev), squared_angle_correlation=interval(rho_sq),
                signed_negative_sites=sorted(negative),
                signed_pair_2_mass=interval(2*signed[marks.index(2)]),
                positive_minimum_pair_2_mass=interval(2*floor),
                full_positive_zero_pairs=[10,21], pin_D=interval(D))


if __name__ == "__main__":
    print(json.dumps(check(),sort_keys=True))
