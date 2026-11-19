# Centered variation of the stationary floor path

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the signed sum in [parallel-temperature-7.md](parallel-temperature-7.md#directed-gains-between-two-true-stationary-pairs) has two new bulk lower certificates. A single pair of floors has an exact upper bound on a product of exponential moments; the gap bounds marked movement and separates it from mass lost in a trajectory limit. A mesh has a different budget, for the **centered variance of the log slopes**. That test passes to compact-interval trajectory laws with a truncation error uniform in the mesh. Neither certificate has a saturation proof through all primes.

## One pair: an exact deficit for two sampled coordinates

Keep $c=1-1/n$, $W_t=1+ct$, $m(t)=\gamma_0(t)$. Sample $I$ uniformly from the **unmarked** coordinates, so $\mathbb E_q$ divides by $n-1$; the $g(t)$ of [bulk-logarithm.md](bulk-logarithm.md) is $c\mathbb E_q\gamma_I(t)$. For $0<a<b$, write

$$
 D=\gamma_I(a)-\gamma_I(b),\quad d=m(a)-m(b),\quad
 C=\sqrt{W_aW_b},\quad H=c\sqrt{ab},\quad M_s=\mathbb E_q e^{sD}\quad(s=\pm1).
$$

The opposite Fourier supports give the two exact mixed products $H M_s+e^{sd}=C$. Multiplying the bulk moments gives a nonnegative deficit:

$$
 \boxed{(C-1)^2-H^2 M_+M_-=2C(\cosh d-1).}                         \tag{1}
$$

For an independent copy $D'$ at the **same two floors**, $M_+M_-=\mathbb E_q\cosh(D-D')$. Thus (1) bounds an unsigned spread unchanged by adding a common constant to the bulk increments. A lower bound $P\le M_+M_-$ gives

$$
 |d|\le 2\operatorname{arsinh}\sqrt{\frac{(C-1)^2-H^2P}{4C}}.       \tag{2}
$$

One long pair can therefore control the entire signed floor sum $2d$, with no intermediate mesh. Lower certificates include the product of the two means of $\min(R,e^{\pm D})$ and the expectation of $\cosh(\lambda(D-D'))$ for $0\le\lambda<1$. The signs can also be certified separately: a lower bound $P_s\le M_s$ gives $sd\le\log(C-HP_s)$. Ignoring rare sites can weaken these certificates but cannot make them false.

### What is lost in a trajectory limit?

On any compact $[a_*,b_*]\subset(0,\infty)$, pass to a subsequence along which the sampled log paths converge in law in $C([a_*,b_*])$ and $m_q\to m_\infty$ uniformly. Write $X$ for the limiting random path. Bulk tightness is as in [parallel-temperature-7.md](parallel-temperature-7.md#a-bulk-scalar-of-the-true-two-floor-inverse); the mark has uniform bounds and a uniform Lipschitz constant. Fix endpoints $a<b$ in this compact, put $U_s=\mathbb E e^{s(X(a)-X(b))}$, $C_\infty=\sqrt{(1+a)(1+b)}$, $H_\infty=\sqrt{ab}$ and $d_\infty=m_\infty(a)-m_\infty(b)$.

The exact products identify the limits $\bar M_s=(C_\infty-e^{s d_\infty})/H_\infty$, which need not equal $U_s$. Fatou, or increasing bounded caps, gives $B_s=\bar M_s-U_s\ge0$. In fact

$$
 (C_\infty-1)^2-H_\infty^2 U_+ U_-
 =2 C_\infty(\cosh d_\infty-1)
   +H_\infty^2\big(B_+U_-+B_-U_++B_+B_-\big).                   \tag{3}
$$

Exhausting the observable budget at one pair forces both zero marked movement and zero loss of exponential moments there. Zero marked movement alone need not exhaust it. The one-sided version is $C_\infty-H_\infty U_s=e^{s d_\infty}+H_\infty B_s$.

For example, fix one hot $b$ with $m_q(b)\to0$ and choose $a_k\downarrow0$. If the supremum of the left side of (3) over prime limit laws at $[a_k,b]$ tends to zero, (2) and the small-floor bound imply $m_q(0)\to0$. For a one-sided theta bound it suffices that the corresponding supremum of $C_\infty-H_\infty U_s$ is at most $1+o_k(1)$; the two signs may use different pairs. These are field-first tests at fixed endpoints and fixed caps, followed by removal of the caps.

For fixed $0<\lambda<1$ the fractional exponential test passes to the path law: the exact moments bound $\mathbb E_q e^{|D-D'|}\le2M_+M_-$, giving an $L^{1/\lambda}$ bound for $e^{\lambda|D-D'|}$. Sending $\lambda\uparrow1$ **after** the field limit gives $U_+U_-$ by monotone convergence of the paired cosh. If $b$ is a hot anchor with $\sup_{q,i\ne0}|\gamma_i(b)|\le K_b$, $B_s$ is between $e^{-K_b}$ and $e^{K_b}$ times the loss in $\mathbb E_q e^{s\gamma_I(a)}$ at the cold floor. Indeed $e^{sD}=e^{s\gamma_I(a)}e^{-s\gamma_I(b)}$; bound the excess over a cap using cold-floor thresholds scaled by $e^{\pm K_b}$ and let those thresholds tend to infinity. The hot bound is provided for $b\ge1024$ by the [large-floor invariant ball](large-smoothing.md). The loss in question is of *first* moments of scaled spectra.

A lower test can also use only signed conditional log means. For a finite partition $\mathcal A$ of the bulk, for example bins of a bounded hot field, conditional Jensen gives $M_s\ge\sum_{B\in\mathcal A}\mathbb P_q(B)\exp(s\,\mathbb E_q[D\mid B])$. This avoids estimating the tails of $e^{sD}$ but can miss within-bin fluctuations. Binning just the Jacobi field leaves a substantial gap at primes in the replay below.

## A different budget: centered log slopes measured on a mesh

The sum of the two mixed identities is

$$
  \cosh d-1+H\,\mathbb E_q(\cosh D-1)=\Delta_{ab},
  \qquad
  \Delta_{ab}=C-1-H=\frac{c(\sqrt b-\sqrt a)^2}{C+1+H}.
$$

Divide this by $(b-a)^2/2$ and take $a,b\to t$ on the diagonal. The difference of the mixed identities gives the first derivative relation. Smoothness at each finite order gives

$$
 (m')^2+ct\,\mathbb E_q[(\gamma_I')^2]=\frac{c}{4tW_t},
 \qquad \mathbb E_q\gamma_I'=-\frac{m'}{ct}.
$$

Subtract the square of the bulk mean. With $\rho_q(t)=c/(2W_t)$, this becomes

$$
 \boxed{2ct^2\operatorname{Var}_q(\gamma_I'(t))
          +\frac{m'(t)^2}{\rho_q(t)}=\rho_q(t).}                  \tag{4}
$$

Centering charges a change in the mark for both the marked derivative energy and the necessary bulk mean drift. For $[a,b]$ let $L_q[a,b]=\int_a^b\rho_q=\tfrac12\log(W_b/W_a)$. For a mesh $\mathcal G$ of this interval, let $D_{lr}=\gamma_I(l)-\gamma_I(r)$ and define the credit

$$
 V_q(\mathcal G)=\sum_{[l,r]\in\mathcal G}
                  \frac{2c\,lr}{r-l}\operatorname{Var}_q(D_{lr}).
$$

The centered increment is minus the integral of the centered slope. Weighted Cauchy–Schwarz with $\int_l^r t^{-2}\,dt=(r-l)/(lr)$ gives $V_q(\mathcal G)\le\int_a^b2ct^2\operatorname{Var}_q(\gamma_I')\,dt$. A second Cauchy–Schwarz on the marked displacement gives the finite certificate

$$
 |m(a)-m(b)|^2
 \le L_q[a,b]\,\big(L_q[a,b]-V_q(\mathcal G)\big).                \tag{5}
$$

In contrast to (1), the quadratic test can be made bounded with an error **uniform in the mesh**. Put $T_R(x)=\max(-R,\min(x,R))$, $R\ge1$, and let $V_{q,R}$ use $\operatorname{Var}_q(T_R(D_{lr}))$. Clipping decreases variance by the independent-copy formula. Also

$$
 \begin{aligned}
 \|D_{lr}-T_R(D_{lr})\|_{L^2(\mathbb P_q)}^2
     &\ll e^{-R}\mathbb E_q(\cosh D_{lr}-1),\\
 0\le\operatorname{Var}_q(D_{lr})-\operatorname{Var}_q(T_R(D_{lr}))
     &\ll e^{-R/2}\mathbb E_q(\cosh D_{lr}-1).
 \end{aligned}
$$

The first bound compares $(|x|-R)_+^2$ with $\cosh x-1$; for the second use the reverse triangle inequality on centered $L^2$ and $\mathbb E_q D_{lr}^2\le2\mathbb E_q(\cosh D_{lr}-1)$. The mixed identity bounds the last expectation by $\Delta_{lr}/(c\sqrt{lr})$. Multiplying by the mesh coefficient costs at most $2\sqrt{lr}\Delta_{lr}/(r-l)\le c(r-l)/4$. Thus

$$
         0\le V_q(\mathcal G)-V_{q,R}(\mathcal G)
                    \ll (b-a)e^{-R/2}.                          \tag{6}
$$

The error does not grow under subdivision. Equation (5) holds with the capped credit without even using (6).

For sampling, take $k$ independent pairs of uniform bulk indices and reuse each pair across the mesh. Each pair contributes the weighted sum of $(T_R(D_{lr})-T_R(D'_{lr}))^2/2$, with mean $V_{q,R}$ and range $[0,A]$ for $A=2R^2\sum_{[l,r]}2c\,lr/(r-l)$. Subtracting $A\sqrt{\log(1/\eta)/(2k)}$ from the sample average gives a lower certificate with probability at least $1-\eta$ by Hoeffding. The sample size can be chosen independently of field order at a fixed mesh and cap. The bound grows under refinement; it does not justify a fixed sample size for moving meshes.

Alternatively, for any centered bounded arithmetic test $f=f(I)$, completion of a square gives

$$
          \operatorname{Var}_q D_{lr}
            \ge 2\mathbb E_q[D_{lr} f]-\mathbb E_q f^2.
$$

Optimizing over a finite span gives the credit from the orthogonal projection of the centered increment onto that span. An arithmetic proof can therefore use signed log correlations against fixed test fields if they account for almost the whole variance budget. It need not identify the full trajectory law.

### The field-first statement

For a limit $(X,m_\infty)$ as above, $X$ lies in $H^1([a,b])$ almost surely, with finite expected squared slope. In the limit (4) gives the local inequality

$$
  2t^2\operatorname{Var}(X'(t))
       +2(1+t)m_\infty'(t)^2\le\frac{1}{2(1+t)}
                  \qquad\text{for a.e. }t\in[a,b].              \tag{7}
$$

Test (4) against a nonnegative continuous function and use lower semicontinuity of weighted squared derivative energy under uniform convergence, then under weak convergence of path laws. For the variance term apply this to the difference of independent paths and divide by two. Strictly positive test weights suffice by adding a constant and sending it to zero. The $H^1$ assertion follows in the same way from the uniform bound on the expected uncentered derivative energy. Weak convergence of paths need not preserve the derivative energy, so (7) can have a positive defect.

Set $L=\tfrac12\log((1+b)/(1+a))$, $V(X)=\int_a^b2t^2\operatorname{Var}(X'(t))\,dt$. The limiting mesh credits converge to $V(X)$ on refinement: for a pair $X,Y$ of independent paths, the discrete slopes used by the credit are averages of $t^2(X'-Y')$ in the measure $dt/t^2$. These piecewise averages converge in $L^2$ as the mesh tends to zero. At each **fixed** mesh the capped credit passes to the field limit by bounded continuous tests; (6) removes the cap at a cost independent of the mesh. Thus the deficit $L-V(X)$ is accessible from squared log differences even when there is exponential loss in (3).

One sufficient prime criterion is: for a sequence $a\downarrow0$ and a fixed hot $b$ with $m_q(b)\to0$, every compact-interval prime limit has $V(X)=L$ on $[a,b]$. More generally, take $a_k\downarrow0,\ b_k\uparrow\infty$ and require the supremum over prime limit laws of $L_k(L_k-V(X))$ to tend to zero. Take the field limit first on each compact. Then (5), $|m_q(0)-m_q(a_k)|\le\tfrac12\log W_{a_k}$, and the [elementary hot mark bound](marked-response.md#an-integral-for-the-conjectured-limit) imply $m_q(0)\to0$. Saturation is stronger than the target: a flat mark does not preclude a bulk slope defect. Fixed-depth parity of odd log tests does not supply the lower variance estimate for the *true* floor path. This criterion is separate from the [public analytic route](https://jig.so/p/7?s=1), which needs a prime estimate on actual complex Hessian nulls.

## Square orders consume a fixed part of both budgets

For $q=r^2$ the [subfield certificate](square-order-control.md#a-square-order-comparison) gives $\vartheta(\overline H_q)=r-1$. For $0<a<1$, the small-floor bound therefore gives

$$
  \liminf_{r\to\infty}m_q(a)\ge\delta_a:=\tfrac12\log\frac{2}{1+a}.
$$

Choose $b$ large and fixed with $\delta=\delta_a-\sqrt3/(2\sqrt b)>0$. The elementary hot mark bound gives $d_\infty\ge\delta$ in every square limit at this pair. With the large-floor result $m_q(b)\to0$ from [bulk-logarithm.md](bulk-logarithm.md#an-integral-with-a-uniformly-integrable-integrand), one can use $\delta_a$ itself. By (3) the observable pair deficit is at least $2C_\infty(\cosh\delta-1)>0$, even with no exponential loss. By (5) or (7) the centered variation deficit is at least $\delta^2/L$ for every limiting mesh credit and for $V(X)$. The signed floor sum has field liminf at least $2\delta$. These obstructions hold at **fixed** positive floors, persist for arbitrary caps and refinements, and do not rely on a model of square concentration.

## Finite replay

I used [the stationary FFT solve](../poisson_weights.py) and $\gamma_i=\operatorname{arsinh}(v_i/(2\sqrt{w_i}))$. Eighteen pairs at primes $9413,37253,151337$ and squares $97^2,193^2,389^2$ tested (1) and the directional mixed identities. The largest stationary residual was $2.0\cdot10^{-12}$ and the largest mixed-product error $1.5\cdot10^{-11}$. Selected results at $[0.05,8]$ follow. The pair gap uses the left side of (1); its capped version uses $\min(16,e^{sD})$ for both signs. The mesh has geometrically spaced floors.

| Order | $d$ | Pair gap | Capped pair gap | $L_q-V_q$, 16 intervals | $L_q-V_q$, 64 intervals |
|---:|---:|---:|---:|---:|---:|
| $9413$ | $-0.001099$ | $0.00000371$ | $0.001922$ | $0.004945$ | $0.000317$ |
| $37253$ | $-0.001106$ | $0.00000376$ | $0.000956$ | $0.004932$ | $0.000314$ |
| $97^2$ | $+0.311775$ | $0.301211$ | $3.54399$ | $0.253368$ | $0.246995$ |
| $193^2$ | $+0.317633$ | $0.312755$ | $3.65981$ | $0.276474$ | $0.269242$ |

Clipping increments at magnitude $3$ did not change these mesh credits to the displayed precision. A conditional Jensen lower test with 64 uniform bins across $[-1.42,1.42]$ of $\sqrt n\,Ke_0$ gave pair gaps about $1.8$ at the primes in the table; those bins alone do not give a useful long-pair certificate. At $[0.05,1024]$ exponential cap $16$ also lost significant credit at these primes. These are floating-point checks. The open step is a lower bound reaching a budget through all primes, or a signed cancellation estimate when saturation fails.
