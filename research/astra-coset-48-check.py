"""Exact prime sweep and interval check for the five-coset sign pattern."""
import json
from math import isqrt

from flint import arb, ctx


def emit(**row):
    print(json.dumps(row, sort_keys=True))


def sieve(limit):
    prime = bytearray([1]) * (limit + 1)
    prime[:2] = b'\x00\x00'
    for i in range(2, isqrt(limit) + 1):
        if prime[i]:
            prime[i*i::i] = bytes((limit - i*i) // i + 1)
    return prime


def primitive_root(p):
    rem = p - 1
    factors = []
    for d in range(2, isqrt(rem) + 1):
        if rem % d == 0:
            factors.append(d)
            while rem % d == 0:
                rem //= d
    if rem > 1:
        factors.append(rem)
    return next(g for g in range(2, p) if all(pow(g, (p-1)//d, p) != 1 for d in factors))


def chi(x, p):
    r = pow(x % p, (p-1)//2, p)
    return -1 if r == p-1 else r


def fiber_stats(p, b, a, B, sigma):
    cosets = [[x*pow(a, j, p) % p for x in B] for j in range(5)]
    assert len(set().union(*map(set, cosets))) == 5*b
    first = [sum(chi(1-x, p) for x in fiber) for fiber in cosets]
    assert first[:2] == [sigma*(b-1), sigma*b] and first[4] == sigma*b
    tnum = sigma*first[2]
    assert first[2] == first[3]
    if b % 2:
        neg = [sum(chi(1+x, p) for x in fiber) for fiber in cosets]
        assert neg == [b-1+chi(2,p), tnum, tnum, tnum, tnum]
        if b % 3 == 0:
            # Twice the real cubic character on C; kernel C^3.
            cubic = lambda x: 2 if pow(x, 5*b//3, p) == 1 else -1
            for fiber in cosets[2:4]:
                assert sum(cubic(x)*sigma*chi(1-x,p) for x in fiber) == b-tnum
            assert sum(cubic(x)*chi(1-x,p) for fiber in cosets for x in fiber) == 2*sigma*(b-tnum-1)
            assert sum(cubic(x)*chi(1+x,p) for fiber in cosets for x in fiber) == 4*(b-tnum)+2*(chi(2,p)-1)
        if b % 9 == 0:
            assert 9*tnum >= b
    elif b > 2:
        assert sigma == 1
        squares = {x*x % p for fiber in cosets for x in fiber}
        assert len(squares) == 5*b//2 and all(chi(1-x, p) == 1 for x in squares if x != 1)
        assert len(squares)*(len(squares)-1) <= (p-1)//2
    return tnum


def scan(limit):
    prime = sieve(limit)
    eligible = tests = critical = 0
    counts = {"odd": 0, "even": 0}
    maximum = {"odd": None, "even": None}
    examples = {}
    hits = 0
    for p in range(41, limit+1, 20):
        if not prime[p]:
            continue
        eligible += 1
        n5 = (p-1)//10
        g = primitive_root(p)
        # 2b is already a clique. Larger divisors cannot be feasible.
        for b in range(2, (1+isqrt(1+4*((p-1)//2)))//4+1):
            if n5 % b:
                continue
            h = pow(g, (p-1)//b, p)
            B = [1, h]
            sigma = chi(1-h, p)
            for _ in range(2,b):
                B.append(B[-1]*h % p)
                if chi(1-B[-1],p) != sigma:
                    break
            for j in (1,2):
                tests += 1
                critical += 10*b*b > p-1
            if len(B) < b or chi(1-B[-1], p) != sigma:
                continue
            base = pow(g, (p-1)//(5*b), p)
            for j in (1,2):
                a = pow(base, j, p)
                if any(chi(1-a*x, p) != sigma for x in B):
                    continue
                t = fiber_stats(p,b,a,B,sigma)
                hits += 10*b*b > p-1
                parity = 'odd' if b % 2 else 'even'
                counts[parity] += 1
                rec = (p,b,j,sigma,t)
                old = maximum[parity]
                if old is None or b*b*(old[0]-1) > old[1]**2*(p-1):
                    maximum[parity] = rec
                if b > examples.get(parity, (0,0))[1]:
                    examples[parity] = rec
    emit(kind='exhaustive_integer_scan', limit=limit, eligible_primes=eligible,
         divisor_and_inverse_pair_choices=tests, critical_choices=critical,
         patterns=counts, critical_patterns=hits,
         largest_normalized_ratio_examples=maximum, largest_b_examples=examples,
         tuple_format=['p','b','generator_power','sigma','b_times_t'])


ctx.prec = 192
k = (3+arb(5).sqrt())/2
C = 10*k/(6+k)
ratio = arb(2).sqrt()/C
assert arb('0.465') < ratio < arb('0.466')
emit(kind='arb192', spectral_constant=str(C), odd_ratio_ceiling=str(ratio),
     cubic_ratio_ceiling=str(3*arb(2).sqrt()/10), boundary_t_lower=str(1-arb(10).sqrt()/k), boundary_t_upper=str((arb(10).sqrt()-4)/6))
scan(200000)
