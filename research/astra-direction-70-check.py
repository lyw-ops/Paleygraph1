"""Rational marked inverse-moment replay at p=13, n=6, larger minus face."""
from fractions import Fraction as F

n = 6
I = {0, 3}


def mean_zero(v):
    mean = sum(v) / n
    return [z - mean for z in v]


def split_projections(v):
    # P_plus has symbol 1 at +1,-1, giving 2 cos(pi*(i-j)/3)/6.
    a = [v[i] if i in I else 0 for i in range(n)]
    b = [v[i] - a[i] for i in range(n)]
    kernel = [2, 1, -1, -2, -1, 1]

    def plus(z):
        return [sum(F(kernel[(i-j) % n], n) * z[j] for j in range(n))
                for i in range(n)]

    pa, pb = plus(a), plus(b)
    return pa, [u - w for u, w in zip(mean_zero(b), pb)]


def compress(v):
    a, b = split_projections(mean_zero(v))
    return mean_zero([a[i] if i in I else b[i] for i in range(n)])


basis = [[F(i == j) for i in range(n)] for j in range(n)]
g = mean_zero(basis[0])
matrix = [list(row) + [rhs] for row, rhs in zip(zip(*map(compress, basis)), g)]
pivots = []
for col in range(n):
    pos = len(pivots)
    candidates = [i for i in range(pos, n) if matrix[i][col]]
    if not candidates:
        continue
    row = candidates[0]
    matrix[pos], matrix[row] = matrix[row], matrix[pos]
    scale = matrix[pos][col]
    matrix[pos] = [z / scale for z in matrix[pos]]
    for i in range(n):
        if i != pos:
            scale = matrix[i][col]
            matrix[i] = [z - scale * y for z, y in zip(matrix[i], matrix[pos])]
    pivots.append(col)

v = [F(0)] * n
for i, j in enumerate(pivots):
    v[j] = matrix[i][-1]
assert compress(v) == g
moment = sum(z * y for z, y in zip(v, g))
# x=(3,0,0,3,0,0); q=1+cos(pi*i/3); q_0=2.
assert moment <= F(15, 4)
print(f"p=13 rank={len(pivots)} marked_inverse_moment={moment} certificate=15/4")
