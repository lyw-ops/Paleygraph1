# Exact Fourier slope fibers for the single rank-two trace

Use the single clean rank-two lift of [Round 159](ordinary-single-lift-ratio-law-159.md). Let \(m=p-1\), and use the full multiplicative character group \(\mathcal X\) of order \(m\). Write \(G\) for the unnormalized trace
\[
 G(\beta,C,\alpha,\delta)=J(\alpha\beta C,(\beta C)^{-1})
       \sum_{z,y}\beta(z)(\alpha\bar\delta\chi)(z+1)
                       C(y)\delta(y+1)\chi(z-y).
\]
This displayed formula is the uncut kernel, with the trivial character zero at zero. In the actual weighted expectation the nine clean restrictions and outer resonances may be imposed or removed at cost \(O(p)\). An exact Fourier support formula below is for the uncut trace, with the indicated physical zeros removed.

## Correct four-ratio coordinates

Use the natural variables \((\beta,C,\alpha,\delta)\) with the true law \(P\) of Round 159. Its plus transform, evaluated at \((a,b,c,d)\in(\mathbb F_p^\times)^4\), is
\[
 \widehat P(a,b,c,d)
       = f(a) f(c/a) f(b^{-1}) f(d) f\bigl(b/(cd)\bigr).
\]
Here \(f\) is extended by zero off \(Q\). Indeed the plus character monomial \(\beta(a)C(b)\alpha(c)\delta(d)\) evaluates \(V,U,V',T,U'\) at the five indicated arguments, respectively. In particular the product form in relative coordinates from Round 159 cannot be copied with unchanged indices into the natural ratio coordinates.

Opening the Jacobi sum in \(u\) and the two-variable kernel gives the same monomial with
\[
 a=\frac{uz}{1-u},\quad b=\frac{uy}{1-u},\quad
 c=u(z+1)=a+(1-a)u,\quad
 d=\frac{y+1}{z+1},\quad cd=b+(1-b)u .
\]
The residual coefficient is \(\chi(z+1)\chi(z-y)=\chi(1-d)\). Thus its sign is at the slope \(d\). The natural variables \(a=1\) or \(b=1\) correspond to one zero physical coordinate in the original expansion. Their actual weighted cost is \(O(p)\), by the signed zero-coordinate comparison in Round 156 for square \(u\), and the nonsquare estimate in Round 159. Remove those two classes and call the resulting uncut trace \(G^\circ\). For \(d\ne1\) one always has \(a\ne b\). The equation of its Fourier graph is
\[
 (1-a)(cd-1)=(1-b)(c-1).
\]
For \(a,b\ne0,1\), \(a\ne b\) and \(d\ne0,1\), set
\[
       u=\frac{b-da}{b-1+d(1-a)},\qquad
       c=\frac{b-a}{b-1+d(1-a)}.
\]
The graph retains the nonzero denominator and \(u\ne0\); \(u=1\) is impossible since \(d\ne1\). The resulting \(c\) is nonzero, and the inverse parameterization is unique. The Fourier transform of \(G^\circ\) with the minus convention has unnormalized coefficient \(m^4\chi(1-d)\) on this graph and is zero elsewhere.

## Disjoint slope fibers and conditional centering

For each \(d\ne0,1\) the allowed set of \((a,b,c)\) is denoted \(V_d\). For fixed \(a\ne0,1\) the excluded \(b\)'s are \(0,1,a,da,1-d+da\). The only repetitions are \(da=1\) at \(a=d^{-1}\) and \(1-d+da=0\) at \(a=1-d^{-1}\), each saving one even if both occur at the same \(a\). Hence \(|V_d|=(p-3)(p-4)\). For \(a\ne1\) the equation determines \(d\) from \((a,b,c)\), so the \(V_d\)'s are disjoint. The slope Fourier atom \(\sum_{V_d}\beta(a)C(b)\alpha(c)\) has squared norm \(|V_d|\) in uniform probability on \(\mathcal X^3\), and these atoms are pairwise orthogonal.

The lift-invariant part projects onto \(a,b,c,d\in Q\). For each fixed \(a,d\in Q\setminus\{1\}\), opening the masks for \(b,c\in Q\) gives \(p/4+O(\sqrt p)\) allowed \(b\). Indeed the numerator and denominator of \(c\) have distinct roots since \(d\ne1,a\ne1\); the terms are bounded quadratic and cubic quadratic-character sums, including reduction to a nonconstant linear factor if the denominator root is zero. Exclusions cost only \(O(1)\) per \(a,d\). Thus the restricted fibers have size \(p^2/8+O(p^{3/2})\), uniformly. Their orthogonality also holds in the quotient character group.

In the independent relative coordinate order \((\alpha,\alpha\beta,C^{-1},\delta)\) the corresponding Fourier arguments are \((c/a,a,b^{-1},d)\). None equals \(1\) after this cut: \(c=a\) would force \(u=0\). Therefore averaging \(G^\circ\) uniformly in any one of these four ratio variables, keeping the others fixed, gives zero. The same holds for the lift-invariant projection. Condition on the common character \(x=U'\). In these relative coordinates the remaining four draws are independent with densities \(w(xr_j)\) on the finite group. One can exactly replace each by \(w(xr_j)-1/m\) in the conditional true pairing with \(G^\circ\). Removing the physical zeros and using the clean trace instead only affects the assembled true expectation by \(O(p)\); this centering is not a pointwise assertion about the clean-cut kernel.

The required ordinary-prime gain is still a bound for the centered four-factor pairing under the actual conditional laws. The disjoint slope fibers give exact uniform orthogonality, while the four other amplitudes remain jointly weighted.

## Exact singular values of a five-character flattening

Before taking expectations with \(w\), lift \(G^\circ\) back to the five original independent character variables \((V,U,V',T,U')\). The corresponding Fourier tuple on the graph is
\[
              (a,c/a,b^{-1},d,b/(cd)).
\]
Its fifth entry also differs from \(1\), since \(cd-b=(1-b)u\ne0\). Hence averaging over any one original character independently and uniformly kills the trace. This gives exact centering of all five true density factors in the assembled zero-removed expectation.

Partition the original variables into two on the left, \((V,U)\), and three on the right, \((V',T,U')\). In their uniform-probability Fourier bases the graph matrix has row index \((a,c/a)\), column index \((b^{-1},d,b/(cd))\), and entries of modulus one at the allowed tuples. The column determines \(b,c,d\), then determines \(a\) from the graph equation because \(cd\ne1\), as \(b\ne1,u\ne1\). Thus different rows have disjoint column supports. For every \(a\ne0,1\) and \(c\ne0,1,a\), fixing \(a,c\) fixes \(u\ne0,1\), and exactly \(p-4\) values of \(b\) are allowed. The exclusions are \(0,1,a,-u/(1-u)\), all distinct. The row Gram matrix is consequently the scalar \(p-4\) on its \((p-2)(p-3)\) nonzero rows. Its nonzero singular values are exactly \(\sqrt{p-4}\), or \(\sqrt{p-4}/p^{3/2}\) for the normalized trace.

Arbitrary further restrictions or weights of modulus at most one on graph entries keep the operator norm at most \(\sqrt{p-4}\), by disjointness of the row supports. This includes square and Legendre sign cuts, which act on the physical graph, rather than being clean-locus cuts in character space. It also includes factor-wise physical amplitude cuts. For actual factors \(h_j\) obtained by a cutoff of the original \(f\) in the corresponding physical Fourier argument, the graph sum is bounded by
\[
                         \sqrt{p-4}\,\prod_{j=1}^5\|h_j\|_2
\]
with counting norms in those physical coordinates. If three of the five amplitudes are at most \(p^{-1/2}\), their norms are \(O(1)\) and the other two norms are \(O(p^{1/4})\); hence this part costs \(O(p)\), with the original coupling and signs. More generally for factor-wise upper thresholds \(p^{-\alpha_j}\), the sufficient exponent condition is \(\sum_j(\alpha_j-1/4)_+\ge3/4\). The result concerns the actual physical graph with \(x,y\ne0\), which is exactly the original square-input domain when restricted to that domain. It gives no \(O(p)\) upper on the remaining moderate-amplitude terms. In particular applying the uniform flattening norm alone to all five uncut true factors would only yield \(O(p^{7/4})\).
