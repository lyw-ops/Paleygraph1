"""Certify a common optimizer head and least energy-envelope cap at prime 97."""
import json
import runpy
from pathlib import Path

from flint import acb, arb, arb_mat, ctx

base = Path(__file__).resolve().parent
face = runpy.run_path(str(base / "astra-face-54-check.py"))
terminal = runpy.run_path(str(base / "astra-optimal-82-check.py"))
ctx.prec = 384


def interval(value):
    scaled = value * 10**9
    return [int(scaled.lower().floor().unique_fmpz()),
            int(scaled.upper().ceil().unique_fmpz())]


def solve(matrix, rhs):
    return list(arb_mat(matrix).solve(arb_mat([[v] for v in rhs])))


def linear_price(row, field):
    return sum((a*b for a, b in zip(row, field)), arb(0))


def check():
    n = 48
    primary, opposite = face["faces"]()
    side, signs = 1, list(map(int, face["mask"]))
    price = terminal["terminal_field"](signs, side, 4)
    marked = [i for i in range(1,n) if price[i] > 0]
    q = [row[0] for row in primary]
    M = 1-q[0]
    alpha = arb(1)/5
    t = alpha*M/arb(n).sqrt()
    y = [(q[i]-t).max(0) if i in marked else arb(0) for i in range(n)]
    assert all(q[i] > t or q[i] < t for i in marked)
    v = [w/sum(y) for w in y]
    # Nonnegative free anchor coordinates and positive derivatives certify
    # that the undisplaced even row minimizes the actual squared hinge.
    assert primary[10][0].is_zero() and primary[10][2].is_zero() and primary[10][1]>0
    assert primary[21][0].is_zero() and primary[21][1].is_zero() and primary[21][2]>0
    gradient = [linear_price([row[k] for row in primary], v) for k in (1, 2)]
    assert all(g > 0 for g in gradient)
    rho = arb(n).sqrt()*linear_price(q,v)/M
    kernel = [z.real*n/arb(97).sqrt() for z in acb.dft(signs,inverse=True)]
    W = [sum(v[i]*kernel[(j-i)%n] for i in marked) for j in range(n)]
    assert all(w < rho/8 or w > rho/8 for w in W[1:])
    heads = [j for j in range(1,n) if W[j]>rho/8]
    assert sorted((-j)%n for j in heads) == heads
    common = (n*linear_price(q,v)-1)/arb(97).sqrt()
    assert (linear_price(q,W)-common).contains(0)
    lower = (common-q[0]*W[0]-rho*M/8)/(1-rho/8)
    assert lower > 0

    state = [arb(0)]*n
    density = [arb(1)/n]*n
    apply = terminal["prior"]["apply_multiplier"]
    for _ in range(4):
        phi = [(4+state[0]**2).sqrt()]+[abs(a) for a in state[1:]]
        state = apply(phi, signs)
        density = [b+a**2 for a,b in zip(state,density)]

    # Variables are the two free anchor ratios and the envelope scale.
    # At the optimum sites 3 and 22 saturate, and site 19 vanishes.
    bindings = [3,22,19]
    matrix = [[primary[j][1], primary[j][2], -density[j] if j!=19 else arb(0)]
              for j in bindings]
    x,z,A = solve(matrix,[-primary[j][0] for j in bindings])
    best = [c+d*x+e*z for c,d,e in primary]
    for j in range(1,n):
        k = min(j,n-j)
        if k == 19:
            assert best[j].contains(0)
            best[j] = arb(0)
        elif not all(y.is_zero() for y in primary[j]):
            assert best[j] > 0
        else:
            assert best[j].is_zero()
        if k in (3,22):
            assert (best[j]-A*density[j]).contains(0)
        else:
            assert best[j] < A*density[j]
    assert (sum(best)-1).contains(0) and (q[0]-best[0]).contains(0)
    # w3*(q3-A*d3)+w22*(q22-A*d22)-w19*q19 equals constant-A.
    matrix[2] = [-v for v in matrix[2]]
    dual = solve(list(map(list,zip(*matrix))),[0,0,-1])
    assert all(w>0 for w in dual)
    dual_price = dual[0]*primary[3][0]+dual[1]*primary[22][0]-dual[2]*primary[19][0]
    assert (dual_price-A).contains(0) and A < arb(22)/100
    assert all((b[i]-b[-i % n]).contains(0)
               for b in [q,best,density,W,price] for i in range(n))

    # Fix the same head and time. Clip the reference energy cap on the
    # negative mask as in (7), interpolate a minorant, then repair it by
    # the free opposite optimum to produce a genuine positive potential.
    cap = [w/5 for w in density]
    for i in marked:
        cap[i] = cap[i].min(arb(4)/(n*(1+price[i])))
    demand = [int(i in heads)+h/4 for i,h in enumerate(price)]
    active = [j for j in range(1,n//2+1) if q[j]>0]
    modes = [j for j in range(1,n//2+1) if signs[j]==-side]
    assert all(q[i]>cap[i] or q[i]<cap[i] for i in range(1,n))
    cost = sum(demand[i]*(q[i]-cap[i]).max(0) for i in range(1,n))
    f = [demand[i] if q[i]>cap[i] else arb(0) for i in range(n)]
    cosine = [(arb(2*i)/n).cos_pi() for i in range(n)]
    coeff = solve([[cosine[(i*j)%n] for j in modes] for i in active],[f[i] for i in active])
    minorant = [sum(k*cosine[(i*j)%n] for k,j in zip(coeff,modes)) for i in range(n)]
    free = [10,21,n-10,n-21]
    assert all(minorant[i]<0 for i in free)
    level = arb(4)
    assert all(g<level for g in demand)
    repair = [i for i in range(n) if opposite[i]>0]
    lam = 1 + max([0]+[int((minorant[i]/opposite[i]).upper().ceil().unique_fmpz())
                        for i in repair])
    U = [u-lam*o for u,o in zip(minorant,opposite)]
    V = [level-u for u in U]
    assert all(V[i]>0 for i in range(n))
    assert all(U[i]<0 for i in repair+free)
    assert all((U[i]-f[i]).contains(0) for i in range(1,n) if q[i]>0)
    residual = sum(V)/n-q[0]*V[0]
    uncovered = sum(cap[i]*(level-V[i]).max(0) for i in range(1,n))
    assert (level*M-residual-uncovered-cost).contains(0)
    assert residual>0 and uncovered>0 and cost>arb(1)/2

    return dict(prime=97,time=4,side=side,alpha="1/5",units="1e-9",precision=ctx.prec,
                joint_demand_cost=interval(cost),positive_potential_root_residual=interval(residual),
                positive_potential_uncovered_charge=interval(uncovered),potential_level=4,
                common_head=heads,mask=marked,normalized_hinge_collision=interval(n*sum(k*k for k in y)),
                rho=interval(rho),common_signed_mean_lower=interval(common),
                uniform_face_head_mass_lower=interval(lower),minimizer_head_mass=interval(sum(q[j] for j in heads)),
                least_energy_profile_scale=interval(A),envelope_optimizer_free_parameters=[interval(x),interval(z)],
                envelope_optimizer_head_mass=interval(sum(best[j] for j in heads)),
                envelope_optimizer_masked_terminal_price=interval(linear_price(best,price)),
                hinge_optimizer_masked_terminal_price=interval(linear_price(q,price)),
                face_gradient=[interval(g) for g in gradient],envelope_dual_weights=[interval(w) for w in dual])


if __name__ == "__main__":
    print(json.dumps(check(),sort_keys=True))
