"""Replay the two-floor and tangent identities at two true p=173 points."""

from fractions import Fraction
import json
from pathlib import Path
import runpy

from flint import acb, arb
import numpy as np


phase = runpy.run_path(str(Path(__file__).with_name("astra-phase-86-check.py")))
monodromy = phase["src"]
base, n, size = monodromy["base"], monodromy["n"], monodromy["N"]
rat, K = monodromy["rat"], monodromy["K"]
x = phase["x"]
mult = [1] + [2] * (size - 2) + [1]


def weighted_sum(values):
    return sum((count * value for count, value in zip(mult, values)), arb(0))


def square_abs(value):
    return value.real**2 + value.imag**2


def relative_logs(t, phi, u):
    bulk_root = (t / n).sqrt()
    return [((a+b) / (2 if i == 0 else 2*bulk_root)).log()
            for i, (a, b) in enumerate(zip(phi, u))]


def interval_floor(t):
    return ((n-1) / arb(n) + 1/t).sqrt()


def compare(y, real_logs, true_phi, true_u, enlarged):
    t = acb(rat(x), rat(y))
    logs = relative_logs(t, true_phi, true_u)
    angles = [z.imag for z in logs]
    co = [a.cos() for a in angles]
    assert all(c > 0 for c in co)
    assert max(a.lower() for a in angles)-min(a.upper() for a in angles) > arb.pi()/2
    bound = (arb(3)/2).atan()
    if enlarged:
        assert all(abs(a) < bound for a in angles)
    else:
        assert any(abs(a) > bound for a in angles)

    delta = [(a-b)/2 for a, b in zip(logs, real_logs)]
    sh, ch = delta[0].sinh(), delta[0].cosh()
    root, reference_root = (n/t).sqrt(), (n/acb(rat(x))).sqrt()
    center, difference = (root+reference_root)/2, (root-reference_root)/2
    ratio = abs(difference/center)
    mean_cost = n*square_abs(interval_floor(t)-interval_floor(acb(rat(x))))/4
    bulk = weighted_sum([arb(0)] + [c*square_abs(d.sinh())
                                      for c, d in zip(co[1:], delta[1:])])
    mark = co[0]*square_abs(center)*square_abs(sh)
    source = co[0]*square_abs(difference)*square_abs(ch)
    source -= 2*angles[0].sin()*(center*difference.conjugate()*sh*ch.conjugate()).imag
    assert (bulk+mark+mean_cost-source).contains(0)
    gamma = (1+abs(angles[0].sin()))/co[0]
    margin = 1-(ratio*gamma)**2
    assert margin > 0
    assert abs(sh) < ratio*gamma/margin.sqrt()
    assert bulk+mean_cost < co[0]*gamma**2*square_abs(difference)/margin

    # Differentiate the inherited polynomial stationary equations along t.
    rhs = monodromy["col"]([acb(0)]+[acb(4)/n]*(size-1))
    dphi = monodromy["jac"](true_phi,true_u).solve(rhs)
    du = K*dphi
    g = [-t*((dphi[i,0]+du[i,0])/(true_phi[i]+true_u[i])
             -(0 if i == 0 else 1/(2*t))) for i in range(size)]
    doubled = [(2*a).cos() for a in angles]
    loss = abs(t)*weighted_sum([arb(0)]+[c*square_abs(v)
                                         for c, v in zip(doubled[1:],g[1:])])/n
    mark_speed = doubled[0]*(g[0].real**2+(g[0].imag+(2*angles[0]).tan()/2)**2)
    W = 1+(n-1)*t/n
    assert (loss+mark_speed-(1/doubled[0]-1/abs(W))/4).contains(0)
    assert any(c < 0 for c in doubled[1:])
    print(json.dumps(dict(kind="actual_post_spread_two_floor_identity",prime=173,
        real=str(x),imag=str(y),enlarged_sector=enlarged,
        marked_log_difference=abs(2*delta[0]).str(8),weight_ratio=ratio.str(8),
        normalized_weighted_bulk_discrepancy=(bulk/n).str(8),
        normalized_retained_mean_cost=(mean_cost/n).str(8),
        signed_tangent_bulk_loss=loss.str(8),
        negative_cosine_orbits=[i for i,c in enumerate(doubled) if c < 0],
        precision=monodromy["ctx"].prec),sort_keys=True))


def main():
    weights = [arb(4)]+[4*rat(x)/n]*(size-1)
    u = base["real_root"](monodromy["Kr"],monodromy["sign"],rat(x),weights)
    phi = [(a*a+w).sqrt() for a,w in zip(u,weights)]
    real_logs = relative_logs(acb(rat(x)),[acb(a) for a in phi],[acb(a) for a in u])
    seed = np.array([complex(float(a),0) for a in phi])
    left = monodromy["anchor"](seed,(x,Fraction(0)))
    assert monodromy["vmax"]([acb(a)-b for a,b in zip(phi,left[0])]) < arb(2)**-40
    first, last = phase["first"],phase["last"]
    seed,left,_ = phase["walk"](Fraction(0),first,seed,left,"before")
    seed,left,_ = phase["walk"](first,last,seed,left,"crossing")
    seed,left,radius = phase["walk"](last,last,seed,left,"crossing")
    s,v,_ = phase["tube_data"](last,last,left,left,radius)
    compare(last,real_logs,s,v,True)
    after = Fraction(11,500)
    seed,left,_ = phase["walk"](last,after,seed,left,"after")
    seed,left,radius = phase["walk"](after,after,seed,left,"after")
    s,v,_ = phase["tube_data"](after,after,left,left,radius)
    compare(after,real_logs,s,v,False)


if __name__ == "__main__":
    main()
