# A Jacobi head charged by the whole marked optimal face

At a genuine terminal time, minimizing a squared density excess on the fixed deficit mask gives one adaptive Jacobi field. Either the minimizing optimizer pays the low-density terminal price, or **every** optimizer on the larger marked face puts mass on the same head, including competitors that never entered the minimization as charged rows. In the second case this mass survives subtraction of an exponentially amplified true cold energy density. A positive opposite-potential formula below computes the least escaping mass, and also handles a simultaneous head and terminal price on one optimizer.

## Choosing the charged rows on the actual face

Use the [round-79 finite terminal window](terminal-height-79.md), a fixed gap \(0<\delta\le1\), \(D=D(p)\), \(J=\lfloor D/8\rfloor\), and any good terminal time \(b\) with its prescribed start and length \(d\asymp D\). Write \(a\) for the optimal root probability, \(\mathcal Q_a\) for the entire larger primary face, and assume \(\sqrt n a\ge1+\delta\). Use the legitimate cutoff \(B=0\) and exterior \(E=G\setminus\{0\}\), so **every** optimizer has the same exterior mass \(M=1-a=1-O(n^{-1/2})\). The terminal deficit \(r\) and companion \(Z\) are fixed before choosing a row. Set \(P=\{i\in E:r_i>\delta/8\}\). Let \(H\) be the base-two tower of height \(\lfloor(\log_2^*p)/2\rfloor\) from one, \(\alpha=H^{-1/4}\), and \(t=\alpha M/\sqrt n\).

Minimize
\[
             n\sum_{i\in P}(q_i-t)_+^2
                   \qquad(q\in\mathcal Q_a).
\]
Choose an even minimizer \(q^*\), possible by convexity and reflection. The vector \(y_i=1_P(i)(q_i^*-t)_+\) in fact agrees for all minimizers. Otherwise the componentwise hinge inequality at their midpoint and strict convexity of the squared norm of their two nonnegative hinge vectors give a strict improvement.

Let \(I=I(q^*)\) be the **actual** joint density, deficit and companion band of round 79. There are constants depending only on \(\delta\) with the following alternative at this same time.

* On \(I\cap\{q_i^*\le2t\}\) the row \(q^*\) pays deficit \(\gg_\delta1\) and companion height \(\gg_\delta d\) after every deletion of at most \(H^2/(4\alpha^2 M^2)\) sites.
* Writing \(s=\sum y_i>0\), \(v=y/s\), \(m=1/\sum v_i^2\), define the *single* head
\[
 W(j)=\sigma\sum_i v_i k(j-i),\qquad
 \rho=\sqrt n\langle v,q^*\rangle/M,\qquad
 T=\{j\in E:W(j)>\rho/8\}.
\]
Here \(\sigma\) is the sign of the primary face. One has \(\rho>\alpha\), \(\rho^2m\gg_\delta H^{3/2}\), and simultaneously for all \(q'\in\mathcal Q_a\),
\[
  q'(T)\ge
  \frac{(\sqrt{n/p}-1/8)\rho M-p^{-1/2}-aW(0)}{1-\rho/8}
                  \gg \rho M.                                             \tag{1}
\]

Indeed, choose the first case if the low part initially pays at least half a fixed uniform lower bound from round 79 after its original deletions. On up to the enlarged number of low sites one has \(\sqrt n\|q^*1_F\|_2\le H\) and \(\|q^*1_F\|_1\le H^2/(2\alpha M\sqrt n)\). The bounded Mellin approximation of the actual three-term deficit envelope from [round 80](astra-surviving-80.md#polynomial-deletion-on-the-actual-weighted-terminal-height) makes the deleted price \(o(1)\). Otherwise the high part of \(I\) pays a uniform fixed deficit after every original deletion of \(H^2/M^2\) sites, and therefore contains more than that many sites. There \(y_i>t\), \(y_i>q_i^*/2\), so
\[
          L_y=n\sum_i y_i^2\gg_\delta \max(D,\alpha^2 H^2).
\]
The first bound uses the normalized second norm of the true deficit. Also \(\rho=\alpha+\sqrt n\sum y_i^2/(s M)\), giving \(\rho^2m\ge L_y/M^2\). The point cap at the optimum gives \(\rho=O(1)\); more sharply the identity below at \(q^*\), together with \(W\le1\), gives \(\rho M\le(\sqrt p+1)/\sqrt n\). Hence \(1-\rho/8\) is bounded away from zero.

The one-sided derivative at \(q^*\) toward **each** \(q'\in\mathcal Q_a\) gives \(\langle v,q'\rangle\ge\langle v,q^*\rangle\). The exact signed sector equation then gives
\[
 \langle q',W\rangle=(n\langle v,q'\rangle-1)/\sqrt p
          \ge \rho M\sqrt{n/p}-1/\sqrt p.
\]
The root contribution equals \(aW(0)\) for every row. On the exterior use \(W\le\rho/8+(1-\rho/8)1_T\), proving (1). Each site carrying positive mass for a genuine primary row is exposed by opposite complementarity. The full set \(T\) may also contain forced zeros.

## A bound on actual truncated terminal height and escaping mass

On the exterior define the true profile
\[
             e_i=1+\sum_{j=1}^{J}|Y_j(i)|^2 .
\]
In the common-head case there exists \(c_\delta>0\) such that
\[
                  n^{-1}\sum_{i\in T} e_i
                         \le \exp(-c_\delta H^{3/2})                      \tag{2}
\]
eventually. To see the claimed rate, use the [round-82 covariance estimate](translated-covariance-82.md#an-arbitrarily-weighted-finite-prime-test) with the same genuine mark coefficients but per-step accuracy \(\epsilon=\exp(-H^2)\) in the shortened-horizon approximation. Its reciprocal has iterated logarithm at most \(\log_2^*H+O(1)\). The initial approximation resource has the same height up to an additive constant and each step through \(J+2\) costs one tower level. The approximants therefore still have dimension and charge at most \(\log_2\log_2 p\), by the tower margin in [round 77](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon). The summed squared-modulus comparison costs \(O(D^{5/2}(\epsilon+p^{-3/8}))\). The main terms are bounded by \(C D^2\exp[-c\min(\rho^2m,\rho\log p)]\), and the arithmetic errors by \(D\,p^{-3/8}\operatorname{polylog}(p)\). The same unweighted test treats the counting measure and bounded marked seed. Here \(\rho\log p\ge H^{-1/4}\log p\gg H^{3/2}\), \(H\le\log_2\log_2p\) eventually, and \(D=O(\log_2^*p)\). Absorb the polynomial factors by decreasing \(c_\delta\). The sharper exponent uses the number of surviving high rows, and the true trajectory error was reduced before multiplying by the cap below.

Put \(A=\exp(c_\delta H^{3/2}/2)\). Two conclusions are simultaneous for every genuine \(q'\):
\[
 \sum_{i\in T} (q'_i-Ae_i/n)_+
       \ge q'(T)-A n^{-1}\sum_T e_i
       \gg \rho M,                                                       \tag{3}
\]
and, for every good terminal time \(b'\) in the same shortened prefix,
\[
 \sum_{i\in T}\min(q'_i,A\sqrt{e_i}/n)\,
       |Z_{\sigma,b'}(i)|
                  \ll \exp(-c_\delta H^{3/2}/2).                         \tag{4}
\]
Indeed the exact [bulk expansion](relative-window-77.md#paired-rows-with-a-nonnegative-bulk-constant) at a single good time involves only the three adjacent \(Y\)'s, bounded coefficients and the scalar \((g_{b'}-g_{b'-1})/2\) of modulus at most two. Thus \(|Z_{\sigma,b'}|\ll\sqrt e\) pointwise on the exterior. Formula (4) is an upper for the truncated **optimizer-weighted** companion price on the frozen heads; (3) locates the mandatory part beyond even the larger energy cap. The first terminal alternative retains its price outside any permitted deletion, and (4) alone gives no upper there.

## Exact positive completion with a coordinate capacity and a price

For any nonnegative exterior capacities \(c_i\) and demand weights \(g_i\ge0\), put
\[
 \Delta_g(c)=\min_{q\in\mathcal Q_a}\sum_E g_i(q_i-c_i)_+,\qquad
 b(V)=\overline V-aV_0.
\]
Write \(V_{-\sigma}\) for the real span of the constants and the opposite Fourier sector. Let \(\kappa\ge\max_E g_i\). Then
\[
 \boxed{\Delta_g(c)=\kappa M-
 \min_{\substack{V\in V_{-\sigma},\ V\ge0\\V_i\ge \kappa-g_i\ (i\in E)}}
        \left[b(V)+\sum_{i\in E} c_i(\kappa-V_i)_+\right].}                    \tag{5}
\]
Both extrema are attained. The demand may include a frozen head and a terminal field from the same time. The special choice \(g\equiv \kappa=1\) says exactly how much positive exterior mass can be matched beneath the profile across the face. For strictly positive \(w_i\), the least scale permitting \(q_i\le A_* w_i\) on the exterior is thus the least \(A\ge0\) such that for every nonnegative opposite \(V\),
\[
          b(V)+A\sum_E w_i(1-V_i)_+\ge M.                                \tag{6}
\]

For the proof, represent the positive-part cost as the maximum of \(\sum f_i(q_i-c_i)\) over \(0\le f_i\le g_i\). Interchange the compact convex face and box by finite minimax. For fixed \(f\), the exact primary constraints say that the minimum of \(\sum f_iq_i\) is the maximum of \(b(U)\) over real opposite \(U_i\le f_i\) on the exterior, by finite linear programming duality. Maximize jointly and take \(f_i=(U_i)_+\) for \(U_i\le g_i\). This gives \(\max_U b(U)-\sum c_i(U_i)_+\). Substitute \(V=\kappa-U\). Adding a sufficient nonnegative multiple of an opposite optimum raises the root to zero if necessary, preserves the root residual, weakens the uncovered-capacity payment and preserves all exterior lower bounds. This gives a globally positive-completable potential as in [round 81](astra-cover-81.md#exact-price-and-an-optimal-genuine-law). Attainment follows from the original finite LP and its dual. Nonzero potentials normalize to genuine opposite probabilities.

In particular \(\Delta_1(Ae/n)=o(H^{-1/4})\) along a putative fixed-gap sequence rules out the common-head case by (3). A *single comparison row*, which can differ from the hinge minimizer, suffices here. In the other direction (3) gives a certificate that the minimum in (5) falls below \(M-c\rho M\) for these capacities and \(g=1\), with an attained positive opposite potential.

For a joint upper, fix nonnegative \(h_i\), for example \(h_i=Z_{\sigma,b}(i)1_P(i)\) on the true negative mask (zero elsewhere). On \(P\) the companion is positive. Take \(g=1_T+h/d\). The *same* attaining primary row in (5) obeys
\[
       q(T)\le c(T)+\Delta_g(c),\qquad
       \langle q,h\rangle/d\le \langle c,h\rangle/d+\Delta_g(c).          \tag{7}
\]
One can keep \(c_i=Ae_i/n\) off \(P\) and replace it on \(P\) by the smaller of this cap and \(d/[n(1+h_i)]\). Then (2) bounds \(c(T)\) and \(\langle c,h\rangle/d\le |P|/n=O_\delta(1/d)\) by the true deficit first norm. The missing inequality in (7) is now a lower on the single minimum over genuine opposite potentials in (5), with the displayed capacities and the remaining terminal price explicitly included. In particular (2) by itself gives no bound on \(\Delta_g(c)\).

## A finite whole-face check

At prime 97, time four, the [384-bit checker](astra-split-83-check.py) reconstructs the [two-parameter even optimal face](astra-face-54.md) from the complementary cyclotomic solutions and uses the finite pin with zero allowance and deficit cutoff \(0.01\). For \(\alpha=1/5\) the origin of those two anchored coordinates minimizes the squared hinge. The two first derivatives in the free nonnegative parameters are strictly positive. The common head has twenty exterior sites and (1) certifies mass above 0.042487719 on **every** row. The selected minimizing row itself has head mass between 0.551341889 and 0.551341890.

With \(w_i=(1+\sum_{j=1}^4|Y_j(i)|^2)/48\), the minimum scale in (6) over the whole face is in \((0.219620428,0.219620429)\). At the attaining row the constraints at 3 and 22 and their reflections saturate, and site 19 and its reflection vanish. A positive combination of the two upper inequalities and the nonnegativity constraint gives the matching lower for the scale; the even optimum is valid on the entire face because the caps are even. This matching row has masked terminal price between 1.613096834 and 1.613096835. The squared-hinge minimizer has price between 1.454308662 and 1.454308663. The computation retains both prices at the same time. The finite cutoff does not meet the asymptotic scale conditions. [Outward interval record](astra-split-83-checks.jsonl)

For the joint demand (7), freeze those same twenty heads and use $h=Z1_P$, $d=4$. Take the capacity $w_i/5$ off $P$ and its minimum with $4/[48(1+h_i)]$ on $P$. An explicit opposite cosine interpolant, repaired with the free opposite optimum, gives a strictly positive potential with $\kappa=4$, root residual in $(2.668717333,2.668717334)$ and uncovered-capacity charge in $(0.245035332,0.245035333)$. The original squared-hinge minimizing row attains the matching joint residual in $(0.507225779,0.507225780)$. Thus the unconstrained energy domination threshold by itself misses a substantial joint charge at this finite time. [Primal and opposite-law check](astra-split-83-check.py)

## Ranked next tests

1. Bound the least mismatch \(\Delta_1(Ae/n)\) at the indicated growing scale by testing the positive root-residual inequality (6), or its additive-error version (5), on the actual larger face. A bound \(o(H^{-1/4})\) lets any energy-compatible comparison row force the low terminal alternative for the squared-hinge minimizer.
2. On the surviving low sites price the same good companion and the same attaining row. Use the joint demand in (7) with the explicit height-sensitive caps; estimate the minimum in (5) including its uncovered-capacity term. The clipped contribution on the high head has the proven upper (4); its escaping part and the low-site price require the additional comparison.
