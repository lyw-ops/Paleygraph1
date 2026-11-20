# Independent exact check of Report 1 identities (audit 181). stdlib only.
import random, sys
from fractions import Fraction as F
def run(p, seed):
    rnd=random.Random(seed)
    Q={x*x%p for x in range(1,p)}
    g=[F(0)]*p
    for x in Q: g[x]=F(rnd.randint(0,6),6)
    g[1]=F(1)
    # mu on chart
    mu={}
    for Y in range(2,p):
        for Dd in range(2,p):
            if Y==Dd: continue
            r=(Y-Dd)*pow(1-Dd,-1,p)%p
            b=Dd*(1-Y)*pow(Y*(1-Dd),-1,p)%p
            if b not in Q: continue
            assert (r,b) not in mu, "not injective"
            assert r!=0
            mu[(r,b)]=g[Y]*g[Dd]
    M1=sum(mu.values())
    m=[F(0)]*p; n=[F(0)]*p
    for (r,b),v in mu.items(): m[r]+=v; n[b]+=v
    # Delta(a,c) = sum_j mu(j) mu(jh), jh=(a r, b + c r)
    Delta={}
    for (r,b),v in mu.items():
        if v==0: continue
        for (r2,b2),v2 in mu.items():
            if v2==0: continue
            a=r2*pow(r,-1,p)%p; c=(b2-b)*pow(r,-1,p)%p
            Delta[(a,c)]=Delta.get((a,c),0)+v*v2
    # C(1)=sum m^2, sum_a Delta(a,0)=sum n^2
    assert sum(v for (a,c),v in Delta.items() if a==1)==sum(x*x for x in m)
    assert sum(v for (a,c),v in Delta.items() if c==0)==sum(x*x for x in n)
    for a in range(2,p):
        assert sum(v for (aa,c),v in Delta.items() if aa==a)==sum(m[r]*m[a*r%p] for r in range(1,p))
    # kernel K(y,e)=sum_{j: j e = y} mu(j), j e = r e + b
    K=[[F(0)]*p for _ in range(p)]
    for (r,b),v in mu.items():
        for e in range(p): K[(r*e+b)%p][e]+=v
    for y in range(p): assert sum(K[y])==M1
    HS=sum(x*x for row in K for x in row)
    Smu2=sum(v*v for v in mu.values()); Sm2=sum(x*x for x in m)
    assert HS - M1*M1 == p*Smu2 - Sm2, "HS"
    G=sum(g)
    for t in range(1,p):
        h=[F(0)]+[g[t*pow(e,-1,p)%p] for e in range(1,p)]
        assert sum(h)==G
        Fh=[sum(K[s][e]*h[e] for e in range(p)) for s in range(p)]
        S=sum(x*x for x in Fh)
        hc=[x-G/p for x in h]
        Fhc=[sum(K[s][e]*hc[e] for e in range(p)) for s in range(p)]
        assert S == M1*M1*G*G/p + sum(x*x for x in Fhc), "split"
        # S = sum_h Delta(h) m_t(h) with m_t(h)=sum_e h(e) h(h^{-1} e), h^{-1}e=(e-c)/a
        tot=0
        for (a,c),v in Delta.items():
            ai=pow(a,-1,p)
            mt=sum(h[e]*h[(e-c)*ai%p] for e in range(p))
            tot+=v*mt
            if a!=1 and c!=0:
                mt2=sum(g[x]*g[a*t*x*pow(t-c*x,-1,p)%p] for x in range(1,p) if (t-c*x)%p)
                # boundary terms: e=c (h^{-1}e=0) contributes 0 since h(0)=0; x with t=cx -> e=c
                assert mt==mt2,(a,c,t)
        assert tot==S, "S=sum Delta m"
    return len(mu)
for p in (13,17,29):
    for sd in range(2): print(p, sd, run(p,sd))
print("ALL OK")
