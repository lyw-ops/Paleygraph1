# A paired positive trial for the cold stationary mark

The scalar Cauchy step in the [round-48 static trial](static-trial-48.md) can be strengthened by retaining a second feasible row in the complementary sector. The resulting quadratic bound is exact when the trial pair is the physical pair. It also gives constructive finite certificates without a stationary solve at the tested cold floor. At prime 173 both sides certify \(|m_{173}(1/2)|<0.017\), overcoming the round-48 static deficit. The minus certificate uses an opposite row proposed at floor 1. The fixed candidate from floor 28 alone has a rigorously certified score deficit. At prime 97 both signs can use references proposed at floor 28. No prime asymptotic existence claim for these trial rows is proved here.

## Exact paired bound

Let \(a>0\), \(c=1-1/n\), \(W=1+ca\), \(E=n^{-1}\sum_i\), and \(E_b=n^{-1}\sum_{i\ne0}\). For sign \(\sigma\) write \(P=P_\sigma(a)\) for its actual positive mean-one stationary row and \(x=P_0/\sqrt n\). Take nonnegative mean-one rows \(\ell\in U_\sigma\) and \(Q\in U_{-\sigma}\), and put

\[
 f=\ell_0/\sqrt n,\qquad g=Q_0/\sqrt n,\qquad H=E_b\sqrt{\ell Q}.
\]

Assume \(Q\) has positive bulk mass. Complementary pairing gives \(1-xg=E_b(PQ)>0\). The first-order equation on \(\ell\) and Cauchy–Schwarz yield

\[
 W=\frac f x+a E_b(\ell/P)
 \ \ge\ \frac f x+\frac{a H^2}{1-gx}.
 \tag{1}
\]

In comparison with the single-row estimate, the useful numerator is a **bulk overlap of two feasible rows**, and the denominator is known as a function of the single unknown mark by exact sector orthogonality. Set \(V=cE_b(\ell Q)-H^2=c(1-fg)-H^2\ge0\). Multiplying (1) gives the equivalent quadratic bound

\[
 [Wg x-1][x-f]\le aVx,\qquad
 Wg x^2-(1+Wfg+aV)x+f\le0 .
 \tag{2}
\]

When \(g>0\) this is a two-sided closed interval with discriminant nonnegative. The physical trial \((P,P_{-\sigma}(a))\) gives \(f=x\), \(g=1/(Wx)\) and \(V=0\), so the roots coincide at the actual mark. Thus the bound's worst-case loss can come from the selected trials even when the physical value lies inside a target tolerance.

In logarithmic form, if both trial marks are positive, put \(L=\log(\sqrt W f)\), \(R=-\log(\sqrt W g)\), \(M=\sigma m_q(a)=\log(\sqrt W x)\). Then (2) becomes

\[
 \cosh\big(M-(L+R)/2\big)
 \le \cosh((L-R)/2)+\tfrac12 aV e^{(R-L)/2}.
 \tag{3}
\]

This separates bulk dispersion from mismatch of the two trial marks. For example if \(f\ge x_*\), \(Wg x_*\le1\) and \(x\le(1-\delta)x_*\), then (2) forces \(aV\ge \delta^2/(1-\delta)\). It follows by bounding \(1-Wg x\ge\delta\) and \((f-x)/x\ge\delta/(1-\delta)\). Thus a vanishing bulk dispersion on trials with the indicated one-sided marks would give a prime lower bound \(x\ge x_*-o(1)\), without fixing their product to \(1/W\). Existence of such trials stays open.

## A convex test with a fixed opposite row

Fix \(x_*>0\) and an opposite \(Q\) with \(x_*g<1\). For any same-side trial it suffices that

\[
 f\ge Wg x_*^2,\qquad
 \frac f{x_*}+\frac{aH^2}{1-gx_*}\ge W .
 \tag{4}
\]

Indeed the quadratic in (2) is nonpositive at \(x\) and nonnegative at \(x_*\). Its upper zero is at least \(x_*\) because the product of the zeros is \(f/(Wg)\ge x_*^2\), and if the upper zero equals \(x_*\) the lower zero also equals \(x_*\). Thus \(x\ge x_*\). This includes the zero-discriminant case. When \(g=0\) the expression in (1) is nonincreasing in \(x\) and the same conclusion holds for \(f>0\), the case of interest. If \(Q\) is left free, a physical trial pair supplies (4) whenever \(x\ge x_*\). One-side certification at \(x_* = e^{-B}/\sqrt W\) on both signs gives \(|m_q(a)|\le B\).

For fixed \(Q\), the objective on the right of (4) is concave in the same-side row. The square of \(E_b\sqrt{\ell Q}\) is a sum of linear and geometric-mean terms in \(\ell\). The branch condition is linear. The supporting-cone formulation is the [round-48 one](static-trial-48.md) with the positive bulk weights \(Q\). In particular if an opposite-sector \(z\) satisfies

\[
 z_0\ge\sqrt n/x_*,\qquad z_i>0\ (i\ne0),\qquad
 \frac{a}{1-x_*g}E_b(Q/z)\le1 ,
 \tag{5}
\]

then \(Ez\) is an upper bound on the score of every \(\ell\) in (4). Use \(H^2\le E_b(z\ell)E_b(Q/z)\) and complementary pairing. This tracks the loss from fixing an unhelpful reference separately from a poor same-side optimizer. Dropping the branch constraint only makes this upper bound more conservative.

## Finite construction and an exact failed reference

The [checker](paired-trial-49-check.py) fixes \(a=1/2\) and \(B=0.017\), below the certified limiting 128-point budget. A floating solve at a warmer floor suggests the opposite row, and a convex optimization in the same Fourier coordinates proposes \(\ell\) for (4). Both rows are rounded to explicit dyadic cosine coefficients. Arb proves strictly positive entries, exact Fourier feasibility by construction, and strictly positive slack in both conditions (4). No solve at \(a=1/2\) enters the proposals. The lower bounds on positive score slack are

| Prime | Sign | Reference floor | Score slack greater than |
|---:|:---:|---:|---:|
| 97 | plus | 28 | 0.01635 |
| 97 | minus | 28 | 0.00419 |
| 173 | plus | 28 | 0.02361 |
| 173 | minus | 1 | 0.000830 |

The rounded opposite row proposed at floor 28 for prime 173 minus has a separate dyadic dual (5), with verified \(W-Ez>0.003\). Thus optimizing the same-side row against that particular reference cannot close the bound. A gradient projection from the floating maximizer failed to certify a dual; the saved dual comes from optimizing (5) and then scaling to satisfy both inequalities. The comparisons concern the finite scalar mark, not the full finite real continuation stencil with its hot coefficients.

Run the checker with the saved [five inputs and enclosures](paired-trial-49-checks.jsonl) to verify without either numerical optimizer or warm solve.

~~~sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/paired-trial-49-check.py \
  --replay research/paired-trial-49-checks.jsonl
~~~
