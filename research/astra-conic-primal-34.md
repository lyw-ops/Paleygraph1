# A marked-preserving clipped reflection for the conic primal

Round 34, 2026-11-18. ETH Problem 26, **ordinary theta**.

**The cold prime-uniform construction is not proved.** The new result is
an explicit quantitative positive-repair lemma on the actual Paley spaces.
It preserves **both means and both marked values**, incurs a rigorously
bounded fidelity cost, and applies even when the input rows have negative
entries. For the shallow-defect hypotheses (13), its squared repair
distance is $O(BC\kappa/\sqrt n)$; it is $o(\kappa)$ when $BC=o(\sqrt n)$.
The clipped gap must still be controlled separately. This is a construction lemma,
not another equivalence with UI, and does not use the unknown source.

There is also a concrete signed-scatter mechanism that is stronger than
its absolute coherence estimate. A source-free, 40-step proposal at prime
order $1000033$ has negative entries in both rows; one clipped reflection
produces a rigorously certified conic feasible pair at

\[
 \tau=1/20,\qquad\kappa=1/1000,\qquad
 d_n(\kappa)/\kappa<0.987402.
\]

At depth 48 the bound is $<0.212819$. These are **finite, non-Newton**
certificates demonstrating the repair, not bounds on a prime limsup. The
matching square-order trial is rigorously negative after the repair.
No claim about HR, marked comparison, or ETH26 follows from these records.

## 1. What is retained, and what is new

We use the full conventions and statements (7)--(22) of
[prime UI 33](parallel-prime-ui-33.md), including the mark in

\[
 m_0=n/W,\quad m_i=\tau/W\ (i\ne0),\quad
 W=1+(n-1)\tau/n,\quad
 D(p,q)=\frac1n\sum_i(\sqrt{m_i}-\sqrt{p_iq_i})^2.
 \tag{1}
\]

The goal remains positive $p\in1+V_+$, $q\in1+V_-$, with means one
and $p,q\ge\kappa$, whose gap is $o(\kappa)$ **field first**. Each
finite field having a zero-gap interval at very small $\kappa$ is
irrelevant to that order of limits.

The root-pinned projection $L$ below is already in
[anchored repair 20](anchored-repair-20.md). The new use here is a
**mean-zero** clipped reflection, a reserve bound proving its positivity,
an exact reflection-energy identity, and a bulk-only Hellinger bound for
the **two-row conic objective**. Unlike adding positive repair rows and
normalizing, this construction changes neither mean nor mark. No claim
of discovering the pinned projection itself is intended.

The fixed scalar obstruction in [scalar seed 25](scalar-seed-25.md),
the Fejer perturbations in [broad source 28](astra-broad-source-28.md), and
the exact scope of [joint law 32](joint-law-32.md) are retained. In
particular, rank-three equidistribution does not identify the law of the
later clipped fields used here.

## 2. An actual-Paley floor-repair lemma

Let the field order be $N=2n+1\equiv1\pmod4$. On the real even cyclic
space, use the actual Paley multiplier $K$, so

\[
 K^T=K,\quad K^2=I-J,\quad K1=0,\quad
 K_{ii}=-1/n,\quad |K_{ij}|\le\sqrt N/n.
 \tag{2}
\]

Here $J=11^T/n$. The diagonal identity is the exact character sum
$\sum_{t\in Q}\chi(1-t)=-1$; the entry bound is the usual normalized
Jacobi-sum bound, in the same normalization as the cited earlier notes.
For $\sigma=\pm1$, set

\[
 P_\sigma=(I-J+\sigma K)/2,\quad
 a_\sigma=(n-1-\sigma)/(2n),\quad
 \ell_\sigma=P_\sigma e_0,\quad
 L_\sigma=P_\sigma-\ell_\sigma\ell_\sigma^T/a_\sigma.
 \tag{3}
\]

Assume $a_\sigma>0$. Thus $L_\sigma$ is an orthogonal projection,

\[
 \operatorname{im}L_\sigma=V_\sigma\cap e_0^\perp,
 \quad L_\sigma1=L_\sigma e_0=0.
\]

Take **any** real even row $z\in1+V_\sigma$, with $z_0\ge\kappa>0$.
No positivity elsewhere is assumed. Define

\[
 d_0=0,\quad d_i=(2\kappa-z_i)_+\ (i\ne0),\quad
 Z=z+d,\quad \widehat z=z+2L_\sigma d.
 \tag{4}
\]

The clipped row $Z$ is positive but generally not feasible. The repaired
row $\widehat z$ has exact mean one, the correct sector, and
$\widehat z_0=z_0$.

Put

\[
 b_n=\frac{1+\sqrt{2n+1}}{2n},\qquad
 \Gamma_{n,\sigma}=2b_n+\frac{2b_n^2}{a_\sigma}.
 \tag{5}
\]

**Repair theorem.** The following statements hold without a source or a
stationary equation:

\[
 \|\widehat z-Z\|_2=\|d\|_2,\qquad
   (\widehat z-Z)_0=0.                                      \tag{6}
\]
\[
 \max_{i\ne0}|\widehat z_i-Z_i|
       \le\Gamma_{n,\sigma}\|d\|_1.                          \tag{7}
\]

Consequently

\[
 \boxed{\quad
  \Gamma_{n,\sigma}\|d\|_1\le\kappa
       \quad\Longrightarrow\quad \widehat z\ge\kappa.
 \quad}                                                     \tag{8}
\]

For $n\ge16$, uniformly in the sign,

\[
 \Gamma_{n,\sigma}\le3/\sqrt n.
 \tag{9}
\]

Thus a simple sufficient condition is
$\|d\|_1\le\kappa\sqrt n/3$. This controls the total **unnormalized**
deficit; using its empirical mean without the factor $n$ would be wrong.

**Proof.** Write $R_\sigma=2L_\sigma-I$. It is an orthogonal reflection,
so $\widehat z-Z=R_\sigma d$ gives (6). Since $d_0=0$, its marked
coordinate is zero. For off-mark indices $i\ne j$,

\[
 |(R_\sigma)_{ij}|\le2b_n+2b_n^2/a_\sigma.
\]

For $i=j\ne0$,

\[
 |(R_\sigma)_{ii}|=(1+\sigma)/n+2\ell_{\sigma,i}^2/a_\sigma
                \le2b_n+2b_n^2/a_\sigma,
\]

where $|\ell_{\sigma,i}|\le b_n$ and $2/n\le2b_n$. This proves
(7). Off the mark $Z_i\ge2\kappa$; (8) follows, with the mark handled
separately. For $n\ge16$, $a_\sigma\ge7/16$ and
$1+\sqrt{2n+1}\le7\sqrt n/4$. Hence

\[
 \Gamma_{n,\sigma}\le\frac7{4\sqrt n}+\frac7{2n}
                  \le\frac{21}{8\sqrt n}<\frac3{\sqrt n}.
\]

This proves (9). All corrections preserve evenness. ∎

## 3. Quantitative fidelity cost, with no marked amplification

Apply (4) to two input rows $z_+\in1+V_+$, $z_-\in1+V_-$, with
both marks at least $\kappa$. Let the clipped rows be $Z_+,Z_-$ and
the repaired rows be $p,q$. Suppose (8) holds on both sides, or prove

\[
 p,q\ge\kappa                                                  \tag{10}
\]

directly. Set

\[
 \begin{split}
 D_{\rm clip}&=\frac1n\sum_i
          (\sqrt{m_i}-\sqrt{Z_{+,i}Z_{-,i}})^2,\\
 B&=\max_{i\ne0}\max(Z_{+,i},Z_{-,i},p_i,q_i),\\
 E_{\rm rep}&=\frac{\sqrt B\,(\|d_+\|_2+\|d_-\|_2)}
                     {(1+\sqrt2)\sqrt{\kappa n}}.
 \end{split}                                                   \tag{11}
\]

Then the explicit feasible pair obeys

\[
 \boxed{\qquad D(p,q)\le
                  \big(\sqrt{D_{\rm clip}}+E_{\rm rep}\big)^2.
 \qquad}                                                       \tag{12}
\]

The clipped objective in (11) is the sum of squares as written. It must
**not** be replaced by $2-2E\sqrt{mZ_+Z_-}$: the clipped rows have lost
their means and sector orthogonality.

**Proof.** On the bulk, by factoring the difference of square roots,

\[
 \begin{split}
 |\sqrt{pq}-\sqrt{Z_+Z_-}|
 &\le\sqrt q\,|\sqrt p-\sqrt{Z_+}|
          +\sqrt{Z_+}\,|\sqrt q-\sqrt{Z_-}|\\
 &\le\frac{\sqrt B}{(1+\sqrt2)\sqrt\kappa}
          (|p-Z_+|+|q-Z_-|).
 \end{split}
\]

Use (6) and the triangle inequality in normalized $\ell_2$. The marked
entry of this difference is **exactly zero**, even though the marks can
be of order $\sqrt n$. A second triangle inequality with $\sqrt m$
proves (12). ∎

Here is a useful explicit rate. If, on each side,

\[
 \|d_\sigma\|_1\le\kappa\sqrt n/3,\qquad
 \|d_\sigma\|_\infty\le C\kappa,\qquad n\ge16,
 \tag{13}
\]

then

\[
 \boxed{\quad
 \sqrt{D(p,q)}\le\sqrt{D_{\rm clip}}+
 \frac{2}{1+\sqrt2}\sqrt{\frac{BC\kappa}{3}}\,n^{-1/4}.
 \quad}                                                       \tag{14}
\]

In particular the squared repair distance is at most

\[
 \frac{4BC}{3(1+\sqrt2)^2}\,\frac\kappa{\sqrt n}.
 \tag{15}
\]

This is an actual-Paley quantitative lemma valid at **every** positive
$\tau$: the weight enters only the fully computable clipped gap. A
deficit supported on at most $\sqrt n/(3C)$ coordinates and of height
at most $C\kappa$ automatically satisfies (13). A bound $B=o(\sqrt n)$
also suffices for the repair distance divided by $\sqrt\kappa$ to
vanish at fixed $\kappa$. This is useful even with a growing bulk cap.

The result does not say that these favorable inputs exist on all primes.
It does remove a specific completion loss: for inputs in (13), one need
not pay a global constant shift or disturb either large mark. If one
eventually proves a prime estimate for $D_{\rm clip}$, (14) transfers it
to a genuinely feasible conic pair. Neither that input estimate nor
entry into (13) is established here.

## 4. The signed arithmetic mechanism and its limitation

The reflected error has the exact form

\[
 R_\sigma d=\sigma Kd-Ed\,1
                 -\frac{2\ell_\sigma}{a_\sigma}
                         \langle\ell_\sigma,d\rangle.
 \tag{16}
\]

This follows from $2P_\sigma-I=\sigma K-J$. In particular the diagonal
identity term cancels. Formula (16) makes it possible to test **signed
scatter of a known clipped proposal**, instead of a stationary weighted
tail. Define the computable one-sided spill

\[
 S_\sigma(d)=\max_{i\ne0}(-(R_\sigma d)_i)_+.
 \tag{17}
\]

The sufficient condition $S_\sigma(d)\le\kappa$ implies positivity
just as in (8), and can be much better than
$\Gamma_{n,\sigma}\|d\|_1$. Alternatively, verify every repaired
coordinate directly; the proof of (12) only needs (10).

This mechanism is falsifiable on a specified source-free trajectory.
The tested trajectory is

\[
 v^{(0)}=0,\qquad
 v^{(t+1)}=K\sqrt{(v^{(t)})^2+4w},\quad
 w_0=1,\ w_i=\tau/n.
 \tag{18}
\]

At the chosen depth form the positive reciprocal raw numbers

\[
 A=(\sqrt{v^2+4w}+v)/2,\quad
 B=(\sqrt{v^2+4w}-v)/2,
\]

and then take the exact affine-sector proposals

\[
 z_+=1+P_+A/(EA),\qquad z_-=1+P_-B/(EB).
 \tag{19}
\]

Apply (4) once. This is a fully specified construction, not a search over
an unspecified finite family. The script never calls a stationary solver,
Newton, SLSQP, or the previous conic driver. Rounding (19) to rational
Fourier coefficients is explicitly part of the certified construction.

The positive scatter evidence below does **not** establish a prime-uniform
bound on (17), on the required depth, or on $D_{\rm clip}$. In fact, a
fixed-depth argument based only on (8) has a precise vulnerability. If
the normalized deficit mass $E d$ tends to any positive constant at
fixed depth and fixed $\kappa$, then

\[
 \Gamma_{n,\sigma}\|d\|_1\asymp\sqrt n\,Ed\longrightarrow\infty.
 \tag{20}
\]

So coherence alone cannot close a fixed-depth proposal with a nonzero
limiting defect density. Growing depth or a new **signed**, prime-specific
estimate is necessary in that case. The common rank-three law cannot be
substituted for the law of $d$ in (16) at the tested depths.

## 5. Strict finite certificates and negative controls

The inputs store exact integer Fourier coefficients divided by $2^{90}$,
with exact DC coefficient one, exact evenness, and exact forbidden zeros.
The recorded Picard depth is proposal provenance: the trajectory was
evaluated in floating point, not enclosed step by step. The rigorous
construction and every certificate start from the saved exact Fourier
input; no accuracy claim about that trajectory is needed.
Arb determines every clipping branch by a strict interval comparison;
it never guesses whether a coordinate is active. It then applies (3)--(4),
checks every output coordinate, the mark and mean, the reflection-energy
identity, and a second Fourier-support test. The algebraic projection
identities, not interval containment alone, prove the exact constraints.

All entries below have $\tau=1/20$, $\kappa=1/1000$. Values are
rounded **outward** from the replay; lower minima are rounded downward.

| actual field | depth | clipped counts (+,-) | repaired minimum (+,-), lower bounds | $D/\kappa$, upper bound |
|---:|---:|---:|---:|---:|
| 9413 | 40 | 6,18 | .00200472, .00173874 | .735334 |
| 9413 | 44 | 2,0 | .00197835, .00257718 | .313868 |
| 9413 | 48 | 0,0 | .00487626, .00426614 | .131884 |
| 1000033 | 40 | 1886,1942 | .00135283, .00129103 | .987402 |
| 1000033 | 48 | 26,14 | .00198854, .00198792 | .212819 |

For the million-order prime at depth 40, the two **absolute** coherence
spill bounds divided by $\kappa$ are approximately 8.6911 and 9.8186,
so (8) does not certify this case. Nevertheless the **signed** spills
are rigorously less than .000846917 and .000999377, respectively, both
below $\kappa$. At depth 48 the absolute bounds already suffice:
they are less than .0000310260 and .0000550744. The raw minus row still
has a negative entry below -.00274275 at this depth, so the repair is
doing actual positivity work.

The bound (12) at the million-order prime is less than .002066648 at
depth 40, and .000233279 at depth 48. Direct evaluation of $D$ gives
the tighter values in the table. These are valid trial upper bounds,
not optimal conic brackets and not exact-source maximum bounds.

For the square control $N=389^2=151321$, depth 48 has 194 active minus
coordinates. The same formula produces a coordinate rigorously less than

\[
 -.37428998128<0.
 \tag{21}
\]

This is saved as `arb_repair_rejected`, together with the exact input and
the index and upper enclosure of the failing coordinate. It refutes this
**trial** on that field, not conic feasibility. It is not hidden by a
subsequent mean shift or normalization.

The fixed $\kappa=.001$ floating sweep at depth 40 exhibits worsening
absolute coherence bounds as the primes grow, despite successful signed
repair. At depth 48 the generic bound succeeds at all three tested
primes. Neither observation implies what happens beyond the tested
orders. At depth 128 the proposals have much smaller gaps, but those
finite tiny gaps are not used as evidence for a uniform construction.

There is also a genuine limitation of using a reserve of $2\kappa$:
at $\kappa=.005$ some late prime proposals already satisfy the desired
floor, but (4) still modifies entries below .01 and increases their gap.
The diagnostic records retain this effect. A practical implementation can
leave an already certified feasible row alone; no claim is made that the
fixed reserve rule minimizes the conic objective.

## 6. Routes tried, scope, and replay

* **Global constant repair:** kept as a diagnostic comparator. At early
  million-prime depth 40 it has $D/\kappa\approx4.809$, whereas the
  marked-preserving reflection has $<.987402$. The comparison is
  finite and floating on the constant-repair side; it proves no
  dimension-uniform superiority.
* **A fixed scalar or fixed rank-three family:** not promoted to a
  positive construction. Scalar seed 25 gives a genuine limiting negative
  residual, and joint law 32 has common prime/square scope only for its
  stated fields. Neither supplies the later signed estimate (17).
* **Repeated clipping without a convergence estimate:** not used to
  assert uniform convergence. The reflection is an isometry on the
  clipped error, so a positive reserve or a signed arithmetic estimate
  is essential. Positivity repair alone does not minimize fidelity.
* **A marked-product-only estimate:** the elementary two-bin lower bound
  $D\ge(\sqrt{1/W}-\sqrt{p_0q_0/n})^2+
  (\sqrt{1-1/W}-\sqrt{1-p_0q_0/n})^2$ applies to any feasible pair.
  In the explored prime proposals it is far below the actual gap; it
  does not explain the missing bulk estimate. It was not pursued as a
  positive construction.
* **Tiny stationary/Newton residual:** absent from the construction and
  the replay. Even the source-free finite certificates do not yield a
  field-first theorem.

The substantive proved output is (6)--(15), with the signed formula (16).
It applies on actual Paley fields at every fixed positive $\tau$, and
quantifies a completion step that preserves all conic affine constraints.
What is still missing is a prime-uniform supply of proposals for which
the clipped gap is superlinear in $\kappa$ and the repair hypotheses
or signed spill bounds hold. HR and the marked arithmetic finish remain
additional, separate open tasks.

```sh
export OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

# Independent exact rational matrix audit at the actual field F_13.
.venv/bin/python -B research/astra-conic-primal-34.py --exact

# Source-free diagnostics, including both cold floors and square controls.
.venv/bin/python -B research/astra-conic-primal-34.py \
  --primes 9413 153649 --square-roots 97 \
  --steps 32 40 44 48 64 96 128 --kappa 1/1000 1/200
.venv/bin/python -B research/astra-conic-primal-34.py \
  --primes 1000033 --square-roots 389 \
  --steps 32 40 44 48 56 64 96 128 --kappa 1/1000 1/200

# Generate rational inputs and prove positive primal trials.
.venv/bin/python -B research/astra-conic-primal-34.py \
  --primes 1000033 --steps 40 48 --save

# Save and rigorously verify the square trial's failure.
.venv/bin/python -B research/astra-conic-primal-34.py \
  --square-roots 389 --steps 48 --save-rejected

# Pure certificate replay; no trajectory or optimization is run.
.venv/bin/python -B research/astra-conic-primal-34.py --precision 224 \
  --replay research/astra-conic-primal-34-q1000033-t40-tau1_20-k1_1000-input.json.gz
```

The combined 224-bit replay contains five positive primal certificates
and one square rejection. The exact audit contains two rational matrix
records, one per sign. There are 74 separate floating diagnostic rows.
The replayable table/hash audit is
`python -B research/astra-conic-primal-34.py --check-records`; its saved
output is [checks.json](astra-conic-primal-34-checks.json), and its primary
interval input is [replay224.jsonl](astra-conic-primal-34-replay224.jsonl).
These are ordinary mathematical proofs and Arb
certificates, not Lean kernel verification. Every file written in this
round has the `research/astra-conic-primal-34` prefix. No README, ledger,
other-prefix artifact, commit, push, or external message is part of it.
