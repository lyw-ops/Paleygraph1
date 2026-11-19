# Rigidity of positive stochastic repair at the true marked depth

A doubly stochastic map that preserves just the sector being repaired and keeps the actual averaged mark cannot change that average in the proved arithmetic window. The map may be chosen adaptively after seeing the whole orbit, and the two signs may use different maps. The proof fixes both the actual nonlinear iteration and its projected averages. There is also a quantitative stability bound in terms of root leakage and the commutator with the true Fourier multiplier.

## Sector invariance for an adaptive positive map

Use the actual notation from the [averaged budget](averaged-mark-35.md). Thus \(n=(q-1)/2\), \(K^2=I-J\), \(K=K^{\mathsf T}\), \(K\mathbf1=0\), \(J=\mathbf1\mathbf1^{\mathsf T}/n\), and \(P_\sigma=(I-J+\sigma K)/2\). Write \(V_\sigma=\operatorname{im}P_\sigma\). A doubly stochastic matrix \(M\) has nonnegative entries and all row and column sums one. For the chosen sign suppose \(M(V_\sigma)\subseteq V_\sigma\). Equivalently, \(M\) preserves the mean-one affine sector.

Let \(F=\ker(I-M)\) on real vectors. By Jensen, \(M\) and \(M^{\mathsf T}\) are contractions for the counting Euclidean norm. If \(Mg=g\), equality in
\(\langle M^{\mathsf T}g,g\rangle=\|g\|^2\) forces this by Cauchy--Schwarz. For any \(g\in F\), put \(h=P_\sigma g\). Since \(Mh\in V_\sigma\), we have
\[
 \langle h,Mh\rangle=\langle g,Mh\rangle
     =\langle M^{\mathsf T}g,h\rangle=\langle g,h\rangle=\|h\|^2.
\]
Contractivity then gives \(Mh=h\). Hence \(F\) is invariant under \(P_\sigma\), and it is invariant under \(K=\sigma(2P_\sigma-I+J)\) because it contains the constants. The proof only requires invariance of the one specified sector.

For \(g\in F\) one also has
\[
 \tfrac12\sum_{i,j}M_{ij}(g_i-g_j)^2=\|g\|^2-\langle g,Mg\rangle=0.
\]
Every positive entry \(M_{ij}\) joins coordinates with equal \(g\) values. Thus a common pointwise real function of any finite tuple of vectors in \(F\) lies in \(F\) as well.

If \(M e_0=e_0\), this applies to the true activation with weights \(w_0=1\) and \(w_i=\tau/n\) at all other sites. Indeed
\[
 v_{t+1}=K\phi_t,\qquad
 \phi_t=f(v_t)+b_t e_0,\qquad
 f(x)=\sqrt{x^2+4\tau/n},\qquad
 b_t=\sqrt{v_t(0)^2+4}-f(v_t(0)).
\]
Starting at zero gives \(v_t,\phi_t\in F\) for every \(t\), by induction. It also gives \(X_{\sigma,T}\in F\) by the actual projected-average definition. The canonical root-neutral mean vector \(1-(P_\sigma e_0)/(P_\sigma e_0)_0\) is in \(F\) too whenever the denominator is positive. In particular adding that mean allowance does not create any new effect of the map on the bulk. For these even inputs it is enough that \(M\) preserves the even part of \(V_\sigma\). Apply the projection argument to even fixed vectors, for which \(P_\sigma g\) is even, and use that the activation and \(K\) preserve evenness.

## The true root forces the map to fix the mark coordinate

The normalization of \(X_{\sigma,T}\) here is the unscaled one in round 35, with \(X_{\sigma,T}(0)\to1\) in the marked window. Its mark is its unique maximum there, uniformly for every allowed \(\tau\) and \(T\). More precisely, for any fixed \(B>0\), shorten the inherited log-star window by the constant needed for accuracy \(D^{-B}\). The approximations \(N_t\) to \(Y_t=\sqrt n v_t\) of [round 40](astra-completion-40.md#a-signed-estimate-uniform-over-the-observed-history) satisfy, up to time \(D+1\),
\[
 \sup_t\|Y_t-N_t\|_{2,n}=O_B(D^{-B}),\qquad
 \sup_t\|N_t\|_\infty\le q^{1/4}.
\]
The latter may use the looser resource bound of [round 38](vanishing-floor-38.md). Thus \(\|v_t\|_\infty\le\|Y_t-N_t\|_{2,n}+\|N_t\|_\infty/\sqrt n=O_B(D^{-B}+q^{-1/4})\). Off the mark the same holds for \(\phi_t\), since \(0\le\tau\le1\). The actual norm budget gives \(\mu_t\le\sqrt{W(t+1)/n}\). Combining these facts with the exact [sum and difference formulas for the average](averaged-mark-35.md#3-projected-averages-have-balanced-marks) gives
\[
 \sup_{i\ne0}|X_{\sigma,T}(i)|=O_B(D^{-B}+q^{-1/4}),\qquad
 X_{\sigma,T}(0)=1+O_B(D^{-B}+q^{-1/4}),
 \quad 1\le T\le D .
\]
For a map satisfying only \((MX_{\sigma,T})(0)=X_{\sigma,T}(0)\), the root row of \(M\) is therefore supported only at 0 on sufficiently large fields. Column stochasticity forces the rest of column 0 to vanish. We have recovered \(Me_0=e_0\), so the exact no-change conclusion applies even when mark preservation is only required on the chosen input.

This proves an obstruction on the true average through primes and prime squares. In particular at zero floor the inherited mean deficit excludes joint nonnegativity at the original means and marks in the window. A sign-preserving doubly stochastic map cannot remove any negative coordinate that is present. There is no restriction here on nonstochastic additions in the affine sector, or on maps whose final pointwise inequalities hold only after a separate Fourier correction. [Zero-floor mean deficit](vanishing-floor-38.md#2-a-necessary-mean-margin-at-the-true-marks)

## Approximate symmetry estimate

Let \(M\) now be any doubly stochastic matrix, with \(S=(M+M^{\mathsf T})/2\), \(\eta=1-M_{00}\), and \(\delta=\|[K,S]\|_{2\to2}\). Set
\[
 \mathcal E(g)=\langle g,(I-S)g\rangle
             =\tfrac12\sum_{i,j}M_{ij}(g_i-g_j)^2 .
\]
Its square root is a seminorm, \(\mathcal E(e_0)=\eta\), and a common one-Lipschitz scalar function contracts it. The identity
\[
 K(I-S)K-(I-S)=-(KS-SK)K
\]
uses \(K^2=I-J\) and \(SJ=J\). In particular
\(\sqrt{\mathcal E(Kg)}\le\sqrt{\mathcal E(g)}+\sqrt\delta\|g\|\).
Since \(|b_t|\le2\) and \(\|\phi_t\|\le2\sqrt{W(t+1)}\), the actual recursion yields
\[
 \sqrt{\mathcal E(v_t)}
 \le 2t\sqrt\eta+2\sqrt{W\delta}\,t^{3/2},\qquad
 \sqrt{\mathcal E(\phi_t)}\le\sqrt{\mathcal E(v_t)}+2\sqrt\eta .
\]
The four terms in the averaged sum and difference identities and Jensen on each row of \(M\) give
\[
 \boxed{\;
 \|(M-I)X_{\sigma,T}\|
 \le 2\sqrt2\big((T+2)\sqrt\eta+\sqrt{W\delta}(T+1)^{3/2}\big).
 \;}
\]
This is also the normalized \(L^2\) change of the scaled row \(\sqrt n X_{\sigma,T}\). When \(M\) commutes with \(K\), the commutator term vanishes exactly. For a map with small loss at the mark in the arithmetic window, the unique maximum estimate also gives
\[
 X_{\sigma,T}(0)-(MX_{\sigma,T})(0)\ge(1-o(1))\eta .
\]
For instance when \(M\) itself completes the row to nonnegativity, the boxed right side must be at least the normalized \(L^2\) size of the input's negative part. This stability statement does not give a positive lower bound on that size at growing depth.

There is a support restriction on such a signed correction at prime order. After subtracting the canonical root-neutral vector for any added mean, the correction has zero mean and lies in \(V_\sigma\). The [Casoratian argument](astra-weighted-62.md#intervals-supporting-an-exact-fourier-update) uses exactly these Fourier hypotheses. It therefore applies to the support of this correction even when neither its initial row nor the corrected trial is an optimizer. At radius \(R=n^{3/4+\epsilon}\), a nonzero correction needs at least \((1/4-\epsilon)\log_2 n-O(\log\log n)\) patches of length \(O(R)\). If a proposed repair iterates exact sector corrections, this applies at each nonzero step after removing its mean increment.

The next repair should use a signed root-neutral sector correction of the actual average. Any proposed scheme implemented through a doubly stochastic map preserving both the one-sector constraint and the mark returns the original row. The remaining test is a worst-site bound for a correction with the exact sector and mark and \(o(1)\) extra scaled mean, alongside the inherited marked cancellation.
