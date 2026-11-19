# Constant covariance against many translated Jacobi angles

The exact covariance exclusion of [round 80](astra-dissipation-80.md#the-conditional-covariance-of-transported-fields-is-constant) holds jointly for any finite list of distinct translated Jacobi angles. This extends the one-angle result to exactly the translates used in the signed Schur-head tests. The finite-field error below also permits the selected list and its weights to depend on the field and on the actual primary row.

## Excluding the two-center resonance

Use a finite field of odd order \(p\equiv1\pmod4\), the cyclic frequency group \(G=\widehat Q\), and select distinct centers \(i_1,\dots,i_m\) in \(G\). For each center let \(J_a\) be its full-character Jacobi line and select one of its two quadratic lifts. Each such line is a negative, convolution-invertible, pure weight-zero object. Its Mellin fiber weights have one \(-1\) at a tame character \(\xi_a\) matching its boundary at zero, and one \(+1\) at the character \(\xi_a\chi\) matching its boundary at infinity. On all other fibers its weight is zero. Different centers give disjoint pairs \(\{\xi_a,\xi_a\chi\}\) by definition of the quotient by the quadratic lift. Inverting a line reverses both signs. This is the rank-one case of the [boundary-weight rule](astra-feedback-52.md#reading-rank-from-two-mellin-characters), without restricting the available boundary characters to \(1,\chi\).

Work on the arithmetic Haar coset of a joint finite expression containing these lines and the fields to be tested. The distribution of \((J_1,\ldots,J_m)\) there is independent Haar on the \(m\)-torus. In fact any line product with a nonzero exponent vector has a nonzero boundary weight at a twist of any participating center. It cannot be a geometric punctual unit, so cannot be trivial on the geometric group. The character criterion for a closed subgroup of a torus gives surjectivity, even though the arithmetic coset may carry field-dependent phases.

Consider two negative geometric simples \(N,N'\) of dimensions greater than one. They are tame with only the interior singularity at one and with sole semisimple inertia eigenvalue \(-1\) there. Assume
\[
              N'\simeq N\star\prod_{a=1}^m J_a^{\,u_a}
\]
for integer \(u_a\). Their common convolution dimension \(d\) is also their common generic rank, since the inertia at one has zero invariants. For a simple of rank \(d\), summing absolute boundary fiber weights over **all** tame matching characters gives \(2d\): at each end the sizes of all its Jordan blocks sum to \(d\). Tensoring by the line product shifts every entry in a participating fiber by \(+u_a\) or \(-u_a\). Since both total absolute weight sums are \(2d\), the triangle inequality over all fibers yields
\[
                       2d\sum_a |u_a|\le4d .
\]
The negative parity scalar acts by \(-1\) on every negative constituent and on all \(J_a\), so \(\sum_a u_a\) must be even. The only nonzero cases left are one coefficient of magnitude two, or two of magnitude one.

For one coefficient of magnitude two, equality in the triangle bound implies the original weights on its two fibers lie in the intervals from zero to the opposite of the respective shift. Every other weight is zero. Both boundaries therefore have a single matching tame character, with block sizes at most two, and the two matching characters differ by \(\chi\). As in round 80, a tame rank-one twist on \(\mathbb P^1\setminus\{0,1,\infty\}\) makes all three inertias unipotent. It gives at least \(d/2\) invariants at each boundary and at least one at one. Geometric irreducibility of rank greater than one and the tame Euler characteristic formula give a contradiction: the sum of invariant dimensions must be at most \(d\).

For two coefficients of magnitude one, equality has a different consequence. All nonzero weights are of magnitude one and occur on the four fibers of the two centers. Each center pair supplies one possible matching character at zero and its quadratic mate at infinity, with the assignment depending on the sign of its coefficient. Write \(a_1,a_2\) for the two multiplicities at zero and \(b_1,b_2\) for the corresponding multiplicities at infinity, so \(a_1+a_2=b_1+b_2=d\). At each center in turn, take the ordinary rank-one twist that trivializes that center's matching character at zero and infinity. It is the Kummer twist matching the zero fiber, tensored with \(\mathcal L_{\chi(1-x)}\), since at infinity the latter supplies the quadratic mate. Both choices make the inertia at one unipotent and give the same number \(c_1\ge1\) of invariants there. Euler characteristic gives \(a_1+b_1+c_1\le d\) for the first choice and \(a_2+b_2+c_1\le d\) for the second. Adding them contradicts \(c_1>0\). This argument also covers a zero multiplicity at any boundary.

Schur orthogonality on the arithmetic coset now shows, for any complex sums \(h,k\) of the rank-greater-than-one negative traces,
\[
                        \mathbb E(\overline h k\mid J_1,\ldots,J_m)
                                  =\langle h,k\rangle.               \tag{1}
\]
Indeed every nonconstant torus Fourier coefficient vanishes by the exclusions just proved, with arithmetic multiplicity coefficients handled as in round 80. The statement passes to their second-norm closure. In particular every \(\mathcal K\)-transported positive field and every such increment satisfies (1). Positive nonpunctual inputs have at least one invariant at one, so after the ordinary quadratic twist the negative output has generic rank at least two. Rank-one seed and exceptional columns need to be kept separately.

## An arbitrarily weighted finite-prime test

Let \(h\) be a finite linear combination of raw lift-averaged negative traces with all geometric constituent dimensions at least two. Define its representation charge \(D_h\) by summing absolute coefficients times convolution dimensions, and let \(d_{\max}\) bound the individual dimensions. On the group \(G\) let
\[
 W(j)=\sigma\sum_a v_a k(j-i_a),\qquad
 v_a\ge0,\quad \sum_a v_a=1,\qquad M^{-1}=\sum_a v_a^2,
\]
where \(k\) is the actual normalized Jacobi kernel of [round 80](astra-surviving-80.md#weighted-translated-jacobi-moments). The symbol \(M\) in this section is the effective number of centers. Write \(b=\mathbb E_{\rm Haar}|h|^2\). Uniformly in these centers and weights and all real \(t\),
\[
 \left|\mathbb E_G\bigl[|h|^2 e^{tW}\bigr]
        - b\,\mathbb E e^{t\widetilde W}\right|
 \le C D_h^2 e^{|t|}
       \left[\frac{1+|t|}{\sqrt p}+
                          \frac{d_{\max}+1+|t|}{p}\right],           \tag{2}
\]
where \(\widetilde W=\sigma\sum_a v_a\cos\theta_a\) for independent uniform angles. In particular the main term is bounded above by \(b e^{t^2/(2M)}\).

For the proof expand one moment \(W^j\), \(j\ge0\), on the full character group. A monomial pairs two negative fields of respective dimensions \(d_1,d_2\) with \(j\) rank-one translated lines or duals. On good full characters its product is the corresponding middle-convolution trace. The pure tame convolution has generic rank at most \((j+2)d_1d_2\) by the [generic rank bound](uniform-fixed-depth.md#generic-ranks-in-a-fixed-tensor-category), including tensor words of mixed types. Its nonpunctual stalk at one costs at most this rank divided by \(\sqrt p\); the punctual part gives the exact arithmetic Haar moment. The union of exceptional characters of the factors has size \(O(d_{\max}+j)\), and on those characters the raw and convolution values are bounded by the convolution dimensions. Weight addition shows that the word has no other bad-character support, as a boundary character can only contribute nonzero weights where some factor has a nonzero weight. Averaging the two lifts gives exactly the cyclic average. Sum the absolute coefficient charges using \(D_h^2\), and the weights of the Jacobi monomials, whose total absolute coefficient sum is at most one. This gives error \(O(D_h^2[(j+2)/\sqrt p+(d_{\max}+j)/p])\). The Haar main term is \(b\,\mathbb E\widetilde W^j\) by (1). Sum the exponential series, which converges absolutely since \(|W|,|\widetilde W|\le1\). This proves (2) without requiring the number of centers to stay bounded.

For a fixed expression charge and \(0<u\le1\), (2) at \(t=\min(uM/2,\log p/8)\) gives
\[
 \mathbb E_G |h|^2\mathbf1_{W>u}
   \ \le\ b\,\exp[-c\min(u^2M,u\log p)]
                  +O\big(D_h^2(1+d_{\max})(1+\log p)p^{-3/8}\big).     \tag{3}
\]
Use the independent-angle exponential bound and \(t^2/(2M)\le tu/4\), then apply Markov to the weighted exponential. For a physical increment \(h_{\rm phys}\) approximated by such a field in normalized second norm, the cost of replacing the two squared moduli in (3) is at most \((\|h_{\rm phys}\|_{2,n}+\|h\|_{2,n})\|h_{\rm phys}-h\|_{2,n}\), uniformly in the chosen mask. This applies at fixed trace-approximable depth to genuinely transported increments with vanishing normalized marked corrections. At growing depth one must supply representation and approximation budgets in (2)–(3).

This controls a dynamical increment tested on the actual Jacobi-bias heads, including heads chosen from an optimizer rather than prescribed independently. The primary probability itself need not have a bounded negative trace representation of this type. Thus (3) is a bound on counting energy after trace weighting. It supplies neither an upper on the actual primary mass of the heads nor a mixed estimate for arbitrary nonlinear feedback tails outside the Jacobi tests.

## Application to a growing part of the true cold trajectory

Write \(D=D(p)\), \(\Lambda=\log_2^*p\), \(J_0=\lfloor D/8\rfloor\) for the marked depth and its shortened horizon, and let \(H\) be the base-two tower of height \(\lfloor\Lambda/2\rfloor\) starting from one. In the [true zero-floor recurrence](sector-trim-78.md), use \(X=\sqrt n K e_0\) and write \(Y_j=\beta_{j-1}X+h_j^{\rm cold}\) for \(1\le j\le J_0\). Here \(h_j^{\rm cold}=K|Y_{j-1}|\), and \(\beta_{j-1}\in[0,2]\) is the actual mark coefficient. Uniformly for all the weighted translate tests above and those times, for \(0<u\le1\),
\[
 \mathbb E_G |h_j^{\rm cold}|^2\mathbf1_{W>u}
 \ \le\ C D\,e^{-c\min(u^2M,u\log p)}+o(1).                       \tag{4}
\]
In the actual Mellin construction of [rounds 77 and 79](terminal-height-79.md#a-tower-scale-deletion-on-the-terminal-height), use error \(\varepsilon=(H+D)^{-4}\) and keep the actual \(\beta\) each time. Approximate \(|Y_{j-1}|\) by its even polynomial in the previous bounded negative fields. Its \(K\)-image is the raw transported geometric part plus the bounded exceptional-character error. Dropping that error leaves the negative part with all simple dimensions at least two, as above. This gives \(h_j\) as in (2), of representation charge and individual dimension at most \(\log_2\log_2p\) for large \(p\): the initial resource height is at most \(\Lambda/2+O(1)\), the elapsed \(J_0+2\) adds at most \(\Lambda/8+O(1)\), and the tower dominates the full resource. The normalized second error to \(h_j^{\rm cold}\) is \(O(D[\varepsilon+p^{-3/8}])=o(D^{-1/2})\), uniformly in time. The normalized second norms of the actual feedbacks are \(O(\sqrt D)\) by the exact cold energy bound. Thus replacement of squared moduli costs \(o(1)\) uniformly over subsets and the error term in (3) is \(o(1)\). This proves (4).

For a concrete common-window consequence, let \(S\) be a high-density charged row set of the [entropy test](entropy-filter-82.md#a-stronger-entropy-lower-when-the-high-branch-persists), with \(L\gg_\delta D\) and \(\rho\ge H^{-1/4}\). Its adaptive Jacobi bias heads are in \(\{W>\rho/8\}\), where the effective number of centers is \(M_S^{\rm eff}=\rho^{-2}L/M_E^2\), with \(M_E\le1\) the exterior clipped mass. Thus \(u^2M_S^{\rm eff}\gg_\delta D\) at \(u=\rho/8\), and \(u\log p\gg D\) since \(H\le\log_2\log_2 p\). Equation (4) gives \(o(1)\) total normalized squared feedback on this same head mask through all times \(j\le J_0\). The mask has vanishing counting fraction by the unweighted Jacobi estimate; the bounded rank-one source can be added for the same conclusion about \(Y_j\). This separates actual counting energy on the paid heads from the required bound on their primary mass.

At these heads one can also sum over the whole shortened prefix:
\[
                       \sum_{j\le J_0}\mathbb E_G |Y_j|^2\mathbf1_T=o(1).
\]
The transported main terms sum to \(O(D^2e^{-c_\delta D})\), and the total approximation cost is \(O(D^{5/2}[\varepsilon+p^{-3/8}])\). The arithmetic errors in (3) remain negligible after multiplication by \(D\). The unweighted exponential bound of [round 81](entropy-heads-81.md#an-exponential-comparison-for-weighted-translates) gives \(|T|/n\le e^{-c_\delta D}+O((\log p)p^{-3/8})\), so the same sum of squared rank-one source terms tends to zero.

1. Test whether the large feedback part of an actual later increment is captured, in its normalized squared weight, by a bounded number of these adaptive translated Jacobi-bias heads. Apply (3) only after obtaining that comparison.
2. For the real route bound the extent to which the true exterior primary measure differs from a controlled transported energy law on the same head set. The rank-one terms and positive normalization must be priced in such a comparison.
