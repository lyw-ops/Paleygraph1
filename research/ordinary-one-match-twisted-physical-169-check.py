"""Exact modular check of the twisted physical slope coordinates on small primes."""

from collections import defaultdict

tested = 0
for p in (5, 13, 17, 29, 41):
    square = {x*x % p for x in range(1, p)}
    g = {x: (x*x+7*x+11) % 17 + 1 for x in square}
    weight = lambda x: g.get(x%p, 0)
    div = lambda a, b: a*pow(b, -1, p)%p
    raw = defaultdict(int)
    dil = defaultdict(int)
    for u in square - {1}:
        for x in range(1,p):
            A = (1-2*x)%p
            C = (1-2*u*x)%p
            if not A or not C:
                continue
            for y in range(1,p):
                Y = (1-2*y)%p
                D = (1-2*u*y)%p
                if not Y or not D:
                    continue
                s = div(D*A,C*Y)
                if s == 1:
                    continue
                for t in range(1,p):
                    s1=div(t,s)
                    raw[s,t,0] += weight(s1*A)*weight(C)*weight(Y)*weight(D)
                    raw[s,t,1] += weight(A)*weight(C)*weight(Y)*weight(s1*D)
                    s2=div(s,t)
                    raw[s,t,2] += weight(A)*weight(s2*C)*weight(Y)*weight(D)
                    raw[s,t,3] += weight(A)*weight(C)*weight(s2*Y)*weight(D)
    for s in range(2,p):
        for z in sorted(square - {1}):
            if s*z%p == 1:
                continue
            dilation=div(1-z,1-s*z)
            for Y in range(2,p):
                den=(1+dilation*div(1-Y,Y))%p
                if not den:
                    continue
                D=div(1,den)
                u=div(1-D,1-Y)
                if Y in square and D in square:
                    assert (u in square) == (dilation in square)
                if dilation not in square or s*z*Y%p == 1:
                    continue
                for t in range(1,p):
                    dil[s,t] += weight(t*z*Y)*weight(z*D)*weight(Y)*weight(D)
    for s in range(2,p):
        for t in range(1,p):
            assert raw[s,t,0] == dil[s,t] == raw[s,t,1], (p,s,t)
            assert raw[s,t,0] == raw[div(1,s),div(1,t),2] == raw[div(1,s),div(1,t),3], (p,s,t)
            tested += 1
print(f'Exact integer replay on {tested} slope pairs across the five named primes.')
