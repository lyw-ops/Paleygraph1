# A sublinear critical-score target for ordinary theta

The short-window critical-slice score need only be \(o(T)\) to prove the ordinary theta limit. This weaker target uses an exact finite inequality from a **supercritical** optimum mixed down to the critical mass. It preserves the distinguished root and works for both signs. The sharp \(T^{1/3}\) inequality of [round 42](astra-witness-resume-42.md) is still relevant to excluding the entire slice at a fixed floor, or to arguments using only one critical witness.

The accompanying Arb checker gives two-sided brackets on the exact score when the slice exists, certifies emptiness by the opposite cone, and tests a dual restricted to early orbit columns. Its prime and square results are finite controls.

## Converting a score upper bound into a theta upper bound

Let \(n=(q-1)/2\), \(W=1+(1-1/n)\tau\), \(a=\sqrt W\), and \(a_0=n^{-1/2}\). Use the actual zero-start undamped Picard path, \(Y_T=\sqrt n v_T\), and the notation of [round 41](astra-repair-41.md). Let

\[
A_\sigma=\max_{\mu\ge0,\ \mu\in\mathbb R\mathbf1+V_\sigma,\ \sum_i\mu_i=1}\sqrt n\,\mu_0
\]

be the ordinary theta optimum divided by \(\sqrt n\) for sign \(\sigma\). The critical slice imposes \(\sqrt n\,\mu_0=a\), and its upper score is

\[
S_{\sigma,T}=\max_{\mu\text{ in the critical slice}}\sigma\langle\mu,Y_T\rangle .
\]

The slice is nonempty exactly when \(A_\sigma\ge a\), by mixing an optimum with uniform probability. Define

\[
B_T=\sum_{j<T}(2-b_j),\quad
F_T=2\sum_{j<T}(a-g_j)\ge0,\quad
C=a-a_0>0.
\]

Here \(b_j=\sqrt{4+v_j(0)^2}-\sqrt{4\tau/n+v_j(0)^2}\) is the true exceptional coefficient. For any feasible probability \(\nu\) of normalized root \(\alpha=\sqrt n\,\nu_0\), the exact positive-floor identity is

\[
\sigma\langle\nu,Y_T\rangle+\alpha B_T
=2(\alpha-a)T+F_T+H_T(\nu),\qquad H_T(\nu)\ge0.                 \tag{1}
\]

Choose a maximizing \(\nu\) for \(A_\sigma\). Write \(\delta=A_\sigma-a\ge0\), and mix \(\nu\) with uniform probability using weight \(\lambda=C/(C+\delta)\) on \(\nu\). The mixture is critical and its signed score is \(\lambda\sigma\langle\nu,Y_T\rangle\) since \(Y_T\) has mean zero. Also \(a-\lambda A_\sigma=(1-\lambda)a_0\ge0\) and \(B_T\ge0\). Thus (1) gives

\[
S_{\sigma,T}+a B_T\ \ge\ \frac{C}{C+\delta}\big(2\delta T+F_T\big).          \tag{2}
\]

This inequality is at the exact critical slice, including when the maximizing root is exactly critical and when the slice contains a strict feasible probability. In particular, if a certified upper score is \(U\), set \(D=U+aB_T\). Whenever \(D<2CT\),

\[
\boxed{\qquad  A_\sigma\le a+C\,\frac{D-F_T}{2CT-D}.\qquad}                 \tag{3}
\]

An empty slice gives \(A_\sigma<a\) directly. A nonempty one always has \(D\ge F_T\) by (1) at critical mass.

## Sufficient prime estimate and a square obstruction at the same mass

In the [round-38 marked window](vanishing-floor-38.md), \(B_T/T=o(1)\) uniformly over \(0<\tau\le1\). Indeed \(0\le 2-b_j\le |v_j(0)|+2\sqrt{\tau/n}\), with the stated marked bound. For each fixed \(\tau>0\), suppose along the primes with a nonempty slice we can choose an increasing depth in the window and show \(S_{\sigma,T}\le o(T)\) for both signs. Then (3) gives

\[
\limsup_{p\to\infty} A_\sigma\le\sqrt{1+\tau}.
\]

It suffices to establish this for a sequence of fixed positive floors tending to zero. Taking the floor limit gives \(\limsup A_\sigma\le1\) for both signs, and the [ordinary complementary product](fourier.md) yields \(A_\sigma\to1\). The same argument works with depth tending to infinity **after** taking the prime limsup at each fixed depth, since fixed-depth marked cancellation suffices for \(B_T/T\to0\) in that order. This is weaker than requiring \(S_{\sigma,T}=o(T^{1/3})\). Conversely, the conjecture would make the slices eventually empty at every fixed positive \(\tau\). A computation observing emptiness at finitely many primes leaves the uniform estimate open.

At prime squares and fixed \(0<\tau<1\), the exact subfield optimum has \(A_+\to\sqrt2\). Equation (2) therefore gives

\[
\liminf_{q\to\infty,\ q\ {\rm square}}\frac{S_{+,T}}{T}
\ \ge\ 2\sqrt{1+\tau}\left(1-\sqrt{(1+\tau)/2}\right)>0                     \tag{4}
\]

through the marked window at increasing depths. In particular a generic bound at that exact critical mass through all field orders cannot prove the proposed estimate. At fixed finite field a bounded score as \(T\to\infty\) does not contradict (2) or (4), since the sublinear marked control is absent at that limit and one must retain \(aB_T\).

## Verifying the true slice LP and a restricted dual

The actual orbit is even under cyclic inversion. Symmetrizing any candidate preserves mass, root, feasibility and the objective. The even mean-one row \(n\mu\) is therefore \(1+\sum_{j:s_j=\sigma} c_j\cos(2\pi i j/n)\), using a single representative of each nontrivial inverse pair. Setting \(\sum_j c_j=\sqrt{nW}-1\) enforces the exact critical root. The score is linear in the coefficients and nonnegativity is tested at every coordinate.

For an upper score, one may use the exact certified inequality

\[
u\mathbf1+v e_0+w\ge \sigma Y_T,\qquad w\in V_{-\sigma},
\]

which gives \(S_{\sigma,T}\le u+v\sqrt{W/n}\). The unrestricted dual takes the full opposite cosine basis. The simpler dual projects \(e_0,Y_1,\ldots,Y_4,Y_T\) to \(V_{-\sigma}\) and uses only their span. The latter columns come from the true orbit. In both versions the numerical LP only proposes coefficients. After rational rounding, the checker adds a provable constant to cover every inequality. For lower bounds it rounds the primal coefficients, repairs the mark by a single exact algebraic coefficient, and mixes with a strict interior row already certified at that mark. Opposite positive reference rows certify empty slices by \(\sqrt n/P_{-\sigma,0}<a\). At the exact saturated square floors it uses the subfield row itself as the primal lower test. All evaluations, including \(B_T,F_T\) of the actual orbit, use outward Arb arithmetic.

Selected depth-64 controls from the [records](critical-shell-44-checks.jsonl) are rounded below for readability. The unrestricted score width is less than \(10^{-6}\) in every nonempty record.

| Order | Floor | Sign | Upper score | Early-column dual bound | Mark correction \(aB_T\) |
|---|---:|---:|---:|---:|---:|
| 101 | \(1/4\) | minus | 2.11465 | 2.17597 | 16.33614 |
| 101 | \(1/20\) | minus | 2.14171 | 2.25618 | 14.24324 |
| 49 | \(1/4\) | plus | 3.56714 | 3.56714 | 21.57777 |
| 121 | \(1/4\) | plus | 5.94673 | 5.96722 | 21.50422 |
| 173 | \(1/1000\) | plus | 2.51779 | 3.08504 | 1.25226 |
| 401 | \(1/100\) | minus | 2.61168 | 3.84727 | 2.13060 |

There are 32 nonempty score certificates and 14 empty-slice certificates. At \(q=49,\tau=12/23\) and \(q=121,\tau=40/59\), the exact square plus optimum itself is critical. These controls check the boundary case without a strictly positive point in the slice.

For \(p=101,\tau=1/4,T=7\), the exact maximum is approximately \(2.088381\). The exact positive example in [round 43](astra-rooted-43.md) establishes unique exceptionality for its own translations and a one-step-subtracted score. It need not attain this LP maximum. There is no inference about the arithmetic window from these finite depths. At the small square controls the limited dual even approaches the full LP, so low-dimensional dual fit by itself provides no prime separation. At the finite samples the dilution upper bound in (3) is weaker than the direct complementary root upper due in part to \(aB_T\). This is why a growing-depth comparison must first establish its marked error estimate.

The [checker](critical-shell-44-check.py) reproduces the interval records with the repository virtual environment. The primary open requirement is still to produce a genuinely prime-uniform sublinear dual bound, or another argument resolving the ordinary theta limit.
