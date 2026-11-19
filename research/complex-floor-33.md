# A complex-floor continuation criterion, and an exact small-prime branch

Round 33, ordinary theta. This is an alternative to proving source UI and
hard-tail response bounds. It does **not** establish the complex estimates
required through all primes, and therefore does not solve Problem 26.

The new finite calculation gives the exact marked central-path cubic at
prime 13. Its discriminant has all roots strictly in the left half-plane,
so this particular stationary marked logarithm extends holomorphically to
the entire right half-plane. The asymptotic continuation criterion below
requires common domains and controlled complex growth for growing primes;
one small prime does not supply those requirements.

## 1. What quantitative analytic continuation would suffice

Let (m_q(t)=\log A_{q,0}(t)=\operatorname{arsinh}(v_{q,0}(t)/2))
for the actual positive stationary pair at floor (t>0). The real germ
is analytic at every finite field and positive floor. The inherited
[large-floor invariant ball](large-smoothing.md) gives, for any fixed hot
interval (E=[T,T+1]), (T\ge1024), and all sufficiently large (q),

\[
 \sup_{t\in E}|m_q(t)|\le6q^{-1/2}.                       \tag{1}
\]

Indeed the scaled marked field has absolute value at most six, so
(|m_q(t)|\le3/\sqrt n\), (n=(q-1)/2). This input is field-general.

Fix (0<a<T). Let (D) be a bounded rectangle containing ([a,T+1])
in its interior, and set

\[
 \omega_a=\omega(a,E,D\setminus E)\in(0,1),
\]

the harmonic measure of the two sides of the interior slit. Suppose the
actual real germ (m_p), for every sufficiently large relevant prime,
extends holomorphically to (D), with

\[
 M_p=\max\{1,\sup_D|m_p|\},\qquad
                         \log M_p=o(\log p).              \tag{2}
\]

Then the two-constants principle on the slit domain, applied to
(\log|m_p|), proves

\[
 \boxed{|m_p(a)|\le(6p^{-1/2})^{\omega_a}
                              M_p^{1-\omega_a}
                   =p^{-\omega_a/2+o(1)}.}                \tag{3}
\]

Zeros of (m_p) cause no problem: its logarithm is subharmonic with
value minus infinity there. The rectangle may be replaced by a regular
bounded domain for which the slit has positive harmonic measure. A compact
cold interval has a positive minimum harmonic measure. The standard
two-constants statement is, for example,
[Langley, postgraduate complex-analysis notes, Theorem 10.2.10](https://www.maths.nottingham.ac.uk/plp/pmzjkl/pg1.pdf).

Consequently, if (2) holds on such a common domain for each member of
some sequence (a_j\downarrow0), the [stationary theta bracket](smoothing.md)
gives

\[
 \limsup_{p\to\infty}
 \left|\log\frac{\vartheta(\overline H_p)}{\sqrt{(p-1)/2}}\right|
       \le\tfrac12\log(1+a_j)\longrightarrow0.             \tag{4}
\]

The domain and rate in (2) may depend on (a_j), since (p\to\infty)
is taken first. This criterion needs neither source UI nor a bound on
the full inverse Hessian. It does need a genuinely new **prime** complex
estimate; finite-dimensional real analyticity supplies none of (2).

## 2. A quantitative obstruction to a field-general shortcut

At squares (q=r^2), the exact theta value and the same real bracket give
for every fixed (0<a<1)

\[
 \liminf_{r\to\infty}m_{r^2}(a)
       \ge\tfrac12\log\frac2{1+a}>0.                     \tag{5}
\]

Thus the holomorphic extension and subpolynomial-growth assumptions
cannot both hold on the same (D) through these square fields.
More precisely, choose a positive (delta) smaller than the right side
of (5). If the extensions do exist, rearranging the two-constants bound
gives eventually

\[
 \boxed{M_{r^2}\ge
  \delta^{1/(1-\omega_a)}
       (\sqrt q/6)^{\omega_a/(1-\omega_a)}.}               \tag{6}
\]

Either the real branch cannot extend over the proposed domain, or its
complex size grows at least as a fixed positive power of the field size.
This is a statement about the actual square stationary family, using
the already proved real bounds. It does not locate its branch points,
assert a particular limiting phase-transition formula, or prove a complex
singularity for any individual square field.

In particular a proof claiming uniform holomorphic control solely from
positive floor, real leverage bounds and coherence would contradict
(5)--(6). A successful continuation argument must use additional prime
structure, just as the UI/response route must.

## 3. Exact stationary equation at prime 13

In the standard cyclic coordinates, the actual multiplier is

\[
 s=(0,1,-1,-1,-1,1),\qquad n=6.
\]

The even plus sector has dimension one. A mean-one spectrum in that
sector is exactly

\[
 u_i=1+x\cos(\pi i/3).
\]

Strict positivity means (-1<x<1). Its logarithmic central-path objective
is

\[
 \log(1+x)+\frac t6
       [2\log(1+x/2)+2\log(1-x/2)+\log(1-x)] .             \tag{7}
\]

Strict concavity gives one critical point in that interval. Multiplying
its derivative by the nonzero denominators yields

\[
 \boxed{f(x,t)=(6+5t)x^3+(t-6)x^2-(24+8t)x+24-4t=0.}       \tag{8}
\]

The multiplying factors do not introduce an interior real solution.
At (t=6), (x=0), consistent with equal coordinate weights.
The actual marked logarithm is

\[
 m_{13}(t)=\tfrac12\log\frac{1+5t/6}{6}+\log(1+x(t)).     \tag{9}
\]

The exact discriminant of (8) with respect to (x) is

\[
 \operatorname{disc}_x f
  =96(25t^4+1926t^3+2754t^2+1728t+1944).                 \tag{10}
\]

For the quartic in parentheses, the four leading Hurwitz determinants
are, in order,

\[
 1926,\quad5261004,\quad1879793568,\quad3654318696192.
\]

All are positive. The
[Routh--Hurwitz criterion](https://faculty.washington.edu/chx/teaching/fbintro/lec10-routh-hurwitz-stability/)
therefore puts all four discriminant zeros in the open left half-plane.
The leading coefficient of (8) vanishes only at (t=-6/5), also there.
Thus over the simply connected domain (operatorname{Re}t>0), its
three roots are distinct holomorphic branches. The one with (x(6)=0)
agrees with the positive stationary branch on the positive real axis.

Finally (f(-1,t)=36), so (1+x(t)) never vanishes at a finite parameter;
the other logarithm in (9) has its zero only at (t=-6/5). Both logarithms
therefore have holomorphic choices on the right half-plane, fixed by
their real values at six. This proves the promised continuation for
the **one actual finite prime**.

## 4. Replay and what remains

```sh
.venv/bin/python -B research/complex-floor-33.py \
  > research/complex-floor-33-certified.jsonl
```

The seven records contain one exact discriminant/Hurwitz calculation,
one validated complex-root isolation, and five Arb stationary-root checks
at rational floors (1/20,1/5,1,6,20). The latter reconstruct positive
spectra and enclose every coordinate of their fixed-point residual around
zero without a Newton solve or optimizer. These are finite normalization
checks, not evidence of a common domain for growing primes.

The continuation criterion (2) remains entirely unproved through primes.
Its two obligations are a common domain for the actual marked branch
and subpolynomial complex growth there. A bound on the real derivative,
or merely observing no branch switch along finitely many numerical paths,
would not discharge either obligation. The existing arithmetic matching
theorems concern fixed trace words, not this stationary complex branch.
