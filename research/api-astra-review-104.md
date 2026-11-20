# Adjacent inverse and overflow review

Both API windows returned drafts. [Receipts](api-astra-104-receipts.json) · [Adjacent inverse draft](api-astra-newton-104.txt) · [Overflow draft](api-astra-overflow-104.txt)

## Propagating a translated bound from a given depth

For two genuine predictor depths \(a<b\), take \(E=D_b-D_a\), and use the [physical translated inverse](translated-newton-103.md) \(Z_j=(I-KD_j)^{-1}K\). The direct resolvent identity gives \(Z_b=Z_a+Z_b E Z_a\). If \(\delta_j=\max_{i,k}|(Z_j)_{ik}|\) and \(\|Z_b\|_{2\to2}\le z\), the two unsigned consequences are
\[
 \delta_b\le\frac{\delta_a}{1-\delta_a\|E\|_1}
 \quad(\delta_a\|E\|_1<1),\qquad
 \delta_b\le\delta_a(1+z\|E\|_2).
\]
The first uses entry bounds on both ends, and the second uses the row second norm on the left and the entry bound on the right. Both norms of \(E\) here are the unnormalized norms of its diagonal.

If actual increments are bounded in normalized second norm by \(Lq^j\), and the scalar curvature on their segments is at most \(C\), then
\[
 \|E\|_1\le CnL(q^a-q^b)/(1-q),\qquad
 \|E\|_2\le C\sqrt n L(q^a-q^b)/(1-q).
\]
Thus the draft's first test requires \(n^{1-\beta}q^a\) sufficiently small if \(\delta_a=O(n^{-\beta})\) is known at depth \(a\). Its expression with \(n^{1/2-\beta}\) assumes a prime-uniform **unnormalized** initial second norm, whereas the supplied physical initial bound is normalized. The two estimates here require a translated bound at the starting depth. They do not promote the available fixed-height estimates to the needed increasing depth. A signed incremental \(O(n^{-\beta}q^j)\) bound on \(Z_{j+1}(D_{j+1}-D_j)Z_j\) would suffice once the physical geometry and contraction hold across those depths.

## Overflow comparison and a prescribed obstruction on the correct kernel

In the [real cap setting](real-cap-exterior-103.md), the marked site contributes no overflow eventually. On the bulk overflow write \(A=\sqrt{M^2+4t}\). Then
\[
 \tau_iU_i=A|\tau_i|+\tau_i^2\le (U_i^2-M^2)_+,
 \qquad \|\tau\|_{2,n}^2\le\alpha .
\]
Consequently
\[
 \mathbb E_n\tau_iY_i
       \le \alpha+\sqrt\alpha\,\|Y-U\|_{2,n}.
\]
In particular a sufficiently small normalized second distance suffices. A bound on actual \(Y_i\) off the mark, together with the cap for \(C\), allows a bulk Lipschitz constant strictly below one. The trivial physical bound \(|Y_0|\le\sqrt p\,\mathbb E_n\Phi_t(Y)=O_t(\sqrt n)\) gives a marked secant gap too since \(t_0=n\); the global Lipschitz factor on the real segments from \(C\) to \(Y\) is then some \(q<1\) independent of \(n\). In that case \(\|Y-U\|_{2,n}\le q\sqrt\alpha/(1-q)\). No such bulk cap or weaker quantitative second distance estimate is supplied.

The draft treats the frequency-space Jacobi kernel \(K\) as a constant-modulus vertex character matrix. That description is incorrect. There is nevertheless a prescribed obstruction on the actual kernel. The marked row has squared norm \(1-1/n\) by \(K^2=I-J_0\) and entries bounded by \(\sqrt3/\sqrt n\). At least \(n/6\) entries of this row have modulus at least \(1/(2\sqrt n)\) for \(n\ge4\), by splitting its squared norm at that threshold. The row is invariant under frequency inversion. Choose an inversion-invariant subset of about \(\sqrt n\) of these entries by taking inverse pairs and excluding the mark and singleton frequencies. Fix \(u>0\) and prescribe \(\tau_i=u\operatorname{sgn}K_{0i}\) on this subset \(S\). To realize it as the overflow of an even mean-zero trial, put \(U_i=(A+u)\operatorname{sgn}K_{0i}\) there, set \(U_0=0\), and choose a single compensating constant on the remaining bulk with modulus \(O(n^{-1/2})<M\). Then
\[
 \alpha=\frac{|S|}{n}(4t+2Au+u^2)=O(n^{-1/2}),\qquad
 (K\tau)_0\ge \frac{u\,|S|}{2\sqrt n}.
\]
This trial need not solve the capped fixed equation. It shows why a proof from the actual Jacobi entry moments and the mean cap defect alone cannot furnish \(\max K\tau=o(1)\). The [critical rectangle deduction](cap-overflow-rectangle-104.md) instead uses both genuine stationary equations and identifies a restricted positive receiving set.

The returned next tests were a signed incremental inverse kernel with the actual normalization, and the signed overflow interaction or a real stationary second norm bound. The review narrows both to the genuine data above.
