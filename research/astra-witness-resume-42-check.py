"""Interval replay of finite true-orbit witness inequalities."""

import json
from pathlib import Path
import sys

from flint import arb, arb_mat, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign


def check(q, sigma, floor):
    tau = arb(floor[0]) / floor[1]
    if q == 101:
        assert pow(2, 50, q) != 1 and pow(2, 20, q) != 1
        symbols = [pow((1-pow(4, j, q)) % q, 50, q) for j in range(50)]
        signs = [s if s != 100 else -1 for s in symbols]
    else:
        assert q == 49 and sigma == 1
        signs = square_field_sign(7)
    n = len(signs)
    root = arb(n).sqrt()
    W = 1+(1-arb(1)/n)*tau
    cosines = [(arb(2*j)/n).cos_pi() for j in range(n)]
    col = [sum(int(s)*cosines[i*j % n] for j, s in enumerate(signs))/n
           for i in range(n)]
    kernel = arb_mat([[col[(i-j) % n] for j in range(n)] for i in range(n)])
    if q == 101:
        qr = arb(q).sqrt()
        prob = [(qr+n*int(i == 0)+sigma*n*col[i])/(n*(qr+1)) for i in range(n)]
        assert all(x > 0 for x in prob)
    else:
        prob = [arb(1)/4 if i % 6 == 0 else arb(0) for i in range(n)]
    assert (sum(prob)-1).contains(0)
    kp = kernel*arb_mat(n, 1, prob)
    assert all((kp[i, 0]-sigma*(prob[i]-arb(1)/n)).contains(0) for i in range(n))
    alpha = root*prob[0]
    gamma = alpha-W.sqrt()
    assert gamma < 0
    a, b = 1/(4*W.sqrt()), 2*tau
    F = H = R = arb(0)
    v = [arb(0)]*n
    first = source0 = None
    for t in range(13):
        y = [root*x for x in v]
        f = [(x*x+4*tau).sqrt() for x in y]
        phi = [x/root for x in f]
        phi[0] = (4+v[0]**2).sqrt()
        nxt_mat = kernel*arb_mat(n, 1, phi)
        nxt = [nxt_mat[i, 0] for i in range(n)]
        if t == 0:
            first, source0 = nxt, phi
        m = sigma*sum(x*p for x, p in zip(y, prob))
        if t in (4, 12):
            U = F+H
            assert (m+R-2*gamma*t-U).contains(0)
            d = U+tau.sqrt()+2*(W.sqrt()*U).sqrt()
            lhs = U+4*(a*b).sqrt()*(d.sqrt()+(d+F).sqrt())
            rhs = 3*(arb.pi()**2*a*b*b*t)**(arb(1)/3)
            assert lhs > rhs
            delta = [v1-v0 for v1, v0 in zip(nxt, first)]
            S = [root*(pt-p0) for pt, p0 in zip(phi, source0)]
            avg = sum(S)/n
            scores = []
            for shift in range(n):
                p = [prob[(i-shift) % n] for i in range(n)]
                score = sigma*root*sum(x*z for x, z in zip(p, delta))
                assert (score-sum(x*z for x, z in zip(p, S))+avg).contains(0)
                scores.append(score)
            assert sum(x*x for x in scores)/n < sum(x*x for x in delta) < 4*W*t
            print(json.dumps(dict(q=q, sigma=sigma, tau=f"{floor[0]}/{floor[1]}",
                                  T=t, precision=ctx.prec, finite_action_left=str(lhs),
                                  finite_action_right=str(rhs), translated_scores=n,
                                  rooted_score=str(scores[0])), sort_keys=True))
        H += sum(p*x for p, x in zip(prob, f))-m
        R += alpha*(2-phi[0]+f[0]/root)
        F += 2*(W.sqrt()-sum(phi)/(2*root))
        v = nxt


if __name__ == "__main__":
    ctx.prec = 256
    check(101, 1, (1, 20))
    check(101, -1, (1, 20))
    check(49, 1, (1, 1))
