"""Certify the signed price/root frontier at two costs on the erased p=769 path."""
import json
from pathlib import Path
import runpy

from flint import arb, arb_mat, ctx, fmpq


def replay():
    previous = runpy.run_path(str(Path(__file__).with_name("astra-quotient-99-check.py")))
    base = previous["base"]
    ctx.prec = 384
    p, n, b, m, J = 769, 384, 48, 8, 16
    signs = list(map(int, base["paley_sign"](p)))
    state = [arb(0)] * n
    prices = [arb(0)] * b
    for j in range(J):
        erased = 2 + 2*j
        assert erased % b
        for r in range(1, b):
            block = sum(state[r::b])
            if erased % b == r:
                block -= state[erased]
            prices[r] += block/(m*J)
        source = list(map(abs, state))
        source[0] = (4*n + state[0]**2).sqrt()
        state = base["apply"](source, signs)
    head = [r for r in range(b) if prices[r] > arb(6)/5]
    assert head == [10, 12, 36, 38]
    assert all(prices[r] < arb(6)/5 for r in range(b) if r not in head)
    hard = previous["replay"]()["four_head_all_law_root_strict_upper"]
    assert hard == "0.076456"

    # The head-zero direction in the mean-zero allowed sector. A uniform
    # background of size 0.137 pays exactly the uniform mass on the head.
    cosine = [arb.cos_pi_fmpq(fmpq(2*r, b)) for r in range(b)]
    kernel = [sum(cosine[(r*k) % b] for k in range(b) if signs[m*k] == 1)/b
              for r in range(b)]
    gram = arb_mat([[kernel[(r-t) % b] for t in head] for r in head])
    coeff = gram.solve(arb_mat([[kernel[t]] for t in head]))
    column = [kernel[r]-sum(kernel[(r-t) % b]*coeff[j, 0] for j, t in enumerate(head))
              for r in range(b)]
    background = arb(137)/1000
    trial = [(v+background)/(b*background) for v in column]
    assert all(x > 0 for x in trial)
    assert all((trial[r]-arb(1)/b).contains(0) for r in head)
    assert (sum(trial)-1).contains(0) and trial[0] > arb(hard)
    direct = sum(price*x for price, x in zip(prices, trial))/trial[0]

    # The fixed support came from a floating LP. Exact feasibility and
    # optimality below use only the actual trigonometric and orbit entries.
    support = [0, 1, 2, 4, 5, 8, 9, 10, 13, 15, 18, 19, 22, 26,
               29, 30, 35, 38, 39, 40, 43, 44, 46, 47]
    forbidden = [k for k in range(1, b//2+1) if signs[m*k] == -1]
    moments = [[arb(1)]*b]
    moments += [[arb.cos_pi_fmpq(fmpq(2*r*k, b)) for r in range(b)] for k in forbidden]
    moments += [[arb.sin_pi_fmpq(fmpq(2*r*k, b)) for r in range(b)]
                for k in forbidden if 2*k != b]
    results = []
    for cost in [fmpq(0), fmpq(-1, 100)]:
        rows = moments + [[prices[r] - arb(cost)*int(r == 0) for r in range(b)]]
        basis = arb_mat([[row[r] for r in support] for row in rows])
        assert len(rows) == len(support)
        unit = arb_mat([[1]] + [[0]]*(len(rows)-1))
        primal = basis.solve(unit)
        dual = basis.transpose().solve(unit)  # root is the first support coordinate
        assert all(primal[i, 0] > 0 for i in range(len(support)))
        assert dual[len(rows)-1, 0] > 0
        for r in range(b):
            slack = sum(dual[i, 0]*row[r] for i, row in enumerate(rows)) - int(r == 0)
            if r in support:
                assert slack.contains(0)
            else:
                assert slack > 0
        assert (primal[0, 0]-dual[0, 0]).contains(0)
        assert primal[0, 0] > arb(hard)
        results.append(dict(normalized_price_cap=str(cost),
                            max_root_units_1e_minus_9=base["enclose"](primal[0, 0])))
    return dict(prime=p, block_order=m, quotient_order=b, sign=1, horizon=J,
                precision_bits=ctx.prec, erasure="2+2j", cutoff="6/5", head=head,
                exact_avoidance_strict_upper=hard, signed_frontier=results,
                common_basic_support=support, centered_column_background="137/1000",
                centered_column_root_units_1e_minus_9=base["enclose"](trial[0]),
                centered_column_price_units_1e_minus_9=base["enclose"](direct))


if __name__ == "__main__":
    print(json.dumps(replay(), sort_keys=True))
