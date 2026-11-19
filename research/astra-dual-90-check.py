"""Replay shortfall propagation at every translate of a true p=97 sharp law."""
import json
from fractions import Fraction
from pathlib import Path
import runpy

from flint import arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-quartic-89-check.py")))
face = prior["face"]
interval = prior["interval"]
ctx.prec = 384


def largest_atom_sum(weights, budget):
    ordered = sorted(weights, reverse=True)
    count = int(budget.floor().unique_fmpz())
    assert count < len(ordered)

    def ball(value):
        return arb(value.numerator) / value.denominator

    return ball(sum(ordered[:count])) + (budget-count)*ball(ordered[count])


def quotient_checks():
    k = 512
    points = [0, 1, 2, 3, 5, 8, 13]
    bound_term = 8/(arb(k+1).sqrt())+(arb(15)/16)**(k-2)
    counts = [1]+[0]*42
    for _ in range(k):
        counts = [sum(counts[(j-i)%43] for i in points) for j in range(43)]
    assert sum(counts)==7**k
    atom = arb(max(counts))/(7**k)
    prime_bound = arb(1)/43+bound_term/7
    composite_bound = arb(1)/49+bound_term/7
    assert atom<prime_bound<arb(1)/7 and composite_bound<arb(1)/7
    # Uniform measure on the order-seven subgroup of Z/49 is idempotent.
    subgroup = list(range(0,49,7))
    assert all(sum((j-i)%49 in subgroup for i in subgroup)==7*int(j in subgroup)
               for j in range(49))
    return dict(order=43, support=points, steps=k, actual_atom=interval(atom),
                prime_bound=interval(prime_bound), composite_order=49,
                composite_false_bound=interval(composite_bound))


def check():
    rows, v = face["faces"]()
    q = [row[0] for row in rows]
    n, a, beta = len(q), q[0], v[0]
    terminal, masks, _ = prior["delayed_masks"](list(map(int, face["mask"])))
    P = set(masks[8])
    assert P == {8, 40} and terminal == 11
    assert all(rows[i][k].is_zero() for i in P for k in (1, 2))
    u = [y/a for y in q]
    # The very same fixed pair is the cubic contact up to one positive scalar.
    active = face["active"][1]
    modes = [i for i in range(1, n//2+1) if face["mask"][i] == -1]
    cosine = [(arb(2*j)/n).cos_pi() for j in range(n)]
    coeff = prior["prior"]["solve"](
        [[cosine[(i*j)%n] for j in modes] for i in active],
        [arb(int(i in P)) for i in active],
    )
    potential = [sum(c*cosine[(i*j)%n] for c,j in zip(coeff,modes)) for i in range(n)]
    for i in range(1, n):
        if v[i].is_zero():
            assert (potential[i]-int(i in P)).contains(0)
    # The two extra interpolation equations follow algebraically from the
    # anchored null directions and constancy of q_8 on the whole face.
    positive = [i for i in range(n) if v[i]>0]
    repair = 1+max(potential[i]/v[i] for i in positive)
    mass = [arb(2)-y+repair*v_i for y,v_i in zip(potential,v)]
    assert all(y>0 for y in mass)
    w = [y/sum(mass) for y in mass]
    c = 2/sum(mass)

    def terms(law, floor):
        S = sum(floor-law[i] for i in P)
        D = floor*(1/a-1)-beta+law[0]
        assert S>0 and D>0 and (D/S-u[8]).contains(0)
        over = [arb(0) for _ in q]
        for i in positive:
            if i:
                over[i] = law[i]-floor
                assert over[i]>0
        alpha = min(over[i]/v[i] for i in positive if i)
        b = (law[0]-floor-alpha*beta)/S
        residual = [(over[i]-alpha*v[i])/S if i else arb(0) for i in range(n)]
        eps = 1-D/S
        for t in range(n):
            pushed = sum(1-u[(t+i)%n] for i in P)/2
            paid = sum(z*u[(t+i)%n] for i,z in enumerate(residual))
            assert (pushed+paid-eps-b*(1-u[t])).contains(0)
        return eps,b,alpha,residual,S

    eps,b,alpha,residual,S = terms(w,c)
    tau = arb(1)/128
    other = terms([(1-tau)*v_i+tau*w_i for v_i,w_i in zip(v,w)], tau*c)
    assert (other[0]-eps).contains(0) and (other[1]-b).contains(0)
    assert (other[2]-(1-tau)-tau*alpha).contains(0) and (other[4]-tau*S).contains(0)
    assert all((x-y).contains(0) for x,y in zip(residual,other[3]))
    H = list(range(0, n, 8))
    clique = (0, 6, 12)
    assert all(i*j%n==0 for i in H for j in clique)
    assert all(face["mask"][(j-k)%n]==-1 for j in clique for k in clique if j!=k)
    assert sum(q[i] for i in H)<arb(1)/3
    budget = 1/(3*a)
    # Lazy symmetrized walk on Z/6 in its subgroup coordinates.
    walk = [Fraction(1)]+[Fraction(0)]*5
    J = arb(0)
    B = b.max(0)
    bounds = []
    for k in range(1, 11):
        walk = [(2*w_i+walk[(i-1)%6]+walk[(i+1)%6])/4 for i,w_i in enumerate(walk)]
        J = (1+(1+B)*J)/2
        packing = largest_atom_sum(walk,budget)
        cost = (1-packing)/J
        assert eps>cost
        bounds.append(cost)
    best = max(range(len(bounds)), key=lambda j:float(bounds[j].mid()))
    return dict(prime=97, terminal=terminal, length=8, mask=sorted(P), subgroup=H,
                annihilator_forbidden_clique=clique, mixture_weight="1/128", translates_per_law=n,
                sharp_efficiency=interval(1-eps), corrected_root_coefficient=interval(b),
                uncorrected_root_coefficient=interval((w[0]-c)/S),
                sharp_ratio=interval(arb(2).root(4)*(1-eps)), best_tested_step=best+1,
                resulting_efficiency_upper=interval(1-bounds[best]), precision=ctx.prec,
                units="1e-9", quotient_convolution=quotient_checks())


if __name__ == "__main__":
    print(json.dumps(check(), sort_keys=True))
