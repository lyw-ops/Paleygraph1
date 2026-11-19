# Complementary smoothing on the Paley Fourier LP

This adapts the deterministic portion of [Chen, Hu, Hu, Wang and Yang, Section 4](https://arxiv.org/html/2610.22971v1#S4) to the two Paley masks. Their random theorem assumes odd cyclic orders and independent distance bits. Here $n=(p-1)/2$ is even, the distance bits are arithmetic, and the degree-one Fourier law is arcsine rather than Gaussian. The identities from their Section 4 use only the three Fourier projections, which exist in even order as well. Their later Gaussian comparison and random sampling results would need arithmetic replacements.

The [local inertia argument](iteration-parity.md) is the current fixed-depth proof draft. The calculations below give the deterministic certificate and the original low-depth arithmetic estimates.

## Fixed point and a sufficient residual estimate

Use the notation in [the Fourier notes](fourier.md). On real even vectors indexed by the Fourier frequencies let $K=F\operatorname{diag}(s)F^{-1}$, where $F$ is the unnormalized Fourier matrix. Then $K^2=I-J$ with $J$ the orthogonal projection onto the constant vectors. We have $K_{j,k}=\lambda_{j-k}/n$, including $K_{0,0}=-1/n$.

For $\tau>0$, put $w_0=1$, $w_k=\tau/n$ at $k\ne0$, and $W=\sum_k w_k$. Let $\Phi(v)_k=\sqrt{v_k^2+4w_k}$. Proposition 4.2 gives the unique zero-mean solution $v^*=K\Phi(v^*)$. The two positive vectors $(\Phi(v^*)\pm v^*)/2$ are supported in the complementary inverse-Fourier subspaces. Their entrywise product is $w$, each has sum $\sqrt{nW}$, and the plus sign corresponds to $\theta_+=\vartheta(\overline H)$. In particular

$$\left|\log(\theta_+/\sqrt n)-\operatorname{arsinh}(v_0^*/2)\right|\le \tfrac12\log W.$$

We also have elementary norm bounds. Writing $u^*=\Phi(v^*)$, we have $\|v^*\|_1\le\sum_k u_k^*=2\sqrt{nW}$. The entry bound $|K_{jk}|\le \sqrt p/n$ gives $\|v^*\|_\infty\le2\sqrt{pW/n}$. In particular $\|v^*\|_2\le 2\sqrt W\,p^{1/4}$.

For an even mean-zero candidate $v$ write $r=v-K\Phi(v)$. The residual estimate in Proposition 4.3 now gives

$$
\left|\log(\theta_+/\sqrt n)-\operatorname{arsinh}(v_0/2)\right|
\le \tfrac12\log W+\sqrt{(\|v\|_2+\sqrt W\,p^{1/4})\,\|r\|_2}.
$$

For each fixed $\tau>0$, a bounded-$\ell_2$ construction with $v_0=o(1)$ and $\|r\|_2=o(p^{-1/4})$ would be sufficient. After taking $p\to\infty$ one can send $\tau\downarrow0$. The bound uses the entry estimate for $K$. An alternative suffices if $\|v\|_2=O(1)$, $v_0=o(1)$, and $|r_0|+\sqrt n\max_{k\ne0}|r_k|=o(1)$. Indeed, in the exact discrepancy identity (4.13), bound the pairing with $v^*$ using the two norms above, while (4.18) bounds the first term by $\|v\|_2\|r\|_2$.

## First two iteration markers

For the Picard iteration $v^{(0)}=0$, $v^{(t+1)}=K\Phi(v^{(t)})$, the first step is

$$v^{(1)}_k=2(1-\sqrt{\tau/n})\lambda_k/n,$$

since $K$ kills constant vectors. This gives $v^{(1)}_0=O_\tau(p^{-1})$. Put $x_k=\lambda_k/\sqrt n$ and $a=1-\sqrt{\tau/n}$. The second step has marked entry

$$v^{(2)}_0=-\frac{\sqrt{4+(v^{(1)}_0)^2}}{n}+\frac{2}{n}\sum_{k\ne0}x_k\sqrt{a^2 x_k^2+\tau}.$$

**Claim.** For fixed $\tau>0$, $v^{(2)}_0=O_\tau(p^{-1/2})$.

To see this, write $x_k=b\operatorname{Re}(G(\psi)/G(\psi\chi))$ with $b=\sqrt{p/n}$ and nontrivial $k$. The two extensions $\psi,\psi\chi$ give the same real part. On $z=\exp(it)$, the test function $h(t)=b\cos(t)\sqrt{a^2 b^2\cos^2(t)+\tau}$ has average zero by the sign change at $t+\pi$. At fixed $\tau$, its derivatives through third order are bounded uniformly for large $p$, so its Fourier coefficients are $O_\tau((1+|m|)^{-3})$ by integration by parts. [Katz, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf), applied to the two distinct shifts $1,\chi$ with exponents $m,-m$, bounds their nonzero empirical Fourier moments by $|m|/\sqrt p+4/(p-1)$. Summing against the Fourier coefficients bounds the average of $h$ by $O_\tau(p^{-1/2})$. The diagonal term contributes $O_\tau(p^{-1})$.

This calculation only controls the marked coordinate after two steps. With $z_k=\sqrt n\,v^{(1)}_k$, the next step additionally needs the joint behavior of $x_k$ and the mixed fields

$$B_{p,k}=\frac1n\sum_{j\ne0}\lambda_{k-j}\sqrt{z_j^2+4\tau}.$$

At the next checkpoint, test for each fixed $\tau>0$ whether the sum

$$\frac1n\sum_{k\ne0}x_k\sqrt{(x_k\sqrt{4+(v^{(1)}_0)^2}+B_{p,k})^2+4\tau}$$

tends to zero. The [joint Mellin proof draft](mellin.md) handles this step. The whole conjecture still requires uniform control of the residual or of the exact fixed point.

### A mixed polynomial correlation

Let $x^2$ mean coordinatewise squaring. A first signed mixed moment that arises on expanding even functions in the feedback is

$$M_p=\frac1n\langle x^2,Kx^2\rangle=O(p^{-1/2}).$$

In fact $F^{-1}x^2=(s*s)/n$, with multiplicative convolution on $Q$, and Parseval gives

$$M_p=\frac{1}{4n^2}\sum_{a\in Q\setminus\{1\}}\chi(1-a)(t(a)-2)^2,\qquad t(a)=\sum_{y\in\mathbb F_p}\chi(y(y-1)(y-a)).$$

For the identity, write $(s*s)(a)=\sum_{y\in Q}\chi((1-y)(y-a))$ and expand the square mask as $(1+\chi(y))/2$ on $y\ne0$. The unweighted quadratic sum over $y\ne0$ is $-2$ since $a\ne1$ and $a\in Q$. The weighted term is $t(a)$ since $-1$ is a square. At $a=1$ the multiplier $s(a)$ vanishes.

For the bound, extend the sum to $U=\mathbb A^1\setminus\{0,1\}$ by expanding $1_Q$. The two quadratic twist weights are $\chi(1-a)$ and $\chi(a(1-a))$. The leading term $t(a)^2$ is the trace of $\operatorname{Sym}^2(\mathrm{Leg})$ plus $p$, where $\mathrm{Leg}=R^1\pi_*\overline{\mathbb Q}_\ell$ for the smooth Legendre family. The symmetric square is geometrically irreducible by the $SL_2$ monodromy of $\mathrm{Leg}$, and it remains irreducible after either rank-one twist. These sheaves are tame at $0,1,\infty$ and pure of weight 2. On $U$, $H_c^0$ and $H_c^2$ vanish, and the tame Euler characteristic formula gives $\dim H_c^1=3$. The trace formula and Deligne's weight bound give $O(p^{3/2})$ for each twisted symmetric-square sum. The constant term $p$ times each quadratic-weight sum is $O(p)$ by the linear and quadratic character sum identities. The terms linear in $t$ are $O(p^{3/2})$ in total even using only Hasse's bound. The required monodromy and tameness are in [Katz, Convolution and Equidistribution, Chapter 15](https://web.math.princeton.edu/~nmk/mellin331.pdf). The same Legendre family is used in [Jig #7's completion obstruction](https://jig.so/p/7).

This is one term in the mixed feedback calculation. The remaining terms include higher-order joint correlations with $B_{p,k}$.

### Compression to functions of the first Fourier field

For any fixed polynomials $P,Q$ and $x_k=\lambda_k/\sqrt n$, one has

$$\frac1n\langle P(x),KQ(x)\rangle=O_{P,Q}(p^{-1/2}).$$

Here is a derivation through Chebyshev polynomials $T_m$ (after the bounded rescaling from $\sqrt n$ to $\sqrt p$). The degree-zero term is killed by $K$. For $m\ge1$, put $g_m=F^{-1}T_m(\lambda/\sqrt p)$. On the full group $\mathbb F_p^\times$, put $s_0(a)=\chi(1-a)$. Away from the trivial mode on $Q$, $T_m(\lambda_k/\sqrt p)$ is the average of $J(\psi,\chi)^m/p^{m/2}$ and $J(\psi\chi,\chi)^m/p^{m/2}$ over the two lifts of the corresponding character. Fourier inversion therefore gives $g_m=p^{-m/2}s_0^{*m}|_Q+O_m(1/p)$ uniformly, with the error arising from the single trivial mode.

Let $\mathcal H_m$ be the hypergeometric sheaf of type $(m,m)$ with upstairs characters all trivial and downstairs characters all $\chi$. Write $H_m$ for its trace function. From the hypergeometric exponential sum formula, its transform at $\psi$ is $-G(\psi)^m\overline{G(\psi\chi)}^{\,m}$. For $\psi\notin\{1,\chi\}$ this equals $-p^{m/2}J(\psi,\chi)^m$. At the two exceptional characters, both the $p^{-m}$ multiple of the hypergeometric transform and the corresponding normalized Jacobi powers have absolute value $p^{-m/2}$. Fourier inversion shows that $g_m(a)=-p^{-m}H_m(a)+O_m(1/p)$ for $a\in Q\setminus\{1\}$. The sign convention is the Frobenius trace convention in [Katz, G₂ and hypergeometric sheaves, Section 2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf).

By Parseval, $n^{-1}\langle T_m(\lambda/\sqrt p),K T_l(\lambda/\sqrt p)\rangle=\sum_{a\in Q}s(a)g_m(a)g_l(a)$. Insert the hypergeometric trace expressions. Off $1$ each normalized trace is $O_m(p^{-1/2})$ by purity, so the aggregate replacement error is $O_{m,l}(p^{-1/2})$. Expand $1_Q$ on $U=\mathbb A^1\setminus\{0,1\}$ as before. Each resulting sum is a trace sum of $\mathcal H_m(m)\otimes\mathcal H_l(l)$ twisted by one of the quadratic sheaves for $\chi(1-a)$ and $\chi(a(1-a))$. It has weight $-2$ and bounded tame rank. There are no geometric coinvariants. For different ranks this follows from irreducibility of the disjoint-parameter hypergeometric sheaves. For equal ranks the inertia eigenvalue multiset at $1$ is $\{1^{m-1},(-1)^m\}$ by the pseudoreflection formula. The quadratic twists exchange the multiplicities of $+1$ and $-1$, whereas duality preserves them. For even $m$ the multiplicities are $(m,0)$, and for odd $m$ they are $(m-1,1)$. They differ in all cases, which excludes the isomorphism to a twisted dual. Thus $H_c^2=0$, $H_c^0=0$, and the tame Euler characteristic bounds $\dim H_c^1$ by $ml$. Deligne's bound on $H_c^1$ gives $O_{m,l}(p^{-1/2})$ as claimed.

Uniform approximation on the bounded range of $x$ and $\|K\|_{2\to2}\le1$ give the corresponding $o(1)$ for any two fixed continuous functions. In the displayed third-update sum put $h(z)=\sqrt{z^2+4\tau}$ and expand $h(c x_k+B_{p,k})$ in $B_{p,k}$ at zero, where $c=\sqrt{4+(v^{(1)}_0)^2}\to 2$. The zeroth-order term tends to zero by the arcsine law. The first-order term is included in the result for continuous functions of $x$, applied to $x\,h'(2x)$ and $h(2x)$. Removing the single trivial-mode entry from $K h(2x)$ incurs $o(1)$ in the normalized pairing. The higher terms are treated by the joint symmetry argument.

## Numerical probe

`smoothing.py` iterates the fixed point using FFTs and records the first three marked entries, the final marked entry, and its $\ell_2$ residual. At $\tau=0.01$ the final markers for $p=10009,50021,100049,200009$ were about $-0.01421$, $0.0000388$, $0.004938$ and $0.0001105$, with residuals below $10^{-8}$. These markers and residuals are floating-point observations.

The `--certify` mode obtains finite-prime bounds directly from the two candidate Fourier rows. It applies the inverse FFT, masks and rounds to form exactly symmetric integer rows with the required zero pattern, bounds each Fourier coefficient from below with FLINT/Arb, and repairs the diagonal by an integer increment before rescaling. The final rational bounds use the exact complementary identity. Their validity is independent of the accuracy of the preliminary NumPy iterate. At $p=1000033$ the rounded-out normalized interval is $[1.000325,1.001326]$. [FLINT/Arb interval DFT](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.dft)
