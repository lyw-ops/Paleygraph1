"""Certify clipped entropy minima on two full one-dimensional primary faces."""
import json
import runpy
from pathlib import Path

from flint import arb, arb_mat, acb, ctx

base = Path(__file__).resolve().parent
prior = runpy.run_path(str(base / "endpoint-direction-45-check.py"))
ctx.prec = 384


def units(x):
    scale = 10**9
    return [int((x*scale).lower().floor().unique_fmpz()),
            int((x*scale).upper().ceil().unique_fmpz())]


def entropy(w):
    return sum(v*(len(w)*v).log() for v in w if v > 0)


def terminal_field(signs, side, b):
    n = len(signs)
    root = arb(n).sqrt()
    apply = prior["apply_multiplier"]
    state = [arb(0)] * n
    raw = [arb(0)] * n
    for t in range(b+1):
        phi = [(4+state[0]**2).sqrt()] + list(map(abs, state[1:]))
        if t:
            weight = arb(1 if t == b else 2)/(2*b-1)
            raw = [v + weight*root*(g-side*y)/2 for v, g, y in zip(raw,phi,state)]
        if t != b:
            state = apply(phi, signs)
    Z = apply([root*(g+side*y)/2 for g,y in zip(phi,state)],
              [int(v in (0,side)) for v in signs])
    column = [z.real for z in acb.dft([int(v == -side) for v in signs], inverse=True)]
    primary = apply(raw,[int(v in (0,-side)) for v in signs])
    inc = (primary[0]/root-sum(raw)/n).max(0)
    pinned = [v+inc*(1-c/column[0]) for v,c in zip(primary,column)]
    cutoff = -arb(1)/100
    assert all(v < cutoff or v > cutoff for v in pinned[1:])
    field = [z if j and pinned[j] < cutoff else arb(0) for j,z in enumerate(Z)]
    assert all((v-field[-j % n]).contains(0) for j,v in enumerate(field))
    return field


def cell_minimum(left, right, active):
    # In normalized coordinates this entire clipping cell is one line segment.
    n = len(left)
    direction = [b-a for a,b in zip(left,right)]
    lo, hi = arb(0), arb(1)
    for _ in range(60):
        theta = (lo+hi)/2
        probe = [a+theta*d for a,d in zip(left,direction)]
        assert all(probe[j] > 0 for j in active)
        log_density = {j:(n*probe[j]).log() for j in active}
        derivative = sum(direction[j]*v for j,v in log_density.items())
        if abs(derivative) < arb(1)/10**15:
            break
        if derivative > 0:
            hi = theta
        else:
            assert derivative < 0
            lo = theta
    # Relative entropy to this probe is nonnegative at every point of the cell.
    minorants = [sum(row[j]*v for j,v in log_density.items()) for row in (left,right)]
    low = min(v.lower() for v in minorants)
    high = sum(probe[j]*v for j,v in log_density.items()).upper()
    assert high-low < arb(1)/10**12
    return low, high, theta


def audit(p, b, pivot):
    signs = prior["paley_sign"](p)
    pair, fail = prior["solve_prime_pair"](signs)
    assert fail is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    assert pair[side][0] > pair[-side][0]
    n = len(signs)
    e = [v/arb(n).sqrt() for v in pair[side]]
    ids = [j for j in range(1,n//2) if e[j] > 0]
    freq = [j for j in range(1,n//2) if signs[j] == -side]
    assert len(ids) == len(freq)+1 and pivot in ids
    cosupport = [j for j in range(1,n) if pair[-side][j].is_zero()]
    assert set(cosupport) == set(ids) | {n-j for j in ids}
    sin = [(arb(2*j)/n).sin_pi() for j in range(n)]
    cols = [j for j in ids if j != pivot]
    mat = arb_mat([[sin[j*k % n] for k in cols] for j in freq])
    sol = list(mat.solve(arb_mat([[-sin[j*pivot % n]] for j in freq])))
    h = [arb(0)]*n
    for j,y in zip([pivot]+cols, [arb(1)]+sol):
        h[j], h[-j] = y,-y
    # The pivot bound (h[pivot]=1) suffices to discard tiny denominators.
    ratios = [(e[j]/abs(h[j]), j) for j in ids if abs(h[j])*e[pivot] > e[j]/2]
    end, binding = min(ratios,key=lambda item:float(item[0].mid()))
    assert all(j == binding or e[j] > end*abs(h[j]) for j in ids)
    cuts = [arb(0), end]
    floor = arb(1)/n
    for j in range(1,n):
        left, right = e[j]-floor, e[j]+end*h[j]-floor
        assert not left.contains(0) and not right.contains(0)
        if (left > 0) != (right > 0):
            cuts.append(-left/h[j])
    cuts.sort(key=lambda x:float(x.mid()))
    assert all(v>w for w,v in zip(cuts,cuts[1:]))
    lows, highs, locations = [],[],[]
    def clips(t):
        raw = [arb(0)]+[(q+t*y-floor).max(0) for q,y in zip(e[1:],h[1:])]
        mass = sum(raw)
        assert mass > 0
        return [v/mass for v in raw],mass
    for a,z in zip(cuts,cuts[1:]):
        ia, ma = clips(a)
        iz, mz = clips(z)
        test,_ = clips((a+z)/2)
        active = [j for j,v in enumerate(test) if v > 0]
        assert all(v > 0 or v.is_zero() for v in test)
        low, high, theta = cell_minimum(ia, iz, active)
        lows.append(low)
        highs.append(high)
        lam = theta*ma/(theta*ma+(1-theta)*mz)
        locations.append((a+lam*(z-a))/end)
    best = min(range(len(highs)),key=lambda j:float(highs[j]))
    global_min = min(lows).union(highs[best])
    even = entropy(clips(arb(0))[0])
    # The same attainable mass on the hard trial, now shared with the even split.
    _,target = clips(locations[best]*end)
    lower = [(v-floor).max(0) for v in e[1:]]
    upper = e[1:]
    assert target > sum(lower) and target < sum(upper)
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (hi+lo)/2
        mass = sum(min(float(v.mid()),max(float(w.mid()),mid)) for v,w in zip(upper,lower))
        if mass > float(target.mid()):
            hi = mid
        else:
            lo = mid
    low_set = [j for j,w in enumerate(lower) if w > mid]
    high_set = [j for j,w in enumerate(upper) if w < mid]
    free = set(range(n-1))-set(low_set)-set(high_set)
    assert free
    level = (target-sum(lower[j] for j in low_set)-sum(upper[j] for j in high_set))/len(free)
    assert all(lower[j]>level for j in low_set) and all(upper[j]<level for j in high_set)
    assert all(upper[j]>level>lower[j] for j in free)
    split = [arb(0)]+[w.max(level).min(v)/target for v,w in zip(upper,lower)]
    projected = entropy(split)
    assert projected < global_min
    assert even-global_min > arb(5)/10000
    field = terminal_field(signs,side,b)
    height = sum(v*x for v,x in zip(field,e))
    assert sum(v*x for v,x in zip(field,h)).contains(0)
    return dict(prime=p, time=b, side=side, floor_B=1, odd_pivot=pivot,
                odd_constraint_rank=len(freq), binding_pair=binding, cells=len(lows),
                even_entropy=units(even), full_min_entropy=units(global_min),
                entropy_gain=units(even-global_min), achieving_trial_fraction=units(locations[best]),
                common_masked_height=units(height), same_trial_mass=units(target),
                projected_entropy=units(projected), projected_floor_level=units(level), precision_bits=ctx.prec, units="1e-9")


if __name__ == "__main__":
    for args in [(257,5,48),(409,6,95)]:
        print(json.dumps(audit(*args),sort_keys=True),flush=True)
