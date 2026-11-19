# Broad pinned defects: a reserve penalty and a weighted cap obstruction

Round 21. Only this note and `astra-broad-21-check.py` are new. No endpoint
asymptotic or uniform prime descent gap is proved.

There are two useful extensions of [anchored repair](anchored-repair-20.md).
First, a broad effective support has an explicit negative term in a bound for
the minimum defect, coming from the positive reference pair and the unused
mean reserve. Second, the smooth-cap argument extends from subgroup indicators
to weighted profiles of arbitrarily small energy relative to the critical
scale. The second extension gives a rich-correlation obstruction, but only
when a separate weighted rooted deficit tends to zero. Broadness alone does
not imply that hypothesis.

## 1. Exact reference identity and the broad-support penalty

Use the notation of [the reciprocal reference](parallel-transport-15.md):

\[
x=cj+u+sv,\qquad y=cj+su+v,\qquad
x_i y_i=0\ (i\ne0),\quad x,y\ge0,\quad 0<s<1,
\]

where \(u\in V_\sigma\), \(v\in V_{-\sigma}\), and
\(c^2+s(\|u\|^2+\|v\|^2)=1\). Let
\(H=y-su\), \(a_s=\sqrt n H_0\), and use the root-zero row
\(M=\mathbf1-P_{-\sigma}e_0/\kappa\) from anchored repair. At target mean
\(\mu\), the explicit affine trial is

\[
Y^{\rm ref}=\sqrt n H+(\mu-c)M.
\]

It has the prescribed mark and mean, regardless of its off-mark signs.
Write \(X_i=\sqrt n x_i\), \(V_i=\sqrt n y_i\), and

\[
A=\frac{s}{1-s^2},\qquad
b_i=\frac{sc}{1+s}+(\mu-c)M_i,\qquad b_* =\min_{i\ne0} b_i.
\]

Solving the two reference equations for \(u\) gives, **exactly** off the mark,

\[
-Y_i^{\rm ref}=A X_i-\frac{V_i}{1-s^2}-b_i.                 \tag{1}
\]

Now take any nonnegative opposite-sector witness \(W\), with \(W_0=1\).
Set \(w=W_{\rm off}\), \(S=\sum W\), \(B=\|w\|_2^2>0\), and
\(m=(S-1)^2/B\). Complementary Fourier support gives
\(\langle W,Y^{\rm ref}\rangle=\mu S\), hence

\[
\frac{a_s-\mu S}{\sqrt B}
=\frac{\langle w,-Y^{\rm ref}_{\rm off}\rangle}{\sqrt B}.
                                                               \tag{2}
\]

For every real \(\beta\), nonnegativity and Cauchy--Schwarz imply

\[
\boxed{\quad
\frac{a_s-\mu S}{\sqrt B}
\le \|(-Y^{\rm ref}_{\rm off}+\beta)_+\|_2-\beta\sqrt m.
\quad}                                                        \tag{3}
\]

Indeed add \(\beta\sum w=\beta(S-1)\) to the numerator in (2),
discard the negative part of the paired row, and apply Cauchy--Schwarz.
No assumption about stationarity, support cardinality, or a numerical
projection residual is used in (1)--(3).

When \(\beta\le b_*\), complementarity \(X_iV_i=0\) gives

\[
(-Y_i^{\rm ref}+\beta)_+
=A\left(X_i-\frac{b_i-\beta}{A}\right)_+
\le A\left(X_i-\frac{b_*-\beta}{A}\right)_+.
\]

Consequently, if the minimum defect is nonzero and \(m\) denotes the
effective support of its exact maximizing witness (equivalently of the
minimum defect), the exact dual in anchored repair proves

\[
\boxed{\quad
d(\mu)\le
\inf_{t\ge0}\left\{
A\|(X_{\rm off}-t)_+\|_2-(b_*-At)\sqrt m
\right\}.
\quad}                                                        \tag{4}
\]

The infimum allows negative \(\beta=b_*-At\); a positive reserve penalty
uses \(0\le t<b_*/A\). In particular, if \(b_*>0\), every nonzero minimum
satisfies, for each such \(t\),

\[
\sqrt m < \frac{A\|(X_{\rm off}-t)_+\|_2}{b_*-At}.             \tag{5}
\]

This is stronger than just charging the full negative-part norm: it retains
the mean reserve against a broad witness. At \(\mu=1\), \(c\le1\),
\(M_i=1+O(n^{-1/2})\), so
\(b_*=1-c/(1+s)+O((1-c)n^{-1/2})>0\) for sufficiently large orders.
The threshold window is asymptotically
\(b_*/A=(1-s)(1+s-c)/s+O((1-c)/(s\sqrt n))\).

For example, any lower bound \(m\ge m_b\) allows replacing \(\sqrt m\)
by \(\sqrt{m_b}\) in (4) when \(b_*-At\ge0\). A bound of its resulting
right side by \(\eta(s)n^{1/4}\) would control **all** minimizing defects
in that broad regime without a descent gap. This is a sufficient criterion,
not an established reference-tail estimate.

The exact multiscale version of (2) is also worth keeping:

\[
a_s-\mu S
=A\int_0^\infty w\{X>t\}\,dt
-\frac1{1-s^2}\int_0^\infty w\{V>t\}\,dt
-\sum_{i\ne0}b_iw_i.                                        \tag{6}
\]

Here \(w\{X>t\}=\sum_{i\ne0:X_i>t}w_i\). This identifies the needed
correlation with the *actual* positive row, rather than an arbitrary set of
the same cardinality. For a maximizing witness \(0\le w_i\le1\), so
\(w(T)\le\min\{|T|,S-1,\sqrt{B|T|}\}\). Substitution in the first integral
is valid but loses the negative second integral; no prime cancellation
follows from that substitution alone.

## 2. What Fourier-phase concentration really requires

The following calculations concern any feasible \(W\) with \(0\le W\le1\),
\(W_0=1\), in sector \(U_\sigma\). They therefore apply to the exact
minimum-defect witness. Let \(q\) be the field order, \(m_0=n/\sqrt q\),
\(\pi=W/S\), and, on the positional square group \(Q\), put

\[
f(x)=\sum_{h\in\widehat Q}\pi_h h(x),\quad
N_f=\|f\|_2^2=\frac{n(1+B)}{S^2},\quad
\delta_2=\frac{\sum_h W_h^2(1-\sigma k(h))}{1+B}.
\]

Extend \(f\) by zero outside \(Q\). With additive Paley convolution
\(\mathcal T\), the multiplicative diagonalization gives

\[
\langle f,(I-\sigma\mathcal T)f\rangle=\delta_2N_f.           \tag{7}
\]

Feasibility says \(f\) vanishes on the wrong positional sign away from
\(1\). Choose \(a\) with \(\chi(a)=\sigma\), set
\(Rf(x)=f(1-ax)\), and \(g=\mathbf1_Q Rf\). Exactly as in
[the reflection argument](parallel-extreme-6.md),
\(Rf-g=\mathbf1_{\{0\}}\). Thus \(|g|\le1\), \(N:=\|g\|_2^2=N_f-1\),
and

\[
\frac{\langle g,(I-\mathcal T)g\rangle}{N}
\le\frac{(\sqrt{\delta_2N_f}+1)^2}{N_f-1}.                   \tag{8}
\]

The constant 1 is the seminorm of the delta function, since the diagonal
of \(\mathcal T\) is zero. This improves an unspecified absolute constant
but does not create concentration where none exists.

The rooted equation only controls the **first-weight** deficit:

\[
\delta_1:=\sum_h\pi_h(1-\sigma k(h))
=1+q^{-1/2}-m_0/S.                                         \tag{9}
\]

Since \(W_h\le1\), it implies merely

\[
\delta_2\le\frac{S\delta_1}{1+B}.                           \tag{10}
\]

This is the broad-support loss. If \(B\ll S\), even \(\delta_1=o(1)\)
does not imply \(\delta_2=o(1)\). And at an infeasible target
\(S<(1-\delta)\sqrt n\), \(\delta_1\) need not tend to zero at all.
Therefore applying the critical phase-cap argument directly to every broad
minimum is unjustified. A sufficient route is
\(S\delta_1=o(B)\), or a direct estimate \(\delta_2=o(1)\).

## 3. A weighted rich-correlation obstruction at subcritical energy

Here is a generalization of the smooth-cap argument that does **not** require
\(N\asymp\sqrt q\), subgroup support, or an indicator profile. Use the cap
coefficient bounds from [Round 20, §1](parallel-rectangle-20.md), ultimately
based on [Xi's Jacobi estimates](https://arxiv.org/abs/1809.04286).
For \(g\) on \(Q\), define

\[
C_g(u)=\left|\sum_{x\in Q}g(ux)\overline{g(x)}\right|,
\qquad
\mathcal K(g)=\sup_{t>0}\frac{t^2\#\{u\ne1:C_g(u)>t\}}{N^2}.
\]

Suppose \(N>0\) and \(\mathcal K(g)\le K_0\) with a fixed constant.
Then there is \(\epsilon(K_0)>0\) such that,
for all sufficiently large \(q\),

\[
\langle g,(I-\mathcal T)g\rangle\ge\epsilon(K_0)N.       \tag{11}
\]

The statement works over prime and square orders; the *verification* of the
rich-correlation hypothesis can distinguish them. It is not an unconditional
prime theorem.

Proof. Write \(a_M\) for the inverse coefficients of
\(P_M(k)=((1+k)/2)^M\). Use a threshold adapted to the profile's energy.
The elementary count \(\#Q=n\) and the weak \(\ell_2\) hypothesis give,
for \(R\ge1\),

\[
\tau=N/\sqrt n,\qquad
\sum_{u\ne1:C_g(u)\le R\tau}C_g(u)^2
\le (1+2K_0\log R)N^2,\qquad
\sum_{u\ne1:C_g(u)>R\tau}C_g(u)
\le \frac{2K_0N\sqrt n}{R}.                                \tag{12}
\]

The first inequality follows by integration up to \(\tau\) using the count
\(n\), then to \(R\tau\) using the weak bound. The second includes the
boundary term at \(R\tau\) and the integral above it. Pairing correlations
with \(a_M\), using Cauchy--Schwarz below \(R\tau\) and the off-identity
supremum above it, gives

\[
\frac{\sum_h P_M(k(h))|\widehat g(h)|^2}{N}
\le |a_M(1)|+\|a_M\|_2\sqrt{1+2K_0\log R}
+\frac{2K_0\sqrt n}{R}\sup_{u\ne1}|a_M(u)|.                 \tag{13}
\]

Taking \(R=M\), then the field limit at fixed \(M\), bounds the right side
by
\(O(M^{-1/2}+M^{-1/4}\sqrt{1+K_0\log M}+K_0M^{-1/2})\).
Choose a sufficiently large fixed integer \(M\) so it is at most \(1/2\).
Since \(1-P_M(k)\le M(1-k)/2\), this gives (11) with \(\epsilon=1/M\).
The normalized threshold \(R N/\sqrt n\) is essential at broad, low-energy
profiles: a fixed threshold would introduce a spurious
\(\log(\sqrt n/N)\) in the low-correlation bound. Thus bounded
\(\mathcal K(g)\) gives a fixed additive spectral gap independent of \(N\).

Combining (8) and (11), any feasible witness sequence with
\(N_f\to\infty\) and \(\delta_2\to0\) must satisfy

\[
\boxed{\qquad \mathcal K(\mathbf1_Q Rf)\longrightarrow\infty.\qquad} \tag{14}
\]

This is a normalized rich-correlation necessary condition for an arbitrary
weighted profile. It is stronger information than a diverging total fourth
moment: the divergence must survive a weak \(\ell_2\) normalization. The
proof uses fixed \(M\) before the field limit and does not claim a usable
rate when \(\mathcal K\) grows.

There is a useful formulation without an unnamed phase parameter. If
\(\mathcal K(g)\le K_0\), (8), (10), and (11) imply

\[
(1+q^{-1/2})S-m_0
\ge (1+B)\left(
\sqrt{\epsilon(K_0)(1-1/N_f)}-N_f^{-1/2}
\right)_+^2.                                               \tag{15}
\]

In particular, when \(N_f\to\infty\), bounded rich-correlation constant
forces **absolute total-mass slack of order \(B\)** above \(m_0\), up to
the bounded correction \(S/\sqrt q\) for witnesses of mass \(O(\sqrt q)\).
Consequently \(B\to\infty\), \(S=O(\sqrt q)\), and
\(S-m_0=o(B)\) force \(\mathcal K(g)\to\infty\). For a fixed-gap
infeasible witness, the slow-width lower bound on \(B\) in anchored repair
already gives \(N_f\to\infty\). It does not give the required small mass
slack. Formula (15) is the quantitative structural alternative furnished
by the cap, including broad witnesses.

For the square subfield witness \(W=\mathbf1_I\), \(f\) is the indicator
of \(\mathbb F_{\sqrt q}^{\times}\), and one can take \(a=1\).
Then \(g=\mathbf1_{\mathbb F_{\sqrt q}^{\times}\setminus\{1\}}\).
Writing \(r=\sqrt q\), its energy is \(N=r-2\); each
\(u\in\mathbb F_r^\times\setminus\{1\}\) has correlation \(r-3\).
For \(r>3\), taking \(t=(r-3)/2\) gives
\(\mathcal K(g)\ge (r-3)^2/[4(r-2)]\to\infty\). This is the explicit
square failure of the dispersion hypothesis. The prime shifted-subgroup
estimate of Round 20 supplies bounded \(\mathcal K\) when the reflected
profile has critical-size subgroup support and norm comparable to that size.
It does not supply it for a general broad witness.

## 4. Scope and verification

The two missing inputs should not be conflated:

* For a genuinely broad minimum, (4) needs a prime estimate for the actual
  reference's thresholded second moment, with the reserve penalty retained.
* To use (14), one must first show weighted phase concentration
  \(\delta_2\to0\), then prove rich-correlation dispersion for the reflected
  positional profile. Neither follows from broad effective support alone.

The check script verifies the exact reference identities, (3)--(4) for
endpoint witnesses, and the square rich-correlation formula on small prime
and square examples. These are normalization and implementation checks, not
asymptotic evidence or interval certificates. The main results above are
finite-dimensional inequalities with the existing smooth-cap theorem as an
explicit arithmetic input.

Replay: `OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B
research/astra-broad-21-check.py`. On primes 101 and 401 and squares 49 and
361, both signs passed; the largest reference-identity or pairing discrepancy
was below \(2.7\cdot10^{-15}\). The square rich-correlation lower bounds
were exactly the stated formulas up to floating-point rounding. No claim of
exact stationarity is inferred from these residuals.
