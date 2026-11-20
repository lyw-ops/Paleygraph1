from collections import defaultdict

count = 0
for p in (5, 13, 17, 29, 37):
    divide = lambda a, b: a*pow(b, -1, p)%p
    squares = {k*k%p for k in range(1,p)}
    weights = {k: 1+(k*k+11*k+3)%11 for k in squares}
    g = lambda k: weights.get(k%p,0)
    raw = defaultdict(int)
    chart = defaultdict(int)
    for u in squares-{1}:
        for x in range(1,p):
            A,C=(1-2*x)%p,(1-2*u*x)%p
            if not A or not g(C):
                continue
            for y in range(1,p):
                Y,D=(1-2*y)%p,(1-2*u*y)%p
                if not g(Y) or not g(D):
                    continue
                s=divide(D*A,C*Y)
                if s!=1:
                    for t in squares:
                        raw[s,t]+=g(Y)*g(D)*g(C)*g(t*divide(A,s))
    maps=set()
    for Y in squares-{1}:
        for D in squares-{1,Y}:
            r=divide(Y-D,1-D)
            b=divide(D*(1-Y),Y*(1-D))
            assert (r,b) not in maps
            maps.add((r,b))
            assert divide(b*r,(1-r)*(1-b))==D
            assert (b in squares)==(divide(1-D,1-Y) in squares)
            if b not in squares:
                continue
            for e in range(1,p):
                s=(b+r*e)%p
                if s in (0,1):
                    continue
                E=divide(1,e)
                A=s*E%p
                if A==1:
                    continue
                C=divide(E*D,Y)
                u=divide(1-D,1-Y)
                assert C==(1-u+u*A)%p
                assert (D*D+((1-s)*C*Y-C-Y)*D+s*C*Y)%p==0
                for t in squares:
                    chart[s,t]+=g(Y)*g(D)*g(C)*g(t*E)
    for s in range(2,p):
        for t in squares:
            assert raw[s,t]==chart[s,t], (p,s,t)
            count+=1
print(f'Exact modular comparison passed for {count} slope and twist pairs.')
