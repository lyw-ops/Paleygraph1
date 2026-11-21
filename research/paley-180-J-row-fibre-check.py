"""Exact checks for the J-pricing lemmas (Round 180 candidate), pure Python.
(1) fixed pi row: 1/D = pi*(1/Y) + (1-pi); fixed rho row: 1/A = c*(1/Y) + (1-c), c=(X-rho)/(1-rho).
(2) J-1 = (pi-rho2)(rho-pi2)/den; J = d(k+d-1)/k with d=h(0), k+d=h(1).
(3) for J not in {0,1}: each value of 1/Y' meets the J-fibre over e in at most 2 lines e'.
"""
import sys
from itertools import product
def inv(a,p): return pow(a%p,-1,p)
for p in map(int,sys.argv[1:]):
    F=range(p); nrow=0; nfib=0; maxmult=0
    for pi,rho,X in product(F,repeat=3):
        if len({0,1,X,pi,rho})<5: continue
        Yi=(1-pi)*inv(rho-pi,p)%p; Di=rho*(1-pi)*inv(rho-pi,p)%p; Ai=(X-pi)*inv(rho-pi,p)%p
        assert Di==(pi*Yi+1-pi)%p
        c=(X-rho)*inv(1-rho,p)%p
        assert c not in (0,1) and Ai==(c*Yi+1-c)%p
        nrow+=1
    for pi,rho in product(F,repeat=2):
        if len({0,1,pi,rho})<4 or (pi*rho)%7: continue   # subsample first lines
        fib={}
        for pi2,rho2 in product(F,repeat=2):
            if len({0,1,pi2,rho2})<4: continue
            den=(rho-pi)*(rho2-pi2)%p
            J=(pi-pi2)*(rho-rho2)*inv(den,p)%p
            assert (J-1)%p==(pi-rho2)*(rho-pi2)*inv(den,p)%p
            jj=lambda z:(z-pi2)*inv(rho2-pi2,p)%p      # j_{e'}; h=j_{e'} o j_e^{-1}
            d=jj(pi); k=(rho-pi)*inv(rho2-pi2,p)%p
            assert (k+d)%p==jj(rho) and J==d*(k+d-1)*inv(k,p)%p
            if J in (0,1): continue
            y=(1-pi2)*inv(rho2-pi2,p)%p
            fib[(J,y)]=fib.get((J,y),0)+1; nfib+=1
        maxmult=max([maxmult]+list(fib.values()))
    assert maxmult<=2
    print(p,'row identities on',nrow,'triples; generic fibre pairs',nfib,'max multiplicity of 1/Y\' per (e,J):',maxmult)
