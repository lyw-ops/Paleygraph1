# Motion in the actual retargeted repair

Use the [Round 150 flow](ordinary-prime-repair-source-150.md) with an ordinary prime \(p\), \(n=(p-1)/2\), fixed \(0<\omega<2\), \(T,T+1\) in the simultaneous marked window, and hypothetical fixed ordinary gap. Expectations and norms have divisor \(n\). Its initial row \(x\) uses the actual true optimum \(q\) and mark \(z_*=(1+\delta)n/q\), where \(\delta=T^{-1/6}\). Let \(F\) be any true opposite optimum and \(R\) any true complementary one. All \(y_j\) have mean one and the same mark and sector. For \(b_j=1_{\rm bulk}(-y_j)_+\), the exact affine identity is
\[
 \mathbb E(Fb_j)=\delta+\mathbb E[1_{\rm bulk}F(y_j)_+]\ge\delta.
\]
Indeed \(\mathbb E(Fy_j)=1\), of which the marked coordinate contributes \(qz_*/n=1+\delta\). The marked term is essential when passing to the negative part.

## Exact secant dissipation

Put \(L=L_\sigma\), \(u_j=Lb_j\), and \(y_{j+1}=y_j+\omega u_j\). On a bulk coordinate choose \(\theta_{j,i}\in[0,1]\) so that the difference of the two negative parts is \(-\theta_{j,i}(y_{j+1,i}-y_{j,i})\), taking zero when the two inputs agree. Set \(\theta_{j,0}=0\) and \(D_j=\operatorname{diag}(\theta_{j,i})\). Then
\[
 b_{j+1}-b_j=-\omega D_j u_j,\qquad
 u_{j+1}=(I-\omega L D_j L)u_j.
\]
The self-adjoint operator \(A_j=LD_jL\) obeys \(0\le A_j\le I\). Therefore
\[
 \begin{split}
 \|u_j\|_2^2-\|u_{j+1}\|_2^2
 &=2\omega\langle u_j,A_j u_j\rangle-\omega^2\|A_j u_j\|_2^2\\
 &\ge\omega(2-\omega)\|D_j^{1/2}u_j\|_2^2
 \ \ge\ (2-\omega)\omega^{-1}\|b_{j+1}-b_j\|_2^2 .
 \end{split}
\]
This holds across changes of the negative set, for either sector and any starting point in the affine space. In particular \(\|u_j\|_2\) is nonincreasing and
\[
 \|b_{j+k}-b_j\|_2\le \sqrt{k\omega/(2-\omega)}\,\|u_j\|_2 .
\]
The factor \(\sqrt k\) follows by summing the squared displacements and applying Cauchy–Schwarz. Thus at any step with \(\|u_j\|_2=o(\mathbb Eb_j)\), two consecutive steps automatically have relatively unchanged negative mass and small relative projected motion. These conditions by themselves supply no flattening estimate.

## A block with the same masked endpoint lower bound

Choose the actual step \(j\) of Round 150 by taking \(m=n^2\). Put \(r_j=\mathbb E b_j\) and \(\varepsilon=n^{-1/3}T^{-2/9}\), so \(\|u_j\|_2/r_j\le\varepsilon\). Continue the same flow for any \(0\le k\le\lfloor n^{2/3}T^{1/9}\rfloor\), beyond its initial selection horizon if necessary. Then
\[
 \|b_{j+k}-b_j\|_2=O_\omega(\delta r_j),\qquad
 r_{j+k}/r_j=1+O_\omega(\delta),\qquad
 \|u_{j+k}\|_2/r_{j+k}=O_\omega(\varepsilon).
\]
The bulk entries of \(\ell=P_\sigma e_0\) are \(O(n^{-1/2})\). Consequently the normalized completed marked value from \(B_i=-\ell^{\mathsf T}b_i/\ell_0\) changes by at most \(O_\omega(\delta\sqrt n)\), and \(B_i>0\) at these steps. Each completed mean-one row still has mark \(q(1+O(\delta))\), opposite projection error \(O(\varepsilon)\) vanishing exactly at the mark, and \(\mathbb E(R b_i)/r_i=O(\delta)\). For the last assertion use the exact complementary marked contribution, and \(n^{1/4}\varepsilon=o(\delta)\), as in Round 150.

For any such \(R\), keep the original positive-part cost \(C_R=1_{\rm bulk}(-(1-\lambda)e_\sigma-c-\delta^{-1/2}R)_+\). It has norm \(O_\tau(T^{-1/2})\) and support density \(O_{\tau,\eta}(T^{-1})\). Pairing the unnormalized difference \(b_{j+k}-b_j\) with \(C_R\) costs \(O(\delta r_j T^{-1/2})\). The original lower bound \(\mathbb E(b_j C_R)/r_j\ge c-o(1)\) therefore persists as \(c-o(1)\) after using \(r_{j+k}/r_j=1+O(\delta)\). This works for every true \(R\). Each of these actual iterates has squared mass at least order \(T\) for \(b_{j+k}/r_{j+k}\) on that same signed endpoint mask, and effective support between \((1-o(1))n/\sqrt p\) and \(O_{\tau,\eta}(n/T)\) by the [Round 150 argument](ordinary-prime-repair-source-150.md#signed-endpoint-forcing-at-the-same-actual-step).

The secant estimate uses no prime arithmetic. The prime support restriction continues to apply at every such actual step. To exploit a short block one needs information beyond preservation of mass and near-zero motion. A candidate is a uniform restricted estimate for the true compressed operators \(L D_i L\) or for the actual signed endpoint on the complementary mask.
