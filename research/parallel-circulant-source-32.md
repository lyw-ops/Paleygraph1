# Actual Paley clipping: a cyclic triangle form and a hard-tail test

Round 32, 2026-11-18. ETH Problem 26, **ordinary** theta.

**Outcome.** This note proves three finite reductions for the actual
positive stationary pair: (i) source UI already handles the `delta` times
unweighted part of the opposite leakage; (ii) the remaining weighted
leakage is an explicit signed quadratic form on an induced **actual Paley
graph**, with its marked subtraction retained; (iii) the actual soft error
is a positive integral of actual bulk hard-tail errors. The last identity
gives a one-parameter, falsifiable sufficient hypothesis, (HR) below,
which together with UI closes the source-tightness step of round 29.

**The prime-uniform hypothesis (HR) is not proved. Neither source UI nor
Problem 26 is proved here.** Even source tightness by itself still needs
the arithmetic approximation step identified in round 29. This work
does not replace that step by an estimate on arbitrary perturbations.
No new non-Paley counterexample is constructed.

For the stationary floating-point pair at `p=1000033`, the largest measured
hard-tail ratio `H(R)^2/eta(R)` is `0.30360593` at `tau=.05` and
`0.30509805` at `tau=.01`, including threshold zero and both sectors.
For thresholds at least one the respective maxima are `0.21677789` and
`0.22322172`. These are grid diagnostics, not estimates through primes.
Squares also have bounded measured ratios; their large tail mass does
not disappear. That distinction is retained throughout.

## 1. Sources and what convolution adds

Read together with [source-pair 29](parallel-source-pair-29.md),
[coherent-source 31](parallel-coherent-source-31.md),
[Fable 28](claude-fable-28.md), and
[activation 26](parallel-activation-26.md). In particular, the prime-Paley
seed in round 31 is subsequently conjugated and **loses cyclic convolution**.
Its shared nonconstant Fourier coefficients prevent its two sources from
occupying opposite sectors of any cyclic convolution. A claim using only
full coherence and reciprocity would therefore repeat an excluded route.

All norms below use counting measure. Let `q=2n+1`, `c=tau/n`,

\[
 w=c\mathbf1+(1-c)e_0,\quad W=1+(n-1)c,\quad
 a=\sqrt{W/n},\quad \rho=c/a^2=\tau/W.
\]

Take the **exact actual** stationary spectra

\[
 A=a\mathbf1+x>0,\quad B=a\mathbf1+y>0,\quad
 AB=w,\quad x\in V_\sigma,\quad y\in V_{-\sigma}.
 \tag{1}
\]

Here `K` is the real even cyclic Paley convolution and
`P_sigma=(I-J+sigma K)/2`. Write

\[
 u=A/a,\quad d=c/(aA),\quad D=\operatorname{diag}d,\quad
 b=(1-c)/A_0,\quad e_-=P_{-\sigma}e_0.
 \tag{2}
\]

The full reciprocal identity, including the mark, is

\[
 d=B/a-(b/a)e_0.                                           \tag{3}
\]

For every cyclic shift `h`, disjoint Fourier sectors give

\[
 \boxed{\quad \sum_i A_{i+h}B_i=W.\quad}                  \tag{4}
\]

This is the full cross-correlation identity already implicit in Fable 28
A1, not a newly claimed discovery. It is substantially stronger than the
single unshifted inner product retained by a general reflection.

Some useful consequences, recorded to delimit the shifted-ratio/log path:

\[
 \sum_i\frac{A_{i+h}}{A_i}
 =n+\frac{1-c}{c}\left(1-\frac{A_h}{A_0}\right).             \tag{5}
\]

Let `pi_i=w_i/W` and `q_i^h=B_i A_{i+h}/W`. These are positive probability
vectors by (4), and cancellation of the cyclic sum of logarithms gives

\[
 \boxed{\quad
 W\operatorname{KL}(\pi\Vert q^h)
 =(1-c)\log(A_0/A_h).
 \quad}                                                     \tag{6}
\]

Thus `A_h<=A0`; the same argument for `B` gives `c<=A_h/A0<=1` off the
mark. For `h!=0`, deleting **both** exceptional coordinates `0,-h`, (5),
evenness, and its reverse-shift version give

\[
 2c\sum_{i\ne0,-h}\sinh^2
 \left(\tfrac12\log\frac{A_i}{A_{i+h}}\right)
 =(1-r_h)(1-c/r_h),\quad r_h=A_h/A_0.                        \tag{7}
\]

Equation (7) agrees with the earlier square-control shift budget; it is
not advertised as an additional asymptotic bound. Equations (5)--(7) hold
at squares too. They do not directly bound the square of a signed
opposite-sector projection.

The sharp Paley entry bound `|Kij|<=sqrt(q)/n` and positivity yield
`A0,B0<=a+sqrt(Wq/n)`; their product is one. Hence both roots are bounded
above and below at a fixed floor, and `d0=O_tau(n^(-1/2))`.

## 2. UI removes the delta part of the actual leakage

Use exactly the stripped error of round 29:

\[
 \theta_i=\frac{\delta}{d_i+\delta},\quad
 t_\delta=\theta x-\theta_0x_0e_0,\quad
 z_\delta=P_{-\sigma}t_\delta,\quad
 \ell_\delta^2=\|D^{1/2}z_\delta\|^2+\delta\|z_\delta\|^2.
 \tag{8}
\]

Define the **full**, unstripped cap

\[
 r_\delta(u)=\frac{\rho(u-1)}{\rho+\delta u},\qquad
 k_\delta=\theta_0x_0.
\]

Since `P_-sigma x=0`, the following is exact:

\[
 \boxed{\quad z_\delta=-aP_{-\sigma}r_\delta(u)-k_\delta e_-.
 \quad}                                                     \tag{9}
\]

For `R>=2`, put `M(R)=n^(-1)sum_i u_i 1_{u_i>R}`, **including** the mark.
The two elementary bounds

\[
 \begin{array}{ll}
 \delta r_\delta(u)^2\le\delta(R+1)(u+1),&u\le R,\\
 \delta r_\delta(u)^2\le\rho u/4,&u>R
 \end{array}
\]

use `E_n u=1` and `z/(1+z)^2<=1/4`. Projection is an unweighted
contraction, so (9) proves the finite inequality

\[
 \boxed{\quad
 \delta\|z_\delta\|^2
 \le4W\delta(R+1)+\frac\tau2 M(R)
       +2\delta k_\delta^2\|e_-\|^2.
 \quad}                                                     \tag{10}
\]

**Deterministic consequence.** UI of `A/a`, the root caps above, and fixed
`tau>0` imply

\[
 \lim_{\delta\downarrow0}\limsup_{p\to\infty}
          \delta\|z_{p,\delta}\|^2=0.                       \tag{11}
\]

The mark has full first mass `u0/n=O_tau(n^(-1/2))`, and
`k_delta=O_tau(1)`. Thus it is harmless in this order of limits; it was
not silently dropped from (10). The source UI in round 29 implies UI of
both `A/a,B/a`, so it supplies this hypothesis. No bound on `||x||^2` is
used. This proves a proper subpart of the previously unresolved leakage
estimate; the `D` part remains.

## 3. The remaining energy is an actual Paley triangle form

Fix a primitive element `g` of the field, so the nonzero squares are
`alpha_k=g^(2k)` and the actual multiplier is
`s(k)=chi(1-alpha_k)`. Let

\[
 E=\{k:s(k)=-\sigma\},\qquad
 \beta_k=\frac1n\operatorname{DFT}(B/a)_k.
\]

Then `beta0=1` and `beta` vanishes off `{0} union E`. For an arbitrary
real even test `h`, put

\[
 r_k=\frac1n\operatorname{DFT}(h)_k\mathbf1_{k\in E},\qquad
 z=P_{-\sigma}h.
\]

**Finite identity.** Fourier multiplication and (3) give

\[
 \boxed{\begin{split}
 \|D^{1/2}z\|^2
 &=n\sum_{k\in E}|r_k|^2\\
 &\quad+n\!\sum_{\substack{k,l\in E\\k-l\in E}}
       \overline{r_k}\,\beta_{k-l}\,r_l
       -\frac ba\left|\sum_{k\in E}r_k\right|^2.
 \end{split}}                                               \tag{12}
\]

To identify the arithmetic rather than merely rename a generic Fourier
quadratic form, note

\[
 s(k-l)=\chi(1-\alpha_k/\alpha_l)
       =\chi(\alpha_k-\alpha_l),                            \tag{13}
\]

since `alpha_l` and `-1` are squares. Thus the middle term in (12) runs
over the **actual induced Paley adjacency** when `-sigma=+1`, and its
complement when `-sigma=-1`, on the vertices
`{alpha in Q:chi(1-alpha)=-sigma}`. Its edge coefficient is the actual
opposite-source Fourier coefficient `beta(k-l)`; the test coefficients
below come from the **actual clipped source**. They are not independent
or arbitrary signs. Formula (12) is directly available both for `h=t_delta`
and for the hard tails in Section 4.

The last term is the exact exceptional-mark subtraction. Deleting it
changes the problem. Neither `beta` nor the test coefficients are assumed
nonnegative; Fable 28 already observed negative positional coefficients
at primes. The positive definiteness of `B/a` makes the full uncorrected
Toeplitz form positive, but does not bound the signed triangle term by a
dimension-independent multiple of its diagonal. The Paley label (13)
and convolution are genuinely used in this reduction; a coherent
rank-twelve conjugate from round 31 does not have (12) with this adjacency.

### A positive two-point remainder, and where signs remain

Set `f_delta(u)=delta*u*(u-1)/(rho+delta*u)`, so
`t_delta=a*f_delta(u)-a*f_delta(u0)e0`. Its exact affine remainder is

\[
 f_\delta(v)-f_\delta(u)-f'_\delta(u)(v-u)
 =\frac{\delta\rho(\rho+\delta)(v-u)^2}
        {(\rho+\delta u)^2(\rho+\delta v)}\ge0.              \tag{14}
\]

Writing `pij=(P_-sigma)ij`, its rows annihilate both `1` and `u`. Hence

\[
 (z_\delta)_i
 =\frac{a\delta\rho(\rho+\delta)}{(\rho+\delta u_i)^2}
   \sum_j p_{ij}\frac{(u_j-u_i)^2}{\rho+\delta u_j}
   -k_\delta(e_-)_i.                                       \tag{15}
\]

All arguments and all positive divided differences here are actual ones.
But the coefficients `pij` still have both signs. Replacing them by their
absolute values is very costly **on the actual source**, not just on an
adversarial direction. For example at `tau=.05,delta=.01`:

| order | side | actual `D` leakage | absolute-remainder upper bound |
|---:|---:|---:|---:|
| 101 | + | .00255953 | 1.57506 |
| 401 | + | .01384968 | 8.21583 |
| 361 | + | .18212347 | 27.71023 |

These finite computations do not prove divergence of the absolute bound;
they show why (14)'s positivity alone has not established the needed
signed estimate. No arbitrary-error instability is substituted for this
calculation.

## 4. Hard-tail superposition and a single additional input

For `R>=0` define the **actual bulk hinge**, its excess first mass and its
weighted opposite response:

\[
 h_R=a(u-R)_+\mathbf1_{i\ne0},\quad
 \eta(R)=\frac1n\sum_{i\ne0}(u_i-R)_+,\quad
 H(R)=\|D^{1/2}P_{-\sigma}h_R\|.                            \tag{16}
\]

The deletion in `h_R` is before projection. All coordinates, including
the newly created mark, are kept in `H`.

The scalar second derivative and its mass are

\[
 f''_\delta(R)=\frac{2\delta\rho(\rho+\delta)}
                         {(\rho+\delta R)^3}>0,\quad
 \int_0^\infty f''_\delta(R)\,dR=1+\delta/\rho.
 \tag{17}
\]

For each fixed `R0`, the integral over `[0,R0]` tends to zero as
`delta->0`. Since `f_delta(0)=0` and `f'_delta(0)=-delta/rho`, the
scalar hinge expansion and `P_-sigma A_bulk=-A0 e_-` prove

\[
 \boxed{\quad
 z_\delta=\frac{\delta A_0}{\rho}e_-
              +\int_0^\infty f''_\delta(R)
                        P_{-\sigma}h_R\,dR.
 \quad}                                                     \tag{18}
\]

This is an exact vector identity at every finite size. It uses the actual
family rather than a norm estimate on all possible errors. In particular,
the potentially order-one stripped soft mark in (8) has become a
`delta*A0/rho` term after the entire hard-tail integral is accounted for.
It would be incorrect to drop its contribution in one formula while
retaining the other terms from the other formula.

The Paley coherence and `sum d<n` give

\[
 \|D^{1/2}e_-\|^2
 \le (e_-)_0^2d_0+\frac{(1+\sqrt q)^2}{4n}=O_\tau(1).
 \tag{19}
\]

Minkowski applied to (18) therefore supplies a new finite sufficient
test. A particularly concrete **unproved arithmetic hypothesis** is

\[
 \boxed{\quad
 \text{(HR)}_\tau:\quad
 H_{p,\sigma}(R)^2\le C_\tau\eta_{p,\sigma}(R)
 \quad\text{for all }R\ge0\text{ and all sufficiently large primes }p,
 \quad}                                                     \tag{20}
\]

where `C_tau<infinity` is independent of `p,R`. Use either side separately,
or both. This is a tail-restriction inequality for the actual Paley pair;
it does **not** ask for a weighted norm bound on the full projection
operator or on arbitrary supported vectors. Its triangle version is
obtained by putting `h=h_R` in (12). A specific numerical candidate for
testing is `C_tau=1` at the three tested floors. That candidate is only
a hypothesis, not a claimed theorem at these floors or at all floors.

**Finite conditional theorem.** Assuming (20), for every `R0>=0`,

\[
 \begin{split}
 \|D^{1/2}z_\delta\|
 &\le \frac{\delta A_0}{\rho}\|D^{1/2}e_-\|\\
 &\quad+\sqrt{C_\tau}\left[
 \frac{2\delta(\rho+\delta)R_0}{\rho^2}
 +(1+\delta/\rho)\sqrt{\eta(R_0)}\right].
 \end{split}                                                \tag{21}
\]

Indeed `eta(R)<=1` and is decreasing. On `[0,R0]`, integrate the upper
bound `f''<=2delta(rho+delta)/rho^2`; on the remaining interval use
`sqrt(eta(R))<=sqrt(eta(R0))` and the full mass (17). This proves (21).

UI of `u` is equivalent to
`lim_R limsup_p eta_p(R)=0`: one direction is immediate and the other
uses `u 1_{u>2R}<=2(u-R)+`. Thus (21), then (10), prove

\[
 \text{source UI}+(\mathrm{HR})_\tau
 \quad\Longrightarrow\quad
 \lim_{\delta\downarrow0}\limsup_{p\to\infty}\ell_{p,\delta}=0.
 \tag{22}
\]

Round 29's certificate now gives inverse-first-source-moment tightness.
There is no second inverse moment or stationary Euclidean-energy bound
in this implication. It still does not supply round 29's missing
arithmetic comparison of the regularized source, so it is not a theorem
of the prime theta asymptotic.

For context, an even stronger, more familiar restricted-projection
hypothesis would be
`H(R)^2<=M_tau ||D^(1/2)h_R||^2`. Since `0<=h_R<=A` off the mark,

\[
 \|D^{1/2}h_R\|^2\le(c/a)\sum_i(h_R)_i=\tau\eta(R),         \tag{23}
\]

that would imply (20) with `C_tau=tau*M_tau`. It is unnecessary to
assume this stronger inequality. The minimal qualitative input at the
hinge-integral interface is a uniform bounded response envelope with
`lim_R limsup_p H(R)=0`; (20) is a precise, readily testable sufficient
version which transfers the already desired UI directly. No assertion
that (20) is logically the weakest possible hypothesis is made: soft
integrals can cancel across `R`, and (18) is not a converse bound.

### A finite reduction of all thresholds

At any fixed source, between consecutive distinct bulk values of `u`,
the vector `P_-sigma h_R` is affine in `R` and `eta(R)` is positive
affine. The quadratic-over-linear function
`H(R)^2/eta(R)` is convex on that interval. Consequently its supremum
over all `R>=0` occurs at `R=0` or one of the bulk `u`-values; the final
interval tends to ratio zero. This gives an exact finite reduction for
testing (20), not a bound on the resulting finite maximum.

The small replay scans all these knots. The million-order replay scans
only the stated grid: its reported maximum is a **lower** bound on the
whole-threshold maximum. No large-size continuum verification is claimed.

### The new hypothesis quantitatively excludes the existing round-31 family

This is a check on the **already constructed** noncirculant family, not
a new counterexample or a replacement for the actual Paley diagnostics.
Reuse its exact eight-group block with
`n=2t^8,m=t^4,H=t^3`, its default background choice, and `s_t=sqrt(W_t)`.
Choose the growing threshold

\[
 R_t=H/(2s_t).
\]

For sufficiently large `t`, stripping the mark leaves exactly the high
`A` tail, at half its original height. In the normalized group basis,

\[
 h_{R_t}=\ell_t e_T,\quad
 \ell_t=H\sqrt m/(2\sqrt n)=t/(2\sqrt2),\quad
 \boxed{\ \eta_t(R_t)=1/(4s_t t).\ }                       \tag{25}
\]

The old block defines `u_+=e_+/sqrt(l_+)`,
`X=x-((1-a)/l_+)e_+`, `E_X=||X||^2`, and

\[
 P_-=I-jj^T-u_+u_+^T-XX^T/E_X,\qquad
 F_t=\|D^{1/2}X\|^2\longrightarrow F_*>0.
\]

Round 31 proves `F_*=.454148254928...` for `tau=.05`. Direct projection
gives the exact identity

\[
 P_-h_{R_t}+X/2
 =\ell_t e_T-\ell_t j_Tj-\ell_t(u_+)_T u_+
   +\left(\tfrac12-\frac{\ell_tX_T}{E_X}\right)X.
 \tag{26}
\]

Each term on the right tends to zero in the `D` norm:
`ell_t^2 d_T=tau/(8s_t t)`, `ell_t j_T=1/(4t)`,
`ell_t(u_+)_T=O(t^(-5))`, and `ell_t X_T/E_X->1/2`.
The remaining factor norms are bounded: `||D^(1/2)j||<=1`,
`||D^(1/2)u_+||=O_tau(1)` by the old source-moment formula, and
`||D^(1/2)X||^2=F_t->F_*`. Therefore

\[
 \boxed{\quad
 H_t(R_t)^2\longrightarrow F_*/4>0,\qquad
 \frac{H_t(R_t)^2}{\eta_t(R_t)}
       \sim\sqrt{1+\tau}\,F_*\,t\longrightarrow\infty.
 \quad}                                                     \tag{27}
\]

Equation (27) disproves (HR) on this family. To check the field-first
qualitative condition separately, fix any `R` above the limiting
background maximum of `u`. Eventually the only bulk hinge is again the
high tail, now with coefficient `(H-s_t R)*sqrt(m/n)~t/sqrt(2)`.
The proof of (26), with this coefficient in place of `ell_t`, gives
`||D^(1/2)(P_- h_R+X)||->0`, hence `H_t(R)^2->F_*>0` for every such
fixed `R`. Thus `lim_R limsup_t H_t(R)` does not vanish either. A moving
threshold alone would not have proved that order of limits.

Both (HR) and the qualitative decaying hard-tail condition therefore
exclude the prior coherence-plus-UI obstruction. They are not consequences
of the hypotheses retained in that family. Its failure of convolution
is still essential to interpreting this comparison; (27) says nothing
against actual prime Paley sources.

The cheap five-block replay at `tau=.05` gives:

| `t` | `eta(R_t)` | `H(R_t)^2` | `H^2/eta` |
|---:|---:|---:|---:|
| 8 | .03049688 | .10040928 | 3.29244 |
| 32 | .00762422 | .11054410 | 14.49907 |
| 128 | .00190605 | .11281728 | 59.18889 |
| 512 | .000476514 | .11335912 | 237.89267 |
| 4096 | .0000595642 | .11351490 | 1905.75665 |

The exact limiting hinge energy is `F_*/4=.113537063732...`. The script
imports the existing `build_block` and `limiting_row` read-only, in the
same eight-dimensional basis; it does not construct a huge matrix.

## 5. What the logarithm path does and does not add

Pointwise reciprocity gives `log A+log B=log w`. With normalized Fourier
coefficients, every nonzero cepstral coefficient of this sum is exactly
`-log(c)/n`, and the zero coefficient is `(1-1/n)log(c)`. This is an
exact log-reciprocity identity with the mark included. It does not imply
that the separate logarithms occupy opposite linear sectors; exponentials
mix convolution powers of those coefficients.

More explicitly, let `g_i=log(A_i/sqrt(c))` off the mark. Then

\[
 \frac1n\sum_{i\ne0}e^{|g_i|}
 \le\frac1n\sum_{i\ne0}\frac{A_i+B_i}{\sqrt c}
 \le2/\sqrt\rho,\qquad
 G_i=2\sqrt\tau(\cosh g_i-1).                               \tag{24}
\]

Thus all fixed logarithmic moments have uniform bounds and the fraction
with `|g|>t` is at most `2e^(-t)/sqrt(rho)`. But source UI is exactly the
critical endpoint requirement that `exp(|g|)` be UI; its bounded first
moment in (24) is insufficient. Squares satisfy these log bounds too.
No new claim of UI follows from the log/cepstral path in this note.

Similarly, (6)--(7) control positive translated ratios and their log
increments but not the signed Paley triangle energy (12). A full Schur
mixing gap for squared entries alone is not used: it does not encode the
signed, source-dependent triangles left in (12). The concrete unresolved
arithmetic input has been isolated as (20), not replaced by coherence,
a positivity slogan, or arbitrary-error instability.

The path comparison is therefore:

| path | deterministic output | remaining obstruction |
|---|---|---|
| cyclic translated pair | (4)--(7), including a KL identity | no signed-projection square bound |
| reciprocal cepstrum | exact exceptional coefficient and (24) | bounded critical exponential moment is not UI |
| actual-error propagation by the sector equation | (9)--(11) dispose of the `delta` part | no bound for the `D` part |
| convex positive remainder | actual two-point formula (15) | signed Paley cancellation survives |
| hard-tail integration | (18), (21), and conditional tightness (22) | prove UI and the uniform actual-source bound (20) |
| Paley convolution triangles | exact actual adjacency formula (12)--(13) | control its source-dependent signed quadratic form |

## 6. Floating-point diagnostics and comparison

The script uses integer actual Paley signs, safeguarded stationary solves
from the existing `weighted_iterate`, stable reciprocal reconstruction,
and exact-source formulas. Residuals are measured at the stored numerical
pair; they are **not distance enclosures** to the exact stationary pair.
All FFTs, quadratic forms, scans, and reported inequalities are floating
point, with no interval-certification claim.

The primary `tau=.05` set includes primes `101,401,9413,153649,1000033`
and square roots `19,97,389`. The smaller-floor sets include a million
prime at `.01` and primes through `153649` at `.001`. Both sectors are
recorded. Some grid maxima, including zero, are:

| order | floor | max measured `H^2/eta` |
|---:|---:|---:|
| 9413 | .05 | .29842260 |
| 153649 | .05 | .30279586 |
| 1000033 | .05 | .30360593 |
| 1000033 | .01 | .30509805 |
| 153649 | .001 | .30474106 |
| 97^2 | .05 | .52071046 |
| 389^2 | .05 | .53104714 |

Threshold zero just returns `P_-sigma A_bulk=-A0 e_-`; its ratio is a
marked first-moment diagnostic. Thus **the maxima near `.30` at zero are
not themselves new tail evidence**. The following positive thresholds
show what is actually being tested on the tail at `p=1000033,tau=.05`:

| side | `R` | `eta(R)` | `H(R)^2` | ratio |
|---:|---:|---:|---:|---:|
| + | 2 | .23183813 | .04140244 | .17858340 |
| + | 4 | .01468942 | .00312035 | .21242167 |
| + | 6 | .000121024 | .0000175049 | .14464024 |
| - | 2 | .23127933 | .04124019 | .17831334 |
| - | 4 | .01469236 | .00318498 | .21677789 |
| - | 6 | .000123288 | .0000164488 | .13341787 |

Both bulk normalized maxima are below `7.18` in that run. This finite
observation supplies neither a field-uniform cap nor UI through primes.
At `389^2`, plus, `R=32`, the excess mass is `.81866407` and the weighted
hinge energy `.39444171`; at `R=128` they remain `.57251022` and
`.19291033`. This records the square obstruction in actual source tails
instead of ignoring it because a projection ratio happens to be bounded.

The soft leakage split at `tau=.05` illustrates the difference:

| order, side | `delta` | `D` contribution | `delta` contribution |
|---|---:|---:|---:|
| 1000033, + | .01 | .01879031 | .000379647 |
| 1000033, + | .0002 | .0000260429 | .0000000101090 |
| 389^2, + | .01 | .45432499 | .00815123 |
| 389^2, + | .0002 | .16855791 | .0000604544 |

Field-first conclusions are not inferred from this finite table. The
rigorous field-first statement about the `delta` column is (10)--(11),
conditional on UI.

The independent small replay explicitly enumerates the Paley triangle
vertices in (12), checks the positive divided-difference formula (15),
integrates the hinge expansion with adaptive quadrature, and scans all
threshold knots. At `101,401,19^2`, the maximum triangle discrepancy is
below `2.5e-13`, the curvature discrepancy below `2.5e-12`, and the hinge
superposition discrepancy below `3.9e-12`. These check implementation
consistency, not exact real-arithmetic validity of a floating solve.
The algebraic proofs are Sections 2--4.

The primary, `.01`, `.001`, and small diagnostic files have respectively
382, 141, 219, and 147 records. The primary and small outputs include six
all-threshold scans each; the `.001` output includes four. Only the small
cases (`n<=300`) make a whole-threshold numerical claim. The
single-prime million runs cost roughly one to two minutes at these floors on this
machine; no dense million-by-million matrix is formed.

## 7. Replay and scope

From the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-circulant-source-32.py \
  > research/parallel-circulant-source-32.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-circulant-source-32.py --primes 101 401 --square-roots 19 \
  > research/parallel-circulant-source-32-small.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-circulant-source-32.py \
  --primes 9413 153649 1000033 --square-roots --tau .01 \
  --thresholds 0 1 2 3 4 5 6 7 8 10 16 32 \
  --deltas .05 .01 .002 .0002 .00002 \
  > research/parallel-circulant-source-32-floor01.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-circulant-source-32.py \
  --primes 401 9413 153649 --square-roots 19 97 --tau .001 \
  --thresholds 0 1 2 3 4 5 6 7 8 10 16 32 \
  --deltas .01 .002 .0002 .00002 \
  > research/parallel-circulant-source-32-floor001.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-circulant-source-32.py --existing31-check \
  > research/parallel-circulant-source-32-existing31.jsonl
```

The read-back consistency audit is replayable without rerunning the
stationary solves:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-circulant-source-32.py --audit-files \
  research/parallel-circulant-source-32.jsonl \
  research/parallel-circulant-source-32-small.jsonl \
  research/parallel-circulant-source-32-floor01.jsonl \
  research/parallel-circulant-source-32-floor001.jsonl \
  research/parallel-circulant-source-32-existing31.jsonl \
  > research/parallel-circulant-source-32-acceptance.jsonl
```

Runtime rows naturally vary between replays. The audit checks identity
residuals, the finite UI upper bounds, direct hinge bounds, positivity,
record completeness by field, and the candidate `C_tau=1` on the recorded
thresholds or scans. It certifies consistency of these floating records;
it does not certify the stationary solves or a uniform prime estimate.
The read-back audit passed for all 895 records (889 Paley replay records
and six reused round-31 block records), including runtime rows
and the intentionally repeated small checks. Its six summary records
are in `parallel-circulant-source-32-acceptance.jsonl`.

Only files beginning `research/parallel-circulant-source-32` were written.
No README/ledger edits, commits, pushes, settings changes, external
communications, or modifications of other research lines were performed.
