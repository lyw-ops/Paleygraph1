# A fourth distinguished input and its fully pooled obstruction

For every sufficiently large eligible prime and prime square the actual stationary section continues holomorphically with \(|m_q(t)|\le3/\sqrt n\), \(n=(q-1)/2\), on
\[
 1040034/65536<\Re t<1040054/65536,\qquad |\Im t|<1/1048576.
\]
The overlap with the [round-57 rectangle](astra-rankfour-57.md) has real width \(2/65536\). At the lower proposed floor \(2031/128=1039872/65536\), the full arithmetic root majorant for the four distinguished inputs escapes even with an arbitrary complex phase for the fourth coefficient and a relative modulus tolerance of \(10^{-4}\). The continuation across that floor and the prime theta limit remain open.

## Signs, determinant contractions, and the translated input

Let \(m\) be the **positive** unitary Jacobi coordinate, \(C_1=(m+m^{-1})/2\), and use the perverse matrices for the raw field \(G=F_5\) of [the exact feedback identity](weighted-arithmetic-57.md#exact-lift-feedback-and-compact-moments). The geometric Jacobi line has value \(-m\) here. In the order \(C,C^\chi,D,D^\chi,E,E^\chi,F,F^\chi\), the rank and determinant exponent pairs are
\[
  (6,0),(6,0),(5,1),(5,-1),(5,-1),(5,1),(7,-3),(7,3).
\]
The standard matrix in a pair \((d,e)\) has determinant \((-m)^e\). Equivalently one may negate all eight matrices and use determinant \(m^e\), since \(d+e\) is even for each pair. With the former convention \(16G\) is the sum of the sixteen standard and dual traces without a sign. In particular the signed arithmetic lines in degree five have a negative coefficient in the positive Jacobi convention.

Conditionally on \(m\) and all older fields the scalar contributions in \((16G)^h\), for \(h=0,\ldots,6\), are respectively
\[
  1,\ 0,\ 16,\ 0,\ 768,\ -4(m+m^{-1}),\ 61444.
\]
Indeed decompose the \(s\)-th tensor power of the standard by adding one box at a time to partitions of length at most \(d\). For a product with \(j-s\) duals, a pair of retained partitions contributes to a scalar exactly when its difference is the constant row \((v,\ldots,v)\), giving character \((-m)^{ev}\). Multiply by the tableau counts of both partitions and the \(\binom js\) orderings. The independence of the derived factors allows multiplication of their tables with the multinomial factors. For example the four rank-five factors supply eight determinant words in degree five, and the two rank-six factors supply four determinant words beyond the 61440 balanced contractions in degree six. Since \(X=\sqrt2\Re m\) and the physical limiting field is \(U=-2\sqrt2 G\), this also gives
\[
  \mathbb E(U^5\mid X,Y,Z,W)=X/1024,\qquad
  \mathbb E(U^6\mid X,Y,Z,W)=15/8+1/8192 .
\]
These are conditional moments in the joint limiting law through the two field families.

Use the [rank-four coefficients](astra-rankfour-57.md#third-distinguished-subtraction) \(\alpha,\beta,\gamma\). In its signed old prefix let \(a\) be the coefficient on the older trivial derived label with Jacobi exponent \(+1\) in arity one, **before** translating by \(\gamma F_4\). Explicitly, with \(b_{l,e}\) the multiplicity of the trivial derived label in \((4W)^l\) at exponent \(e\), the formula used is
\[
 a=\sum_{l=0}^4\sum_{k=0}^7\sum_e
 (l+1)(\beta/4)^l d_{1+l,k,00}\, b_{l,e}\,
 \frac{\#\{z\in E_k:e+z=1\}}{|E_k|},\qquad
 E_0=\{0\},\quad E_k=\{-k,k\}\ (k>0).
\]
Duality gives the same coefficient at exponent \(-1\). Define the holomorphic fourth coefficient by \(\delta_*=-2\gamma a\). The input is \(S+\alpha Y+\beta W+\gamma F_4+\delta_*G+Z\). The new arity-zero amendment **before** \(K\) is \(+\delta_* C_1F_4\). Indeed \(K(C_1F_4)=-G+D_qKe_0\) with bounded \(D_q\), so it realizes the required subtraction \(-\delta_*G\) up to the exact column correction \(-\delta_*D_qKe_0\) in the residual update. This cancels exactly the old positive charge coming from the selected two terms \(\gamma a m^{\pm1} F_4\). Every other charge is kept.

At both twists \(D_G=L(C_1*D_{F_4})\) as measures, writing \(C_1\) for the symmetric unit-step measure here. The nonzero atoms are \(9/8,1/4,5/16,0,1/16\) at each sign of weights one through five, and the projected zero atom is \(9/4\). Thus the amendment alone buys no off-zero saving when the new branch is immediately propagated unsigned. The change of coordinates still allows the slightly smaller actual rectangle above.

## Certified upper rectangle

From the round-57 polynomial upper kernels, remove the originally charged measure \(|\gamma a|(\delta_1+\delta_{-1})*D_{F_4}\) from arity zero. On each slab only a lower bound for this deductible term is removed. This is valid since that explicit charge was included separately in the rank-four checker. Denote the resulting bounds by \(P_r\). The arity-\(j\) upper measure is
\[
  \sum_{h=0}^{28-j}\binom{j+h}j |\delta_*|^h P_{j+h}*D_G^{*h}.
\]
The frozen-zero argument uses the 50 positive caps in the checker, \(\eta=1/5\) and \(\epsilon=6\cdot10^{-7}\). The omitted binomial tail beyond degree 28 includes the extra term \(|\delta_*|\sum_w D_G(w)\cosh(\eta w)\) in the input norm. The corresponding coordinate debit is \(23|\delta_*|/4\). The old signed prefix, positive remainder, core convolution and mixed derivative bound are as in round 57.

Ten closed real slabs of width \(2/65536\), with the full claimed imaginary thickness and \(s\in\sqrt8\pm10^{-12}\), have off-zero excess below \(395/10^9\) and full coordinate cap \(4.648\). The uniform convergent absolute Taylor majorant also pays for all bad compact-lift errors after applying \(K\), as well as the true marked activation. Their first-packet cost is \(O(n^{-1/2})\), absorbed by the slack. The bulk Euclidean contraction factor is strictly below \(3/4\) by \(4.648/\sqrt{4(1040034/65536)-4.648^2}<3/4\); the marked derivative has denominator \(\sqrt{4n-4.648^2}\). Exact iteration from the four distinguished seeds stays bounded and converges locally uniformly. The limit has positive factors on the real overlap, so uniqueness identifies it with the physical branch. Its scaled marked coordinate gives the stated inverse-hyperbolic-sine bound. [Exact branch argument](marked-domain-53.md#from-scalar-slack-to-the-actual-holomorphic-section)

## Lower certificate after full arithmetic collection

Fix either real floor below with the preceding three distinguished coefficients and the limiting seed scale. Allow the fourth coefficient to be any complex number \(\delta\) with the indicated modulus. At each fixed arity collect all infinite Taylor terms by full arithmetic irreducible including the signed phase in positive coordinates and the total exponent. Between nodes propagate the residual by the unsigned packet convolution rule.

First compute old signed rank-three lower/upper measures, retaining Legendre degree four, \(W\)-degree four and every Jacobi mode at arities through thirteen. The [rank-four lower construction](astra-rankfour-57.md#a-quantitative-limitation-after-full-arithmetic-pooling) then yields bounds on the degree-28 arity kernels through all four old factors, with the nonconstant unique-shift degree-two sectors retained, the scalar unit debited, and all degree-three-and-higher contributions debited in full. Amend their arity-zero lower/upper measures by subtracting/adding \(|\delta|C_1*D_{F_4}\). Taking positive parts gives degree-28 lower measures \(L_r\), with upper measures \(U_r\). This reverse triangle inequality permits *every* phase for \(\delta\).

The sixteen new linear characters have distinct derived labels, and are disjoint from degree zero. Since each new standard has dimension at least five, none of their quadratic nontrivial labels is linear. Every such quadratic label occurs at a unique determinant shift in degree two in the chosen partition gauge. For a single factor the possibilities are the symmetric square, exterior square, their duals, and the adjoint. The symmetric/exterior pairs of the dual and the standard stay distinct in these dimensions. Products across two factors have their two nontrivial representations specified separately. Thus there is no cross-old-label collision for each retained new derived label. Sixteen ordered dual pairings supply the coefficient \(1/16\) on the unit. The arity-\(j\) polynomial lower measure is bounded from below by
\[
 \begin{split}
 L_j&+(j+1)d\,L_{j+1}*D_G\\
 &+{j+2\choose j}d^2\big[L_{j+2}*(D_G^{*2}-\delta_0/16)-U_{j+2}/16\big]\\
 &-\sum_{h=3}^{28-j}\binom{j+h}j d^h U_{j+h}*D_G^{*h},\qquad d=|\delta|.
 \end{split}
\]
Higher-degree arithmetic cancellations are all covered by the last debit, irrespective of the full signed determinant character. At each weight additionally subtract the ordinary binomial tail divided by \(R^j\), at the best of ten positive trial radii \(R\), using total input dimension \(s+2|\alpha|+3|\beta|+4|\gamma|+23d/4+R\). Take positive parts and retain shifts through 18, arities through nine and output packets through 28.

| Floor | Allowed \(\lvert\delta\rvert/\lvert\delta_*\rvert\) | First certified height with lower mass above 21 |
|---|---|---:|
| \(2031/128\) | \([1-10^{-4},1+10^{-4}]\) | 1403 |
| \(1015/64\) | \([1-10^{-3},1+10^{-3}]\) | 377 |

In both cases the exact quadratic zero-shift atom exceeds \(1/20\). Jensen conditional on one packet shows the next full mass exceeds the square of the current full mass divided by 20. There is no finite-mass supersolution for this map at either floor. This conclusion allows the indicated fourth-parameter annulus at each separate floor and assumes unsigned residuals between nodes. No physical singularity or monotonicity in the floor is inferred.

## A two-node noncollision test

Consider the arity-zero pure \(C_4\), the individual quadratic Legendre symmetric squares, and the product of the two different Legendre standards. The group theory of the old two independent \(SL_2\)'s and invertibility of the Jacobi powers make each incoming constituent simple. From the [two-boundary twist rule](astra-feedback-52.md#reading-rank-from-two-mellin-characters), the generic irreducible output after the first \(K\) has the following data up to exchanging the twists.

| Incoming constituent | Output at \(1\) | Output at \(\chi\) | Output dimension |
|---|---|---|---:|
| \(m^4\) | \((-4,0,0,4)\) | \((0,0,0,0)\) | 4 |
| \(\operatorname{Sym}^2 N\) | \((-4,0,0,0)\) | \((0,0,0,4)\) | 4 |
| \(N\star N^\chi\) | \((-2,-2,0,0,0,0,2,2)\) | same | 8 |

At the next \(C_1\) vertex convolution by either Jacobi line shifts every weight in a given list by the same integer. The dimension and the unordered pair of diameters therefore separate the three families even after the possible quadratic twist. Applying the next \(K\) tensors the generic local system by an invertible ordinary line, so it cannot identify distinct surviving simple inputs. Consequently signed collection across these three families at the leading linear outer vertex cannot improve their total by cross-family cancellation. Lower-order exceptional columns in the finite vector formulas are separate. Other sources and collisions within a family remain available.

## Replay and ranked next tests

From the repository root run

    .venv/bin/python -B research/astra-ranknext-58-check.py

The [checker](astra-ranknext-58-check.py) emits [four records](astra-ranknext-58-checks.jsonl) from integer representation counts and Arb192. The optional [floating cap search](astra-ranknext-58-probe.py) accepts the rectangle endpoints as integer arguments. It supplies no proof bounds.

1. Carry signed residual coefficients through a second vertex only for matched signatures. Enumerate the old arity-zero sources at the same signature as each of the three table rows, including old rank-three and rank-four products. For each pair test actual sheaf equivalence by an arithmetic identity, then debit the complementary root kernels. Success requires actual overlap reaching below \(2031/128\). An exhaustive mismatched-signature or distinct-trace proof on the chosen finite list rules out that list as a source of savings.
2. Investigate the actual trial with a different invariant on residuals, retaining the sign and the field of at least one packet across activations. The two annulus escapes exclude changing only the fourth coefficient's phase or its modulus within the stated bounds while propagating unsigned residuals. Require a strict invariant crossing the same floor or a fully debited lower escape of the specified signed propagation.
