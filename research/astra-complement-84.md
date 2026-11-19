# The mixed arithmetic term of two actual complementary optima

For the two true optimal rows the mixed Jacobi coefficient against any bounded test is uniformly of order at most $1/p$, including after removing both root masses. On the first actual transported square the main term at this scale can be computed in normalized mean square over common translations, with error $O(p^{-5/4})$ before scaling. At the specified root, a projection of the actual terminal deficit recovers its one-sided primary price from just this mixed coefficient. A fixed gap forces a negative correction there. The original all-prime conjecture is equivalent to vanishing of the scaled cubic coefficient against the single fixed Jacobi column at the root, as in (7).

## The conditional law and the exterior fields

Write $n=(p-1)/2$, $G=\widehat Q$, $E=n^{-1}\sum_i$, $k(i)=nK_{i0}/\sqrt p$. Let $q,r$ be actual opposite optimal probabilities at the same root, primary sign $s$, root masses $a,b$ with $nab=1$. The hypotheses give $\|q\|_\infty=a,\ \|r\|_\infty=b$, and $a,b=O(p^{-1/2})$. Under translation any opposite pair has overlap $1/n$; at alignment all its overlap sits at the root. [Opposite budgets](astra-localized-71.md) · [Point cap](sector-trim-78.md)

Put $U=s\sum_jq_j k(\cdot-j)=(nq-1)/\sqrt p$ and $V=-s\sum_jr_j k(\cdot-j)=(nr-1)/\sqrt p$. Write $r_t(i)=r_{i+t}$, and similarly for $V$. The weights $\mu_t(i)=nq_i r_{i+t}$ give a probability for every $t$ and $\mu_0=\delta_0$. For any real $f$,
\[
 p E(f U V_t)=\mu_t(f)-q(f)-r_t(f)+Ef.                       \tag{1}
\]
Here a probability acting on $f$ denotes its ordinary expectation. In particular $E(UV_t)=0$, $pE|UV_t|\le4$, and $|p E(fUV_t)|\le2\operatorname{osc}(f)$. The absolute bound follows by majorizing $|nq-1||nr_t-1|$ by $(nq+1)(nr_t+1)$ and expanding.

Use the actual root-trimmed fields
\[
 U_x=(U-sa k)/(1-a),\qquad V_y=(V+sb k)/(1-b),\qquad M=(1-a)(1-b).
\]
The means $E|U|,E|V|\le2/\sqrt p$, the kernel cap $|k|\le1$, and (1) imply
\[
 pM E|U_x (V_y)_t|\le 4+2\sqrt p(a+b)+pab=O(1)               \tag{2}
\]
at every displacement. Thus for bounded $f$ and fixed real $u,v$, the true mixed increment $E[f(e^{uU_x}-1)(e^{v(V_y)_t}-1)]$ is $O_{u,v}(\|f\|_\infty/p)$, using the unit cap on the normalized fields. At alignment $pE(U_x V_y)=1$ exactly. Indeed their normalized exterior source laws $x=(q-a\delta_0)/(1-a)$ and $y=(r-b\delta_0)/(1-b)$ have disjoint supports, and the opposite signs and $K^2=I-J$ give $E(U_xV_y)=-n(\langle x,y\rangle-1/n)/p$. Their independent-angle Haar cross moment is exactly zero since the two sets of centers are disjoint. Thus the arithmetic $1/p$ scale is already sharp on the constant test.

## The leading correction under common translation

For a probability or signed measure $m$ let $T_m f(c)=\sum_i m_i f(c+i)$. Write $f_c(i)=f(c+i)$, $F=f-Ef$, and $A_f=\max_{\xi\ne1}|\widehat f(\xi)|$ with normalized Fourier coefficients on $G$. Transform measures without the normalization. Equation (1) at alignment gives the signed main term
\[
 pE(f_cUV)=F(c)-T_qF(c)-T_rF(c).
\]
The last two functions occupy disjoint nonconstant Fourier sectors. Exactly,
\[
 \|pE(f_cUV)-F(c)\|_{2,c}^2
 =\sum_{\xi\ne1}|\widehat f(\xi)|^2
    (|\widehat q(\xi)|^2+|\widehat r(\xi)|^2)
 \le A_f^2\,[n(\|q\|_2^2+\|r\|_2^2)-2].                       \tag{3}
\]
Here $\|\cdot\|_{2,c}$ uses uniform counting and the norms of measures on the right count masses. Formula (3) gives separate RMS bounds for each one-power error $E(f_c U)=(T_q F)(c)/\sqrt p$ and $E(f_c V)$. For a fixed test with $A_f=O(p^{-1/2})$ they are $O(p^{-3/4})$, uniformly on the two optimal faces. It permits a larger error at a prescribed translation.

The aligned trimmed estimate is
\[
 \big\|pM[E(f_c U_xV_y)-Ef/p]-F(c)\big\|_{2,c}
       \ll A_f n^{1/4}.                                           \tag{4}
\]
To see this, use the signed measure $m_i=pM U_x(i)V_y(i)/n-\delta_{i0}$. Equation (1) and the two root removals give the coordinate identity
\[
 m_i={1+s\sqrt p(a-b)k_i-pab k_i^2\over n}
      -q_i(1-s\sqrt p b k_i)-r_i(1+s\sqrt p a k_i).
\]
Thus $\sum m_i=M-1$, and $\|m\|_2\ll n^{-1/2}+\|q\|_2+\|r\|_2\ll n^{-1/4}$. The residual in (4) equals $T_m F$, with squared normalized norm at most $n A_f^2\|m\|_2^2$.

Apply (3) and (4) to the physical $f=L_1^2$, with $S=2\sqrt n K e_0$ and $L_1=K(S^2/2)$. Here $A_f=O(p^{-1/2})$, uniformly at every nonidentity positional coordinate. In fact the fixed-depth trace representative of $L_1$ is uniformly bounded and differs in normalized second norm by $O(p^{-1/2})$. The square differs from its finite positive middle-convolution representative by the same normalized first-norm bound, including the bounded exceptional characters. Fourier inversion of each raw lift-averaged Mellin trace gives its positional trace on $Q$. All punctual constituents are supported at one. Elsewhere each middle-extension stalk has absolute trace at most its bounded generic rank divided by $\sqrt p$, since the lisse sheaf underlying the weight-zero perverse middle extension has weight $-1$. The first-norm approximation bounds every Fourier coefficient error. This argument uses the same arithmetic square that gave sharp one-field bias in round 83. [Fixed-expression inversion](iteration-parity.md#uniform-fixed-expression-trace-estimates) · [Physical square and representative](weighted-covariance-sharpness-83.md) · [Katz, Chapters 2–5](https://web.math.princeton.edu/~nmk/mellin331.pdf)

Consequently, as functions of the common translation $c$,
\[
 E(f_cUV)={f(c)-Ef\over p}+O_{L^2(c)}(p^{-5/4}),\qquad
 E(f_cU_xV_y)={f(c)\over p}+O_{L^2(c)}(p^{-5/4}).              \tag{5}
\]
For the second formula $M=1+O(p^{-1/2})$ and $f$ is bounded. The [positive variance](astra-centered-78.md#a-square-with-positive-variance-at-unbounded-primes) makes the first mixed term have RMS bounded below by a positive constant times $1/p$. The distribution of the arithmetic error at this scale therefore retains a nonconstant physical square even on the actual optimal pair. Chebyshev bounds the number of translations where the first scaled approximation errs by more than $u>0$ by $O(n(\|q\|_2^2+\|r\|_2^2)/u^2)=O(\sqrt p/u^2)$. The same order follows for the second approximation at fixed $u$. These bounds concern counting translations. The distinguished translation is fixed by the mark.

## A single-primary terminal price at the distinguished translation

For a true round-79 good terminal window with $d\asymp D(p)$, take its actual exterior deficit $f\ge0$, extended by zero at the root. It has $Ef=O(1/d)$, $\|f\|_{2,n}=O(d^{-1/2})$, and a fixed larger-side gap forces $q(f)\gg_\delta1$. Let $P_s=(I-J+sK)/2$, $\pi=(P_s)_{00}\asymp1$, and form the true root-neutral primary test
\[
 h=P_s f-\frac{(P_s f)_0}{\pi}P_s e_0 .
\]
Its root, counting mean and opposite price all vanish, and $\|h\|_{2,n}\le\|f\|_{2,n}$ by orthogonal projection. Pairing first in the primary sector and then with (1) gives
\[
 q(f)=Ef+(a-1/n)\frac{(P_s f)_0}{\pi}-p E(hUV).              \tag{6}
\]
The pin term is $O(d^{-1/2})$ since $|(P_s f)_0|\le\sqrt n\,\|f\|_{2,n}$. In particular every fixed-gap sequence forces $pE(hUV)\le-c_\delta$ on every such window, eventually. For a fixed $q$, every opposite optimum yields precisely the same value in (6). On common translations one has $pE(h_cUV)-h(c)=-T_qh(c)$, whose normalized second norm is $O(d^{-1/2})$ by convolution contraction. At $c=0$ the main term vanishes. The gap must select a translation with an order-one residual in this otherwise small normalized second norm. The stronger $p^{-5/4}$ estimate in (5) applies to the fixed transported square. It has not been established at the prescribed root for $h$. The finite-field identities also apply to eligible square orders, which makes prime-specific control at the actual root necessary. [True terminal norms and payment](terminal-height-79.md#a-tower-scale-deletion-on-the-terminal-height)

## A fixed cubic test at the marked root

Orient $s$ toward the larger optimal mark and put $\gamma=\sqrt n\,a\ge1$, so $\sqrt n\,b=1/\gamma$. Use the fixed Jacobi column $k$ itself in (1). Its mean vanishes, $k(0)=-1/\sqrt p$, and both one-sided prices follow from the sector equations. For every common translation,
\[
 pE(k_c UV)=k(c)-{s n\over\sqrt p}(q_{-c}-r_{-c}).
\]
In particular
\[
 -s pE(k UV)=\sqrt{n/p}\,(\gamma-\gamma^{-1})+s/\sqrt p.        \tag{7}
\]
Thus the all-prime ordinary theta conjecture is equivalent to $pE(kUV)\to0$ for this one bounded, fixed test at the specified translation. Any pair of actual optima gives the same marked value. There is a stronger averaged error for this test. Complementarity on the exterior gives the exact formula
\[
 E_c\big|pE(k_cUV)-k(c)\big|={2(1-b)\over\sqrt p}.
\]
This is already an $O(p^{-3/2})$ first-norm error for the unscaled mixed coefficient after subtraction of $k(c)/p$. It holds also for the known exceptional square-order family.

One can keep the repeated-center terms in (7) at their true price. Define $C(i,j)=E_z k(z)k(z-i)k(z-j)$, $\Delta_q=q(k^2)-Ek^2$ and $\Delta_r=r(k^2)-Ek^2$. Expanding $UV$ and evaluating the two axes by the sector equations yields
\[
 pE(kUV)=-p\sum_{i,j\ne0}q_i r_j C(i,j)
      +s\sqrt p(a\Delta_r-b\Delta_q)+pab\,E k^3 .                 \tag{8}
\]
Every summand of the exterior sum with nonzero weight has three distinct centers $0,i,j$. The last term is $O(p^{-1/2})$ by the one-angle third moment and $pab=O(1)$. The exactly uniform displacement budget gives exterior pair weight $1/n-a r_t-b q_{-t}+ab1_{t=0}$ for $j-i=t$. This keeps the arithmetic signs of the distinct-center cubic terms and both one-law square prices, all at the actual maximal mark. [Odd Jacobi moment](entropy-heads-81.md) · [Zero column sum of positional signs](parallel-witness-6.md)

There is a conditional obstruction at the optimal face for the one-field test. Since $s\,q(k)=(na-1)/\sqrt p$ and $Ek^2=(n-1)/p$, Jensen gives
\[
 s\,q(L_1)=2(p/n)\Delta_q
 \ \ge\ 2\big(\gamma^2-1-2a+2/n\big).
\]
Consequently the *signed linear test* $L_1$ has one-power error of magnitude $\gg_\delta p^{-1/2}$ on every true primary optimum along any fixed-gap sequence. Its counting mean is zero and its Haar mean against a single weighted Jacobi field vanishes by [first-moment exclusion](astra-dissipation-80.md#the-conditional-covariance-of-transported-fields-is-constant). Furthermore $EL_1^2=2+o(1)$ by the physical Gram estimate there. Squaring the preceding lower bound once it is positive gives
\[
 q(L_1^2)-EL_1^2\ \ge\ 4(\gamma^2-1)^2-2-o(1).
\]
If $\liminf\gamma>\sqrt{1+1/\sqrt2}$, the exact square from round 83 therefore has positive physical one-power bias $\gg p^{-1/2}$ on the maximal face itself. The corresponding Haar one-power moment vanishes by the joint covariance exclusion. Replacing the physical square by its bounded raw trace approximant changes its pairing with $U$ by $O(p^{-3/4})$, using the $O(p^{-1/2})$ normalized second error and $\|U\|_{2,n}=O(p^{-1/4})$. The threshold enters only this square argument. [Joint covariance](translated-covariance-82.md)

## Certified prime tests and ranked follow-ups

The [384-bit replay](astra-complement-84-check.py) reconstructs genuine opposite endpoint pairs at $p=101,257,409,769$, checks (1) on every relative displacement for $L_1^2$, checks every common translation and the exact spectral sum in (3), and checks the exact trimmed constant correction. It verifies (7), the common-translation first norm and the distinct-center sum in (8) by summing at each counting coordinate before applying the two endpoint laws. For the finite zero-allowance terminal deficits at times $4,5,6,7$, the four actual rooted values $p E(hUV)$ lie respectively in $(-0.020666,-0.020665),(-0.046053,-0.046052),(-0.030143,-0.030142),(-0.017825,-0.017824)$. The prime $769$ first square has centered RMS between 2.4083 and 2.4084, scaled mixed RMS between 2.1935 and 2.1936, and RMS residual from (3) between 0.2772 and 0.2773. These four time choices illustrate the algebra independent of the asymptotic good-time conditions. [Interval records](astra-complement-84-checks.jsonl)

1. At the marked root compare the true distinct-center sum in (8) with the two measured one-law square prices at additive error $o(1)$ after scaling. By (7) this is necessary and sufficient for the original conjecture, with no moving time or nonlinear terminal test.
2. On one true good terminal window, prove $pE(hUV)\ge-o(1)$ at the prescribed root of (6), retaining the signed positional coefficients where the primary multiplier is supported. Changing the opposite optimizer alone cannot improve this value. Formula (5) gives a benchmark for fixed trace squares before terminal projection and truncation.
