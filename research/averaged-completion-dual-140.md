# The exact dual of full and localized averaged completion

Let \(X\in\mathbb R\mathbf1\oplus V_\sigma\) be inversion-even, with mean \(M>0\) and raw marked value \(a=X_0>0\). This includes the [actual projected average](averaged-mark-35.md) in the marked window. Write \(W_\sigma=V_\sigma\cap\{r_0=0\}\), \(\ell=P_\sigma e_0\), and \(k=\mathbf1-\ell/\ell_0\). The row \(k\) preserves the sector, has mean one, and vanishes at zero. For sufficiently large primes it is positive at every bulk coordinate. In fact \(\ell_0=(1-(1+\sigma)/n)/2\) and \(|\ell_i|\le(1+\sqrt p)/(2n)\) on the bulk. All pairings below use normalized counting measure.

For an inversion-symmetric bulk set \(B\) and a uniform raw reserve \(0\le\rho<\min(M,a)\), minimize the additional mean \(\delta\ge0\) over corrections \(r\in W_\sigma\) with \(X+r+\delta k\ge\rho\) at the sites of \(B\). Let \(\theta_{-\sigma}(B)\) be the maximal marked value among nonnegative mean-one opposite-sector rows supported on \(B\cup\{0\}\), defined to be zero when none exists. The exact cost is
\[
 \boxed{\displaystyle
 \delta_B(\rho)=\bigl((a-\rho)\,\theta_{-\sigma}(B)/n-(M-\rho)\bigr)_+.}             \tag{1}
\]
For the full bulk and zero reserve this is \(\bigl(a/\theta_\sigma-M\bigr)_+\) by ordinary reciprocity. In particular, for the unrestricted repair proposed for the actual average, solving the LP just evaluates an ordinary optimum through these two scalars. The spatial profile of the endpoint defect can guide a particular constructive correction, and it supplies no further parameter in this unrestricted value.

For the proof, finite LP duality gives the maximum of \(-\mathbb E[\lambda (X-\rho)]\) over \(\lambda\ge0\) supported on \(B\) with \(\lambda\perp W_\sigma\) and \(\mathbb E(\lambda k)\le1\). The primal is feasible since \(k>0\) on \(B\). Evenness may be imposed by reflection on both sides. The annihilator condition says \(P_\sigma\lambda=\beta\ell\). Put \(F=\lambda-\beta e_0\) and \(m=\mathbb E F\). Then \(F\in\mathbb R\mathbf1\oplus V_{-\sigma}\), \(\mathbb E(\lambda k)=m\) and \(\mathbb E[\lambda(X-\rho)]=m(M-\rho)+\beta(a-\rho)/n\). A strictly positive dual objective has nonzero \(\lambda\), \(m>0\) and \(\beta<0\). Hence \(F/m\) is a nonnegative mean-one opposite row supported on \(B\cup\{0\}\), with marked value \(-\beta/m\). Use \(m\le1\) to obtain the upper bound in (1). Conversely an opposite maximizing row of mean one gives a dual weight after deleting its marked coordinate, with normalization exactly one and objective \((a-\rho)\theta_{-\sigma}(B)/n-(M-\rho)\). The zero dual weight handles the other cases.

Every positive-cost dual witness consequently needs at least \(n/(1+\sqrt p)-1\) bulk sites. Indeed its normalized opposite row satisfies \(0\le F_i\le1+\sqrt p\) from \(KF=-\sigma(F-\mathbf1)\) and \(|K_{ij}|\le\sqrt p/n\). For any prime divisor \(l\) of \(n\), the [subgroup uncertainty test](parallel-kernel-11.md#a-density-bound-from-a-large-prime-factor-of-the-cyclic-order) also gives \(|B|\ge(l-1-\sqrt p)/2\) for such a witness. The nonnegative row supported in \(B\cup\{0\}\) has nonzero pushforward to the characters of the positional subgroup of order \(l\). Prime cyclic uncertainty tests its forbidden positions; the complete Jacobi bound controls the sign count there. A set below either threshold can be given the stated reserve at zero additional mean and exact mark.

## Sites near zero in the actual average

On the genuine projected prefix write \(X/M=U+e\) as in the [pinned reflection calculation](astra-completion-37.md#1-the-reciprocal-rows-charge-large-endpoint-errors-quadratically). The positive time averages satisfy \(\mathbb E U_+=\mathbb E U_-=1\) and \(U_+U_-\ge c/M^2\ge c_\tau>0\) on the bulk at fixed \(\tau\). Here the floor is \(c=\tau/n\). The actual endpoint error satisfies \(\mathbb E e_\sigma^2=O_\tau(T^{-1})\) by \(\|v_{T+1}\|_2^2\le4W(T+1)\), \(nM^2\) bounded away from zero, and the exact opposite-sector endpoint formula. Put \(\rho=M T^{-1/3}\). Every member of \(B=\{i\ne0:X_i\le\rho\}\) has either \(U_i\le 2T^{-1/3}\) or \(|e_i|\ge T^{-1/3}\). The first set has relative size \(O_\tau(T^{-1/3})\) by the reciprocal lower product and mean of the companion, and the second has relative size \(O_\tau(T^{-1/3})\) by the second moment. Thus \(|B|=O_\tau(nT^{-1/3})\).

Along any family where \(n\) has a prime divisor at least \(\eta n\) for fixed \(\eta>0\), this actual set is below the subgroup threshold once \(T\to\infty\). Therefore inside the proved growing marker window the actual near-zero sites in each sector admit a correction to reserve \(M T^{-1/3}\) at zero additional mean and exact mark on such a family. This gives no bound on spill onto the complementary bulk and does not prove global positivity even on that subfamily. A genuinely endpoint-dependent route must bound that spill or control broad dual witnesses. The full-bulk, all-prime cost remains open.

## The signed cost for one explicit repair

There is an all-prime sufficient test at this same reserve scale. Write \(u=T^{-1/3}\), \(Z=X/M\), and \(d_i=(u-Z_i)_+\) on the bulk with \(d_0=0\). From \(Z=U+e\) and the reciprocal bound, \(\mathbb E(1/U)\le c_\tau^{-1}\). The two pointwise estimates
\[
 (u-Z)_+\le(2u-U)_++(-e-u)_+,\qquad
 (2u-U)_+\le u^2/U,\quad (-e-u)_+\le e^2/(4u)
\]
therefore give \(\mathbb E d=O_\tau(T^{-2/3})\). Let
\(L_\sigma=P_\sigma-\ell\ell^{\mathsf T}/\ell_0\) be the counting orthogonal projection onto \(W_\sigma\). For each \(i\ne0\),
\[
 (Z+2L_\sigma d)_i
 =\max(Z_i,u)+\sigma(Kd)_i-\mathbb E d
              -2\ell_i\,\ell^{\mathsf T}d/\ell_0.
\]
The last two terms have modulus \(O(\mathbb E d)\) uniformly on the bulk, using \(d_0=0\), \(\ell_0\) bounded below and \(|\ell_i|=O(n^{-1/2})\) off zero. Consequently it would suffice to prove
\[
 \inf_{i\ne0}\sigma(Kd)_i\ge-\tfrac12 T^{-1/3}                 \tag{2}
\]
for both actual deficits at a growing depth in the proved marked window. Then this one reflection has exact mean and mark and is positive for large enough \(T\). The field-uniform estimates above already handle the mean and pin terms at a smaller scale than the reserve. They give no signed bound (2) for the Jacobi convolution of the actual deficit. This test does not require the large-prime-divisor hypothesis.
