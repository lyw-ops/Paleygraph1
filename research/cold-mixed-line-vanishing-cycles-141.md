# The first Jacobi–Legendre inverse-line collision

Use the actual position and frequency conventions of [Round 140](cold-leading-inverse-legendre-140.md). Write \(S=s_n C_1\), \(s_n=2\sqrt{p/n}\), and let \(Y\) be the actual Legendre center in \(KC_2=Y-2C_1/\sqrt p\). Consider the selected mixed block between the degree-one marked derivative from \(S\) and that from \(Y\), before adding any other nonseed words. The pure-seed square does not contain this block.

## The physical mixed trace

On \(G=\mathbb F_p^{\times2}\), the inverse Fourier row of \(C_1\) is \(s(v)/\sqrt p\). Since \(C_2=2C_1^2-1\), the exact feedback and the [quadratic sign convolution](paired-legendre-cubic-116.md#conversion-to-a-restricted-legendre-family) give
\[
 Y^\vee(v)=\frac{2}{p}s(v)\bigl((s*_G s)(v)+1\bigr)
          =-\frac{s(v)}p A_p(v).
\]
This holds at \(v=1\) as well, because \(s(1)=0\). The notation \(Y^\vee(v)\) here denotes inverse Fourier transform, not a dual sheaf. The actual marked linear derivative rows are \(a\,s+b\) for \(S\) and \(-\chi(1-v)A_p(v)/(2p\sqrt t)+b_Y\) for \(Y\). Here \(a,b\) are those of Round 140 and
\[
 b_Y=\frac{Y_0}{2n}\left(n^{-1/2}-t^{-1/2}\right)
\]
is a constant positional correction. Any chosen coefficient of \(Y\) multiplies the second row and can be factored out of this selected mixed block.

For any two rows \(d_1,d_2\) the inverse-line kernel in \(u=x/z\) is
\[
 H_{1,2}(x)=s(x)\sum_{u\in G}s(x/u)d_1(u)d_2(x^2/u).
\]
The substitution \(u\mapsto x^2/u\) preserves \(G\) and \(s(x/u)\), because \(s(v^{-1})=s(v)\) on \(G\). Thus the two mixed orders are exactly equal, with all marked corrections. At the collision both factors see their argument \(1\). Their values at that point do not give their nearby cycles.

## The local family at \(-1\)

For the nonconstant parts of the two rows, use the rank-one Jacobi Kummer sheaf and the rank-two twisted Legendre sheaf. Suppress their nonzero scalar normalizations and the common sign of the Legendre inverse Fourier trace. At their interior singularities their geometric tame inertia representations are respectively \(\chi_2\) and \(\chi_2\otimes\operatorname{Unip}(2)\). [Katz, Legendre and twisted Legendre monodromy](https://web.math.princeton.edu/~nmk/mellin324book.pdf)

Over the henselization at \(x=-1\), the family with \(v=x^2/u\) has moving singular sections at \(u=1,x^2,x\). Only \(u=1\) and \(u=x^2\) meet at this fiber. The Kummer factor \(s(x/u)\) and the outer factor \(s(x)\) are lisse at the collision and both have special trace \(\chi(2)\), so their product gives a trivial local arithmetic twist. The two full-field sums from the square indicator differ by \(\chi(u)=\chi(v)\). These are the two Legendre mates, with their relative twist locally trivial and of value one at the collision. The square selector averages two identical local contributions, and symmetrizing the two convolution orders doubles the physical mixed sum.

The map \(x\mapsto x^2\) is étale at \(-1\). At the collision the nearby calculation is therefore that of multiplication at \((1,1)\), with target parameter \(x^2=1\). The tame local convolution theorem gives the tensor product of the two inertia blocks on the degree-one vanishing cycles of the ordinary fiber sum. It is \(\operatorname{Unip}(2)\). This computes the geometric inertia; the Kummer signs just checked specify the extra arithmetic twists, without evaluating the intrinsic local Frobenius matrix. The other sections, including the two boundary sections of the compactified \(u\)-line, are disjoint near this fiber with fixed tame conductors, so the same local acyclicity argument as in the multiplication-family calculation applies there. [Rojas-León, Lemma 5.5 and Corollary 5.7](https://arxiv.org/pdf/1106.1398)

The special-fiber \(H_c^2\) still vanishes. At \(u=x=-1\) the two row sheaves are lisse, whereas \(s(x/u)\) has nontrivial scalar quadratic inertia. This excludes geometric coinvariants at the special and nearby fibers for both square-selector branches. The specialization sequence therefore makes the nontrivial unipotent vanishing-cycle space a quotient of nearby \(H_c^1\). For each branch, the tame Euler characteristic gives generic dimension six and special dimension four: the rank is two on the respective five-puncture and four-puncture lines, and the actual product has zero stalk at the deleted points. These dimensions do not determine the rest of the nearby Jordan form. The full-field single-row constant corrections \(b,b_Y\) do not contribute vanishing cycles at this collision: with either row constant, its section at \(1\) or \(x^2\) is absent and the remaining sections stay disjoint. The \(C_1\) correction in the separate formula for \(KC_2\) belongs to the rank-one-by-rank-one word and is not the Legendre collision computed here.

This establishes ramification of the displayed mixed trace realization, with the physical marks and both orders retained. It does not show that all other analytic words in the actual square difference preserve the corresponding local contribution, or give a lower bound on \(P_{5000}\).
