# What transfers a square-root-size source tail

Round 30, 2026-11-18. This supplies a deterministic stability theorem for the
terminal-source test of [round 29](astra-source-window-29.md). It also states
precisely how a compact-group approximation would turn that tail into a
coset extremum. It proves no prime/square arithmetic matching and no prime
tail estimate. The distinction matters: weak convergence, even with bounded
arrays, does not determine this vanishing-fraction tail.

## 1. Fractional top sums and the exact norm loss

For a real array \(y\in\mathbb R^N\) and \(0\le k\le N\), use

\[
\operatorname{Top}_k(y)=
\max_{0\le\lambda_i\le1,\ \sum_i\lambda_i=k}
\sum_i\lambda_i y_i.
\]

This includes negative entries and uses linear interpolation at a
nonintegral capacity. For \(1\le p\le\infty\), Hölder gives

\[
|\operatorname{Top}_k(y)-\operatorname{Top}_k(z)|
\le k^{1-1/p}\|y-z\|_p. \tag{1}
\]

For finite \(p\), the dual weight obeys
\(\sum_i\lambda_i^{p/(p-1)}\le k\); the endpoints follow directly.
This proves (1) without assumptions on either array's signs.

Write \(g=G/\sqrt n\), \(f=F/\sqrt n\), let the bulk contain \(n-1\)
entries, and use normalized norms with divisor \(n\). Then

\[
|\operatorname{Top}_{k_n}(g)-\operatorname{Top}_{k_n}(f)|
\le k_n^{1-1/p}n^{1/p-1/2}
\|G-F\|_{p,n}. \tag{2}
\]

In particular, when \(k_n/\sqrt n\to\kappa>0\), the normalized \(L^2\)
loss is \(\sqrt{k_n}\sim\sqrt\kappa\,n^{1/4}\), rather than a constant.
Thus normalized \(L^2\) error \(o(1)\) alone does not transfer the source
top mass. Error \(o(n^{-1/4})\) suffices. For a growing depth \(T_n\),
the weaker target of an \(o(T_n)\) error needs
\(\|G-F\|_{2,n}=o(T_n n^{-1/4})\).

An exceptional error bounded in counting \(\ell_1\) is inexpensive:
\(\|G-F\|_1\le C\) gives top-mass error at most \(C/\sqrt n\).
A uniform pointwise error \(\epsilon\) gives at most
\((k_n/\sqrt n)\epsilon\). These estimates explain why an approximation
with controlled exceptional characters differs materially from an
unquantified normalized \(L^2\) approximation.

The exponent is sharp. Set \(n=s^2\), \(k=s\), \(F=0\), and let \(G\)
equal one on \(s\) bulk coordinates and zero elsewhere. Then

\[
\|G-F\|_{2,n}=n^{-1/4},\qquad
\operatorname{Top}_{\sqrt n}(G/\sqrt n)=1.
\]

The arrays are uniformly bounded and their empirical laws converge to
\(\delta_0\), yet the top mass stays one. This is an abstract array example,
not an actual Paley trajectory. It also disproves an inference from weak
convergence plus boundedness to vanishing square-root-size top mass.

## 2. A finite near-maximum sampling lemma

Suppose a bulk array \(G_n\) is bounded by \(B\) in absolute value. Outside
a set \(E_n\) of size at most \(N_0\), it approximates sampled values
\(F_n(\xi_i)\) within \(\epsilon\). Suppose

* \(F_n\le M_n\) on its whole sampling domain, with \(|M_n|\le B_0\);
* at least \(\delta n\) indices outside \(E_n\) have
  \(F_n(\xi_i)\ge M_n-\epsilon\).

If \(k_n\le\delta n\), choosing those near-maximum entries and bounding
the exceptional contribution proves

\[
\frac{k_n}{\sqrt n}(M_n-2\epsilon)
\le\operatorname{Top}_{k_n}(G_n/\sqrt n)
\le\frac{k_n}{\sqrt n}(M_n+\epsilon)
 +\frac{N_0(B+B_0+\epsilon)}{\sqrt n}. \tag{3}
\]

The near-maximum sampling hypothesis is essential. A continuous function
on a compact coset has a positive Haar fraction near its maximum. To use
(3) for character rows, one must additionally establish that their empirical
cutoff mean samples that fraction. Compactness by itself is not such an
arithmetic sampling theorem.

The compact-group approximation and cutoff-mean sampling asserted in the
[uniform fixed-depth draft](uniform-fixed-depth.md) have exactly this form,
with constants depending on fixed depth, floor and tolerance. Conditional
on those draft inputs, (3) identifies the fixed-depth top mass with the
appropriate **field's own** coset maximum, up to arbitrarily small errors.
It does not identify the cosets at different fields. In particular it
does not identify prime and square extrema.

For the terminal source of round 29,

\[
G_{n,T}=\sqrt n\,\widehat g_T,\qquad
\frac{k_n}{\sqrt n}\longrightarrow
\kappa_\tau=\sqrt{1+\tau}-\sqrt\tau>0.
\]

At fixed depth its bulk activation is a continuous even function of the
scaled iterate. The map
\(y\mapsto\sqrt{y^2+4\tau}-2\sqrt\tau\) is 1-Lipschitz, so a uniform
approximation with bounded exceptions passes to this source. A finite
geometric combination, at fixed relaxation and horizon, preserves that
property. Thus the draft's machinery applies if its approximation and
sampling inputs are valid. The source tail can suppress boundedly many
exceptional frequencies that would affect an ordinary maximum.

## 3. The local top seminorm is not stable under the reflection

Let \(\mathcal N_k(e)=\operatorname{Top}_k(|e_{\rm bulk}|)\). Replacing a
sup norm by this seminorm in a repeated nonlinear iteration needs an
additional propagation argument. There is no dimension-independent bound
\(\mathcal N_k(Ke)\le C\mathcal N_k(e)\), even for coherent reflections.

More precisely, suppose \(K=K^T\), \(K^2=I-J\), \(K\mathbf1=0\), and
\(|K_{ij}|\le\mu/\sqrt n\). For an integer \(1\le k\le n/2\), choose a
set of \(k\) nonroot indices and put independent random signs on it,
zero elsewhere, obtaining \(y\). Hoeffding's inequality and a union bound
give a realization for which

\[
\|Ky\|_\infty\le\mu\sqrt{2k\log(4n)/n}.
\]

Indeed each row has coefficient square sum at most \(\mu^2k/n\), so the
probability that any of the \(n\) rows exceeds this threshold is at most
\(1/2\). Put \(e=Ky\). Then \(Ke=(I-J)y\), and at each support index
\(|(Ke)_i|\ge1-k/n\). Therefore

\[
\frac{\mathcal N_k(Ke)}{\mathcal N_k(e)}
\ge\frac{1-k/n}{\mu\sqrt{2k\log(4n)/n}}. \tag{4}
\]

If \(K\) commutes with inversion, the same example can be made inversion
even when \(k\) is even and \(k/2\) nontrivial nonroot inverse pairs are
available: choose those pairs and use a common sign within
each pair. The row coefficient square sum is then at most
\(2\mu^2k/n\), and the denominator in (4) is replaced by
\(2\mu\sqrt{k\log(4n)/n}\). Both \(e\) and \(Ke\) have mean zero.
For \(k\asymp\sqrt n\), the lower bound grows as
\(n^{1/4}/\sqrt{\log n}\). Paley multipliers satisfy these hypotheses
with a fixed coherence constant, as do the square controls.

This is an exact existence argument about propagation of unrestricted
errors, not a construction of an error produced by the actual activation
or a counterexample to any Paley orbit estimate. It rules out a generic
norm-closure shortcut. Extra structure of the actual approximation errors
could still permit a useful local bound.

## 4. Conditional arithmetic transfer, stated without identifying groups

There is a useful consequence if the missing arithmetic input can be
established. Fix \(\tau,\rho\). For every sufficiently large fixed \(T\),
assume the compact approximation and sampling above on the square controls.
The proved square lower bound of round 29 says

\[
\liminf_{r\to\infty}\operatorname{Top}_{k_n}
(\widehat g_{T,\mathrm{bulk}})
\ge a_\tau\rho T-b_\tau\beta_T,
\quad a_\tau=c_\tau/C_\tau>0.
\tag{5}
\]

For any \(L<a_\tau\rho T-b_\tau\beta_T\), (3) forces the square coset
maximum above \(L/\kappa_\tau\), up to a chosen small tolerance. Uniform
Lipschitz/packing bounds and the draft's cutoff sampling then give a
positive, possibly very small, fraction of square bulk rows above a
slightly lower threshold.

**Additional premise.** Along an infinite prime subsequence the cutoff
means for that finite approximation and threshold match those square
means, to an error smaller than this positive fraction. This must hold
simultaneously for the expressions used in that cutoff. No equality of
cross-field compact groups is assumed; this is precisely a scalar
arithmetic-mean matching requirement.

Under that premise the prime rows also have a positive fraction above the
threshold. Since \(k_n=o(n)\), their top mass has the same lower bound
after the prime limit. Letting the tolerances decrease gives

\[
\limsup_{p\to\infty}\operatorname{Top}_{k_n}
(\widehat g_{T,\mathrm{bulk}})
\ge a_\tau\rho T-b_\tau\beta_T. \tag{6}
\]

If the additional matching premise holds for **every sufficiently large
fixed depth**, (6) contradicts the sublinear \(\liminf_T\) prime criterion
in round 29. Matching at merely an unbounded sequence of depths would
not alone refute that \(\liminf_T\) condition. Prime subsequences may
depend on depth; no single prime sequence uniform in growing depth is
needed for this conditional conclusion.

Neither the matching premise nor a common prime/square law is proved
here. Finite quadratic-residue patterns alone have not been shown to
control every required arithmetic invariant trace. Accordingly this note
does **not** refute the prime criterion. It identifies an exact dependency
that the independent arithmetic-coset investigation must resolve.

## 5. Verification and research consequence

The [replay script](top-tail-transfer-30.py) checks fractional capacities,
the norm losses in (1), and the bounded-array sharpness example. Its
compact-grid demonstration checks the deterministic near-maximum lemma;
it is not evidence of character equidistribution or arithmetic matching.
Six actual-kernel diagnostics test the arbitrary-error propagation example
on four prime and two square orders; they do not generate nonlinear orbit
errors. No numerical stationary solve is involved.

The [two additional nested-word diagnostics](top-tail-transfer-30-nested-probe.jsonl)
extend Astra's explicit arithmetic test, using its existing `diag` function:

| Order | mean \(x^2z^2\) | mean \(z^4\) | mean \(xz^3\) |
|---|---:|---:|---:|
| \(1000033\) | 0.49983783 | 0.74663235 | 0.12488283 |
| \(997^2\) | 0.50586153 | 0.77070787 | 0.13353346 |

These are floating evaluations of \(z=K(xK(x^2))\), not proofs of limits,
of a persistent gap, or of finite-Artin invariants. They specify a concrete
next arithmetic test beyond the reused first-feedback law.

The immediate practical consequence is an error budget: a normalized
\(L^2\) approximation must pay the \(n^{1/4}\) top-tail loss, whereas
bounded exceptional \(\ell_1\) error or a fixed-accuracy sup approximation
does not. This is relevant to the growing-depth calculation, not a
substitute for the actual prime source estimate required by Problem 26.
The [independent audit](parallel-audit-30.md) checks the proofs and their
scope. The [acceptance record](top-tail-transfer-30-acceptance.json) records
the separate replays and unresolved arithmetic inputs.
