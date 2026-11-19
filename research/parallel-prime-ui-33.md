# Prime source UI as a positive-floor conic boundary slope

Round 33, 2026-11-18. ETH Problem 26, **ordinary** theta.

**Status.** Prime-uniform source UI is not proved, nor is ETH26. This note
gives a different exact target: the entire escaping first mass equals the
right boundary slope of a concrete convex optimization problem on the two
**actual Paley positive spectral cones**. Its objective involves known
weights and feasible trial pairs, not the unknown stationary point. There
is a dimension-free, finite tail upper certificate and a simple conic dual
lower certificate. The reduction uses full stationary reciprocity and both
complementary sectors; it does not assume the round-32 hard-tail response
hypothesis (HR), inverse-source tightness, or a stationary L2 bound.

The accompanying code also turns an exact rational Fourier pair into an
Arb certificate for tails of the **unknown exact stationary source**.
Floating Newton solves propose the pair; they are not trusted in its replay.
Verified finite results and replay commands appear in Sections 6--7.

## 1. Normalization and relation to the earlier obstructions

Fix tau>0, n=(q-1)/2, c=tau/n, W=1+(n-1)c, a=sqrt(W/n), and
rho=c/a^2=tau/W. Let E_+=span(1)+V_+ and E_-=span(1)+V_- be the actual
even cyclic Paley spectral spaces, with multiplier chi(1-t) on Q. For the
actual reciprocal stationary pair set

\[
 u=A/a,\qquad v=B/a,\qquad m=w/a^2,
 \qquad m_0=n/W,\quad m_i=\rho\ (i\ne0).
 \tag{1}
\]

Write E f=n^{-1}sum_i f_i. Exactly,

\[
 u\in E_+,\quad v\in E_-,\quad u,v>0,\quad
 Eu=Ev=Em=1,\quad uv=m.
 \tag{2}
\]

The roles of the two sectors can be exchanged. Fixed-floor root caps in
[round 32](parallel-circulant-source-32.md) imply u0+v0=O_tau(sqrt n), hence
their normalized first mass tends to zero. All limits below keep tau fixed.

The requested bulk source is

\[
 G=\sqrt W\,(u+v-2\sqrt\rho)\quad(i\ne0).
 \tag{3}
\]

Thus UI of G is equivalent to joint UI of u,v. If Lambda is the escaping
first mass defined in (14), the corresponding escaping G first mass is
sqrt(1+tau)*Lambda. Adding the bounded constant in (3) does not alter a
first-moment escape limit: its contribution on a tail is bounded by a
constant times the tail's probability, which is O(1/R).

The log/shift identities of round 32 and the log-moment bounds do not
control this endpoint. The actual-prime Fejer obstruction already in
[square-order-control](square-order-control.md) and
[translation](translation.md) excludes an argument using positive spectrum,
support, and a root cap alone. No such counterexample is repeated here.
The identity below instead needs the **full opposite positive reciprocal
source** in (2). The earlier KL identity for feasible pairs in
[Fable 28, D2](claude-fable-28.md) is also relevant: exact positivity repair
remains an arithmetic problem. The new point is an exact first-mass
interpretation and quantitative tail transfer for a different, conic
fidelity objective; it is not a claim that positivity repair is automatic.

## 2. A computable fidelity defect equals the unknown-source error

Take any positive feasible trial pair

\[
 p\in E_+,\quad q\in E_-,\quad Ep=Eq=1.
 \tag{4}
\]

Opposite sectors imply **all four** cross identities

\[
 E(pq)=E(uq)=E(pv)=E(uv)=1.
 \tag{5}
\]

Define the computable defect

\[
 \mathcal D(p,q)
 =E\big(\sqrt m-\sqrt{pq}\big)^2
 =2-2E\sqrt{mpq}\ge0.
 \tag{6}
\]

**Exact error identity.**

\[
 \boxed{\quad
 \mathcal D(p,q)
 =E\big(\sqrt{uq}-\sqrt{vp}\big)^2.
 \quad}                                                     \tag{7}
\]

Indeed expansion of the right side uses (5) and uv=m. This is not an
estimate of the stationary distance from a floating residual. The left
side is determined by the **feasible pair and prescribed weights only**.
In particular, the large mark is included in (6) and (7).

On the bulk write

\[
 r=\sqrt{\rho p/q},\quad s=\sqrt{\rho q/p},\quad
 e_i=(\sqrt{u_iq_i}-\sqrt{v_ip_i})^2.
\]

Then pointwise

\[
 e_i=q_i\frac{(u_i-r_i)^2}{u_i}
     =p_i\frac{(v_i-s_i)^2}{v_i},\qquad Ee=\mathcal D.
 \tag{8}
\]

These are stronger than a log-moment bound: they control a weighted
**first-mass** discrepancy. A very small q or p still costs a reciprocal
factor. The explicit positive floor below keeps that factor visible.

### A dimension-free joint tail certificate

Suppose p_i,q_i>=kappa>0 on the bulk. Put

\[
 M(R)=E\big[u\mathbf1_{i\ne0,u>R}
                +v\mathbf1_{i\ne0,v>R}\big].
\]

For R>sqrt(rho) the two high sets are disjoint because uv=rho. On the
u-high set use u=(u-r)+r in L2 with measure E(1/u); on the v-high set use
v=(v-s)+s with measure E(1/v). The triangle inequality on their disjoint
union, (8), and Ep=Eq=1 give

\[
 \begin{split}
 \sqrt{M(R)}
 &\le\sqrt{\mathcal D/\kappa}
  +\left[E\left(\frac{\rho p}{qu}\mathbf1_{u>R}
                      +\frac{\rho q}{pv}\mathbf1_{v>R}\right)\right]^{1/2}\\
 &\le\sqrt{\mathcal D/\kappa}
             +\sqrt{2\rho/(\kappa R)}.
 \end{split}
\]

Consequently

\[
 \boxed{\quad
 M(R)\le\frac{(\sqrt{\mathcal D(p,q)}+
                         \sqrt{2\rho/R})^2}{\kappa}.
 \quad}                                                     \tag{9}
\]

Only bulk floor bounds are needed for (9); the optimization below imposes
the same floor everywhere for convenience. The mark error contributes
positively to D and is retained. No bound on p's maximum, on stationary
energy, or on an opposite projection is needed. For example, a proved
trial gap D<=epsilon*kappa and R>=2rho/(epsilon*kappa) imply M(R)<=4epsilon.

The same argument on just one high set gives

\[
 E[u\mathbf1_{i\ne0,u>R}]
 \le(\sqrt{\mathcal D}+\sqrt{\rho/R})^2/\kappa
 \tag{10}
\]

for every R>0, without a disjointness restriction.

### Pointwise bounds useful for finite certified replays

Since e_i<=nD, (8) is a quadratic inequality in u_i. Every bulk coordinate
obeys

\[
 \boxed{\quad
 u_i\le r_i+\frac{n\mathcal D}{2q_i}
       +\sqrt{\frac{n\mathcal D r_i}{q_i}
                      +\left(\frac{n\mathcal D}{2q_i}\right)^2}.
 \quad}                                                     \tag{11}
\]

Exchange (u,r,q) with (v,s,p) for the other bound. This estimate loses n,
so it is a **finite** certification tool, not the uniform UI theorem.
Summing its outward upper bounds at coordinates whose upper bound exceeds
R gives a valid tail certificate. In particular an upper maximum below R
proves that the exact source tail at R is empty.

## 3. The conic problem: the escaping mass is exactly its boundary slope

For 0<=kappa<=1 define

\[
 d_n(\kappa)=\min\{\mathcal D(p,q):
   p\in E_+,\ q\in E_-,\ Ep=Eq=1,\ p,q\ge\kappa\}.
 \tag{12}
\]

The feasible set is compact and nonempty (p=q=1). On it the objective is
2-2E sqrt(mpq), a convex function because the geometric mean is concave.
An explicit SOCP formulation is

\[
 \begin{array}{ll}
 \text{maximize}& E[\sqrt m\,t]\\
 \text{subject to}& p\in E_+,\ q\in E_-,\ Ep=Eq=1,\ p,q\ge\kappa,\\
                 &t_i\ge0,\quad t_i^2\le p_iq_i,
 \end{array}
 \qquad d_n(\kappa)=2-2\,\text{maximum}.
 \tag{13}
\]

The quadratic constraint is the usual rotated second-order cone. This
formulation uses the actual Paley signs; it does not use a supplied
stationary point. At kappa=0 the actual (u,v) is feasible and d_n(0)=0.
Convex interpolation of feasible pairs proves convexity of d_n in kappa.
Therefore d_n(kappa)/kappa is nondecreasing in kappa>0.

Let F be **any** sequence of these actual fields with n->infinity (in
particular all primes p=1 mod4). Define

\[
 \Lambda_{\mathcal F}
 =\lim_{R\to\infty}\limsup_{n\in\mathcal F} M_n(R).
 \tag{14}
\]

**Boundary-slope theorem.** With the fixed-floor root caps,

\[
 \boxed{\quad
 \Lambda_{\mathcal F}
 =\lim_{\kappa\downarrow0}\limsup_{n\in\mathcal F}
                            \frac{d_n(\kappa)}{\kappa}.
 \quad}                                                     \tag{15}
\]

In particular, prime source UI is **equivalent** to the right side being
zero. It suffices to construct actual positive feasible trial pairs with

\[
 \lim_{\kappa\downarrow0}\limsup_{p\to\infty}
                 \mathcal D(p_{p,\kappa},q_{p,\kappa})/\kappa=0.
 \tag{16}
\]

This is a sufficient construction criterion with no unknown-source pairing.
It does **not** assert that the particular numerical repair procedure below
attains the optimum, or that actual Picard trajectories satisfy (16).

There is a quantitative payoff to a superlinear defect rate. For example,
if uniformly in the field-limsup sense
d_n(kappa)<=C*kappa^(1+alpha), alpha>0, then choosing
kappa=(2*rho_infinity/(C*R))^(1/(1+alpha)) in (9) gives

\[
 \limsup_n M_n(R)\le
 4C^{1/(1+\alpha)}(2\rho_\infty/R)^{\alpha/(1+\alpha)}
 \tag{16a}
\]

for all sufficiently large R. A quadratic defect bound would give an
explicit O(R^(-1/2)) first-mass tail. Merely d_n(kappa)->0 without its
division by kappa supplies no UI conclusion.

**Proof of the lower inequality in (15).** Apply (9) to an optimizer of
(12). At fixed kappa take the field limsup, and then R->infinity. Since
rho_n->rho_infinity=tau/(1+tau)>0, this gives

\[
 \Lambda_{\mathcal F}
 \le\limsup_{n\in\mathcal F}d_n(\kappa)/\kappa.
 \tag{17}
\]

The limit as kappa decreases exists by the monotonicity above.

**Proof of the opposite inequality.** Use the following feasible pair for
the proof only:

\[
 p=(1-\kappa)u+\kappa,\qquad q=(1-\kappa)v+\kappa.
 \tag{18}
\]

This is not proposed as a computable source-free construction. Write
z=u+v, b=(1-kappa)sqrt m, and

\[
 T=\kappa(1-\kappa)z+\kappa^2,\qquad
 \delta=\sqrt{b^2+T}-b\ge0.
\]

Then sqrt(pq)-sqrt m=delta-kappa sqrt m, so

\[
 (\sqrt{pq}-\sqrt m)^2\le\delta^2+\kappa^2m,
 \qquad \delta^2\le\min\{T,T^2/(4b^2)\}.
 \tag{19}
\]

For any L>0 the bulk has b^2=(1-kappa)^2 rho and T<=kappa(z+1).
Use the quadratic bound when z<=L and the linear bound otherwise. At the
mark use delta0^2<=T0. The resulting explicit finite inequality is

\[
 \begin{split}
 \frac{d_n(\kappa)}\kappa
 &\le\kappa+
 \frac{\kappa(L+1)^2}{4(1-\kappa)^2\rho_n}
 +(1+1/L)E[z\mathbf1_{i\ne0,z>L}]\\
 &\quad+\frac{(1-\kappa)(u_0+v_0)+\kappa}{n}.
 \end{split}                                                \tag{20}
\]

The last line vanishes in the field limit. On the bulk uv=rho_n, so the
escaping first mass of z=u+v equals (14): the smaller member is <=sqrt rho,
and on a tail where the larger member exceeds R it is <=rho/R; moving a
threshold by a bounded amount cannot change the R->infinity escape limit.
Take the field limsup in (20), then kappa->0 with L fixed, then L->infinity.
This gives the reverse of (17) and proves (15).

The loss of uniformity is explicit. For **each finite field** d_n(kappa)=0
whenever kappa<=min(u,v). Thus every finite problem has zero derivative at
zero. The field-first boundary slope in (15) can nevertheless be positive.
Interchanging those limits would erase every field-dependent boundary layer;
the finite square controls below make that risk concrete.

## 4. A conic dual certificate and a practical new arithmetic target

The following elementary certificate gives lower bounds on d_n(kappa),
independently of a stationary solve. Choose alpha_i,beta_i>=0 with
alpha_i beta_i>=m_i. Suppose there are real a,b and mean-zero sector vectors
z_- in V_-, z_+ in V_+ such that

\[
 a+z_-\ge\alpha,\qquad b+z_+\ge\beta.
 \tag{21}
\]

For every feasible p,q from (12), AM--GM and sector orthogonality give

\[
 \begin{split}
 2E\sqrt{mpq}&\le E(\alpha p+\beta q)\\
 &\le(1-\kappa)(a+b)+\kappa E(\alpha+\beta).
 \end{split}
\]

Hence

\[
 \boxed{\quad
 d_n(\kappa)\ge
 2-(1-\kappa)(a+b)-\kappa E(\alpha+\beta).
 \quad}                                                     \tag{22}
\]

For example E(alpha p)=a-E[(a+z_--alpha)p]
<=a-kappa E(a+z_--alpha). This proves the claimed floor contribution;
discarding it loses the boundary slope. Product and positivity constraints
can be checked with rational arithmetic or intervals. This note does not
claim a new nonzero prime-uniform dual lower bound, or a dual attainment
theorem beyond this valid weak-duality certificate.

The next arithmetic target is therefore concrete: construct primal feasible
Paley pairs with o(kappa) defect uniformly through primes, or discover a
nonzero boundary-slope dual certificate. A genuine positive prime slope
would refute UI, while a primal construction as in (16) would prove it.
The optimization is convex, uses the given multiplier, and has verifiable
finite upper and lower certificates. Unlike a bounded exponential log
moment, its **linear** boundary rate is precisely the missing first mass.

A certified actual tail lower bound M_n(R)>=L also gives a lower
certificate for the conic problem, directly from (9):

\[
 d_n(\kappa)/\kappa\ge
       (\sqrt L-\sqrt{2\rho_n/(\kappa R)})_+^2.
 \tag{23}
\]

This can be useful when a very accurate reciprocal-source witness is easier
to obtain than a good positive-floor conic dual witness.

## 5. Routes compared and the scope of the computation

1. **Logarithms, shifted ratios, and analytic-center first variations.**
   These reduce to the existing cross-correlation and reverse-KL budgets.
   They provide no superlinear first-mass estimate. Not promoted to a proof.
2. **Positive cone/sparse spectral gap alone.** The already known actual-prime
   Fejer example defeats this route. It lacks the full reciprocal opposite
   pair; (7) and the boundary theorem retain that constraint.
3. **Actual increment/higher-tail monotonicity.** The exact activation losses
   in [round 26](parallel-activation-26.md) are useful but do not by themselves
   yield a prime-uniform first-mass bound. No tail-monotonicity assertion is
   made on the basis of finite runs.
4. **Strictly positive opposite feasible pairs.** This gives (7)--(22),
   an exact escape-mass theorem, a new conic formulation, and certified
   finite source tails. Its remaining burden is the uniform primal repair
   rate (16), rather than HR. It does not solve the arithmetic approximation
   step after source/inverse-source tightness in round 29 either.

The script projects the two raw spectra of a real Picard/Newton proposal
onto their exact complementary spaces, adds a constant when needed, and
normalizes each mean to one. If a projected spectrum C has mean b and
minimum l, adding max(0,(kappa*b-l)/(1-kappa)) imposes the requested floor
before normalization. This simple repair is a **trial**, not the optimizer
of (12). In floating computations an attained floor may differ from kappa
by roundoff; the finite bound always uses the measured minimum. Rigorous
replay instead checks the rounded rational Fourier pair and uses an outward
lower endpoint, with no reliance on that measured float minimum.

The stored Fourier coefficients are integers divided by 2^90, real and
even, with DC coefficient one and every forbidden coefficient exactly
zero. Arb DFT evaluates their exact spectra at 160 bits, proves positivity,
and encloses (6). It then applies (11) to the exact stationary source.
The high-precision replay needs no claim that a Newton iterate lies within
its reported residual of stationarity.

## 6. Verified finite results

### Exact-source interval certificates, including a million-order prime

The following are **outward rounded rigorous bounds** from the stored
rational Fourier inputs and Arb replay. They concern the exact stationary
source, not just the proposed numerical iterate.

| field order | tau | fidelity D upper | certified bulk floor lower | exact bulk max G upper |
|---:|---:|---:|---:|---:|
| 1000033 (prime) | .05 | 1.330e-25 | .00663891963809 | 6.90943062 |
| 1000033 (prime) | .01 | 3.552e-23 | .00128019534842 | 7.57382883 |
| 389^2=151321 | .05 | 3.149e-25 | .00013550999395 | 359.637209 |

At the two prime floors, both exact normalized spectra have bulk maximum
less than 8, as does G. Their first-mass tails at R=8,16,32,64,128 are
therefore **exactly zero**. This is finite information at one prime, not
UI through primes. The .05 million-order input was replayed at 192 bits,
and the square input at 224 bits, with the same displayed outward bounds.

The square certificate also encloses the actual source tail at every
R=8,16,32,64,128 by

\[
 .9218119478
 < E[G\mathbf1_{i\ne0,G>R}]
 < .9218119492.
 \tag{24}
\]

For the normalized pair at R=128 it gives
.9007153490 < M(128) < .9007153504. These are finite lower **and** upper
bounds, obtained from both roots of the quadratic in (11); they are not
inferred from thresholded floating-point support detection. The root
subtraction and all coordinates in the gap remain present.

### Actual conic optimum: certified primal/dual brackets

[The conic driver](parallel-prime-ui-33-conic.py) uses SLSQP to propose a
positive feasible pair, and LPs to propose the opposite-sector covers in
(21). It rounds the Fourier coefficients to exact rationals. The replay
proves the floor and primal feasibility, constructs alpha=sqrt(m)*lambda
and beta=sqrt(m)/lambda from positive rational lambda, and checks (21).
Thus alpha*beta=m is exact. No optimizer success flag, residual tolerance,
or floating dual feasibility is trusted. In particular the one square
kappa=.1 optimizer reported failure, yet its resulting rigorous (wider)
bracket is still valid; it is not used to claim exact optimality.

Selected **outward rounded brackets for d_n(kappa)/kappa**, at tau=.05:

| field order | kappa | rigorous slope interval |
|---:|---:|:---|
| 101 (prime) | .01 | [0, 3.177e-14] |
| 401 (prime) | .01 | [0, 2.883e-13] |
| 401 (prime) | .05 | [.2493888, .2493923] |
| 19^2=361 | .01 | [.1743623, .1743861] |
| 31^2=961 | .01 | [.2902258, .2902521] |
| 31^2=961 | .005 | [.1429443, .1429993] |

The finite positive slope values are secants at the displayed kappa. They
are **not** derivatives at zero or field-limit slopes. The tiny prime
upper bounds are genuine primal bounds, not equality-to-zero assertions.
The table is a useful test that the conic target has nontrivial, checkable
certificates on actual Paley data. It does not extrapolate the small-field
optima to all primes. All 13 primal/dual inputs are also replayed at 224 bits;
see [the complete replay](parallel-prime-ui-33-conic-all-replay224.jsonl).

### Uncertified orbit diagnostics, kept separate

The grid covers four actual primes 9413,153649,1000033,151337 and square
orders 97^2,389^2 at tau=.05, kappa=.001,.01,.05,.1. Proposals use actual
Picard depths 4,8,16,32,64,128 and a safeguarded Newton solve. There are
168 feasible-pair diagnostic rows and 1176 associated tail-bound rows.
The largest check of (7) against the numerical stationary pair differs by
3.587e-14. These checks are floating-point algebra diagnostics only.

For example, at kappa=.001 the simple projection/constant-repair trial has

| field order | D_trial/kappa at depth 32 | at depth 128 | Newton proposal |
|---:|---:|---:|---:|
| 1000033 | 18.6657 | 7.142e-8 | 1.330e-22 |
| 389^2 | 184.762 | 112.419 | .359793 |

The large early values are trial upper bounds, not optimal conic values.
In particular they can exceed the universal optimal upper bound
d_n(kappa)/kappa<=d_n(1)=2-2E sqrt(m). The existing actual-increment
identities explain why a late obstruction can evade shallow tests; these
records do not prove a depth-uniform contraction or tail monotonicity.

## 7. Replays and remaining work

All scripts, inputs, and records written in this round have the authorized
`parallel-prime-ui-33` prefix. No README, ledger, other-prefix file, commit,
push, or external communication is part of this work.

```sh
# Floating actual-trajectory diagnostics, not certificates.
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33.py \
  --primes 9413 153649 1000033 151337 --square-roots 97 389 --tau 1/20 \
  --steps 4 8 16 32 64 128 --stationary --kappa .001 .01 .05 .1 \
  > research/parallel-prime-ui-33-diagnostics.jsonl

# Generate and rigorously replay a million-order positive Fourier witness.
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33.py --primes 1000033 --tau 1/20 \
  --stationary --kappa .001 --certify-prefix research/parallel-prime-ui-33-certified \
  > research/parallel-prime-ui-33-certified.jsonl

# Replay the exact saved witness, without solving stationarity.
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33.py --precision 192 --replay \
  research/parallel-prime-ui-33-certified-q1000033-tau1_20-safeguarded-Newton-proposal-k0.001-input.json.gz \
  > research/parallel-prime-ui-33-certified-replay192.jsonl

# The second prime floor and the square exact-source control.
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33.py --primes 1000033 --tau 1/100 \
  --stationary --kappa .0001 --certify-prefix research/parallel-prime-ui-33-floor01 \
  > research/parallel-prime-ui-33-floor01.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33.py --square-roots 389 --tau 1/20 \
  --stationary --kappa .00001 --certify-prefix research/parallel-prime-ui-33-square \
  > research/parallel-prime-ui-33-square.jsonl

# Small conic optimum brackets. Optimization proposes; Arb replay proves.
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33-conic.py --primes 101 401 --square-roots 19 \
  > research/parallel-prime-ui-33-conic.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-prime-ui-33-conic.py --primes 1009 --square-roots 31 \
  --kappa 1/100 1/200 --output-prefix research/parallel-prime-ui-33-conic-large \
  > research/parallel-prime-ui-33-conic-large.jsonl
```

The remaining prime theorem is the uniform o(kappa) primal rate in (16),
or equivalently a vanishing conic boundary slope (15). A concrete stronger
target is d_p(kappa)<=C_tau*kappa^2, which would give (16a) with alpha=1.
Neither the observed positive floor at one prime, nor the finite conic
brackets, establishes such a rate. The construction of feasible pairs is
where a new prime-specific estimate must enter. HR and subsequent marked
arithmetic comparison remain separate open steps for ETH26; no conclusion
about ordinary theta is drawn from the finite UI certificates alone.

