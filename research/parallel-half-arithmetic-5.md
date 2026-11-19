# The reciprocal pair and the half-angle slow directions

For Problem 26, the actual stationary pair gives two restrictions on small half-angle high sets. The two directions obtained by splitting the exact inverse column have a mixed Jacobi form of size $O(\sqrt{\tau}+p^{-1/2})$ before normalization, while their dissipation forms are of order one. This limits exchange **between these two directions**. As the floor tends to zero, a high set of nearly minimum size on one sign also forces the opposite set to have at least twice that size and the signed half-angle mark to tend to $1/3$ on the first sign. The near-minimum support has signed Jacobi endpoint differences. A high set of size $O(\sqrt p)$ carrying positive stationary mass gives a slow Rayleigh quotient but need not give a vanishing Jacobi deficit.

## Notation and identities for the actual pair

Write $p\equiv1\pmod4$, $n=(p-1)/2$, $G=\widehat Q$ for the frequency group of the nonzero squares, $m_0=n/\sqrt p$, and $k(h)=\lambda_h/\sqrt p$. Thus $K_{ij}=k(j-i)/m_0$, $|k|\le1$, $K_{00}=-1/n$, and $K^2=P=I-J$. Except in the prime-only phase test, the arguments below also apply with $p$ replaced by a square field order $q$.

The weights are $w_0=1$ and $w_i=\tau/n$ elsewhere, with $0<\tau\le1$, $W=\sum_i w_i$, $\nu=\sqrt{\tau/n}$, and $c=\sqrt{W/n}$. For the exact even stationary spectra $A_\sigma=(u+\sigma v)/2$, set $\mu_\sigma=A_\sigma/\sqrt{nW}$ and $a_\sigma=A_{\sigma,0}$. The equations give

$$
 A_{+,i}A_{-,i}=w_i,\qquad K A_\sigma=\sigma(A_\sigma-c\mathbf1),\qquad
 \sum_i A_\sigma(i) A_{-\sigma}(i+h)=W \quad(h\in G).                 \tag{1}
$$

The last equality follows from disjoint nonconstant positional Fourier supports. We use the [translation budget](translation.md#an-exact-deficit-for-each-translate) consequence that $A_\sigma(i)\le a_\sigma$ for both signs: for $h\ne0$, the two terms meeting the mark in the plus/minus correlation are $t+\nu^2/t$, $t=A_{+,h}/a_+$. By evenness and reciprocity the other terms pair into reciprocal ratios times $\nu^2$, and contribute at least $(n-2)\nu^2$. Thus $t+\nu^2/t\le1+\nu^2$, so $\nu^2\le t\le1$. Also $a_+a_-=1$, and the feasible entry cap gives $a_\sigma\le c+\sqrt{nW}/m_0$.

## Signed coupling of the exact half-angle column

Use the stripped half-angle $B$ from [the exact inverse column](stationary-secant.md#the-exact-inverse-column), with $B_0=0$ and $B_i=\tanh(\gamma_i/2)$ elsewhere. Put $V=|B|^{1/2}$, $z=KPe_0$, $a=u_0-2\nu$, and split $N=VKV$ into blocks on $I_\sigma=\{i:\sigma B_i>0\}$. Zero coordinates can be dropped. As in the [signed time integral](parallel-sign-4.md#common-time-and-the-signed-response), write

$$
 L_\sigma=I-\sigma N_{\sigma\sigma},\quad C=N_{+-},\quad
 \mathcal A=\begin{pmatrix} L_+&-C\\ C^{\mathsf T}&L_-\end{pmatrix},
 \quad b=((Vz)_+,-(Vz)_-).
$$

Here subscripts on vectors mean restriction to the sign blocks. Extend vectors on a block by zero whenever applying $K$.

Define $x_\sigma=\mathbf1_{I_\sigma}V|v|$, $g_\sigma=Vx_\sigma$, and $r_\sigma=A_\sigma-g_\sigma$. The half-angle identity $B_i v_i=u_i-2\nu$ off the mark gives $g_\sigma=\mathbf1_{I_\sigma}(u-2\nu)$. On $I_\sigma$, $r_\sigma=2\nu-A_{-\sigma}$; elsewhere off the mark $r_\sigma=A_\sigma\le\nu$. Thus $0\le r_{\sigma,i}\le2\nu$ on the bulk, and $r_{\sigma,0}=a_\sigma$. In particular $0\le g_\sigma\le A_\sigma$.

The mixed form $\mathcal C=\langle x_+,Cx_-\rangle=\langle g_+,Kg_-\rangle$ satisfies the exact identity

$$
 \mathcal C=\langle r_+,Kr_-\rangle+
 \langle A_+,g_-\rangle-\langle g_+,A_-\rangle
 + c\big(\|g_+\|_1-\|g_-\|_1\big).                                  \tag{2}
$$

To see it, expand the first pairing and use (1) and $\langle A_+,K A_-\rangle=0$. Each middle product is at most $(n-1)\nu^2$ by reciprocity. The bulk of each $r_\sigma$ has norm at most $2\sqrt\tau$, the mark-mark pairing costs $O(1/n)$, and $\|g_\sigma\|_1=\sqrt{nW}-\|r_\sigma\|_1$. Hence $|\mathcal C|\ll\sqrt\tau+p^{-1/2}$.

Let $\mathcal E_\sigma=\langle x_\sigma,L_\sigma x_\sigma\rangle$. Since $\|x_\sigma\|_2^2-\|g_\sigma\|_2^2\le 2\nu\sum_i |v_i|\ll\sqrt\tau$, one has

$$
\begin{aligned}
 \mathcal E_\sigma
 &=\|x_\sigma\|_2^2-\|g_\sigma\|_2^2
    +W-2c\|r_\sigma\|_1+\langle r_\sigma,(I-\sigma K)r_\sigma\rangle\\
 &=W+a_\sigma^2+O(\sqrt\tau+p^{-1/2}).                              \tag{3}
\end{aligned}
$$

For the norm difference use $(1-|B_i|)|v_i|\le2\nu$ on the bulk. The first line uses $(I-\sigma K)A_\sigma=c\mathbf1$; for the second use the bulk bound on $r_\sigma$, with $K_{00}=-1/n$. These estimates require no bound on the size of either block.

The exact inverse is $\mathcal A^{-1}b=(x_+,x_-)/a$, where the pair denotes block concatenation. Testing its two rows against $x_+$ and $x_-$ gives

$$
 m_B-K_{00}=\frac{\mathcal E_+-\mathcal E_--2\mathcal C}{a^2}.         \tag{4}
$$

Indeed $m_B-K_{00}=\langle Vz,(x_+,x_-)\rangle/a$, and the two row tests read $\mathcal E_+-\mathcal C=a\langle(Vz)_+,x_+\rangle$ and $\mathcal E_-+\mathcal C=-a\langle(Vz)_-,x_-\rangle$. The sign in (4) comes from the opposite signs of the off-diagonal blocks of $\mathcal A$.

Fix $0\le\rho<1$, and define $S_\sigma=\{i\ne0:\sigma B_i>\rho\}$, $m_\sigma=|S_\sigma|$, and $M_\sigma=\mu_\sigma(S_\sigma)$. Put $R_\rho=(1+\rho)/(1-\rho)$. Off $S_\sigma$ in the bulk one has $A_\sigma\le R_\rho\nu$, since $A_{\sigma,i}/\nu=e^{\sigma\gamma_i}$. Therefore

$$
 M_\sigma\ge1-R_\rho\sqrt{\tau/W}-a_\sigma/\sqrt{nW},\qquad
 \big\|x_\sigma-\mathbf1_{S_\sigma} A_\sigma\big\|_2\ll_\rho\sqrt\tau. \tag{5}
$$

For the norm, use $g_\sigma\le x_\sigma\le A_\sigma$ on $I_\sigma$. If $m_\sigma=O(m_0)$ and $M_\sigma$ stays bounded below, (5), Cauchy–Schwarz and the point cap give $\|x_\sigma\|_2^2\asymp m_0$. For sufficiently small floors the unit direction $\widehat x_\sigma=x_\sigma/\|x_\sigma\|_2$ then has $L_\sigma$ Rayleigh quotient $\ell_\sigma\asymp p^{-1/2}$ by (3). Here $S_\sigma$ is a fixed-threshold set; the size estimate for the much deeper window in the [half-angle note](stationary-secant.md#uniform-transfer-along-the-hyperbolic-path) alone does not imply this mass hypothesis. If the fixed-threshold hypotheses hold on both signs,

$$
 \frac{|\langle\widehat x_+,C\widehat x_-\rangle|}
      {\sqrt{\ell_+\ell_-}}
   =\frac{|\mathcal C|}{\sqrt{\mathcal E_+\mathcal E_-}}
   \ll\sqrt\tau+p^{-1/2}.                                         \tag{6}
$$

Thus in the joint limit $\tau\to0$ the projected exchange is smaller than the dissipation on this two-dimensional compression. Equations (2)–(6) do not bound $C$ as an operator between all slow directions, or its action on the finite-time source. In particular they do not establish the signed tail criterion of the time integral. They rule out explaining its cancellation by a large direct exchange between the two stationary inverse directions alone.

## Which Jacobi endpoint information survives at each size?

For mixed edges, let $U_\pm$ be arbitrary bulk sets on which the respective actual spectra are at least $d_\pm>0$. Every $h$ occurs as $j-i$, $i\in U_+$, $j\in U_-$, at most $W/(d_+d_-)$ times by (1). In particular, with $L_t=\{h:1-k(h)^2\le t\}$, the part of the mixed block on $U_+\times U_-$ with differences in $L_t$ has squared Frobenius norm at most

$$
 \frac{W|L_t|}{d_+d_-m_0^2}
 \ll \frac{W}{d_+d_-}\big(\sqrt t+p^{-1/4}\big).                    \tag{7}
$$

Here we used the [one-cap Jacobi estimate](critical-sets.md#repeated-differences-are-necessary). For the deep half-angle sets $\{i\ne0:\sigma B_i\ge1-\delta\}$ take $d_\sigma=\nu(2/\delta-1)$. At fixed floor and $\delta\asymp p^{-1/2}$ the factor $W/(d_+d_-)$ is bounded. The estimate also holds uniformly as the floor decreases if the bulk amplitude cutoffs $d_\pm$ are fixed. At $t\asymp p^{-1/2}$ this is only an $O(p^{-1/8})$ bound on the norm at fixed cutoffs. It does not control coupling at the $p^{-1/2}$ dissipation scale. In contrast, (2) bounds the **signed sum over all differences** for the stationary directions: if $R_g(h)=\sum_i g_+(i)g_-(i+h)$, then $0\le R_g(h)\le W$ and $\mathcal C=m_0^{-1}\sum_h k(h)R_g(h)$. The small signed sum does not follow by counting the cap edges.

For within-sign edges on $S=S_\sigma$, use $f=\mathbf1_S A_\sigma$ and $\pi=f/\|f\|_1$. If $m=|S|=O(m_0)$ and $M_\sigma$ is bounded below, the exterior $A_\sigma-f$ has bounded squared norm by (5) and the mark cap. Expanding $I-\sigma K$ as in (3) gives

$$
 \langle f,(I-\sigma K)f\rangle=O_\rho(1),\qquad
 \mathbb E_{i,j\sim\pi}\sigma k(j-i)
  =m_0\|\pi\|_2^2-O_\rho(p^{-1/2})
  \ge \frac{m_0}{m}-O_\rho(p^{-1/2}).                              \tag{8}
$$

The expectation is for independent samples; the error constants can also depend on the lower bound on $M_\sigma$. A constant size factor $m/m_0>1$ gives a lower bound separated from zero, but that bound is separated from the endpoint.

At near-minimum size put $\varepsilon=(m/m_0-1)_++p^{-1/2}$. Both the weighted deficit $1-\mathbb E_{\pi\otimes\pi}\sigma k$ and the variance $m\|\pi\|_2^2-1$ are $O_\rho(\varepsilon)$, using (8) and the upper bound $\sigma k\le1$. At most $O_\rho(\varepsilon m)$ indices have $\pi_i<1/(2m)$, by the variance. On pairs of the other indices the uniform probability weight is at most four times $\pi_i\pi_j$. Since each signed deficit is between zero and two,

$$
 \frac1{m^2}\sum_{i,j\in S}\big(1-\sigma k(j-i)\big)
    \ll_\rho \varepsilon.                                         \tag{9}
$$

This gives the endpoint with its sign on the actual support. Since $1-k^2\le2(1-\sigma k)$, the [paired-anchor result](parallel-five-4.md) applies when $m\le m_0+o(p^{17/120})$ with $M_\sigma$ bounded below. It gives a nonzero overlap of order at least $p^{3/7}$, also after any bounded list of exclusions. The overlap conclusion does not follow merely from $m=O(m_0)$ or from a qualitative $o(1)$ deficit.

At near-minimum size there is also just one slow eigenvector of $L_\sigma$ on its sign block. Indeed, (8) in quadratic-form notation gives $\lambda_{\max}(\sigma K_{SS})\ge1-O(p^{-1/2})$, whereas $\|K_{SS}\|_{\rm F}\le m/m_0$. All the other eigenvalues of $\sigma K_{SS}$ therefore have absolute size $O(\sqrt\varepsilon)$. If a two-dimensional subspace has $L_\sigma$ Rayleigh quotients at most $\delta$, choose a unit vector $y$ in it with $(Vy)_S$ orthogonal to the first compression eigenvector. The inequality $L_\sigma\succeq I-V^2$ gives $\|y_{S^c}\|^2\le\delta/(1-\rho)$. Consequently the compression and $\|K\|\le1$ give

$$
 1-\delta\le \sigma\langle Vy,KVy\rangle
 \le O(\sqrt\varepsilon)+2\sqrt{\delta/(1-\rho)}+\delta/(1-\rho).
$$

This is impossible at a sufficiently small fixed $\delta=\delta(\rho)$ once $\varepsilon=o(1)$. By min–max the second eigenvalue is bounded below by $\delta$, while the first is at most $\ell_\sigma$. Hence $\widehat x_\sigma$ is within $O(p^{-1/4})$ of the first eigenvector up to sign. This is a result for the one-sign block; it does not give a gap or a coupling estimate for the opposite block.

## Near-minimum on one sign forces a signed imbalance

From the maximum-at-mark property in (1),

$$
 a_\sigma\ge\frac{\sqrt{nW}\,M_\sigma}{m_\sigma},\qquad
 m_+m_-\ge nW M_+M_-.                                              \tag{10}
$$

The first inequality is for a nonempty high set. At fixed $\rho$ along $\tau\to0$ and $p\to\infty$, the second bound has right side $(2-o(1))m_0^2$. Along such a sequence with $m_\sigma\le(1+o(1))m_0$, (5) and the entry cap force $m_\sigma\sim m_0$, $a_\sigma\to\sqrt2$, and $a_{-\sigma}\to1/\sqrt2$. It follows that

$$
 \sigma m_B\longrightarrow\frac13,\qquad
 m_{-\sigma}\ge(2-o(1))m_0,\qquad
 m_0\|\mu_{-\sigma}\|_2^2\le\tfrac12+o(1).                          \tag{11}
$$

Use $m_B=v_0/(u_0-2\nu)$ with $v_0=A_{+,0}-A_{-,0}$ for the first conclusion, and $\|\mu_{-\sigma}\|_2^2\le a_{-\sigma}/\sqrt{nW}$ for the last. Under bounded-time cancellation of the true half-angle orbit at these orders, (11) would put the same nonzero limit in its signed tail at each fixed cutoff. Bounded-time cancellation is a separate hypothesis for the actual diagonal. More generally, if $m_\sigma\le(D+o(1))m_0$ with $D<\sqrt2$, (10) gives $\liminf\sigma m_B\ge(2-D^2)/(2+D^2)$ in the same limit. An unspecified constant in $m_\sigma=O(m_0)$ gives no such sign.

Near-minimum size also anchors the endpoint to the **mark**. Under the hypotheses of (11), the exact stationary equation gives

$$
 \sum_h \mu_\sigma(h)(1-\sigma k(h))
   =1+1/\sqrt p-\frac{m_0 a_\sigma}{\sqrt{nW}}=o(1).
$$

In fact $\mu_\sigma$ is close in $\ell_1$ to $\mathbf1_{S_\sigma}/m_\sigma$: with $L=(1+\sqrt p)/n$, the distance is at most

$$
 \kappa=2(1-M_\sigma)+2(Lm_\sigma-1)_+ .                            \tag{12}
$$

The positive excess over the uniform probability on $S_\sigma$ is at most $(Lm_\sigma-1)_+$ inside and $1-M_\sigma$ outside. Hence the rooted average signed deficit is $o(1)$ on the uniform support as well. This qualitative rooted estimate uses the small floor; the within-support width in (9) does not pay the $\sqrt\tau$ loss in (5).

There is a stronger exact restriction on the very high cores. For $\theta_\pm\in(0,1)$ with $2\theta_+\theta_->W$, let $P_\pm$ be any subsets of $\{i:A_\pm(i)\ge\theta_\pm a_\pm\}$, possibly including the mark. Every difference from $P_+$ to $P_-$ occurs at most once by (1) and $a_+a_-=1$. Equivalently

$$
 (P_+-P_+)\cap(P_--P_-)=\{0\}
$$

when both cores are nonempty. Thus any nonzero near-endpoint difference occurring on the first core is forbidden on the other core. Under the hypotheses of (11), the core in the near-minimum high set contains all but $o(m_0)$ of that set for any fixed $\theta_\sigma<1$, since the average on the high set is asymptotic to $a_\sigma$. With the finer size slack $m_\sigma\le m_0+o(p^{17/120})$, restrict (9) to this core: the deficits are nonnegative and the core retains a $1-o(1)$ fraction of the points. The paired-anchor overlap of size $\gg p^{3/7}$ therefore occurs at a translation forbidden on the opposite core. If also $m_{-\sigma}\le(2+o(1))m_0$, that core retains all but $o(m_0)$ points of its high set too. Choose both thresholds fixed with product greater than $1/2$; their mixed differences then cover $(1-o(1))n$ distinct elements of $G$. This is a necessary packing condition at the lower bound for the opposite sign. Neither unique mixed differences nor the paired-anchor bound proves that the two supports cannot exist.

## A prime-only phase test without a coset cover

Let $S=S_\sigma$ and $F_S(x)=m^{-1}\sum_{i\in S}i(x)$ for $x\in Q$, where $i(x)$ denotes the character. For the actual feasible $\mu_\sigma$, (12) implies that

$$
 x\ne1,\quad |F_S(x)|>\kappa \quad\Longrightarrow\quad s(x)=\sigma .
$$

Thus if positional sets $U,V'\subset Q$ have $|F_S(x/y)|>\kappa$ for every distinct $x\in U,y\in V'$, then at prime order

$$
 |U||V'|\le n+|U\cap V'|.                                          \tag{13}
$$

Indeed $\chi(y-x)=s(x/y)$ for $y\in Q$; scale both sets by a nonsquare for the negative sign. Then apply [Hanson–Petridis, Theorem 1.2](https://arxiv.org/pdf/1905.09134) to the two sets with one negated. This can be tested on arbitrary phase configurations with a margin, without representing $S$ by cosets.

For example, when $\kappa<1$ take the positional unit vectors $\Phi_S(x)=(i(x))_{i\in S}/\sqrt m$. No common complex line can have squared projection $>(1+\kappa)/2$ for more than $(1+\sqrt{1+4n})/2$ of these vectors. For any two in such a cluster, projecting onto the line and using Cauchy–Schwarz for the perpendicular components gives $|\langle\Phi_S(x),\Phi_S(y)\rangle|>\kappa$; take $U=V'$ in (13). In the square-field subfield example a whole positional subgroup of size $\sim\sqrt q$ has identical phases on the annihilator, so this is a prime-only obstruction. The Jacobi overlap estimate does not currently produce a violating phase cluster or rectangle for an arbitrary near-minimum $S$.

## A check on the scale distinction

At square order $q=r^2$, translate the actual subfield annihilator $H$ off the mark, and add $m=|H|=(r+1)/2$ padding indices chosen outside the translate and mark. Call the padded set $S$, of size $2m\sim2m_0$. On the test vector $\mathbf1_{H+h}/\sqrt m$, the Rayleigh quotient of $K_{SS}$ is $(r(m-1)-1)/n=1-O(1/r)$, by the [subfield Jacobi values](parallel-five-4.md#critical-compressions-feasible-spectra-and-square-orders). The prescribed stripped diagonal equal to $1-1/r$ on $S$ and zero off $S$ therefore gives an $O(1/r)$ eigenvalue of its positive $L_+$. Nevertheless some padding gives $d(S)\ge1/4-o(1)$: the average squared normalized Jacobi entry is $(n-1)/q$ by Parseval, and deleting $O(r)$ possible differences changes this average by $o(1)$. Thus the two cross terms between the translated subgroup and random padding already contribute $1/4-o(1)$ in expectation. This is a prescribed-diagonal example with the Paley kernel, not a construction of a stationary pair. It illustrates why a general critical-scale slow direction needs extra information on which part of the support contributes.

For finite checks, the existing FFT stationary solver was run at $173,853,9413,13^2,29^2,97^2$ with $\tau=0.03,0.003,1/n$. The maximum stationary residual was $6.0\cdot10^{-11}$, and the mixed identity, the exact first line of (3), the signed row tests, and the constant cross-correlation agreed within $1.9\cdot10^{-11}$. At $97^2$ and $\rho=1/2$, the plus size was $0.9898m_0$ at all three floors; the minus size exceeded $56m_0$. The ratio $|\mathcal C|/\sqrt{\mathcal E_+\mathcal E_-}$ decreased from $0.1080$ to $0.00832$, while $m_B$ increased from $0.3119$ to $0.3241$. At $\tau=1/n$ a dense check on the positive block gave first and second eigenvalues $0.03133$ and $1.02083$, with $\widehat x_+$ within $2.3\cdot10^{-6}$ of the first eigenvector up to sign. The matched prime $9413$ had both high sets above $41m_0$ and $m_B<0.00044$ at these floors. These finite floating-point checks test the identities and indexing, not any prime asymptotic.

The prime step still missing is to force a phase obstruction such as (13), exclude the near-minimum stationary support by another arithmetic constraint, or estimate the signed time tail through modes other than the two inverse directions above. The constant cross-correlation is compatible with the square-order imbalance and therefore cannot by itself exclude that imbalance at prime order.
