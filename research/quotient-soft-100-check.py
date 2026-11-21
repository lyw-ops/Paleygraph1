"""Outward trial comparison after an exact signed autocorrelation repair."""

import json
from pathlib import Path
import runpy

from flint import acb, arb, ctx


def main():
    base = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
    ctx.prec = 384
    prime, size, depth, block_size = 769, 384, 16, 8
    count = size//block_size
    signs = list(map(int, base["paley_sign"](prime)))
    state = [arb(0)]*size
    prices = [arb(0)]*count
    for j in range(depth):
        erased = 2+2*j
        assert erased % count
        for block in range(1, count):
            price = sum(state[block::count])
            if erased % count == block:
                price -= state[erased]
            prices[block] += price/(block_size*depth)
        source = list(map(abs, state))
        source[0] = (4*size+state[0]**2).sqrt()
        state = base["apply"](source, signs)

    clique = {0, 1, 19, 30, 11, 29}
    assert all(signs[block_size*((x-y) % count)] == 1
               for x in clique for y in clique if x != y)
    modes = acb.dft([int(x in clique) for x in range(count)])
    q = [(x.real*x.real+x.imag*x.imag)/(count*len(clique)) for x in modes]
    multiplicities = [sum((x+shift) % count in clique for x in clique)
                      for shift in range(count)]
    energy = sum(value**2 for value in multiplicities)
    assert 288*energy == 19*count*len(clique)**2
    error = arb("1e-90")
    assert abs(sum(q)-1) < error and abs(q[0]-arb(1)/8) < error
    autocorrelation = [sum(q[x]*q[(x+offset) % count] for x in range(count))
                       for offset in range(count)]
    repaired = [v-(q[x]+q[-x])/8 for x, v in enumerate(autocorrelation)]
    assert abs(sum(repaired)-arb(3)/4) < error
    assert abs(repaired[0]/(arb(3)/4)-arb(5)/108) < error
    assert repaired[0] > arb(3)/100
    for coefficient, sign in zip(acb.dft(repaired), signs[::block_size]):
        if sign == -1:
            assert abs(coefficient) < error and coefficient.contains(0)
    original_price = sum(x*y for x, y in zip(prices, autocorrelation))/autocorrelation[0]
    repaired_price = sum(x*y for x, y in zip(prices, repaired))/repaired[0]
    assert arb("2.255343363") < original_price < arb("2.255343364")
    assert arb("1.796814795") < repaired_price < arb("1.796814796")
    print(json.dumps(dict(
        kind="genuine_erased_signed_autocorrelation_repair",
        precision_bits=ctx.prec, prime=prime, block_size=block_size, horizon=depth,
        base_clique=sorted(clique), base_root="1/8", atom_removed="1/8 at zero",
        repaired_root="5/108", previous_normalized_price=original_price.str(14),
        repaired_normalized_price=repaired_price.str(14),
    ), sort_keys=True))


if __name__ == "__main__":
    main()
