# Translated opposite amplitude tails on the physical cold forcing line

At any two available heights and floors in the enlarged cold phase sector, the positive amplitude tail of the first actual forced row and the negative amplitude tail of the second have small weighted overlap at **every** frequency translate. The cost is quadratic in the two actual height-600 residuals and is uniform over primes. This includes comparison to the true unforced real row. Independently, a singular right-angle spread contact requires every prime divisor of the cyclic order to have cofactor larger than \(5.2\cdot10^{345}\). This excludes contacts of every corank at all eligible orders satisfying the cofactor test, without an upper cutoff on the order. A quadratic imaginary-floor estimate also keeps the entire forcing path strictly inside the unit-derivative phase chamber on an explicit order-dependent strip.

## Two physical rows and an arbitrary translate

Let \(p=2n+1\equiv1\pmod4\) be prime, \(n\ge10^{30}\), and take floors in the closed square of half-width \(2^{-17}\) about \(2031/128\). At a floor \(t\) write \(X=V_{600}(t)\), \(R=K\Phi_t(X)-X\), \(r=\|R\|_{2,n}\), \(q=1-\lambda\), \(0\le\lambda\le1\), \(h=\lambda r\). Use any available point of the actual forcing line in \(|\phi_i|\le\arctan(3/2)\), with the continuous logarithms \(z_i=\rho_i+i\phi_i\). Write \(A_i=\sqrt{t_i}e^{z_i}\), \(B_i=\sqrt{t_i}e^{-z_i}\), and use normalized counting \(E\). The root has \(t_0=n\), the bulk \(t_i=t\). For two such choices at the same prime use superscripts \(1,2\) and residual costs \(h_1,h_2\). Define bulk profiles, extended by zero at the mark, by
\[
 P_i^{(j)}=(2.20 e^{\rho_i^{(j)}}-7.1)_+,\qquad
 N_i^{(j)}=(2.20 e^{-\rho_i^{(j)}}-7.1)_+.
\]
Then on the cyclic frequency group, for **every** translate \(k\),
\[
                 E_i P_i^{(1)} N_{i-k}^{(2)}
                         \le 13000(h_1^2+h_2^2).                    \tag{1}
\]
In particular the average of \(e^{\rho_i^{(1)}-\rho_{i-k}^{(2)}}\) on the overlap where both individual factors exceed 10, with the average divided by the full \(n\), is at most the same right side. The floors, remaining forcing parameters, and translate can be chosen after seeing the two profiles. At a real second floor the positive stationary branch at \(\lambda_2=1\) is available for every field in range. [Reality and continuation on the real segment](phase-action-84.md) · [Actual predictor and residual](astra-source-88.md)

To prove (1), first consider just one row. Set \(\Delta=U-X\), \(G=\{|\Delta_i|\le1\}\), \(T=G^c\). The physical secant gives
\[
 E1_G|\Delta|^2+E1_T|\Delta|\le870h^2,\qquad
 \Delta=K M\Delta+\lambda R,\qquad \|M\|_\infty\le1 .
\]
Here \(M_i=\tanh((z_i+z_i^{X})/2)\), including coincident coordinates. Each Jacobi row has counting second norm at most one and each entry has modulus at most \(\sqrt p/n\). Applying these two bounds to \(G,T\) respectively, then using \(\|R\|_\infty\le\sqrt n r\), gives
\[
           \|\Delta\|_\infty\le (1+\sqrt{870})\sqrt n h
                              +870\sqrt p\,h^2<31\sqrt n h            \tag{2}
\]
when \(h>0\). The last step uses the finite-prime bound \(r<3.932\cdot10^{-175}\). All zero-cost cases below follow with the non-strict zero bounds. [Enlarged-sector secant](astra-imaginary-84.md#large-derivatives-at-height-600-beyond-unit-phase) · [Seed-centered residual](astra-source-88.md)

The completed factors are \(A^c=A+qR/2, B^c=B-qR/2\). Let \(a',b'\) be the real parts of their differences from the two completed factors at \((X,\lambda=0)\). Their nonconstant components lie in the respective plus and minus sectors. The exact scalar secant gives
\[
 a'=\Re[((M+1)\Delta-\lambda R)/2],\qquad
 b'=\Re[((M-1)\Delta+\lambda R)/2].
\]
Thus each modulus is bounded by \(w=|\Delta|+\lambda |R|/2\), with \(w_0<31.5\sqrt n h\) for \(h>0\). The mark could have a large negative discrepancy, so remove it on each side. Use \(J\) for the constant projector, \(e_0\) for the mark, and put
\[
 k_\sigma=\frac{(I-J+\sigma K)e_0}{1-1/n+\sigma K_{00}},\qquad
 a=a'-a'_0 k_+,\qquad b=b'-b'_0 k_- .
\]
The identity \(K^2=I-J\) puts \(k_\sigma\) in the corresponding mean-zero sector. It is one at the mark and has modulus below \(1.42/\sqrt n\) on the bulk by the Jacobi entry bound and the lower bound on \(n\). Hence the correction on the bulk costs less than \(45h\) on either side.

On the bulk, the uncompleted factors at \(X\) have modulus at most \(1.77\sqrt{|t|}\). The two true factors have positive real parts bounded below by \(2.20e^{\rho_i}\) and \(2.20e^{-\rho_i}\), since \(|\arg\sqrt t|<10^{-6}\) and \(\sqrt{|t|}\cos(\arctan(3/2)+10^{-6})>2.20\). With \(\|R\|_\infty<0.011\) this gives \(a_i\ge 2.20e^{\rho_i}-7.1\) and \(b_i\ge2.20e^{-\rho_i}-7.1\). Both corrected rows vanish at zero. Thus \(a_+\ge P, b_+\ge N\), and both negative parts have sup norm at most 7.1. For either corrected row \(v\),
\[
 \|1_Gv\|_{2,n}\le76h,\quad \|1_Gv\|_\infty\le1.01,\quad
 E1_T|v|\le875h^2,\quad |Ev|\le77h .                              \tag{3}
\]
The first two inequalities use \(w+45h\) off zero. For the third use \(P(T)\le870h^2\) and the same upper, with \(\lambda |R_i|/2\le0.0055\). These estimates also show where the true residual enters the tail price. [Predictor log cap](phase-action-84.md#exact-secant-comparison-in-logarithmic-coordinates)

Translation preserves each Fourier sector. Consequently \(E_i a_i^{(1)} b_{i-k}^{(2)}=(Ea^{(1)})(Eb^{(2)})\) even for different floors. To bound the negative products, the two good-coordinate sets together cost at most \(76^2 h_1 h_2\) by Cauchy–Schwarz. When exactly one coordinate is in its tail, the good entry costs at most 1.01 times the modulus of the tail entry. When both are in their tails, any negative product has modulus at most 7.1 times the sum of their moduli. Integrating the latter two bounds costs at most \((1.01+7.1)875(h_1^2+h_2^2)\). The positive-positive contribution is bounded by the absolute product of means plus this negative budget. Apply (3) and \(2h_1h_2\le h_1^2+h_2^2\) to obtain (1).

For a balanced ramified first contact, [the two actual tail sets](astra-source-88.md#the-two-delocalized-tails) each contain more than \(n/(2\sqrt p)\) sites with \(e^{\pm\rho_i}>224/q\). Calling them \(T_+,T_-\), (1) forces, at every translate,
\[
 \frac{|T_+\cap(k+T_-)|}{n}
    <\frac{26000\lambda^2 r^2}{(2.20\cdot224/q-7.1)^2}.             \tag{4}
\]
On the inner half-square one factor in the denominator can be replaced by \(2.20\max(224,0.0004735/|\Im t|)/q-7.1\) when the larger-threshold tail from round 88 is used on that side. Formula (1) applies to all active-count ratios and to regular sector exits as well. The lower sizes alone allow small overlaps, so (4) does not exclude such a contact at arbitrary primes.

## Prime divisors of the cyclic order at a singular contact

Let \(S\) comprise the two bulk phase extremes at a contact of spread \(\pi/2\) on the same enlarged-sector line. Suppose the full physical Jacobian is singular. Its two complementary nonzero eigenrows are supported on \(S\). The genuine predictor loss at each extreme exceeds 2.4, and the two eigenvalues in the compression give
\[
        \sqrt2/\sqrt p\le |S|/n< (870/2.4)h^2 .                     \tag{5}
\]
This uses no assumption on corank, parity, ramification or the active counts. [Contact rotation](relative-phase-rotation-85.md#exact-rotation-of-the-linear-problem) · [Extreme-site loss](astra-source-88.md#an-all-corank-finite-prime-exclusion-on-the-forced-line)

Let \(\ell\mid n\) be prime, and work on the positional subgroup \(H\) of order \(\ell\) inside the quadratic residues. A nonzero mean-zero \(\sigma\)-eigenrow \(f\) supported on \(S\) has a positional inverse transform supported on \(D_\sigma=\{x:\chi(1-x)=\sigma\}\). Select a coset \(C=bH\) where that transform is nonzero. Its restriction is the transform on \(H\) of the coefficients of \(f\) folded modulo \(\ell\), with the phases from \(b\) retained before folding. This permits cancellations and signed coefficients. The folded support has at most \(|S\bmod\ell|\) entries. On the other hand, the restriction vanishes on at least \((\ell-\sqrt p)/2\) points. Indeed
\[
  |C\setminus D_\sigma|
     =\tfrac12\big(\ell+1_C(1)-\sigma\sum_{x\in C}\chi(1-x)\big).
\]
Expanding the coset indicator in the multiplicative characters trivial on \(H\) expresses its character sum as a unit-weighted average of complete Jacobi sums, each bounded by \(\sqrt p\). Prime cyclic uncertainty on \(H\) now yields
\[
 |S|\ge |S\bmod\ell|\ge1+(\ell-\sqrt p)/2 .
\]
This extends the earlier anchored nonnegative restriction argument to the signed null rows by allowing every positional coset. [Jacobi convention](fourier.md) · [Anchored subgroup estimate](parallel-kernel-11.md#a-density-bound-from-a-large-prime-factor-of-the-cyclic-order) · [Tao, Theorem 1.1](https://arxiv.org/abs/math/0308286)

Since \((\sqrt p-2)/n<2/\sqrt p\), (5) gives the necessary cofactor bound
\[
          \frac{\ell}{n}<(2+\sqrt2)\frac{870}{2.4}\,\lambda^2r^2 .
                                                                         \tag{6}
\]
In particular **no singular spread contact occurs at any eligible field with \(n\ge10^{30}\) and \(n/\ell\le5.2\cdot10^{345}\) for some prime divisor \(\ell\)**. Using the field-first uniform residual limsup \(<3.06\cdot10^{-208}\) gives the same exclusion for cofactor at most \(8.6\cdot10^{411}\) at sufficiently large eligible orders, with no effective starting order claimed for this second version. Neither exclusion assumes that primes satisfying a fixed cofactor bound exist at arbitrarily large orders. Regular spread crossing and subsequent exit or singularity remain possible. [Field-first residual rate](astra-dissipation-80.md)

## An absolute-sector exit bound with a quadratic imaginary-floor factor

Put \(L=2031/128-2^{-17}\), \(\eta=|\Im t|\) and \(r_*=3.932\cdot10^{-175}\). For every \(n\ge10^{30}\) on the concentric half-square, at any available forcing point in the enlarged sector,
\[
 Y=E|t_i|\sin^2\phi_i\le\eta^2
                  (0.032+5\cdot10^{10}\sqrt n\,r_*^3).                \tag{7}
\]
In particular the entire real forcing segment from \(X\) to the genuine stationary point exists with \(\max_i|\phi_i|<\pi/4\) whenever
\[
              n\eta^2(0.032+5\cdot10^{10}\sqrt n\,r_*^3)<L/2 .        \tag{8}
\]
This supplies an explicit shrinking strip through the cold center at unbounded orders, for the forced path itself. Using only the real slice of that path to identify its endpoint gives the physical stationary section there. The unforced phase identity already gives an order-\(n^{-1/2}\) strip for the germ started directly on the real slice; (8) concerns every intermediate forcing height.

Write \(b_i=\Im R_i\), \(u_i=\Im U_i\), and set \(b=2872\), \(c=1.031\cdot10^{-169}\). Reality on the real slice, the outward sup record, and the residual counting bound on the outer square give \(\|b_i\|_\infty\le b\eta\), \(\|b_i\|_{2,n}\le c\eta\). For the second use Cauchy on disks with radius tending to \(2^{-18}\) about the vertical integration segment, in normalized counting norm. The unrotated physical imaginary-part identity gives
\[
                Y\le\eta^2/(4L)+qE|b_i u_i|/2 .
\]
In fact the deterministic bulk term is at most \(|t|\sin^2(\arg(t)/2)\le\eta^2/(4L)\), and the mark has real floor. [Imaginary-part identity](astra-imaginary-84.md#a-conjugate-phase-identity-up-to-and-beyond-the-unit-derivative-threshold) · [Physical source derivative](astra-forced-87.md#the-residual-perpendicular-to-a-line)

For \(\tau_i=|t_i|\), the formula \(U_i=2\sqrt{t_i}\sinh z_i\) gives
\[
 |u_i|\le \sqrt{4+|U_i|^2/\tau_i}\,\sqrt{\tau_i}|\sin\phi_i|
                  + \eta |U_i|/(2L).
\]
Indeed \(2\sqrt{\tau_i}\cosh\rho_i\le\sqrt{4\tau_i+|U_i|^2}\), and the explicit floor rotation in the other term acts only in the bulk. The square-root coefficient is at most 2.5 on \(G\), and on \(T\) it is at most \(3.46|\Delta_i|\), since \(|U_i|\le5.768|\Delta_i|\) there. Equation (2) and the first-norm tail price imply
\[
 E1_T|\Delta|^2\le870\cdot31\sqrt n\,h^3.
\]
Hence Cauchy–Schwarz bounds \(E|b_i u_i|\) by
\[
 \eta A\sqrt Y+\eta^2 D/(2L),\qquad
 A=2.5c+3.46 b\sqrt{870\cdot31\sqrt n\,h^3},\quad
 D=5.768(c+870b h^2).
\]
Applying Young's inequality gives
\[
 Y\le\eta^2\big((1+qD)/(2L)+q^2 A^2/4\big)
 \le\eta^2(0.032+1.4\cdot10^{12}\sqrt n\,q^2\lambda^3r^3).
\]
Use \(\max_{[0,1]}(1-\lambda)^2\lambda^3=108/3125\) to conclude (7).

The initial predictor has \(\max_i|\phi_i|<0.26\). If its forcing path first reached an absolute phase \(\pi/4\) in magnitude, this single site would give \(Y\ge L/(2n)\), contrary to (8). For a fixed field (2) bounds every coordinate, and inside this phase chamber \(\|\operatorname{diag}\tanh z\|<1\) gives local implicit continuation. More precisely, (8) gives a strict phase margin and (2) a finite amplitude cap even at every cluster point on a maximal segment; the Jacobian stays invertible on this compact set. The continuation reaches \(\lambda=1\), and implicit neighborhoods along its compact segment give local holomorphic dependence on \(t\) there. The branch selected by this path is continuous from the real stationary solution throughout the strip. No positive common width follows from (8).

1. Test signed concentration of the two contact eigenrows on shifts of the actual two opposite tails. A lower on one of their weighted shifted overlaps exceeding (1) would exclude the corresponding physical ramification. Inputs from both eigenrows would be needed to improve the counting lower given solely by the two tail sizes.
2. For orders with large cofactor for every prime divisor, seek a support lower for the joint plus and minus nulls in (5) by combining several positional restrictions, or use their actual shifts in (1). No common cold square through all eligible primes or ordinary-theta asymptotic follows from the present estimates.

The [exact rational replay](astra-tails-89-check.py) checks the constants and a finite coset-restriction instance. [Replay records](astra-tails-89-checks.jsonl)
