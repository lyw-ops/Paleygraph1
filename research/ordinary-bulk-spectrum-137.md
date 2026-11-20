# The actual bulk energy as a source-weighted inverse square moment

Fix an eligible prime \(p\equiv1\pmod4\), put \(n=(p-1)/2\), and let \(q=\theta_\epsilon\) be the ordinary optimum in sign \(\epsilon\). Use counting inner products. The actual pinned face consists of real rows \(F\ge0\) with \((I-\epsilon K)F=\mathbf1\) and \(F_0=q\). The equation forces mean one, since \(K\mathbf1=0\). Reflection commutes with \(K\). Hence the minimum of the bulk squared norm over real rows agrees with the minimum over the required even rows, by averaging, and its unique minimizer is even. Existence follows from compactness of the nonnegative mean-one face. These are the [ordinary complementary faces](ordinary-seed-window-134.md).

Let \(F\) be this minimizer, \(S=\{i\ne0:F_i>0\}\), and \(x=F|_S\). Write \(E_S\) for extension by zero and set
\[
 A=I_S-\epsilon E_S^*KE_S,\qquad g=\mathbf1_S+\epsilon q E_S^*Ke_0.
\]
The compressed equation is \(Ax=g\), with \(0\le A\le2I\). For \(v\in\ker A\), positivity of \(I-\epsilon K\) and \(\langle E_Sv,(I-\epsilon K)E_Sv\rangle=0\) give \((I-\epsilon K)E_Sv=0\) on the whole group. Thus \(F\pm uE_Sv\) belong to the pinned face for all sufficiently small real \(u\), since every coordinate of \(F\) on \(S\) is strictly positive. Stationarity gives \(x\perp\ker A\), so \(x=A^\dagger g\). This argument uses the support of the actual minimum-energy row. An arbitrary proposed support or the maximal support of the pinned face would require an additional positivity check for the least-squares row.

Let \(\mu_p(B)=n^{-1}\|\mathbf1_B(A)g\|_2^2\). It has zero mass at zero, even when \(A\) is singular. The exact equalities are
\[
 \frac1n\|x\|_2^2=\int_{(0,2]}\lambda^{-2}\,d\mu_p(\lambda),\qquad
 \int_{(0,2]}\lambda^{-1}\,d\mu_p(\lambda)
 =1-\frac{2q}{n}+\frac{q^2}{n}\left(1+\frac{\epsilon}{n}\right).
\]
For the second formula, use \(\langle g,A^\dagger g\rangle=\langle g,x\rangle\). The mass of \(x\) is \(n-q\). The marked equation gives \(\epsilon (K E_S x)_0=q-1-\epsilon qK_{00}\). Finally \(K_{00}=-1/n\) by the zero-character Jacobi sum in the [Fourier formulas](fourier.md#fourier-formulas). The factor \(q\ll\sqrt n\) makes the first inverse moment uniformly bounded. An empty \(S\) gives zero for both expressions by the same marked equation and mass constraint.

The inverse square moment is equivalent to the actual least bulk energy and is the remaining estimate for each sign. The measure weights the specific marked forcing, so a small eigenvalue with zero or very small overlap need not matter. A bound \(\mu_p((0,t])\le Ct^{2+\eta}\), uniform in eligible primes for \(0<t\le1\) with \(\eta>0\), would suffice. Indeed
\[
 \int_{(0,2]}\lambda^{-2}\,d\mu_p(\lambda)
 =\tfrac14\mu_p((0,2])+2\int_0^2 t^{-3}\mu_p((0,t])\,dt.
\]
The precise test is uniform boundedness of this integral. A uniform bound on it would imply the pointwise estimate with exponent \(2\) by restriction to \((0,t]\). The exact first inverse moment only implies a bound of order \(t\). For example, the abstract measures \(m^{-1}\delta_{1/m}\) have first inverse moment one and second inverse moment \(m\). For each fixed \(u>0\), their integrals against \((\lambda+u)^{-2}\) tend to zero. This shows why passing to a prime limit at fixed positive regularization cannot certify the unregularized estimate from the exact first inverse moment alone.

Equivalently, the required prime-uniform estimate is
\[
 |\langle g,v\rangle|\le C\sqrt n\,\|Av\|_2\qquad(v\in\mathbb R^S).
\]
The upper follows from \(Ax=g\) and Cauchy–Schwarz when the energy is bounded. Conversely take \(v=A^\dagger x\), so \(Av=x\) and \(\langle g,v\rangle=\|x\|_2^2\). In this form the test compares a known combination of the total mass and the marked column to the leakage on the actual support itself.

Applied to both actual signs, a uniform bound on the inverse square moments would give the [signed Jacobi tail](ordinary-sector-square-tail-135.md) by the bulk square identity and \((b-L)_+\le b^2/(4L)\). A direct estimate of the signed tail can still succeed without bounded bulk energy. This reduction supplies no prime-uniform inverse square bound or clipped-window parity estimate.
