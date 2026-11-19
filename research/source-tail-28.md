# A signed source-tail certificate without the stationary norm

This gives a direct ordinary-theta certificate from any rational trial vector. It replaces the unknown stationary Euclidean norm by a one-sided, signed support function of the transformed residual. The stationary reciprocal pair supplies a sharp bulk cap coupled to its unknown marked value. A scalar threshold and an explicit one-variable maximum enclose the resulting support function. Neither a stationary solve nor a floating-point optimizer is trusted by the certificate.

The new target differs from Euclidean coercivity. [Astra's fixed-forcing construction](astra-broad-source-28.md) has vanishing total absolute reciprocity error and diverging source norm, while its signed-tail bound tends to zero. Thus that norm obstruction does not refute this certificate. A prime estimate for the **actual** source tail on the required horizon is still unproved. The certificate and finite computations do not solve Problem 26.

## 1. Exact signed discrepancy

Use $q\equiv1\pmod4$, $n=(q-1)/2$, $h=\tau/n<1$, $w_0=1$, $w_i=h$ on the bulk, and $W=1+(n-1)h$. Let $v^*=K\Phi(v^*)$, $u^*=\Phi(v^*)$, with $\Phi_i(v)=\sqrt{v_i^2+4w_i}$. For any trial $z$ put

$$
r=z-K\Phi(z),\quad b=-Kr=\Phi(z)-\overline{\Phi(z)}\mathbf1-Kz,
\quad S_z=\sum_i\Phi_i(z)/\sqrt n.
$$

In particular $\sum b=0$. The mean-zero correction of $z$ in the implementation is convenient; the identities below also hold without it. Stationarity gives $\sum u^*=2\sqrt{nW}$. Therefore the exact hyperbolic discrepancy is

$$
\boxed{\quad
\Delta=\langle u^*,\Phi(z)\rangle-\langle v^*,z\rangle-4W
=2\sqrt W S_z-4W+\langle b,u^*\rangle\ge0.
\quad} \tag{1}
$$

Writing $v_i^*=2\sqrt{w_i}\sinh\gamma_i$ and $z_i=2\sqrt{w_i}\sinh\eta_i$, this equals $4\sum_iw_i[\cosh(\gamma_i-\eta_i)-1]$. Consequently any upper bound $D\ge\Delta$ gives

$$
|\gamma_0-\eta_0|\le R:=\operatorname{arcosh}(1+D/4),\qquad
\frac{e^{\eta_0-R}}{\sqrt W}
\le\frac{\theta_+}{\sqrt n}\le\sqrt W e^{\eta_0+R}.
\tag{2}
$$

The last step is the ordinary theta bracket from the positive stationary Fourier pair. No factor involving $\|v^*\|_2$ occurs in (1)--(2).

## 2. The reciprocal pair gives more than a common height cap

Let $A=(u^*+v^*)/2$, $B=(u^*-v^*)/2$. They are positive complementary Fourier-sector rows, have equal mean $\sqrt{W/n}$, and satisfy $A_0B_0=1$, $A_iB_i=h$ off the mark. The [translation identity](translation.md) gives $A_i\le A_0$ and $B_i\le B_0$. One short proof uses

$$\sum_iw_i\log(A_{i+j}/A_i)
\le\sum_iB_i(A_{i+j}-A_i)=0.$$

The constant bulk weights cancel after summation, leaving $(1-h)\log(A_j/A_0)\le0$. The same argument applies to $B$.

The Jacobi entry bound and the means give

$$A_0,B_0\le C:=(1+\sqrt q)\sqrt{W/n}.$$

Put $s=u_0^*=A_0+B_0$. Then $2\le s\le C+C^{-1}$. The off-mark product is $h$, so maximizing $x+h/x$ over the interval allowed by the two root caps gives the sharper bound

$$
\boxed{\quad
a:=2\sqrt h\le u_i^*\le M(s):=
\frac{1+h}{2}s+\frac{1-h}{2}\sqrt{s^2-4}
\quad(i\ne0).
\quad} \tag{3}
$$

In particular $u_i^*\le C+h/C$, which is appreciably smaller than the root bound at a small floor. The function $M$ is increasing and concave on $[2,\infty)$.

Let $\mathcal B=2\sqrt{nW}-na$. Removing the baseline $a\mathbf1$, the root consumes excess mass $d=s-a$; the bulk excess has sum $\mathcal B-d$ and each entry lies in $[0,M(s)-a]$. For upper bounds we may enlarge the true feasible root set to

$$2\le s\le s_{\max}:=\min(C+C^{-1},\mathcal B+a).$$

Some points in this interval can fail the bulk total-cap constraint. Including them only weakens an upper bound. A common-cap calculation with cap $s$ would instead impose $\mathcal B/n\le d\le\mathcal B$; that feasibility condition must not be omitted when claiming an exact common-cap optimum.

## 3. One threshold and an explicit concave maximum

Choose **any real** threshold $t$ and set $U_t=\sum_{i\ne0}(b_i-t)_+$. The box and mass constraints imply

$$
\langle b,u^*\rangle\le
(s-a)(b_0-t)+(M(s)-a)U_t+t\mathcal B.
\tag{4}
$$

Here the baseline vanishes because $\sum b=0$. Negative values of $b$ and negative thresholds are retained. This is not a top sum of the positive part of $b$.

Write $\alpha=(1+h)/2$, $\beta=(1-h)/2$ and

$$L=b_0-t+\alpha U_t,\quad J=\beta U_t\ge0,\quad
T=t\mathcal B-a(b_0-t+U_t).$$

The right side of (4) is exactly

$$F_t(s)=Ls+J\sqrt{s^2-4}+T.$$

It is concave. Its maximum on $[2,s_{\max}]$ occurs at an endpoint or, when $L<-J$ and the point is inside the interval, at

$$s_*=-\frac{2L}{\sqrt{L^2-J^2}},\qquad
F_t(s_*)=T-2\sqrt{L^2-J^2}. \tag{5}$$

Thus $D=\max(0,2\sqrt W S_z-4W+\max_sF_t(s))$ is a certificate in (2). The scalar mass term is kept with its sign. A numerical minimization merely suggests a useful $t$; every selected threshold has the proved upper-bound property. No global optimality assertion for that numerical minimization is needed.

The [implementation](source-tail-28.py) saves the rounded rational trial and threshold. Arb reconstructs $z$, its activation, and $Kz$, encloses $b$, and rounds each cost upward to the exact grid $10^{-14}\mathbb Z$. It then computes $U_t,L,J$ rationally and encloses (5) and the endpoints at 160 bits. Replacing costs by componentwise upper bounds remains safe after the zero-sum baseline has been removed for the true $b$, since the coefficients of $b_0$ and $U_t$ in (4) are nonnegative. Uncertain endpoint comparisons include the critical point conservatively.

The standalone `--replay-input` branch calls no optimization or stationary solver. It checks the field, scales, symmetry and rational-input premises. A safeguarded Newton proposal, when selected, is only a trial generator; its convergence is not an assumption of the certificate and it is not labeled an actual Picard prefix.

## 4. What the tail asks for on a true trajectory

For the actual unaveraged Picard trial $z=v_t$, $t\ge1$,

$$b_t=(I-J)[\Phi(v_t)-\Phi(v_{t-1})]
=(I-J)(g_t-g_{t-1}),$$

where $g_t=\Phi(v_t)-\Phi(0)\ge0$. For the averaged iteration $z_{t+1}=(z_t+K\Phi(z_t))/2$ starting at zero,

$$
b_t=(I-J)\left[\Phi(z_t)-
\sum_{j<t}2^{-(t-j)}\Phi(z_j)\right]. \tag{6}
$$

These identities locate the missing estimate in the **positive centered activation change**, with its marked value and signed scalar mass term retained. A bound for arbitrary approximate profiles is not a bound for (6) on actual prime trajectories.

The effective tail capacity in the corresponding exact box support function is $O_\tau(\sqrt n)$. [Astra's construction, §5](astra-broad-source-28.md) proves that the norm-divergent fixed-forcing profiles have $b_0=O_\tau(\delta)$ and $\max_{i\ne0}b_i=O_\tau(\delta/\sqrt n)$, with the scalar term also $O_\tau(\delta)$. Taking the latter bulk upper bound as a threshold in (4) gives a complete discrepancy certificate $D=O_\tau(\delta)$. It can therefore certify the mark while Euclidean distance from the true stationary source diverges. This is a proved separation of the two criteria; those constructed profiles are not actual iterates and do not have a conjecturally vanishing marked value imposed.

For a prime-aspect proof one still needs trials with $\eta_0\to0$ and a bound on (1)--(5) tending to zero, in the field-first/floor limit or along a justified growing horizon. A finite small residual, a finite positive budget, or uniform integrability without a compatible test-function estimate does not establish that input.

## 5. Finite certified comparisons

The [first nine certificates](source-tail-28-certified.jsonl) use primes 61 and 9413 and square order $97^2$ at averaged Picard depths 8, 32, 128. The [next nine](source-tail-28-larger-certified.jsonl) use primes 153649 and 1000033 and square order $389^2$ at depths 32, 128, 512. Their proposals are floating point; their reported discrepancy and theta bounds are Arb certificates for the saved rational trials. They are not interval bounds on the trials' distance from exact Picard iterates.

At $\tau=1/20$, selected marked-error upper bounds from (2), rounded upward, are:

| Field | Depth 32 | Depth 128 | Depth 512 |
|---|---:|---:|---:|
| $9413$ | 0.2564 | 0.02165 | — |
| $153649$ | 0.28646 | 0.02304 | 0.000003442 |
| $1000033$ | 0.30012 | 0.02476 | 0.000003499 |
| $97^2$ | 0.58685 | 0.41000 | — |
| $389^2$ | 0.63549 | 0.57229 | 0.41051 |

The square theta controls lie in every corresponding certified interval. The $p=61$ intervals also contain the independently computed finite LP diagnostic. These comparisons preserve the square obstruction and illustrate a finite improvement; they do not prove a prime-uniform rate.

The [small-floor Newton proposals](source-tail-28-tight-certified.jsonl) separately test whether this direct certificate gives useful finite theta intervals. Their metadata explicitly distinguishes them from Picard trajectories. Every certificate remains valid independently of how its proposal was found.

At $p=9413$, $\tau=1/10000$, the certified marked hyperbolic error is below $1.638\cdot10^{-6}$ and the normalized theta lies in $[1.0003790,1.0004824]$, with both decimal endpoints rounded outward. This is a finite theorem about ordinary theta, not evidence of a uniform asymptotic rate. The [optimizer-free replay output](source-tail-28-replayed.jsonl) repeats the certified quantities from each accepted rational input exactly.

The [acceptance record](source-tail-28-acceptance.json) covered 19 interval records at the round-28 checkpoint. The pending small-floor proposal at $p=1000033$ subsequently completed with exit code zero in round 29 and passed independent optimizer-free replay, raising the accepted total to 20. Its normalized theta interval is $[1.0007690,1.0008822]$, rounded outward. The former terminal session `82328` is complete and must not be treated as a live wait. The [root-dependent refinement](root-coupled-tail-29.md) gives an additional finite improvement from the same inputs.

Reproduce from the repository root:

```sh
export VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
.venv/bin/python -B research/source-tail-28.py 61 9413 --square-roots 97 \
  --steps 8 32 128 --certify
.venv/bin/python -B research/source-tail-28.py 153649 1000033 --square-roots 389 \
  --steps 32 128 512 --certify
.venv/bin/python -B research/source-tail-28.py 9413 1000033 \
  --tau 1/10000 --newton --certify
.venv/bin/python -B research/source-tail-28.py \
  --replay-input research/source-tail-28-q9413-tau1_20-t128-input.json
```

Independent audit checked the discrepancy constants, signed cap, sharper root coupling, scalar maximum and outward arithmetic. The prime estimate on the actual signed source tail remains the research task. No full solution of Problem 26 is asserted.
