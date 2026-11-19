"""Check prime spectral escape, the two coset limits, and a square physical control."""
import json
from fractions import Fraction
from pathlib import Path
import runpy

from flint import acb, arb, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-quartic-89-check.py")))
ctx.prec = 384
interval = prior["interval"]


def prime():
    face = prior["face"]
    signs = list(map(int, face["mask"]))
    n = len(signs)
    rows, opposite = face["faces"]()
    q = [row[0] for row in rows]
    a = q[0]
    b, masks, heights = prior["delayed_masks"](signs)
    assert b == 11
    # The nonnegative anchor directions have positive derivatives at the origin
    # for length two; every row agrees on the length-eight mask.
    assert all(sum((q[i] / a) ** 3 * rows[i][j] for i in masks[2]) > 0 for j in (1, 2))
    assert all(rows[i][j].is_zero() for i in masks[8] for j in (1, 2))
    cubic = [(q[i] / a) ** 3 if i in masks[2] else arb(0) for i in range(n)]
    total = sum(cubic)
    alpha = a * total
    muhat = [z.real for z in acb.dft([v / total for v in cubic])]
    qhat = [z.real for z in acb.dft(q)]
    kappa = max(abs(muhat[i]) for i in range(n) if signs[i] == -1)
    cut = ((1 + kappa) / 2).sqrt()
    assert kappa < arb(84) / 100 and muhat[0].contains(1)
    assert all(abs(muhat[i]) < cut for i in range(1, n))
    k = 128
    bound = 1 / (n * a) + cut ** (k - 1) / alpha.sqrt()
    actual = sum(qhat[i] * muhat[i] ** k for i in range(n)) / (n * a)
    assert actual < bound < arb(18) / 100

    # At length eight the maximal Fourier set is exactly the annihilator
    # of the order-three subgroup. Equal shortfalls give an exact integer walk.
    assert masks[8] == [8, 40] and (q[8] - q[40]).contains(0)
    K, C = [0, 16, 32], [8, 24, 40]
    H = [i for i in range(n) if i % 3 == 0]
    assert {i for i in range(n) if (16 * i) % n == 0} == set(H)
    assert any(signs[i] == -1 for i in H)
    counts = [int(i == 0) for i in range(n)]
    distances = {}
    for step in range(1, 22):
        counts = [counts[(i - 8) % n] + counts[(i + 8) % n] for i in range(n)]
        if step not in (20, 21):
            continue
        target = C if step % 2 else K
        tv = sum(abs(Fraction(c, 2 ** step) - Fraction(int(i in target), 3))
                 for i, c in enumerate(counts)) / 2
        assert tv == Fraction(2, 3 * 2 ** step)
        root = sum(c * q[i] for i, c in enumerate(counts)) / (2 ** step * a)
        uniform_root = sum(q[i] for i in target) / (len(target) * a)
        tv_ball = arb(tv.numerator) / tv.denominator
        if step % 2:
            assert abs(root - uniform_root) < tv_ball
        else:
            assert q[16].is_zero() and q[32].is_zero()
            assert (root - uniform_root - tv_ball).contains(0)
        distances[step] = str(tv)
    qK, qC = (sum(q[i] for i in coset) for coset in (K, C))
    overlap = sum(sum(q[i] for i in range(j, n, 16))
                  * sum(opposite[i] for i in range(j, n, 16)) for j in range(16))
    assert (overlap - arb(3) / n).contains(0)
    assert all(heights[i] > arb(15) / 100 for i in masks[8])
    return dict(prime=97, terminal=11, length2_alpha=interval(alpha),
                length2_forbidden_max=interval(kappa), length2_high_characters=1,
                length2_root_ratio_step128=interval(actual), length2_upper=interval(bound),
                length8_even_coset=K, length8_odd_coset=C, length8_tv=distances,
                length8_even_root_limit=interval(qK / (3*a)),
                length8_odd_root_limit=interval(qC / (3*a)),
                quotient_overlap_exact="3/48", precision_bits=ctx.prec, units="1e-9")


def square(r):
    signs = list(map(int, prior["square_field_sign"](r)))
    n = len(signs)
    _, masks, heights = prior["delayed_masks"](signs)
    K = list(range(0, n, r - 1))
    m = len(K)
    P = set(masks[8])
    assert set(K).intersection(P) == set(K[1:])
    # The genuine subfield primary law is uniform on K. Its sharp cubic is
    # uniform on K minus the root. Its nontrivial restricted eigenvalue
    # is -1/(m-1), and every walk therefore has normalized root test one.
    assert all(signs[i] != -1 for i in range(n) if (i * (r - 1)) % n == 0)
    assert min(heights[i] for i in K[1:]) > arb(15) / 100
    assert (n // m) * (n // m - 1) > n
    return dict(field_order=r*r, length=8, subgroup_size=m,
                positional_clique=n//m, alpha=str(Fraction(m-1, m)),
                eta=1, all_walk_root_ratios=1,
                total_variation_after_step20=str(Fraction(m-1, m * (m-1)**20)),
                physical_height_payment=interval(sum(heights[i] for i in K[1:])/m),
                precision_bits=ctx.prec, units="1e-9")


if __name__ == "__main__":
    for row in [prime(), square(31)]:
        print(json.dumps(row, sort_keys=True))
