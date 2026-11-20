"""Exact modular replay of the full diagonal before its asymptotic estimates."""

from collections import Counter

for p in (13, 17, 29, 41):
    squares = {i * i % p for i in range(1, p)}
    weights = {i: 1 + (i*i + 11*i + 3) % 11 for i in squares}

    def g(value):
        return weights.get(value % p, 0)

    def divide(a, b):
        return a * pow(b % p, -1, p) % p

    raw = Counter()
    for u in squares - {1}:
        for x in range(1, p):
            A, C = (1-2*x) % p, (1-2*u*x) % p
            if not g(A) or not g(C):
                continue
            for y in range(1, p):
                Y, D = (1-2*y) % p, (1-2*u*y) % p
                if not g(Y) or not g(D):
                    continue
                s = divide(D*A, C*Y)
                if s != 1:
                    raw[s] += g(A)*g(C)*g(Y)*g(D)

    chart = Counter()
    lines = set()
    checked = 0
    for Y in squares - {1}:
        for D in squares - {1, Y}:
            r = divide(Y-D, 1-D)
            b = divide(D*(1-Y), Y*(1-D))
            u = divide(1-D, 1-Y)
            assert (b in squares) == (u in squares)
            if b not in squares:
                continue
            inverse_line = (divide(-r,b), divide(1,b))
            assert inverse_line not in lines
            lines.add(inverse_line)
            for s in range(2, p):
                if s == b:
                    continue
                X = divide(1, s)
                e = divide(1-b*X, r)
                assert X == sum((inverse_line[0]*e, inverse_line[1])) % p
                A = divide(1, e)
                C = divide(A*D*X, Y)
                assert C == (1-u+u*A) % p
                assert (D**2+((1-s)*C*Y-C-Y)*D+s*C*Y) % p == 0
                if A != 1:
                    chart[s] += g(A)*g(C)*g(Y)*g(D)
                checked += 1
    assert raw == chart, p
    print(p, len(lines), checked)
