# A genuine overflow rectangle with both sides at high stationary weight

At the critical real cap-defect scale, failure of marked cancellation forces a signed Jacobi rectangle entirely within the high part of the true stationary source. One side consists of actual capped overflow with the same sign as the true stationary row at each retained site. The other side may also be chosen to have one true stationary sign. This conclusion uses the actual signed overflow pairing and requires no small Gram residual.

Use the [real capped comparison](real-cap-exterior-103.md). In particular \(p=2n+1\equiv1\bmod 4\), \(t,M>0\) are fixed, and \(a=\Phi_t(C_M(U))\), \(b=\Phi_t(Y)\), \(U=Ka\), \(Y=Kb\). Put \(g=b-2\sqrt t\ge0\), \(A=\sqrt{M^2+4t}\), and let \(\tau,\alpha,\gamma\) be the signed enlarged-threshold overflow, mean cap deficit and true log mark. Suppose on a prime subsequence that \(\alpha\le B/\sqrt n\) and \(|\gamma|\ge\delta>0\), with fixed \(B>0\). The real comparison (1), capped mark decay, and \(s_0/n\to1\) give
\[
 \mathbb E_n \tau_iY_i\ge c:=\cosh\delta-1>0
\]
eventually. Here and below the \(2,n\) norm is normalized, \(\|K\|_{2\to2}\le1\), and \(\max |K_{ij}|\le\sqrt3/\sqrt n\). The marked coordinate of \(\tau\) is eventually zero. The elementary bounds used below are
\[
 \mathbb E_n |\tau|\le \frac{\alpha}{2A},\qquad
 \mathbb E_n|\tau|^2\le\alpha,\qquad
 |\operatorname{supp}\tau|\le\frac{n\alpha}{4t}.
\]
Indeed on bulk overflow the local cap deficit is \(4t+2A|\tau_i|+\tau_i^2\). Also \(\mathbb E_n g\le\mathbb E_n b\le B_0:=2\sqrt{1+t}\), \(\|Y\|_\infty\le C_Y\sqrt n\) for \(C_Y=\sqrt3 B_0\), and \(\|g\|_\infty\le C_g\sqrt n\) for \(C_g=2+C_Y\) and \(n\ge t\).

## Localize the signed pairing before using the true update

Choose \(L>0\) large and \(\lambda>0\) small so that \(C_Y B/L\le c/8\) and \(\lambda B/(2A)\le c/8\). Remove sites with \(|\tau|>L\) and \(|Y|<\lambda\sqrt n\). Their absolute debits in the normalized pairing are at most \(C_Y\sqrt n\,\alpha/L\) and \(\lambda\sqrt n\,\alpha/(2A)\). Removing the remaining sites where \(\tau Y\le0\) only increases the lower bound. Split the survivors by their common sign. For one sign \(\epsilon\in\{+1,-1\}\), the retained actual overflow \(f=\tau\mathbf 1_{S_*}\) has
\[
  \mathbb E_n f_iY_i\ge 3c/8,\qquad
  0<\epsilon f_i\le L,\quad \epsilon Y_i\ge\lambda\sqrt n
                  \quad (i\in S_*).
\]
In particular \(S_*\) has size comparable to \(\sqrt n\). The upper bound comes from the overflow count. The lower bound uses \(LC_Y\sqrt n\) as the pointwise upper of \(f_iY_i\). The same sign at each site refers to the actual \(U_i\) as well, since \(\operatorname{sgn}\tau_i=\operatorname{sgn}U_i\) on this support.

Fix \(0<\eta\le\lambda/2\) so small that \(\sqrt{B\eta B_0}\le c/16\), and let \(H=\{i\ne0:g_i\ge\eta\sqrt n\}\). The true update is \(Y=Kg\). The low bulk part of \(g\) has \(\|\mathbf1_{\{i\ne0\}\setminus H}g\|_{2,n}\le\sqrt{\eta B_0}\,n^{1/4}\). Its pairing with \(Kf\) costs at most \(\sqrt{B\eta B_0}\), because \(\|Kf\|_{2,n}\le\sqrt B\,n^{-1/4}\). The part at the mark has \(2,n\) norm at most \(C_g\), so it costs \(o(1)\). Consequently
\[
 \mathbb E_n f_i (K(\mathbf1_H g))_i\ge c/4
\]
eventually. This use of the \(2,n\) contraction removes the low true source even when it carries order-one normalized first mass. Moreover \(S_*\subset H\) eventually, since on \(S_*\) one has \(g_i\ge |Y_i|-2\sqrt t\).

## Extract the two genuine high-source levels

Split \(H\) by the true sign of \(Y\). Every site of \(H\) has \(Y_i\ne0\) at these bulk floors. One sign class \(H_\sigma\) preserves a pairing at least \(c/8\). Write \(f=\epsilon |f|\) on \(S_*\), and \(g/\sqrt n\in[0,C_g]\) on \(H_\sigma\). The two layer-cake identities and the last lower bound give thresholds \(s\in[0,L)\), \(u\in[0,C_g)\) with
\[
 S'=\{i\in S_*:|f_i|>s\},\qquad R'=\{j\in H_\sigma:g_j/\sqrt n>u\},
 \qquad
 \epsilon\sum_{i\in S',\,j\in R'}K_{ij}\ge \frac{c\,\sqrt n}{8LC_g}.
\]
The thresholds can be taken strictly positive because there are only finitely many levels. Both sets are subsets of \(H\), and \(|H|\le B_0\sqrt n/\eta\). The entry bound and this upper imply a lower of order \(\sqrt n\) for each set. The two stationary signs \(\epsilon,\sigma\) need not coincide, and the sets need not be disjoint. If disjoint sets are useful, the diagonal contributes at most \(O(1)\) by the entry bound and the size bound. Assign sites independently to two classes and retain only pairs from the first class on \(S'\) to the second on \(R'\). Each off-diagonal pair is retained with probability \(1/4\), so a deterministic partition keeps a fixed positive fraction of the signed bound. This last refinement gives restrictions of the two levels.

Thus the additional conclusion beyond the [previous real rectangle](cap-overflow-rectangle-104.md) is the actual high-source overlap on the overflow side and the common high stationary set containing both sides. An arithmetic upper \(o(\sqrt n)\) for this restricted signed sum would exclude the obstruction **under** the critical cap-defect rate. The critical rate itself and this upper remain unproved.

## A near-unit compression on the same high set

The independent reviewer supplied the following consequence for every sufficiently small fixed \(\eta\) as above. Write \(g_H=\mathbf1_Hg\), with \(P_H\) the coordinate projection. Since \(S_*\subset H\) and \(g_i\ge\lambda\sqrt n-2\sqrt t\) on \(S_*\), we have \(\|g_H\|_{2,n}^2\ge c_*\sqrt n\) for a constant \(c_*>0\) independent of \(\eta\). Off \(H\), the two bounds
\[
\|P_{H^c}g\|_{2,n},\quad\|P_{H^c}Y\|_{2,n}
     \ll \sqrt{\eta}\,n^{1/4}+1
\]
follow from the low-source estimate and \(|Y_i|\le g_i+2\sqrt t\), with \(O(1)\) cost for either marked entry in normalized second norm. As \(K g=Y\), this also bounds \(\|P_{H^c}K g_H\|_{2,n}\). The exact squared-norm identity for \(K\) now gives
\[
\frac{\|P_H K P_H g_H\|_{2,n}^2}{\|g_H\|_{2,n}^2}
=1-\frac{(\mathbb E_n g_H)^2+\|P_{H^c}K g_H\|_{2,n}^2}{\|g_H\|_{2,n}^2}
\ge 1-C\eta-o(1),
\]
where \(C\) is independent of sufficiently small fixed \(\eta\). The support size budget is \(|H|\le B_0\sqrt n/\eta\), so this provides a quantitative size-versus-gap test on genuine high sets and a positive test vector. A contradiction by this route requires an upper gap stronger than \(C\eta\) at the corresponding size budget.

The same reviewer gave a signed version on the true sign class containing the aligned overflow. Let \(H_\epsilon=\{i\in H:\epsilon Y_i>0\}\), \(h=g\mathbf1_{H_\epsilon}\), and \(f_\epsilon=(b+\epsilon Y)/2\), an exact nonnegative stationary factor. Its centered part is an \(\epsilon\)-eigenvector for \(K\), since \(KY=b-\nu\mathbf1\) and \(Kb=Y\), where \(\nu=\mathbb E_n b\) and \(\mathbb E_n Y=0\). On \(H_\epsilon\), the difference \(h-f_\epsilon\) is uniformly \(O_t(1)\) by \(b-|Y|\le 2\sqrt t\) on the bulk. On the opposite-sign bulk \(f_\epsilon\le\sqrt t\), and on the remaining low bulk its normalized second norm squared costs \(O(\eta\sqrt n+1)\) by the low-source estimate. The mark contributes \(O(1)\) in squared normalized second norm. Thus \(\|h-f_\epsilon\|_{2,n}^2=O(\eta\sqrt n+1)\). On centered rows \(I-\epsilon K\) is positive semidefinite of norm at most two and kills the centered \(f_\epsilon\). Since \(\mathbb E_n h=O(1)\),
\[
 \|h\|_{2,n}^2-\epsilon\langle h,Kh\rangle_{2,n}
 \le (\mathbb E_n h)^2 + 2\|h-f_\epsilon\|_{2,n}^2 .
\]
The overlap \(S_*\subset H_\epsilon\) gives \(\|h\|_{2,n}^2\ge c_*\sqrt n\) as before. Therefore the signed Rayleigh quotient of \(h\) is at least \(1-C'\eta-o(1)\), again with \(C'\) independent of sufficiently small fixed \(\eta\). This test uses a nonnegative high-source vector on one genuine stationary sign class, including an aligned overflow subset of critical size.

1. On the actual set \(H\), test a restricted Jacobi-energy bound using the sign of the true row and the alignment of \(U,Y\) on the overflow side, including the \(\eta\)-dependent size budget for the near-unit test.
2. Seek the cap defect \(O(n^{-1/2})\) from a genuine long pre-exit interval or another estimate on the actual capped fixed point. The proof only consumes this rate and does not generate it.
