"""Arb replay of the two affine marginal columns and their shifted-atom tests."""
from pathlib import Path
import json
import runpy
import sys

from flint import acb, arb, ctx

base = Path(__file__).resolve().parent
sys.path.insert(0, str(base.parent))
previous = runpy.run_path(str(base / "astra-matched-88-check.py"))
from theta import prime_field_generator

ctx.prec = 384
equal = previous["equal"]
units = previous["units"]
positions = previous["positions"]


def audit(p, probes, odd_pivot=None):
    prior = previous["prior"]
    signs = list(map(int, prior["paley_sign"](p)))
    n = len(signs)
    root_p = arb(p).sqrt()
    pair, error = prior["solve_prime_pair"](prior["paley_sign"](p))
    assert error is None
    q, r = ([value / arb(n).sqrt() for value in pair[s]] for s in (1, -1))
    if odd_pivot is not None:
        previous["add_odd"](r, -1, odd_pivot, signs)
    endpoint = {1: positions(q), -1: positions(r)}
    equal(n*q[0]*r[0], 1)
    for side, row in ((1, q), (-1, r)):
        assert all(value.is_zero() or value > 0 for value in row)
        equal(sum(row), 1)
        for i in range(1, n):
            if signs[i] != side:
                equal(endpoint[side][i], 0)
    if odd_pivot is not None:
        assert any(abs(value.imag) > 0 for value in endpoint[-1])
    law = {s: [(row[i] + row[-i % n]) / 2 for i in range(n)]
           for s, row in [(1, q), (-1, r)]}

    generator = prime_field_generator(p)
    squares = [pow(generator, 2*i, p) for i in range(n)]
    logs = {x: i for i, x in enumerate(squares)}
    mult = [acb(0, arb.pi()*2*i/n).exp() for i in range(n)]
    add = [acb(0, arb.pi()*2*k/p).exp() for k in range(p)]
    if p == 409:
        j = max(range(1, n), key=lambda i: float(q[i].lower()))
        t = -j % n
    else:
        j = 0
        t = max(range(1, n), key=lambda i: float(r[i].lower()))
    mu = [n*q[i]*r[(i+t) % n] for i in range(n)]
    equal(sum(mu), 1)
    equal(mu[0], r[t]/r[0])
    if j:
        equal(mu[j], q[j]/q[0])
    shifted = [mu[(i+j) % n] for i in range(n)]
    conditional = positions(shifted)
    equal(sum(conditional)/n, mu[j])
    original = positions(mu)
    for i in range(n):
        equal(conditional[i], original[i]*mult[-i*j % n])
    cstar = n*(r[0] - q[0])/root_p

    def mask(z, s, probe):
        node = probe*probe*(z + (s == -1)) % p
        return node in logs and signs[logs[node]] == s

    configs = [
        ("unweighted", [acb(1)]*p, arb(1)/4),
        ("shifted_atom", [conditional[(logs[(z+2) % p] + 3) % n]
                          if (z+2) % p in logs else acb(0) for z in range(p)],
         mu[j]/8),
        ("conditional_collision", [abs(original[(logs[(z+2) % p]+3) % n])**2
                                   if (z+2) % p in logs else acb(0) for z in range(p)],
         sum(x*x for x in mu)/8),
        ("index_two_coset", [acb(int((z+2) % p in logs and logs[(z+2) % p] % 2 == 1))
                             for z in range(p)], arb(1)/16),
    ]
    for i in range(n):
        equal((1-mult[i*n//2 % n])/2, int(i % 2 == 1))
    width = p//6
    tent = [arb(max(0, width-min(z, p-z)))/width for z in range(p)]
    tent_transform = [z/p for z in acb.dft(tent)]
    for k in range(p):
        short_sum = sum(add[-k*z % p] for z in range(width))
        equal(tent_transform[k], short_sum*short_sum.conjugate()/(p*width))
    equal(sum(tent_transform), 1)
    equal(tent_transform[0], arb(width)/p)

    results = []
    for name, test, main_factor in configs:
        columns = {}
        for side in (1, -1):
            for other in probes:
                for k in (0, 1, 5):
                    raw = []
                    for field_value in squares:
                        z = (field_value - (side == -1)) % p
                        raw.append(test[z]*add[k*z % p] if mask(z, -side, other) else acb(0))
                    columns[side, other, k] = [v/root_p for v in positions(raw)]
        raw_totals, tent_totals = [], []
        max_column = arb(0)
        observed = None
        for u in probes:
            for v in probes:
                signed = [acb(0) for _ in range(p)]
                matched = []
                for z in range(p):
                    if mask(z, 1, u) and mask(z, -1, v):
                        x, y = u*u*z % p, v*v*(z+1) % p
                        signed[z] = (endpoint[-1][logs[y]].real -
                                     endpoint[1][logs[x]].real)*test[z]/root_p
                        matched.append(z)
                for k in (0, 1, 5):
                    marginal = {}
                    for s, own, other in ((1, u, v), (-1, v, u)):
                        column = columns[s, other, k]
                        for i, value in enumerate(column):
                            center = n*main_factor/root_p if i == 0 and k == 0 else 0
                            max_column = max(max_column, abs(value-center).upper())
                        shift = logs[own*own % p]
                        full = sum(w*mult[i*shift % n]*value for i, (w, value) in
                                   enumerate(zip(law[s], column)))
                        axis = (pow(own*own, -1, p) - (s == -1)) % p
                        toll = test[axis]*add[k*axis % p]/root_p if mask(axis, -s, other) else 0
                        marginal[s] = full - toll
                        measured = sum((test[z]*add[k*z % p] *
                                        endpoint[s][logs[own*own*(z+(s == -1)) % p]].real
                                        for z in matched), acb(0))/root_p
                        equal(marginal[s], measured)
                    direct = sum(value*add[k*z % p] for z, value in enumerate(signed))
                    equal(marginal[-1]-marginal[1], direct)
                transform = acb.dft(signed)
                start, stop = p//5, p//2
                samples = [int(start <= z < stop) for z in range(p)]
                window = [arb(max(0, width-min((z-u*v) % p, (u*v-z) % p)))/width
                          for z in range(p)]
                raw_totals.append(sum(signed).real)
                tent_totals.append(sum(w*x for w, x in zip(window, signed)).real)
                for weight in (samples, window):
                    spec = acb.dft(weight)
                    equal(sum(w*x for w, x in zip(weight, signed)),
                          sum(x*y.conjugate() for x, y in zip(transform, spec))/p)
                if (u, v) == (2, 3):
                    value = sum(s*w for s, w in zip(signed, samples))
                    observed = dict(count=len(matched), interval_real=units(value.real),
                                    interval_imag=units(value.imag))
        assert max_column < 5
        results.append(dict(test=name, main_term=units(cstar*main_factor),
                            average_full_real=units(sum(raw_totals)/len(raw_totals)),
                            average_tent_real=units(sum(tent_totals)/len(tent_totals)),
                            column_residual_upper_1e9=units(max_column)[1],
                            probe_2_3=observed))
    return dict(prime=p, precision_bits=ctx.prec, units="1e-9", probes=probes,
                odd_minus_pivot=odd_pivot, displacement=t, atom=j, atom_mass=units(mu[j]),
                cstar=units(cstar), tested_additive_frequencies=[0, 1, 5], rows=results)


def square_audit(s):
    residue = {i*i % s for i in range(1, s)}
    d = next(i for i in range(2, s) if i not in residue)

    def character(a, b):
        norm = (a*a-d*b*b) % s
        return 0 if norm == 0 else 1 if norm in residue else -1

    counts = []
    for u in (2, 3):
        for v in (2, 3):
            count = 0
            for a in range(s):
                for b in range(s):
                    x, y = (u*u*a, u*u*b), (v*v*(a+1), v*v*b)
                    if (character(*x) == character(*y) == 1
                        and character(1-x[0], -x[1]) == 1
                        and character(1-y[0], -y[1]) == -1):
                        assert b != 0
                        count += 1
            assert count > 0
            counts.append(dict(u=u, v=v, count=count, signed_price=units(arb(2)*count/(s*(s+1)))))
    quarter = arb(3-s)/(8*s)
    assert quarter < 0
    return dict(square_order=s*s, subfield_prime=s, units="1e-9",
                quarter_cstar=units(quarter), ordered_probes=counts)


if __name__ == "__main__":
    for p, probes, pivot in ((53, [2, 3], None), (257, [2, 3, 5, 7], 48),
                             (409, [2, 3, 5, 7], 95)):
        print(json.dumps(audit(p, probes, pivot), sort_keys=True), flush=True)
    for s in (11, 19, 43):
        print(json.dumps(square_audit(s), sort_keys=True), flush=True)
