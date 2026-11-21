import random
def inv(a,p):
    a%=p; assert a, "div0"; return pow(a,p-2,p)
def labels(r,b,s,p):
    A=r*s*inv(s-b,p)%p; C=r*b*inv((1-r)*(s-b),p)%p
    Y=r*inv(1-b,p)%p; D=r*b*inv((1-r)*(1-b),p)%p
    return A,C,Y,D
def cr(z,a,b,c,p):  # [z;a,b,c], c finite
    return (z-a)*(b-c)%p*inv((z-c)*(b-a),p)%p
def interior(r,b,s,p):
    if r in (0,1) or b in (0,1) or s in (0,1) or s==b: return False
    return all(L not in (0,1) for L in labels(r,b,s,p))
stats={}
for p in (13,17,29,101):
    cnt=[0,0,0]
    trip=[(r,b,s) for r in range(p) for b in range(p) for s in range(p) if interior(r,b,s,p)] if p<40 else None
    random.seed(1)
    def pairs():
        if p<40:
            byS={}
            for (r,b,s) in trip: byS.setdefault(s,[]).append((r,b))
            for s,L in byS.items():
                for e in L:
                    for e2 in L: yield s,e,e2
        else:
            for _ in range(200000):
                s=random.randrange(2,p); r,b,r2,b2=[random.randrange(2,p) for _ in range(4)]
                if interior(r,b,s,p) and interior(r2,b2,s,p): yield s,(r,b),(r2,b2)
    for s,(r,b),(r2,b2) in pairs():
        A,C,Y,D=labels(r,b,s,p); A2,C2,Y2,D2=labels(r2,b2,s,p)
        v,x,u=inv(A,p),inv(Y,p),inv(C,p); v2,x2,u2=inv(A2,p),inv(Y2,p),inv(C2,p)
        k=(x2-v2)*inv(x-v,p)%p; d=(v2-k*v)%p
        J=d*(k+d-1)%p*inv(k,p)%p
        pi,rho=inv(b,p),(1-r)*inv(b,p)%p; pi2,rho2=inv(b2,p),(1-r2)*inv(b2,p)%p
        X=inv(s,p)
        # Lemma 1
        assert inv(A,p)==(X-pi)*inv(rho-pi,p)%p and inv(Y,p)==(1-pi)*inv(rho-pi,p)%p
        assert inv(C,p)==cr(X,pi,rho,0,p) and inv(D,p)==cr(1,pi,rho,0,p) and rho==Y*inv(D,p)%p
        # Round 179 companion: u2 = v2 + (lam/k)(u - v)
        f0=lambda t: t*(1-t)%p
        lam=f0(v2)*inv(f0(v),p)%p
        assert u2==(v2+lam*inv(k,p)*(u-v))%p
        # cross ratio
        Jcr=(pi-pi2)*(rho-rho2)%p*inv((rho-pi)*(rho2-pi2),p)%p
        assert J==Jcr
        assert (J==0)==(pi2==pi or rho2==rho)
        assert (J==1)==(pi2==rho or rho2==pi)
        cnt[0 if J==0 else 1 if J==1 else 2]+=1
        if J not in (0,1):
            # normal form
            z0,z1,zX=[cr(t,pi,rho,rho2,p) for t in (0,1,X)]
            zinf=(rho-rho2)*inv(rho-pi,p)%p
            assert cr(pi2,pi,rho,rho2,p)==J
            zs=[z0,z1,zX,zinf]
            assert len(set(zs))==4 and not (set(zs)&{0,1,J})
            c=lambda z,a,bb,cc: cr(z,a,bb,cc,p)
            assert inv(A,p)==c(zX,0,1,zinf) and inv(Y,p)==c(z1,0,1,zinf)
            assert inv(C,p)==c(zX,0,1,z0) and inv(D,p)==c(z1,0,1,z0)
            assert inv(A2,p)==(zX-J)*inv(zX-zinf,p)%p and inv(Y2,p)==(z1-J)*inv(z1-zinf,p)%p
            assert inv(C2,p)==(zX-J)*inv(zX-z0,p)%p and inv(D2,p)==(z1-J)*inv(z1-z0,p)%p
            assert X==c(zX,z0,z1,zinf) and pi==c(0,z0,z1,zinf) and rho==c(1,z0,z1,zinf) and pi2==c(J,z0,z1,zinf)
    # rows: fixed pi, 1/D' = pi z + 1 - pi ; fixed rho, 1/A' = c z + 1-c
    print(p,"pairs J0/J1/gen",cnt)
# Lemma 8 exhaustive at p=29,37 over all lines (pi,rho), all J generic
for p in (29,37):
    worst=0
    for pi in range(2,p):
        for rho in range(1,p):
            if rho==pi: continue
            for J in range(2,p):
                cnt={}
                for u in range(p):
                    for t in range(p):
                        if u==t: continue
                        if ((pi-u)*(rho-t)-J*(rho-pi)*(t-u))%p: continue
                        if u==1 and t!=1: pass
                        if t==u: continue
                        y=(1-u)*inv(t-u,p)%p
                        cnt[y]=cnt.get(y,0)+1
                if cnt: worst=max(worst,max(cnt.values()))
    print("Lemma8 p",p,"max multiplicity",worst)
