# Independent audit of the root-preserving signed-tail certificate

Round 29, 2026-11-18. This audits the proposed refinement of
[the signed source-tail certificate](source-tail-28.md) and
[its new replay checker](root-coupled-tail-29.py). The two quadratic
inequalities, outward cost rounding, and implemented branch enclosures
are valid. Three small saved inputs replayed exactly. The result is a
finite certificate and an alternative sufficient root-localization
criterion. A strict asymptotic improvement for actual Paley trials is
not proved.

## Exact derivation with the root retained

Use the conventions of the source-tail note:
\(n=(q-1)/2\), \(h=\tau/n<1\), \(W=1+(n-1)h\),
\(a=2\sqrt h\), and
\(\mathcal B=2\sqrt{nW}-na\). For a real trial \(z\), put

$$\phi=\Phi(z),\quad b=(I-J)\phi-Kz,\quad
E=2\sqrt W\sum_i\phi_i/\sqrt n-4W.$$

The exact stationary complementary pair has
\(A_0B_0=1\). Write

$$x=A_0=e^{\gamma_0},\qquad
s=x+x^{-1},\qquad v_0^*=x-x^{-1},\qquad
x\in[C^{-1},C],\quad C=(1+\sqrt q)\sqrt{W/n}.$$

The bulk pair products equal \(h\), and the translation argument
gives \(A_i\le A_0\), \(B_i\le B_0\). Maximizing
\(y+h/y\) on \([hx,x]\) therefore gives

$$M(x)=\begin{cases}x+h/x,&x\ge1,\\x^{-1}+hx,&x\le1.\end{cases}$$

For any real threshold \(t\), set

$$U=\sum_{i\ne0}(b_i-t)_+,\quad m=b_0-t,\quad
T=t\mathcal B-a(m+U).$$

Removing the true zero-sum baseline before estimating the bulk gives
the same signed support bound as before, now at the actual root:

$$\Delta=E+\langle b,u^*\rangle
\le H(x):=E+m(x+x^{-1})+UM(x)+T.$$

The exact full hyperbolic discrepancy is a sum of nonnegative
coordinate discrepancies. Its root term alone is

$$\Delta\ge d_0(x):=(\phi_0-z_0)x+(\phi_0+z_0)x^{-1}-4.$$

Consequently \(d_0(x)\le H(x)\). Multiplying by the positive
number \(x\) proves the proposed inequalities

$$A_+x^2-Rx+B_+\le0\quad(x\ge1),$$

$$A_+=\phi_0-z_0-m-U,\quad
B_+=\phi_0+z_0-m-hU,$$

and

$$A_-x^2-Rx+B_-\le0\quad(x\le1),$$

$$A_-=\phi_0-z_0-m-hU,\quad
B_-=\phi_0+z_0-m-U,$$

with the common value \(R=4+E+T\). There is no missing factor of
two or four. The inequalities are necessary conditions on the
actual stationary root, not equations asserting that every surviving
root is realized by a stationary solution.

Any enclosing interval \([x_-,x_+]\) immediately gives

$$\frac{x_-}{\sqrt W}\le\frac{\theta_+}{\sqrt n}
\le x_+\sqrt W.$$

This retains the usual smoothing-floor loss while avoiding a
maximum over the root before extracting its marker.

## Upward grid rounding remains conservative

Let \(b_0\) increase by \(\delta_0\ge0\), and let the computed
positive bulk excess increase by \(\delta_U\ge0\), with the
threshold fixed. Although \(T\), and hence \(R\), decrease, the
combined quadratic polynomial decreases. Its exact changes are

$$\delta P_+=-\delta_0(x^2-ax+1)
-\delta_U(x^2-ax+h),$$

$$\delta P_-=-\delta_0(x^2-ax+1)
-\delta_U(hx^2-ax+1).$$

Since \(a=2\sqrt h\), these factors are

$$x^2-ax+1=(x-\sqrt h)^2+1-h>0,$$

$$x^2-ax+h=(x-\sqrt h)^2\ge0,\qquad
hx^2-ax+1=(\sqrt h\,x-1)^2\ge0.$$

Thus upward rounding weakens each necessary inequality in the safe
direction. It is unnecessary, and generally incorrect, to demand
that the rounded \(R\) separately be an upper bound for its
unrounded value. The baseline identity \(\sum b=0\) is used for
the true cost before rounding; the rounded cost vector need not
have zero sum.

## Arb branch checker and independent replay

The new checker reconstructs the same exact rational centered trial,
activation and Fourier action as the old checker, rounds every cost
upward on the saved rational grid, and forms the displayed
coefficients at 160-bit Arb precision. The field constructors check
the prime or prime-square premises. The payload checks include the
trial length, integral numerators, evenness, positive scales,
\(0<\tau<1\), and matching field order.

If the leading coefficient is not certified positive, keeping the
whole field half-interval is conservative. If it is positive, the
exact feasible set is between the exact quadratic roots. A certified
negative discriminant excludes the branch. Otherwise the upper
endpoint of the discriminant gives a radical at least as large as
the true radical; interval evaluation then gives an outward lower
bound for the smaller root and upper bound for the larger root.
Clipping these to \([C^{-1},1]\) or \([1,C]\) is safe. The
possibly dependent coefficient errors cause no difficulty: interval
evaluation encloses every exact coefficient value, and for each
fixed positive leading coefficient enlarging the radical moves both
root bounds outward. The implementation handles an uncertain
discriminant by retaining the larger nonnegative radical.

Keeping an entire branch can lose the finite improvement. It is
always legitimate to intersect the result with any independently
valid old marker interval and the field cap. A fair comparison
should apply the field cap to the old interval too; otherwise a
reported improvement can come entirely from that already available
cap. An exact solution of the root-preserving necessary inequalities
is contained in the old global-discrepancy root bound. The checker's
deliberate whole-branch fallback need not preserve this containment.

The independently saved [three-record replay](parallel-root-audit-29-replay.jsonl)
uses \(p=61\), \(\tau=1/20\), and the saved trials at depths
8, 32 and 128. A second invocation was byte-identical, and all three
records equal Main's corresponding saved records. The normalized
theta enclosures, with the following decimal endpoints rounded
outward, are

| Saved trial | Lower | Upper |
|---|---:|---:|
| depth 8 | 0.600435822764 | 1.384199425712 |
| depth 32 | 0.766973743199 | 1.042246757514 |
| depth 128 | 0.872129717140 | 0.919332211391 |

At depth 128 the positive-root half-branch is excluded. These are
certificates for the saved rational trials; no interval tracking of
their distance from exact finite iterates is asserted. No optimizer
or stationary solve was called by this replay.

```sh
.venv/bin/python -B research/root-coupled-tail-29.py \
  research/source-tail-28-q61-tau1_20-t8-input.json \
  research/source-tail-28-q61-tau1_20-t32-input.json \
  research/source-tail-28-q61-tau1_20-t128-input.json \
  > research/parallel-root-audit-29-replay.jsonl
```

## A scalar localization diagnostic

One can expose what the retained root actually buys. Define

$$H_1:=H(1)=E+2m+(1+h)U+T,$$

$$k=\phi_0-m-\frac{1+h}{2}U,\qquad
g=|z_0|+\frac{1-h}{2}U,\qquad d=(H_1)_+.$$

The identity

$$M(x)-(1+h)=\frac{1+h}{2}(s-2)
+\frac{1-h}{2}|x-x^{-1}|$$

and \(\phi_0\ge2\) imply the necessary bound

$$k(s-2)\le H_1+g|x-x^{-1}|
\le d+g|x-x^{-1}|.$$

If \(k>g\), set \(y=|\gamma_0|\), so
\(s-2=2(\cosh y-1)\) and \(|x-x^{-1}|=2\sinh y\). Completing
the hyperbolic cosine gives the explicit valid estimate

$$\boxed{\quad
|\gamma_0|\le
\operatorname{artanh}(g/k)+
\operatorname{arcosh}\!\left(
\frac{k+d/2}{\sqrt{k^2-g^2}}\right).
\quad}$$

In particular \(k\ge\kappa>0\), \(z_0\to0\), \(U\to0\),
and \((H_1)_+\to0\) suffice for marker cancellation. This is a
conditional theorem in directly computable trial quantities, not a
claim that those quantities have the required prime asymptotics.

## Asymptotic scope: formal relaxation versus actual trials

At the level of arbitrary scalar coefficient tuples, retaining the
root can be strictly stronger than making the largest discrepancy
bound vanish. For example, \(z_0=0\), \(U=0\),
\(m=\lambda\in(0,2)\), and \(H_1=0\) give

$$H(x)=\lambda(s-2),\qquad
d_0(x)-H(x)=(2-\lambda)(s-2).$$

The retained-root inequalities force \(x=1\), while
\(\max H=\lambda(C+C^{-1}-2)>0\). This is only an algebraic
relaxation example. No sequence of actual Paley trials realizing
these coefficients is constructed here, so it does not establish a
strict separation of asymptotic Paley criteria.

For the natural late-depth regime there is a useful converse
diagnostic. Suppose along a sequence the field caps stay bounded
and contain a fixed neighborhood of \(x=1\), while
\(z_0\to0\), \(h\to0\), \(m\to0\), and \(U,H_1\) stay
bounded. If the entire nonempty feasible set of the exact
root-preserving inequalities shrinks to \(\{1\}\), then

$$H_1\longrightarrow0,\qquad U\longrightarrow0.$$

To prove this, pass to a convergent coefficient subsequence. If the
limit of \(H_1\) is positive, a fixed neighborhood of 1 is
feasible; if it is negative, a fixed neighborhood is excluded,
contradicting nonempty feasible sets shrinking to 1. Thus its limit
is zero. If the limit of \(U\) is positive, then near
\(\gamma=0\) the limiting difference is

$$d_0-H=2(s-2)-U(e^{|\gamma|}-1)
=-U|\gamma|+O(\gamma^2),$$

which is negative on a nonzero fixed neighborhood on both sides.
That again prevents shrinkage. This argument concerns the necessary
inequality feasible set, not unknown uniqueness of the actual root.

On the compact field interval,

$$H(x)=H_1+m(s-2)+U[M(x)-(1+h)].$$

Consequently the same assumptions imply \(\sup_x|H(x)|\to0\).
In this bounded-coefficient late-depth regime, successful localization
by the full root-preserving feasible set therefore forces the old
global-discrepancy bound to vanish as well. The direct quadratic
method can still improve finite intervals substantially.

Main's fixed-depth normalization agrees with this diagnostic:
for an actual unaveraged Picard trial at depth at least one,
\(b_0\to0\); for the averaged trial at depth \(T\),
\(b_0\to2^{1-T}\). These follow from root cancellation and
\(K^2=I-J\). The fixed-depth uniform bulk bound gives natural
thresholds of size \(O_{T,\tau}(n^{-1/2})\). Thus taking depth
large after the field limit leads naturally to \(m\to0\), where
the preceding caveat applies. Additional trial structure or a
different coefficient regime would be needed for a demonstrated
strict asymptotic gain. No prime signed-tail estimate or solution
of Problem 26 follows from the present acceptance audit.

## Independent audit of Astra's terminal-source window note

The derivations in [Astra's window note](astra-source-window-29.md),
including (3)--(11), (19)--(21), and the sufficient criterion
(22)--(24), are correct with a fixed relaxation \(0<\rho\le1\).
This acceptance concerns the mathematics and stated scope. Main
handles replay of Astra's rational checks and floating diagnostics;
no such diagnostic is treated here as an interval certificate.

### Time telescopes and the scalar reserve

The squared norm identity is

$$\|Ku_t\|_2^2=E_t+4W-S_t^2.$$

The text before (3) calls this the "norm"; it should say "squared
norm." The subsequent formulas use the squared norm correctly.
The relaxed update gives

$$E_{t+1}-E_t=\rho(4W-S_t^2)
-\rho(1-\rho)\|r_t\|_2^2.$$

Subtracting
\(R_t=(1-\rho)\|r_t\|_2^2/2+(S_t-2\sqrt W)^2/2\)
from \((E_t-E_{t+1})/(2\rho)\) indeed leaves exactly
\(2\sqrt W S_t-4W\). The root is included in \(S_t\).

Summation by parts gives both signs in (4). For uniform weights
on \(0,\ldots,T-1\), the negative terminal reserve is
\(-E_T/(2\rho T)\), and the transformed residual is
\(Kz_T/(\rho T)\). A later window has a positive initial energy;
increasing weights have the displayed positive interior energy
terms. None can be silently discarded as a nonpositive reserve.

For Picard, \(g_0=0\) is exactly what removes the initial term in
(6)--(7). For general relaxation, inserting the exact recursion
for \(z_t\) gives the coefficients in (8), and

$$\sum_j\kappa_j=\sum_t\lambda_t(1-\rho)^t.$$

For decreasing weights, replacing every later \(\lambda_t\)
by \(\lambda_j\) in the geometric sum proves (9), including
\(\rho=1\) with its last-index term. Thus the raw activation
combination is nonnegative before centering. For uniform weights,
\(z_T=K\widehat u_T\) gives (10), with the initial activation
and its root value retained. Formula (11) is the standard exact
prefix-mixture identity: telescoping
\(\alpha_k=k(\lambda_{k-1}-\lambda_k)\) gives
\(\alpha_k\ge0\) and \(\sum_k\alpha_k=1\). Its statement
about exact discrepancies does not compare minima of relaxed
support-function bounds.

### Capacity index, root cost and square lower bound

For the common bulk baseline \(a=2\sqrt h\), put
\(B=2\sqrt{nW}-na\), \(d=s-a\), and
\(C_n=C+C^{-1}\). Actual stationary bulk excess has mass
\(B-d\) and entry cap \(d\), since \(u_i^*\le s\).
Its fractional capacity is exactly

$$\frac{B-d}{d}=\frac B{s-a}-1
\le k_n:=\frac B{2-a}-1.$$

The minus one is the root's excess-mass consumption. Since
\(\widehat u_T\ge0\), its fractional top sums are increasing
in the capacity index. The exact baseline identity is

$$\langle P\widehat u_T,u^*\rangle
=\langle\widehat u_T,u^*-a\mathbf1\rangle
-B\overline{\widehat u_T}.$$

Bounding the first term by
\(d[\widehat u_{T,0}+operatorname{Top}_{B/d-1}
(\widehat u_{T,\mathrm{bulk}})]\), then using \(d\le C_n\),
gives the stated estimate. The discarded mean term is nonpositive.
The root term is retained separately; it is not a bulk source
coordinate. Finally

$$\operatorname{Top}_{k_n}(\widehat u_{T,\mathrm{bulk}})
=\operatorname{Top}_{k_n}(\widehat g_{T,\mathrm{bulk}})
+k_n\beta_Ta.$$

Combining this with (5) and the root discrepancy lower bound (16)
proves (19), with both positive reserves
\(E_T/(2\rho T)\) and \(T^{-1}\sum R_t\) in its bracket.
Dropping these reserves would weaken the lower bound, not invalidate
its square obstruction.

At fixed \(T\), marker cancellation gives
\(\widehat u_{T,0}\to2\beta_T\). Direct algebra yields

$$\frac{k_n}{\sqrt n}\to
\sqrt{1+\tau}-\sqrt\tau,\qquad
k_na\to2\sqrt\tau(\sqrt{1+\tau}-\sqrt\tau).$$

The limiting \(C_n\) and discrepancy constant in (20)--(21)
therefore have the stated values. At \(\tau=.05\), the exact
formula gives a slope coefficient approximately
\(0.09788687145942727\) and constant approximately
\(2.358257569495584\); Astra's displayed rounded bounds point
outward. The lower bound uses the actual square theta value and
does not assign a subfield or an arithmetic coset to any prime.

For every fixed horizon, the inherited fixed-depth draft makes
the marker averages vanish uniformly over normalized nonnegative
weights on that horizon. Formula (19) itself is finite and applies
also to growing horizons. Obtaining its positive limiting right
side on a growing horizon separately requires the marker-average
hypothesis; the fixed-depth draft does not supply it.

### The sufficient prime criterion and its comparison with amplitude

Equation (22) follows by discarding the two nonpositive reserves
in (5) and applying the same common-cap support bound. For each
fixed \(T\), its root and floor contributions tend to
\(\beta_T(2+d_\tau)\), which is bounded independently of \(T\).
Hence (23), along its selected sequence of depths, makes
\(\limsup_p\bar\Delta\) vanish as the depth increases. Jensen
gives (14); the finite set of trial root angles vanishes in the
field limit; the usual final \(\tau\downarrow0\) step removes
the smoothing loss. Only a \(\liminf_T\) is required because a
sequence of arbitrarily good fixed depths suffices. This is a
valid sufficient criterion, with no field-dependent-depth exchange.
If \(\rho\) were instead allowed to tend to zero, its factor in
\(1/(\rho T)\) would have to be retained in the hypothesis.

The one-way comparison (24) is also valid for the same relaxation
on both sides. Subadditivity of fractional top sums and
\(g_{j,i}\le|z_{j,i}|\) give (24). If

$$A_j=\limsup_p\sqrt n\max_{i\ne0}|z_{j,i}|<\infty,
\qquad A_j=o(j),$$

then the fixed geometric convolution of \(A_j\) is \(o(T)\).
Together with \(k_n/\sqrt n\to\sqrt{1+\tau}-\sqrt\tau\),
this implies (23). Finiteness of \(A_j\) is provided by the
separate uniform fixed-depth draft, not by marked cancellation.
For \(\rho=1\) only the terminal Picard index \(T-1\) remains.
An amplitude theorem for one relaxation is not automatically an
amplitude theorem for a different relaxation.

Thus "weaker" is justified as an implication between sufficient
assumptions on matching actual trajectories, conditional on the
inherited fixed-depth uniform finiteness. Strictness within actual
prime trajectories remains unproved. Astra's two height-one
static spikes correctly show a strict functional distinction, but
they violate a uniform fixed-depth bound on the scaled maximum.
Even that additional uniform bound does not by itself make the
functional tests equivalent: consider static, even mean-zero
arrays with root zero, values \(T^2/\sqrt n\) at two opposite
nonroot indices, and value
\(-2T^2/[\sqrt n(n-3)]\) at the other nonroot indices. At
every fixed \(T\), their scaled maximum is bounded by a constant
depending on \(T\), and they admit an exceptional error of
bounded \(\ell_1\) norm at that depth. Their activation source
has total mass \(O_{T,\tau}(n^{-1/2})\), so its field-first
top-source limit is zero, whereas \(A_T/T=T\). Applying the
same geometric combination to this static array sequence preserves
zero field-first terminal top mass. These arrays still do not
satisfy the actual recurrence; they prove no strict separation
inside the Paley orbit family.

No equality of prime and square limiting arithmetic means is
needed for the sufficient criterion or proved by this comparison.
Fable's premise (a') remains open. The square failure of (23)
therefore does not reject the prime criterion. This audit changes
no solution claim: the missing input is a prime estimate for the
actual source tails or another compatible trajectory quantity.

## Short algebra audit of the paired reciprocal inverse

This checks only the proposed Schur-complement identities from
[the reciprocal-source note](parallel-reciprocal-28.md). It is
independent of the separate, still-pending source-pair research chat.
Write \(c=\tau/n\), \(a=\sqrt{W/n}\),
\(\rho_0=c/a^2=\tau/W\),
\(x_+=A-a\mathbf1\), \(x_-=B-a\mathbf1\), and
\(e_\pm=P_\pm e_0\). All inner products use counting measure.
Assume \(0<c<1\), as in that note, and both sectors are nonempty.

Let \(D_\pm=\operatorname{diag}(c/(aA_\pm))\),
\(T_\pm=P_\pm D_\pm P_\pm|_{V_\pm}\), and \(Q=D_+^{-1}\).
Pointwise reciprocity \(AB=w\) gives

$$d_{+,i}d_{-,i}=\rho_0\ (i\ne0),\qquad
d_{+,0}d_{-,0}=\rho_0c,$$

and hence exactly

$$Q=D_-/\rho_0+k e_0e_0^*,\qquad
k=\frac{1-c}{d_{+,0}}
=\frac{(1-c)A_0}{a\rho_0},\qquad
Q\mathbf1=\frac{A}{a\rho_0}.$$

In the orthogonal decomposition
\(\mathbb R\mathbf1\oplus V_+\oplus V_-\), use the normalized
constant vector \(\mathbf1/\sqrt n\). The blocks are

$$Q_{00}=1/\rho_0,\qquad
Q_{+0}=\frac{x_+}{\rho_0\sqrt W},\qquad Q_{-0}=0.$$

Therefore the inverse-of-compression Schur identity is precisely

$$T_+^{-1}=Q_{++}-\frac{x_+x_+^*}{\rho_0W}
-Q_{+-}H^{-1}Q_{-+},\qquad
H=Q_{--}=T_-/\rho_0+k e_-e_-^*.$$

In particular the proposed denominator \(\rho_0W\) is correct;
using an unnormalized constant vector without adjusting its block
would lose the factor \(W\).

There is a source-specific simplification of the entire marked
Woodbury update. The accepted source equation gives

$$T_-^{-1}e_-=rac{B_0}{1-c}x_-,\qquad
\langle e_-,T_-^{-1}e_-\rangle
=\frac{B_0(B_0-a)}{1-c}.$$

Since \(A_0B_0=1\), the Woodbury denominator collapses to

$$1+\rho_0k\langle e_-,T_-^{-1}e_-\rangle
=1+\frac{B_0-a}{a}=\frac{B_0}{a}.$$

Substitution gives the exact operator and source identities

$$\boxed{\quad
H^{-1}=\rho_0\left(T_-^{-1}-\frac{x_-x_-^*}{1-c}\right),
\qquad H^{-1}e_-=rac{\rho_0a}{1-c}x_-.
\quad}$$

Thus the two marked inverse moments for this block are

$$\langle e_-,H^{-1}e_-\rangle
=\frac{\rho_0a(B_0-a)}{1-c},\qquad
\|H^{-1}e_-\|_2^2
=\left(\frac{\rho_0a}{1-c}\right)^2\|x_-\|_2^2.$$

The cross block simplifies on the same actual source:

$$Q_{+-}x_-=\frac{1-c}{a\rho_0}e_+
-\frac{x_+}{\rho_0},\qquad
Q_{+-}H^{-1}e_-=e_+-\frac{a}{1-c}x_+.$$

The first equality is simply \(Qx_-=(w-aA)/(a\rho_0)\)
projected onto \(V_+\); the second follows by substitution.
All identities also hold with the signs exchanged and the
corresponding inverse diagonal chosen. They are useful exact
consistency relations between the actual two sources. The second
inverse moment still contains \(\|x_-\|_2^2\) itself. No bound
on either centered energy, no prime estimate, and no acceptance of
the pending source-pair research attempt is inferred from this
algebra audit.
