# Initial sources of actual repair deficits

Fix \(\tau>0\), and use \(T=T(p)\to\infty\) with \(T+1\) in the actual simultaneous marked window. Norms and expectations have divisor \(n=(p-1)/2\). The projected average is \(Z=X_{\sigma,T}/M=U_\sigma+e_\sigma\), with \(U_\sigma\) the positive time average and \(e_\sigma\) the signed endpoint error. The [Round 141 bounds](averaged-hinge-opposite-141.md) give \(U_\sigma U_{-\sigma}\ge c_\tau>0\), \(\mathbb E U_{-\sigma}=1\), and \(\|e_\sigma\|_2^2=O_\tau(T^{-1})\). Under a fixed hypothetical gap let \(F\) be a true opposite mean-one optimum with mark \(q\ge(1+\eta)\sqrt n\), where \(\sqrt{1+\tau}<1+\eta\). A true complementary optimum \(R\) has \(R_0=n/q\) and \(FR=0\) on the bulk.

## Restricting both coordinates of the first spill

For the [first reflection](ordinary-pinned-reflection-flow-148.md), put \(u=T^{-1/3}\), \(d_i=(u-Z_i)_+\) off the root and \(d_0=0\). Its support lies in \(\{U_\sigma<2u\}\cup\{|e_\sigma|\ge u\}\) and has relative size \(O_\tau(T^{-1/3})\). Fix \(b_*>0\) sufficiently small compared to the gap lower bound on \(\mathbb E(Fb^{(0)})\). Set \(f=1_{\{b^{(0)}\ge b_*,\, R=0,\,i\ne0\}}(F-H)_+\) for \(0\le H=o(T)\). Dropping smaller deficits costs at most \(b_*\mathbb E F=b_*\) and clipping costs \(O_\tau(\sqrt{H/T})\). The retained output set has density \(O_{\tau,b_*}(T^{-1})\). There \(-\sigma Kd\ge b_*+u/2\), so the signed spill paired against \(f\) has a positive lower bound. We have \(\mathbb E f\le1\), \(\|f\|_2\le\sqrt q\), since an optimum peaks at its mark.

Put \(d_{\rm low}=d1_{\{d\le A\}}\), \(d_{\rm high}=d1_{\{d>B\}}\). Then
\[
 |\mathbb E(fKd_{\rm low})|\ll_\tau
 n^{1/4}\min\{A T^{-1/6},\sqrt{A T^{-2/3}}\},\qquad
 |\mathbb E(fKd_{\rm high})|\ll_\tau \sqrt n/(TB).
\]
Use \(\|K\|\le1\) and either the support bound or \(\mathbb E d_{\rm low}^2\le A\mathbb Ed\) for the first estimate. Use \(|K_{ij}|\le\sqrt p/n\) and \(\mathbb E d_{\rm high}\le\mathbb E d^2/B\) for the second. The two marked coordinates are absent. Deleting the diagonal of any such pairing costs at most \(q\mathbb E d/n=O_\tau(n^{-1/2}T^{-2/3})\). Taking \(A=n^{-1/4}\), \(B=\sqrt n\,T^{-2/3}\) removes these ranges at costs \(O_\tau(T^{-1/6})\) and \(O_\tau(T^{-1/3})\). The cutoffs are ordered in the marked window. A gap still forces a positive signed sum on the remaining distinct bulk pairs. Bounds on individual levels need summable errors or a common bound for their sum.

## The static model matches the unnormalized cost

Let \(z_0=Z_0\), \(g=qz_0/n-1\asymp_{\tau,\eta}1\), \(D=\mathbb E[1_{\rm bulk}F^2]\), and \(\ell=P_\sigma e_0\). The first reflected deficit costs at least \(g\) and has squared norm \(O_\tau(T^{-1})\). Therefore \(D\gg_{\tau,\eta}T\), while \(D\le q=O(\sqrt n)\). For \(b=(g/D)(F-qe_0)\) put \(r=\mathbb E b\), \(B=-\ell^{\mathsf T}b/\ell_0\). Then
\[
 L_\sigma b=0,\quad (b+Be_0)/(r+B/n)=F,\quad
 \mathbb E(Fb)=g,\quad r\asymp_{\tau,\eta}D^{-1},\quad
 \|b\|_2^2=g^2/D .
\]
Also \((z_0-1)B/n-r=\|b\|_2^2\), the scalar stationary contact equality. The [Round 149 phase identity](ordinary-averaged-repair-dual-149.md#constraints-on-the-same-selected-prime-deficit) gives phase ratio \(q/\sqrt p+o(1)\). These identities are conditional on a gap and use the same true optimizer as the original unscaled cost. The scalar descriptors are compatible with a gap. This vector has no demonstrated negative-part history.

## Retargeting the mark before relaxed repair

Put \(\delta=T^{-1/6}\), \(z_*=(1+\delta)n/q\), \(k=\mathbf1-\ell/\ell_0\) and \(\lambda=1-z_*/z_0\). The gap, marked mean bounds and cap separate \(\lambda\) from zero and one. Then \(x=(1-\lambda)Z+\lambda k\) is mean one, in sign sector \(\sigma\), with mark \(z_*\). Write \(x=V+(1-\lambda)e_\sigma\), where \(V=(1-\lambda)U_\sigma+\lambda k\ge2c>0\) on the bulk for fixed \(c=c_{\tau,\eta}\). The initial bulk negative part has squared norm, mean and relative support size all \(O_{\tau,\eta}(T^{-1})\), by the second moment of \(e_\sigma\) and the fixed reserve.

Start \(y_0=x\). For fixed \(0<\omega<2\) run \(b_j=1_{\rm bulk}(-y_j)_+\), \(y_{j+1}=y_j+\omega L_\sigma b_j\). Each \(\mathbb E(Fb_j)\ge\delta\) by the pinned affine constraints, so \(r_j=\mathbb E b_j\ge\delta/q\). Set \(B_j=-\ell^{\mathsf T}b_j/\ell_0\), \(s_j=(z_*-1)B_j/n-r_j\), and \(U_*=\mathbf1+(z_*-1)\ell/\ell_0\). The [Round 149 arguments](ordinary-averaged-repair-dual-149.md) give \(\|x-U_*\|_2=O_{\tau,\eta}(\sqrt T)\), \(|s_j|\ll_{\tau,\eta}r_j\), \(\sum_{j<m}\|L_\sigma b_j\|_2^2=O_{\tau,\eta,\omega}(T^{-1})\), and \(\sum_{j<m}s_j\ge-O_{\tau,\eta,\omega}(T)\).

With \(\epsilon=T\sqrt n/(m\delta)\) and \(v=n/(mT\delta^2)\), the probabilities proportional to \(r_j\) give averages \(s_j/r_j\ge-O(\epsilon)\) and \(\|L_\sigma b_j\|_2^2/r_j^2\le O(v)\), respectively. Discard steps with \(\|L_\sigma b_j\|_2/r_j>v^{1/3}\), of total probability \(O(v^{1/3})\). Boundedness of \(|s_j|/r_j\) gives a retained step with \(s_j/r_j\ge-O(\epsilon+v^{1/3})\). Choose \(m=n^2\), for which \(\epsilon+(\sqrt T+n^{1/4})v^{1/3}=o(\delta)\) in the proved growing window.

At this step \(B_j>0\) and \(G=(b_j+B_je_0)/(r_j+B_j/n)\) is nonnegative of mean one. Its wrong-sector projection has norm at most \(v^{1/3}\) and root zero. Its marked value satisfies \(G_0\ge(1-O(\epsilon+v^{1/3}))q/(1+\delta)\). For every true complementary \(R\),
\[
 G_0/q\le\mathbb E(RG)=1+\langle R-\mathbf1,P_\sigma G\rangle
       \le 1+O(n^{1/4}v^{1/3}),\qquad
 \mathbb E(Rb_j)/r_j=O_{\tau,\eta,\omega}(\delta).
\]
For the last bound subtract the marked contribution \(G_0/q\) and use \(B_j/(nr_j)=O(n^{-1/2})\). Thus \(G_0/q=1+O(\delta)\) and the completed-root identity gives \(\mathbb E(b_jc_\sigma)/r_j=q/\sqrt p+O(\delta)\).

## Signed endpoint forcing at the same actual step

The starting-row pairing is \(\langle b_j,x\rangle=-s_j+\langle L_\sigma b_j,x-U_*\rangle\), so \(\langle b_j,x\rangle/r_j\le O(\epsilon+v^{1/3}\sqrt T)=o(1)\). Using \(t_+\ge t\) and \(V\ge2c\) gives
\[
 \frac{\mathbb E[b_j (-(1-\lambda)e_\sigma-c-\delta^{-1/2}R)_+]}{r_j}
 \ge c-o(1)
\]
for every true complementary \(R\). The penalty costs \(O(\sqrt\delta)\). The positive part is supported on \(S_R=\{i\ne0:-(1-\lambda)e_\sigma>c+\delta^{-1/2}R\}\), with density \(O_{\tau,\eta}(T^{-1})\) and bulk norm \(O_\tau(T^{-1/2})\) for the positive part. Cauchy–Schwarz gives \(\mathbb E[1_{S_R}(b_j/r_j)^2]\gg_{\tau,\eta}T\). The effective support \(nr_j^2/\mathbb E b_j^2\) is \(O_{\tau,\eta}(n/T)\). The relative pinned projection tends to zero, so the same support is at least \((1-o(1))n/\sqrt p\) and obeys the [Round 20 prime dichotomy](anchored-repair-20.md#a-uniform-single-step-gap-for-concentrated-prime-defects).

The output root is absent. Expanding \(e_\sigma=-P_{-\sigma}g_T/(2TM)\) permits removal of the input root at uniform \(o(1)\) bulk cost, by the marked bound on \(g_T(0)\), the bulk projector entry bound, and \(M\gg_\tau n^{-1/2}\). The positive-part pairing is Lipschitz under this change because \(b_j/r_j\) has mean one.

This uses a real iterate of the new flow started from the retargeted \(x\), which depends on the true \(q\). The approximate opposite row and signed error mask differ from the near-cap mixtures and activation mask of [Round 147](ordinary-oriented-terminal-mask-147.md). The static vector with \(g\) replaced by \(\delta\) can pay this endpoint cost in the prescribed affine space as well. Its relation to \(x\) is \(\langle b,x\rangle/r=-\delta/(1-q/n)\), and \(\mathbb E(Rb)=0\). A prime exclusion still needs a uniform weighted endpoint estimate or control of the exact negative-part dependence.
