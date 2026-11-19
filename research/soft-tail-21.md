# Smoothing the fixed-mark repair tail

The [fixed-mark repair](anchored-repair-20.md) finishes a Fourier projection by paying the upper tail of the remaining defect. Smoothing that tail gives a convex problem whose exact dual penalizes $ell_2$ concentration at the Jacobi scale. A large penalty suppresses every witness of bounded effective size relative to that scale, while a genuinely broad witness retains its full margin. The limiting identity below separates the broad regime of [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) from the critical-size regime.

## The tail, its quadratic smoothing and the exact dual

Use the notation of [Round 20](anchored-repair-20.md#root-zero-fourier-correction). Let $P=P_{-\sigma}$, $\kappa=P_{00}$, $\ell=Pe_0$, $L=P-\ell\ell^\mathsf T/\kappa$, and $M=\mathbf1-\ell/\kappa$. Let $Y\in U_{-\sigma}$ have mark $a_s>\mu>0$ and ordinary mean $\mu$. For $i\ne0$ put $h_i=W^{(i)}_i$ for the height of the nonnegative marked-zero repair of mean one from Round 20, and $b_i=M_i/h_i$. Here $m_0=n/\sqrt q$, $M_i=1+O(q^{-1/2})$ and $h_i/m_0\to1$ uniformly off the mark and in the sign. The geometry below assumes $M_i>0$ off the mark, as holds for all sufficiently large fields.

Write $g_i=-Y_i/M_i$, let $C=\{v:0\le v_i\le b_i,\ \sum_i v_i\le1\}$ off the mark, and define

$$\Phi_\lambda(Y)=\max_{v\in C}\left[\sum_i v_i g_i-\frac{\lambda}{2}\sum_i\frac{v_i^2}{b_i}\right],\qquad \lambda>0.\tag{1}$$

The hard nonnegative finish price is $\Phi_0(Y)$, obtained by restricting the threshold in Round 20 to $t\ge0$. Since $\sum v_i^2/b_i\le\sum v_i\le1$, the smoothing error obeys $0\le\Phi_0(Y)-\Phi_\lambda(Y)\le\lambda/2$. To optimize the gradient numerically, use the exact scalar formula

$$\Phi_\lambda(Y)=\min_{t\ge0}\left[t+\sum_i b_i\psi_\lambda(g_i-t)\right],\qquad
\psi_\lambda(u)=\begin{cases}0&u\le0,\\ u^2/(2\lambda)&0<u<\lambda,\\ u-\lambda/2&u\ge\lambda.\end{cases}\tag{2}$$

At a minimizer $t$, $v_i=b_i[(g_i-t)/\lambda]_0^1$ and $t(1-\sum v)=0$. Any $t\ge0$ gives an upper certificate in (2). The derivative in the $Y$ variables is $-v_i/M_i$ off the mark; its Lipschitz constant is at most $\max_i b_i/(\lambda M_i^2)$. This follows by comparing the two variational inequalities for the strictly concave maximizing $v$ in (1), or by viewing it as a weighted Euclidean projection. Projecting that derivative with $L$ preserves the target mark and mean.

Put $\mathcal H_q(\lambda)=\inf_Y\Phi_\lambda(Y)$ on the specified affine slice. The exact dual is

$$\boxed{\displaystyle
\mathcal H_q(\lambda)=\max_{W\in U_\sigma,\ W\ge0,\ S=\sum W\le1}
\left[a_s W_0-\mu S-\frac{\lambda}{2}\sum_{i\ne0}M_i h_i W_i^2\right].}\tag{3}$$

Indeed interchange the affine infimum and the maximum over the compact convex set $C$ by finite-dimensional minimax. Write $w_i=v_i/M_i$ off the mark and set $w_0=0$. The infimum is finite exactly when $Lw=0$. Set $\gamma=-\ell^\mathsf T w/\kappa$ and $W=w+\gamma e_0$. Then $PW=0$, $\sum v=\sum w+\gamma=S$, and $-\langle w,Y\rangle=a_s\gamma-\mu S$. Cases $\gamma<0$ cannot yield a positive value because $a_s>\mu>0$. Conversely, every feasible $W$ in (3) satisfies the capacities in (1): pairing with $W^{(i)}$ gives $h_i W_i\le\langle W,W^{(i)}\rangle=S\le1$. The quadratic term is $\sum v_i^2/b_i=\sum M_i h_i W_i^2$. The affine infimum is also attained: use auxiliary real variables $s_i\ge\max(g_i-t,0)$ in (2), project the resulting polyhedron onto $(t,s)$, and minimize the continuous coercive objective there.

At $\lambda=0$, formula (3) gives the exact missing mean $(\mu_* -\mu)_+$ from Round 20. Formula (3) at positive $\lambda$ still gives both sides: each primal trial bounds it above, and an exactly feasible $W$ bounds it below. Neither bound requires an optimal support or a small gradient.

## Isolating the broad witness margin

Assume $a_s=O(\sqrt n)$ and keep $\mu>0$ fixed. For mass-one feasible $W$ let $m_{\rm eff}(W)=(\sum_{i\ne0}W_i)^2/\|W_{\rm off}\|_2^2$, and define

$$\Delta_q(K)=\sup_{W\in U_\sigma,\,W\ge0,\,\sum W=1,\,m_{\rm eff}(W)\ge K m_0}(a_s W_0-\mu)_+$$

with supremum zero if the slice is empty. The Jacobi point cap gives $W_0=O(m_0^{-1})$, so uniformly for mass-one witnesses

$$B(W):=\sum_{i\ne0}M_i h_i W_i^2\asymp \frac{m_0}{m_{\rm eff}(W)}.$$

For every $K\ge1$ and $\lambda>0$, absolute comparison constants (also depending on the bound on $a_s/\sqrt n$ and the fixed $\mu$) give

$$\boxed{\displaystyle
\Delta_q(K)-C\lambda/K\le\mathcal H_q(\lambda)\le\max\{\Delta_q(K), C K/\lambda\}.}\tag{4}$$

A broad witness can be inserted at mass one, paying at most $C\lambda/K$. For narrower witnesses write $W=uV$ with $\sum V=1$ and $0\le u\le1$. The linear margin of $V$ is uniformly bounded by the point cap, and $B(V)\ge c/K$. Maximizing $u\Delta-\lambda B(V)u^2/2$ bounds this branch by $C K/\lambda$. Consequently, along any specified field family and marks satisfying the bound,

$$\lim_{\lambda\to\infty}\limsup_q\mathcal H_q(\lambda)=\lim_{K\to\infty}\limsup_q\Delta_q(K).\tag{5}$$

For the lower bound take the field limsup with $\lambda,K$ fixed and then $K\to\infty$. For the upper bound take $\lambda\to\infty$ at each fixed $K$ and then send $K$ to infinity. The limits on both sides exist by monotonicity. In particular, large-penalty decay of the smooth primal optimum would exclude every prime obstruction whose effective support divided by $m_0$ diverges. At mean one, a fixed gap $\vartheta_\sigma/\sqrt n>1+\delta$ supplies a positive margin for the actual mark $a_s/\sqrt n\to1/(1+s)$ once $s$ is sufficiently small. Bounded effective size still needs its own argument, including the low-energy critical case. The large-penalty prime estimate in (5) remains open.

An immediate sufficient bound for (5) is a uniform $O(\sqrt{m_0})$ Euclidean minimum defect on the anchored slice. In fact (2) at $t=0$ and $\psi_\lambda(u)\le(u_+)^2/(2\lambda)$ give $\mathcal H_q(\lambda)\ll\min_Y\|(-Y)_+\|_2^2/(\lambda m_0)$. This relaxes the vanishing normalized minimum defect required to close the entire conjecture. Inequality (4) also offers an a posteriori bound for large-effective-size witnesses from any single finite upper certificate.

## The exact squared-field comparison

On square plus, let $I$ be the subfield annihilator with $h=(\sqrt q+1)/2$. For $W=\mathbf1_I/h$, set $d=a_s/h-\mu>0$. On $I\setminus\{0\}$, $M_i=h/(h-1)$ and the anchored kernel height is $h_I=h-2+2/(h-1)$ by the square Jacobi entries. Thus $B(W)=h_I/h<1$, and the scaled square witness gives

$$\mathcal H_q(\lambda)\ge\max_{0\le u\le1}\left[ud-\frac\lambda2\frac{h_I}{h}u^2\right].\tag{6}$$

There is equality whenever a trial has its defect constant on $I\setminus\{0\}$ and is nonnegative off $I$. This holds in the two [exact square rows from Round 20](anchored-repair-20.md#the-square-control) at mean one. The $g_i$ then equal $d$ on the subfield bulk and are nonpositive elsewhere. For a prescribed mass of $v$ on that bulk the least quadratic cost has equal weights, and its total capacity is $h/h_I>1$. Thus (1) attains the right side of (6). In particular, as $\lambda\to\infty$ this exact obstruction falls as $d^2/(2\lambda(h_I/h))$, although the unsmoothed missing mean is the positive number $d$. The square dual lower in (6) holds regardless of whether the flattened trial has been verified.

## A weighted endpoint estimate from the reflected profile

The anchor-average argument in [the cross-ratio note](parallel-crossratio-21.md#3-the-cap-does-work-with-a-strong-endpoint-moment) also improves the weak-$\ell_2$ requirement in [Astra's weighted cap argument](astra-broad-21.md#3-a-weighted-rich-correlation-obstruction-at-subcritical-energy). Let $g$ be any nonzero profile on $Q$, with $N=\|g\|_2^2$ and normalized correlations

$$r(u)=\frac{\sqrt q}{N}\left|\sum_{x\in Q}g(ux)\overline{g(x)}\right|\quad(u\ne1).$$

If $q^{-1}\sum_{u\ne1}r(u)^{3/2}\le C$ uniformly, then $\langle g,(I-\rho\mathcal T)g\rangle\ge c(C)N$ for each sign $\rho$. Here $\mathcal T$ is the additive Paley operator, restricted by extending $g$ as zero. To see it, use the [cap coefficients](parallel-rectangle-20.md#1-a-smooth-jacobi-cap) at $M_j=4^j$, and set $v_j=\sqrt q\,|a_{M_j,\rho}|$ off identity. With mass $1/q$ per point, $\|v_j\|_2\ll 2^{-j/2}$ and $\|v_j\|_\infty\ll2^j$, at fixed number of scales and sufficiently large field. Splitting $V_K=\sum_{j\le K}v_j$ at scale $2^{j_0}\asymp t$ shows $\Pr(V_K>t)\ll t^{-3}$ until its upper bound $O(2^K)$. Hence $\|V_K\|_3=O(K^{1/3})$ and the averaged correlation contribution is $O(C^{2/3}K^{-2/3})$ by Hölder. The averaged identity coefficient is $O(K^{-1})+o_q(1)$. With $K$ fixed large enough, the averaged cap mass is at most $N/2$. The bound $1-P_{M_j,\rho}(x)\le M_j(1-\rho x)/2$ implies the claimed gap. The proof works at any profile energy $N$. Proving this moment for actual reflected prime obstructions remains an arithmetic task.

## Replay

The [script](soft-tail-21.py) solves the scalar budget in (2) and uses accelerated projected gradient iterations. It certifies the selected primal trial by rounding its direction in the allowed Fourier sector and exactly removing the marked component. This gives a trial of the actual reference mark and prescribed mean. The value upper bound then evaluates (2) with interval arithmetic, allowing for the error of the stationary reference. Square plus rows also carry the exact subfield lower in (6). The other projected-dual values recorded by the iteration are floating-point diagnostics.

For a sufficiently positive projected dual on a prime, the script also rounds one mass-one candidate in the opposite sector and adds a rational constant to ensure nonnegativity. It divides by its exact mass, encloses the quadratic cost in (3), and optimizes the overall scale against the lower margin. This gives a proof-grade lower bound independent of the primal trial. The remaining per-step dual columns are diagnostic.

The [mean-one comparison](soft-tail-21-certified.jsonl) contains 120 rows and 30 interval upper bounds. On all three primes and both signs the certified upper is at most $1.3\cdot10^{-12}$ for all three penalties. The [smaller-mean comparison](soft-tail-21-low-certified.jsonl) contains 72 rows and 18 upper bounds, with six rounded prime lower bounds and three square subfield lower bounds. All replay parameters use their exact binary values. Representative intervals at width $1/64$ are rounded outward below.

| Order and sign | Mean | Penalty | Lower | Upper |
|---|---:|---:|---:|---:|
| $1000033,-$ | $1$ | $1/8$ | $0$ | $1.1\cdot10^{-12}$ |
| $389^2,+$ | $1$ | $1/8$ | $0.30891323$ | $0.30891326$ |
| $389^2,+$ | $1$ | $1$ | $0.06944583$ | $0.06944585$ |
| $389^2,+$ | $1$ | $8$ | $0.0086807292$ | $0.0086807304$ |
| $153649,+$ | $0.96$ | $8$ | $0.00167245$ | $0.00537056$ |
| $153649,-$ | $0.96$ | $8$ | $0.00160653$ | $0.00540257$ |

The square optimum at mean one falls with increasing penalty despite an unsmoothed missing mean of approximately $0.37077551$. The prime comparison at the smaller mean exhibits a strictly positive smoothed optimum that the rounded dual detects. These finite intervals do not bound the field limsup in (5). A separate dense check compared 24 primal minimizations with constrained dual quadratic programs on both signs at $29,97,7^2,11^2$.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/soft-tail-21.py --steps 64 --certify-max-order 1000033
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/soft-tail-21.py --primes 9413 153649 --square-roots 389 \
  --mean .96 --steps 128 --certify-max-order 153649
```
