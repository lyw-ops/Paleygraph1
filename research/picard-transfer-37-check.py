"""Validate transfer normalization on actual prime- and square-field orbits."""
import json
from pathlib import Path
import runpy

from flint import arb, arb_mat, ctx


def check(q, square_base, depth):
    cold = runpy.run_path(str(Path(__file__).with_name("astra-cold-37.py")))
    ctx.prec = 256
    sign = cold["square_field_sign"](square_base) if square_base else cold["paley_sign"](q)
    n = len(sign)
    # Direct cosine sums give a DFT-independent check of the normalization.
    kernel = [sum(arb(int(s)) * (2 * arb.pi() * (k * j % n) / n).cos()
                  for k, s in enumerate(sign)) / n for j in range(n)]
    labels = [[0]] + [[j, n-j] for j in range(1, n//2)] + [[n//2]]
    size = len(labels)
    K = arb_mat([[sum(kernel[(i-k) % n] for k in orbit)
                  for orbit in labels] for i in range(size)])
    tau = arb(1) / 20
    W = 1 + (n-1)*tau/n
    w4 = [arb(4)] + [4*tau/n]*(size-1)
    fixed = cold["real_root"](K, sign, tau, w4)

    def total(values):
        return sum(len(orbit) * value for orbit, value in zip(labels, values))

    v = [arb(0)]*size
    dissipation = arb(0)
    mark_error = arb(0)
    for _ in range(depth+2):
        s = [(x**2+w).sqrt() for x, w in zip(v, w4)]
        v_next = (K * arb_mat(size, 1, s)).entries()
        H = total([2*w*(((x/w.sqrt()).asinh()-(y/w.sqrt()).asinh()).cosh()-1)
                   for x, y, w in zip(v, fixed, w4)])
        N = (total(s)/arb(n).sqrt()-2*W.sqrt())**2
        D_drop = total([(x-y)**2-(u-y)**2 for x, u, y in zip(v, v_next, fixed)])
        assert (D_drop-H-N).contains(0)
        assert (total([u**2-x**2 for u,x in zip(v_next,v)])-4*W
                + total(s)**2/n).contains(0)
        dissipation += H+N
        mark_error += (v[0]-fixed[0])**2
        v = v_next
    C = max((1+4*q*W/n).upper(), (arb(9)*q/n).upper())
    assert mark_error < C*dissipation
    assert dissipation < 4*W*arb(q).sqrt()
    print(json.dumps(dict(kind="arb_actual_picard_transfer_check", order=q,
                          tau="1/20", precision=ctx.prec, checked_steps=depth+2,
                          stationary_mark=(fixed[0]/2).asinh().str(18),
                          mean_square_mark_error=(mark_error/(depth+2)).str(18)),
                     sort_keys=True))


if __name__ == "__main__":
    for order, root in [(13, None), (17, None), (113, None), (121, 11)]:
        check(order, root, 48)
