# Exact finite certificates for the nested arithmetic sign

> Round-32 update: the [uniform arithmetic calculation](astra-prime-phase-32.md)
> now proves the positive sign over all odd finite fields. These finite
> certificates remain independent normalization checks, not the uniform proof.

Round 31, 2026-11-18. The [rank-three theorem](astra-nested-moment-31.md)
proves that the remaining determinant phase \(c_q\) is a sign. This note
selects \(c_p=+1\) rigorously at two stated primes. It does not select
the sign at every prime, and it does not prove Problem 26.

## 1. A rational full-character contraction

Use the full multiplicative group \(G\), of size \(N=q-1\), and its
integer sign array \(s\). Convolutions below are cyclic counting
convolutions. Define

\[
U=s\cdot\bigl(s*(s\cdot(s*s))\bigr),\qquad
r(a)=U(a^{-1})-s(a^{-1}).
\]

The exact Pfaff identity in the rank-three note identifies this \(r\)
with its pure reflected hypergeometric positional array. Thus

\[
J=F_Gs/\sqrt q,\quad A=F_Gr/q^{3/2},\qquad
T_q=\mathbb E_{\widehat G}[A^3J]
=\frac{(r*r*r*s)(1)}{q^5}. \tag{1}
\]

No special characters are omitted. The four perverse-trace minus signs
cancel, so the unique geometric invariant of
\(\mathcal R^{\otimes3}\otimes\mathcal M\) contributes \(c_q\),
with this orientation. Equation (1) is an exact rational number.

The [checker](nested-phase-31.py) computes all convolutions as integer
polynomial products modulo \(X^N-1\), using FLINT. It obtains the numerator
as the zero coefficient of two paired products, without a floating FFT,
stationary solve, or numerical optimizer. At the small control prime it
also checks the products by direct Python-integer cyclic convolution.

## 2. An explicit error enclosure

The rank-three object has convolution dimension and generic rank three;
the Jacobi object has dimension and rank one. The inherited generic-rank
bound \(r(M*N)\le r(M)d(N)+d(M)r(N)\) gives

\[
r(\mathcal R^2)\le18,\quad
r(\mathcal R^3)\le81,\quad
r(\mathcal R^3\mathcal M)\le108,
\qquad d(\mathcal R^3\mathcal M)=27.
\]

The all-character mean of the word trace is its trace at one. Its
nonpunctual stalk has dimension at most 108 and weights at most minus
one, so the difference from \(c_q\) is at most \(108/\sqrt q\).
For the product-versus-word replacement, allow conservatively 20 bad
characters, twice the sum of the four input ranks. At each, both the
product trace and the word trace have absolute value at most 27, by
the all-character dimension bound. Consequently

\[
\boxed{\quad
|T_q-c_q|\le B_q:=\frac{108}{\sqrt q}+\frac{1080}{q-1}.
\quad} \tag{2}
\]

These are deliberately conservative constants; no numerical fit enters
(2). The rank and all-character inputs are the same cited Mellin lemmas
used in the [fixed-width audit](parallel-fixed-width-13.md).

Since \(c_q\in\{1,-1\}\), a certified positive gap

\[
T_q+1-B_q>0 \tag{3}
\]

excludes \(-1\). Arb at 160 bits encloses only the elementary square root
and rational subtraction in (2)--(3); the large convolution coefficient
is already an exact integer.

## 3. Accepted finite signs

The [three replay records](nested-phase-31-certified.jsonl) give:

| Prime | Exact \(T_p\) | Outward lower bound for the gap | Result |
|---:|---|---:|---|
| 13 | \(224331/371293\) | negative | No sign selected by this bound |
| 9413 | \(73859407377179529891/73899294693571938293\) | 0.77154 | \(c_p=+1\) |
| 153649 | \(85565001652314817932485663/85634485014532191720043249\) | 1.71663 | \(c_p=+1\) |

The last two primes have opposite values of \(\chi_p(2)\). This supplies
two exact arithmetic checks, not a proof that the sign depends on no
other data. No common global rank-one model, ramification bound or
Dirichlet-character description is assumed here. Establishing such
structure, or an exact determinant normalization, is still needed to
select the sign uniformly through primes.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/nested-phase-31.py > research/nested-phase-31-certified.jsonl
```
