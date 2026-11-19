"""Certify quantile envelopes and feasible restricted frame packings at prime fields."""
import importlib.util
import json
from pathlib import Path

from flint import acb, arb, ctx

path = Path(__file__).with_name("astra-transport-52-check.py")
spec = importlib.util.spec_from_file_location("transport", path)
transport = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transport)
ep = transport.ep
ctx.prec = 320


def check(prime):
    mask = transport.late.paley_sign(prime)
    n = len(mask)
    root_n = arb(n).sqrt()
    pair, error = ep.solve_prime_pair(mask)
    assert error is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    probabilities = {s: [x / root_n for x in pair[s]] for s in pair}
    for s, law in probabilities.items():
        spectrum = acb.dft(law)
        assert all(spectrum[j].contains(0) for j in range(n) if mask[j] == -s)
    v = [arb(0)] * n
    rows = []
    for t in range(1, 17):
        activation = [abs(x) for x in v]
        activation[0] = (4 + v[0] ** 2).sqrt()
        v = ep.apply_multiplier(activation, mask)
        if t not in (1, 8, 16):
            continue
        z = [side * root_n * x for x in v]
        first = transport.dot(probabilities[side], z)
        second = -transport.dot(probabilities[-side], z)
        distance = transport.late.cross_distance(
            z, [x * n for x in probabilities[side]], [x * n for x in probabilities[-side]])
        envelope = (first + second + distance) / 2
        # Integrate the maximum of the survival functions at rounded sites.
        sites = [(x.mid(), w, arb(0)) for x, w in zip(z, probabilities[side])]
        sites += [(-x.mid(), arb(0), w) for x, w in zip(z, probabilities[-side])]
        sites.sort(key=lambda item: item[0])
        last = sites[0][0]
        value = last
        a = b = arb(1)
        for position, wa, wb in sites:
            value += (position - last) * (a + b + abs(a - b)) / 2
            last = position
            a -= wa
            b -= wb
        error = sum(x.rad() * (u + w) for x, u, w in zip(z, probabilities[side], probabilities[-side]))
        assert (value + arb(0, error.upper()) - envelope).contains(0)
        lower_packs = {}
        threshold = arb(2) if t == 1 else arb(t) / 8
        for s in pair:
            selected = [i for i, x in enumerate(v) if i and s * root_n * x > threshold]
            if not selected:
                continue
            count = len(selected)
            selected = set(selected)
            transform = acb.dft([arb(int(i in selected)) / count for i in range(n)])
            eta = max(abs(transform[j]).upper() for j in range(n) if mask[j] == -s)
            mass = min(arb(1) / (1 + 3 * eta), pair[s][0] * count / root_n)
            lower_packs[s] = dict(count=count, dimension_cap=4, packing_lower=str(mass.lower()),
                                  actual_mass=str(sum(probabilities[s][i] for i in selected)))
        M = max(abs(x).upper() for x in z)
        seed_gap = None
        if t == 1:
            bound = M - (M-first)*(M-second)/(2*M)
            assert envelope < bound
            seed_gap = str(bound)
        rows.append(dict(t=t, envelope=str(envelope), threshold=str(threshold),
                         seed_envelope_upper=seed_gap, packs=lower_packs))
    print(json.dumps(dict(p=prime, rows=rows), sort_keys=True), flush=True)


if __name__ == "__main__":
    for p in (101, 173, 401):
        check(p)
