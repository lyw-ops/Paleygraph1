# Report 1 exact checks (pure python)
import random, itertools, sys
def inv(a,p): return pow(a,p-2,p)
for p in (13,17,29,37):
    F=range(p); NZ=[x for x in F if x not in (0,1)]
    random.seed(p)
    g={x:random.randint(0,3) for x in F}
    # chart masses with mask b in Q
    Q={x*x%p for x in range(1,p)}
    m=[0]*p; msh=[0]*p
    for Y in NZ:
        for D in NZ:
            if Y==D: continue
            r=(Y-D)*inv(1-D,p)%p
            b=D*(1-Y)*inv(Y*(1-D)%p,p)%p
            assert r not in (0,1) and b not in (0,1)
            msh[r]+=g[Y]*g[D]
            if b in Q: m[r]+=g[Y]*g[D]
    bad=0
    for lam in range(2,p):
        # line injectivity
        lines=set()
        for D1 in NZ:
            for D3 in NZ:
                # line (1-D3)(X-D1)=lam(1-D1)(Z-D3): store as set of points
                pts=frozenset((X,Z) for X in F for Z in F if ((1-D3)*(X-D1)-lam*(1-D1)*(Z-D3))%p==0)
                lines.add(pts)
                # nonvertical/nonhorizontal: one point per X and per Z
                assert len({x for x,_ in pts})==p and len({z for _,z in pts})==p
        assert len(lines)==len(NZ)**2
        # Omega tuples and determination
        Om=[(Y1,D1,Y3,D3) for Y1 in NZ for D1 in NZ for Y3 in NZ for D3 in NZ
            if Y1!=D1 and Y3!=D3 and ((Y1-D1)*(1-D3)-lam*(Y3-D3)*(1-D1))%p==0]
        for pos in range(4):
            keys={}
            for t in Om:
                k=t[:pos]+t[pos+1:]
                keys[k]=keys.get(k,0)+1
            if max(keys.values())>1: bad+=1
        Csh=sum(g[a]*g[b]*g[c]*g[d] for a,b,c,d in Om)
        C=sum(msh[r]*msh[lam*r%p] for r in range(p))
        assert Csh==C, (p,lam)
        # r1 = lam r3 direction check
    # energy identity sum_lam C^2 = sum_xi W^2 (masked m)
    E1=sum(sum(m[r]*m[l*r%p] for r in range(1,p))**2 for l in range(1,p))
    E2=sum(sum(m[r]*m[xi*inv(r,p)%p] for r in range(1,p))**2 for xi in range(1,p))
    assert E1==E2
    print(p,"ok, determination failures:",bad, "maxm<=G:",max(m)<=sum(g[x] for x in F)*3)
