"""Exact prime-mask sieve for periodic caps with prime quotient order."""

import json
import sys
from collections import Counter
from math import isqrt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from theta import paley_sign, prime_divisors


def check(limit):
    counts = Counter()
    examples = {}
    for p in range(5, limit + 1, 4):
        if any(p % divisor == 0 for divisor in range(3, isqrt(p) + 1, 2)):
            continue
        n = (p - 1) // 2
        quotients = sorted(b for b in prime_divisors(n) if b < n and b * b >= 4 * n)
        if not quotients:
            continue
        sign = paley_sign(p)
        for b in quotients:
            period = n // b
            fibers = sign.reshape(b, period)
            for side in (1, -1):
                forbidden = (fibers == -side).sum(axis=0)
                central = int(forbidden[0])
                exterior = int(forbidden[1:].min())
                outcome = 'excluded' if exterior <= central else 'survives'
                counts[outcome] += 1
                key = f'{outcome}_sign_{side}'
                if key not in examples:
                    examples[key] = dict(p=p, b=b, sign=side, central=central,
                                         minimum_exterior=exterior)
    return dict(limit=limit, criterion='b prime proper divisor of n with b^2 >= 4n',
                counts=dict(counts), first_examples=examples)


if __name__ == '__main__':
    print(json.dumps(check(20000), sort_keys=True))
