"""Certify the terminal transfer and truncated Abel sum on the actual 769 orbit."""
import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx


def main():
    ctx.prec = 384
    parent = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
    apply = parent["apply"]
    prime, n, m, J = 769, 384, 8, 16
    b = n // m
    signs = list(map(int, parent["paley_sign"](prime)))
    mask = signs[::m]
    jacobi = apply([1] + [0] * (b - 1), mask)
    lam = jacobi[0]
    eta = arb(2) / (J * (J - 1))

    def equal(x, y):
        err = x - y
        assert err.contains(0) and abs(err) < arb("1e-64"), err

    def trial(clique):
        assert all(mask[(i - j) % b] == 1 for i in clique for j in clique if i != j)
        transform = acb.dft([int(r in clique) for r in range(b)])
        return [(z.real * z.real + z.imag * z.imag) / (len(clique) * b) for z in transform]

    first = trial({0, 1, 11, 19, 29, 30})
    second = trial(set(range(0, b, 8)))
    for q in (first, second):
        equal(q[0], arb(1) / 8)
    pair = lambda q, row: sum(x * y for x, y in zip(q, row))
    blocks = lambda row: [sum(row[r::b]) / m for r in range(b)]
    state = [arb(0)] * n
    previous = state.copy()
    force, prior, minority, gain, mean, root_mark = [arb(0) for _ in range(6)]
    prior_loss = force_loss = endpoint = previous_flat = arb(0)
    for j in range(J - 1):
        amplitude = list(map(abs, state))
        a = blocks(amplitude)
        z = blocks(state)
        exterior = a.copy()
        exterior[0] = arb(0)
        signed_ext = z.copy()
        signed_ext[0] = arb(0)
        drive = pair(jacobi, exterior)
        wj = eta * (J - 1 - j)
        tri_idx, prior_idx = 1 + 2*j, 2 + 2*j
        assert tri_idx % b and prior_idx % b
        cut = jacobi[-tri_idx % b] * amplitude[tri_idx] / m
        force += wj * drive
        force_loss += wj * cut
        prior += pair(first, exterior) / J
        prior_loss += first[prior_idx % b] * amplitude[prior_idx] / (m * J)
        source = amplitude.copy()
        source[0] = (4*n + state[0]**2).sqrt()
        mark = (source[0] - amplitude[0]) / m
        g2 = sum(source) / n
        if j < J - 2:
            gain += wj * (1 - lam) * a[0]
            root_mark += wj * (1 - lam) * mark
            mean += wj * g2
            minority += wj * (pair(first, exterior) - pair(first, signed_ext))
        previous, state = state, apply(source, signs)
        if j == J - 2:
            last_f = drive
            last_f_cut = drive - cut
            endpoint = pair(first, signed_ext)
            last_a, last_mark, last_g = a[0], mark, g2
            last_ext = exterior
        previous_flat += pair(first, signed_ext) / J

    w = first[0]
    # d_0=0. The final preceding signed value has two copies in the truncated slope.
    slope = eta * (J * previous_flat + endpoint) / w

    equal(force - eta*last_f + slope, gain + root_mark + (minority - mean)/w)
    assert 2*(J*eta)*prior/w >= slope
    late_diff = [v - u for v, u in zip(state, previous)]
    inc = blocks(late_diff)
    inc[0] = arb(0)
    inc_erased = inc.copy()
    erased_inc = 39
    inc_erased[erased_inc % b] -= late_diff[erased_inc]/m
    increment_prices = []
    for q in (first, second):
        root = q[0]
        last_signed = blocks(previous)
        last_signed[0] = arb(0)
        reserve = (pair(q, last_ext) - pair(q, last_signed))/root
        equal(pair(q, inc)/root, (1-lam)*(last_a+last_mark) - last_f - last_g/root + reserve)
        increment_prices.append((pair(q, inc_erased)/root).str(14))
    threshold = arb(1)/5
    head = [r for r, v in enumerate(inc_erased) if v > threshold]
    assert head == [2, 8, 40, 46]
    assert all(inc_erased[r] < threshold for r in range(b) if r not in head)
    assert all(r % 6 for r in head)  # The second clique law lives on 6Z/48.
    total_energy = sum(y*y for y in late_diff)/n
    assert total_energy < 4
    assert sum(y*y for y in inc_erased)/b < total_energy
    print(json.dumps(dict(prime=prime, sign=1, quotient_order=b, horizon=J, root="1/8",
        precision_bits=ctx.prec, erasures="triangular 1+2j; prior 2+2j; increment 39",
        original_triangular=(force-force_loss).str(14), last_erased_kick=last_f_cut.str(14),
        truncated_triangular=(force-force_loss-eta*last_f_cut).str(14),
        nonnegative_preceding_exterior_price=((prior-prior_loss)/w).str(14),
        terminal_signed_increment_prices=increment_prices,
        increment_cutoff="1/5", increment_head=head,
        physical_increment_mean_square=total_energy.str(14),
        measured_block_increment_mean_square=(sum(y*y for y in inc_erased)/b).str(14)
    ), sort_keys=True))


if __name__ == "__main__":
    main()
