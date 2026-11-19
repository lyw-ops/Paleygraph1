# Certified activation losses on actual Picard prefixes

The [Round 26 contraction criterion](parallel-activation-26.md) uses actual source-generated increments. A fixed-depth limiting law does not supply its prime-uniform growing-depth estimate. Here the finite prefixes themselves are certified by interval arithmetic. The method keeps the exact coordinatewise harmonic activation loss, root secants, and mean reserve. It gives a stronger finite comparison than replacing all these losses by a weighted second-moment bound.

Four 128-step prefixes at floor $\tau=1/20$ are certified: primes $9413,153649$ and squares $97^2,389^2$. Additional root-aware products are certified on the first prime/square pair. At $p=9413$ a verified invariant ball then bounds the actual orbit and its exact fixed point for **all subsequent depths**. These are finite-field results. No uniform prime estimate or proof of Problem 26 is claimed.

The [unequal-rate and time-block theorem](parallel-rate-27.md) supplies a new way to combine these losses. Its backward root/bulk recursion is a weighted vertex-cover problem on time when root information is discarded. Favorable bulk losses at an arbitrary positive fraction of times need not suffice; a fraction greater than one half does suffice on the stated uniform prefixes. An alternating linear example explains this restriction without claiming to be a nonlinear orbit.

## 1. Norm shadowing avoids exploding coordinate intervals

Use unscaled variables

$$
c_0=4,\qquad c_i=4\tau/n\ (i\ne0),\qquad
F(v)=K\Phi(v),\quad \Phi_i(x)=\sqrt{x_i^2+c_i},
\quad v_0=0,\quad v_{t+1}=F(v_t).
$$

Both $K$ and $\Phi$ are nonexpansive in $\ell_2$. Floating point chooses rational trial points $p_t$, with common denominator $2^{60}$. It supplies no trusted error estimate. Arb encloses every local defect

$$\eta_t=\|F(p_t)-p_{t+1}\|_2\le\widehat\eta_t.$$

Starting with $p_0=0$ and $E_0=0$, the outward recurrence

$$
E_{t+1}=E_t+\widehat\eta_t
\quad\Longrightarrow\quad \|v_t-p_t\|_2\le E_t
\tag{1}
$$

is a rigorous actual-orbit bound. Every FFT in the local defect is an Arb DFT of an exact rational point's activation. The cyclic sign masks come from integer finite-field constructions. The code hashes the entire sequence of selected rational points; regenerating a different trial sequence would require new local verifications, rather than trusting the old bounds.

This propagates a norm bound using nonexpansiveness, without repeatedly applying the absolute-value Fourier matrix to coordinate radii. The four final norm errors are below $1.581\cdot10^{-13}$. Independent dense 192-bit Arb matrix evolution at $p=61$ checks the trajectory bounds and all loss directions; see [the independent audit](parallel-rate-27-orbit-audit.py).

## 2. Certifying a harmonic bulk loss

At step $t$, put $x=p_t$, $y=p_{t+1}$, $d=y-x$, $e=E_t$, $e'=E_{t+1}$ and $E_D=e+e'$. The true increment $D=v_{t+1}-v_t$ satisfies $\|D-d\|_2\le E_D$.

For a coordinate with activation constant $c$, set

$$Q(x,y)=\frac{\sqrt{x^2+c}\sqrt{y^2+c}+xy+c}{2}.$$

The true secant $s=(v_t+v_{t+1})/(\Phi(v_t)+\Phi(v_{t+1}))$ obeys $1-s^2=c/Q(v_t,v_{t+1})$. Since

$$|\partial_xQ|\le[\sqrt{y^2+c}+|y|]/2,$$

the following is a conservative upper bound on its true denominator:

$$
Q^+=Q(x,y)+\frac12\left[
(\Phi(y)+|y|+2e')e+(\Phi(x)+|x|+2e)e'\right].
\tag{2}
$$

All quantities are enclosed outward. Let $w_i$ be a nonnegative lower bound for $\min(1,c_i/Q_i^+)$. Then $w_i\le1-s_i^2$. On the bulk $B$, the triangle inequality gives

$$
\boxed{\quad
\delta_t:=\frac{\sum_B(1-s_i^2)D_i^2}{\|D_B\|_2^2}
\ge
\left[
\frac{(\|\sqrt w\,d_B\|_2-E_D)_+}
{\|d_B\|_2+E_D}
\right]^2.
\quad}
\tag{3}
$$

Use lower and upper norm enclosures in the numerator and denominator. If the true bulk increment is zero the corresponding contraction is vacuous. The proof uses $\|\operatorname{diag}(\sqrt w)(D-d)\|\le E_D$; it does not sum coordinate error bounds as if independent.

For comparison the script also certifies the endpoint-weighted amplitude $A_t$ from Round 26. For either endpoint $p$ and its error $e$,

$$
\|v_BD_B\|_2\le\|p_Bd_B\|_2+\|p_B\|_\infty E_D
                         +e(\|d_B\|_2+E_D).
$$

Dividing by $(\|d_B\|-E_D)_+$ and multiplying the squared ratio by $n$ gives an upper bound for the scaled amplitude. This yields the weaker loss bound $4\tau/(A_t+4\tau)$. Both columns below are certified **lower bounds**, widened downwards, at depth 64.

| Field | Harmonic loss (3) | Second-moment loss |
|---|---:|---:|
| $9413$ | 0.1773686 | 0.0371577 |
| $97^2$ | 0.00632080 | 0.0000903872 |
| $153649$ | 0.1689949 | 0.0356763 |
| $389^2$ | 0.000834924 | 0.0000740809 |

These bounds certify the actual nonlinear prefixes, in contrast to the floating-point moment diagnostics in the preceding round. The square rows retain their delayed slow contribution.

## 3. Root, mean, and block products

Formula (2) at the root, with $c_0=4$, also gives a rigorous upper bound $a_t$ for its squared secant. Write $h=\Phi(v_{t+1})-\Phi(v_t)$. Its mean reserve is

$$m_t=(\sum_i h_i)^2/(n\|D\|_2^2).$$

The trial activation difference has norm error at most $E_D$, so its sum has error at most $\sqrt n E_D$. Subtract that error from the absolute trial sum, take the positive part, and upper-bound $\|D\|$ by $\|d\|+E_D$ to certify $m_t$ from below. The exact loss identity then gives

$$
\frac{\|D_{t+1}\|^2}{\|D_t\|^2}
\le q_t:=\min\{1,\max(1-\delta_t,a_t)-m_t\}.
\tag{4}
$$

The recorded $q_t$ use the indicated outward bounds. Multiplication yields a residual bound at time $T$ of $\|D_0\|\sqrt{\prod_{t<T}q_t}$. The initial norm is enclosed directly, rather than replaced by a bound invalid at large floors. The CLI restricts floors to $(0,1)$.

The program compares this with two conservative alternatives. The paired bound uses $1-(1-2/n)\min(\delta_{2j},\delta_{2j+1})$. The [time-block theorem](parallel-rate-27.md) uses $\bar\rho_t=\max(1-\delta_t,1/2)$, $\Gamma=n/(n-2)$, and backward weights

$$u_T=v_T=1,\qquad u_t=a_tv_{t+1},\quad
v_t=\bar\rho_t\max(u_{t+1},v_{t+1}).$$

Dropping its nonnegative mean improvement gives energy factor $\min(1,\Gamma^T\max(u_0,v_0))$. The version with $a_t=1$ discards root information and equals the minimum weighted vertex-cover budget minus the finite-field inflation. All these are upper bounds, so taking their minimum is valid.

At time 128 the [root-aware certificates](harmonic-orbit-27-root-certified.jsonl) give these outward-rounded residual upper bounds:

| Field | Paired | Block, root discarded | Block, root retained | One-step, root and mean |
|---|---:|---:|---:|---:|
| $9413$ | 0.004971 | 0.004548 | 0.000008584 | 0.000004022 |
| $97^2$ | 0.471302 | 0.467039 | 0.089471 | 0.040274 |

The maximum squared root secant is below $0.000017432$ and $0.050903$, respectively. Thus the worst-case undamped-root comparison is conservative on these finite prefixes. No uniform root bound is inferred from the table.

For the prime prefixes, the minimum certified bulk losses through step 127 exceed $0.1563821$ and $0.1644233$. The corresponding square minima exceed only $0.00487319$ and $0.000592648$. These minima describe four fixed fields and 128 steps. A positive finite critical-budget margin does not prove an asymptotic limit: the required margin must diverge along primes, the trial norm must be controlled, and the marked value must vanish.

More generally, a field-independent summable upper envelope for the increments throughout the growing horizon suffices to transfer fixed-depth marked cancellation. For example, a uniform time-block budget $S_{q,T}\ge cT^\beta-C$, $c,\beta>0$, on every prefix up to the required horizon supplies such an envelope. A budget only at the final time gives no such tail bound. The prime arithmetic estimate for this entire horizon is still missing.

## 4. A certified all-future tail at one prime

There is a separate finite validation beyond the prefix. For a rational center $p$ and radius $R$, put

$$\kappa(R)=\max_i\frac{|p_i|+R}{\sqrt{(|p_i|+R)^2+c_i}}<1.$$

The map $F$ is $\kappa(R)$-Lipschitz on the Euclidean ball $\overline B(p,R)$. If

$$\|F(p)-p\|\le(1-\kappa(R))R,\qquad E_T<R,$$

the ball is invariant and contains the actual state $v_T$. Banach's theorem places every future iterate and the exact fixed point in the ball. In particular

$$\|v_t\|\le\|p\|+R,\qquad
A_t\le n\max_{i\ne0}(|p_i|+R)^2\quad(t\ge T).$$

At $p=9413$, $T=128$, the interval computation verifies $R=1/500$, $\kappa<0.997985666$, invariance margin greater than $5.6055\cdot10^{-8}$, and entry error less than $1.227\cdot10^{-13}$. Hence

$$\boxed{\quad\|v_t\|<2.294685\quad\text{for every }t\ge128.\quad}$$

Its all-future scaled bulk amplitude is below $49.4943$. This is a conservative pointwise bound, not the much smaller observed increment-weighted amplitude. No tail ball was certified for the square at this prefix within the tested radius menu; that failure does not establish nonexistence of an invariant ball at a later prefix. The constants at one prime do not establish a uniform theorem over primes.

## Replay and scope

```sh
export VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
.venv/bin/python -B research/harmonic-orbit-27.py 9413 --square-roots 97 --steps 128
.venv/bin/python -B research/harmonic-orbit-27.py 153649 --square-roots 389 --steps 128
.venv/bin/python -B research/harmonic-orbit-27.py 9413 --square-roots 97 \
  --steps 128 --root-budget
.venv/bin/python -B research/parallel-rate-27-orbit-audit.py
```

The [first prefix certificates](harmonic-orbit-27-certified.jsonl), [larger prefix certificates](harmonic-orbit-27-larger-certified.jsonl), and [root/tail certificates](harmonic-orbit-27-root-certified.jsonl) separate local orbit errors, actual loss bounds, and derived products. The last file repeats the first pair's same rational paths with additional certificates; these are not independent sampled trajectories. Mathematical audit checked shadowing, (2)--(4), all product indices, and the local invariant-ball argument. The independent dense audit uses direct cosine sums without the FFT evaluator and encloses the actual orbit in 192-bit Arb.

The next estimate must concern actual prime increments or sources on the entire required horizon. [Astra's cone gap](astra-increments-27.md) handles nonnegative source on a critical coset union with exterior leakage explicit; the [signed transport inverse lemma](parallel-transport-27.md) records what critical concentration and sign information would be needed to apply that gap. Neither supplies the broad prime estimate. Problem 26 remains open in this campaign.
