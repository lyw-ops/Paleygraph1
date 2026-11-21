"""Exact check of the normalized four-point form of a generic J class."""
import random
def inv(a,p): return pow(a%p,-1,p)
def CR(z,a,b,c,p):  # image of z under a->0,b->1,c->inf ; all finite
    return (z-a)*(b-c)*inv((z-c)*(b-a),p)%p
def CRinf(z,a,b,p): # c = infinity
    return (z-a)*inv(b-a,p)%p
for p in (101,409,1009):
    random.seed(p); n=0
    while n<3000:
        pi,rho,pi2,rho2,X=(random.randrange(2,p) for _ in range(5))
        if len({0,1,X,pi,rho})<5 or len({0,1,X,pi2,rho2})<5 or len({pi,rho,pi2,rho2})<4: continue
        J=(pi-pi2)*(rho-rho2)*inv((rho-pi)*(rho2-pi2),p)%p
        gam=lambda z:(z-pi)*(rho-rho2)*inv((z-rho2)*(rho-pi),p)%p
        z0,z1,zX=gam(0),gam(1),gam(X); zinf=(rho-rho2)*inv(rho-pi,p)%p
        assert gam(pi2)==J and J not in (0,1)
        for (a,b) in ((pi,rho),): pass
        # first copy labels
        assert CRinf(X,pi,rho,p)==CR(zX,0,1,zinf,p)       # 1/A
        assert CRinf(1,pi,rho,p)==CR(z1,0,1,zinf,p)       # 1/Y
        assert CR(X,pi,rho,0,p)==CR(zX,0,1,z0,p)          # 1/C
        assert CR(1,pi,rho,0,p)==CR(z1,0,1,z0,p)          # 1/D
        # second copy: [z;J,inf,c]=(z-J)/(z-c)
        assert CRinf(X,pi2,rho2,p)==(zX-J)*inv(zX-zinf,p)%p
        assert CRinf(1,pi2,rho2,p)==(z1-J)*inv(z1-zinf,p)%p
        assert CR(X,pi2,rho2,0,p)==(zX-J)*inv(zX-z0,p)%p
        assert CR(1,pi2,rho2,0,p)==(z1-J)*inv(z1-z0,p)%p
        # output and masks
        assert X==CR(zX,z0,z1,zinf,p)
        assert pi==CR(0,z0,z1,zinf,p) and pi2==CR(J,z0,z1,zinf,p)
        n+=1
    print(p,'ok',n)
