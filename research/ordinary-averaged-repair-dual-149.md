# An opposite row from finitely many actual relaxed repairs

Use the [actual pinned reflection and relaxed updates](ordinary-pinned-reflection-flow-148.md) on either sign \(\sigma\). Fix \(\tau>0\) and \(0<\omega<2\). Let \(T=T(p)\to\infty\) with \(T+1\) in the simultaneous marked window. Write \(z_0=a/M\) for the actual pinned mark, \(\ell=P_\sigma e_0\), \(L=L_\sigma=P_\sigma-\ell\ell^{\mathsf T}/\ell_0\), and use normalized counting inner products and norms. Assume a true opposite mean-one optimum \(F\) has mark \(q\ge(1+\eta)\sqrt n\) and \(\sqrt{1+\tau}<1+\eta\). This assumption is along the hypothetical gap subsequence. The repair count \(m\) is separate from the Picard window.

Define \(U=\mathbf1+(z_0-1)\ell/\ell_0\). This is the mean-one pinned affine representative orthogonal to the range of \(L\), and \(y^{(j)}-U\in\operatorname{im}L\) for every \(j\). The [Picard energy and mean bounds](averaged-mark-35.md) give \(E_t\le4Wt\), \(nM^2\ge\tau\), \(a=1+o(1)\), and \(nM^2\le1+\tau+o(1)\). Thus \(z_0\asymp_\tau\sqrt n\). Also \(\|Z-\mathbf1\|_{2,n}^2=O_\tau(T)\): each positive row \((\phi_t+\sigma v^{(t)})/2\) has counting squared norm at most \((\|\phi_t\|_2^2+\|v^{(t)}\|_2^2)/2=E_t+2W\), and the projection and averaging do not increase the corresponding bound. The initial correction \(2Ld\) has squared normalized norm \(O_\tau(T^{-1})\), and \(\|U-\mathbf1\|_{2,n}^2=(z_0-1)^2/(n\ell_0)=O_\tau(1)\). In particular \(\|y^{(0)}-U\|_{2,n}^2=O_\tau(T)\).

## Telescoping the defect pairing

For the actual bulk deficit \(b_j=1_{\rm bulk}(-y^{(j)})_+\), set
\[
 r_j=\mathbb E b_j,\qquad B_j=-\ell^{\mathsf T}b_j/\ell_0,\qquad
 s_j=(z_0-1)B_j/n-r_j.
\]
Round 148 and \(F_i\le1+\sqrt p\) imply
\[
 \mathbb E(Fb_j)\ge qz_0/n-1\gg_{\tau,\eta}1,\qquad
 r_j\gg_{\tau,\eta} n^{-1/2},\qquad
 \sum_{j<m}\|Lb_j\|_{2,n}^2=O_{\tau,\omega}(T^{-1}).
\]
All constants are uniform in the number of repairs. The bulk bound \(|\ell_i|\le(1+\sqrt p)/(2n)\) and \(b_j(0)=0\) give \(|B_j|\ll\sqrt n\,r_j\), hence \(|s_j|\ll_\tau r_j\).

Since \(\langle b_j,y^{(j)}\rangle_{2,n}=-\|b_j\|_{2,n}^2\), decomposition at \(U\) gives the exact identity
\[
 s_j=\|b_j\|_{2,n}^2+\langle Lb_j,y^{(j)}-U\rangle_{2,n}.
\]
The scalar product here has the sum
\[
 \sum_{j<m}\langle Lb_j,y^{(j)}-U\rangle_{2,n}
 =\frac{\|y^{(m)}-U\|_{2,n}^2-\|y^{(0)}-U\|_{2,n}^2}{2\omega}
   -\frac{\omega}{2}\sum_{j<m}\|Lb_j\|_{2,n}^2
 \ge -O_{\tau,\omega}(T).
\]
This is a one-sided time-summed estimate and leaves the terminal distance unrestricted.

## A positive average and a single-step alternative

Write bars for averages over the first \(m\) deficits. Put \(\epsilon_m=T\sqrt n/m\) and \(v_m=n/(mT)\). If \(\epsilon_m=o(1)\), the preceding inequality yields \((z_0-1)\bar B/n\ge(1-O_{\tau,\eta,\omega}(\epsilon_m))\bar r\), so \(\bar B>0\) eventually. The nonnegative mean-one row
\[
 F_m=\frac{\bar b+\bar B e_0}{\bar r+\bar B/n}
\]
satisfies
\[
 F_m(0)\ge(1-O_{\tau,\eta,\omega}(\epsilon_m))\frac{n}{z_0},\qquad
 \|P_\sigma F_m\|_{2,n}=O_{\tau,\eta,\omega}(\sqrt{v_m}),\qquad
 (P_\sigma F_m)_0=0.
\]
Indeed \(nB/(nr+B)\) is increasing in \(B\) for \(r>0\), and \(\|L\bar b\|_{2,n}\le(\sum_{j<m}\|Lb_j\|_{2,n}^2/m)^{1/2}\). The projection formula is \(P_\sigma(\bar b+\bar B e_0)=L\bar b\).

There is also a single actual repair step with both a large positive mark and a small normalized projection. Give \(j<m\) probability \(r_j/\sum_{k<m}r_k\). The expectation of \(s_j/r_j\) is at least \(-O_{\tau,\eta,\omega}(\epsilon_m)\), while
\[
 \mathbb E_{\rm steps}\!\left[\left(\frac{\|Lb_j\|_{2,n}}{r_j}\right)^2\right]
 \le \frac{\sum_{j<m}\|Lb_j\|_{2,n}^2}{(\min_{j<m}r_j)\sum_{j<m}r_j}
 =O_{\tau,\eta,\omega}(v_m).
\]
If \(v_m=o(1)\), discard the steps for which the ratio exceeds \(v_m^{1/3}\). Their probability is \(O_{\tau,\eta,\omega}(v_m^{1/3})\). The boundedness of \(s_j/r_j\) guarantees a retained step with \(s_j/r_j\ge-O_{\tau,\eta,\omega}(\epsilon_m+v_m^{1/3})\). For that \(j\), \(B_j>0\) eventually. The row
\[
 F^{[j]}=\frac{b_j+B_j e_0}{r_j+B_j/n}
\]
is nonnegative and mean one, has mark at least \((1-O_{\tau,\eta,\omega}(\epsilon_m+v_m^{1/3}))n/z_0\), and has \(P_\sigma\)-projection of normalized norm at most \(v_m^{1/3}\) and zero marked coordinate. Both errors vanish for \(m\gg\max(T\sqrt n,n/T)\) with ratios tending to infinity.

Both normalized rows \(G\) have the exact cap \(G_0\le1+\sqrt p\) at the mark. The identity \(2P_\sigma=I-J+\sigma K\) gives \(\sigma(KG)_0=1-G_0\) there, and the entrywise \(K\) bound and nonnegative mean one give \(|(KG)_0|\le\sqrt p\).

## Constraints on the same selected prime deficit

Put \(m_0=n/\sqrt p\) and \(c_\sigma(i)=-\sigma m_0 K_{i0}\) on the bulk. Then \(|c_\sigma(i)|\le1\) and
\[
 2\ell_0 B_j=r_j+\sqrt p\,\mathbb E(b_j c_\sigma).
\]
The selected step therefore has \(\mathbb E(b_j c_\sigma)/r_j\ge n/(\sqrt p\,z_0)-o(1)\) when both repair errors vanish. In particular it puts a positive fraction of its bulk mass on some fixed favorable phase arc for each fixed floor. For example, if \(0<2\rho<\sqrt{\tau/2}\), then the normalized \(b_j\)-mass of \(c_\sigma\ge\rho\) is at least \(\rho/(1-\rho)\) eventually.

Moreover \(\|Lb_j\|_{2,n}/\|b_j\|_{2,n}\le\|Lb_j\|_{2,n}/r_j=o(1)\). By the [concentrated prime-defect gap](anchored-repair-20.md#a-uniform-single-step-gap-for-concentrated-prime-defects), the effective support size of this same \(b_j\) is at least \((1-o(1))m_0\). Fix a layer parameter \(0<\lambda<1\) and energy margin \(\Delta>0\). That theorem also gives \(\xi>0\) such that either the effective size exceeds \((1+\xi)m_0\) or the set \(S=\{i:b_j(i)\ge\lambda\|b_j\|_2/\sqrt{m_0}\}\), with counting norm in its definition, has additive energy less than \((1/2+\Delta)|S|^3\), for every sufficiently large prime in the gap subsequence.

The [stationary trial identity](anchored-repair-20.md) already gives an exact opposite witness at a minimizer. The finite-step statements here control physical iterates quantitatively, retain the actual complementary weighted deficit, and in the single-step case keep the original negative-part form. Approximate sector membership and a mark of size \(n/z_0\) still allow a true gap and the square-order control. The open arithmetic step is to exclude the observed joint positive mark, small projection, and true weighted cost on the actual prime deficits.
