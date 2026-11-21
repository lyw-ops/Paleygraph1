# Signed blocks of the marked curvature and moving caps at fixed correction sums

At a genuine clipped stationary pair, the curvature of the physical mark is bounded above and below by two responses obtained by varying just one sign of the corrected products. The same bounds hold after changing the cap endpoints so each sign's counting correction stays fixed, with a constant direction removed from each block. A genuine balanced pair at prime 173 has strictly nonzero curvature with the cap held fixed. At the same pair the moving cap admits a local holomorphic mark.

## Two signed one-block bounds at the actual row

Use the normalized products and canonical action \(\mathcal P\) of [round 94](cap-curvature-94.md). At the base pair write \(s=n/t\), keep its current rotation frozen, and let \(g_i=\frac12(\log A_i-\log B_i)\). The real bulk prices are \(q_i=1+e_i\). The subscripts \(+,-\) on vectors and matrices refer to the two strictly corrected sets \(\mathcal A_+,\mathcal A_-\), and \(H=\Im(\partial_q g)\), \(c=\partial_s g\) denote the actual complex product response restricted to the active sites. Here \(\partial_s g\) has only the active bulk entries. The complex product branch and its symmetric Jacobian are those of round 94. Take \(C=\operatorname{diag}(+1,-1)\) on the two sign sets, \(Q=\operatorname{diag}(q_i)\), and \(a=\tan\theta\), \(\kappa=(1-a^2)/a>0\).

For any real vector \(h\) of product variations supported on the active set, the true local product branch has phase variation \(F=Hh\) there. Use the [anisotropic factor pairing](rotated-cap-93.md#the-angular-work-inequality) at the base point. The inactive sites are nonexpansive for the fixed-product differential. The marked differential also has its product fixed because only \(h\) varies. Summing the active identity with the two possible signs gives
\[
   -h^{\mathsf T} C Hh\ge \kappa (Hh)^{\mathsf T}Q(Hh),\qquad
   -\tfrac12(CH+HC)=\begin{pmatrix}-H_{++}&0\\0&H_{--}\end{pmatrix}.
                                                                    \tag{1}
\]
This uses only the base active phases; the holomorphic perturbation in products need not be a clipped solution away from the base point. When \(h\) belongs to the kernel of one diagonal block and is supported on that sign, (1) gives \(Hh=0\). Conversely, if \(Hh=0\), then \(h^{\mathsf T}(-H_{++}\oplus H_{--})h=0\), so each sign component belongs to its diagonal kernel. For brevity put \(A=-H_{++}\), \(D=H_{--}\) and \(B=H_{+-}\). The null directions split as \(\ker H=\ker A\oplus\ker D\). The complexified range contains \(c\) on any smooth clipped patch by the phase equations in round 94.

On the diagonal ranges use the positive inverses of \(A,D\) and put
\[
  x=A^{-1/2}c_+,\qquad y=D^{-1/2}c_-,\qquad T=A^{-1/2}BD^{-1/2}.
\]
The relevant congruence for \(H\) has matrix \(\bigl(\begin{smallmatrix}-I&T\\T^*&I\end{smallmatrix}\bigr)\). Its inverse is found by squaring, since its square is \(\operatorname{diag}(I+TT^*,I+T^*T)\). The curvature \(-c^*H^\dagger c\) therefore has the two exact forms
\[
 \begin{split}
  \Delta_s\mathcal P
    &=\|(I+TT^*)^{-1/2}(x-Ty)\|^2-\|y\|^2\\
    &=\|x\|^2-\|(I+T^*T)^{-1/2}(y+T^*x)\|^2 .
 \end{split}                                                       \tag{2}
\]
In particular
\[
              -c_-^*D^\dagger c_-\ \\le\ \\Delta_s\mathcal P
                      \ \\le\ c_+^*A^\dagger c_+ .                   \tag{3}
\]
The bounds use independent quadratic responses of the original row and hold for arbitrary cross coupling \(B\). On the upper side it suffices to control the one-sign system obtained by freezing the other sign's prices. The lower side uses the reverse choice. These charges use the same base row, including its actual opposite-sector amplitudes.

The squared-loss formula also places the charge at the marked coordinate of a definite energy on each sign. With \(\dot U=\dot A'-\dot B'\), \(\dot S=\dot A'+\dot B'\) and \(d_i=|\dot U_i|_a^2-|\dot S_i|_a^2\), it gives the exact identity
\[
 -h^{\mathsf T}CHh=\kappa\sum_{i\in\mathcal A}q_i|(Hh)_i|^2
   +\frac{1}{4a}\left(\sum_{i\notin\mathcal A}d_i
                     +\|\dot S\|_a^2-\|\dot U\|_a^2\right).
\]
All quantities in parentheses are nonnegative, including \(d_0\). Let \(L_0<1\) be the norm of multiplication by \(\tanh(g_0-ib)\) in the same scalar anisotropic metric. Since \(\dot U_0=(A'_0+B'_0)c^{\mathsf T}h\), the marked term after division by \(4a\) is at least \(\gamma|s||c^{\mathsf T}h|^2\) for \(\gamma=a(1-L_0^2)\cos^2\theta\). In particular, with \(D_+=A,D_-=D\), the real and imaginary parts of the marked sensitivity on each sign give two rank-one terms bounded together by \(D_\sigma/(\gamma|s|)\). Taking their traces after conjugating by \((D_\sigma^\dagger)^{1/2}\) gives \(c_\sigma^*D_\sigma^\dagger c_\sigma\le2/(\gamma|s|)\). On the centered reciprocal cone \(\gamma\) has a positive bound on compact sets by the [uniform marked log and strict relative angle](cap-curvature-94.md#a-common-locally-lipschitz-extension-and-a-criterion-for-the-theta-limit). A vanishing charge would require the mark to contribute a vanishing share of this energy uniformly over active variations in its sign.

## Fixing the signed correction sums by moving both boundaries

Work on an open smooth selection of the admissible chart with both active sign sets locally fixed and nonempty, as in [round 94](cap-curvature-94.md#a-canonical-differential-in-the-cap-and-marked-product). Let \(V\) have columns the two active sign indicators, and let \(\lambda=(U_*,L_*)\) be the cap angles. In this paragraph all vectors are in full counting coordinates. On differentiating at fixed \(s\) the active phase constraints give \(H,dq=V,d\lambda\). Thus both columns of \(V\) lie in the range of \(H\), and the Jacobian of the two canonical signed correction sums with respect to \(\lambda\) is the symmetric matrix
\[
                 G=V^{\mathsf T}H^\dagger V .
\]
Taking \(h=H^\dagger V e_+\) and \(h=H^\dagger V e_-\) in (1) yields \(G_{++}\le-\kappa\sum_+q_i<0\) and \(G_{--}\ge\kappa\sum_-q_i>0\), respectively. Therefore \(G\) is invertible, regardless of any cross derivative. The implicit function theorem selects nearby \(\lambda(s)\) at prescribed signed sums \(\varepsilon=(E_+,E_-)\) equal to their base values. Along this section the real action \(\mathcal P^{\varepsilon}=\mathcal P(s,\lambda(s))+\varepsilon^{\mathsf T}\lambda(s)\) satisfies \(d\mathcal P^{\varepsilon}=\Im(g_0\,ds)\). Its curvature again measures the weak Cauchy–Riemann defect of the selected mark.

Let \(W=\ker V^{\mathsf T}\) and let \(P_W\) be its Euclidean projection. Product derivatives of this section lie in \(W\), because the two sums are fixed, while the phase derivatives on the active sites lie in \(\operatorname{im}V\). At the base let \(H_W=P_WH|_W\), \(c_W=P_Wc\). Project the two active phase equations for variations of \(\Re s,\Im s\) to obtain
\[
              \Delta_s\mathcal P^{\varepsilon}=-c_W^*H_W^\dagger c_W. \tag{4}
\]
Equivalently, writing \(d=V^{\mathsf T}H^\dagger c\), this is
\[
   \Delta_s\mathcal P^{\varepsilon}=\Delta_s\mathcal P+d^*G^{-1}d.    \tag{5}
\]
In fact \(z=H^\dagger c-H^\dagger VG^{-1}d\) belongs to \(W\) and satisfies \(H_Wz=c_W\). Any difference from the generalized inverse solution is orthogonal to the tested vector \(c_W\). Formula (5) isolates the part of the fixed-cap curvature affected by moving the two boundaries.

The sign matrix preserves \(W\). On this subspace the left side of (1) is unchanged after compressing \(H\) to \(H_W\). The right side controls \(\kappa\|H_W h\|^2\) since \(Q\succeq I\). The block argument for (3) applies also to (4). Let \(\mathbf 1_\sigma\) be the constant vector on sign \(\sigma\). Its one-block charge in the fixed-sums bound is
\[
  \inf_{\xi\in\mathbb C}(c_\sigma-\xi\mathbf1_\sigma)^*D_\sigma^\dagger
                      (c_\sigma-\xi\mathbf1_\sigma)
  =c_\sigma^*D_\sigma^\dagger c_\sigma
     -\frac{|\mathbf1_\sigma^{\mathsf T}D_\sigma^\dagger c_\sigma|^2}
            {\mathbf1_\sigma^{\mathsf T}D_\sigma^\dagger\mathbf1_\sigma}.      \tag{6}
\]
Both \(c_\sigma\) and \(\mathbf1_\sigma\) lie in the diagonal range by the kernel split and the range facts above. To see (6) from the compressed inverse, solve \(D_\sigma z=c_\sigma-\xi\mathbf1_\sigma\) in that range and choose \(\xi\) so \(\mathbf1_\sigma^{\mathsf T}z=0\). The resulting energy is the minimum shown. Thus the moving cap tests signwise variation of the marked sensitivity in the inverse-energy norm. The correction sums themselves supply no bound in that norm. On inversion-even solutions these statements use the same full counting inner product restricted to even vectors; the constant vectors and projections carry the orbit multiplicities.

## One actual balanced row and the limit still needed

At the [prime-173 balanced pair](astra-center-94.md#actual-balance-and-a-two-sector-real-test), \(t=1/50+17i/1000\), \(a=1/\sqrt2\), the upper orbit is the singleton 43 and the lower orbit is \(\{29,57\}\). The signed total corrections both equal \(0.4150123601606\ldots\) exactly in the balanced root. The Arb256 replay certifies the active block in orthonormal orbit coordinates, solves the reciprocal complex product derivatives, and independently differentiates the fixed-center clipped root with respect to \(\Re s,\Im s\). The charges in (3) lie near \(1.5425762\cdot10^{-6}\) and \(7.8207790\cdot10^{-7}\), respectively. The curvature in \(s\) lies in \((7.11921,7.11923)\cdot10^{-7}\), so equal signed total corrections fail to force a holomorphic mark with a fixed cap.

For the section with moving endpoints and both sums fixed the even space \(W\) of active product changes is zero, because there is one orbit per sign. Equivalently, fixing the two actual orbit products leaves a holomorphic exact-product section, and its two current extreme angles define the moving caps. Strict active, inactive and marked margins from the interval solve keep these caps admissible as a local positive-angle chart. Here admissibility only means that this genuine root meets the cap conditions in a neighborhood; it does not invoke the small-ratio Brouwer region. This realizes the same genuinely positive balanced pair on a locally holomorphic marked section with varying endpoints. [Arb checker](cap-blocks-95-check.py) · [Interval record](cap-blocks-95-checks.jsonl)

## Vanishing-mass positive product repairs on a common domain

There is a direct way to compare fixed positive repairs to the true marks. At a real reciprocal floor \(z>0\), take the positive real stationary pair for products \(w_0=nz\), \(w_i=1\) off the mark. Compare to the pair at the same mark with fixed positive bulk weights \(w'_i=q_i\). Denote their real marks by \(g_0,g'_0\). The [two-pair real Hellinger identity](astra-velocity-92.md#simultaneous-changes-to-the-real-weights) and its nonnegative marked summand give
\[
   4nz\sinh^2((g'_0-g_0)/2)
      \le \sum_{i\ne0}(\sqrt{q_i}-1)^2 .                              \tag{7}
\]
Indeed the marked crossed factors are \(\sqrt{nz}\exp(\pm(g'_0-g_0)/2)\). Thus the difference of the marks is at most \(\sqrt{n^{-1}\sum(\sqrt{q_i}-1)^2/z}\). For upward repairs this is at most \(\sqrt{n^{-1}\sum(q_i-1)/z}\). The bound uses positivity and the mean/subspace identities; it needs no coordinatewise margin on the repairs.

The bounded marked phase in [round 36](parallel-cold-complex-36.md#1-the-exceptional-coordinate-forces-a-complex-sector) also holds for these arbitrary fixed positive bulk weights. In the modified complex exact-product problem write \(Q_0=\sum_{i\ne0}q_i\), \(L=|s+Q_0|\) and \(r=\bar A_0/A_0\). The complementary Hermitian pairing, with equal means, is
\[
           \sum_i\bar A_i B_i=L,qquad |L-sr|\le Q_0 .               \tag{8}
\]
Consequently \(\Re(sr)/|s|\ge\cos(\arg s-\arg(s+Q_0))\). In the positive marked log lift this gives \(|\Im g'_0|\le\frac12|\arg s-\arg(s+Q_0)|<\pi/4\) on \(\Re s>0\), throughout a connected continuation where the lift agrees with the positive real marks. For marked-only continuation, the polynomial product and complementary equations for the positive pair still have an invertible row Jacobian at the real point. Thus the same irreducible-curve projection argument as in round 36 yields full factor lifts away from finitely many points of the projected marked curve. The continued mark satisfies the projected polynomial by the identity theorem. Continuity then passes (8)'s angular bound across exceptional fibers.

Suppose that through all eligible primes one can choose one fixed positive profile per prime such that \(n^{-1}\sum(\sqrt{q_i}-1)^2\to0\). Suppose their modified physical marked logs extend holomorphically on one connected common subdomain of \(\Re z>0\), agreeing with the repaired positive real marks on a hot open real interval and at a sequence of cold reciprocal floors increasing to infinity. Equation (8) gives the same uniform phase bound as before. The functions \(\exp(i g'_0)\) are then uniformly bounded and bounded away from zero, and (7) gives \(g'_0\to0\) on the hot interval from the inherited true-mark limit. Normal families and the identity theorem force \(\exp(i g'_0)\to1\) locally uniformly on the domain. To fix the real-log multiples of \(2\pi\), take a compact chain of overlapping disks from one hot point to any nominated cold point. On that chain the values of \(\exp(i g'_0)\) lie in a fixed small disk about 1 for all sufficiently large primes, and the continuous log lift is fixed at the hot end. Thus \(g'_0\to0\) at every nominated real floor. A second application of (7) and the [theta bracket](smoothing.md#fixed-point-and-a-sufficient-residual-estimate) gives ETH26. This criterion permits strictly positive product corrections at finite primes and asks their total repair cost to vanish in the specified normalized metric. No such repaired common domain has been constructed.

1. Try to bound the scaled one-sign charges \(n c_+^*A^\dagger c_+\) and \(n c_-^*D^\dagger c_-\) on the actual centered cold patch. The sandwich (3) requires no estimate of the coupling between sign sets. Each charge is a response to product perturbations on that same sign of the true row.
2. Test signwise centered charge (6) on actual two-sign survivors, or choose one fixed positive product profile approximating their active corrections for an entire complex patch. For the second approach (7) reduces the real comparison to the normalized square-root cost, even if individual repairs are large. Both approaches still need a connected common domain.
