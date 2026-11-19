# Cooling with the full Jacobi seed

For the actual marked logarithm, through eligible primes and prime squares,
\[
 \sup_{197/8\le t\le25}|m_q(t)|=O(n^{-1/21000}),\qquad
 \sup_{25\le t\le28}|m_q(t)|=O(n^{-1/2100}).
\]
Together with the [hot theorem](seed-majorant-47.md), the real decay range starts at \(197/8=24.625\). A different positive predictor consisting of four finite polynomial updates gives
\[
 \limsup_{p\to\infty}\sup_{11\le t\le25}|m_p(t)|<0.0154,\qquad
 \limsup_{q\to\infty}\sup_{12\le t\le25}|m_q(t)|<0.0146.
\]
The second bound includes prime squares. A sharper square-root transfer certifies the earlier positive tolerance \(0.017\) throughout \([10,25]\) through primes and \([11,25]\) through primes and squares. The cold stencil at \(t=1/2\) and the ordinary prime theta limit remain open.

## Combining Laurent modes before charging rank

Use \(S=2\sqrt n K e_0\), \(s=2\sqrt{q/n}\), and \(H_t(v)=\sqrt{4t+v^2}\). The exact Jacobi bound gives \(|S_i|\le s\), including the exceptional characters. Let \(T_k(\cos\theta)=\cos(k\theta)\). Write the absolutely convergent expansion
\[
 H_t(s\cos\theta+y)=\sum_{j,k\ge0}c_{jk} T_k(\cos\theta)y^j.             \tag{1}
\]
When \(s+|y|<2\sqrt t\), expand first in the even Taylor powers of \(s\cos\theta+y\), then expand each power of cosine into cosines of integer multiples. Thus \(j+k\) is even, and the signed contributions to a given \((j,k)\) combine *before* taking absolute values. This is the difference from grading the raw powers of the seed by their multiplicity.

For a product of \(j\) negative fields of ranks \(r_i\), the exact rank cost of applying \(K\) to that product times \(T_k(S/s)\) is at most
\[
 (k+j)\prod r_i+
 O\!\left( (k+\textstyle\sum r_i)\prod r_i/\sqrt n\right),             \tag{2}
\]
for \(k+j>0\). The constant term is killed exactly. To see (2), use the [two Jacobi lifts and negative-field calculus](seed-majorant-47.md). On their original good characters \(S/s\) equals the half-sum of a rank-one invertible trace and its inverse up to the common sign. By the Chebyshev identity, \(T_k(S/s)\) there is the half-sum of the two inverse \(k\)-th powers up to the sign raised to \(k\). For \(k=0\) use the tensor unit. Expand the other lift averages. A summand before the quadratic twist contains \(k+j\) negative factors, the \(k\) copies of the seed having rank one. The generic rank bound gives the first term. On the bad full characters test the *original* seed and inputs, before cancellation. There are \(O(k+\sum r_i)\) bad characters. Both the original expression and the proposed lifted expression have magnitude at most \(\prod r_i\) there, by \(|T_k(S/s)|\le1\) and convolution dimension. The exact translated correcting columns give the second term. For \(j=0\) the empty product is one. All constants in (2) are uniform in the indices as in the even-product rank bound.

## A power rate for the new hot range

Use the auxiliary formal series
\[
 R(z)=K\sum_{j,k\ge0}c_{jk}z^{k+1}T_k(S/s)R(z)^j,\qquad R(0)=0.
                                                                    \tag{3}
\]
Every degree is determined by previous degrees. A term of degree \(d=1+k+\sum d_i\) has rank at most \(2^{d-1}\): the main term in (2) is at most \((k+j)2^{\sum d_i-j}\le2^{d-1}\), and each correction column has rank one. Through \(D=\lfloor(\log_2 n)/3\rfloor\), the relative error factor in (2) is \(1+o(1)\), uniformly over the contributing indices, since \((k+\sum r_i)/(k+j)\le 2^D\). Coefficients may have many terms, but this comparison applies before summing their absolute costs.

The [scalar checker](astra-warm-51-check.py) proves, uniformly on each indicated closed interval and for all sufficiently large \(n\),
\[
 \sum_{j,k}(k+j)|c_{jk}|\rho^{k+1}b^j<C<b .
                                                                    \tag{4}
\]

| Interval | \(b\) | \(\rho\) | \(C\) |
|---|---:|---:|---:|
| \([197/8,25]\) | 1.74 | 1.0001 | 1.7399 |
| \([25,28]\) | 1.77 | 1.001 | 1.766 |

The calculation groups all Taylor powers through 28, using the exact binomial coefficient of each Laurent mode and Arb at 160 bits. For the remaining even powers \(2l\), the rank and radius charge is at most \(2\sqrt t\,\rho(2l)r^l\), \(r=(s\rho+b)^2/(4t)\). Indeed \(k\) is at most the original number of seed factors and the absolute coefficients of each power of cosine sum to one. Summing this tail bounds the contribution for all discarded degrees, including contributions to the same low Laurent modes. The checker encloses \(s\) in an interval with \(2\sqrt2\) in its interior and covers the full floor intervals by closed rational subdivisions.

Iterate the scalar coefficient majorant of (3) from zero. By (4) its weighted sum at \(\rho\) stays below \(b\) even with the relative exceptional factor through degree \(D\). Coefficients stabilize degree by degree, giving \(\sum_{d\le D}\rho^d\|R_d\|_\infty\le b\). Let \(R_{[D]}(z)\) be its actual vector truncation (coefficients of (3)), and set \(V=S+R_{[D]}(1)\). Form \(U\) by substituting this polynomial on the right of (3) *before* applying \(K\), truncating to degree \(D\) and evaluating at 1. Exactly \(KU=V-S\). The full substituted series has weighted sum of coefficient sup norms bounded by \(\sum |c_{jk}|\rho^{k+1} b^j=O(1)\), using (4) and the bounded constant term. At 1 it equals \(H_t(V)\) by (1), so
\[
 \|U-H_t(V)\|_\infty=O(\rho^{-D}),\qquad \|V\|_\infty<4.6.
\]

Set \(u_0=2\), \(u_i=U_i/\sqrt n\) otherwise, \(v=Ku\). Then \(\sqrt n\,v=V-U_0Ke_0\) at every site. Since \(H_t(V)\ge2\sqrt{197/8}>9\) and every entry of the correcting column is \(O(n^{-1/2})\), both \(A_\pm=(u\pm v)/2\) are strictly positive entrywise for all sufficiently large fields. They have equal means, lie in the complementary Fourier sectors and are the stationary factors for their product weights \(w'\). At the mark \(w'_0=1+O(1/n)\) and their log ratio divided by two is \(O(n^{-1/2})\). On the bulk \(nw'_i=t+O(\rho^{-D}+n^{-1/2})\). Normalize weights by \(w'_0\) and apply [square-root weight stability](marked-response.md#weighted-complementary-projections) to compare to the actual constant bulk weights. This proves the two power rates since \(1.0001^{21000}>8\) and \(1.001^{2100}>8\).

## A positive four-step predictor at lower floors

Let \(H^{[14]}\) denote the Taylor polynomial of \(H_t\) through degree 28 at zero. Start \(V_0=S\), and iterate \(V_i=S+K H^{[14]}(V_{i-1})\) four times. This is a finite vector calculation using only the Jacobi seed. With \(b_0=0\), recursively bound the limiting rank costs of \(V_i-S\) by
\[
 b_i=\sum_{j,k}(j+k)|c^{[14]}_{jk}|b_{i-1}^j,\qquad B_i=s+b_i .
\]
Here the coefficients are for the finite polynomial. At fixed depth and degree the exceptional costs in (2) are \(o(1)\), uniformly on each compact interval of floors. Thus \(\|V_i\|_\infty\le B_i+o(1)\). The checker uses upper endpoints for each scalar \(B_i\). We omit the vanishing errors in the following limiting estimates.

Write \(\|\cdot\|_{2,n}^2=n^{-1}\sum_i|\cdot|^2\). For \(i\le3\) let \(e_i=2\sqrt t\,r_i^{15}/(1-r_i)\) with \(r_i=B_i^2/(4t)<1\), bounding the activation's truncation error on \([-B_i,B_i]\). For \(d_i=\|V_i-V_{i-1}\|_{2,n}\),
\[
 d_1\le\frac{\operatorname{sd}(S^2)}{4\sqrt t}+e_0,\qquad
 d_i\le\frac{B_{i-1}}{\sqrt{4t+B_{i-1}^2}}d_{i-1}+e_{i-1}+e_{i-2}
 \quad(2\le i\le4).
\]
For the first bound, \(K\) kills the mean and is an \(L^2\) contraction, and \(x\mapsto\sqrt{4t+x}\) on nonnegative reals is \(1/(4\sqrt t)\)-Lipschitz, hence contracts standard deviation by this factor. The second uses the Lipschitz constant of \(H_t\) on the stated interval; the rank radii increase from \(b_0=0\). Universally \(\operatorname{sd}(S^2)\le s^2/2\) by the range bound. For primes \(S\) has limiting law \(2\sqrt2\cos\theta\) and is uniformly bounded, so \(\operatorname{Var}(S^2)\to8\). The checker uses the eventual bound \(8.001\). [Prime Jacobi law](fourier.md)

Now use the same positive-factor construction with \(U=H^{[14]}(V_3)\) and \(V=V_4\). The corrected marked entry is again \(O(n^{-1/2})\) in \(v\). The interval check proves the strictly positive lower bound on the bulk product and the normalized RMS defect
\[
 L=\tfrac14[(2\sqrt t-e_3)^2-B_4^2]>0,\qquad
 \|nw'-t\|_{2,b}\le
 J=\tfrac14[(B_3+B_4)d_4+(2\sqrt{4t+B_3^2}+e_3)e_3]+o(1).
\]
Here \(\|\cdot\|_{2,b}^2=n^{-1}\sum_{i\ne0}|\cdot|^2\). In this display the minimum includes a vanishing correction: \(nw'_i\ge L-o(1)\) on the bulk. The calculations have \(2\sqrt t-e_3>0\), so both sector factors are entrywise positive. Dividing by \(w'_0=1+O(1/n)\) has vanishing cost. The square-root weight comparison then gives \(|m_q(t)|\le J/(\sqrt t+\sqrt L)+o(1)\). This uses the actual marked weight and the RMS defect only *after* pointwise positivity is proved. The checker covers the entire intervals with slabs of width \(1/8\), yielding the strict positive-tolerance bounds above. No cold solve, optimized row, or field-specific tangent radius is used.

### A sharper square-root comparison

The Taylor remainder on the positive real argument \(r_i\le1\) is at most \(e_i=2\sqrt t\,|\binom{1/2}{15}|r_i^{15}\) by alternating signs. To measure square-root weight error directly, put \(c=2\sqrt t\). For \(u\ge0\) and \(0\le v<c\), the function
\[
 f(u,v)=\frac{u+v}{\sqrt{c^2+u^2-v^2}+c}
\]
is increasing in both variables. For the \(u\)-derivative multiply the numerator by the positive \(d=\sqrt{c^2+u^2-v^2}\); the sign reduces to that of \(c^2-v^2+cd-uv>0\), since \(d\ge u\) and \(c>v\). The \(v\)-derivative is positive directly. Subtract the ideal square root \(\sqrt{4t+V_3^2-V_4^2}/2\) from the trial bulk square root first. Its distance from \(\sqrt t\) is at most \(\tfrac12 f(B_3,B_4)|V_3-V_4|\). The truncation error in the preceding subtraction, in the scaled bulk, is bounded by the second term below. Thus the normalized square-root weight distance is at most
\[
 D_*=\tfrac12 f(B_3,B_4)d_4+
 \frac{(2\sqrt{4t+B_3^2}+e_3)e_3}
 {4(\sqrt L+\sqrt{t-B_4^2/4})}+o(1),
\]
where the checker verifies \(B_4<2\sqrt t-e_3\) on each slab. The mark is normalized to one before comparing the weights, with an \(o(1)\) adjustment.

Finally, in the exact weighted differential identity \(\nu\dot\gamma=(\Pi_+-\Pi_-)\dot\nu\), \(\nu_i=\sqrt{w_i}\), the image is orthogonal to \(\nu\), and the signed projection is contractive. Evaluating at the fixed mark of weight one projects \(e_0\) to \(\nu^\perp\) at cost \(\sqrt{1-1/W}\). Along the straight segment in bulk square roots, their Euclidean norm is at most \(\sqrt t+D_*+o(1)\). Consequently the actual marked log difference is bounded by
\[
 D_*\frac{\sqrt t+D_*}{\sqrt{1+(\sqrt t+D_*)^2}}+o(1).
\]
Subdividing the intervals as before gives strict upper bounds below \(0.017\) through primes on \([10,25]\) and through both field families on \([11,25]\). The two sharper rows use the same four polynomial updates.

Run the checker with the project virtual environment to reproduce the [six scalar records](astra-warm-51-checks.jsonl).

1. Separate the explicitly known first feedback \(K H_t(S)\) together with the seed in the Laurent rank bound. A rank-cost ball with strict slack below \(197/8\) and radius-controlled activation would extend genuine marked decay. A certified minimum of the proposed majorant minus its radius above zero rules out that particular ball construction.
2. At lower target floors, refine the RMS difference by retaining the covariance of adjacent polynomial Picard outputs. A positive factor pair with \(J/(\sqrt t+\sqrt L)<0.017\) at \(t=1/2\) would certify the prime stencil's cold-node tolerance. A nonpositive entry on unbounded primes or a definite excess in that comparison rejects the specified predictor or its certified bound.
