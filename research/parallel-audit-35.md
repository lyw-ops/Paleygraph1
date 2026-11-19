# The remaining inverse bridge, and a direct finite-depth alternative

Round 35. This note proves a useful sector-preserving \(L^1\)
consequence of first-inverse source tightness, records precisely what
the proposed weight regularization does and does not supply, and
independently accepts the direct averaged-mark criterion in
[averaged-mark-35](averaged-mark-35.md).

The original UI + actual HR route still lacks its arithmetic comparison.
There is no replacement of a first inverse by a second inverse, and no
removal of an inverse merely from weak convergence. The direct alternative
uses a specified finite-depth positive completion and bypasses that
particular stationary comparison. Its prime-uniform positivity is also
unproved.

## 1. First-inverse tightness gives bounded-energy affine \(L^1\) approximants

Use [source-pair 29](parallel-source-pair-29.md), Sections 1--3, exactly:
\(A=a1+x\), \(u=A/a\), \(a^2=W/n\), \(D_{ii}=\rho/u_i\),
\(\rho=\tau/W\), \(T=P_\sigma D P_\sigma|_{V_\sigma}\),
\(Tx=be\), and

$$
Q=\langle x,Tx\rangle<1,\qquad
x_\delta=b(T+\delta I)^{-1}e,\qquad
\Delta_\delta=\int\frac{\delta}{\lambda+\delta}\,d\nu(\lambda).
$$

The inherited source-energy estimate is
\(\|T^{1/2}(x-x_\delta)\|^2\le\Delta_\delta\), with
\(x_0-(x_\delta)_0=\Delta_\delta/b\). Set

$$\widetilde u_\delta=1+x_\delta/a.$$

There are two further finite inequalities:

$$
\boxed{\quad
\mathbb E_n|u-\widetilde u_\delta|
 \le\sqrt{\Delta_\delta/\tau},\qquad
\|x_\delta\|_2^2\le Q/\delta.
\quad}\tag{1}
$$

Indeed, including the exceptional marked entry,

$$
\|T^{1/2}(x-x_\delta)\|^2
 =\sum_i\frac{\rho}{u_i}(x_i-(x_\delta)_i)^2
 =\tau\,\mathbb E_n\frac{(u-\widetilde u_\delta)^2}{u}.
$$

Cauchy--Schwarz and \(\mathbb E_nu=1\) prove the first estimate.
For the second,

$$
\delta\|x_\delta\|^2
\le \langle x_\delta,(T+\delta I)x_\delta\rangle
=b^2\langle e,(T+\delta I)^{-1}e\rangle\le Q.
$$

Thus UI + actual HR, through their already proved implication
\(\lim_{\delta\downarrow0}\limsup_p\Delta_{p,\delta}=0\), give
affine-sector, mean-one \(L^1\) approximants with bounded physical
energy at every fixed regularization. Their physical marked values
also approximate \(A_0\).

This does not assert that \(\widetilde u_\delta\ge0\). It only bounds
the empirical first mass of its negative part by
\(\sqrt{\Delta_\delta/\tau}\). Nor are these finite-depth or
source-free approximants: their \(T\) is built from the unknown exact
stationary \(A\). A fixed-\(\delta\) empirical \(L^1\) estimate does
not supply the \(O(\kappa\sqrt n)\) **counting** deficit required
by the absolute-coherence repair of round 34. No quantitative rate
allowing those limits to be interchanged is present here.

The measure \(\nu=b^2\lambda^{-1}\mu_e\) in this argument is the
positive source measure for \(T\). Its tightness is a first-inverse
claim for \(\mu_e\). The stronger quantity
\(\|x\|^2=\int\lambda^{-1}\,d\nu\) is not used. The indefinite
marked-response operator in [marked-response](marked-response.md)
is a different operator; its inverse is not silently identified with
the one here.

## 2. Weight regularization: an exact transfer and the surviving unknown source

The proposed one-sided regularization is correct:

$$
w^{(\delta)}=w+\delta aA,\quad
A^{(\delta)}=\sqrt{1+\delta}\,A,\quad
B^{(\delta)}=\frac{B+\delta a}{\sqrt{1+\delta}},\quad
W^{(\delta)}=(1+\delta)W.
\tag{2}
$$

Both rows have mean \(a\sqrt{1+\delta}\), remain in their respective
affine sectors, and have product \(w^{(\delta)}\). Strict concavity
therefore identifies them with the actual pair for these new positive
weights. In normalized coordinates the opposite row is
\((v+\delta)/(1+\delta)\), uniformly bounded below by
\(\delta/(1+\delta)\).

The marked weight also changes. If \(\gamma_0=\log A_0\) initially,
the **new hyperbolic** marked logarithm is

$$
\gamma_0^{(\delta)}-\gamma_0
 =\frac12\log\frac{1+\delta}{1+\delta aA_0}.
\tag{3}
$$

Thus its fixed-\(\delta\), field-first change is generally
\(\frac12\log(1+\delta)\), not zero. The log of the unnormalized
first row changes by exactly \(\frac12\log(1+\delta)\).

There is also a symmetric version:

$$
\widehat A=A+\delta a,\quad \widehat B=B+\delta a,\quad
\widehat w=w+\delta a(A+B)+\delta^2a^2 1,\quad
\widehat W=(1+\delta)^2W.
\tag{4}
$$

Here the physical difference \(A-B\) and both centered rows are
unchanged. In particular the regularization supplies a positive
normalized floor but **does not bound the original centered energy**.
Its marked hyperbolic log changes by

$$
\frac12\log(1+\delta a/A_0)
-\frac12\log(1+\delta a/B_0)=O_{\tau,\delta}(n^{-1/2})
$$

using the actual fixed-floor root caps.

The positive inverse that (2) improves is the full compression

$$
S=P_\sigma\operatorname{diag}(B/a)P_\sigma
 =T+(b/a)e\otimes e,
\qquad S^{(\delta)}=\frac{S+\delta I}{1+\delta}
\tag{5}
$$

on \(V_\sigma\). The marked rank-one term must remain. Exactly,

$$
Sx=\frac{1-c}{a}e,\qquad
S^{(\delta)}x
 =\frac1{1+\delta}\left[\frac{1-c}{a}e+\delta x\right].
\tag{6}
$$

The now uniformly invertible compression has acquired an unknown
distributed forcing \(\delta x\). Dropping that forcing would produce
the resolvent approximation, not the stationary pair in (2). Its norm
cannot be bounded using a second-inverse estimate that is absent from
the hypotheses. This is the exact algebraic reason the new normalized
floor alone does not make the arithmetic comparison source-free.

UI does give a genuine marked transfer for truncating these weights.
Let

$$w^{(\delta,R)}=w+\delta a^2\min(u,R).$$

Along the linear interpolation of square roots between
\(w^{(\delta)}\) and \(w^{(\delta,R)}\), the marked square root is
at least one. The weighted response identity of marked-response
therefore gives

$$
\boxed{\quad
|\gamma_0(w^{(\delta)})-\gamma_0(w^{(\delta,R)})|
\le
\sqrt{\delta W\,\mathbb E_n(u-R)_+}.
\quad}\tag{7}
$$

Here \((\sqrt s-\sqrt t)^2\le|s-t|\) bounds the square-root weight
distance; the estimate remains valid when the marked weight changes.
UI makes this error small in the field-first, cutoff-second limit.
The bounded bulk profile \(\min(u,R)\), however, is still the
unknown stationary profile. Boundedness of a deterministic profile
does not give the fixed-expression arithmetic law used for actual
Picard iterates. No such replacement is made.

## 3. Independent proof of the direct finite-depth marked budget

This bypass is independent of (1)--(7). Use the undamped zero-start
Picard iteration, rather than the averaged update used in
[iterate majorants](iterate-majorants.md):

$$
v_0=0,\quad v_{t+1}=K\phi_t,\quad
\phi_t=\sqrt{v_t^2+4w},\quad
\mu_t=\mathbb E_n\phi_t/2,\quad E_t=\|v_t\|^2.
$$

Because \(K^2=I-J\),

$$E_{t+1}-E_t=4W-4n\mu_t^2.$$

For \(M_T=T^{-1}\sum_{t=1}^T\mu_t\), summation and Jensen give

$$
nM_T^2\le
W+\frac{E_1-E_{T+1}}{4T}
\le B_{n,T}:=
W+\frac{(1-\sqrt c)^2(1-1/n)}{T}.
\tag{8}
$$

Indeed \(v_1=2(1-\sqrt c)Ke_0\).
At fixed \(\tau,T\), the sharper upper budget tends to
\(1+\tau+1/T\), rather than \((1+\tau)(1+1/T)\).

For \(A_{\sigma,t}=(\phi_t+\sigma v_t)/2\), write

$$X_{\sigma,T}=M_T1+\frac1T\sum_{t=1}^TP_\sigma A_{\sigma,t}.$$

At a single time its exact vector expression is

$$
X_{\sigma,t}^{\rm one}
=\frac{\mu_t}{2}1+
\frac{\phi_t+Kv_t+\sigma(v_t+v_{t+1})}{4}.
$$

It follows that

$$
\begin{split}
X_{+,T}(0)-X_{-,T}(0)
 &=\frac1{2T}\sum_{t=1}^T(v_t(0)+v_{t+1}(0)),\\
X_{+,T}(0)+X_{-,T}(0)
 &=\frac{\mu_T-\mu_0}{T}
 +\frac1{2T}\sum_{t=1}^T(\phi_t(0)+\phi_{t-1}(0)).
\end{split}\tag{9}
$$

Thus inherited fixed-depth marked cancellation gives both limits one
at each fixed \(T\). For growing \(T=T_n\), it is sufficient that

$$T_n^{-1}\sum_{t=0}^{T_n+1}|v_t(0)|^2\longrightarrow0.$$

The endpoint \(T_n+1\) is needed for the difference formula.
Cauchy--Schwarz controls its signed mean, and
\(\sqrt{4+x^2}-2\le x^2/4\) controls the source average.
The remaining mean boundary term is uniformly \(O_\tau(n^{-1/2})\)
because \(\mu_T\le\sqrt{W(T+1)/n}\).

## 4. A specific arithmetic quantity sufficient for the finish

Normalize \(z_{\sigma,T}=X_{\sigma,T}/M_T\). For any chosen
\(\kappa>0\) below both marks, define the actual explicit deficits

$$
d_{\sigma,0}=0,\quad
d_{\sigma,i}=(2\kappa-z_{\sigma,T}(i))_+,\quad
R_\sigma=2L_\sigma-I,
\quad
S_\sigma=\max_{i\ne0}[-(R_\sigma d_\sigma)_i]_+.
\tag{10}
$$

The round-34 lemma gives a wholly finite-depth sufficient test:
if \(S_\sigma\le\kappa\) on both sides, the specified rows
\(p_\sigma=z_{\sigma,T}+2L_\sigma d_\sigma\) are positive, have
mean one, and preserve both marks. The more conservative bound
\(\Gamma_{n,\sigma}\|d_\sigma\|_1\le\kappa\) also suffices.
These tests involve only the prescribed finite orbit, the known
Paley projection, and one pointwise clipping. They involve neither
the stationary pair nor an inverse. They need no estimate for
the clipped fidelity objective.

For any such pair, opposite-sector orthogonality implies
\(\langle p_+,q_-\rangle=n\). Pairing any plus optimizer with
the minus row gives

$$
\frac{p_+(0)}{\sqrt n}
\le\frac{\theta_+}{\sqrt n}
\le\frac{\sqrt n}{p_-(0)}.
$$

In particular, (8) and root preservation imply exactly Main's bound

$$
\frac{X_{+,T}(0)}{\sqrt{B_{n,T}}}
\le\frac{\theta_+}{\sqrt n}
\le\frac{\sqrt{B_{n,T}}}{X_{-,T}(0)}.
\tag{11}
$$

One needs positive marked denominators. They hold eventually under
the marked limits above. If the test (10), or any other verified
mean/mark/sector preserving positive completion, works for all
sufficiently large primes for a sequence
\(\tau_j\downarrow0,\ T_j\to\infty\), taking each field limit
first yields ETH26. Growing \(T_n\) is also valid with the stated
Cesaro condition and eventual positive completion.

This is an explicit constructive sufficient condition; no
prime-uniform estimate for its signed spill has been proved here.
The old iterate-majorant repair pays a mean increase, whereas
(11) depends on keeping the displayed mean budget. The old averaged
update and this raw Picard update should not be mixed when checking
their projection telescopes.

## 5. Square obstruction and the conic marked comparison

For square orders \(\theta_-=(r+1)/2\) and
\(\theta_-/\sqrt n\to1/\sqrt2\). If \(\tau+1/T<1\), the
right normalization in (8)--(9) forces
\(z_{-,T}(0)/\sqrt n>1/\sqrt2\) eventually through squares.
No mean-one minus nonnegative row can preserve this mark. For
growing depth the same holds with the Cesaro condition and
\(\tau<1\). The square threshold uses the sharper budget
\(1+\tau+1/T\); it is not obtained by silently replacing the
coarser budget \(W(1+1/T)\).

For the saved round-34 \(389^2\), depth-48 minus input, direct
exact summation gives

$$
q_0=\frac{157965757215948832140631}{590295810358705651712},
\qquad
q_0-195=
\frac{42858074196001230056791}{590295810358705651712}>0.
$$

The independent script checks its actual minus Fourier support,
mean one, and evenness before applying the known exact
\(\theta_-=195\). This excludes every nonnegative completion
preserving **mean one, that sector, and that mark**. It does not
exclude changes of mean followed by renormalization, or conic
feasibility in general.

Main's conic comparison (11) also has the correct constant and sign.
For \(\gamma=\log A_0\), \(h=\frac12\log(p_0/q_0)\),
\(\alpha=p_0q_0/n\), the marked Hellinger error is exactly

$$
\frac{(\sqrt{u_0q_0}-\sqrt{v_0p_0})^2}{n}
=4\sqrt{\alpha/W}\,
 \sinh^2((\gamma-h)/2).
$$

The original fidelity marked summand is
\((W^{-1/2}-\sqrt\alpha)^2\). Thus \(D\to0\) and
\(h\to0\), with fixed floor, force the actual mark to zero;
an \(o(\kappa)\) rate is not needed for this **marked** conclusion.
This does not supply the hypotheses from source UI.

## 6. Replays and acceptance scope

The [independent minimal checker](parallel-audit-35.py) emits ten
records: four exact rational resolvent/regularization checks using
a nonconstant actual \(p=13\) stationary pair, four Arb192
zero-Picard averaged-budget checks at \(p=13\) and \(q=25\),
the exact square obstruction, and a final success row.

    .venv/bin/python -B research/parallel-audit-35.py \
      > research/parallel-audit-35.jsonl

The rational stationary pair uses \(\tau=30/19\) and
\(u=(3/2,5/4,3/4,1/2,3/4,5/4)\); its actual complementary
projection equations are checked exactly. It tests (1)--(6)
without approximating an inverse or using a floating stationary
solver. The small-orbit checks are normalization checks, not
positivity claims for the averaged proposals.

I also formally read Main's entire averaged-mark note and code,
and independently replayed all thirteen records to
[parallel-audit-35-main-replay.jsonl](parallel-audit-35-main-replay.jsonl).
They are byte-for-byte identical to its certificate. The five
prime root-only theta bounds correctly declare their dependency
on round-34 positive exact-input certificates; no new large
transform, exact Picard trajectory, or positivity construction is
misrepresented. Its conic comparison, sharp budget, square scope,
and fixed/growing-depth limit orders all pass this audit.

The actual missing stationary arithmetic bridge has not been
proved by (1)--(7). The direct criterion (10)--(11) is a different
finish with a source-free finite-depth target. Both its positive
completion estimate and the broader stationary route remain open.
Only this prefix is written; no shared-source, ledger, README,
commit, push, or external message is changed.

## 7. Independent acceptance of the structural complex-path note

I checked [parallel-complex-structure-35](parallel-complex-structure-35.md)
and its complete checker, taking the inherited mixed-product Mellin
norm estimate as input as requested. The seven records were independently
replayed to
[parallel-audit-35-complex-replay.jsonl](parallel-audit-35-complex-replay.jsonl)
and are byte-for-byte identical to its certificate. No correction is
required.

For Theorem 1, the complex square-root choices are well defined by
their binomial series on the radius-six Mellin ball. The scalar
rationalization bounds use
\(\operatorname{Re}\sqrt{1+w}\ge\sqrt{1-|w|}\), and
\(|1-\sqrt{\tau/n}|\le1\) follows from
\(|\sqrt{\tau/n}|<1\) and
\(|\arg\sqrt{\tau/n}|<\pi/4\). Both estimates are used only
on the specified hot region. The positive-coefficient series give
the stated \(S_2,S_3\); expanding a difference of powers into mixed
products gives exactly the extra factor \(2\ell\) in \(S_3\).
The resulting bounds \(B<5.13\), \(L<.78\) are uniform for
\(n,|\tau|\ge1024\) in that region.

The negative-type norm span is finite dimensional and complete.
The map is holomorphic and has a common contraction constant, so
its zero-start iterates converge locally uniformly to a holomorphic
fixed point. The region is connected, and real positive uniqueness
identifies its actual branch. The explicitly constructed roots
have nonzero product \(w_i\), proving coordinatewise nonvanishing.
The marked \(\operatorname{arsinh}\) is taken within its small
analytic disk, and its bound is below \(4/\sqrt n\).
No cold propagation follows from these hot estimates.

For Theorem 2 let \(C\) have columns \(\sqrt{w_i}v_i\).
It is a real coisometry \(CC^T=I\); after complexification,
both \(C\) and \(C^T\) still have Hermitian operator norm one.
Thus sandwiching the diagonal derivative multiplier is legitimate.
For \(|v_i^Tz|\le1/8\), its norm is bounded by

$$
\left[(1-1/8)^{-2}-1\right]
+|\delta|(1-1/8)^{-2}
\le17/49.
$$

The center displacement is at most one quarter of the ball radius,
so \(117/196\) is the correct self-map ratio. The leverage bound
\(w_i\|v_i\|^2\le1\) gives the advertised universal local disk.
Conversely its trace is the tangent rank, so (14) is the correct
lower bound on the largest row vector. The actual even-plus rank
\(\lfloor n/4\rfloor\) counts inversion pairs and includes the
self-inverse positive mode exactly at \(4\mid n\).
It forces this particular full-Hessian isotropic certificate to
have width of order \(n^{-1/2}\), not an actual complex singularity
within that distance.

The prime-13 jets are normalized at the actual equal-weight point.
The implicit derivative \(-72\), the log/square identities, all three
Hankel determinants, and their negative quadratic witnesses check.
Positive semidefiniteness of the differentiated global Pick kernel
is a necessary condition for a global upper-half-plane Pick
extension. It is not a condition for ordinary right-half-plane
holomorphy. The negative-normalized-spectrum test uses \(-x\)
instead of \(-1-x\), which changes only the irrelevant constant.
The derivative signs and determinant signs exclude both Pick
directions for each of the stated observables; they do not
exclude arbitrary changes of parameter or other observables.

Finally, the phase lemma correctly anchors the positive-real
function at the real hot value \(m_q(T)\). Disk Cayley estimates
and a finite chain inside the common domain bound the marked
logarithm on a fixed compact subdomain by
\(C(1+\sup_D|\operatorname{Im}m_q|)\). Combining this with the
slit two-constants principle gives exactly the square exponent
\(\omega/[2(1-\omega)]\). The imaginary part is the unwrapped
analytic logarithm, not a principal argument. A fixed-sector or
positive-real marked spectrum would bound this phase after
normalization at the positive real anchor, so cannot provide such
a common square-family continuation. The conclusion remains a
disjunction between failed extension and large phase. The common
cold domain and subpolynomial phase bound through primes are
unproved.
