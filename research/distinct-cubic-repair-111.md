# A signed distinct-triple Jacobi test on the genuine core

The core of an actual late negative repair can only stay near its signed Jacobi eigenspace if an average of **distinct-triple** cubic correlations survives at the full square-root arithmetic scale. Collision configurations are smaller. This gives a finite, more specific arithmetic observable than a generic compressed norm.

Use the hypotheses and the moving-threshold core of [the actual defect balance](repair-core-defect-balance-110.md) for fixed \(t,M\) and a fixed prime subsequence. In particular \(0<\beta<1/10\), \(\eta=n^{-\beta}\), \(\bar h=u+r\) with \(u=1_C\bar h\ge0\) the genuine core row, and \(r=1_{C^c}\bar h\). The available estimates are
\[
 \mathbb E_n u\asymp n^{-1/2},\quad
 \|u\|_{2,n}^2\asymp n^{-1/2},\quad
 \|u\|_\infty=O(1),\quad
 \|r\|_{2,n}=O(n^{-1/4-\beta/2}).
\]
Also \(\|K\bar h-\epsilon\bar h\|_{2,n}=O(n^{-1/2})\). The actual \(K\) contracts in normalized second norm, so
\[
 \|Ku-\epsilon u\|_{2,n}=O(n^{-1/4-\beta/2}),\qquad
 \|Ku\|_\infty\le\sqrt p\,\mathbb E_n u=O(1).
\]
The cubic difference therefore obeys
\[
 \left|\mathbb E_n(Ku)^3-\epsilon\,\mathbb E_n u^3\right|
  \ll\|Ku-\epsilon u\|_{2,n}
       \big(\|Ku\|_{2,n}+\|u\|_{2,n}\big)
  =O(n^{-1/2-\beta/2}).
\]
For the inequality expand the difference of cubes, take Cauchy–Schwarz and use the two uniform supremum bounds. Since \(u\ge0\),
\((\mathbb E_n u^2)^2\le(\mathbb E_n u^3)(\mathbb E_n u)\). Thus \(\epsilon\,\mathbb E_n(Ku)^3\gtrsim n^{-1/2}\) for large primes on the obstruction subsequence. This test concerns the third moment. Removing the exterior at this relative precision does not remove it at the sharper local balance scale of the preceding round.

## Expanding the correct Jacobi kernel

On the multiplicative frequency group \(G=\widehat Q\), write \(K_{x,y}=\lambda_{x-y}/n\), \(k(d)=\lambda_d/\sqrt p\), and
\[
 \pi_y=\frac{u_y}{\sum_z u_z},\qquad
 T(a,b,c)=\mathbb E_{x\in G} k(x-a)\,k(x-b)\,k(x-c).
\]
Then \(\max\pi=O(n^{-1/2})\) and \(\sum\pi^2=O(n^{-1/2})\). For these genuine weights,
\[
 \mathbb E_n(Ku)^3
   =(\sqrt p\,\mathbb E_n u)^3
        \sum_{a,b,c}\pi_a\pi_b\pi_c\,T(a,b,c).
\]
The prefactor is comparable to one.

We use the same quantitative Gauss-angle moment estimate and two-lift Jacobi formula as in [Three-point Jacobi caps](parallel-arithmetic-2.md). In detail, \(k(x-y)\) is the real part of a normalized Gauss quotient with one pair of quadratic-twisted characters, except on the bounded exceptional Mellin indices where its modulus is still at most one. Distinct \(y\)'s supply disjoint pairs of full-field character twists. After expansion into monomials and collection of exponents, if a shift occurs an odd number of times its exponent in its pair cannot vanish. Hence each monomial with multiplicities \((2,1)\) or \((1,1,1)\) has a nonzero Gauss exponent vector on a distinct list. The total degrees are bounded, so its mean is \(O(p^{-1/2})\) by [Katz, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf), with \(O(p^{-1})\) cost for the exceptional indices. The products of real parts descend, so the average over full-field characters gives the desired average on \(G\).

The mass of triples with exactly two equal indices is \(O(n^{-1/2})\) by \(\sum\pi^2\). Their contribution is \(O(n^{-1})\) by the just-mentioned translated estimate. The all-equal mass is at most \(\max\pi\sum\pi^2=O(n^{-1})\), which also bounds its contribution by the entry bound. Consequently the actual necessary signed inequality is
\[
 \boxed{\qquad
   \epsilon\!\!\sum_{\substack{a,b,c\in C\\a,b,c\ {\rm distinct}}}
                  \pi_a\pi_b\pi_c\,T(a,b,c)\ \gtrsim\ p^{-1/2}.
       \qquad}                                                    \tag{1}
\]
Here \(C\) and \(\pi\) arise from the true capped factor and the actual projected repairs, and the sign is the matching persistent marked sign. The uniform individual Gauss bound is only \(O(p^{-1/2})\). Cancellation to \(o(p^{-1/2})\) for this actual average would exclude the obstruction under the critical cap-rate premise. It is not supplied by the generic moment estimate.

The [static square-coset example](api-astra-review-110.md) illustrates the critical rate: for \(u=1_C\) on a subfield-annihilator coset, \(Ku=u-\rho\mathbf1\), \(\rho=|C|/n\asymp n^{-1/2}\). Then \(\mathbb E_n(Ku)^3=\rho(1-\rho)(1-2\rho)\asymp n^{-1/2}\), and the same collision bookkeeping holds. This applies to a prescribed square-field vector, without providing a genuine prime repair obstruction.

1. Seek a signed averaged bound on the noncollision kernel for the genuine \(\pi\), potentially after regrouping by translation differences. Any improvement on a single translated moment must be justified uniformly for the required shifts.
2. Maintain the true marked pairing and late repair history if the cubic kernel is estimated only on structurally restricted probability weights. A generic arbitrary-weight estimate is insufficient at its known square-root error.
