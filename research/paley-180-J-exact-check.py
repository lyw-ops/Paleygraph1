"""Exact modular checks of the projective normal form (Round 180 candidate)."""
from itertools import product
def inv(a,p): return pow(a%p,-1,p)
def check(p):
    Q={x*x%p for x in range(1,p)}
    # 1. interior <=> six distinct points, labels as cross-ratios
    n_int=0
    for r,b,s in product(range(p),repeat=3):
        if b not in Q or s==0 or b==0: continue
        if r in (0,1) or s==b or b==1 or s==1: 
            continue
        A=r*s*inv(s-b,p)%p; C=r*b*inv((1-r)*(s-b),p)%p
        Y=r*inv(1-b,p)%p; D=r*b*inv((1-r)*(1-b),p)%p
        X=inv(s,p); pi=inv(b,p); rho=(1-r)*inv(b,p)%p
        interior = all(l not in (0,1) for l in (A,C,Y,D))
        distinct = len({0,1,X,pi,rho})==5
        assert interior==distinct,(p,r,b,s)
        if not distinct: continue
        n_int+=1
        assert inv(A,p)==(X-pi)*inv(rho-pi,p)%p
        assert inv(Y,p)==(1-pi)*inv(rho-pi,p)%p
        assert inv(C,p)==rho*(X-pi)*inv(X*(rho-pi),p)%p
        assert inv(D,p)==rho*(1-pi)*inv(rho-pi,p)%p
        assert rho==Y*inv(D,p)%p
    # 2. pairs at a common s: J from Round 179 definition
    npairs=0; cnt={'J0':0,'J1':0,'gen':0}
    for s in Q-{1}:
        rows=[]
        for r,b in product(range(2,p),Q-{1}):
            if s==b: continue
            A=r*s*inv(s-b,p)%p; C=r*b*inv((1-r)*(s-b),p)%p
            Y=r*inv(1-b,p)%p; D=r*b*inv((1-r)*(1-b),p)%p
            if not {A,C,Y,D}<=Q-{1}: continue
            rows.append((inv(A,p),inv(Y,p),inv(C,p),inv(b,p),(1-r)*inv(b,p)%p))
        for (v,x,u,pi,rho),(v2,x2,u2,pi2,rho2) in product(rows,repeat=2):
            k=(x2-v2)*inv(x-v,p)%p; d=(v2-k*v)%p
            J=d*(k+d-1)*inv(k,p)%p
            den=(rho-pi)*(rho2-pi2)%p
            assert den!=0
            assert J==(pi-pi2)*(rho-rho2)*inv(den,p)%p
            assert (J==0)==(pi==pi2 or rho==rho2)
            assert (J==1)==(pi2==rho or rho2==pi)
            cnt['J0' if J==0 else 'J1' if J==1 else 'gen']+=1
            npairs+=1
    return n_int,npairs,cnt
for p in (13,17,29,37,41):
    print(p,check(p))
