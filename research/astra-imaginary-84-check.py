"""Arb192 certificate for rank-four returns, a physical rectangle, and the cold source."""
import json
import runpy
from collections import defaultdict
from math import comb
from pathlib import Path

from flint import acb, arb, arb_poly

HERE = Path(__file__).resolve().parent
prior = runpy.run_path(str(HERE / "astra-direction-83-invariant.py"))
fields = prior["fields"]
rank_three = fields["kern"]["p3"]
rank_four = fields["kern"]["prior"]
F = fields["kern"]["F"]
UNIT = arb(1) / 2**20


def cancellation(x, y):
    denom = abs(x) + abs(y) + abs(x + y)
    if not denom > 0:
        return arb(0)
    num = 2 * (abs(x) * abs(y) - (x * y.conjugate()).real)
    return max(arb(0), (num / denom).lower())


def signed_upper(t):
    rows, pars = fields["upper"](t)
    _, beta, groups, amendments = rank_three["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    units = []
    for terms in rank_three["rank_powers"](4):
        units.append([(shift, multiplicity) for (a, b, c, d, shift), multiplicity
                      in terms.items() if (a, b, c, d) == (0, 0, 0, 0)])
    columns = []
    for r in range(9):
        coeff = defaultdict(lambda: acb(0))
        for l, terms in enumerate(units):
            for k in range(10):
                labels = amendments[k] if r+l == 0 and k in amendments else groups[r+l, k]
                w = comb(r+l, r) * (beta/4)**l / (2 if k else 1)
                for (u, v), value in labels.items():
                    if u + v > 5:
                        continue
                    for shift, multiplicity in terms:
                        for e in ((-k, k) if k else (0,)):
                            coeff[u, v, e+shift] += value * w * multiplicity
        columns.append(coeff)

    for j in range(7):
        returned = defaultdict(lambda: arb(0))
        labels = set().union(*(col.keys() for col in columns[j:j+4]))
        for u, v, e in sorted(labels):
            if abs(e) > 9:
                continue
            for h in (0, 1):
                if j+h+2 > 8:
                    continue
                if h == 0 and u == v == 0 and abs(e) <= 5:
                    continue  # Already pooled in the earlier rank-four calculation.
                if j == 0 and h == 0 and e == 0 and (u, v) in ((1, 1), (2, 0), (0, 2)):
                    continue  # Later Legendre root subtractions.
                if j == 0 and h == 1 and u == v == 0 and abs(e) == 1:
                    continue  # Later rank-five root subtraction.
                if h == 0:
                    scale0 = 1
                    scale2 = gamma**2 * comb(j+2, 2) / 8
                    fiber = [(0, 1)]
                else:
                    scale0 = gamma * (j+1)
                    scale2 = 3 * gamma**3 * comb(j+3, 3) / 8
                    fiber = [(i, F[i+4]) for i in range(-4, 5)]
                label = (u, v, e)
                first = scale0 * columns[j+h].get(label, 0)
                second = scale2 * columns[j+h+2].get(label, 0)
                loss = cancellation(acb(first), acb(second))
                for s in range(-2*u, 2*u+1, 4):
                    for k, weight in fiber:
                        returned[s-e+k] += loss * (v+1) * weight
        for k in range(len(rows[j])):
            debit = (2 * min(returned[k].lower(), returned[-k].lower())
                     if k else returned[0].lower())
            rows[j][k] -= debit
            assert rows[j][k] >= 0
    return rows, pars


def envelope(base, half, height, nx, ny, lam):
    rows = None
    for i in range(nx):
        for j in range(ny):
            w = half / nx
            v = height / (2*ny)
            t = acb(arb(base+(2*i+1-nx)*w, w), arb((2*j+1)*v, v))
            local, params = signed_upper(t)
            if rows is None:
                rows, pars = local, params
            else:
                rows = [[max(x.upper(), y.upper()) for x, y in zip(r, s)]
                        for r, s in zip(rows, local)]
                pars = [max(x.upper(), y.upper()) for x, y in zip(pars, params)]
    rows[0] = [lam*x for x in rows[0]]
    a, b, c, d, z, w, v = pars
    sym = prior["symmetric"]
    components = [(1, sym([0, fields["kern"]["dim"]])), (2, sym([a, 0, a])),
                  (3, sym([b, 3*b/2, 0, 3*b/2])), (4, c*F), (5, d*fields["kern"]["G"]),
                  (2, z*fields["old"]["R"]), (4, (w+v)*fields["field"])]
    center = sum((pol.left_shift(5-r) for r, pol in components), arb_poly())
    mass = fields["kern"]["dim"]+2*a+3*b+4*c+23*d/4+8*(z+w+v)
    return acb(arb(base, half), arb(0, height)), rows, center, mass


def invariant(label, base, half, height, nx, ny, lam, caps):
    data = envelope(base, half, height, nx, ny, lam)
    frozen = [arb(x)/10**20 for x in caps]
    out, leak, cap = prior["image"](base, half, data, frozen)
    assert leak >= 0
    for k, (x, y) in enumerate(zip(out, frozen), 1):
        leak += max(arb(0), (x-y).upper()) * (k*prior["eta"]).cosh()
    leak += arb(1)/10**12
    assert leak < prior["EPS"] and cap < arb("4.654")
    print(json.dumps(dict(kind="signed_rank_four_physical_invariant", domain=label,
                          real_center_units=str(base/UNIT), real_halfwidth_units=str(half/UNIT),
                          imag_halfwidth_units=str(height/UNIT), lambda_radius=str(lam),
                          nonnegative_weighted_excess=str(leak), coordinate_cap=str(cap))),
          flush=True)


def source():
    t0 = arb(2031)/128
    h = arb(1)/32
    t = acb(arb(t0, h), arb(0, h))
    rows, (a,b,c,d,z,w,v) = fields["upper"](t)
    dim = fields["kern"]["dim"]+2*a+3*b+4*c+23*d/4+8*(z+w+v)
    ratio = dim**2/(4*(t0-h))
    bn = arb(1)
    for j in range(1, 16):
        bn *= (arb(3)/2-j)/j
    # A product of 2l center factors has absolute boundary index at most 10l.
    tail = 20*abs(t).sqrt()*abs(bn)*ratio**15*(15/(1-ratio)+ratio/(1-ratio)**2)
    sup = sum(k*x for k,x in enumerate(rows[0])) + tail + arb(1)/10**12
    cauchy = sup / (h - arb(1)/2**17)
    assert ratio < 1 and dim < 5 and sup < arb(".142") and cauchy < arb("4.52")
    print(json.dumps(dict(kind="physical_cold_source_conjugate_bound",
        source_domain_halfwidth="1/32", source_coordinate_cap=str(sup),
        cold_source_floor_derivative_cap=str(cauchy))), flush=True)


if __name__ == "__main__":
    assert rank_four["four_powers"](2)[rank_four["ZERO"], 0] == 8
    for label in rank_four["four_powers"](1):
        assert rank_four["four_powers"](3)[label] >= 24
    source()
    caps = json.loads((HERE/"astra-imaginary-84-caps.json").read_text())
    invariant("warm", 16640276*UNIT, 16*UNIT, 2*UNIT, 16, 1, arb(1), caps["warm"])
    invariant("cold", 16637952*UNIT, 8*UNIT, 8*UNIT, 8, 4,
              arb(9989815)/10**7, caps["cold"])
