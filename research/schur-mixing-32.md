# Squared-kernel mixing does not control the reciprocal source tail

Round 32. Ordinary theta, ETH Problem 26. All norms below are counting norms.

The actual Paley reflection has an almost perfectly mixing squared-entry
kernel: its nonconstant eigenvalues are (O(q^{-1/2})). Equivalently, the
Hadamard product of its opposite sector projectors has gap

\[
 \frac14+O(q^{-1/2}).
\]

This looks promising for a source-tail argument, but is insufficient even
when added to all the coherent stationary hypotheses of round 31. A bounded
rank change between uniformly coherent reflections changes this squared
kernel by only (O(n^{-1/2})) in operator norm. Consequently the exact
stationary UI counterfamily of [round 31](parallel-coherent-source-31.md)
also has the same limiting gap, despite positive inverse source mass escaping
to zero. It is still **not a Paley counterexample**: its signed entries lose
cyclic convolution. This observation excludes a proposed additional input;
it supplies no bound on the actual Paley leakage.

The final section identifies an actual source first-moment correlation with
the square of the Jacobi seed. Finite prime diagnostics improve the generic
retained-mass lower bound to approximately .82, but leave a positive deficit.
They do not prove inverse tightness or an asymptotic constant.

## 1. Exact spectrum of the cross-projector Hadamard product

Use (q=2n+1\equiv1\pmod4), (s(a)=\chi(1-a)) on the nonzero squares
(Q), and (K=F\operatorname{diag}(s)F^{-1}). Write

\[
 P=I-J,\quad P_\pm=(P\pm K)/2,\quad
 k=Ke_0,\quad H=P_+\circ P_- .                         \tag{1}
\]

The symbol (\circ) means entrywise product, not operator composition.
Since (P_+P_-=0), (H\mathbf1=0). The Schur product theorem gives
(H\succeq0). In cyclic coordinates its Fourier eigenvalue at (a\in Q)
is exactly

\[
 \lambda_H(a)=\frac1n
     (\mathbf1_{s=+1}*\mathbf1_{s=-1})(a).                \tag{2}
\]

Here convolution is unnormalized on (Q). Put (h=s*s). Since
(\mathbf1_{s=+1}+\mathbf1_{s=-1}=\mathbf1-\delta_1),

\[
 4(\mathbf1_{s=+1}*\mathbf1_{s=-1})
       =(n-2)\mathbf1+\delta_1-h.                       \tag{3}
\]

At (1), (h(1)=n-1), so the eigenvalue is zero. Off (1), the exact
quadratic-character completion from [round 31](astra-nested-moment-31.md)
gives

\[
 h(a)=\frac{L(a)-2}{2},\qquad
 L(a)=\sum_{v\in\mathbb F_q}\chi(v(v-1)(v-a)).
\]

Thus for every nonconstant Fourier mode

\[
 \boxed{\lambda_H(a)=\frac{q-3-L(a)}{4(q-1)}}.             \tag{4}
\]

The cubic is squarefree for (a\ne0,1). The Hasse bound
(|L(a)|\le2\sqrt q) proves

\[
 \left\|H-\tfrac14P\right\|_{\rm op}
       \le\frac{1+\sqrt q}{2(q-1)}.                     \tag{5}
\]

This is uniform over prime powers and has no prime-versus-square gap.

Equivalently, put (S=K\circ K). Its row sum is (1-1/n), and its
nonconstant Fourier eigenvalues are

\[
 \lambda_S(a)=\frac{h(a)}n=\frac{L(a)-2}{q-1}.
\]

Therefore

\[
 \left\|S-(1-1/n)J\right\|_{\rm op}
       \le\frac{2\sqrt q+2}{q-1}.                       \tag{6}
\]

The normalized nonnegative matrix (S/(1-1/n)) is a symmetric Markov
kernel with this strong mixing property. A further exact interpretation,
for a real vector (f), is

\[
 \|P_-\operatorname{diag}(f)P_+\|_{\rm HS}^2
       =f^{\mathsf T}Hf .                              \tag{7}
\]

In particular a constant-order cross-block Poincare inequality is available
for (f=\log A) as for any other vector. The missing step would be a
source-dependent estimate of the left side; stationarity does not bound it
by a vanishing quantity merely from (5).

## 2. Stability under the coherent finite-rank implantation

Let (K_0,K_1) be real symmetric reflections on (\mathbf1^\perp),
annihilating constants, with

\[
 |(K_i)_{ab}|\le C_i/\sqrt n,\quad
 \operatorname{rank}(K_1-K_0)\le r.
\]

Since each reflection has operator norm at most one,
(\|K_1-K_0\|_{\rm HS}\le2\sqrt r). Entrywise factorization gives

\[
 \begin{split}
 \|(K_1\circ K_1)-(K_0\circ K_0)\|_{\rm op}
 &\le\|(K_1-K_0)\circ(K_1+K_0)\|_{\rm HS}\\
 &\le\frac{C_0+C_1}{\sqrt n}\|K_1-K_0\|_{\rm HS}\\
 &\le2(C_0+C_1)\sqrt{r/n}.                             \tag{8}
 \end{split}
\]

Both squared-entry matrices have row sum (1-1/n), so the comparison
also acts on (\mathbf1^\perp). The associated cross-projector products
satisfy the exact identity

\[
 H_1-H_0=-\tfrac14
       [(K_1\circ K_1)-(K_0\circ K_0)].                  \tag{9}
\]

It follows that the prime-seeded stationary family of round 31, with
(r\le12) and (C_1=C_\tau<\infty), satisfies

\[
 \|H_1-\tfrac14P\|_{\rm op}=O_\tau(n^{-1/2}),\qquad
 \|(K_1\circ K_1)-(1-1/n)J\|_{\rm op}
       =O_\tau(n^{-1/2}).                              \tag{10}
\]

All its reciprocal, UI and escaping-source conclusions therefore coexist
with (10). This application uses the asymptotic existence proof of that
family, not a claim that the current script builds its enormous matrices.
The auxiliary finite conjugation tests below check (8)--(9) separately.

Thus squared-entry mixing, the gap in (5), and the unweighted Poincare
inequality (7) cannot by themselves close UI-to-inverse-tightness. A useful
prime argument must retain additional structure of the signed convolution
and its actual reciprocal spectra.

## 3. What the actual marked first moment sees

Use the stationary conventions of [round 29](parallel-source-pair-29.md):

\[
 c=\tau/n,\quad W=1+(n-1)c,\quad a=\sqrt{W/n},\quad
 A=a\mathbf1+x\in a\mathbf1+V_\sigma,\quad
 B=a\mathbf1+y\in a\mathbf1+V_{-\sigma},\quad AB=w.
\]

Set (D=\operatorname{diag}(c/(aA))),
(T=P_\sigma D P_\sigma|_{V_\sigma}), (e=P_\sigma e_0),
(b=(1-c)/A_0), (Q=(1-c)(1-a/A_0)), and
(p_\sigma=e_0^{\mathsf T}P_\sigma e_0=(1-(1+\sigma)/n)/2).
The marked measure (\mu) of (T) has mass (p_\sigma),
(d\nu=b^2\lambda^{-1}d\mu), and (\nu((0,\infty))=Q).
Its first ordinary spectral moment has the exact formula

\[
 \begin{split}
 M_1:=\langle e,De\rangle
  ={}&\frac14-\frac1{2n}
    +\frac{B_0}{a}
       \left\{\frac1{2n}-\frac{1+\sigma}{2n^2}
                         +cp_\sigma^2\right\}\\
    &+\frac1{4a}\langle B-a\mathbf1,k^2\rangle .          \tag{11}
 \end{split}
\]

To check every root term, use (D=B/a-(b/a)\operatorname{diag}(e_0))
and (e=(e_0-\mathbf1/n+\sigma k)/2). Entrywise squaring and projecting
onto (V_{-\sigma}) gives

\[
 P_{-\sigma}(e^2)
   =\tfrac14(1-2\sigma/n)P_{-\sigma}e_0
                       +\tfrac14P_{-\sigma}(k^2).
\]

Substitution yields (11). In scaled seed notation (X=\sqrt n\,k) and
(Y=\sqrt n(B-a\mathbf1)), its last term is
(\mathbb E(YX^2)/(4\sqrt W)). The known pointwise root caps make the
explicit root correction (O_\tau(n^{-1/2})). It is the correlation with
the **actual stationary** opposite spectrum that remains, rather than a
known fixed-depth moment.

Cauchy--Schwarz on (\mu|_{(\epsilon,\infty)}) gives

\[
 \nu((\epsilon,\infty))\ge
 \frac{b^2}{M_1}
       \left(p_\sigma-\frac{\epsilon Q}{b^2}\right)_+^2. \tag{12}
\]

Indeed (\mu((0,\epsilon])\le\epsilon Q/b^2) and
((\int d\mu)^2\le(\int\lambda d\mu)(\int\lambda^{-1}d\mu))
on the retained range. Formula (11) can sharpen the generic coherence
substitute for (M_1), but (12) forces all mass to remain only if its
limiting lower bound reaches (Q). No such equality is proved here.

At floor (\tau=.05), the floating records give:

| field | sign | (M_1) | (b^2p_\sigma^2/M_1) | (Q) |
|---|---:|---:|---:|---:|
| (9413) | + | .3043994 | .8199090 | .9850585 |
| (153649) | + | .3059806 | .8189983 | .9962979 |
| (1000033) | + | .3040610 | .8208339 | .9985520 |
| (1000033) | − | .3048181 | .8215228 | .9985496 |
| (389^2) | + | .2813563 | .4687427 | .9972935 |
| (389^2) | − | .4792117 | .9888656 | .9948704 |

Even in these finite prime diagnostics the first-moment bound allows a
deficit of approximately .18. Strong squared-kernel mixing does not
remove the unknown correlation in (11).

## 4. Reproduction and scope

Run from the project root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/schur-mixing-32.py > research/schur-mixing-32-check.jsonl
```

There are 20 records: six exact integer cyclic-convolution audits (four
also compare every nontrivial mode against a direct prime-field Legendre
sum), twelve actual stationary floating diagnostics, and two auxiliary
finite-rank floating comparisons. The integer rows also contain separately
labelled FFT errors; the exact statements do not depend on their rounding.
The finite conjugations are not claimed to be the stationary UI family.
All asymptotic statements (4)--(12) are mathematical deductions above,
not conclusions extrapolated from the records. No Lean verification and
no solution of Problem 26 are claimed.
