# A common marked rectangle across the rank-three escape floor

For sufficiently large eligible primes and prime squares, the actual marked stationary section is holomorphic and obeys \(|m_q(t)|\le 3/\sqrt n\), \(n=(q-1)/2\), on
\[
  1040052/65536 < \Re t < 1040130/65536,\qquad
  |\Im t|<1/65536.
\]
The previous section starts at \(1040128/65536\). The new rectangle contains \(16251/1024=1040064/65536\), where the earlier fully collected rank-three map escaped. The new three-seed map, even after *full* arithmetic collection at each root, has a quantitative escape at \(2031/128\) and separately at \(1015/64\). Neither floor is an asserted singularity of the actual branch. The common cold-domain question and the prime theta limit remain open. [Rank-three section and barrier](astra-rankthree-56.md)

## Third distinguished subtraction

Use the rank-three notation, where the old distinguished fields are \(Y,W\), the scaled seed is \(S=s C_1\), and \(s^2=8+4/n\). Denote the rank-four field by \(F\). With \(c_{rk}\) the degree-28 cosine/Taylor coefficients and \(d_{rk,uv}\) their Legendre coefficients after translation by \(\alpha Y\) and before subtraction, put
\[
 \alpha=c_{02}+c_{22}c_{02}^2/2-7/10^5,\qquad
 \beta=2d_{01,10}-6/10^5,\qquad
 \gamma=(499/500)\,\beta d_{11,00}.
\]
These are fixed holomorphic prescriptions at the actual field scale. The exact scaled input is \(S+\alpha Y+\beta W+\gamma F+Z\). In residual arity zero subtract \(\alpha C_2+\beta C_1Y+\gamma C_1W\) before applying \(K\). The first two aliases are those of round 55. The third one is
\[
  K(C_1W)=F-\frac{n(1+q+h_q)}{2q^2}K e_0,\qquad |h_q|\le2q .
\]
The coefficient multiplying \(Ke_0\) is bounded and its first-packet cost vanishes as \(O(n^{-1/2})\). In the source with arity zero, \(W\)-degree one, cosine mode one and trivial Legendre label, the amended coefficient is exactly \(\beta d_{11,00}/500\). This evaluation avoids interval subtraction at a cancellation. [All-lift rank-four identity](rank-four-arithmetic-56.md#the-next-distinguished-complex-feedback)

At either twist the averaged eight standard and dual characters of \(F\) have measure
\[
 D_F=\tfrac74\delta_0+\tfrac12(\delta_{1}+\delta_{-1}+\delta_{2}+\delta_{-2})
                         +\tfrac18(\delta_{4}+\delta_{-4}).
\]
Every rank-four irreducible has a unique derived label consisting of four dominant partitions with last entry zero. Separately keep an integer Jacobi exponent. For a standard or dual factor add or subtract one from a row, discard non-dominant results, subtract the new last entry from **all four** rows, and add that entry times the factor's determinant exponent \((2,-2,0,0)_i\) to the Jacobi exponent. This is the rational \(GL_4\) Pieri rule. The exponents are valid for the actual arithmetic objects by round 56, including the positive coordinate translation. Combine these labels with the old \(SL_2^2\), \(SL_3^2\) labels, using a single shared Jacobi exponent. Independence of their derived factors and surjectivity to the Jacobi torus give uniqueness.

At twist one the four weight lists in factor order are \((-2,-2,1,1),(0,0,0,2),(0,0,0,0),(-2,-1,-1,4)\), and \(m^e\) shifts weights by \(-e\). The quadratic twist swaps the first two lists and the last two, and shifts by \(+e\). Restricting a partition successively under \(GL_k\to GL_{k-1}\) uses interlacing lower rows. The difference of row sums multiplies the weight of the removed coordinate. Exact integer checks of the resulting dimensions and full weight measures at both twists give \((8D_F)^{*h}\) through \(h=4\). The scalar multiplicities in \((8F)^2\) and \((8F)^4\) are
\[
 h=2:\quad 8\cdot1,\qquad
 h=4:\quad 2m^{-2}+196\cdot1+2m^2 .
\]
In degree four the 192 balanced terms count twelve for each of four individual factors and twenty-four for each of six pairs. The other eight are the actual determinant contractions. The degree-two Pieri table also pools both exterior squares for each factor with their actual determinant shifts. [Rank-four arithmetic factors](rank-four-arithmetic-56.md)

## An upper bound with all omitted terms charged

First form the signed rank-three coefficients of round 56 at arity \(r\) in \(Z+\gamma F\), with the above amendments at \(r=0\). Collect its prefix with \(r\le6\), \(W\)-degree \(l\le4\), total Legendre degree at most three and source Jacobi exponent of magnitude at most seven. The other degree-28 sources are charged positively by their actual full boundary measures after Legendre collection. From the prefix set aside every coefficient \(s_{r,e}\) with trivial old derived labels and \(|e|\le3\). For all other labels charge the modulus times the corresponding weight measure. This produces an unsigned remainder \(P_r\) and the signed \(s_{r,e}\). Its two twist costs agree after summing the simultaneous twist symmetry of the old pairs and the two exponent signs, as in round 56.

For final arity \(j\) and \(h=r-j\), multiply by \(\binom rj\gamma^h\) and tensor with \(F^h\). Charge \(P_r\) convolved with \(D_F^{*h}\) positively. On the extracted sector sum all the degree-zero and degree-two irreducibles and the three degree-four scalar lines, by the common rank-four label and **total** Jacobi exponent, before taking moduli. At \(h=4\) the complementary measure is \(D_F^{*4}-(2\delta_{-2}+196\delta_0+2\delta_2)/4096\). Charge it against each \(|s_{r,e}|\) with the correct shift. All other \(h\) in the extracted sector are charged with \(D_F^{*h}\). These disjoint sets cover the entire Taylor polynomial. The full lower-floor map studied below collects more coincidences and is bounded above by this method.

The 50 rational packet caps in the checker use the frozen zero atom \(\sum(k-1)h_k+\epsilon/\eta+10^{-8}\), with \(\eta=1/5\), \(\epsilon=6\cdot10^{-7}\). The remaining nonzero atoms have hyperbolic cosine norm at most \(\epsilon\). The ordinary degree-28 binomial tail uses the previous total input norm plus the actual contribution
\[
 |\gamma|\big(7/4+\cosh\eta+\cosh(2\eta)+\cosh(4\eta)/4\big)
\]
from \(F\). The core is convolved exactly and the mixed excess uses the first derivative of the positive scalar series at the norm cap. [Frozen-zero argument](astra-signed-54.md#freezing-the-zero-weight)

The envelope on 78 closed complex slabs has off-zero output excess below \(4\cdot10^{-7}\) and full coordinate bound below \(4.68\), certified at Arb192 with \(s\) enclosed in \(\sqrt8\pm10^{-12}\). The uniform analytic tail before any signed collections also bounds the sum of dimensions in the exceptional-lift debit. Strict slack absorbs these \(O(n^{-1/2})\) errors, the exact distinguished aliases and the actual mark-column correction. Starting with \(Z=0\), the exact iterates stay in the invariant. Since \(4.68/\sqrt{4(1040052/65536)-4.68^2}<3/4\), their successive differences contract in the complex Euclidean norm. The mark derivative has the larger denominator \(\sqrt{4n-4.68^2}\). The locally uniform limit has positive stationary factors on the real interval, hence agrees on the overlap with the actual physical section by uniqueness and analytic continuation. The bound on the scaled mark gives the stated bound on its inverse hyperbolic sine. [Actual branch identification](marked-domain-53.md#from-scalar-slack-to-the-actual-holomorphic-section)

## A quantitative limitation after full arithmetic pooling

Take the limiting real scale with the same three seed prescriptions. Define the full map by collecting the *infinite* analytic series by residual arity and arithmetic irreducible, including its Jacobi exponent, before taking coefficient moduli. Between activations use the usual unsigned pooled measure of the residual, independently convolved for its powers, and the usual packet projection.

For degree at most 28 generate lower and upper old kernels \(L_r,U_r\), now with no extracted scalar sector. For \(r\le11\) sum all source Jacobi modes and the indicated \(W\)-degree \(l\le4\), Legendre degree \(u+v\le4\). The reverse triangle inequality debits the complementary higher-\(l\) and higher-Legendre terms at each boundary weight. Take the positive part of the retained kernel minus that measure for \(L_r\). Their sum bounds from above for \(U_r\). For larger \(r\) set \(L_r=0\) and use the full precollection cost for \(U_r\).

Within the quadratic rank-four power retain every nontrivial derived label that occurs with only *one* Jacobi shift in that power, with its full multiplicity. Write \(Q_2\) for their normalized weight measure. The degrees zero and one have distinct derived sectors, disjoint from \(Q_2\). Indeed on each \(SL_4\) the central element \(-I\) detects parity, and the nontrivial two-box representations and cross-factor products cannot be a single standard or dual. A degree-two scalar can cancel the degree-zero term, so debit its entire cost. The nonconstant quadratic labels with multiple shifts can be omitted altogether since their derived labels are disjoint. Every term of degree \(h\ge3\) is debited by its full upper measure. Thus a pointwise lower kernel at arity \(j\le9\), through Taylor degree 28, is
\[
 L_j+(j+1)|\gamma|L_{j+1}*D_F+
 {j+2\choose j}|\gamma|^2\big(L_{j+2}*Q_2-U_{j+2}/8\big)
 -\sum_{h=3}^{28-j}{j+h\choose j}|\gamma|^h U_{j+h}*D_F^{*h}.
\]
For the \(Q_2\) lower term the unique shift is essential: tensoring a fixed old arithmetic label produces no overlap with a different old label at that shift. All displayed products are boundary-measure convolutions.

At each weight subtract the ordinary binomial tail at input dimension \(s+2|\alpha|+3|\beta|+4|\gamma|+R\) divided by \(R^j\), optimizing over the same finite positive radii as in round 56. Full arithmetic decomposition preserves the dimension used in this Cauchy debit. Retain the positive parts, shifts through 18 and output packets through 28. At \(2031/128\) the zero-start lower iteration exceeds mass 21 at height 1130. At \(1015/64\) it does so at height 334. In each case the zero shift at arity two exceeds \(1/20\). For a full post-projection measure of mass \(b\), the normalized weight has mean zero and expected absolute value one. Conditional Jensen gives the next full mass at least \(b^2/20\). Thus neither floor admits a finite-mass zero-start majorant in this fully collected map. The argument concerns the specified coefficients at these two floors and proves no monotonicity in \(t\).

From the repository root the reproducible check is

    .venv/bin/python -B research/astra-rankfour-57-check.py

The [checker](astra-rankfour-57-check.py) and [four records](astra-rankfour-57-checks.jsonl) use exact integers and Arb192. The optional [cap search](astra-rankfour-57-probe.py) with integer arguments 1040052 and 1040130 is floating-point guidance only.

## Ranked next tests

1. Keep the dominant arity-one term through a second activation by retaining the signed sources of \(K[C_1 Kf]\) for the leading arity-zero \(f\), beginning with the remaining pure mode \(C_4\) and the Legendre pair. Compute the coincident arithmetic labels after the inner \(K\), carrying their exceptional columns. Require an overlapping upper rectangle reaching below \(2031/128\) with all other terms paid. An escaping lower map for the same explicitly grouped two-activation operator at that floor rejects that prescription.
2. Test other real offsets for the three coefficients against the same complete arithmetic map. Upper success requires a strict overlapping invariant below \(2031/128\). A uniform lower escape throughout a specified offset box at that floor rules out that entire box. The two lower records above concern only the displayed coefficients.
