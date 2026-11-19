"""Exact norm-one square-field checks for the cell-square identity in Round 24."""
from collections import Counter
import json
from pathlib import Path


def check(ell):
    q = ell*ell
    nr = next(x for x in range(2,ell) if pow(x,(ell-1)//2,ell) != 1)
    def sub(x,y):
        return (x%ell-y%ell)%ell+ell*((x//ell-y//ell)%ell)
    def mul(x,y):
        a,b,c,d = x%ell,x//ell,y%ell,y//ell
        return (a*c+nr*b*d)%ell+ell*((a*d+b*c)%ell)
    def norm(x):
        return ((x%ell)**2-nr*(x//ell)**2)%ell
    def power(x,n):
        y = 1
        while n:
            if n&1:
                y = mul(y,x)
            x,n = mul(x,x),n//2
        return y
    def inv(x):
        return power(x,q-2)
    def chi(x):
        return 0 if x == 0 else (1 if pow(norm(x),(ell-1)//2,ell)==1 else -1)
    B = {x for x in range(1,q) if norm(x)==1}
    b = len(B)
    d = {x: 1 if power(x,b//2)==1 else -1 for x in B}
    assert b == ell+1
    S = sum(d[x]*chi(sub(1,x)) for x in B-{1})
    Y = {sub(1,x) for x in B-{1}}
    R = Counter(mul(x,inv(y)) for y in Y for x in Y if x != y)
    V = sum(not R[u] for u in range(1,q) if chi(u)==-1)
    cosets = {}
    for x in range(1,q):
        if x not in cosets:
            cosets.update({mul(x,y):(x,d[y]) for y in B})
    cells = {}
    for alpha in range(1,q):
        beta = sub(1,alpha)
        if chi(alpha)*chi(beta) == -1:
            ca,da = cosets[alpha]
            cb,db = cosets[beta]
            N,L = cells.get((ca,cb),(0,0))
            cells[ca,cb] = N+1,L+da*db
    total = sum(L*L for N,L in cells.values())
    assert total == (q-S*S)//2 == 0
    assert V == sum(N==1 for N,L in cells.values()) == 0
    assert all(N==2 and L==0 for N,L in cells.values())
    return dict(ell=ell,order=q,b=b,twist_sum=S,vacancies=V,
                sum_squared_cell_labels=total,nonsquare_nonempty_cells=len(cells))

rows = [check(ell) for ell in [7,11,13,31]]
Path(__file__).with_name('parallel-vacancy-24-square-certified.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
