"""Single-step operator rate of the seed-linear map x -> K(S x)/(2 sqrt t) in the
weighted dimension price pi_a(M) = r_M + a*z_M (r = convolution dim = pooled
mass, z = pooled zero multiplicity) on negative simples, using the Round 80 rule.
Per weight w (pooled entries, each counted 1/2):
  input  a(w) = |w| + a*[w==0]
  output summed over both line children: b(w) = phi(w+1)+phi(w-1),
  phi(g) = |g| + a*max(|g|-1,0)   (z' = sum_{g!=0}(|g|-1)/2, r' = sum|g|/2).
Constraint for a negative simple: sum_w n_w*(|w|-1) = 0 (pooled mass = pooled
first absolute moment).  Rate = (s/(4|sqrt t|)) * max ratio over admissible
distributions; extreme points of the LP use <= 2 weight values.
Exact Fractions for the ratio; rate factor s/(4 sqrt t) -> 0.177515 (limit)."""
from fractions import Fraction as F
def phi(g, a): return abs(g) + a * max(abs(g) - 1, 0)
def ain(w, a): return abs(w) + (a if w == 0 else 0)
def b(w, a): return phi(w + 1, a) + phi(w - 1, a)
def maxratio(a, W=60):
    best = F(b(1, a), ain(1, a))           # single weight |w|=1 satisfies constraint
    for k in range(2, W):                  # mix zeros (|w|-1=-1) with |w|=k (+k-1)
        n0, nk = F(k - 1), F(1)            # n0*(-1)+nk*(k-1)=0
        r = (n0 * b(0, a) + nk * b(k, a)) / (n0 * ain(0, a) + nk * ain(k, a))
        best = max(best, r)
    return best
fac = 0.1775150596  # s_p/(4 sqrt(a-2^-17)) in the limit s_p -> 2 sqrt 2
rows = []
for num in range(0, 41):
    a = F(num, 20)
    m = maxratio(a)
    rows.append((float(a), float(m), fac * float(m)))
for r in rows: print("a=%.2f  max ratio=%.5f  seed rate=%.5f" % r)
bestrow = min(rows, key=lambda r: r[2]); print("best:", bestrow)
