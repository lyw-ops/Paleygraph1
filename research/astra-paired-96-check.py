"""Certificate for pooled arithmetic unit returns in the nine-center recurrence."""
from collections import defaultdict
from math import comb
from pathlib import Path
import json
import runpy

from flint import acb, arb

HERE = Path(__file__).resolve().parent
previous = runpy.run_path(str(HERE / "astra-depth-95-check.py"))
r84 = previous["r84"]
fields = previous["fields"]
p3 = previous["rank_three"]
unit = previous["unit"]
trivial = (0, 0, 0, 0)
tags = [trivial] + previous["tags"]


def columns(groups, amendments, beta, tag):
    powers = p3["rank_powers"](4)
    shifts = [[(s[-1], n) for s, n in degree.items() if s[:4] == tag]
              for degree in powers]
    result = []
    for r in range(9):
        values = defaultdict(lambda: acb(0))
        for ell, terms in enumerate(shifts):
            if not terms:
                continue
            for k in range(10):
                src = amendments[k] if r + ell == 0 and k in amendments else groups[r+ell, k]
                wt = comb(r+ell, r) * (beta/4)**ell / (2 if k else 1)
                for (u, v), a in src.items():
                    if u + v > 5:
                        continue
                    if (r, ell, k, u, v) == (0, 1, 1, 0, 0):
                        a = a / 500
                    for shift, multiplicity in terms:
                        for e in ((shift-k, shift+k) if k else (shift,)):
                            values[u, v, e] += a * wt * multiplicity
        result.append(values)
    return result


def signed_upper(t):
    rows, pars = previous["signed_upper"](t)
    _, beta, groups, amend = p3["coefficients"](
        t, acb(fields["prev"]["da"]), acb(fields["prev"]["db"]))
    gamma = arb(499)/500 * beta * groups[1, 1][0, 0]
    delta = -2 * gamma * fields["kern"]["linear_scalar"](groups, beta)
    z = fields["old"]["prefix"](t)[0]
    w = fields["joint"]["coefficient"](t, 0, 2, 0)
    v_amp = fields["selected"](t)
    square = delta**2/16 + z**2 + 2*w**2 + 2*v_amp**2
    for tag in tags:
        data = columns(groups, amend, beta, tag)

        def inner(r, u, v, e):
            if r > 8 or abs(e) > 5:
                return acb(0)
            return data[r].get((u, v, e), acb(0))

        def scalar(r, e):
            # The original degree-four scalar projection includes all three
            # Jacobi shifts. Each source exponent was restricted to [-5,5].
            return (inner(r, 0, 0, e)
                    + comb(r+2, 2)*gamma**2/8*inner(r+2, 0, 0, e)
                    + comb(r+4, 4)*gamma**4/4096*(
                        196*inner(r+4, 0, 0, e) + 2*inner(r+4, 0, 0, e-2)
                        + 2*inner(r+4, 0, 0, e+2)))

        for j in range(7):
            debit = defaultdict(lambda: arb(0))
            for (u, v, e), direct in data[j].items():
                if j == 0 and tag == trivial and (
                    (e == 0 and (u, v) in ((1, 1), (2, 0), (0, 2)))
                    or (abs(e) == 4 and (u, v) == (0, 0))):
                    continue
                returned_source = data[j+2].get((u, v, e), acb(0))
                if tag == trivial and (u, v) == (0, 0) and abs(e) <= 5:
                    direct = scalar(j, e)
                    returned_source = scalar(j+2, e)
                elif tag != trivial or abs(e) <= 9:
                    # This unit was pooled before any later-center children
                    # by R95 (nontrivial) or R84 (trivial).
                    direct += comb(j+2, 2)*gamma**2/8*returned_source
                elif (u, v) == (0, 0):
                    continue
                returned = comb(j+2, 2)*square*returned_source
                gain = r84["cancellation"](direct, returned)
                if not gain:
                    continue
                for wt, count in p3["pair_fiber"](*tag):
                    for legendre in range(-2*u, 2*u+1, 4):
                        debit[wt+legendre-e] += count*(v+1)*gain
            for k in range(len(rows[j])):
                saved = (2*min(debit[k].lower(), debit[-k].lower())
                         if k else debit[0].lower())
                rows[j][k] -= saved
                assert rows[j][k] >= 0
    return rows, pars


r84["envelope"].__globals__["signed_upper"] = signed_upper


if __name__ == "__main__":
    caps = json.loads((HERE / "astra-paired-96-caps.json").read_text())
    for row in caps:
        previous["verify"](*row)
    r84["envelope"].__globals__["signed_upper"] = previous["signed_upper"]
    lo, hi, nx, cap = caps[0]
    mid, half = (lo+hi)*unit/2, (hi-lo)*unit/2
    data = r84["envelope"](mid, half, unit, nx, 1, arb(1))
    prior = r84["prior"]
    h = [arb(x)/10**20 for x in cap]
    first = prior["image"](mid, half, data, h)[0][0]-h[0]
    assert first > arb("1e-8")
    print(json.dumps(dict(comparison="same coldest cap without new square returns",
                          first_packet_overrun=str(first))), flush=True)

    t = arb(2031)/128 - arb(1)/2**17
    r = 4 * arb(".428236")**600
    delta = 625*r**2
    d = arb(".6")
    q = arb(".8")
    c = arb(".1")
    leakage = ((1-q*q)/(1-d*d)).sqrt()
    assert arb("5.768") / (4*t+arb("5.768")**2).sqrt() < d
    assert (q*q-d*d*leakage**2).sqrt() > c+d*leakage
    mean = 25*r/(4*t).sqrt() + 1250*r**2
    assert 1/(1+t) < arb(".059287")
    assert mean**2 < arb("1.65e-440")
    assert delta**2/c**2 < arb("1.096e-874")
    assert (16*delta/c)**2 < arb("2.805e-872")
    print(json.dumps(dict(kind="two_physical_derivatives", mean_HS_upper="0.059287",
                          exceptional_density=str(delta), signed_trace_tolerance=str(mean**2),
                          stationary_paired_slow_fraction=str((delta/c)**2),
                          late_Picard_slow_fraction_on_selected_blocks=str((16*delta/c)**2))),
          flush=True)
