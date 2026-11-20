"""Exact integer replay of the Round 80 line-shift/transport weight rule on the
leading seed fields H_j (all 2^j leaves inequivalent, equal |coefficients|).
Computes E r_j (uniform over leaves) exactly and the ratios E r_{j+1}/E r_j,
which give the exact Fourier-algebra (collected Deligne) rate of the
seed-linear operator x -> K(S x)/(2 sqrt t) on the leading fields:
   A(H_{j+1})/A(H_j) * (1/(2 sqrt t)) = (s_p/(2 sqrt t)) * E r_{j+1}/E r_j.
Also checks the Round 80 worst-path table for the first steps.
Plain stdlib; exact Fractions."""
from collections import Counter
from fractions import Fraction
import sys

def transport(G1, G2):
    tot = sum(abs(w) for w in G1) + sum(abs(w) for w in G2)
    assert tot % 2 == 0
    r = tot // 2
    N1 = [w for w in G1 if w < 0] + [w for w in G2 if w > 0]
    N2 = [w for w in G2 if w < 0] + [w for w in G1 if w > 0]
    assert len(N1) <= r and len(N2) <= r, (G1, G2)
    N1 += [0] * (r - len(N1)); N2 += [0] * (r - len(N2))
    return (tuple(sorted(N1)), tuple(sorted(N2))), r

def child(state, s):
    F1, F2 = state
    return transport([w + s[0] for w in F1], [w + s[1] for w in F2])

SH = [(-1, 1), (1, -1)]
start, r1 = transport([-2], [2])          # transported J^2 leaf
assert start == ((-2, 2), (0, 0)) and r1 == 2
# worst path check: shifts (+1,-1),(+1,-1),(-1,+1),(-1,+1),...
st = start; seq = [(1, -1), (1, -1), (-1, 1), (-1, 1)]
for j in range(1, 41):
    st, r = child(st, seq[(j - 1) % 4])
    assert r == j + 2, (j, r)
print("worst path r_j=j+2 verified through j=40")

maxdepth = int(sys.argv[1]) if len(sys.argv) > 1 else 22
dist = Counter({start: 1}); weight = 1
prevE = Fraction(2)
print("j  distinct_states  E[r_j]  ratio E r_j/E r_{j-1}  (zero frac z/r avg)")
for j in range(2, maxdepth + 1):
    nd = Counter()
    for stt, c in dist.items():
        for s in SH:
            ns, _ = child(stt, s)
            nd[ns] += c
    dist = nd; weight *= 2
    Er = Fraction(sum(c * len(s[0]) for s, c in dist.items()), weight)
    zf = Fraction(sum(c * Fraction(s[0].count(0) + s[1].count(0), 2 * len(s[0])) for s, c in dist.items()), weight)
    print(j, len(dist), float(Er), float(Er / prevE), float(zf))
    prevE = Er
