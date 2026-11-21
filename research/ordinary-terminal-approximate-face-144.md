# The actual terminal comparison with an approximate sector row

Fix a floor \(\tau>0\). Use the true zero-start orbit, the projected average \(X=X_{\sigma,T}\) of the positive row with sign \(\sigma\), its mean \(M=M_T\), its mark \(a=X_0\), and \(Z=X/M=U_\sigma+e_\sigma\). Write \(s=-\sigma\), \(g=g_T=\Phi(v_T)-\Phi(v_0)\), \(G=\sqrt n\,g\). Take \(T\to\infty\) with \(T+1\) in the actual simultaneous marked window. In these conventions \(e_\sigma=-P_s g/(2TM)\) and \(U_\sigma\ge0\). All inner products below use normalized counting measure.

Let \(F\ge0\) be any real mean-one row with \(q=F_0=O(\sqrt n)\). Set \(\lambda=F-qe_0\) and let \(r=P_\sigma(F-\mathbf1)\). There is no exact sector constraint on \(F\). Define
\[
 \mathcal R_F=\mathbb E\!\left[r\left(Z-\mathbf1-\frac{g}{2TM}\right)\right].
\]
Then
\[
 1-\frac{q a}{nM}\ \ge\
 -\frac{\mathbb E(\lambda G)}{2T\sqrt n M}
 -\mathcal R_F-O_{\tau,B}(T^{-B-1}).                             \tag{1}
\]
Indeed the exact projected pairing gives
\[
 \mathbb E(\lambda Z)=1+\mathbb E[r(Z-\mathbf1)]-\frac{q a}{nM}.
\]
By \(P_sF=F-\mathbf1-r\), positivity of \(U_\sigma\) and self-adjointness, the same pairing is at least the following quotient:
\[
 \mathbb E(\lambda e_\sigma)=
 \frac{
  -\mathbb E(\lambda g)+(1-q/(2n))\mathbb E g+
     (q/(2n))(s(Kg)_0-g_0)+\mathbb E(rg)
 }{2TM}.
\]
The mean term is nonnegative eventually. The physical term is \(O_{\tau,B}(T^{-B-1})\) after division, since \(Kg=v_{T+1}-v_1\), \(0\le g_0\le |v_T(0)|\), the mark estimate applies simultaneously, and \(M\ge\sqrt{\tau/n}\). This proves (1).

There is a convenient norm bound
\[
 |\mathcal R_F|\le C_\tau\sqrt T\,\|r\|_{2,n}.                  \tag{2}
\]
The actual unweighted energy gives \(\|v_j\|_{2,n}^2\le4Wj/n\), \(\|\Phi(v_j)\|_{2,n}^2\le4W(j+1)/n\), and \(\|g\|_{2,n}=O_\tau(\sqrt{T/n})\). The averaged projected row \(Z-\mathbf1\) is the average of the projected \((\Phi(v_j)+\sigma v_j)/(2M)\); each projection is a contraction. These bounds prove \(\|Z-\mathbf1\|_{2,n}=O_\tau(\sqrt T)\) and \(\|g\|_{2,n}/(2TM)=O_\tau(T^{-1/2})\), hence (2).

Let \(q_s\) denote the true ordinary optimum on sign \(s\). At each sign it would suffice to choose a nonnegative mean-one row with \(q=q_s+o(\sqrt n)\), \(\mathbb E(\lambda G)=o(T)\), and \((\mathcal R_F)_+=o(1)\), at a selectable growing marked time. In particular \(\|P_\sigma(F-\mathbf1)\|_{2,n}=o(T^{-1/2})\) suffices for the defect condition. Exact dual-face optimization and projection back into the positive cone are not prerequisites for this sufficient test. For such rows (1) yields \(q_s/\sqrt n\le \sqrt{1+\tau}+o(1)\) by the actual marked mean and root bounds. Reciprocity gives the squeeze after the prime limit and then \(\tau\downarrow0\).

If \(q_s/\sqrt n\ge1+\eta\) on a prime subsequence at one sign, choose \(\sqrt{1+\tau}<1+\eta\). Every row with \(q=q_s+o(\sqrt n)\) at each chosen growing time then satisfies
\[
 \frac{\mathbb E(\lambda G)}{2T\sqrt n M}+\mathcal R_F
 \ \ge c_{\tau,\eta}>0
\]
eventually. Thus, along that subsequence, a row with low actual cost must have an aligned positive sector residual. A row obtained by truncation, smoothing or approximate interpolation still needs an arithmetic estimate on that alignment. Equations (1)–(2) are field-general comparisons and leave the required prime-uniform construction open.

## Interpretation of the two face-selection drafts

The exact interpolation proposal \(P_{U_{-s}}b=P_{U_{-s}}(\mathbf1-q_s e_0)\) for \(b\ge0\) supported on the common bulk zero set \(I\) has a solution at every field. Take \(b=F-q_s e_0\) for any true optimizer. Conversely any such \(b\) makes \(F=b+q_s e_0\) a nonnegative mean-one row with \(P_{V_{-s}}F=0\) and root \(q_s\), hence it is precisely a true optimizer. This uses normalized pairing \(\mathbb E(bZ)\), so a sum with mass-normalized weights uses \(b_i/n\). The cost of exact interpolation is exactly the old face cost. Equation (1) breaks that identity only by tracking the residual of an approximate row.

A single dual minorant of low value cannot prove that the maximum over all minorants has low value. The cap-translation proposal does retain the original root and unshifted cost, but on the canonical least-norm optimum its cap set is a period subgroup and such averaging reproduces the same row. Noncanonical exact cap translates may give a different row. Neither observation controls a prime-uniform endpoint cost.
