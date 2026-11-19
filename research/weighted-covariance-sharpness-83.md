# The square-root arithmetic error survives genuine positive weighting

The [joint Jacobi covariance](translated-covariance-82.md) estimates counting moments. Its \(p^{-1/2}\) error cannot be improved uniformly even if the center weights come from the clipped exterior of a genuine feasible primary row with a prescribed mark and with effective support comparable to \(n\). The first arithmetic correction has a signed expression on that same primary row. An estimate using the optimal face or a second arithmetic cancellation can still control it.

## The first signed correction

Use \(n=(p-1)/2\), \(k(j-i)=nK_{ji}/\sqrt p\), \(E=n^{-1}\sum_i\), and \(P_s=(I-J+sK)/2\). For every feasible probability \(q\) in the sign-\(s\) sector, set \(W_q(i)=s\sum_a q_a k(i-a)\). There are exact identities for every real row \(f\):
\[
 W_q(i)=\frac{nq_i-1}{\sqrt p},\qquad
 \sqrt p\,E(fW_q)=\sum_i q_if_i-Ef=s\sum_i q_i(Kf)_i .
 \tag{1}
\]
The first follows from \(sKq=q-\mathbf1/n\); the second also uses symmetry. If a positive exterior split \(x\) has total mass \(M>0\) and \(q=x+z\), write \(W_x(i)=s\sum_a(x_a/M)k(i-a)\). The corresponding identity is
\[
 \sqrt p\, M E(f W_x)=s\langle x,Kf\rangle
   =\langle q,f\rangle-Ef-s\langle z,Kf\rangle .
 \tag{2}
\]
For the covariance test \(f=|h|^2\), this is the interaction of the actual positive weights with the next transported square. Haar parity removes the punctual part in the one-power test. The nonpunctual stalk is essential: for the single translate \(k(\cdot-a)\),
\[
                 \sqrt p\,E(f k(\cdot-a))=(Kf)_a.              \tag{3}
\]
In particular \(E|Kf|^2=E|f-Ef|^2\). Thus whenever the tested square has uniformly positive variance, no uniform-in-center \(o(p^{-1/2})\) estimate for the one-power covariance is possible.

## Sharpness with spread, feasible, root-pinned center weights

Let \(S=2\sqrt n K e_0\) and \(h=L_1=K(S^2/2)\), the first finite leading row of [round 80](astra-dissipation-80.md). Put \(f=h^2\). This is an actual physical row. Its fixed-depth negative Mellin approximant \(h_{\rm tr}\) has only rank-greater-than-one constituents, with uniformly bounded charge and error \(O(p^{-1/2})\) in normalized second norm. The finite geometric computation follows by squaring the two Jacobi lifts, then applying the ordinary quadratic twist to the nonpunctual part. Positive nonpunctual constituents have a nonzero invariant stalk at one, so those outputs have rank greater than one. Both \(h\) and its approximant are uniformly bounded.

The [variance proof](astra-centered-78.md#a-square-with-positive-variance-at-unbounded-primes) gives \(\liminf_p\operatorname{Var}_n(f)>0\). Also \(\|Kf\|_\infty=O(1)\) and \(E(fKf)=o(1)\). Indeed replace \(f\) by \(|h_{\rm tr}|^2\), of the same normalized second-norm accuracy. Its positive Mellin product representation has a discrepancy on only boundedly many cyclic characters, with bounded values. The true transport of that product has a bounded finite negative trace representation and a uniform \(O(p^{-1/2})\) error from transporting those columns. Transport of the initial second-norm discrepancy has sup norm \(O(1)\) by the counting contraction. The even-odd product of the representative fields has no punctual unit by [simultaneous parity](iteration-parity.md#types-of-local-inertia). The bounded nonpunctual terms and all second-norm errors tend to zero in \(E(fKf)\).

Set \(\pi_s=(P_s)_{00}\) and use the root-neutral zero-mean direction
\[
              g=P_s f-\frac{(P_s f)_0}{\pi_s}P_s e_0 .
\]
It is uniformly bounded and lies in the sign-\(s\) sector. The function \(g\) is the orthogonal projection of \(f\) onto the subspace of that sector vanishing at zero. Hence
\[
 \begin{split}
 E(fg)&=\|P_s f\|_{2,n}^2-\frac{(P_s f)_0^2}{n\pi_s}\\
      &=\tfrac12\operatorname{Var}_n(f)+\tfrac{s}{2}E(fKf)-O(n^{-1})
        \ \ge c>0                                                   \tag{4}
 \end{split}
\]
eventually for either sign. All constants may be chosen uniformly in the two signs.

Fix \(0<\gamma<1/\sqrt2\). The genuine normalized law
\[
 q^{\rm base}=\frac1n\mathbf1+
                 \frac{\gamma/\sqrt n-1/n}{\pi_s} P_s e_0
\]
has \(q^{\rm base}_0=\gamma/\sqrt n\) and \(\inf_{i\ne0}nq^{\rm base}_i\ge1-\sqrt2\gamma-o(1)\). For the latter bound use \(\pi_s=1/2+O(n^{-1})\) and \(|(P_s)_{i0}|\le(1+\sqrt p)/(2n)\) off the root. In particular \(nq^{\rm base}_i=O_\gamma(1)\) uniformly off it. Choose fixed positive \(B,\epsilon\) small enough that
\[
       q^\pm=q^{\rm base}\pm\frac{\epsilon}{n}g
       \quad\text{satisfy}\quad nq^\pm_i\ge 2B\quad(i\ne0).
\]
These are genuine feasible rows with exactly the same prescribed mark. Their positive clipped exteriors \(x^\pm=(q^\pm-B/n)_+\mathbf1_{\{i\ne0\}}\) have the same mass \(M=1-\gamma/\sqrt n-B(1-1/n)\), bounded away from zero. Each normalized exterior has \(m_{\rm eff}=(\sum(x_i^\pm/M)^2)^{-1}\asymp n\) and uniformly bounded relative entropy. The difference of the two reverse bias fields is exact:
\[
            W_{x^+}-W_{x^-}=\frac{2\epsilon}{M\sqrt p}g .
\]
Consequently the difference of their physical one-power moments with \(f\) is at least \(c_\gamma/\sqrt p\) by (4). The same lower bound, with a smaller constant, holds with \(|h_{\rm tr}|^2\) because \(\|g\|_\infty=O(1)\). Both corresponding Haar one-power moments vanish. For any fixed nonzero real \(t\), the difference of the two physical exponential tests also has magnitude at least \(c_{\gamma,t}/\sqrt p\). Indeed the difference vanishes at the root, both \(W_{x^\pm}\) are \(O_\gamma(p^{-1/2})\) everywhere off the root by (1) and the removal of the mass \(q^\pm_0=O(p^{-1/2})\), and the exponential difference there equals \(t(W_{x^+}-W_{x^-})+O_{\gamma,t}(p^{-1})\). By the Gaussian upper moment bound for the independent Jacobi angles, both Haar exponential factors are \(1+O_{\gamma,t}(p^{-1})\). At least one of the errors in the two instances of the [exponential comparison](translated-covariance-82.md#an-arbitrarily-weighted-finite-prime-test) with the raw negative approximant therefore has magnitude \(\gg_{\gamma,t}p^{-1/2}\).

There is also a conditional sharpness statement at supercritical feasible marks. If a genuine larger optimum has \(\sqrt n q^*_0\ge 1+\delta\), take \(q^{\rm base}=(1-\kappa)q^*+\kappa\mathbf1/n\) for \(\kappa=\delta/[4(1+\delta)]\). This retains mark at least \(1+3\delta/4\) after multiplying by \(\sqrt n\), and gives uniform bulk slack \(nq^{\rm base}_i\ge\kappa\). The same fixed-sign construction, with \(B,\epsilon\) chosen using this slack, gives (4) and the \(p^{-1/2}\) one-power separation at that common supercritical mark. This conditional version does not ensure \(m_{\rm eff}\asymp n\), nor does it place the perturbed rows on the maximal mark face.

## Consequences for the prime-uniform estimate

The covariance error multiplied by \(\sqrt p\) can have order one even on clipped exteriors of genuine positive rows. The sign-sensitive functional in (2) is the quantity to estimate instead. The construction changes neither the shared root nor the exact Fourier sector, so those constraints and center spreading are insufficient to improve the one-power error uniformly. Under a hypothesized gap it still leaves open cancellation on the actual maximum-mark face and in exterior cutoffs where activity is constrained by the chosen terminal window.

1. Price \(s\langle x,K|h|^2\rangle\) on a jointly chosen true marked face and terminal window using a nonnegative opposite completion. Estimate the signed residual from the concentrated subset instead of the worst-case stalk size.
2. Use true complementary optimal laws \(q,r\) together. The exact identity \(\sum_iq_i r_{i+a}=1/n\) for every \(a\) follows from disjoint nontrivial Fourier supports. Seek a mixed test whose nonpunctual correction is a controlled function of the displacement \(a\), so this identity averages the leading signed error.
