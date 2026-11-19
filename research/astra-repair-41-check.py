"""Check the finite reserve identities and inequalities on actual subfield tests."""

import json
from pathlib import Path
import sys

from flint import arb, arb_mat, ctx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from square_control import square_field_sign


def check(r, floor):
    signs = square_field_sign(r)
    n = len(signs)
    root_n = arb(n).sqrt()
    step = r-1
    support = list(range(0, n, step))
    alpha = root_n / len(support)
    tau = arb(1) if floor == "one" else (alpha**2-1)/(1-arb(1)/n)
    W = 1+(1-arb(1)/n)*tau
    gamma = alpha-W.sqrt()
    gamma_neg = -gamma if floor == "one" else arb(0)
    cosines = [(arb(2*j)/n).cos_pi() for j in range(n)]
    col = [sum(int(s)*cosines[i*j % n] for j, s in enumerate(signs))/n
           for i in range(n)]
    K = arb_mat([[col[(i-j) % n] for j in range(n)] for i in range(n)])
    prob = [arb(int(i in support))/len(support) for i in range(n)]
    kp = K * arb_mat(n, 1, prob)
    assert all((kp[i, 0]-prob[i]+arb(1)/n).contains(0) for i in range(n))
    v = [arb(0)]*n
    H = R = F = losses = arb(0)
    for t in range(16):
        scaled = [root_n*x for x in v]
        m = sum(prob[i]*scaled[i] for i in support)
        f = [(x**2 + 4*tau).sqrt() for x in scaled]
        b = (4+v[0]**2).sqrt()-f[0]/root_n
        H += sum(prob[i]*f[i] for i in support)-m
        R += alpha*(2-b)
        phi = [x/root_n for x in f]
        phi[0] += b
        g = sum(phi)/(2*root_n)
        F += 2*(W.sqrt()-g)
        losses += (W.sqrt()-g)**2
        nxt = K * arb_mat(n, 1, phi)
        v = [nxt[i, 0] for i in range(n)]
        T = t+1
        if T not in (4, 16):
            continue
        m = root_n*sum(prob[i]*v[i] for i in support)
        energy = sum(x**2 for x in v)
        assert (m+R-2*gamma*T-F-H).contains(0)
        assert (W.sqrt()*F-energy/4-losses).contains(0)
        V = m+R+2*T*gamma_neg
        U = F+H
        assert V*(V+2*(T*W.sqrt()*V).sqrt()+tau.sqrt()) > 2*tau*T
        assert U > tau/alpha*(1+2*alpha*T/(U+tau.sqrt())).log()
        print(json.dumps(dict(q=r*r, floor=floor, T=T, precision=ctx.prec,
                              witness_signed_mean=str(m), total_curvature=str(H),
                              marked_error=str(R)), sort_keys=True))


if __name__ == "__main__":
    ctx.prec = 256
    for root in (7, 11):
        for label in ("one", "critical"):
            check(root, label)
