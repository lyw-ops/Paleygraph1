"""Finite modular replay of the argument pins, plus the exact exponent margin."""

from collections import Counter
from fractions import Fraction
from itertools import combinations

epsilon = Fraction(1, 1280)
delta = Fraction(1, 640)
margin = Fraction(1, 52) - (12 + Fraction(5, 52))*epsilon - (6 + Fraction(9, 104))*delta
assert margin == Fraction(9, 33280)

for p in (13, 17, 29, 41):
    squares = {x*x % p for x in range(1, p)}

    def divide(a, b):
        return a * pow(b % p, -1, p) % p

    pairs = Counter()
    parameters = Counter()
    tuples = 0
    for u in squares - {1}:
        for A in squares - {1}:
            C = (1-u+u*A) % p
            if C not in squares - {1}:
                continue
            for Y in squares - {1,A}:
                D = (1-u+u*Y) % p
                if D not in squares - {1}:
                    continue
                s = divide(D*A, C*Y)
                assert s != 1
                r = divide(Y-D, 1-D)
                b = divide(D*(1-Y), Y*(1-D))
                assert C == divide(A-r, 1-r)
                assert divide(1,Y) == (divide(b,D)+1-b) % p
                for (i,label_i),(j,label_j) in combinations(enumerate((A,C,Y,D)), 2):
                    pairs[s,i,j,label_i,label_j] += 1
                for j,label in enumerate((A,C,Y,D)):
                    parameters[s,0,b,j,label] += 1
                    parameters[s,1,r,j,label] += 1
                tuples += 1
    assert max(pairs.values(), default=0) <= 2
    assert max(parameters.values(), default=0) <= 1
    print(f'p={p}: {tuples} tuples, maximum two-label pin {max(pairs.values(), default=0)}')
