# Jacobi-angle control of the true prefix and sharp pathwise Dirichlet loss

Let \(p=2n+1\equiv1\pmod4\) be prime, \(s_p=2\sqrt{p/n}\), and \(S=2\sqrt n K e_0\). Write \(\|\cdot\|_N\) for normalized counting second norm. The real physical mark satisfies
\[
 \limsup_{p\to\infty}\sup_{|t-2031/128|\le2^{-17},\ t\in\mathbb R}|m_p(t)|
 <3.83\cdot10^{-221}.
\]
For the true leading rows \(L_1=K(S^2/2)\), \(L_{j+1}=K(S L_j)\), their normalized Gram matrix has the uniform estimate
\[
 \langle L_j,L_k\rangle_N
 ={\bf1}_{j=k}\frac{s_p^4}{32}(s_p^2/2)^{j-1}
     +O(6^{j+k}/\sqrt p).\tag{1}
\]
The compact leading fields also satisfy \(\mathcal E(H_j)\le1296\|H_j\|_2^2\) at arbitrary heights. The error in (1) tends uniformly to zero for \(1\le j,k\le (\log_2 p)/16\). These rows are the leading large-floor coefficients of the seed increments and are different from the full nonlinear increments at the cold floor. The mark bound uses the actual nonlinear nine-center prefix of height 600. It is a positive tolerance, with common complex continuation for unbounded sizes still open. [Leading rows](astra-newton-77.md) · [Physical nine-center prefix](astra-predictor-76.md)

## The conditional covariance of transported fields is constant

On a fieldwise compact Haar coset use the unitary Jacobi convolution line \(J\) with boundary weights \((-1,+1)\) at the trivial and quadratic fibers. Reversing its sign convention or replacing it by its inverse has no effect below. Its projection is Haar on the unit circle because the first geometric weight circle acts with weight of magnitude one. Put \(C=\Re J\), choosing the overall trace sign so the seed is \(s_p C\) (a translation of the angle by \(\pi\) is harmless). For every complex linear combination \(h\) of negative trace fields, and its second-norm closure, there is a complex number \(b\) such that, with \(a=\|h\|_2^2\),
\[
 \mathbb E(|h|^2\mid J)=a+2\Re(bJ^2),\qquad 2|b|\le a.                \tag{2}
\]
In particular
\[
 \tfrac14\|h\|_2^2\le \|Ch\|_2^2\le\tfrac34\|h\|_2^2.            \tag{3}
\]
Both constants in this full negative complex span are attained, using \(h=\Im J,\Re J\).

Indeed an inner product between a negative simple character and \(J^k\) times another vanishes unless the two geometric simples agree after that line twist. This remains true of twisted characters on an arithmetic coset by matrix-coefficient orthogonality, after collecting each arithmetic multiplicity. Both negative simples then have the same convolution dimension \(d\), also the generic rank of each. In each fiber tensoring by \(J^k\) shifts all \(d\) weights by \(+k\) or all by \(-k\). The pooled sum (one half of the sum over both fibers) of the original absolute weights is \(d\), as is that of the shifted absolute weights. The triangle inequality forces \(|k|d\le2d\). The common geometric scalar \(-I\) on the negative generators, including the Jacobi line, eliminates odd \(k\) in the conditional square. Uniqueness of Fourier coefficients on the circle proves the form in (2). Its continuous nonnegative density gives the coefficient bound. Passing to the closure uses \(L^1\) convergence of squared moduli. The inequalities and vanishing character integrals also pass to the subsequential compact models by the fixed-word approximation. [Two-fiber rank formula](astra-feedback-52.md) · [Odd tensor parity](iteration-parity.md) · [Coset orthogonality](astra-fixed-79.md)

In fact the endpoint \(|k|=2\) is excluded when \(d>1\). Equality in the weight triangle inequality holds entrywise. For one choice of sign the original first-fiber weights all belong to \([-2,0]\) and the quadratic-fiber weights to \([0,2]\), with the roles interchanged for the other sign. Thus at position zero all boundary Jordan blocks have a single tame character and sizes at most two. At infinity they have the opposite character and sizes at most two. Tensor the ordinary generic local system with a rank-one Kummer local system on \(U=\mathbb P^1\setminus\{0,1,\infty\}\) that trivializes these two characters. Its character at one is quadratic since those boundary characters are opposite. Concretely a product of the two Kummer systems for \(x\) and \(1-x\), with exponents zero or one, realizes these prescribed signs. The old inertia at one had only eigenvalue \(-1\), so the new inertia there is unipotent. The new local system remains geometrically irreducible of generic rank \(d>1\). Its invariant dimensions at zero and infinity are each at least \(d/2\), since the unipotent blocks have size at most two. At one it has at least one invariant. The tame Euler characteristic of the ordinary \(j_*\) extension on \(\mathbb P^1\) is \(-d+\sum_{x=0,1,\infty}\dim V^{I_x}>0\); geometric irreducibility of rank greater than one makes both \(H^0\) and \(H^2\) zero. This contradiction eliminates the endpoint resonance. Here \(H^2\) agrees with compact-support \(H^2\) on the open curve by the punctual-stalk exact sequence. [Weight-to-Jordan correspondence](astra-feedback-52.md) · [Tame Euler characteristic method](astra-rank-six-67.md)

There is a second orthogonality specific to \(\mathcal K\), the geometric positive-to-negative transport. A positive nonpunctual simple has unipotent inertia at one, so its invariant stalk has dimension at least one. Its generic rank \(r\) is at least \(d+1\ge2\), where \(d\) is its convolution dimension, equal to the drop at one. The negative output has convolution dimension \(r\). It is therefore orthogonal to every \(J^k\), all of dimension one. This proves \(\mathbb E(\mathcal K f\mid J)=0\), including \(L^2\) limits of positive fields. In the full limiting Picard recurrence \(U_{j+1}=S+\mathcal K F_t(U_j)\) with \(F_t(x)=\sqrt{4t+x^2}\), we have \(\mathbb E(U_{j+1}\mid J)=S\). The same holds for the initial nine-center row by its positive finite preimage.

Every output of \(\mathcal K\) thus has all its negative simples of dimension greater than one. For any two such outputs \(h,k\), polarization and the endpoint exclusion give
\[
 \mathbb E(\bar h k\mid J)=\langle h,k\rangle .
 \tag{4}
\]
The identity extends to their complex \(L^2\) closure. In particular for \(U=S+h\) all true compact feedbacks have conditional second moment \(\mathbb E(|U|^2\mid J)=S^2+\|h\|_2^2\). It is their second moments, including all pairs of heights, that satisfy (4); higher conditional moments require separate estimates.

## Explicit logarithmic-height field comparison for the leading coefficients

Define the compact rows \(H_1=\mathcal K((s_p C)^2/2)\), \(H_{j+1}=\mathcal K(s_p C H_j)\) for the prime in question. Each \(H_j\) has zero conditional mean given \(J\). Transport is an isometry on centered positive fields, so \(\|H_1\|_2^2=s_p^4/32\) by the circle moments, and \(\|H_{j+1}\|_2^2=s_p^2\|CH_j\|_2^2\). By (4), multiplication by \(s_p C\) followed by transport scales every inner product on this image by \(s_p^2/2\), since the preimages \(s_p C H_j\) have mean zero. Moreover \(\langle H_1,H_{j+1}\rangle=0\) for \(j\ge1\) by \(\mathbb E(H_j\mid J)=0\) applied after removing the common transport. Repeatedly reducing both indices gives the diagonal Gram matrix in (1) exactly on the fieldwise compact coset.

For clarity about simultaneous heights, retain each full-character geometric term and both quadratic lifts before collecting any signs. Let \(D_j\) be the sum of absolute coefficients times convolution dimensions of this expansion after transport. Since the seed is the sum of two invertible lines of total coefficient mass \(s_p<3\) for large primes, the first mass is at most \(s_p^2\): a square of a Jacobi line has generic rank two and mixed opposite powers are punctual. For a negative simple of rank and dimension \(r\), adding either line changes the pooled first absolute moment by at most \(r\). Its transported product accordingly has dimension at most \(2r\). Thus \(D_{j+1}\le 2s_pD_j\le6D_j\), and \(D_j\le2\cdot6^j\). Positive intermediate products have convolution dimension equal to their old dimension before the line shift. These are fieldwise finite objects for every \(j\).

Let \(E_pH_j\) denote the raw compact-support Mellin trace evaluation of this lift-invariant expression. The raw product giving one new step agrees with the convolution evaluation except at the two full characters \(1,\chi\), representing one cyclic coordinate. The discrepancy at that coordinate costs at most \(2s_pD_j\), by the dimension bound for raw traces. Fourier inversion implements the ordinary twist exactly on the full preimage evaluation, including its zero at position one. Consequently
\[
 \|L_{j+1}-E_pH_{j+1}\|_N\le s_p\|L_j-E_pH_j\|_N+2s_pD_j/\sqrt n .
\]
The initial discrepancy is \(O(1/\sqrt n)\) by the same one-coordinate argument. Iteration gives \(O(6^j/\sqrt p)\) with absolute constant. For the cross moment the convolution expression \(\overline{H_j}H_k\) has total absolute dimension at most \(D_jD_k\), and total absolute generic rank at most \(2D_jD_k\) by the tame two-factor rank bound. Only the same two full characters require product or dual repairs, at cost \(O(D_jD_k/p)\) in the mean. The punctual trace at one is exactly the Haar coset integral. The nonpunctual stalks have weight at most \(-1\), contributing at most \(2D_jD_k/\sqrt p\). This bounds the discrepancy of the physical raw cross moment from the Haar moment by \(O(6^{j+k}/\sqrt p)\). The raw evaluation has supremum at most \(D_j\), so replacing it by \(L_j\), and the other evaluation by \(L_k\), gives the same error, proving (1). [Single bad cyclic coordinate](marked-domain-53.md) · [Convolution rank and Haar versus stalk average](uniform-fixed-depth.md)

## The nonlinear nine-center secants

Write \(a_0=2031/128, L=a_0-2^{-17}, B=1.94\), and use the closed square of half-width \(2^{-17}\) around \(a_0\). The actual nine-center caps imply in every subsequential compact model \( |U_j-S|\le B\) for \(0\le j\le600\), with limiting \(S=\sqrt8 C\) up to the common sign. On adjacent segments use \(b=0\) on the real interval and \(b=B\) on the complex square. For \(y\) on such a segment,
\[
 |F'_t(y)|^2\le \frac{|y|^2}{4L-2b^2+|y|^2}
 \le g_b(|C|),\qquad g_b(c)=\frac{(\sqrt8 c+B)^2}{4L-2b^2+(\sqrt8 c+B)^2}.
\]
Every increment from the nine-center start is a difference of two transported fields because the seed cancels, including \(U_1-U_0\) by the finite preimage of the starting row. Thus (4) gives the exact equality \(\mathbb E[g_b(|C|)|h|^2]=\mathbb E[g_b(|C|)]\|h\|_2^2\) for these increments. This applies to the angular upper bound for the entire secant before the norm contraction under \(\mathcal K\).

Uniformly in all subsequential models the real contraction factor is below \(0.428236\), and the complex factor is below \(0.449922\). The checker bounds the squared factor by left Riemann sums for \(g_b(\cos\theta)\) on \([0,\pi/2]\) with normalized Lebesgue measure. The integrand is decreasing. After taking the square root the 8192-interval upper sums are below those two constants. Fixed-prefix transfer on the closed square uses the absolutely convergent round-76 trace approximations (complex coefficients are allowed), or real and imaginary joint moments with duals. The physical marked correction has vanishing normalized second norm at each fixed step, using the uniform physical cap and the single column comparison. Subsequence compactness in the floor makes the estimates uniform in the limsup. This transfer gives no effective field threshold for the refined factors. [True prefix and exceptional repairs](astra-predictor-76.md) · [Subsequential model](astra-fixed-79.md)

The initial normalized increment is below four. Consequently the field-limsup of the real height-600 increment is at most \(4(0.428236)^{599}\), and the complex normalized residual at that row has limsup at most \(4(0.449922)^{600}<3.06\cdot10^{-208}\). For the latter step only the height-599 and height-600 inputs need the cap. The real positive-factor comparison costs at most \(0.4\) times the height-600 increment in the mark limsup. The strict numerical bound on \(1.6(0.428236)^{599}\) gives the claimed physical tolerance. The normalized complex residual is separate from the counting residual required for common continuation. [Initial increment and real transfer](astra-newton-77.md) · [Interval replay](astra-dissipation-80-check.py) · [Records](astra-dissipation-80-checks.jsonl)

## Nonlinear Dirichlet balance at every real height

Use the real limiting bulk orbit from the Jacobi seed and the two-circle Dirichlet form \(\mathcal E\) of round 79. On a positive expression \(f\) define \(\mathscr L(f)=\mathcal E(f)-\mathcal E(\mathcal K f)\). On each nonpunctual geometric character its energy contribution is multiplied by \(1-d/r\) in this nonnegative quadratic form. For \(t>0\), at every integer \(H\ge1\),
\[
 \mathcal E(U_H)+
 \sum_{j=0}^{H-1}\left[
 4t\,\mathcal E\!\left(\operatorname{arsinh}(U_j/(2\sqrt t))\right)
 +\mathscr L(F_t(U_j))\right]
 =\mathcal E(U_0)+4H.                                          \tag{5}
\]
This also holds from a real finite nine-center start, with its corresponding initial energy. Orthogonality between the seed and the transported characters persists after either circle derivative by Schur matrix-coefficient orthogonality. The two unit Jacobi weights give \(\mathcal E(S)=4\) in the limiting model. The chain rule and the scalar identity \(F'_t(x)^2+4t\,[(\operatorname{arsinh}(x/(2\sqrt t)))']^2=1\) give (5) by telescoping. At any finite real height outside the certified sup ranges the graph-norm construction still works. Approximate the preceding negative input by real trace polynomials in the graph norm, compose with the globally Lipschitz functions with bounded continuous derivatives, and on each approximant's compact range approximate the function and its derivative by parity-correct polynomials. The convergence of the differentiated compositions follows by boundedness of the derivatives and dominated convergence in measure against the squared limiting gradient. Apply the closed transport contraction. Physical normalized \(L^2\) identification at each such height follows by the same Lipschitz approximation, starting with the seed; the actual mark can be restored by the fixed-depth comparison. [Compact model and chain rule](astra-fixed-79.md) · [Fixed-depth physical passage](iteration-parity.md)

For example the height-average of the two nonnegative losses in (5) is at most \(4+\mathcal E(U_0)/H\). Since the inverse hyperbolic sine is odd on the real negative input and has zero mean, its second moment is also bounded by its energy. Thus the same bound holds if its energy in the sum is replaced by its actual limiting second moment. Equation (5) controls every compact-model real prefix, without a uniform compact sup assumption. Concentration of the original increment on high \(|U_j|\) remains possible with these aggregate bounds.

## Average and worst cumulative discounts on Jacobi paths

Consider a negative simple of dimension \(r>1\), multiply by either Jacobi line, and transport the positive result. Line multiplication preserves geometric simplicity and convolution dimension \(r\). The input to transport cannot be punctual because its dimension exceeds one. Its generic rank \(r'\) is between \(r+1\) and \(2r\) by its nonzero unipotent invariants and the shifted two-fiber absolute-moment bound. The output is again a negative simple. Along any \(h\) lifts the product of the successive multiples \(d/r_{\rm generic}\) is exactly \(r_0/r_h\), at most \(r_0/(r_0+h)\). This product counts the transport discounts alone. Multiplication by a line changes the energy before the next discount.

With independent equiprobable signs there is a stronger estimate
\[
 \mathbb E_{\rm paths}(r_0/r_h)\ \le\ (7/8)^{\lfloor h/2\rfloor}.          \tag{6}
\]
Let \(z,b_1\) be the pooled zero and absolute-weight-one multiplicities in the parent. The pooled mass and first absolute moment both equal \(r\), so mass at \(|w|\ge2\) is at most \(z\) and \(b_1\ge r-2z\). The two possible shifts give \(\mathbb E r'=r+z\), since the mean of \(|w\pm1|\) equals \(\max(1,|w|)\). The shifted nonzero counts are preserved by transport. The expected number of shifted zeros is \(b_1/2\); hence \(\mathbb E z'=z+b_1/2\ge r/2\). For the second independent shift, \(\mathbb E r''=\mathbb E(r'+z')\ge3r/2\), and \(1\le r''/r\le4\). The chord \(1/x\le1-(x-1)/4\) on this interval gives the conditional two-step bound \(7/8\). Successive conditioning gives (6). The equal probabilities describe the two terms of a single Jacobi factor before combining paths into characters. The conditional covariance (4) handles signed sums of transported fields directly.

For the leading field \(H_j\), the branch probabilities in (6) are its actual squared character coefficients divided by \(\|H_j\|_2^2\). The first two nonpunctual positive terms \(J^2,J^{-2}\) are inequivalent lines with equal coefficients. Positive nonpunctual transport preserves inequivalence, and there are two distinct negative simple outputs. At every succeeding step children with the same line sign can coincide only if their parents agree, by injectivity of both line multiplication and transport. A collision between children with opposite signs would identify their parents after the \(J^{\pm2}\) twist excluded above, since the parents have dimension greater than one. Thus all \(2^j\) leaves of \(H_j\) are mutually inequivalent, defined over the field, with equal absolute coefficients. In particular (6) controls the average accumulated rank discount of the full leading expansion, including the slow path below with its exact squared mass fraction \(2^{-j}\).

There is an all-height normalized Dirichlet bound on the same signed leading fields:
\[
                   \mathcal E(H_j)\le1296\,\|H_j\|_2^2,\qquad j\ge1.     \tag{7}
\]
For an individual negative simple put \(e=(\sum_{\rm pooled} w^2)/r\), its Dirichlet energy in the unit character normalization. The line shift increases the root mean square of its weights by at most one. Transport preserves the numerator and changes the denominator, so \(\sqrt{e'}\le\sqrt{r/r'}(\sqrt e+1)\). Twice along a path this gives
\[
 \sqrt{e''}\le\sqrt{r/r''}\big(\sqrt e+1+\sqrt{r'/r}\big)
              \le\sqrt{r/r''}\big(\sqrt e+1+\sqrt2\big).
\]
Use the conditional two-step reciprocal bound and then Minkowski over the parent paths to get \((\mathbb E e_{j+2})^{1/2}\le\sqrt{7/8}((\mathbb E e_j)^{1/2}+1+\sqrt2)\). The initial character has \(e_1=2\) and \(\sqrt{e_2}\le\sqrt2+1\). Since \(\sqrt{7/8}(36+1+\sqrt2)<36\), induction gives (7). Distinct characters are orthogonal after differentiation, so their mean energy here is exactly \(\mathcal E(H_j)/\|H_j\|_2^2\). This is a uniform compact arithmetic estimate on the real leading fields. A derivative on the physical finite vector has not been defined.

For sharpness of the worst-path result take \(J\) with shifts \((-1,+1)\), start at the negative twist of \(J^2\), and successively choose the shifts \((+1,-1),(+1,-1),(-1,+1),(-1,+1)\), repeated indefinitely. The initial square has dimension one, rank two and nonzero weights \(-2,+2\) split between the fibers; after transport both belong to the first fiber. At index \(j=4k+i\) write \(v=2k\). Exponents in the table give multiplicities, with zero multiplicities omitted.

| \(i\) | First fiber | Quadratic fiber |
|---|---|---|
| 0 | \((-2)^{v+1},1^v,2\) | \(0^{v+2},1^v\) |
| 1 | \((-1)^{v+1},0^{v+2}\) | \((-1)^{v+2},2^v,3\) |
| 2 | \(0^{v+3},1^v,2\) | \((-2)^{v+2},1^{v+2}\) |
| 3 | \((-1)^{v+3},2^{v+2}\) | \((-1)^{v+2},0^{v+2},1\) |

Indeed at each step shift by the indicated opposite unit weights, retain negative weights at their original fibers and exchange positive weights. Fill each fiber up to the new dimension, half the sum of all absolute shifted weights, with zeros. Substitution gives the next row, including \(i=3\) to \(i=0\) with \(v\) increased by two. Each fiber has dimension \(2+j\). This proves equality in the worst-path bound for \(r_0=2\) and gives successive positive simple ratios \((j+2)/(j+3)\) tending to one. The weights after shift have bounded magnitude (at most four), so each corresponding normalized character has bounded Dirichlet energy while its output's absolute dimension cost diverges. This path occurs with the squared mass computed above in the leading coefficient. Its contribution to the full nonlinear increment at the cold floor involves additional orders. The independent integer replay checks the first 1025 outputs. [Arithmetic rule for line shifts and transport](weighted-arithmetic-57.md) · [Replay](astra-dissipation-80-check.py)

1. At the cold real floor, estimate the tilted increment mass \(\int_{|U_j-S|>B}|\Delta_j|^2\) for genuine growing heights, together with a physical-to-Haar error at those heights. A small relative mass combined with (4) gives a strict secant contraction without requiring every site to meet the old cap. On a complex tube also control the branch and derivative on the exceptional coordinates.
2. Price higher conditional moments of the genuine transported fields on \(|U_j-S|>B\). A uniform fourth-moment or mixed-moment estimate controlling \(\mathbb E[|\Delta_j|^2|U_j-S|^2]/\mathbb E|\Delta_j|^2\) at growing heights would estimate the exceptional increment mass in the first test. Test first the exact signed mixed fourth moment at short heights against the higher-rank trace relations.
