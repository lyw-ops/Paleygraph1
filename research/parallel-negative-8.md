# What controls the negative part of the projected average?

This continues [the opposite-spectrum test (8)](parallel-extension-7.md#opposite-sector-tests-with-the-same-weights) for [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). The positive time average forces a **joint** endpoint and time-average level set. The unweighted mean of the scaled negative part is $O_\tau(T^{-2/3})$, improving the bound for the part paired against bounded scaled opposite heights. At square orders the true pairing stays positive even as the negative part tends to zero in unscaled $\ell_2$. At prime orders an explicit Fejér construction shows why small $\ell_2$ error, projection, and full opposite feasibility alone do not suffice, even for even trials with the same limiting ports as the actual iterate.

## Locating the terms that can contribute

Use $w_0=1$, $w_i=\tau/n$ off the mark, $W=\sum_i w_i$, and the averaged iteration $z_0=0$, $u_t=\sqrt{z_t^2+4w}$, $z_{t+1}=(z_t+Ku_t)/2$. Write $j=\mathbf1/\sqrt n$, $J=jj^{\mathsf T}$, $P_\epsilon=(I+\epsilon K-J)/2$, $U_\epsilon=\mathbb Rj\oplus\operatorname{ran}P_\epsilon$, and $\epsilon=-\sigma$. Set

$$
\bar A_{\sigma,T}=(\bar u_T+\sigma\bar z_T)/2,\qquad
H=H_{\sigma,T}=(I+\sigma K)\bar u_T/2
  =\bar A_{\sigma,T}+\sigma z_T/T.
$$

Let $g_i=\sqrt n(H_i)_-$ on the bulk and $g_0=0$. The mean and mark of $H$ are $c_T=\langle j,H\rangle$ and $b=H_0$. The [averaged norm bounds](iteration-parity.md#a-criterion-involving-only-the-iterates) give $0<c_T\le\sqrt W$ and $\|z_T\|_2^2\le2WT$. For a probability $\mu\ge0$ in $U_\epsilon$, the (8) pairing with $B=\sqrt{nW}\mu$ is $\sqrt W\sum_i\mu_i g_i$. Take $\mu=A_\epsilon/\sqrt{nW}$ for the true pairing, or maximize over this cone for the solve-free upper bound. Inversion averaging allows $\mu$ to be even since $g$ is even.

On the bulk define $x_i=(-\sigma\sqrt n\,z_{T,i}/T)_+$ and $y_i=\sqrt n\,\bar A_{\epsilon,T,i}$, with both set to zero at the mark. At each time $A_{\sigma,t,i}A_{\epsilon,t,i}=\tau/n$, so Cauchy–Schwarz in time gives $n\bar A_{\sigma,T,i}\bar A_{\epsilon,T,i}\ge\tau$. In particular

$$
0\le g_i\le (x_i-\tau/y_i)_+,\qquad
\{g>u\}\subseteq S_u:=\{i\ne0:x_i>u+\tau/y_i\}\quad(u\ge0).
\tag{1}
$$

Here $S_0=\{i\ne0:x_i y_i>\tau\}$; the division by $y_i$ is only on the bulk. Thus a large endpoint alone need not make the trial negative. For any opposite probability,

$$
\sum_i\mu_i g_i\le\int_0^\infty\mu(S_u)\,du .
\tag{2}
$$

This allows testing the Fourier mass of the joint sets instead of the top entries of the entire endpoint. The exact layer sets $\{g>u\}$ give equality in (2). More locally, for $y_i\le L$ use $g_i\le Lx_i^2/(4\tau)$, from $(x-a)_+\le x^2/(4a)$; for $y_i>L$ use $g_i\le x_i\mathbf1_{S_0}(i)$.

Write $\overline f=n^{-1}\sum_i f_i$. Since $\overline{x^2}\le2W/T$ and $\bar y\le\sqrt W$, Hölder bounds the density of $S_0$ by $\tau^{-2/3}(\overline{x^2})^{1/3}\bar y^{2/3}$. Cauchy–Schwarz with $g\le x\mathbf1_{S_0}$ now gives

$$
\bar g\le
\min\left\{\sqrt{2W/T},\;
      2^{2/3} W^{5/6}\tau^{-1/3}T^{-2/3}\right\}.
\tag{3}
$$

For any test spectrum $B=\sqrt{nW}\mu$, the portion of the pairing on $\sqrt n B_i\le M$ is at most $M\bar g$. At each fixed floor the cap can grow as $o(T^{2/3})$. The tail test still needs control of opposite mass on the joint level sets of (1), with the size of the cost accounted for as in (2).

The elementary [translated Jacobi witness](iterate-majorants.md#repair-with-translated-witnesses) gives $\mu_i\le1/h_\sigma$ for all $i$, with $h_\sigma=1+(n-1-\sigma)/(\sqrt q+1)$ at field order $q$, by pairing against a sign-$\sigma$ witness centered at $i$. Thus one can insert $\min(1,|S_u|/h_\sigma)$ in (2). For an alternative bound using full feasibility before applying the cap, $\sum_i\mu_i g_i=\bar g+\sum_i\mu_i(P_\epsilon g)_i$. Maximizing the last sum over just the point cap is the average of the top $h_\sigma$ entries of $P_\epsilon g$, with fractional weighting at the cutoff. This projects the **clipped** cost. In fact $P_\epsilon H=0$, but $P_\epsilon g$ need not vanish. Cauchy–Schwarz with the point cap gives

$$
\sqrt W\max_{\mu}\sum_i\mu_i g_i \le
W\sqrt{\frac{2n}{h_\sigma T}}.
\tag{4}
$$

For example, $T/\sqrt q\to\infty$ suffices for this bound to vanish, but does not establish that the trial mark remains $1+o(1)$ at those depths. In the field-first order, (3) and (4) control neither the full pairing nor the point-cap average on exceptional sets of size comparable to $h_\sigma$.

## Actual square obstruction at fixed and moving floors

At $q=r^2$, let $I=(\mathbb F_r^\times)^\perp$ of size $m=(r+1)/2$, including the mark. The [subfield certificate](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) gives the feasible plus probability $\mathbf1_I/m$ and $\theta_+=r-1=n/m$. For the minus trial, Fourier orthogonality gives $\sum_{i\in I}H_{-,T,i}=mc_T/\sqrt n$, so the sum of bulk negative entries on $I$ is at least $b-mc_T/\sqrt n$. This yields the worst-feasible lower bound

$$
\sqrt W\max_{\mu\in U_+,\ \mu\ge0,\ \sum\mu_i=1}\sum_i\mu_i g_i
\ \ge\ \sqrt W\big((r-1)b/\sqrt n-c_T\big).
\tag{5}
$$

For the actual stationary $A_+$, the complementary theta values and $A_{+,0}A_{-,0}=1$ give $A_{+,0}\ge(r-1)/\sqrt{nW}$. If $b\ge0$, testing the signed trial against $A_+$ and dropping the positive bulk terms similarly yields

$$
\sum_{i\ne0}A_{+,i}(H_{-,T,i})_-
\ \ge\ \frac{(r-1)b}{\sqrt{nW}}-c_T\sqrt W .
\tag{6}
$$

Using the [fixed-depth marked cancellation draft](uniform-fixed-depth.md#applying-the-algebra-to-smoothing) on the square family as in [the square control](square-order-control.md#square-order-comparison), $b\to1$ at each fixed $(\tau,T)$. Then the lower bounds in (5) and (6) tend in liminf to at least $\sqrt{2(1+\tau)}-(1+\tau)$ and $\sqrt{2/(1+\tau)}-(1+\tau)$, respectively. These are positive for $0<\tau<1$ and $0<\tau<2^{1/3}-1$, respectively, uniformly in the choice of fixed depth in this order of limits. There is also a single diagonal sequence with $T\to\infty,\ \tau\to0,\ b\to1$: choose the fixed pairs $(T,\tau)=(j,1/j)$, then take the square order sufficiently large for $|b-1|<1/j$. On this sequence $\|(H_{-,T})_-\|_2\le\sqrt{2W/T}\to0$, yet the true bulk pairing has liminf at least $\sqrt2-1$, as does the worst-feasible pairing. Equation (6) needs only the exact square theta values and actual port $b$; all use of fixed-depth cancellation is in specifying $b\to1$.

## Prime counterexample to a norm-only use of full feasibility

The following construction uses prime Paley kernels. It shows that a bounded, vanishing-$\ell_2$ signed perturbation in the trial sector can produce order-one bulk negative cost against a **genuinely opposite-feasible** spectrum. It does not assert that such a perturbation is created by the smoothing recurrence.

Fix $L\ge2$, put $d=4$, and take arbitrarily large primes $p\equiv1\pmod{8\prod_{j=1}^{L-1}(4^j-1)}$, with $\operatorname{ord}_p(d)>2L-2$. Dirichlet's theorem, quadratic reciprocity and inversion symmetry give $s(d^j)=+1$ for $0<|j|<L$, as in the [Fejér compression example](square-order-control.md#a-sector-estimate-that-fails-even-at-prime-order). There is a square $a\in Q$ with $s(ad^j)=-1$ for $|j|<L$ and $a^2\notin\{d^j:|j|\le2L-2\}$. Indeed the signs $\chi(a)=1$, $\chi(1-ad^j)=-1$ have distinct linear roots, so expansion of their indicator and [Weil's character sum bound](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/) give $p/2^{2L}+O_L(\sqrt p)$ candidates. Excluding the roots and the $O(L)$ solutions for $a^2$ leaves a candidate for large $p$.

On frequency $k$, set

$$
F_L(k)=\frac1L\left|\sum_{j=0}^{L-1}k(d)^j\right|^2,\qquad
C(k)=\operatorname{Re}k(a),\qquad
R(k)=\frac{F_L(k)C(k)}{L\sqrt n}.
$$

The inverse Fourier support of $F_L$ consists of the powers $d^j$, $|j|<L$. Thus $\mu=F_L/n$ is a plus probability. The support of $F_L C$ lies in the two sets $a^{\pm1}d^j$, $|j|<L$, all of sign minus, so $R\in\operatorname{ran}P_-$ and $\sum_i\mu_i R_i=0$. Both spectra are even. We have $\|R\|_2\le L^{-1/2}$ from $0\le F_L\le L$ and $\bar F_L=1$, and $\sqrt n\|R\|_\infty\le1$. Character orthogonality gives $\overline{F_L^2}=(2L^2+1)/(3L)$ and $\overline{F_L^2 C^2}=\overline{F_L^2}/2$; the cosine at $a^2$ in $C^2$ is removed by the exclusion on $a^2$. Since $|C|\ge C^2$,

$$
\sum_i\mu_i|\sqrt n R_i|\ge\frac{\overline{F_L^2}}{2L}\ge\frac13 .
\tag{7}
$$

The negative part alone has weighted mean at least $1/6$ because the signed mean is zero. It has no negative value at the mark. The unweighted mean of its absolute value is at most $1/L$. This example satisfies the full support constraint on the other side, and $L/n$ can be chosen much smaller than the Jacobi point cap.

**Keeping the port bounds and the reciprocal inequality.** Start with the actual $H=H_{-,T}$. For a fixed $\eta=6$ and either choice of sign, form the nonnegative adjustment

$$
\Delta u^\pm=\frac{2\eta}{L\sqrt n}F_L(1\pm C),\qquad
\widehat H^\pm=\frac{I-K}{2}(\bar u_T+\Delta u^\pm)
              =H+\frac{\eta}{L\sqrt n}\mathbf1\ \pm 2\eta R .
$$

The mean port changes by $\eta/L$ and the mark by $O(1/\sqrt n)$. Keep $\bar z_T$ unchanged and modify the endpoint to $z_T+TK\Delta u^\pm/2$. Then $K(\bar u_T+\Delta u^\pm)-\bar z_T$ is still twice the endpoint divided by $T$, and both positive unprojected sign averages increase by $\Delta u^\pm/2$. Their coordinatewise product stays at least $w$, as for the actual averages by Cauchy–Schwarz in time. This is a perturbation of the data in the averaged identity.

There is enough slack to keep $c_T+\eta/L\le\sqrt W$ and the modified endpoint norm at most $\sqrt{2WT}$. Indeed, with $m_t=\langle j,u_t\rangle/2$, the averaged norm identity gives $\|z_T\|_2^2\le2WT-2\sum_{t<T}m_t^2$. In particular the squared norm has slack at least $2Tc_T^2$ by Jensen. Also
$$
(\sqrt W-m_0)^2\le \sum_{t<T}(\sqrt W-m_t)^2
\le 2T\sqrt W\,(\sqrt W-c_T).
$$
Here $m_0=n^{-1/2}+(1-1/n)\sqrt\tau$ is the value at time zero. At $\tau=1/T$ and large $n,T$, the mean slack is $\gg T^{-1}$. The slack in the endpoint norm itself is $\gg\sqrt T\,c_T^2\gg T^{-1/2}$, using $c_T\ge(1-1/n)\sqrt\tau$. Taking $L=T^4$ makes the endpoint perturbation $O(T/\sqrt L)=O(T^{-1})$ and the mean perturbation $O(T^{-4})$. Thus the perturbation retains the hypotheses used in (1)–(4).

Write $v=\sqrt n H+\eta/L$ and $r'=2\eta\sqrt n R$. Pointwise $(v+r')_-+(v-r')_-\ge |r'|-v$. If $b\ge0$, the bulk $\mu$-mean of $v$ is at most $c_T+\eta/L$, by opposite orthogonality and the nonnegative marked entry. Removing the mark in (7) costs $L/n$. Thus for one of $\widehat H^\pm$ the pairing against $\sqrt{nW}\mu$ is at least

$$
\frac{\sqrt W}{2}
\left[2\eta(1/3-L/n)-c_T-\eta/L\right].
\tag{8}
$$

Choose $(T,\tau,L)=(j,1/j,j^4)$ and then $p$ sufficiently large for the sign pattern, $L/n=o(1)$ and $b\to1$ (using the fixed-depth draft at each pair). The modified trial has the same limiting port data, and its bulk negative $\ell_2$ norm is at most $\sqrt{2W/T}$, by positivity of the unprojected average and the modified endpoint bound. Yet (8) gives a positive liminf. This rules out a uniform LP estimate based just on the projected and positive-average forms, the reciprocal inequality for the averages, the port bounds, and the endpoint norm bound. For the true prime iterates the recurrence might rule out this alignment, or the stationary reciprocal relation could improve on the worst-feasible pairing. Neither inference follows from the example.

As arithmetic checks, $(p,L,a)=(109,2,12),(181,3,108),(709,4,95),(2269,5,382),(5881,6,714)$ satisfy the finite sign and order conditions by modular exponentiation with $d=4$. FFT evaluation verifies $KF_L=F_L-\mathbf1$, $KR=-R$, the zero signed pairing and the cosine-square mean used in (7) to within $2\cdot10^{-10}$; the bulk negative $\mu$-means of $\sqrt n R$ range from $0.2135$ to $0.2389$. These checks use the explicit constructed opposite witnesses; they are not LP or stationary comparisons.
