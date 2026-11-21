# Independent exact check of Report 2 row-pair identity (audit 181).
import random
from fractions import Fraction as F
def run(p,seed):
    rnd=random.Random(seed)
    Q={x*x%p for x in range(1,p)}
    g=[F(0)]*p
    for x in Q: g[x]=F(rnd.randint(0,5),5)
    g[1]=F(1)
    w=[g[x]*(1-g[x]) for x in range(p)]
    w2=[F(rnd.randint(0,9),7) if x in Q else F(0) for x in range(p)]  # arbitrary weight too
    QQ=Q-{1}
    def chart(wt):
        M=0; cnt=0
        for s in QQ:
            for r in range(2,p):
                for b in QQ:
                    if s==b: continue
                    A=r*s*pow(s-b,-1,p)%p; C=r*b*pow((1-r)*(s-b),-1,p)%p
                    Y=r*pow(1-b,-1,p)%p; Dd=r*b*pow((1-r)*(1-b),-1,p)%p
                    if not {A,C,Y,Dd}<=QQ: continue
                    cnt+=1
                    # also check cross-ratio chart of Round 180
                    X=pow(s,-1,p); pi=pow(b,-1,p); rho=(1-r)*pow(b,-1,p)%p
                    assert pow(A,-1,p)==(X-pi)*pow(rho-pi,-1,p)%p
                    assert pow(Y,-1,p)==(1-pi)*pow(rho-pi,-1,p)%p
                    assert pow(C,-1,p)==(X-pi)*rho*pow(X*(rho-pi),-1,p)%p
                    assert pow(Dd,-1,p)==(1-pi)*rho*pow(rho-pi,-1,p)%p
                    M+=wt[s]*g[A]*g[C]*g[Y]*g[Dd]
        return M,cnt
    def rows(wt):
        M=0; cnt=0
        for k in QQ:
            R=[(Y,Dd) for Dd in QQ for Y in QQ if (1-Y-k*(1-Dd))%p==0]
            for (Y,Dd) in R:
                for (A,C) in R:
                    s=A*Dd*pow(C*Y,-1,p)%p
                    if s==1: continue
                    cnt+=1
                    M+=g[Y]*g[Dd]*g[A]*g[C]*wt[s]
        return M,cnt
    for wt in (w,w2):
        a,ca=chart(wt); b,cb=rows(wt)
        assert a==b and ca==cb,(p,a,b,ca,cb)
    # E_Q bound and h form
    h=lambda z: g[(1-z)%p] if z%p else F(0)
    EQ=sum(sum(h(z)*h(k*z) for z in range(1,p))**2 for k in QQ)
    Mw,_=chart(w)
    assert Mw<=EQ/4
    Gam=sum(x*x for x in g); W=sum(w)
    assert Mw<=W*Gam*Gam
    return ca
for p in (13,17,29,37,41):
    print(p, run(p,1))
print("OK")
