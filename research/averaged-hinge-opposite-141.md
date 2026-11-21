# Testing the averaged hinge against an actual opposite optimizer

Use the actual mean-one projected row \(Z=X/M\) and its pinned hinge correction from [Round 140](averaged-completion-dual-140.md#the-signed-cost-for-one-explicit-repair). Put \(u=T^{-1/3}\), \(d_i=(u-Z_i)_+\) on the bulk, \(d_0=0\), and \(Z'=Z+2L_\sigma d\). Write \(a=X_0\). For any actual ordinary opposite optimizer \(F\) of mean one, let \(q_*=F_0=\theta_{-\sigma}\) and \(\lambda=F-q_*e_0\). Pairings use normalized counting measure. The sector equations and exact pinning give
\[
 \mathbb E(\lambda Z')=1-\frac{q_*a}{nM},\qquad
 \mathbb E(\lambda\,\sigma Kd)
    =\mathbb E d-\mathbb E(Fd)-\sigma q_*\,\mathbb E((Ke_0)d).
\]
The second formula uses \(KF=-\sigma(F-\mathbf1)\). The last term is \(O(\mathbb E d)\) since \(q_*\le 1+\sqrt p\) and \(\|Ke_0\|_\infty\le\sqrt p/n\). Inserting the actual bulk bound \(Z'\ge u+\sigma Kd-O(\mathbb E d)\) and \(\mathbb E\lambda=1-q_*/n\) gives
\[
 \boxed{\displaystyle
 1-\frac{q_*a}{nM}\ \ge\
 u(1-q_*/n)-\mathbb E(Fd)-O_\tau(T^{-2/3}).}                 \tag{1}
\]

One may choose \(F\) within the true opposite optimal face. A prime-uniform estimate \(\mathbb E(Fd)=o(1)\) for such a choice on each sign and inside the actual growing marked window would suffice. Indeed (1) and \(\theta_\sigma q_*=n\) give \(\theta_\sigma\ge a/[M(1+o(1))]\). In that window \(a=1+o(1)\) and \(\limsup\sqrt n M\le\sqrt{1+\tau}\). Applying the bound to both signs and then taking \(\tau\downarrow0\) gives the proposed original normalized limit. This route avoids controlling the maximum of the signed Jacobi image. It also avoids a stronger uniform bulk energy claim. The weighted estimate itself remains open.

An intermediate stronger sufficient condition is \(\inf_{i\ne0}\sigma(Kd)_i\ge-o(1)\). The reflected row then has bulk minimum at least \(-o(1)\), and adding \(o(1)k\) in mean-one scale repairs it with unchanged mark. The corresponding raw extra mean is \(o(n^{-1/2})\). Thus an explicit negative bound of order \(T^{-1/3}\) is needed only for completing with the original exact mean by one reflection.

The same identities explain a genuine square-order obstruction. On the eligible square family \(p=r^2\) in the field-size notation and on the minus side, \(q_*=\theta_+=r-1\). Thus \(q_*/\sqrt n\to\sqrt2\), whereas the actual square marks have \(a\to1\) inside the same proved growing marker window. For each fixed \(0<\tau<1\), (1) gives
\[
 \liminf \mathbb E(Fd)\ge \sqrt{\frac{2}{1+\tau}}-1>0.
\]
This uses the true square opposite optimizer and its true hinge, although \(\mathbb E d=O_\tau(T^{-2/3})\). It isolates a need for prime-specific arithmetic in the weighted estimate. It gives no analogous lower bound for ordinary primes. [Square optimum and mark budget](averaged-mark-35.md) · [Simultaneous prime and square marked window](parallel-depth-window-30.md)

## One actual weighted error remains after the hinge split

Write \(Z=U_\sigma+e_\sigma\) using the actual positive time average and endpoint correction. Since \(U_\sigma U_{-\sigma}\ge c_\tau>0\) and \(\mathbb E U_{-\sigma}=1\), the set \(U_\sigma<2u\) has relative size \(O_\tau(u)\). Squaring the split \(d\le(2u-U_\sigma)_++(-e_\sigma-u)_+\) and using \(\mathbb E e_\sigma^2=O_\tau(T^{-1})\) gives
\[
 \mathbb E d^2=O_\tau(u^3+T^{-1})=O_\tau(T^{-1}).
\]
For the actual opposite optimizer the same split gives
\[
 \mathbb E(Fd)
 \le 2u+\frac{\mathbb E(F e_\sigma^2)}{4u}.
\]
The first term is automatic from \(F\ge0\) and \(\mathbb E F=1\). Thus an extra weighted small-ball estimate for \(U_\sigma\) is unnecessary for this reduction. The remaining sufficient error estimate is \(\mathbb E(F e_\sigma^2)=o(u)\). One may instead use \(\mathbb E(Fd)\le u+\mathbb E[F(-e_\sigma)_+]\). Both use the exact \(F\), not a surrogate with chosen support.

## A terminal activation test without a positive-part hinge

On the actual Picard orbit let \(\phi_j=\Phi(v_j)\), \(g_T=\phi_T-\phi_0\ge0\), and \(\mu_j=\mathbb E\phi_j/2\). The correct endpoint identity and \(v_{T+1}-v_1=Kg_T\) imply exactly
\[
 e_\sigma
 =\frac{\sigma P_{-\sigma}(v_{T+1}-v_1)}{2TM}
 =-\frac{P_{-\sigma}g_T}{2TM}.
\]
Pair with \(\lambda=F-q_*e_0\), which vanishes at the physical mark. Positivity of \(U_\sigma\) then gives
\[
 \begin{split}
 1-\frac{q_*a}{nM}
 &=\mathbb E[\lambda(U_\sigma+e_\sigma)]\\
 &\ge
 -\frac{\mathbb E(Fg_T)-\mathbb E g_T
             -q_*\,\mathbb E[(P_{-\sigma}e_0)g_T]}{2TM}.
 \end{split}                                                      \tag{2}
\]
Let \(s=-\sigma\) and \(\Delta v=v_{T+1}-v_1\). Substitution of \(P_s=(I-J+sK)/2\) shows that the numerator on the right of (2), after taking the negative sign, is exactly
\[
 -\mathbb E[1_{\{i\ne0\}}F g_T]
 +\left(1-\frac{q_*}{2n}\right)\mathbb E g_T
 +\frac{q_*}{2n}\bigl(s\Delta v_0-g_T(0)\bigr).
\]
The unweighted mean term is nonnegative. Since \(q_*=O(\sqrt p)\) and \(M\gg_\tau n^{-1/2}\), the last term after division by \(2TM\) is \(O_\tau(T^{-1/2})\) on any exact prefix. Here \(g_T(0)\le |v_T(0)|\), \(|v_j(0)|\le 2\sqrt p\,\mu_{j-1}\), and the energy identity gives \(\mu_j=O_\tau(\sqrt{(j+1)/n})\). In the simultaneous marked window with \(T+1\) included, \(\max_{j\le T+1}|v_j(0)|=O_{\tau,B}(T^{-B})\) for the chosen \(B\). Thus the improved bound in that window is
\[
 \boxed{\displaystyle
 1-\frac{q_*a}{nM}\ \ge\
 -\frac{\mathbb E[1_{\{i\ne0\}}F g_T]}{2TM}
 -O_{\tau,B}(T^{-B-1}).}                                         \tag{3}
\]

Consequently \(\sqrt n\,\mathbb E[1_{\{i\ne0\}}F g_T]/T=o(1)\) for each actual opposite sign inside the proved marked window gives the original squeeze after \(\tau\downarrow0\). The two signs may use different growing times inside that window. This terminal test is equivalent, within the window, to a linear signed correlation:
\[
 \frac{\sqrt n}{T}s\,\mathbb E(F\Delta v)=o(1).
\]
Indeed \(\mathbb E[1_{\{i\ne0\}}F g_T]=\mathbb E g_T+s\mathbb E(F\Delta v)-q_*g_T(0)/n\) by the exact opposite-sector equation. The first and last terms, after multiplication by \(\sqrt n/T\), are \(O_\tau(T^{-1/2})\) or smaller. The terminal condition is distinct from the sufficient weighted hinge estimate. Neither weighted bound is established here. On the true eligible square minus side (3) forces the lower bound
\[
 \liminf\frac{\sqrt n}{T}\mathbb E[1_{\{i\ne0\}}F g_T]
 \ \ge\ 2\bigl(\sqrt 2-\sqrt{1+\tau}\bigr)>0
\]
in the actual simultaneous growing window at \(0<\tau<1\). This follows by multiplying (3) by \(2\sqrt n M\), using \(q_*a/\sqrt n\to\sqrt 2\) and the upper bound on the true mean budget. [Actual mean and endpoint identities](averaged-mark-35.md) · [Weighted projected prefix](astra-completion-37.md)
