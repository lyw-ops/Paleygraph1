# Separate signed tests for the ordinary ratio and the fixed-cap defect

Use the actual zero-floor all-site cap \(M>0\) and the exact cap-inactive bulk ordinary pair \(Y=Kb\) of [Round 132](zero-floor-endpoint-132.md). Write \(\nu=\mathbb E_n b\), \(\eta=Y_0/b_0\), \(\tau_i=\operatorname{sgn}Y_i\) on the bulk, and \(F_\epsilon=(b+\epsilon Y)/\nu\) for the two ordinary factors of mean one. Thus \(b_i=|Y_i|\) off the mark and \(\eta\to0\) is equivalent to the ordinary theta limit. For an actual capped trial row \(W\), put \(a=\Phi_0(C_M(W))\), \(\mu(W)=\mathbb E_n a\), and \(r=Ka-W\). Use the two signed bulk contributions
\[
 e_\epsilon(W)=\mathbb E_n[1_{\{i\ne0,\;\tau_i=\epsilon\}}|Y_i|(\epsilon W_i-a_i)] .
\]
For \(\tau_i=\epsilon\), this charges aligned spill positively and the ordinary-weighted mismatch negatively. Zero entries of \(Y\) carry zero weight.

Because \(KF_\epsilon=\epsilon(F_\epsilon-\mathbf1)\), the full pairing is \(\mathbb E_n[F_\epsilon(a-\epsilon W)]=\mu(W)+\epsilon\langle F_\epsilon,r\rangle_{2,n}\). On the bulk, \(\nu F_\epsilon/2\) equals the weight in \(e_\epsilon\). Subtracting the marked summand gives the exact identity
\[
 e_\epsilon(W)=\frac{(b_0+\epsilon Y_0)(a_0-\epsilon W_0)}{2n}
                 -\frac{\nu\mu(W)}2
                 -\frac{\epsilon\nu}2\langle F_\epsilon,r\rangle_{2,n}.
                                                               \tag{1}
\]
It includes the actual nonlinear marked activation in both rows and needs no bulk division.

## An antisymmetric criterion for the original theta limit

Subtracting the two signs gives
\[
 e_+(W)-e_-(W)
 =\mathbb E_n[1_{\{i\ne0\}}(b_iW_i-a_iY_i)]
 =\frac{a_0Y_0-b_0W_0}{n}-\langle b,r\rangle_{2,n}.
                                                               \tag{2}
\]
At the actual capped fixed point \(U\), the residual is zero, \(U_0/\sqrt n\to0\) through primes at every fixed cap, and \(a_0,b_0=2\sqrt n+O_M(n^{-1/2})\). So the right side is \(4\eta+o_p(1)\).

For the genuine averaged recurrence \(W_{j+1}=W_j+r_j/2\), denote averages over \(0\le j<J\) by an overline. The last term of (2) averages to \(-2\langle b,W_J\rangle_{2,n}/J\). Its numerator is \(O_M(1)\) through primes, uniformly in \(J\), since \(b=\nu(F_++F_-)/2\) and the absolute terminal pairings with each \(F_\epsilon\) are bounded by the [exact averaging recursion](zero-floor-averaged-weighted-tail.md#the-actual-weighted-quantity-telescopes). The mark \(W_{j,0}/\sqrt n\to0\) for every fixed \(j\) by the [fixed-depth parity result](zero-floor-averaged-weighted-tail.md#fixed-depth-marked-limit-with-the-zero-floor-kept). Hence
\[
 \overline e_+-\overline e_-=4\eta+O_M(J^{-1})+o_{M,J,p}(1).
\]
In particular
\[
 \lim_{J\to\infty}\limsup_{p\to\infty}
 \left|\mathbb E_n[1_{\{i\ne0\}}(b_i\overline W_i-\overline a_iY_i)]\right|
       =4\limsup_{p\to\infty}|\eta|.
                                                               \tag{3}
\]
The order fixes \(M,J\), takes primes first, and then grows \(J\). This tests the original ordinary ratio at any fixed cap. It does not require vanishing of the cap defect, so a small-cap defect is compatible with this criterion. The arithmetic upper on its left still has to be proved.

## An equal-sign test that retains the cap deficit

Put \(E(W)=(e_+(W)+e_-(W))/2\). This is \(\mathbb E_n[1_{\{i\ne0\}}(Y_iW_i-|Y_i|a_i)]/2\). At the actual capped fixed point with mean \(\mu\), (1) gives \(E(U)=2-\nu\mu/2+o_p(1)\). Since \(\mu=\sqrt{4-\alpha_M}\) and \(\nu=(b_0/\sqrt n)\sqrt{1-\eta^2}\), this has the exact asymptotic decomposition
\[
 E(U)=\frac{\alpha_M}{4}+\eta^2+
 \left(\sqrt{1-\alpha_M/4}-\sqrt{1-\eta^2}\right)^2+o_p(1).
                                                               \tag{4}
\]
At averaged horizons the difference from \(E(U)\) is at most \(O_M(J^{-1/2})+o_{M,J,p}(1)\), using (1), the same terminal bound, and the [field-uniform comparison of means](zero-floor-mean-131.md). The prime-first upper on the equal-sign average therefore vanishes exactly when the ordinary limit and the true fixed-cap deficit both vanish. For the theta-only target, (3) avoids this additional condition and has the smaller terminal error.

At the fixed point the endpoint statistic \(S=\mu-(a_0/b_0)\nu\) from Round 132 obeys \(\nu S=\eta(e_+-e_-)-2E(U)\) exactly. Thus passing directly to an absolute overlap can discard the nonnegative reserve in (4). The genuine signed correlation in (3) offers a separate arithmetic target without an unweighted cap prerequisite.

## Replacing the activations by bounded polynomial approximants

The antisymmetric statistic permits a fixed-depth approximation without an \(L^2\) bound on the ordinary optimizer. Fix \(M,J\) and an accuracy \(0<\rho\le1\). The fixed-depth arithmetic approximation in [Round 129](zero-floor-averaged-weighted-tail.md#fixed-depth-marked-limit-with-the-zero-floor-kept) provides, for each \(j<J\), a bounded negative-field approximant to \(W_j\) in normalized second norm. Approximate the even function \(g_M(w)=\min(|w|,M)\) on that approximant's bounded range by an even polynomial. The approximation and polynomial accuracy can be chosen so the resulting arithmetic row \(q_j\) is bounded by \(M+\rho\) in modulus and approximates \(g_M(W_j)\) in normalized second norm within \(\rho\), for all sufficiently large primes. All complexities are set before the prime limit.

Put \(\widetilde a_j=2\sqrt n\,e_0+q_j\), \(\widetilde W_0=0\), and \(\widetilde W_{j+1}=(\widetilde W_j+K\widetilde a_j)/2\). The actual marked activation minus \(2\sqrt n\) is \(O_M(n^{-1/2})\). Thus the actual and surrogate activations differ in normalized second norm by at most \(\rho+O_M(n^{-1/2})\) and in maximum norm by \(O_M(1)\), uniformly through the finite horizon. The averaged difference recurrence and \(\|K\|_{2\to2}\le1\) give \(\sup_{j\le J}\|W_j-\widetilde W_j\|_{2,n}\le\rho+O_M(n^{-1/2})\).

Apply the difference version of (2) to these two sequences. The differences in the marked terms are \(O(\rho)+O_M(n^{-1/2})\), by the normalized second-norm bound for \((W_j-\widetilde W_j)_0/\sqrt n\), and the activation difference at the mark is itself bounded. The terminal pairing has
\[
 |\langle b,W_J-\widetilde W_J\rangle_{2,n}|
 \le \sum_{j<J} 2^{j-J}|\langle Y,a_j-\widetilde a_j\rangle_{2,n}|
 =O_M(1),
\]
because \(K\) is self-adjoint, \(b\ge |Y|\), \(\nu\le2\), and the activation differences are bounded in maximum norm. It follows that replacing both bulk rows in (3) by the paired surrogate changes its value by at most \(O(\rho)+O_M(J^{-1})+o_{M,J,p}(1)\), with constants independent of the ranks of the polynomial expressions. This estimates the *signed pair* together even though approximating each optimizer-weighted product separately by its normalized second-norm error would lose a field factor.

The single seed pairing also identifies the same limiting target directly. With \(S_{\rm Jac}=2\sqrt n\,Ke_0\) one has \(\mathbb E_n[1_{\{i\ne0\}}b_i(S_{\rm Jac})_i]=4\eta+O_M(n^{-1})\) by \(Kb=Y\) and \((S_{\rm Jac})_0=-2/\sqrt n\). To gain an arithmetic estimate from the polynomial surrogate one must still use the actual ordinary-support information beyond this scalar identity.
