# One early companion with a sparse physical deficit mask

One can choose an early true terminal time, hold its unpinned companion fixed, and vary the start of the primary pin. Among logarithmically many admissible lengths there is a physical deficit mask of counting fraction \(O_\delta(1/(d\log D))\), before restricting either persistence or primary density. At the same length a fixed gap costs at least \(c_\delta d\log D/\log\log D\) in pure terminal inverse leverage. This length can be smaller than a fixed multiple of \(D\). At an early time a separate local fourth-moment upper on the true face brings the actual inverse leverage below the polynomial weighted-hinge threshold.

## Delaying the start at a prescribed terminal companion

Let \(D=D(p)\) be the inherited marked depth, \(n=(p-1)/2\), and \(0<\delta\le1\) fixed. Write \(E_j=\|v_j\|_2^2\), \(Y_j=\sqrt n v_j\), \(g_j=\sqrt n\,\overline{\phi_j}/2\) for the actual zero-floor orbit. The exact energy identity is \(E_{j+1}-E_j=4(1-g_j^2)\), with \(0\le E_j\le4j\). Maximize \(E_j+\lambda j\) on \(0\le j\le J=\lfloor D/13\rfloor\), where \(\lambda=\delta/16\). At any maximizing index \(T\) take \(b=T-2\). Then
\[
  T\ge\lambda J/(4+\lambda),\quad
  E_k\le E_T+\lambda(T-k)\quad(0\le k\le T),\quad
  E_{T-v}\ge E_T-4v.
\]
Also \(\sum_{j=T-3}^{T-1}g_j^2=3+(E_{T-3}-E_T)/4\le3(1+\lambda/4)<4\).
Thus \(b\asymp_\delta D\), \(b\le D/13\), and its three neighboring means are below two. This uses the actual energy and selects the same time for both signs.

Take any length \(d\le b\) with \(d\to\infty\), put \(a_0=b-d+1\), \(\theta=(2d-1)^{-1}\), and set \(\omega_{a_0}=\cdots=\omega_{b-1}=2\theta,\ \omega_b=\theta\). From the telescope,
\[
  G_\omega^2\le\sum_j\omega_jg_j^2
   =1+\frac{2E_{a_0}-E_b-E_{b+1}}{4(2d-1)}
   \le1+\frac{2\lambda(d+1)+12}{4(2d-1)}.                 \tag{1}
\]
The marked factors \(m_s^\omega=1+o(1)\) uniformly by the inherited prefix theorem. Pin with \(\epsilon=\delta/8\). By (1) the coefficient \((1+\epsilon)m_s^\omega-G_\omega\) exceeds a fixed positive multiple of \(\delta\). The early scalar term in the exact paired formula is bounded below by \(-\theta g_{a_0-1}\). In fact \(\sum_{a_0-1}^{T-1}g_j^2\le(1+\lambda/4)(T-a_0+1)\), so this cost is \(O(d^{-1/2})\). The other scalar, multiplied by \(\theta\), is \(O(1/d)\) by the three good means. The bulk pin direction tends uniformly to one. Hence the coefficient identity of round 79 gives, for the actual opposite pin \(R_{s,d}\) and the single true companion \(Z=Z_{-s,b}\),
\[
 R_{s,d}+\theta Z\ge0\quad\hbox{on the exterior}.
\]
Write \(r_d=(R_{s,d})_-\) there, zero at the mark, \(u=\delta/8\), and \(P_d=\{r_d>u\}\). On \(P_d\), \(Z\ge (2d-1)r_d\). The positive part of \(Z\) on the exterior has normalized first moment \(O(1)\) by the three-time bulk expansion and the good means. The pin is nonnegative as an addition. The normalized second norm of \(r_d\) is at most \(C/\sqrt d\): the weighted displacement before projection in the round-69 identity is
\[
  \theta[(Y_{b+1}-Y_{a_0})+(Y_b-Y_{a_0})].
\]
Each displacement has normalized second norm at most twice the square root of its time span by nonexpansiveness. These estimates hold uniformly even for \(d=o(b)\). [Exact projection and marked pin](timed-pinning-69.md) · [Paired coefficient identity and original good times](terminal-height-79.md) · [Three-time bulk expansion](relative-window-77.md)

## Counting the physical sites and pricing the very high heights

Take all powers of two \(d\) in \([\sqrt b,b]\), numbering \(m\asymp\log D\). Write \(\mathbb E=n^{-1}\sum_i\) and put \(h=Z_+\) on the exterior, zero at the mark. The primary masks may change with \(d\). Their companion is common, so summing the geometric series at each site gives
\[
   \sum_d d\,|P_d|/n\le\sum_d d\,\Pr(h>ud)\ll_\delta\mathbb E h\ll_\delta1.     \tag{2}
\]
For the same lengths put \(L_d=d^2\mathbb E[1_{P_d}r_d^2/(1+h)]\). For every \(A\ge2\),
\[
  L_d\ll \mathbb E[h1_{ud<h\le Ad}]+1/A,\qquad
  \sum_d L_d\ll_\delta \log(2A)+m/A.                                \tag{3}
\]
For the first term use \(r_d\le h/(2d-1)\) on the mask. On \(h>Ad\) use \(1/(1+h)\le1/(Ad)\) and \(\mathbb E r_d^2\ll1/d\). A site belongs to at most \(O_\delta(\log(2A))\) of the displayed height bands. This calculation needs no bound \(\mathbb E h^2=O(d)\), which the single-time energy estimate would imply only with \(b\) in place of \(d\).

Take \(A=m\). At one and the same length, indeed at a positive proportion of the lengths by Markov's inequality,
\[
  \frac{|P_d|}{n}\ll_\delta\frac1{dm},\qquad
  L_d\ll_\delta\frac{\log(2m)}{m}.                                    \tag{4}
\]
The first bound holds for the entire **physical** mask and therefore for any subset satisfying the temporal persistence requirement of round 87, irrespective of the tested primary row or its leverage. One can instead restrict to \([b/B,b]\) for any \(B\to\infty\), \(B\le\sqrt b\), and take \(m\asymp\log B\). There is a fixed-constant consequence at proportional lengths. Given any \(S>1\), choose a sufficiently large integer \(m=m(\delta,S)\), independently of \(p\), and use the \(m\) largest dyadic lengths below \(b\). The same estimates give a length \(d\ge 2^{-m}b\asymp_{\delta,S}D\) with \(d|P_d|/n\le1/S\) and \(L_d\le1/S\). The proportion constant can shrink with the requested saving. A single fixed range of ratios alone gives no little-oh counting bound.

Now fix a larger-side mark \(a\sqrt n\ge1+\delta\) and any genuine maximizing row \(q\). Opposite orthogonality at this same pin gives \(q(r_d1_{P_d})\ge m_s^\omega(\sqrt n a-1-\epsilon)-u\gg_\delta1\). For the pure terminal charged energy \(V_d(q)=(n/d)\sum_{P_d}(1+h_i)q_i^2\), Cauchy–Schwarz gives
\[
     q(r_d1_{P_d})^2\le V_d(q)L_d/d.
\]
Thus (4) forces the **entire** true marking face, including the actual pure inverse-norm minimizer, to pay
\[
        \ell_{+,d}^{-1}\ge1+\min_q V_d(q)\gg_\delta
                      d\,m/\log(2m).                                  \tag{5}
\]
The same length gives \(\mathbb E[r_d1_{P_d}]\ll_\delta1/(d\sqrt m)\), by its normalized second norm and (4). Hence every such row pays a fixed deficit, and order-\(d\) companion height, on \(P_d\cap\{nq_i>c_\delta d\sqrt m\}\): the discarded low densities cost at most \(c_\delta d\sqrt m\,\mathbb E[r_d1_{P_d}]\). The same subtraction works after any deletion for which a fixed deficit lower has already been proved.

The opposite sign's terminal field also satisfies (2)–(3); summing all four normalized tests selects a common length for both signs if desired. In the fixed-constant variant, one can thus force \(\ell_{+,d}^{-1}>C d\) for any prescribed \(C\) at a \(D\)-proportional length, with comparability allowed to depend on \(C,\delta\). The ratio gain in (5) uses a weighted estimate in addition to the small counting fraction. The result rules out a fixed-gap sequence with moderate inverse at *every* length of this adaptive family. It supplies no polynomial inverse upper on unrestricted faces. [Pure terminal norm and persistent paying sites](astra-terminal-87.md)

## A local fourth-moment certificate for a polynomial inverse upper

Use any original early good window of round 86, or the tilted endpoint and any growing length above. Put \(M=1-a\), \(H\) the half-height tower of round 83, \(\alpha=H^{-1/4}\), and \(t=\alpha M/\sqrt n\). Write \(P=P_d\), \(X_i=nq_i\), and \(Q_F(q)=\mathbb E[X^4 1_F]\). For fixed \(0<\xi<12/13\) allow every \(K\ge2\) with \(\log_2^*K\le(12/13-\xi)\log_2^*p\). Then
\[
    \boxed{\quad\min_{q\in\mathcal Q_a}Q_P(q)=O(nK^2)
                 \quad\Longrightarrow\quad \ell_+^{-1}=o(nt).\quad}       \tag{6}
\]
The minimization is convex and admits an even solution. This is an upper for the actual norm on the face. In particular a single comparison row with \(nq_i\le n^{1/3}K^{2/3}\) on the mask except for \(O(K^2)\) arbitrary sites suffices. Those exceptional sites can attain the true point cap. A row-independent, finite-LP sufficient test bounds the number of \(i\in P\) for which \(n s_i>n^{1/3}K^{2/3}\), where \(s_i=\max_{q\in\mathcal Q_a,\ q\ {\rm even}}q_i\). If only \(O(K^2)\) such sites occur, every even comparison row qualifies.

For the proof, apply the finite arithmetic approximation to the three adjacent true iterates at precision \(K'=K/\alpha\). The tower height of \(K'\) is at most \(\max(\log_2^*K,(\log_2^*p)/2)+O(1)\), and \(b\le D/13+O(1)\) leaves a fixed relative margin. Replacing their signed positive parts in the bulk expansion, and then taking a positive part, gives a bounded bulk approximation to \(h\) of supremum \(U=O(1+\log\log p)\) and normalized second error \(o(\alpha/K)\). In particular for every \(F\subset P\)
\[
   d V_F(q)\le (1+U)Q_F(q)^{1/3}+o(\alpha/K)\,Q_F(q)^{1/2}.            \tag{7}
\]
Here \(\mathbb E[X^2 1_F]\le Q_F^{1/3}\) by interpolation with \(\mathbb E[X1_F]\le1\). For \(Q_F=O(nK^2)\) the right side is \(o(\alpha\sqrt n)\), since \(U,K,1/\alpha\) are at most fixed powers of \(1+\log\log p\) eventually. At \(F=P\) the remaining exterior contribution to the full inverse norm on the trial row is at most \(1/d\) by the point cap. This proves (6). Below the proposed density cutoff, \(X^4\le nK^2 X\); each arbitrary exceptional site contributes \(O(n)\) to \(Q_F\) because \(a=O(1/\sqrt n)\). [Physical approximation at the earlier terminal time](astra-leverage-86.md) · [Weighted-hinge branch threshold](astra-terminal-87.md)

There is also a necessary localized lower along *any* sequence with \(\ell_+^{-1}\gtrsim nt\). For every true optimizer and every \(|A|\le K^2\), let \(G=P\cap\{X>n^{1/3}K^{2/3}\}\setminus A\). Uniformly in these choices,
\[
                       Q_G(q)/(nd^2K^2)\longrightarrow\infty.             \tag{8}
\]
Indeed \(P\setminus G\) has fourth moment \(O(nK^2)\) by the same two bounds. Its cost is \(o(nt)\) by (7), and the full inverse bound forces \(V_G(q)\gtrsim nt\). Mass bounds the counting fraction of \(G\) by \(n^{-1/3}K^{-2/3}\). The bounded approximation and its error give \(\|(1+h)1_G\|_{2,n}=o(\alpha/K)\), so \(dV_G\le o(\alpha/K)\sqrt{Q_G}\). This proves (8). On a window satisfying (6) the selecting weighted-hinge optimizer of round 87 pays a fixed deficit on its low sites and hence order-\(d\) companion height there. The finite envelope and deletion argument use only the good neighbors and the early approximation. No fourth-moment bound on that particular selecting row is required.

## Finite checks

At \(p=97\), maximizing \(E_j+j/256\) through \(j=24\) gives the strict maximum \(T=13\), hence \(b=11\). With finite allowance \(1/20\) and cutoff \(1/100\), the masks at lengths \(2,4,8\) have respectively \(10,6,2\) sites on the same companion. Its positive exterior mean is \(0.890942991\ldots\); the three values of \(L_d\) are \(0.001421950\ldots, 0.001302536\ldots, 0.000290317\ldots\). The checker verifies the energy telescope, positive pin increments, the paired inequality on every bulk site, and the projected defect second norm for all three starts.

At \(p=97,b=d=4\), using the previous zero-allowance finite pin and cutoff \(1/100\), the genuine plus even face has two nonnegative anchor parameters. At their origin both first derivatives of \(Q_P\) are strictly positive. Convexity and reflection certify its whole-face minimum \(15.511698750\ldots\). The same row gives the genuine pure inverse minimum \(2.492042059\ldots\). Using the exact masked collision in (7) and a clipping height \(2.72\), the finite upper is \(2.503980874\ldots\): bound the excess \((h-2.72)_+\) by its normalized second norm times \(\sqrt{Q_P}\) and keep the true uncharged cost. The even-face exterior coordinate capacities \(s_i=\max_{q\text{ even}}q_i\) sum to \(1.010374910\ldots\); exactly \(22,8,2,0\) exceed \(1/n,2/n,4/n,8/n\). Individual coordinate maxima can occur on different genuine rows. The checker encloses the whole feasible polygon by rational halfspaces and evaluates feasible interior perturbations for all coordinate lower bounds. These finite values do not check the asymptotic height or gap assumptions. [Arb384 checker](astra-persistent-88-check.py) · [Outward intervals](astra-persistent-88-checks.jsonl)

1. Minimize the masked fourth moment, or certify the clipped comparison directly, on the actual face at the same adaptive sparse-mask window in (4). An upper of the form (6) would force the low-site weighted-hinge payment, in a regime where (5) already quantifies the loss of moderate leverage.
2. Bound the surviving low-density deficit on that window using its actual opposite pin and the measured charge beyond the height cutoff. For restriction to \(d\asymp D\) with a fixed comparability constant one needs another selector or a single-height counting estimate. The dyadic saving here requires \(b/d\) to range over a growing factor.
