"""Replay two true endpoint responses, affine Fourier columns, and sharp cells."""
import json
from pathlib import Path
import runpy
import sys

from flint import acb, arb, ctx

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent))
old = runpy.run_path(str(here / "astra-matched-88-check.py"))
prior = old["prior"]
equal, units, positions = (old[k] for k in ("equal", "units", "positions"))
from theta import prime_field_generator

ctx.prec = 384
outcomes = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def even(row):
    return [(v + row[-i]) / 2 for i, v in enumerate(row)]


def displaced(row, opposite):
    n = len(row)
    j = max(range(1, n), key=lambda i: float(row[i].lower()))
    mu = [n*row[i]*opposite[(i-j) % n] for i in range(n)]
    equal(sum(mu), 1)
    equal(mu[0], 0)
    equal(mu[j], row[j]/row[0])
    coeff = even(mu)
    response = sum(a*b for a, b in zip(even(row), coeff))
    equal(sum(a*b for a, b in zip(even(opposite), coeff)), 0)
    assert response > row[j]**2/(2*row[0])
    return j, mu[j], coeff, response


def audit(p, odd_pivot):
    signs = list(map(int, prior["paley_sign"](p)))
    n = len(signs)
    pair, error = prior["solve_prime_pair"](prior["paley_sign"](p))
    assert error is None
    q, r = [[v/arb(n).sqrt() for v in pair[s]] for s in (1, -1)]
    if odd_pivot is not None:
        old["add_odd"](r, -1, odd_pivot, signs)
    endpoints = [positions(row) for row in (q, r)]
    equal(n*q[0]*r[0], 1)
    for row, spectrum, sign in zip((q, r), endpoints, (1, -1)):
        equal(sum(row), 1)
        assert all(v.is_zero() or v > 0 for v in row)
        for i in range(1, n):
            if signs[i] != sign:
                equal(spectrum[i], 0)
    if odd_pivot is not None:
        assert any(abs(v.imag) > 0 for v in endpoints[1])
    jq, uq, cq, dq = displaced(q, r)
    jr, ur, cr, dr = displaced(r, q)
    gap = r[0]-q[0]
    scale = gap/(dq+dr)
    assert 0 < scale < 1
    equal(gap-scale*(dq+dr), 0)

    gen = prime_field_generator(p)
    coordinates = [pow(gen, 2*i, p) for i in range(n)]
    logs = {z: i for i, z in enumerate(coordinates)}
    phases = [acb(0, arb.pi()*2*i/n).exp() for i in range(n)]
    root = arb(p).sqrt()
    gates = {}
    for side, row, coeff in ((0, q, cq), (1, r, cr)):
        for sign in (1, -1):
            mass = [sign*scale*v/2 for v in coeff]
            mass[0] += arb(1)/2
            spectrum = [v.real for v in positions(mass)]
            convolved = old["convolution"](even(row), mass)
            for j, v in enumerate(positions(convolved)):
                equal(v, spectrum[j]*endpoints[side][j].real)
            gates[side, sign] = spectrum, convolved

    results = []
    for u, v in [(2, 3), (3, 2), (2, 2), (3, 3)]:
        shifts = [logs[u*u % p], logs[v*v % p]]
        def node(z, side):
            return (u*u*z if side == 0 else v*v*(z+1)) % p

        def strict(z, side):
            val = node(z, side)
            return val in logs and signs[logs[val]] == (1, -1)[side]

        def window(z):
            w = (z+2) % p
            return p//8 <= z < 7*p//8 and (p == 53 or w in logs and logs[w] % 2 == 0)

        matched = [z for z in range(p) if window(z) and strict(z, 0) and strict(z, 1)]
        raw = {z: (endpoints[1][logs[node(z, 1)]].real -
                   endpoints[0][logs[node(z, 0)]].real)/root for z in matched}
        weights = {z: [] for z in matched}
        cell_prices = []
        for eps, delta in outcomes:
            locked = [gates[0, eps], gates[1, delta]]
            for z in matched:
                weights[z].append(locked[0][0][logs[node(z, 0)]]*
                                  locked[1][0][logs[node(z, 1)]])
            principal = sum((raw[z]*weights[z][-1] for z in matched), arb(0))
            marginals = []
            for side in (0, 1):
                other = 1-side
                base_column = []
                for w in coordinates:
                    z = (w-side) % p
                    base_column.append(locked[other][0][logs[node(z, other)]]
                                       if window(z) and strict(z, other) else arb(0))
                columns = positions(base_column)
                full = sum(m*c*phases[(i*shifts[side]) % n] for i, (m, c) in
                           enumerate(zip(locked[side][1], columns)))
                probe = (u, v)[side]
                axis = (pow(probe*probe, -1, p)-side) % p
                if window(axis) and strict(axis, other):
                    full -= locked[side][0][0]*locked[other][0][logs[node(axis, other)]]
                marginals.append(full/root)
            equal(marginals[1]-marginals[0], principal)
            cell_prices.append(principal)
        equal(sum(cell_prices), sum(raw.values()))
        cuts, law_price = {}, [arb(0) for _ in outcomes]
        for z in matched:
            equal(sum(weights[z]), 1)
            cut = [0]
            for end in range(1, len(outcomes)):
                cut.append(int((p*sum(weights[z][:end])).ceil().unique_fmpz()))
            cut.append(p)
            cuts[z] = cut
            for cell in range(len(outcomes)):
                prob = arb(cut[cell+1]-cut[cell])/p
                assert abs(prob-weights[z][cell]) < arb(2)/p
                law_price[cell] += prob*raw[z]

        def assigned(z, slope, offset):
            label = (slope*z+offset) % p
            return next(i for i in range(4) if label < cuts[z][i+1])

        sharp = [arb(0) for _ in outcomes]
        for z in matched:
            sharp[assigned(z, 5, 7)] += raw[z]
        equal(sum(sharp), sum(raw.values()))
        if p == 53:
            # Exact joint averages of the sharp prices, including their variances.
            for cell in range(len(outcomes)):
                first = second = arb(0)
                for slope in range(p):
                    for offset in range(p):
                        price = sum((raw[z] for z in matched
                                     if assigned(z, slope, offset) == cell), arb(0))
                        first += price
                        second += price*price
                equal(first/(p*p), law_price[cell])
                variance = arb(0)
                for z in matched:
                    prob = arb(cuts[z][cell+1]-cuts[z][cell])/p
                    variance += raw[z]**2*prob*(1-prob)
                equal(second/(p*p)-law_price[cell]**2, variance)
        results.append(dict(u=u, v=v, matches=len(matched),
                            measured_weighted=[units(w) for w in cell_prices],
                            measured_sharp=[units(w) for w in sharp]))
    return dict(prime=p, precision_bits=ctx.prec, units="1e-9", odd_minus_pivot=odd_pivot,
                parent_atoms=[jq, jr], atom_masses=[units(uq), units(ur)],
                parent_responses=[units(dq), units(dr)], gap=units(gap),
                cancellation_scale=units(scale), zero_main_cell=[1, -1],
                coset="unrestricted" if p == 53 else "log(z+2) even",
                interval="[floor(p/8),floor(7p/8))",
                additive_seed=[5, 7], all_seed_variances_checked=p == 53, probes=results)


def square_audit(s):
    residue = {i*i % s for i in range(1, s)}
    d = next(i for i in range(2, s) if i not in residue)
    n = (s*s-1)//2
    index = (s+1)//2

    def multiply(x, y):
        a, b = x
        c, e = y
        return ((a*c+d*b*e) % s, (a*e+b*c) % s)

    def char(x):
        a, b = x
        norm = (a*a-d*b*b) % s
        return 0 if norm == 0 else 1 if norm in residue else -1

    for candidate in ((a, b) for b in range(1, s) for a in range(s)):
        step = multiply(candidate, candidate)
        w, log = (1, 0), {}
        while w not in log:
            log[w] = len(log)
            w = multiply(w, step)
        if len(log) == n:
            break
    assert len(log) == n
    cos = [(arb(2*i)/index).cos_pi() for i in range(index)]
    for a in range(1, s):
        equal(cos[log[a, 0] % index], 1)
    a, b = arb(2)/(s+1), arb(1)/(s-1)
    # On the subfield annihilator only the translated opposite mark can survive.
    atoms = [n*a*(b if i == s-1 else 0) for i in range(0, n, s-1)]
    equal(sum(atoms), 1)
    assert len(atoms) == index
    values = []
    for u, v in ((2, 3), (3, 2)):
        counts = [arb(0) for _ in outcomes]
        for re in range(s):
            for im in range(s):
                x = (u*u*re % s, u*u*im % s)
                y = (v*v*(re+1) % s, v*v*im % s)
                if (x not in log or y not in log or char((1-x[0], -x[1])) != 1
                        or char((1-y[0], -y[1])) != -1):
                    continue
                assert im != 0
                tx, ty = cos[log[x] % index], cos[log[y] % index]
                for i, (eps, delta) in enumerate(outcomes):
                    counts[i] += (1+eps*tx)*(1+delta*ty)/4
        prices = [2*c/(s*(s+1)) for c in counts]
        assert all(h > 0 for h in prices)
        values.append(dict(u=u, v=v, actual_prices=[units(h) for h in prices]))
    return dict(square=s*s, precision_bits=ctx.prec, units="1e-9",
                positive_first_cell_prime_prediction=units(n*(b-2*a)/(16*s)), probes=values)


if __name__ == "__main__":
    for order, pivot in ((53, None), (257, 48), (409, 95)):
        print(json.dumps(audit(order, pivot), sort_keys=True), flush=True)
    for subfield in (11, 19, 43):
        print(json.dumps(square_audit(subfield), sort_keys=True), flush=True)
