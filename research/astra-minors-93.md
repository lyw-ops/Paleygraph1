# Exterior Fourier minors at a first tie and a physical obstruction at large real floors

At a first tie, a signed test on exterior Fourier minors is necessary in both sectors. The bound entering the test is sharp over the two omitted row scales. At the nominated real floor \(2031/128\), an all-profile column upper would force two unaveraged opposite-sector interpolation errors to total at most \(4\cdot10^{-208}\) on one genuine pair with prescribed marked factors. At every sufficiently large fixed real floor, genuine positive stationary pairs with exactly the prescribed extensive mark and bulk products within \(\epsilon\) of one can have marked-column entries of order \(\epsilon\), uniformly through primes. This includes widths tending to zero more slowly than \(1/\sqrt n\). At the nominated floor, the same two-center perturbation has order-one first derivative at prime 173. The upper bound for its profile selected by first contact is open. [Real first-contact criterion](astra-velocity-92.md)

## A signed test after deleting two rows

Use full cyclic counting, \(p=2n+1\equiv1\bmod4\) prime, and the physical positive equal-mean pair \((P,Q)\) with \(w=PQ,\ \nu=\sqrt w,\ g=\frac12\log(P/Q)\). Fix \(s=\pm1\), a real orthonormal basis matrix \(V\) for the mean-zero native sector \(H_s\), and a bulk site \(i\). Write \(u_j\) for the transposed row of \(V\). Insert the physical squared row multipliers \(t_j=e^{-2s g_j}\) at \(j\notin\{0,i\}\) and form
\[
 D=\sum_{j\ne0,i}t_j u_j u_j^{\mathsf T},\qquad
 a=u_0^{\mathsf T}D^{-1}u_0,\quad b=u_i^{\mathsf T}D^{-1}u_i,\quad
 d_{si}=u_i^{\mathsf T}D^{-1}u_0.
\]
For all sufficiently large \(p\), the native two-row projector compression has both eigenvalues \(1/2+O(n^{-1/2})\), uniformly in \(i\), by the diagonal formula and the Jacobi entry bound. Thus its two rows are linearly independent, and no native sector vector can be supported on just \(0,i\). This gives invertible \(D\) for all positive exterior tilts. Set
\[
 R_{si}=1-d_{si}^2/(ab),\qquad
 U_{si}=\sqrt{\frac{1-\sqrt{R_{si}}}{1+\sqrt{R_{si}}}},\qquad
 0<R_{si}\le1 .
\]
For any positive squared row multipliers \(x,y\) inserted at \(0,i\), the weighted orthogonal projector satisfies
\[
 \Pi_{si0}(x,y)=
 \frac{\sqrt{xy}\,d_{si}}{1+xa+yb+xy(ab-d_{si}^2)},\qquad
 \sup_{x,y>0}|\Pi_{si0}(x,y)|=\tfrac12 U_{si}.                    \tag{1}
\]
The first identity follows by the two-row inverse formula. Divide the denominator by \(\sqrt{xy}\) and apply AM–GM separately to the first and last terms and to the middle two. The choice \(xa=yb=R_{si}^{-1/2}\) attains the bound. The sign is fixed by \(d_{si}\) for every scaling. Collect the weighted squared Fourier minors according to inclusion of neither, just zero, just \(i\), or both, before inserting those two multipliers. Their totals are \(\det D\) times \(1,a,b,ab-d_{si}^2\). Thus \(R_{si}\) is their cross ratio, neither times both divided by the other two. The signed quantity \(d_{si}\det D\) is the sum of products of the two minors with common weighted exterior rows and the respective unscaled row \(0\) or \(i\) appended last. Add the rank-one update from \(u_0+z u_i\) to \(D\) and compare coefficients linear in \(z\) in Cauchy–Binet.

At a first cold tie take the actual real mark \(r\), selected profile \(k'\), labels \(\sigma_i,\eta\), and probability \(\lambda\) from round 92, with \(e=1-10^{-8}\). At that same real mark one has
\[
 \boxed{\quad
 \sqrt n\sum_{\eta \sigma_i s d_{si}>0}\lambda_i U_{si}
 >956-\sqrt n\,\frac{r\sqrt e}{W}>955.4,\qquad s=+1,-1 .\quad}     \tag{2}
\]
Indeed \(J_{i0}=s(2\Pi_{si0}+r\sqrt e/W)\) on the selected sites. Apply the oriented column lower bound, then discard the nonpositive terms and use (1). Since \(W\ge r^2+(n-1)e\), the subtracted amount is at most \(\tfrac12\sqrt{n/(n-1)}<0.6\) for \(n\ge4\). Cauchy–Schwarz before optimizing the multipliers also gives \(-n\sum_i\lambda_i\operatorname{Cov}_s(I_i,I_0)>(955.4)^2/4>228{,}000\) for the actual determinantal law in each sector. Only the other coordinates' amplitudes enter each term of (2). [Signed physical lower bound](astra-velocity-92.md#quantitative-arithmetic-tests)

## A two-center perturbation at fixed extensive mark

There are absolute constants \(c_*>0,T_*<\infty\) with the following property. Fix \(T\ge T_*\). For every sufficiently large eligible prime and every \(0<\epsilon\le10^{-8}\), there is a genuine even positive stationary pair with
\[
 w_0=n/T,\qquad 1-\epsilon<w_i<1\quad(i\ne0),\qquad
 |J_{h0}|\ge c_*\epsilon,\qquad h=n/2 .                            \tag{3}
\]
Whenever \(\sqrt n\,\epsilon_p\to\infty\), this same pair has \(-n\operatorname{Cov}_s(I_h,I_0)\to\infty\) for both signs, since \(\nu_h\nu_0/W=O_T(n^{-1/2})\). Even an all-profile bound with numerical constant 956 fails at those extensive marks. The profiles in (3) are free to vary in the box. No origin at complex contact is asserted.

Write \(K\) for the native Jacobi reflection, \(X_j=\sqrt n K_{j0}\), and \(H_j=X_jX_{j-h}\). Put \(F=H-EH=H+1/n\), since \(K^2=I-\mathbf1\mathbf1^{\mathsf T}/n\). Both \(F\) and \(KF\) are even, mean zero, and uniformly bounded. In detail \(\|H\|_\infty\le p/n\). For \(k(j)=\sqrt{n/p}X_j\), the counting mean of a product of at most four translates differs by \(O(p^{-1/2})\) from that for independent Haar cosines at distinct centers, with repeated centers identified. A translated \(k\) at a good full character is a real part of a Gauss quotient with the center's two quadratic twists. Different centers have disjoint twist pairs. Expand each cosine, combine repeated exponents, and apply Katz's Gauss moment bound to every nonconstant monomial. The bounded number of exceptional lifts costs \(O(1/p)\). An odd product of three cosines has zero Haar mean, including all collisions. Hence uniformly in \(j\),
\[
 (KF)_j=\sqrt p\,(p/n)\,E_\ell k(j-\ell)k(\ell)k(\ell-h)=O(1).
\]
The fourth moment uses two distinct centers, giving
\[
 (K\operatorname{diag}(F)K)_{h0}
  =E(HF)=(p/n)^2(1/4+O(p^{-1/2}))-(EH)^2=1+o(1).                 \tag{4}
\]
Also \(F_0=O(n^{-1/2})\), since \(K_{00}=-1/n\). [Shift-uniform moment proof](entropy-heads-81.md#an-exponential-comparison-for-weighted-translates) · [Katz, §§9.5–9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf#page=84)

Put \(c=\sqrt{1-\epsilon/2}\). Take the actual real pair \(A,B\) with bulk product \(c^2\) and marked product \(n/T\). The hot stationary estimate \(\sqrt n\|\widetilde A-\widetilde B\|_\infty\le6\) for marked product one and bulk \(c^2T/n\), rescaled by \(\sqrt{n/T}\), gives \(\|A-B\|_\infty\le6/\sqrt T\) once \(n\ge T,\ c^2T\ge1024\). Thus \(\|g(0)\|_\infty=O(T^{-1/2})\), by the inverse hyperbolic sine formula at every site, and both bulk factors are \(c+O(T^{-1/2})\), uniformly in \(\epsilon\). [Uniform large-floor arithmetic bound](astra-hardtail-33.md#11-input-from-the-existing-hot-argument)

For \(s=\pm1\) let \(\kappa_s=\Pi_s^{\rm native}e_0/(\Pi_s^{\rm native})_{00}\). This row equals one at the mark and is \(O(n^{-1/2})\) everywhere else. Define
\[
 f_s=sF+KF,\qquad v_s=f_s-f_s(0)\kappa_s .
\]
Both \(v_s\in H_s\) exactly, since \(K^2F=F\), and their sup norms are bounded by an absolute constant. Set \(A(t)=A+t v_+\), \(B(t)=B+t v_-\). These are positive equal-mean complementary rows on \(|t|\le b_0\epsilon\) for an absolute sufficiently small \(b_0>0\). Both marks are fixed, the bulk factors stay positive, and bounded slopes give \(|A_i(t)B_i(t)-c^2|<\epsilon/2\) off the mark. The sector equations therefore identify these rows with the positive real stationary optimizers of the new products. Their common mean and total bulk product are constant throughout.

For \(g(t)=\frac12\log(A(t)/B(t))\), uniformly on this interval,
\[
 \|g(t)\|_\infty=O(T^{-1/2}+|t|),\qquad
 \|\dot g(t)-F/c\|_\infty=O(T^{-1/2}+|t|+n^{-1/2}).
\]
For the second estimate use the bulk reciprocals \(1/A_i(t),1/B_i(t)=1/c+O(T^{-1/2}+|t|)\), the bounds on both directions, and \(f_+-f_-=2F\). At the mark \(\dot g_0=0\) and \(F_0=O(n^{-1/2})\). A projector on an \(e^L\)-scaled subspace differs from the initial one by at most \(\|L\|_\infty\) in operator norm, by integrating its off-diagonal block derivative on the linear log interpolation. Thus \(\|J(t)-K\|\le2\|g(t)\|_\infty\). The physical reflection differential now gives
\[
 \partial_t J(t)_{h0}
 =(J(t)\operatorname{diag}(\dot g(t))J(t))_{h0}
 =c^{-1}(K\operatorname{diag}(F)K)_{h0}
                  +O(T^{-1/2}+|t|+n^{-1/2}).                       \tag{5}
\]
All implicit constants are absolute. Choose \(T_*\) large, shrink \(b_0\) once, and take the prime sufficiently large. Equations (4)–(5) give \(\partial_t J(t)_{h0}\ge1/2\) on the entire interval. One of its two endpoints has \(|J_{h0}|\ge b_0\epsilon/2\), proving (3) simultaneously for every allowed width. [Reflection differential](response-locality.md#contraction-and-response-derivative)

## An alternative on the nominated real floor

At \(T=2031/128\), let \(\epsilon=10^{-8}\) and take the same constant-bulk baseline with \(c^2=1-\epsilon/2\). Write \(U_s=\mathbb R\mathbf1+H_s\). For every sufficiently large eligible prime, either some even physical profile at mark \(n/T\) in the open bulk box has \(|J_{h0}|>956/\sqrt n\), or a **single** such positive pair \((A',B')\) satisfies the following two simultaneous approximation requirements. In full counting first norm, put \(l_j=J_{hj}J_{j0}\) using its own reflection. Then
\[
 \operatorname{dist}_1(l/A',\,U_-+\mathbb R e_0)
 +\operatorname{dist}_1(l/B',\,U_++\mathbb R e_0)
 \ \le\ 4\cdot10^{-208}.                                               \tag{6}
\]
Both marked factors and both means of this pair equal those of the baseline. This alternative addresses a bound on the entire near-flat box. A large column for some freely chosen profile does not decide the first-contact test on its specific profile.

To prove (6), put \(\tau=c^2T\) and use the actual normalized counting residual \(r_p\) at \(V_{600}(\tau)\). The shifted real floor lies inside the nominated square since \(T\epsilon/2<2^{-17}\). The physical discrepancy estimate on the real unforced branch gives \(\|U-V_{600}\|_\infty\le31\sqrt n\,r_p\), in the convention that the raw real difference \(U\) has factor products \(\tau\) in the bulk and \(n\) at the mark. The prefix bound is \(\|V_{600}\|_\infty<4.768\). The field-first real contraction yields \(\limsup r_p\le4(0.428236)^{600}<4.1\cdot10^{-221}\). After dividing both raw factors by \(\sqrt T\), the baseline obeys
\[
 \max_{j\ne0}(A_j+B_j)
 \le 2c+(4.768+31\sqrt n\,r_p)/\sqrt T <4+8\sqrt n\,r_p.
\]
[Real-branch sup discrepancy, equation (2)](astra-tails-89.md#two-physical-rows-and-an-arbitrary-translate) · [Real residual input](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) · [Field-first contraction](astra-dissipation-80.md#explicit-logarithmic-height-field-comparison-for-the-leading-coefficients)

Let \(X_s\) be the even subspace of \(H_s\) vanishing at the mark. Use the maximum of the two sup norms on \(X_+\times X_-\). For \(M=10^{211}\), the entire closed ball of radius \(R=M/\sqrt n\) consists of admissible perturbations \((A+x,B+y)\) for all sufficiently large \(p\). The bulk product deviation is at most \(R(4+8\sqrt n\,r_p)+R^2\), whose limsup is at most \(8M\limsup r_p<3.28\cdot10^{-9}<\epsilon/2\). Both factors stay positive by continuity on the connected ball and strict positivity of the products. The marks and means are unchanged, and every perturbed pair is physical for its own weights.

Assume the first alternative fails. Throughout the ball the smooth function \(f(x,y)=J_{h0}\) has oscillation at most \(1912/\sqrt n\). Maximize \(f(u)-k\|u\|_\infty\) there with \(k=2000/M\). Every boundary value is strictly below the value at zero. At an interior maximizer, testing both directions gives \(|Df(u)[v]|\le k\|v\|_\infty\) for **all** \(v\in X_+\times X_-\) at that same pair. By the reflection differential,
\[
 Df(u)[v]=\tfrac12\sum_j l_j
        \left(v_{+,j}/A'_j-v_{-,j}/B'_j\right).
\]
The norm of a linear functional on a finite-dimensional subspace with inherited sup norm equals its counting \(\ell^1\) distance to the annihilator, by Hahn–Banach. The dual norm on the product adds the two norms. All rows \(l,A',B'\) are even since \(h=n/2\) is fixed by inversion. The annihilator of \(X_s\) consists of \(U_{-s}+\mathbb R e_0\) plus odd rows; evenizing an approximant removes its odd part without increasing the distance. This proves (6) with \(2k=4\cdot10^{-208}\). The same argument works for any fixed even signed bulk probe \(a\) with \(\|a\|_1\le1\) on replacing \(f\) by \(a^{\mathsf T}Je_0\) and \(l\) by \((Ja)\odot(Je_0)\). The resulting pair may depend on the probe.

## Nominated-floor replay and next tests

At \(p=173,\ T=2031/128,\ \epsilon=10^{-8}\), the baseline pair has the exact mark and bulk products above. At its singleton site 43 the two genuine projected entries are \(0.05450686044\ldots\) and \(-0.08025434429\ldots\). The sharp exterior caps in (1) are \(0.05596231546\ldots\) and \(0.08202559986\ldots\). Direct reinsertion of the optimizing multipliers verifies attainment in both sectors. The two physical endpoint profiles at \(t=\pm\epsilon/64\) stay strictly inside the box with the same mark and means. The secant of \(J_{43,0}\) and its exact center derivative are both between \(0.97075232278\) and \(0.97075232279\). This single prime tests the mechanism on the nominated real floor. [Arb checker](astra-minors-93-check.py) · [Outward records](astra-minors-93-checks.jsonl)

1. On the selected profile at a hypothetical cold tie, test the signs and cross ratios in (2) with the two endpoint rows deleted. An upper bound for one sector suffices; the \(\lambda_i\) and individual exterior signs are both available.
2. At the nominated mark, bound the sum of the two opposite-sector interpolation errors in (6) from below on the whole admissible perturbation ball. A lower above its threshold excludes an all-profile 956 bound. The two-center rows in (4) give an explicit dual test; at cold floors the sign and size of its pairing on the full ball remain open.
