"""Enclose selective Schur rows at four genuine primary endpoints and cold windows."""
import json
import runpy
from pathlib import Path

from flint import acb, arb, arb_mat, ctx

source = runpy.run_path(str(Path(__file__).with_name("endpoint-direction-45-check.py")))
ctx.prec = 768


def record_interval(value):
    value = value * 10**7
    return [int(value.lower().floor().unique_fmpz()), int(value.upper().ceil().unique_fmpz())]


def cold_mask(sign, side, start, n):
    def kernel(v):
        ft = acb.dft(v)
        return [z.real for z in acb.dft([a * b for a, b in zip(ft, sign)], inverse=True)]

    root = [arb(i == 0) for i in range(n)]
    col = kernel(root)
    pin = [1 - (a - arb(1)/n + side*b) / (1 - arb(1)/n + side*col[0])
           for a, b in zip(root, col)]
    weights = [25, 64, 81, 64, 25]
    profile = [arb(0)] * n
    state = [arb(0)] * n
    for j in range(start + len(weights)):
        phi = [(4 + state[0]**2).sqrt()] + [abs(v) for v in state[1:]]
        if j >= start:
            raw = [arb(n).sqrt() * (v + side*w)/2 for v, w in zip(phi, state)]
            mean = sum(raw)/n
            proj = [(v + mean + side*w)/2 for v, w in zip(raw, kernel(raw))]
            shift = (1 + arb(1)/1000)*proj[0]/arb(n).sqrt() - mean
            weight = arb(weights[j-start])/sum(weights)
            profile = [a + weight*(v + shift*b) for a, v, b in zip(profile, proj, pin)]
        state = kernel(phi)
    threshold = -arb(1)/40
    assert all(v > threshold or v < threshold for v in profile)
    return [i for i in range(1, n) if profile[i] < threshold]


def schur_row(col, i, targets):
    n = len(col)
    heads = sorted(set(targets) - {i})
    if not heads:
        return [col[(i-j) % n] for j in range(n)]
    principal = arb_mat([[col[(u-v) % n] for v in heads] for u in heads])
    coeff = list(principal.solve(arb_mat([[col[(j-i) % n]] for j in heads])))
    row = [col[(i-j) % n] - sum(c*col[(u-j) % n] for c, u in zip(coeff, heads))
           for j in range(n)]
    assert all(row[j].contains(0) for j in heads) and row[i] > 0
    return row


def check(p, start, tops):
    signs = source["paley_sign"](p)
    n = len(signs)
    pair, err = source["solve_prime_pair"](signs)
    assert err is None
    side = 1 if pair[1][0] > pair[-1][0] else -1
    q = [v/arb(n).sqrt() for v in pair[side]]
    assert min(q[i] for i in tops) > max(q[j] for j in range(n) if j not in tops)
    x = [(v-arb(1)/n).max(0) for v in q]
    z = [v-w for v, w in zip(q, x)]
    sites = cold_mask(list(map(int, signs)), -side, start, n)
    selected = [i for i in sites if x[i] > 0]
    assert all(x[i] > 0 or x[i].is_zero() for i in sites)
    col = [z.real for z in acb.dft([int(t == -side) for t in signs], inverse=True)]
    h0 = {i: schur_row(col, i, tops) for i in selected}
    exterior = sorted(set(range(n)) - set(tops))
    exterior_mass = sum(x[j] for j in exterior)
    cap_excess = cap_low_energy = arb(0)
    for i in selected:
        row = h0[i]
        tail = [j for j in exterior if j != i and x[j] > 0]
        coefficient = max(((-row[j]).max(0)/row[i] for j in tail), default=arb(0))
        excess = (q[i]-coefficient*exterior_mass).max(0)
        low = sum(row[j]*z[j] for j in exterior if j != i)/row[i]
        assert excess.is_zero() or abs(low) > excess
        cap_excess += n*excess**2
        cap_low_energy += n*low**2
    graph = {}
    incoming = [arb(0)] * n
    original = removed_private = arb(0)
    for i in selected:
        price = [-n*x[i]*h0[i][j]*x[j] for j in range(n)]
        original += sum(price[j] for j in range(n) if j != i and j not in tops)
        candidates = [j for j in range(n) if j not in tops and j != i and price[j] > 0]
        # Midpoints choose arbitrary legal deletions; rounded ties use increasing site index.
        heads = sorted(candidates, key=lambda j: (-round(float(price[j].mid()), 14), j))[:2]
        graph[i] = heads
        for j in heads:
            incoming[j] += x[i]
            removed_private += price[j]
    hubs = sorted((j for j in range(n) if incoming[j] > 0),
                  key=lambda j: (-round(float(incoming[j].mid()), 14), j))[:2]
    common = set(tops) | set(hubs)
    signed = diag = residual = removed_all = arb(0)
    min_diag = arb(1)
    for i in selected:
        blocked = (common | set(graph[i])) - {i}
        row = schur_row(col, i, blocked)
        min_diag = min(min_diag, row[i])
        diag += n*x[i]**2*row[i]
        signed -= n*x[i]*sum(row[j]*x[j] for j in range(n) if j != i and j not in blocked)
        residual += n*x[i]*sum(row[j]*z[j] for j in range(n) if j not in blocked)
        removed_all -= n*x[i]*sum(h0[i][j]*x[j] for j in blocked-set(tops))
    assert (diag + residual - signed).contains(0)
    assert removed_private > 0 and signed > 0
    return dict(p=p, side=side, start=start, top=tops, hubs=hubs, mask_size=len(sites),
                clipped_mask_size=len(selected), mark=record_interval(pair[side][0]),
                hinge=record_interval(n*sum(x[i]**2 for i in selected)),
                top_mask_hinge=record_interval(n*sum(x[i]**2 for i in selected if i in tops)),
                exterior_clipped_mass=record_interval(exterior_mass),
                masked_cap_excess=record_interval(cap_excess), masked_low_energy=record_interval(cap_low_energy),
                initial_signed=record_interval(original),
                initial_private_price=record_interval(removed_private),
                initial_added_deletions_price=record_interval(removed_all),
                final_signed=record_interval(signed), final_diagonal=record_interval(diag),
                final_low_inner=record_interval(residual), min_local_diagonal=record_interval(min_diag),
                units="1e-7", precision=ctx.prec)


if __name__ == "__main__":
    for case in [(101, 24, [0, 10, 40]), (257, 10, [0, 33, 95]),
                 (409, 20, [0, 9, 33, 171, 195]),
                 (769, 2, [0, 89, 147, 168, 216, 237, 295])]:
        print(json.dumps(check(*case), sort_keys=True), flush=True)
