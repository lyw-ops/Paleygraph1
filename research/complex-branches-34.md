# Two-variable stationary curves and their marked logarithms

Round 34. The actual marked logarithms at prime $p=17$ and square order
$q=25$ both extend holomorphically to $\operatorname{Re}\tau>0$.
This extends the exact prime-13 example of
[round 33](complex-floor-33.md) to genuinely two-variable central paths.
The proof checks reconstruction denominators as well as discriminants;
a scalar elimination polynomial alone would not establish the claim.

These are finite-field results. In particular the square example has the
same continuation domain as the prime examples. Absence of branch points
in these small fields does **not** distinguish the asymptotic prime and
square problems, prove a common domain for growing fields, or give the
subpolynomial complex-growth bound needed in round 33. Problem 26 remains
open.

## 1. The actual prime-17 plus curve

Write $n=8$, $W=1+7\tau/8$, $a=\sqrt{W/8}$. In the standard
cyclic coordinates the actual multiplier is

\[
 (0,1,-1,-1,1,-1,-1,1).
\]

Every even normalized plus spectrum is

\[
 u_i=1+x\cos(\pi i/4)+y(-1)^i.
\]

Set $\alpha=1+y$, $r=x/\alpha$, and $t=(1-y)/\alpha$, so
$\alpha=2/(1+t)$. The positive real stationary branch has
$r\in(-1,1)$, $t>|r|/\sqrt2$. Up to constants independent of the
variables, its weighted logarithmic objective is

\[
 F_{17}(r,t;\tau)=W\log\frac2{1+t}+\log(1+r)
       +\frac\tau4\log(t^2-r^2/2)+\frac\tau8\log(1-r).
                                                               \tag{1}
\]

The first-order equations imply

\[
 (16+6\tau)t^2-8\tau t-(8+7\tau)r^2=0,
\quad
 L_{17}t(1+t)=4Wr(1-r^2),
\]

where $L_{17}=8-\tau-(8+\tau)r$. Away from $L_{17}=0$,

\[
 t=N_{17}/D_{17},\quad D_{17}=4L_{17},\quad
 N_{17}=r[16+6\tau-2(8-\tau)r-4\tau r^2].                 \tag{2}
\]

Exact elimination gives the quintic

\[
\begin{split}
 Q_{17}={}&4\tau^2r^5+(-4\tau^2+32\tau)r^4
 +(-21\tau^2-144\tau-64)r^3\\
 &+(-6\tau^2+32\tau+128)r^2
 +(15\tau^2+144\tau-64)r+8\tau^2-64\tau.                \tag{3}
\end{split}
\]

To specify which factors were removed, substitute (2) in the quadratic
equation without dividing by $r$. Its numerator is exactly

\[
 (16+6\tau)N_{17}^2-32\tau N_{17}L_{17}
       -16(8+7\tau)r^2L_{17}^2
       =8(3\tau+8)rQ_{17}.                               \tag{4}
\]

The actual branch satisfies $Q_{17}=0$, including at $r=0,\tau=8$
by continuity. At that equal-weight point its original coordinates are
$x=y=0$, hence $r=0,t=1$.

## 2. The actual square-25 minus curve

Here $n=12$, $W=1+11\tau/12$, $a=\sqrt{W/12}$, and the multiplier is

\[
 (0,-1,1,1,-1,-1,1,-1,-1,1,1,-1).
\]

The permutation of frequencies $i\mapsto5i$ preserves this multiplier
and the marked weights. Uniqueness of the positive optimum makes the
stationary spectrum invariant under it. The even minus spectrum is
therefore of the form

\[
 v_i=1+X[\cos(\pi i/6)+\cos(5\pi i/6)]
                          +Y\cos(2\pi i/3).
\]

The unrestricted even minus space has three dimensions; this extra
symmetry makes its stationary problem two-dimensional. This is an actual
symmetry reduction, not an imposed ansatz. Equivalently, averaging over
the symmetry preserves positivity and improves the concave log objective.

Put $\alpha=1+Y$, $\beta=1-Y/2$, $r=2X/\alpha$, and
$t=2\beta/\alpha$. Then $\alpha=3/(1+t)$. The distinct values are

| Frequency class | Spectrum value |
|---|---|
| 0 | $\alpha(1+r)$ |
| 1,5,7,11 | $\alpha t/2$ |
| 2,10 | $\alpha(t+r)/2$ |
| 3,9 | $\alpha$ |
| 4,8 | $\alpha(t-r)/2$ |
| 6 | $\alpha(1-r)$ |

Its objective is, up to constants,

\[
 F_{25}=W\log\frac3{1+t}+\log(1+r)
 +\frac\tau{12}[4\log(t/2)+2\log((t^2-r^2)/4)+\log(1-r)]. \tag{5}
\]

The two stationary equations yield, with
$L_{25}=12-\tau-(12+\tau)r$,

\[
 t=N_{25}/D_{25},\quad
 N_{25}=-rL_{25}-8\tau(1-r^2),\quad
 D_{25}=rL_{25}-3(4+\tau)(1-r^2).                         \tag{6}
\]

The reduced quintic is

\[
\begin{split}
 Q_{25}={}&(5\tau^2+12\tau)r^5+(-4\tau^2+36\tau+144)r^4\\
 &+(-34\tau^2-384\tau-864)r^3
 +(-20\tau^2+144\tau+1152)r^2\\
 &+(21\tau^2+360\tau-432)r+16\tau^2-192\tau.             \tag{7}
\end{split}
\]

The exact cleared identity is

\[
 L_{25}N_{25}^2-D_{25}^2[r^2L_{25}+4\tau r(1-r^2)]
                   =4\tau(r-1)(r+1)Q_{25}.              \tag{8}
\]

The positive stationary branch satisfies (7). At equal weights
$\tau=12$, it has $r=0,t=2$. No deleted $r=\pm1$ factor belongs to
the positive real branch.

## 3. Exact discriminants and reconstruction checks

Integer polynomial computation gives

\[
 \operatorname{disc}_rQ_{17}=2^{18}\tau^4 H_{17}(\tau),
\qquad
 \operatorname{disc}_rQ_{25}=2304(11\tau+12)^4H_{25}(\tau),\tag{9}
\]

where both $H$'s have degree ten. Their full integer coefficients and
all ten leading Hurwitz determinants are in the first three records for
each field in [the certificate](complex-branches-34-certified.jsonl).
Every determinant is a strictly positive integer. The general
[Hurwitz criterion, Theorem 40](https://arxiv.org/pdf/0802.1805)
therefore puts every zero of both degree-ten factors in the open left
half-plane. Acb root isolation independently verifies those locations.
The leading coefficients of the quintics vanish only at zero or negative
real parameters. Hence each quintic has five distinct holomorphic roots
over the simply connected right half-plane.

It remains to check that the rational reconstructions and marked
logarithms do not introduce new singularities. Exact resultants are

\[
\begin{array}{c|l}
 &\operatorname{Res}_r(Q,\text{denominator})\\\hline
17,D_{17}&-2^{20}(\tau-8)\tau^2(3\tau+8)^2\\
17,D_{17}+N_{17}&-2^{20}(\tau-8)(3\tau+8)(7\tau+8)^3\tau^4\\
25,D_{25}&-1728(\tau+4)\tau^2(11\tau+12)^4\\
25,D_{25}+N_{25}&-20736\tau(2\tau+3)(11\tau+12)^5.
\end{array}                                                   \tag{10}
\]

Thus neither reconstruction denominator nor $1+t$ can vanish in the
right half-plane, except for the possible prime-17 point at eight.
There, the actual $r$ root is simple; the real stationary solution is
analytic and has $t=1$. Its rational reconstruction consequently has a
removable singularity, rather than a pole. Boundedness along the real
approach suffices because that reconstruction is meromorphic locally.

Finally $Q_{17}(-1,\tau)=256$ and $Q_{25}(-1,\tau)=2592$.
The root factors $1+r$ never vanish. The stationary scaling $W$ has
its zero on the negative axis. Therefore the expressions

\[
\begin{split}
 m_{17}(\tau)&=\tfrac12\log(W/8)
                         +\log\frac{2(1+r)}{1+t},\\
 m_{25}(\tau)&=-\tfrac12\log(W/12)
                         -\log\frac{3(1+r)}{1+t}
\end{split}                                                   \tag{11}
\]

have holomorphic choices on $\operatorname{Re}\tau>0$, normalized to
zero at eight and twelve respectively. The minus sign in the second
line is essential: the square calculation used the **minus** spectrum,
and $A_0B_0=1$. These expressions agree with the actual real stationary
germs, so they give their marked analytic continuations. The
[independent audit](parallel-audit-34.md#4-extra-finite-conclusion-all-complex-spectral-coordinates-are-nonzero)
also proves that every coordinate of both actual reciprocal rows has a
nonvanishing holomorphic continuation on this half-plane. It checks the
remaining coordinate factors using the original cleared first-order
equations, including the equal-weight removable point. Positivity is
asserted only on the positive real axis. This stronger statement still
concerns only these two fixed fields.

## 4. Reproduction and consequence for the larger question

```sh
.venv/bin/python -B research/complex-branches-34.py \
  > research/complex-branches-34-certified.jsonl
```

The fourteen records comprise two exact elimination/resultant identities,
two exact degree-ten Hurwitz checks, two validated discriminant-root lists,
and eight interval stationary reconstructions. At each field the tested
floors are $1/20,1,n,20$. Arb validates positive spectra, both means,
and every fixed-point residual coordinate, with no Newton or optimization
proposal. The general continuation statements follow from (9)--(11),
not from sampling the real floors.

The [entropic-discriminant literature](https://arxiv.org/abs/1108.2925)
studies related branch loci of analytic-center equations. No theorem from
it is assumed to give the parameter locations in these Paley examples;
the eliminations above are computed explicitly. Their relevance is to
make the proposed continuation route testable beyond a one-dimensional
special case.

In particular, the square example shows that a finite right-half-plane
continuation theorem alone is insufficient for prime/square separation.
The common-domain and growth obligations of round 33 are still open for
growing primes; the square-family obstruction there still applies.
Neither an asymptotic complex-growth estimate nor a solution of ETH26 is
claimed.
