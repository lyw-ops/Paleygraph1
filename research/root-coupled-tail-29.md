# Keeping the marked root inside the signed-tail certificate

Round 29, 2026-11-18. This is a finite ordinary-theta certificate, not a proof
of the prime asymptotic. It retains a dependency discarded in
[the previous certificate](source-tail-28.md): the stationary bulk cap and
the marked hyperbolic error involve the same unknown root. The resulting
necessary conditions are two explicit quadratic inequalities. No stationary
solve or optimizer is trusted.

## 1. The two quadratic conditions

Use the notation and proved stationary cap of the previous note:

\[
h=\tau/n,\quad W=1+(n-1)h,\quad
a=2\sqrt h,\quad \mathcal B=2\sqrt{nW}-na,
\quad C=(1+\sqrt q)\sqrt{W/n}.
\]

For a rational trial \(z\), put

\[
\phi=\Phi(z),\quad b=(I-J)\phi-Kz,\quad
E=2\sqrt W\frac{\sum_i\phi_i}{\sqrt n}-4W.
\]

Choose any signed threshold \(t\), and define

\[
U=\sum_{i\ne0}(b_i-t)_+,\quad m=b_0-t,
\quad T=t\mathcal B-a(m+U),\quad R=4+E+T.
\]

Let \(x=A_0=e^{\gamma_0}\) be the unknown marked coordinate of the actual
positive stationary pair. Its opposite root is \(B_0=x^{-1}\), and
\(C^{-1}\le x\le C\). For \(x\ge1\) the bulk cap is \(x+h/x\); for
\(x\le1\) it is \(x^{-1}+hx\). These are the two branches of the exact
root-dependent cap, not independent bounds on the two roots.

The exact full discrepancy dominates its marked summand:

\[
\Delta\ge (x+x^{-1})\phi_0-(x-x^{-1})z_0-4.
\]

The signed mass/cap bound gives, on the positive branch,

\[
\Delta\le E+m(x+x^{-1})+U(x+h/x)+T.
\]

Multiplication by \(x>0\) therefore proves the following necessary
conditions for the **same actual root**:

\[
\boxed{
\begin{array}{ll}
A_+x^2-Rx+B_+\le0,&1\le x\le C,\\
A_-x^2-Rx+B_-\le0,&C^{-1}\le x\le1,
\end{array}}
\tag{1}
\]

where

\[
\begin{aligned}
A_+&=\phi_0-z_0-m-U,&B_+&=\phi_0+z_0-m-hU,\\
A_-&=\phi_0-z_0-m-hU,&B_-&=\phi_0+z_0-m-U.
\end{aligned}
\]

Enclose the surviving subsets of the two branches by
\([x_{\min},x_{\max}]\). The ordinary-theta bracket is then

\[
\boxed{\qquad
\frac{x_{\min}}{\sqrt W}\le
\frac{\vartheta(\overline H)}{\sqrt n}
\le x_{\max}\sqrt W.
\qquad} \tag{2}
\]

The previous method first took a maximum over the unknown root to bound
\(\Delta\), then bounded its marked summand. Here (1) retains that root
throughout. This can improve finite enclosures. No claim that it provides
a strictly weaker asymptotic Paley hypothesis is made.

## 2. Safe rounding and branch enclosure

The [checker](root-coupled-tail-29.py) reconstructs each rational trial,
\(\Phi(z)\), and \(Kz\) in 160-bit Arb arithmetic. As in the previous
checker, each cost is rounded upward to \(10^{-14}\mathbb Z\). Write the
resulting increments of the root cost and excess as \(\delta b\ge0\) and
\(\delta U\ge0\). Their changes to the positive-branch polynomial in (1)
are respectively

\[
-\delta b(x^2-2\sqrt h\,x+1),\qquad
-\delta U(x-\sqrt h)^2.
\]

On the negative branch the latter is
\(-\delta U(\sqrt h\,x-1)^2\); the root-cost expression is unchanged.
All are nonpositive since \(h<1\). Thus the rounded polynomial remains
a necessary inequality. This is a joint rounding argument: the rounded
\(R\) need not itself be an upper bound for its unrounded counterpart.

For a branch with certified positive leading coefficient, the feasible set
lies between its quadratic roots. A certified negative discriminant excludes
the branch. Otherwise its outward upper bound supplies a conservative
square root, and outward division bounds both roots. The result is
intersected with its field interval and half-line. If positivity of the
leading coefficient cannot be certified, the checker keeps the whole branch;
that fallback is safe and makes no sharpness assertion.

The rational threshold is inherited from each saved input. The present
comparison does not optimize a new threshold and asserts no global optimizer
property. Multiple valid thresholds could be intersected, but that is not
needed for the reported records.

## 3. Finite comparisons and limits of the improvement

The [20 certified records](root-coupled-tail-29-certified.jsonl) reuse exactly
the rational trials accepted by the previous checker, including the completed
million-order small-floor proposal. The latter has also been independently
replayed by the previous optimizer-free checker. Its floating-point Newton
generation is not evidence about an exact Picard prefix and is not an
assumption of either certificate.

Selected decimal endpoints below are rounded outward:

| Field, floor, trial | Previous interval | Root-dependent interval |
|---|---|---|
| \(61,1/20,T=32\) | \([0.75624,1.06888]\) | \([0.76697,1.04225]\) |
| \(9413,1/10000,\text{Newton trial}\) | \([1.0003790,1.0004824]\) | \([1.00037909,1.00048227]\) |
| \(1000033,1/10000,\text{Newton trial}\) | \([1.0007690,1.0008822]\) | \([1.00076969,1.00088152]\) |

All 20 new intervals are contained in the previously reported raw intervals.
Some early improvements come entirely from clipping by the already-known
field/root cap. A fair comparison also clips the old interval by
\([1/(C\sqrt W),C\sqrt W]\). Relative to that baseline, the new width is
about 88.1% at \(p=61,T=32\), and about 98.8% at the million-order small-floor
trial. Early square intervals still permit the exact square theta value.
The [comparison record](root-coupled-tail-29-comparison.jsonl) separates this
clipping effect from the quadratic improvement.
The [acceptance record](root-coupled-tail-29-acceptance.json) distinguishes
the interval certificates, exact controls, floating diagnostics and pending
cross-side research. Its recorded process from round 28 has completed.

In the natural late-depth regime \(z_0,m\to0\), a nonvanishing \(U\) causes
a linear cusp in the root-dependent upper bound near \(\gamma_0=0\).
Consequently the new finite algebra does not itself remove the need to
control the actual positive tail. The
[independent audit](parallel-root-audit-29.md) records the precise scalar
criterion and this limitation. A prime-uniform tail estimate and compatible
marked cancellation remain unproved.

Replay from the repository root:

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B \
  research/root-coupled-tail-29.py \
  research/source-tail-28-q1000033-tau1_10000-t0-input.json
```
