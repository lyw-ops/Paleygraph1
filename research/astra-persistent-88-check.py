"""Whole even-face coordinate capacities and masked quartic moment at 97."""
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx

root = Path(__file__).resolve().parent
prior = runpy.run_path(str(root / "astra-split-83-check.py"))
face = prior["face"]
ctx.prec = 384


def coordinate_caps(rows):
    # The anchor/mark ratios are in [0,1] by translation optimality.
    rational = [tuple(face["rounded"](v) for v in row) for row in rows]
    err = Fraction(6, face["scale"])
    zero = Fraction(0)
    one = Fraction(1)
    constraints = [(zero, one, zero), (one, -one, zero),
                   (zero, zero, one), (one, zero, -one)]
    constraints.extend((a+err,b,c) for a,b,c in rational if a or b or c)
    outer = set()
    for a,b in combinations(constraints,2):
        point = face["intersection"](a,b)
        if point and all(face["at"](row,point) >= 0 for row in constraints):
            outer.add(point)
    assert outer
    mix = Fraction(1,10**11)
    anchor = Fraction(1,10000)
    inner = [tuple(face["rb"](x*(1-mix)+anchor*mix) for x in p) for p in outer]
    assert all(face["at"](row,pt) >= 0 for row in rows for pt in inner)
    bounds = []
    for exact,rounded in zip(rows,rational):
        if all(v.is_zero() for v in exact):
            bounds.append((arb(0),arb(0)))
            continue
        low = max(face["at"](exact,p).lower() for p in inner)
        high = face["rb"](max(face["at"](rounded,p) for p in outer)+err).upper()
        assert low <= high and high-low < arb(1)/10**11
        bounds.append((low,high))
    return bounds


def main():
    rows,opp = face["faces"]()
    cap = coordinate_caps(rows)
    n = len(rows)
    even = [row[0] for row in rows]
    assert rows[10][0].is_zero() and rows[10][2].is_zero() and rows[10][1]>0
    assert rows[21][0].is_zero() and rows[21][1].is_zero() and rows[21][2]>0
    price = prior["terminal"]["terminal_field"](list(map(int,face["mask"])),1,4)
    charged = [i for i in range(1,n) if price[i]>0]
    assert all(v > 0 or v.is_zero() for v in price)
    fourth = sum((n*even[i])**4 for i in charged)/n
    derivatives = [sum(4*(n*even[i])**3*rows[i][k] for i in charged) for k in (1,2)]
    assert min(derivatives)>0
    # Every optimizer's reflection average belongs to the genuine two-parameter face.
    weighted = [(n*(1+price[i])/4 if i in charged else 1/(4*even[0]))
                for i in range(n)]
    support = [i for i in range(1,n) if opp[i].is_zero()]
    assert all(sum(weighted[i]*even[i]*rows[i][k] for i in support)>0 for k in (1,2))
    inv = 1+sum(weighted[i]*even[i]**2 for i in support)
    collision = sum((n*even[i])**2 for i in charged)/n
    residual = sum(weighted[i]*even[i]**2 for i in support if i not in charged)
    # Evaluate a clipped-height comparison with a rational cutoff chosen independently
    # of the final interval enclosures.
    def bound_at(cut):
        tail = (sum((price[i]-cut).max(0)**2 for i in charged)/n).sqrt()
        return 1 + residual + ((1+cut)*collision+tail*fourth.sqrt())/4
    candidates = [(arb(j)/100,bound_at(arb(j)/100)) for j in range(701)]
    cut,upper = min(candidates,key=lambda z:float(z[1].mid()))
    assert upper > inv and upper < bound_at(arb(0)) and upper < bound_at(arb(7))
    interval = prior["interval"]
    print(json.dumps(dict(prime=97,precision_bits=384,units="1e-9",
        normalized_fourth_moment=interval(fourth),
        comparison_inverse_norm=interval(inv),terminal_time=4,
        even_capacity_mass=[interval(sum(t[0] for t in cap[1:]))[0],
                            interval(sum(t[1] for t in cap[1:]))[1]],
        envelope_sites_above_d_over_n={str(d): count_at(cap,d,n) for d in (1,2,4,8)},
        clipped_comparison_upper=interval(upper),clip_centis=round(float((cut*100).mid())),
        quartic_derivatives=[interval(v) for v in derivatives]),sort_keys=True))


def count_at(cap,d,n):
    assert all(n*hi < d or n*lo > d for lo,hi in cap[1:])
    return sum(n*lo > d for lo,_ in cap[1:])


def check_delayed_companion():
    signs = list(map(int,face["mask"]))
    n, horizon = len(signs),24
    root_n = arb(n).sqrt()
    apply = prior["terminal"]["prior"]["apply_multiplier"]
    projected,companions,means,energies = [],[],[],[]
    state = [arb(0)]*n
    column = [z.real for z in acb.dft([int(x == -1) for x in signs],inverse=True)]
    for j in range(horizon+1):
        phi = [(4+state[0]**2).sqrt()] + list(map(abs,state[1:]))
        energies.append(sum(v*v for v in state))
        means.append(root_n*sum(phi)/(2*n))
        projected.append(apply([root_n*(v-y)/2 for v,y in zip(phi,state)],
                               [int(x in (0,-1)) for x in signs]))
        companions.append(apply([root_n*(v+y)/2 for v,y in zip(phi,state)],
                                [int(x in (0,1)) for x in signs]))
        state = apply(phi,signs)
    assert all((energies[j+1]-energies[j]-4*(1-means[j]**2)).contains(0)
               for j in range(horizon))
    scores = [v+arb(j)/256 for j,v in enumerate(energies)]
    T = max(range(len(scores)),key=lambda j:float(scores[j].mid()))
    assert all(j==T or scores[T] > v for j,v in enumerate(scores))
    b = T-2
    assert T==13 and max(means[b-1:b+2]) < 2
    Z = companions[b]
    records = []
    for d in (2,4,8):
        start = b-d+1
        weights = [arb(1 if j==b else 2)/(2*d-1) for j in range(start,b+1)]
        times = list(range(start,b+1))
        mean_sq = sum(w*means[j]**2 for w,j in zip(weights,times))
        telescoped = 1+(2*energies[start]-energies[b]-energies[b+1])/(4*(2*d-1))
        assert (mean_sq-telescoped).contains(0)
        raw = [sum(w*projected[j][i] for w,j in zip(weights,times)) for i in range(n)]
        inc = (1+arb(1)/20)*raw[0]/root_n-sum(raw)/n
        assert inc > 0
        pin = [v+inc*(1-c/column[0]) for v,c in zip(raw,column)]
        u = arb(1)/100
        assert all(v < -u or v > -u for v in pin[1:])
        mask = [i for i in range(1,n) if pin[i]<-u]
        assert all(pin[i]+Z[i]/(2*d-1) > 0 for i in range(1,n))
        ratio = d**2*sum(pin[i]**2/(1+Z[i]) for i in mask)/n
        second = sum((-v).max(0)**2 for v in pin[1:])/n
        assert second < ((arb(d).sqrt()+arb(d-1).sqrt())/(2*d-1))**2
        records.append(dict(d=d,mask_size=len(mask),ratio=prior["interval"](ratio)))
    common = sum(v.max(0) for v in Z[1:])/n
    print(json.dumps(dict(prime=97,horizon=horizon,tilt_denominator=256,
        tilted_record=T,terminal_time=b,allowance="1/20",deficit_cutoff="1/100",
        companion_bulk_positive_mean=prior["interval"](common),
        lengths=records,precision_bits=384,units="1e-9"),sort_keys=True))


if __name__ == "__main__":
    main()
    check_delayed_companion()
