# Unfolding the first nested mixed moment

> Round-32 update: the arithmetic sign left open in this historical note is
> now [uniformly positive](astra-prime-phase-32.md). The
> [full joint law for this family](joint-law-32.md) is also identified.

Round 31, 2026-11-18. The exact nine-variable sum of
[the arithmetic audit](astra-arithmetic-coset-30.md) can be reorganized
using two complex full-character fields. This note proves the finite
alias identities and reduces the cubic target to specified correlations.
The new rank-three proof is recorded and audited separately; the numerical
diagnostics do not prove its group statements. The prime arithmetic sign
and Problem 26 remain open.

## 1. Full group and Fourier convention

Let \(G=\mathbb F_q^\times\), \(Q=G^2\), \(N=q-1=2n\), with
\(q\equiv1\pmod4\). Use unnormalized forward Fourier transforms
\(F_G,F_Q\). Put \(s(a)=\chi(1-a)\), and on full-character arrays define

\[
\mathcal K=F_G\operatorname{diag}(s)F_G^{-1},\quad
J=F_Gs/\sqrt q,\quad V=\mathcal K(J^2),\quad
R=\mathcal K(JV).
\]

These are raw full Mellin fields, with exceptional characters retained.
Let \(\mathcal S\) denote the frequency shift by the quadratic character,
and write \(R^\chi=\mathcal S R\). Full arrays can be complex. In code,
\(\mathcal K f\) is `fft(s*ifft(f))`; discarding its imaginary part, or
using the real square-subgroup convention without checking inversion,
would change these fields.

Since \(s(a^{-1})=\chi(a)s(a)\),

\[
J^\chi=\overline J,
\qquad \overline{\mathcal K f}=\mathcal S\mathcal K\overline f.
\tag{1}
\]

Also \(V\) is real: its positional function is
\(s(s*s)/q\), invariant under inversion. Here convolution on \(G\)
uses counting measure. This is the already-known twisted-Legendre trace,
and \(|V|\le2\) at all characters. No new group identification is
needed for this input.

## 2. Exact square-subgroup aliases

On \(\widehat Q\), use the original fields

\[
x=F_Q(s|_Q)/\sqrt n,\quad y=K(x^2),\quad z=K(xy).
\]

For a lift \(\psi\) of a character of \(Q\), restriction gives
\(F_Q(f|_Q)=(F_Gf(\psi)+F_Gf(\psi\chi))/2\). Consequently, writing
the values at one lift without changing their names,

\[
\boxed{\begin{aligned}
x&=a\operatorname{Re}J,& a&=\sqrt{q/n},\\
y&=\frac q{4n}(V+V^\chi)-\frac{x}{\sqrt n},\\
z&=b\operatorname{Re}(R+R^\chi)-\frac y{\sqrt n},&
b&=\sqrt{q/n}\,\frac q{4n}.
\end{aligned}} \tag{2}
\]

These hold at every character, including the trivial character.

For the second line, expand the square-subgroup indicator in its
convolution. At \(a_0\in Q\setminus\{1\}\),

\[
(s|_Q*s|_Q)(a_0)=\tfrac12\{(s*s)(a_0)-2\}.
\]

The extra sum is
\(\sum_{b\ne0}\chi((1-b)(b-a_0))=-2\): the complete quadratic sum
is \(-1\), and the removed \(b=0\) term equals one. At \(a_0=1\)
the formula differs, but multiplication by \(s(1)=0\) removes it.
Fourier transformation proves the second line exactly.

For the third line, multiply the first two. The four full products
are \(JV,JV^\chi,J^\chi V,J^\chi V^\chi\). Applying (1), using real
\(V\), turns their \(\mathcal K\)-images into
\(R,\overline R,R^\chi,\overline{R^\chi}\). The correction term is
\(-K(x^2)/\sqrt n=-y/\sqrt n\). This proves (2) with its normalization.

## 3. The remaining cubic correlations

All means in this section are over the full \(N\) characters, with no
exceptions deleted. Put

\[
C=\mathbb E_G[\operatorname{Re}J(\operatorname{Re}R)^3],\qquad
D=\mathbb E_G[\operatorname{Re}J(\operatorname{Re}R)^2
                              \operatorname{Re}R^\chi].
\]

The shift preserves \(\operatorname{Re}J\) and exchanges \(R,R^\chi\).
Thus (2) gives

\[
\mathbb E_Q\!\left[x\left(z+\frac y{\sqrt n}\right)^3\right]
=ab^3(2C+6D). \tag{3}
\]

Since \(|x|<2\), \(|y|\le(q+\sqrt q)/n\le4\), and
\(\|z\|_{2,n}\le\|x\|_\infty\|y\|_{2,n}<4\), expansion of the
cube also proves

\[
\mathbb E_Q[xz^3]=ab^3(2C+6D)+O(n^{-1/2}),\qquad
ab^3\longrightarrow\tfrac12. \tag{4}
\]

This error estimate uses the known low-order bounds and \(L^2\)
contraction only, rather than a proposed group for \(R\).

Finally define

\[
T_3=\mathbb E_G[\overline J R^3],\quad
T'_3=\mathbb E_G[J R^3],\quad
T_{21}=\mathbb E_G[(J+\overline J)R^2\overline R].
\]

Expansion and conjugation give the exact relation

\[
C=\tfrac18\operatorname{Re}(T_3+T'_3)
                      +\tfrac38\operatorname{Re}T_{21}. \tag{5}
\]

Equations (3)--(5) isolate the proposed determinant correlation
\(T_3\) from the other correlations that must be bounded. No limit
for any of these new correlations follows from the first-feedback law.

## 4. What the independent rank-three calculation settles

The [independent nested calculation](astra-nested-moment-31.md) identifies
a pure reflected hypergeometric field \(A\) of convolution dimension
three. The raw full field here satisfies exactly
\(R_\alpha=A_{\alpha^{-1}}+J_\alpha/q\). Its proof establishes independent
derived \(SL_3\) factors for the pure field and its quadratic twist,
including their relation to the old Jacobi and Legendre factors. The
small correction does not alter the leading moments. In this normalization,
writing \(\alpha_q\) for the conjugate determinant phase, the invariant
calculation gives

\[
T_3=\alpha_q+O(q^{-1/2}),\quad
T'_3,T_{21},D=O(q^{-1/2}),
\]

and (4)--(5) give

\[
\mathbb E_Q[xz^3]=\tfrac18\operatorname{Re}\alpha_q
                                      +O(q^{-1/2}). \tag{6}
\]

The additional all-extension reality argument in that note proves
\(\alpha_q\in\{1,-1\}\), and \(\alpha_{r^2}=1\) for every odd base
field. It uses the full real character contraction at every extension
degree, not a conjectured rational decomposition of its highest-weight
part. Consequently the square cubic main term is \(1/8\). The prime
sign has not been selected. The same audited calculation proves
\(\langle x^2z^2\rangle=1/2+O(q^{-1/2})\) and
\(\langle z^4\rangle=3/4+O(q^{-1/2})\) on both prime and square orders.
Geometric determinant identification and finite probes alone would not
have justified removing that arithmetic sign.

## 5. Replay scope

The [script](nested-lift-31.py) checks four small-field subgroup
convolution identities with integer arithmetic. Its five complex-field
diagnostics at primes 401, 9413, 153649 and squares \(97^2,389^2\)
test all aliases, the finite cubic reduction, and the specified full
mixed correlations. Floating identities agree within \(6\cdot10^{-15}\)
in the recorded run; they are not interval certificates or monodromy
computations. Some displayed cubic correlations omit only the two
special characters; the `cubic_reduction` fields explicitly use all
characters as required in (3)--(5).

At \(p=153649\), the good-character diagnostics give
\(\mathbb E[\overline J R^3]\approx0.99920\),
\(\mathbb E[J R^3]\approx-0.00761\), and
\(\mathbb E|R|^4\approx2.00124\). These suggest a determinant-coupled
unitary model; no such model is concluded from the measurements.

The [independent audit](parallel-audit-31.md) checks the exact lift and
the separately supplied rank-three theorem. The [acceptance record](nested-lift-31-acceptance.json)
distinguishes exact identities, theoretical constructions, floating checks
and finite arithmetic sign certificates.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/nested-lift-31.py > research/nested-lift-31-check.jsonl
```
