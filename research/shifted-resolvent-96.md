# All-source coordinate bounds for the transported cold predictor resolvent

On the nominated complex square, the genuine height-100 and height-250 predictors have transported linearized inverses whose **every** matrix entry is \(O(n^{-1/2})\) through eligible primes. At height 600 the bound is \(O(n^{-0.467})\). The bounds apply to arbitrary source and target coordinates, including ones chosen after examining the real or complex predictor. They use one extra pair of Mellin fibers for a translated source and the verified norms of the physical prefixes.

## Boundary weights for a translated column

Use the real symmetric Paley operator \(K\) on the full group \(G=\widehat Q\), with \(K^2=I-P_1\), where \(P_1\) is averaging. Let the branch \(V_j(t)\) be the physical nine-center row and set \(D_j=\operatorname{diag}(\Phi_t'(V_j(t)))\). Here \(t_0=n\) and \(t_i=t\) off zero, as in [round 88](astra-source-88.md#the-seed-centered-disks-on-the-complex-square). The translated Jacobi column \(K e_x\) is, up to a scalar of modulus \(\sqrt p/n\), the lift-average Mellin trace of the actual rank-one Jacobi object with a Kummer twist. If \(\xi\) is a full lift of \(x\) or its inverse according to the Fourier convention, its possible boundary characters lie in \(\{\xi,\chi\xi\}\). The averages over the two lifts are included in the coefficients. Its ordinary tame inertia at one is still of negative type. [Mellin parity and bounded exceptional sets](iteration-parity.md#uniform-fixed-expression-trace-estimates)

The unmarked multiplier \(D_j\) is represented by the odd analytic expansion in the physical negative fields used in [round 82](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative). The raw activation uses a distinct expression only at zero. Because the coefficients of the odd words are collected before taking absolute values, use the same positive symmetric pre-transport weight majorant \(\mu\) as for the round-82 scalar packet bound. Its weights in the base pair of fibers \(\{1,\chi\}\) have finite absolute first moment, and its mass equals the corresponding upper on the sum of absolute coefficients times convolution dimension. Outside the base pair each geometric word has only zero weights. The odd word multiplied by one negative column is of positive type before the \(\chi(1-u)\) twist, by the even-product rule. This conclusion uses the original odd word expansion even if its intermediate convolution lacks a one-sign inertia description on its own. [Two base fibers and transport](astra-feedback-52.md#reading-rank-from-two-mellin-characters) · [Arithmetic exceptional column](marked-domain-53.md#the-exceptional-character-stays-at-the-mark)

At every further step the boundary set of a column term is contained in the union of the base pair and the added pair. For each fixed Mellin twist, the fiber weights add under convolution. At any character outside the union both inputs have only zero weights, so no new boundary character can occur by [Katz's fiber theorem](https://web.math.princeton.edu/~nmk/mellin331.pdf). Transport by \(K\) preserves the negative weights of the generic positive input and swaps the positive weights between the two fibers in each pair. The punctual part dies. Each resulting negative term has convolution dimension equal to its generic rank.

Use the fixed round-82 price \(\pi(|w|)\), with \(\pi(0)=0\), \(k\le\pi(k)\le2k\) and eventual slope \(l\in(1,2)\). For a negative term \(H\) of dimension \(r\), let \(h_k\) be the number of its pooled base weights of absolute value \(k\), \(k>0\), counting the two fibers with half weight each. Let \(b_H\) be the absolute first moment of its weights on the other pair, again with half weights. The negative-term rank identity now reads \(r=\sum_{k>0}k h_k+b_H\): it sums the block lengths at both boundary points with half weights. The multiplicity of zero in the base pair is exactly \(\sum_{k>0}(k-1)h_k+b_H\). When the two pairs coincide set \(b_H=0\). Assign to this term the price
\[
                    P_\Lambda(H)=\sum_{k>0}\pi(k)h_k+\Lambda b_H,
                    \qquad \Lambda\ge1 .                            \tag{1}
\]
It is at least \(r\), so the absolute-coefficient sum of these prices bounds the coordinate sup norm by the compact-support Mellin trace bound. Take the infimum over finite representations and use their closure in each finite field. Boundary symmetry of \(H\) is unnecessary: a symmetric dominating multiplier measure charges \(+k\) and \(-k\) equally.

## The two estimates for one physical derivative step

For the multiplier majorant let \(m=\int d\mu\), \(\nu=\int\pi(|w|)d\mu(w)\). An input of base price \(A=\sum\pi(k)h_k\) and off-base first moment \(b=b_H\) has geometric output bounded by
\[
                A'\le q A+\nu b,\qquad b'\le m b .                   \tag{2}
\]
Indeed the part \(\sum(k-1)h_k\) of its base zeros and the atoms at \(\pm k\) have exactly the original round-82 packet bound \(q\), obtained from the supremum of the column prices over \(k\ge1\). The extra \(b\) zeros in the base fibers each cost \(\nu\) after multiplying by the multiplier. In the other fibers the multiplier is all zero weights, so their absolute first moment is simply multiplied by at most \(m\). These statements are preserved by the ordinary twist and the cosine-symmetric comparison. Product terms before transport with both independent quadratic lifts exchange the two fibers inside each pair, so the two pairwise pooled calculations are valid. In particular \(m+\nu/l\le q\) by taking the limit of the original affine-price column formula as \(k\to\infty\), using the finite first moment to pass to the limit. Thus \(m\le q\) and \(\nu\le 2q\).

For the actual finite-field operator one must also restore the products at the bad Mellin characters. There are at most two cyclic coordinates, namely the two quotients of the boundary pairs (zero and the translated source, with the sign convention chosen by the seed). On any one of these coordinates the product error of two single objects is at most twice the product of their convolution dimensions by the compact-support dimension estimate. After \(K\), these errors are multiples of \(K e_0\) and \(K e_x\), whose prices are at most \(\Lambda\sqrt p/n\) per unit coefficient. The marked-only activation derivative has the same form with source zero. This costs \(O_\Lambda(n^{-1/2})(A+\Lambda b)\) in (2), uniformly in the source and in the floor. To see the uniformity with the analytic multiplier, first apply the estimate termwise to finite sums, then sum the absolute coefficient times dimension bound for the multiplier's analytic tail from round 82. The analytic expansion has strict radius margin on the actual bounded prefix. The marked-only coefficient difference is bounded because both real-marked and unmarked bulk derivative formulas are bounded at \(V_{j,0}\). Geometry, ordinary twist, and application of the exact correction preserve the boundary union, so the estimate iterates indefinitely. No fixed-height error is accumulated in the trace-to-vector identification.

In particular the operator \(K D_j\) has price rate at most
\[
                     q+2q/\Lambda+O_\Lambda(n^{-1/2}).               \tag{3}
\]
All bounds concern the exact finite-prime matrices once \(n\) is sufficiently large. The threshold is uniform in the translated coordinate and may depend on \(\Lambda\). Taking the closure of the norm balls is legitimate because the ordinary finite-field matrix is continuous and the tail estimates are absolutely summable.

## Consequences for the full linearized inverse

At height 250 use \(q<0.996682\) and \(\Lambda=1000\). Then (3) is strictly less than one for all sufficiently large eligible primes. The marked-column Neumann expansion from each translated seed therefore gives
\[
                    \max_{i,x}|[(I-KD_{250})^{-1}K]_{ix}|\ll n^{-1/2} . \tag{4}
\]
For every height with \(q<1\), the triangular form (2) also yields an explicit asymptotic constant. Use \(\Lambda=1\) in the exceptional bounds, so the nonnegative comparison matrix for \((A,b)\) differs from \(\left(\begin{smallmatrix}q&\nu\\0&m\end{smallmatrix}\right)\) by \(O(n^{-1/2})\) entrywise. Its resolvent remains bounded uniformly because \(m\le q<1\) and \(\nu\le2q\). For the unshifted seed the limiting price sum per unit Jacobi coefficient is at most \(1/(1-q)\). For a distinct source the initial vector is \((0,1)\), and the price sum is at most
\[
   \frac{1+\nu/(1-q)}{1-m}
   \le \frac{l}{1-q}+\frac{1-l}{1-m}
   \le \frac{2}{1-q}-1 .
\]
The uniform finite-field perturbation of the comparison matrix tends to zero, so after multiplying by \(\sqrt{p/n}\) these are limsup bounds on \(\sqrt n\) times each entry. In particular, with the height-100 rate \(q<0.984138\), the limsup of the full maximum scaled by \(\sqrt n\) is below 178. The limsup for the marked source alone at that height is below 90. If \(t\) is real, the real reference reflection is \(M(I-KD_j)^{-1}K M-D_j\) for \(M=\sqrt{I-D_j^2}\), by [the symmetric response formula](response-locality.md). Its off-diagonal entries obey the same bounds.

At height 600 round 82 gives \(q<1.046434\). With \(\Lambda=5000\) the rate in (3) is less than \(1.048\) eventually. Independently \(\|KD_{600}\|_{2\to2}<0.514\) by the actual derivative bound in round 88. The first \(h\) terms of the Neumann expansion on \(K e_x\) are bounded at every coordinate by \(C n^{-1/2}(1.048)^h\). The remaining terms are bounded in counting second norm by \((0.514)^h/(1-0.514)\), since \(\|K e_x\|_2\le1\). Balancing the bounds by \(h=\lfloor(\log n)/(2\log(1.048/0.514))\rfloor\) gives
\[
                        \max_{i,x}|[(I-KD_{600})^{-1}K]_{ix}|\ll n^{-0.467} . \tag{5}
\]
The exponents and strict margins follow from the [arithmetic replay](shifted-resolvent-96-check.py). The small-prime part of a maximal-entry estimate on a tube requires a separate resolvent existence check; (4) and (5) are sufficiently-large-prime estimates on the fixed nominated square.

An immediate stability test concerns a diagonal perturbation \(E\) supported on any set \(B\). Write \(R=(I-KD_j)^{-1}K\) and \(r_n=\max |R_{ix}|\). If \(r_n\sum_{i\in B}|E_i|<1\), then \(I-K(D_j+E)\) is invertible and its transported inverse has maximal entry at most \(r_n/(1-r_n\sum_B|E_i|)\). Factor the matrix by \(I-KD_j\), restrict the resulting \(I-RE\) to \(B\), and sum its contraction in the counting supremum norm. Thus bounded perturbations on arbitrary \(o(\sqrt n)\) sites at height 250 and on arbitrary \(o(n^{0.467})\) sites at height 600 cannot produce a singularity within this linear comparison. This includes field-dependent supports; the predictor diagonal itself remains fixed outside the support.

At a first activation of the uniquely selected near-flat comparison, the [real signed forcing test](astra-count-96.md) uses the same height-100 reference reflection. If \(i\) is a first-hit coordinate and \(X=\sqrt{3B}\,J_w e_0\) its actual midpoint column, this test strips the mark and the hitting site from the sum of \(R_{ij}^\mathrm{ref}\sinh(\gamma_j-g_{100,j})X_j\). The new diagonal bound \(\lvert R_{ii}^\mathrm{ref}\rvert\le\lvert D_{100,ii}\rvert+178/\sqrt n\) raises its signed lower bound from \(4.89\cdot10^{-5}\) to \(7.648\cdot10^{-5}\) eventually. Applying the off-diagonal bound to that sum gives the untransformed exterior preimage counting first norm
\[
   \sum_{j\notin\{0,i\}}\big|\sinh(\gamma_j-g_{100,j})X_j\big|
                >4.296\cdot10^{-7}\sqrt n .                           \tag{6}
\]
This holds for all sufficiently large eligible primes at any such first hit. A bounded number of contributions with bounded amplitudes cannot pay this cost. The actual upper remains open, and the first hit here is the near-flat comparison's activation.

1. Attempt the same shifted-column analysis on a genuinely updated reference with geometric preimage price below one, and measure the weighted remainder on the physical high sites. The current comparison does not show that the true stationary diagonal differs from this reference only on the allowed small support.
2. In the count test, use the translated resolvent as the reference for the two real endpoint columns and keep the contribution on the actual exceptional sites separate. To reach the rest of the diagonal one needs structured control or stronger smallness there; a field-first normalized residual with a fixed positive bound alone permits support larger than (4) or (5) can absorb.
