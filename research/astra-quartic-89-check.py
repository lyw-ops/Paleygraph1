"""Certify the masked quartic minimizers on three delayed pins of one true companion."""
import json
from pathlib import Path
import runpy
import sys

from flint import acb, arb, ctx

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base.parent))
from square_control import square_field_sign

prior = runpy.run_path(str(base / "astra-split-83-check.py"))
face = prior["face"]
interval = prior["interval"]
apply_multiplier = prior["terminal"]["prior"]["apply_multiplier"]
ctx.prec = 384


def delayed_masks(signs):
    n = len(signs)
    root = arb(n).sqrt()
    state = [arb(0)] * n
    energy, primary, companion = [], [], []
    for j in range(25):
        energy.append(sum(y * y for y in state))
        phi = [(4 + state[0] ** 2).sqrt()] + list(map(abs, state[1:]))
        primary.append(apply_multiplier([root * (v - y) / 2 for v, y in zip(phi, state)],
                                        [int(x <= 0) for x in signs]))
        companion.append(apply_multiplier([root * (v + y) / 2 for v, y in zip(phi, state)],
                                          [int(x >= 0) for x in signs]))
        state = apply_multiplier(phi, signs)
    scores = [v + arb(j) / 256 for j, v in enumerate(energy)]
    T = max(range(len(scores)), key=lambda j: float(scores[j].mid()))
    assert all(j == T or scores[j] < scores[T] for j in range(len(scores)))
    b = T - 2
    column = [v.real for v in acb.dft([int(x == -1) for x in signs], inverse=True)]
    masks = {}
    for d in (2, 4, 8):
        assert b >= d
        raw = [(2 * sum(row[i] for row in primary[b-d+1:b]) + primary[b][i]) / (2*d-1)
               for i in range(n)]
        inc = arb(21) * raw[0] / (20 * root) - sum(raw) / n
        assert inc > 0
        pin = [v + inc * (1 - c / column[0]) for v, c in zip(raw, column)]
        cut = -arb(1) / 100
        assert all(v > cut or v < cut for v in pin[1:])
        assert all(pin[i] + companion[b][i] / (2*d-1) > 0 for i in range(1, n))
        masks[d] = [i for i in range(1, n) if pin[i] < cut]
    return b, masks, companion[b]


def prime_97():
    rows, opp = face["faces"]()
    n = len(rows)
    b, masks, _ = delayed_masks(list(map(int, face["mask"])))
    assert b == 11 and all(opp[j].is_zero() for P in masks.values() for j in P)
    assert [[j for j in masks[d] if j <= n//2] for d in (2, 4, 8)] == [
        [2, 3, 8, 18, 22], [3, 8, 22], [8]]

    def q(j, point):
        return face["at"](rows[j], point)

    def values(P, point):
        return sum((n*q(j, point))**4 for j in P)/n

    def grad(P, point):
        return [sum(4 * (n*q(j, point))**3 * rows[j][k] for j in P) for k in (1, 2)]

    origin = (arb(0), arb(0))
    assert rows[10][0].is_zero() and rows[10][2].is_zero() and rows[10][1] > 0
    assert rows[21][0].is_zero() and rows[21][1].is_zero() and rows[21][2] > 0
    assert all(v > 0 for v in grad(masks[2], origin))
    assert all(rows[j][k].is_zero() for j in masks[8] for k in (1, 2))

    # On q_19=0 parameterize the second anchor by z, so q_j=A_j+B_j z.
    e0, e1, e2 = rows[19]
    location = -e0/e1
    slope = -e2/e1
    def edge(j):
        c, x, z = rows[j]
        return c + x*location, z + x*slope
    a3, b3 = edge(3)
    a22, b22 = edge(22)
    assert b3 < 0 < b22
    ratio = (b22 / -b3).root(3)
    z = (ratio*a22 - a3)/(b3 - ratio*b22)
    point = (location + slope*z, z)
    for j in range(n):
        if min(j, n-j) == 19:
            assert q(j, point).contains(0)
        elif any(not v.is_zero() for v in rows[j]):
            assert q(j, point) > 0
    grad4 = grad(masks[4], point)
    normal = grad4[0] / e1
    assert normal > 0 and (grad4[1] - normal*e2).contains(0)
    # Rank two of the charged affine measurements gives strict convexity.
    assert abs(rows[3][1]*rows[22][2] - rows[3][2]*rows[22][1]) > 0
    minima = [values(masks[2], origin), values(masks[4], point), values(masks[8], origin)]
    assert values(masks[4], origin) > minima[1] and values(masks[2], point) > minima[0]
    # Interpolate the cubic on the exposed face. Orbit 3 is the dependent
    # interpolation equation by the edge stationarity identity above.
    mark = q(0, point)
    P = set(masks[4])
    cubic = [(q(i, point)/mark)**3 if i in P else arb(0) for i in range(n)]
    active = [i for i in range(1,n//2+1) if i != 19 and q(i, point) > 0]
    independent = [i for i in active if i != 3]
    modes = [i for i in range(1,n//2+1) if face["mask"][i] == -1]
    cos = [(arb(2*i)/n).cos_pi() for i in range(n)]
    coeff = prior["solve"]([[cos[(i*j)%n] for j in modes] for i in independent],
                           [cubic[i] for i in independent])
    U = [sum(c*cos[(i*j)%n] for c,j in zip(coeff,modes)) for i in range(n)]
    assert all((U[i]-cubic[i]).contains(0) for i in active) and U[19] < 0
    repair = 1 + max([arb(0)] + [U[i]/opp[i] for i in range(n) if opp[i] > 0])
    W = [1-u+repair*r for u,r in zip(U, opp)]
    assert all(w > 0 for w in W)
    floor = 1/sum(W)
    w = [v*floor for v in W]
    deficit = [floor*c for c in cubic]
    for i in range(1,n):
        if i in P:
            assert (floor-w[i]-deficit[i]).contains(0)
        elif opp[i] > 0 or min(i,n-i) == 19:
            assert w[i] > floor
        else:
            assert (w[i]-floor).contains(0)
    residual = floor*(1/mark-1) - (1/(n*mark)-w[0])
    denom = sum(deficit[i]**(arb(4)/3) for i in P)**(arb(3)/4)
    dual = (residual/denom)**4
    scaled_min = minima[1]/(n**3*mark**4)
    assert (dual-scaled_min).contains(0) and residual > 0
    return dict(prime=97, terminal_time=b, lengths=[2,4,8],
                quartic_minima=[interval(v) for v in minima],
                length4_origin=interval(values(masks[4], origin)),
                length2_on_length4_minimizer=interval(values(masks[2], point)),
                length4_anchors=[interval(v) for v in point],
                length4_normal_multiplier=interval(normal),
                length4_opposite_floor=interval(floor), length4_root_residual=interval(residual),
                length4_dual_fourth_power=interval(dual),
                length2_origin_gradient=[interval(v) for v in grad(masks[2], origin)])


def square(h):
    signs = list(map(int, square_field_sign(h)))
    n = len(signs)
    b, masks, Z = delayed_masks(signs)
    A = set(range(0, n, h-1))
    a = arb(1)/len(A)
    gamma = arb(n).sqrt()*a
    kernel = [v.real for v in acb.dft([int(x == -1) for x in signs], inverse=True)]
    assert (kernel[0]-arb(1)/2).contains(0)
    assert all((kernel[j]+arb(1)/(h-1)).contains(0) for j in A if j)
    records = []
    for d, P in masks.items():
        S = set(P) & A
        Q = sum((n*a)**4 for _ in S)/n
        V = n*a*a*sum(1+Z[i] for i in S)/d
        assert S == A - {0} and (Q-gamma**4*n*len(S)).contains(0)
        records.append(dict(d=d, physical_sites=len(P), paying_subfield_sites=len(S),
                            quartic_over_n=interval(Q/n), charged_energy=interval(V)))
    return dict(field_order=h*h, terminal_time=b, subfield_annihilator_size=len(A),
                lengths=records)


if __name__ == "__main__":
    for record in (prime_97(), square(31), square(59)):
        print(json.dumps(dict(**record, precision_bits=ctx.prec, units="1e-9",
                              tilt="1/256", allowance="1/20", cutoff="1/100"), sort_keys=True))
