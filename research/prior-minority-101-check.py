"""Replay the projected prior and minority identities on the actual cold path."""

import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx


def main():
    source = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
    ctx.prec = 384
    size, block_size, depth = 384, 8, 16
    count = size//block_size
    signs = list(map(int, source["paley_sign"](769)))
    apply = source["apply"]
    sector = signs[::block_size]
    rho = arb(2)/(depth-1)
    zero = [arb(0)]*count
    e0 = zero.copy()
    e0[0] = arb(1)
    column = apply(e0, sector)

    def equal(a, b):
        assert (a-b).contains(0) and abs(a-b) < arb("1e-65"), (str(a), str(b))

    def accumulate(row, values, weight):
        for i, v in enumerate(values):
            row[i] += weight*v

    def block_means(row):
        return [sum(row[k::count])/block_size for k in range(count)]

    clique = {0, 1, 19, 30, 11, 29}
    assert all(sector[(i-j) % count] == 1 for i in clique for j in clique if i != j)
    q = [(v.real*v.real+v.imag*v.imag)/(count*len(clique))
         for v in acb.dft([int(i in clique) for i in range(count)])]
    pair = lambda row: sum(a*b for a, b in zip(q, row))
    w = arb(1)/8
    equal(q[0], w)
    state = [arb(0)]*size
    triangle, minority, flat, prior = (zero.copy() for _ in range(4))
    exterior, prior_erased, flat_erased = (zero.copy() for _ in range(3))
    c_tri = g_tri = c_prior = g_prior = loss_tri = loss_prior = loss_flat = arb(0)
    for j in range(depth):
        omega = arb(2*(depth-1-j))/(depth*(depth-1))
        amplitude = list(map(abs, state))
        a, z = block_means(amplitude), block_means(state)
        accumulate(triangle, a, omega)
        accumulate(minority, [x-y for x, y in zip(a, z)], omega)
        accumulate(flat, z, arb(1)/depth)
        new_source = amplitude.copy()
        new_source[0] = (4*size+state[0]*state[0]).sqrt()
        marked, mean = (new_source[0]-amplitude[0])/block_size, sum(new_source)/size
        c_tri += omega*marked
        g_tri += omega*mean
        it, ip, iz = 1+2*j, 2+2*j, 3+2*j
        assert all(k % count for k in (it, ip, iz))
        shell = a.copy()
        shell[0] = arb(0)
        shell[it % count] -= amplitude[it]/block_size
        accumulate(exterior, shell, omega)
        loss_tri += omega*column[-it % count]*amplitude[it]/block_size
        shell = z.copy()
        shell[0] = arb(0)
        shell[iz % count] -= state[iz]/block_size
        accumulate(flat_erased, shell, arb(1)/depth)
        loss_flat += q[iz % count]*state[iz]/(block_size*depth)
        if j < depth-1:
            accumulate(prior, a, arb(1)/depth)
            a[ip % count] -= amplitude[ip]/block_size
            accumulate(prior_erased, a, arb(1)/depth)
            loss_prior += q[ip % count]*amplitude[ip]/(block_size*depth)
            c_prior += marked/depth
            g_prior += mean/depth
        state = apply(new_source, signs)

    defect = [a-rho*b for a, b in zip(minority, prior)]
    defect[0] += c_tri-rho*c_prior
    projected = apply(defect, [int(s >= 0) for s in sector])
    for entry in projected:
        equal(entry, g_tri-rho*g_prior)
    f = apply(exterior, sector)[0]
    equal(f+loss_tri, (1-column[0])*triangle[0]-minority[0]
          +rho*flat[0]-column[0]*c_tri)
    equal(pair(prior_erased)+loss_prior, pair(prior))
    signed = pair(flat_erased)/w
    equal(signed+loss_flat/w, (pair(prior)-g_prior)/w+c_prior-flat[0])
    assert pair(prior_erased) >= prior_erased[0]*w
    print(json.dumps(dict(
        kind="genuine_prior_minority_and_original_block_quotient", prime=769,
        horizon=depth, block_size=block_size, quotient_order=count, root_mass="1/8",
        precision_bits=ctx.prec, erasures="triangular 1+2j, prior 2+2j, flat 3+2j",
        weighted_original_block_minority=minority[0].str(14),
        original_signed_flat_mean=flat[0].str(14),
        measured_triangular_forcing=f.str(14),
        positive_prior_price_after_erasures=(pair(prior_erased)/w).str(14),
        signed_flat_price_after_erasures=signed.str(14)
    ), sort_keys=True))


if __name__ == "__main__":
    main()
