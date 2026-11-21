"""Arb192 replay for the shifted arithmetic dual cube and exterior square."""
from collections import defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb

HERE = Path(__file__).resolve().parent
r101 = runpy.run_path(str(HERE / "astra-rank-101-check.py"))
r84, fields, p3, unit = (r101[k] for k in ("r84", "fields", "p3", "unit"))
zero = r101["zero"]


def rank_four_scalars(columns, gamma):
    result = {}
    for r in range(1, 9):
        row = defaultdict(lambda: acb(0), columns[r])
        if r+2 <= 8:
            factor = comb(r+2,2)*gamma**2/8
            for key, x in columns[r+2].items():
                row[key] += factor*x
        if r+4 <= 8:
            factor = comb(r+4,4)*gamma**4/4096
            for (u, v, e), x in columns[r+4].items():
                for shift, m in ((-2,2), (0,196), (2,2)):
                    row[u,v,e+shift] += factor*m*x
        result[r] = row
    return result


def signed_upper(t):
    rows, params = r101["signed_upper"](t)
    _, beta, groups, amended = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1,1][0,0]
    delta = -2*gamma * fields["kern"]["linear_scalar"](groups,beta)
    z = fields["old"]["prefix"](t)[0]
    w = fields["joint"]["coefficient"](t,0,2,0)
    v_amp = fields["selected"](t)
    q = delta**2/16 + z**2 + 2*w**2 + 2*v_amp**2
    debit = [defaultdict(lambda: arb(0)) for _ in range(7)]
    for tag in r101["tags"]:
        cols = r101["r99"]["r96"]["columns"](groups, amended, beta, tag)
        scalar = rank_four_scalars(cols, gamma)
        for j in range(7):
            by_site = defaultdict(lambda: arb(0))
            if j <= 5:
                cubic = comb(j+3,3)
                # Three D's return to D-dual times det(D). Three D-duals
                # return to D times det(D)^-1. Index e is the FINAL exponent.
                for shift, fiber in ((4, ((0,3),(4,1))), (-4, ((-4,1),(0,3)))):
                    for (u, v, source), x in scalar[j+3].items():
                        e = source + shift
                        if j == 0 and tag == zero and e == 0 and (u,v) in ((1,0),(0,1)):
                            continue
                        base = (j+1)*scalar[j+1].get((u,v,e), acb(0))
                        base += (3*cubic*q)*scalar[j+3].get((u,v,e), acb(0))
                        gain = abs(w).lower()*r84["cancellation"](base, cubic*w**2*x)
                        if gain:
                            for k in range(-2*u,2*u+1,4):
                                for offset, m in fiber:
                                    by_site[k-e+offset] += (v+1)*m*gain
            # Wedge^2 D^dual = wedge^2 D times det(D)^-1. The physical
            # wedge^2 D fiber has three weights -4 and three weights 0.
            factor = comb(j+2,2)*abs(w).lower()**2
            for (u, v, e), x in scalar[j+2].items():
                y = scalar[j+2].get((u,v,e+4))
                if y is None:
                    continue
                gain = factor*r84["cancellation"](x,y)
                if gain:
                    for k in range(-2*u,2*u+1,4):
                        for offset in (-4,0):
                            by_site[k-e+offset] += 3*(v+1)*gain
            for site, value in by_site.items():
                for weight, mult in p3["pair_fiber"](*tag):
                    debit[j][site+weight] += mult*value
    for j, gains in enumerate(debit):
        for k in range(len(rows[j])):
            rows[j][k] -= (2 if k else 1)*min(gains[k].lower(),gains[-k].lower())
            assert rows[j][k] >= 0
    return rows, params


r84["envelope"].__globals__["signed_upper"] = signed_upper


def verify_signatures():
    from collections import Counter
    paths = [Counter({(0,0,0,0): 1})]
    for _ in range(3):
        stage = Counter()
        for label, multiplicity in paths[-1].items():
            for k in range(4):
                for step in (-1,1):
                    changed = list(label)
                    changed[k] += step
                    if changed == sorted(changed, reverse=True):
                        stage[tuple(changed)] += multiplicity
        paths.append(stage)
    assert paths[2][1,1,0,0] == paths[2][0,0,-1,-1] == 1
    assert paths[3][1,0,0,0] == paths[3][0,0,0,-1] == 6
    assert paths[3][1,1,1,0] == paths[3][0,-1,-1,-1] == 1


def witness():
    verify_signatures()
    t = acb(arb(16640183*unit, unit), arb(0,unit))
    _, beta, g, am = p3["coefficients"](t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500*beta*g[1,1][0,0]
    delta = -2*gamma*fields["kern"]["linear_scalar"](g,beta)
    z = fields["old"]["prefix"](t)[0]
    w = fields["joint"]["coefficient"](t,0,2,0)
    v = fields["selected"](t)
    q = delta**2/16+z**2+2*w**2+2*v**2
    s = rank_four_scalars(r101["r99"]["r96"]["columns"](g,am,beta,zero), gamma)
    # D^3 at inner exponent 1 and D-dual at final exponent 5.
    a = s[1][0,0,5]+3*q*s[3][0,0,5]
    cubic = abs(w).lower()*r84["cancellation"](a, w**2*s[3][0,0,1])
    # At j=1 the two exterior squares use old exponents -3 and 1.
    exterior = 3*abs(w).lower()**2*r84["cancellation"](s[3][0,0,-3],s[3][0,0,1])
    assert cubic > arb("1.374e-12") and exterior > arb("3.65e-10")
    print(json.dumps(dict(kind="dual_displacement_witness", cubic_multiplicity=1,
                          exterior_square_multiplicity=1, cubic_saving=str(cubic),
                          exterior_square_saving=str(exterior))), flush=True)


def compare(entry):
    lo, hi, nx, caps = entry
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    image_globals = r84["envelope"].__globals__
    image_globals["signed_upper"] = r101["signed_upper"]
    try:
        before = r84["envelope"](mid,half,unit,nx,1,arb(1))
    finally:
        image_globals["signed_upper"] = signed_upper
    frozen = [arb(x)/10**20 for x in caps]
    out = r84["prior"]["image"](mid,half,before,frozen)[0]
    excess, packet = max(((x-y).lower(), k) for k,(x,y) in enumerate(zip(out,frozen),1))
    assert excess > arb("2.35e-9") and packet == 3
    print(json.dumps(dict(kind="same_cap_before_dual_displacements", previous_packet=packet,
                          previous_overrun_lower=str(excess))), flush=True)


if __name__ == "__main__":
    import sys
    caps = json.loads((HERE / "astra-cubic-102-caps.json").read_text())
    tasks = sys.argv[1:] or ["witness", *map(str,range(len(caps))), "comparison"]
    for task in tasks:
        if task == "witness":
            witness()
        elif task == "comparison":
            compare(caps[0])
        else:
            r101["r99"]["r95"]["verify"](*caps[int(task)])
