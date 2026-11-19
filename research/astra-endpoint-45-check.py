"""Certify indistinguishable critical rows on the actual cold orbit at p=101."""
import json
from pathlib import Path
import runpy

from flint import arb, arb_mat, ctx


def run(shifts):
    p, n, sigma = 101, 50, -1
    assert {pow(4, j, p) for j in range(n)} == {i*i % p for i in range(1, p)}
    signs = [pow(1-pow(4, j, p), n, p) for j in range(n)]
    signs = [-1 if z == p-1 else z for z in signs]
    m = 4
    assert all(signs[k] == sigma for k in range(1, m+1))
    cos = [(arb(2*k)/n).cos_pi() for k in range(n)]
    col = [sum(s*cos[i*j % n] for j, s in enumerate(signs))/n for i in range(n)]
    kernel = arb_mat([[col[(i-j) % n] for j in range(n)] for i in range(n)])
    v = [arb(0)]*n
    for _ in range(3):
        phi = [abs(z) for z in v]
        phi[0] = (4+v[0]**2).sqrt()
        v = list(kernel*arb_mat(n, 1, phi))
    support = [k for k in range(1, n//2+1) if signs[k] == sigma]
    coef = runpy.run_path(str(Path(__file__).with_name('astra-rooted-43-check.py')))['PAIR'][sigma]
    assert len(support) == len(coef)
    X = [1+sum(a*cos[i*k % n] for a, k in zip(coef, support))/10**12 for i in range(n)]
    assert min(z.lower() for z in X) > 0
    fejer = [1+sum(2*(1-arb(k)/(m+1))*cos[i*k % n] for k in range(1,m+1)) for i in range(n)]
    # Each translate is nonnegative exactly by its defining Fourier square.
    candidates = [[(fejer[(i-h) % n]+fejer[(i+h) % n])/2 for i in range(n)]
                  for h in range(n//2+1)]
    def tests(row):
        return [arb(1), row[0]-1,
                sum((z-1)*t for z,t in zip(row,v))/n,
                sum((z-1)*t for z,t in zip(row,X))/n]
    matrix = arb_mat([tests(candidates[h]) for h in shifts]).transpose()
    weights = list(matrix.solve(arb_mat([[1],[0],[0],[0]])))
    assert min(w.lower() for w in weights)>0
    z = [sum(w*candidates[h][i] for w,h in zip(weights,shifts)) for i in range(n)]
    assert min(t.lower() for t in z)>0
    for value in tests(z)[1:]:
        assert value.contains(0) and value.rad()<arb('1e-80')
    root = arb(n).sqrt()
    critical = (1+(1-arb(1)/n)/4).sqrt()
    eps = (X[0]-critical*root)/(X[0]-1)
    assert 0<eps<1
    base = [(1-eps)*x+eps for x in X]
    alt = [(1-eps)*x+eps*y for x,y in zip(X,z)]
    for row in (base,alt):
        assert (row[0]/root-critical).contains(0)
        assert all((w-sigma*(r-1)).contains(0)
                   for w,r in zip(list(kernel*arb_mat(n,1,row)),row))
    def energy(row):
        return sum((x-1)**2 for x in row)/n
    gap = energy(alt)-energy(base)
    assert gap>0 and (gap-eps**2*energy(z)).contains(0)
    scores = [sigma*sum(r*y for r,y in zip(row,v))/root for row in (base,alt)]
    assert (scores[0]-scores[1]).contains(0)
    print(json.dumps(dict(q=p, sign=sigma, floor='1/4', orbit_floor=0, t=3,
                          shifts=shifts, weights=[str(w) for w in weights],
                          precision=ctx.prec, mark=str(critical), diluted_fraction=str(eps),
                          cold_score=str(scores[0]), uniform_matched_energy_excess=str(energy(z)),
                          critical_collision_gap=str(gap)), sort_keys=True))


if __name__ == '__main__':
    ctx.prec = 384
    run([3, 4, 23, 24])
