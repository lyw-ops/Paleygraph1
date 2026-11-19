"""Check real reciprocal moment identities at an actual cold prime and the constants."""
import json

from flint import arb, ctx

ctx.prec = 192
one = arb(1)
q = 13
n = 6
t = arb(30) / 19
c = one - one / n
W = 1 + c * t
root = arb(q).sqrt()
r = root / (root + 1)
cosine = [one, one / 2, -one / 2, -one, -one / 2, one / 2]
plus = [1 + z / 2 for z in cosine]
minus = [n / (W * plus[0])] + [t / (W * v) for v in plus[1:]]
k = [(2 * cosine[i] - 2 * cosine[2*i % n] - (-1)**i) / root for i in range(n)]


def bulk(values):
    return sum(values[1:]) / n


for sign, row in ((1, plus), (-1, minus)):
    assert (sum(row) - n).contains(0)
    own = 1 + (n - 1 - sign) / (root + 1)
    opposite = 1 + (n - 1 + sign) / (root + 1)
    moment = bulk([x*y for x, y in zip(k, row)])
    assert (sign * moment - 1 + row[0]/n + (1-opposite*row[0]/n)/r).contains(0)
    cost = bulk([r * (1+sign*x)/y for x,y in zip(k,row)])
    assert ((own / row[0] - 1)/t - c + cost).contains(0)
    print(json.dumps(dict(kind="physical-prime-13", sign=sign, floor="30/19",
                          signed_jacobi_moment=True, trial_cost_identity=True)))

b = arb(3) / 4
I = arb(2).sqrt() / arb.pi() * ((1+b).sqrt() + (1-b)/(2*b).sqrt()
                                 * (2*b/(1-b)).sqrt().asinh())
cold = 1 - I*I/(1-b/2)
assert cold > arb(11166)/100000 and cold < arb(11167)/100000
fixed = (2 - 8/arb.pi()**2).log()
assert fixed > arb(173)/1000 and fixed < arb(174)/1000
assert 1 - 2*arb(2).sqrt()/arb.pi() > arb(99)/1000
print(json.dumps(dict(kind="analytic-constants", cold_loss_interval=["0.11166","0.11167"],
                      t1_mark_bound_interval=["0.173","0.174"], cold_model_slack_gt="0.099")))
