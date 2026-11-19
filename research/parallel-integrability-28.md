# Stationary source integrability and residual pairings

Uniform integrability of the stationary bulk source implies a subcritical stationary energy and broad effective support. It also supplies a sufficient residual-pairing criterion when accompanied by a suitable bound on the residual test functions. Uniform integrability alone does not justify that pairing step. The explicit functional counterexample below has decaying residual-test \(L^2\) norm and bounded test functions at every fixed depth. It does not construct a nonlinear Paley stationary orbit, so whether the stationary self-consistency equation supplies the missing control remains open here.

## Exact source normalization

Fix \(\tau>0\), \(n=(q-1)/2\), \(w_0=1\), \(w_i=\tau/n\) off the mark, and \(W=\sum w\). For the actual stationary vector \(v^*=K\Phi(v^*)\), write

$$g=\Phi(v^*)-\Phi(0)\ge0,\qquad
G_i=\sqrt n\,g_i\quad(i\ne0),\qquad V_i=\sqrt n\,v_i^*.$$

The [complementary smoothing identity](smoothing.md) gives

$$\sum_i g_i=2\sqrt{nW}-2-2(n-1)\sqrt{\tau/n}.$$

With normalized bulk sums still divided by \(n\), this is

$$\mathbb E_nG
=2\sqrt W-\frac2{\sqrt n}
-2(1-1/n)\sqrt\tau-\frac{g_0}{\sqrt n}
\longrightarrow L_\tau:=2(\sqrt{1+\tau}-\sqrt\tau)>0.$$

The root term is bounded uniformly in the field, by the existing stationary coordinate bound. On the bulk there are exact pointwise relations

$$G_i\le |V_i|\le G_i+2\sqrt\tau,\qquad
V_i^2=G_i^2+4\sqrt\tau\,G_i.$$

Thus source uniform integrability is equivalent to uniform integrability of the absolute scaled stationary bulk vector.

## Consequences and a distinction from broadness

Paley coherence and the stationary \(\ell_1\) bound give \(\max_iG_i\le C_\tau\sqrt n\). If

$$\epsilon(R):=\limsup_q\mathbb E_n[G\mathbf1_{G>R}]
\longrightarrow0,$$

then

$$\mathbb E_nG^2
\le R\mathbb E_nG+C_\tau\sqrt n\,
\mathbb E_n[G\mathbf1_{G>R}].$$

First take the field limit at fixed \(R\), then let \(R\to\infty\). The result and the exact pointwise relation above imply

$$\|v^*\|_2^2=o(\sqrt n),\qquad
\|v^*\|_2=o(n^{1/4}).$$

For the effective support of the bulk source,

$$m_{\rm eff}(G)
=\frac{(\sum G_i)^2}{\sum G_i^2}
=\frac{n(\mathbb E_nG)^2}{\mathbb E_nG^2},$$

one obtains \(m_{\rm eff}(G)/\sqrt n\to\infty\). The converse implication fails for arbitrary profiles. A profile of height \(n^\alpha\) on a fraction \(n^{-\alpha}\) of coordinates, with \(0<\alpha<1/2\), has mean one and effective support \(n^{1-\alpha}\), but its entire first-moment mass escapes every fixed truncation. Source uniform integrability also permits an unbounded second moment, as the explicit example below shows.

## What a residual split actually requires

Let \(r_{q,T}\) be a mean-zero residual and put \(H_{q,T}=\sqrt n(Kr_{q,T})\) on the bulk. Since

$$v^*=K\Phi(0)+g_0Ke_0+
K\left(\frac{G\mathbf1_B}{\sqrt n}\right),$$

self-adjointness gives

$$\langle r_{q,T},v^*\rangle
=\langle r_{q,T},K\Phi(0)+g_0Ke_0\rangle
+\mathbb E_n[H_{q,T}G].$$

The first term is \(O_\tau(\|r_{q,T}\|_2)\). The marked coordinate of \(g\) has been separated explicitly. If

$$a_T=\limsup_q\|r_{q,T}\|_2,\qquad
B_T=\limsup_q\|H_{q,T}\|_\infty,$$

and these quantities are finite, truncation and \(\|K\|_{2\to2}\le1\) yield

$$\limsup_q|\langle r_{q,T},v^*\rangle|
\le C_\tau a_T(1+\sqrt R)+B_T\epsilon(R).$$

Here \(\|G\mathbf1_{G\le R}\|_{2,n}\le\sqrt{R\mathbb E_nG}\). This proves transfer if \(a_T\to0\) and \(B_T\) is bounded uniformly in \(T\). More generally it suffices to choose \(R_T\to\infty\) with \(a_T\sqrt{R_T}\to0\) and \(B_T\epsilon(R_T)\to0\). Merely knowing that each \(B_T\) is finite supplies no such choice. The inherited fixed-depth proof gives approximation by bounded arithmetic expressions in normalized \(\ell_2\). That statement alone does not bound the supremum norm of the actual residual test, even at a fixed depth.

A further sufficient condition is a dual Orlicz bound. For a convex superlinear \(A\), let \(A^*\) be its convex conjugate. If \(\sup_q\mathbb E_nA(G)<\infty\) and, for every \(\eta>0\),

$$\lim_{T\to\infty}\limsup_q\mathbb E_n
A^*(|H_{q,T}|/\eta)=0,$$

Young's inequality gives \(\mathbb E_n|GH|\le
\eta\mathbb E_nA(G)+\eta\mathbb E_nA^*(|H|/\eta)\), hence vanishing pairings. This states precisely an additional test-function condition.

## A counterexample to the uniform-integrability pairing inference

On \((0,1)\) with Lebesgue probability, set

$$G(s)=s^{-3/4},\qquad
H_T(s)=T^{1/4}\left(\mathbf1_{s\le1/T}-\frac1T\right).$$

The singleton \(\{G\}\) is uniformly integrable, each test is bounded and mean zero, and

$$\|H_T\|_2=T^{-1/4}\sqrt{1-1/T}\longrightarrow0.$$

Nevertheless

$$\int_0^1GH_T\,ds=4(1-T^{-3/4})\longrightarrow4.$$

The source can also obey the stationary coordinate scale. Let

$$g_n(s)=\min(s^{-3/4},\sqrt n),\qquad
m_n=\int_0^1g_n=4-3n^{-1/6},\qquad G_n=g_n/m_n.$$

These profiles have mean one, \(G_n\le\sqrt n\), and a uniform first-moment tail bound \(\int G_n\mathbf1_{G_n>R}\le4R^{-1/3}\). Their second moments are

$$\int G_n^2=\frac{3n^{1/3}-2}{(4-3n^{-1/6})^2}\longrightarrow\infty.$$

At every fixed \(T\), \(\int G_nH_T\to1-T^{-3/4}\), which tends to one as \(T\to\infty\). Conditional expectations on uniform finite partitions preserve this uniform integrability and the coordinate cap. For partitions with \(T\mid n\), the pairing with \(H_T\) is unchanged, so the same example exists on finite normalized counting spaces.

For any reflection \(K^2=I-J\), a mean-zero finite test vector \(H\) is realized by \(r=KH/\sqrt n\): then \(\sqrt nKr=H\) and \(\|r\|_2=\|H\|_{2,n}\). Thus the reflection norm identity does not remove this functional obstruction. The example does not impose \(G=\sqrt n[\Phi(v^*)-\Phi(0)]\) for a genuine stationary solution, or require the tests to be residuals of the actual Picard orbit. A proof exploiting those additional equations would add substantive information.

## Reproducible arithmetic of the example

The [script](parallel-integrability-28.py) evaluates the closed-form clipped moments and pairings in the counterexample. The [records](parallel-integrability-28.jsonl) are floating-point evaluations of explicit formulas. The displayed identities supply the proof.

```sh
.venv/bin/python -B research/parallel-integrability-28.py > research/parallel-integrability-28.jsonl
```

## Audit of the direct stationary cap certificate

For any real trial \(z\), put \(u^z=\Phi(z)\), \(r=z-Ku^z\), and
\(b=-Kr=u^z-\overline{u^z}\mathbf1-Kz\). Then \(\sum b=0\), and

$$\Delta:=\langle u^*,u^z\rangle-\langle v^*,z\rangle-4W
=2\sqrt W S_z-4W+\langle b,u^*\rangle,$$

where \(S_z=\sum u^z/\sqrt n\). If
\(v_i^*=2\sqrt{w_i}\sinh\gamma_i\) and
\(z_i=2\sqrt{w_i}\sinh\eta_i\), the same quantity equals

$$\Delta=4\sum_iw_i[\cosh(\gamma_i-\eta_i)-1]\ge0.$$

Consequently any valid upper bound \(U\ge\Delta\) gives
\(|\gamma_0-\eta_0|\le\operatorname{acosh}(1+U/4)\). The log-theta
certificate includes the additional \(\tfrac12\log W\). Neither displayed
identity needs the trial to have exactly zero mean, since \(K\mathbf1=0\).

Here is a direct proof of the stationary point cap used in that argument.
Write the stationary positive pair as \(p,q\), so
\(p_iq_i=w_i\), \(p,q\) have opposite Fourier sectors and sum
\(\sqrt{nW}\). Every shift \(p^{(j)}\) has
\(\langle p^{(j)},q\rangle=W\). Therefore \(\log x\le x-1\) gives

$$\sum_iw_i\log(p_{i-j}/p_i)
\le\sum_iq_i p_{i-j}-W=0.$$

Put \(h=\tau/n<1\). The left side is
\((1-h)\log(p_{-j}/p_0)\), because the unweighted sum of the translated log
ratios vanishes. Hence \(p_i\le p_0\), and likewise \(q_i\le q_0\).
Thus \(u_i^*\le s:=u_0^*=p_0+q_0\). The Jacobi point bound supplies

$$p_0,q_0\le C:=(1+\sqrt q)\sqrt{W/n},\qquad p_0q_0=1,$$

so \(2\le s\le C+C^{-1}\).

For the common-floor cap let \(a=2\sqrt h\),
\(\mathcal B=2\sqrt{nW}-na\), and \(d=s-a\). At fixed \(d\), the exact
maximum of \(\langle b,u\rangle\) under just this box and total-sum
relaxation is

$$d\left[b_0+
\operatorname{Top}_{\mathcal B/d-1}(b_B)\right].$$

The feasible interval for its one-dimensional maximization must be

$$[2-a,C+C^{-1}-a]\ \cap\ [\mathcal B/n,\mathcal B].$$

The second interval enforces \(0\le\mathcal B-d\le(n-1)d\). Fractional
Top uses the largest entries with their signs retained, at the exact mass.
On each interval between \(d=\mathcal B/(j+1)\), the expression is affine.
Thus endpoints and these breakpoints suffice.

There is also a smaller available bulk cap. Given \(p_0q_0=1\),
\(p_i\le p_0\), \(q_i\le q_0\), and \(p_iq_i=h\), convexity of
\(x+h/x\) gives

$$u_i^*\le\max(p_0+hq_0,q_0+hp_0)\le C+h/C
\qquad(i\ne0).$$

With the constant bulk excess cap \(D=C+h/C-a>0\), the corresponding
relaxation instead has objective

$$d b_0+D\operatorname{Top}_{(\mathcal B-d)/D}(b_B),$$

on \([2-a,C+C^{-1}-a]\cap
[\mathcal B-(n-1)D,\mathcal B]\). This is again piecewise affine, now with
breakpoints \(d=\mathcal B-jD\). For fixed \(\tau<1\) and large fields,
\(C+h/C<2\), so this uniform bulk cap is smaller than every allowed root
height. At small orders one can retain both bulk caps by taking their
minimum.

The fractional Top mechanism is already used in the anchored-repair and
gradient-splitting notes. The specific direct cap on the stationary
hyperbolic discrepancy was not found in the scoped comparison with those
notes. These formulas provide finite certificates, and do not themselves
supply a uniform prime tail estimate.

### Root-coupled cap and a threshold certificate

The sharper cap at a specified \(s=p_0+q_0\) is

$$M(s)=\alpha s+\beta\sqrt{s^2-4},\qquad
\alpha=(1+h)/2,\quad\beta=(1-h)/2.$$

For every real threshold \(t\), put \(U=\sum_B(b_i-t)_+\). The exact sum
constraint and the bulk cap imply

$$\langle b,u^*\rangle
\le(s-a)(b_0-t)+(M(s)-a)U+t\mathcal B.$$

This becomes \(Ls+J\sqrt{s^2-4}+c\), with

$$L=b_0-t+\alpha U,\quad J=\beta U\ge0,\qquad
c=t\mathcal B-a(b_0-t+U).$$

It is concave on \(s\ge2\). On
\([2,\min(C+C^{-1},\mathcal B+a)]\), check the endpoints and, when
\(L<-J\) and \(J>0\), the possible interior maximum

$$s_*=-\frac{2L}{\sqrt{L^2-J^2}},\qquad
F(s_*)=c-2\sqrt{L^2-J^2}.$$

Enlarging the interval by including root heights that fail a bulk
feasibility condition preserves this upper certificate. Replacing every
true \(b_i\) by a rational upper bound is also safe: the zero-sum baseline
is eliminated before replacement, and both coefficients \(s-a\) and
\(M(s)-a\) are nonnegative.

The independent code review of [the direct implementation](source-tail-28.py)
found the interval directions and critical-point branch conservative. A
short \(q=61\), \(\tau=1/20\), eight-step trial replay used only temporary
files and produced the outward interval
\([0.599196047789,1.428539046365]\) for normalized theta. This certifies a
rounded trial without assuming it equals an exact finite iterate.

## Independent acceptance audit of Fable's position-space note

This appendix audits [Fable's round-28 note](claude-fable-28.md). Its
Propositions 1--3 and equation (7) are finite-dimensional identities or
inequalities with the stated Fourier normalization. They do not require
the field order to be prime. The numerical records remain floating-point
diagnostics; their replay does not certify the stationary points or an
asymptotic arithmetic premise.

For A1, \(m^2=W/n\), \(u_+u_-=w\), and unnormalized multiplicative
convolution give

$$\widehat f_+\widehat f_-=nw/W,\qquad
f_+*f_-=\frac{1-\tau/n}{W}\mathbf1_Q+
\frac\tau W\delta_1.$$

Thus \(\gamma=(1-\tau/n)/W\) and \(1-\gamma=\tau/W\), with no
missing factor of \(n\). The sector equations give \(f_\pm(1)=1\)
and the complementary supports. Those supports are inversion closed,
so \((\phi_+*\phi_-)(1)=0\). The asserted inverse follows by
convolving \(f_+\) with
\(f_--\gamma\mathbf1_Q/(1+A)\); its normalization by
\(1-\gamma\) is legitimate for \(\tau>0\).

For A2, writing \(c=\operatorname{mean}\Phi(v)\) and
\(r=v-K\Phi(v)\) gives exactly

$$2\sum_iw_i\cosh(g_i-g_i^*)
=ncm-\tfrac12\langle r,v^*\rangle,
\qquad nc^2=4W+2\langle v,r\rangle-\|r\|_2^2.$$

Applying \(\sqrt{1+x}\le1+x/2\) to the latter square root proves
the coefficients \(1/4\) and \(-1/8\) in (4). For A3, exchanging
the two unnormalized Fourier sums proves (5); the position \(x=1\)
contributes zero because \(f_+(1)-f_-(1)=0\). In particular its
mean-zero restriction is sufficient but unnecessary. For a Picard
residual the displayed formula using \(G_{T-1}-G_T\) requires
\(T\ge1\). For an averaged iterate the residual instead equals
\(2(z_T-z_{T+1})\); these two conventions must be kept separate.

### The point cap and the meaning of the weaker stationary factor

The stated root bound \(\Phi_0^*\le2\sqrt{qW/n}\) is correct. A
proof uses the positive stationary pair, rather than substituting a
bound on \(|v_0^*|\) into its square root. Coherence and the sector
equations give

$$u_{+,0},u_{-,0}\le C=(1+\sqrt q)\sqrt{W/n},
\qquad u_{+,0}u_{-,0}=1.$$

Consequently \(\Phi_0^*\le C+C^{-1}\le2\sqrt{qW/n}\). The last
inequality is equivalent to \(1\le2W\), which holds here since
\(W\ge1\). This generic cap does not identify a prime-specific
improvement.

There is also an exact norm comparison for Fable's stationary factor.
Let \(D=\phi_+-\phi_-\). Its supports are disjoint, it vanishes at
the identity, and \(\widehat D=v^*/m\). Parseval and
Cauchy--Schwarz give

$$\|D\|_2^2=\|v^*\|_2^2/W,\qquad
m(\|\phi_+\|_1+\|\phi_-\|_1)
=m\|D\|_1\le\sqrt{1-1/n}\,\|v^*\|_2.$$

Thus bounded stationary \(\ell_2\) norm implies bounded positional
factor. Calling this factor condition weaker is accurate in that
logical sense. The complete transfer criteria are not ordered by this
comparison, because the new residual supremum can be larger. A strict
separation for the actual stationary Paley family is not established
by the finite square-order runs. Those runs show bounded measured
factors; they do not prove a uniform bound at every square order, nor
that the residual supremum is the only possible square-order failure
in an asymptotic theorem.

### What the order-of-limits argument establishes conditionally

At a fixed depth \(T\), assume the uniform class-function
approximation asserted in [the fixed-depth draft](uniform-fixed-depth.md),
including its bounded \(\ell_1\) exceptional error. The exact square
theta value and the averaged-iterate discrepancy imply
\(\langle z_T,v^*\rangle\ge T c_\tau^2-o(1)\) for
\(0<\tau<1\). The root contribution vanishes. Frequencies with
\(\sqrt n|z_T|<T c_\tau^2/(4\sqrt W)\) contribute at most half
this lower bound, by \(\|v^*\|_1\le2\sqrt{nW}\). Boundedly many
exceptional frequencies contribute \(o(1)\), by the fixed-depth
uniform bound and the stationary coordinate cap. The remaining
large values therefore include good frequencies. Bounded complexity
and a uniform Lipschitz bound turn such a class-function value into a
positive Haar fraction of the **same field's arithmetic coset**, and
the fixed-complexity trace estimate turns it into a positive fraction
of that square field's frequencies. This validates the square-side
step in C, conditional on the fixed-depth draft being valid.

Transfer to primes requires a separate arithmetic premise. One
precise sufficient version of (a') is: for each fixed \(T\) and the
chosen positive cutoff margin, the finitely many good-character
means used in a polynomial approximation to that cutoff match along
one common infinite prime subsequence and a square subsequence.
Matching individual expressions along unrelated infinite prime sets
would not suffice. A common prime subsequence for all depths is not
needed for the stated \(\limsup_p\) obstruction. No common compact
group or common arithmetic coset across the two field families has
been proved or used here. Geometric inertia parity supplies neither
this matching nor equality of arithmetic traces on invariants.

Under that precise matching premise the same cutoff has positive
prime frequency density, so

$$\limsup_p\sqrt n\max_{k\ne0}|z_T(k)|\ge c'_\tau T.$$

It would then rule out the field-first sublinear hypothesis for this
particular averaged-field supremum. Without the premise it does not
rule out that hypothesis at primes. The unconditional wording in
C/E that a fixed-depth field-first version is not a suitable target
should therefore be read as conditional guidance, not a proved
rejection of an existing ledger target.

Three further qualifications are necessary. First, a limiting law
by itself yields a lower bound on a limiting maximum from its
support. Equality of the maximum with the support radius requires
control of exceptional frequencies: a bounded \(\ell_1\) error
can have an \(O(1)\) spike invisible to the empirical law. Second,
the frequency-side averaged-field argument just described does not
by itself transfer the positional **residual** hypothesis (II): that
concerns another Fourier array, and its Picard/averaged convention
and arithmetic comparison must be supplied separately. The
`possup` data are evidence for that extension, not its proof. Third,
E's phrase "or equivalently in position form" is too strong. The
two Fourier supremum hypotheses are alternative sufficient routes
with different stationary factors. The displayed normalizations do
not make the norms equivalent; Fourier inversion allows losses
growing with \(n\).

The accepted ledger conclusion remains: A1--A3 supply valid
field-general reformulations and conditional transfer bounds;
arithmetic premise (a'), positional negative-mass control, and
growing-depth estimates remain open. No previously proved
sufficient implication has been refuted, and Problem 26 has not
been solved by these diagnostics.
