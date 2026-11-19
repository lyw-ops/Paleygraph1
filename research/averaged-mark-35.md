# An averaged mark budget gives a direct theta finish

Round 35, ordinary theta. The missing prime-uniform positive completion
is **not proved** here. Positivity of suitable averaged proposals, with
their means and marks preserved, would itself suffice for ETH26.
A conic $o(\kappa)$ gap, UI, HR, and an inverse-source comparison are
not additional requirements for this particular constructive route.

The proposal inherits the averaged projected rows of
[iterate majorants](iterate-majorants.md). That earlier construction
repairs them by adding mean. Here we combine the
[round-34 repair](astra-conic-primal-34.md), which preserves mean and
mark, with the elementary Picard mean budget below. No discovery of
the Fourier theta LP, energy telescope, or pinned projection is claimed.

There is also a stronger finite negative control: the saved square
trial at $q=389^2$, depth 48, has minus mark $267.60440179976\ldots$,
whereas its maximum feasible value is exactly $195$. **Every**
nonnegative mean-one minus-sector completion preserving that mark is impossible, not just
the reflection tested earlier. This is not conic infeasibility.

## 1. Two feasible marks bracket ordinary theta

Use the [Fourier convention](fourier.md):
$\theta_+=\vartheta(\overline H)$, $\theta_-=\vartheta(H)$,
$\theta_+\theta_-=n$. If $p\in1+V_+$ and $q\in1+V_-$ are real,
nonnegative, even rows of mean one, then

$$
p_0\le\theta_+,\quad q_0\le\theta_-,
\qquad
\boxed{\frac{p_0}{\sqrt n}\le\frac{\theta_+}{\sqrt n}
                         \le\frac{\sqrt n}{q_0}.}          \tag{1}
$$

The upper bound assumes $q_0>0$. Their cross inner product is $n$,
so $p_0q_0\le n$. Balanced marks near $\sqrt n$ suffice; fidelity is
one way to find them, not a necessary objective once they are feasible.

## 2. The actual Picard mean budget

Let $0<\tau<n$, $c=\tau/n$, $w_0=1$, $w_i=c$ off the mark,
$W=1+(n-1)c$. Use counting norms and the actual Paley operator
$K^2=I-J$, $K1=0$. Put

$$
v^{(0)}=0,\quad \phi_t=\sqrt{(v^{(t)})^2+4w},\quad
v^{(t+1)}=K\phi_t,\quad
\mu_t=\frac1{2n}\sum_i\phi_t(i),\quad E_t=\|v^{(t)}\|_2^2.
$$

Exactly,

$$
\boxed{E_{t+1}-E_t=4W-4n\mu_t^2.}                         \tag{2}
$$

Indeed $\|K\phi_t\|^2=\|\phi_t\|^2-n(\mathbb E\phi_t)^2$ and
$\|\phi_t\|^2=E_t+4W$. Individual $\mu_t^2$ need not stay below
$W/n$; no monotonicity is asserted.

For $T\ge1$, set $M_T=T^{-1}\sum_{t=1}^T\mu_t$. Cauchy--Schwarz
and (2) give

$$
\begin{split}
nM_T^2
&\le\frac nT\sum_{t=1}^T\mu_t^2
 =W+\frac{E_1-E_{T+1}}{4T}\\
&\le B_{n,T}:=
 W+\frac{(1-\sqrt c)^2(1-1/n)}{T}\le W(1+1/T).
\end{split}                                               \tag{3}
$$

Here $v^{(1)}=2(1-\sqrt c)Ke_0$, so
$E_1=4(1-\sqrt c)^2(1-1/n)$. At fixed $\tau,T$,
$B_{n,T}\to1+\tau+1/T$.
More generally, decreasing weights $\alpha_t\ge0$ with
$\sum\alpha_t=1$ give
$n(\sum\alpha_t\mu_t)^2\le W+\alpha_1E_1/4$ by summation by parts.

## 3. Projected averages have balanced marks

For $P_\sigma=(I-J+\sigma K)/2$, define raw positive rows
$A_{\sigma,t}=(\phi_t+\sigma v^{(t)})/2$ and projected averages

$$
X_{\sigma,T}=M_T1+\frac1T\sum_{t=1}^T P_\sigma A_{\sigma,t},
\qquad z_{\sigma,T}=X_{\sigma,T}/M_T\in1+V_\sigma.          \tag{4}
$$

They have the correct mean and sector and are even, but need not be
nonnegative. For the single-time row
$X_{\sigma,t}^{\rm one}=\mu_t1+P_\sigma A_{\sigma,t}$, exact
**vector** identities are

$$
\begin{split}
X_{+,t}^{\rm one}-X_{-,t}^{\rm one}
 &=\tfrac12(v^{(t)}+v^{(t+1)}),\\
X_{+,t}^{\rm one}+X_{-,t}^{\rm one}
 &=(\mu_t-\mu_{t-1})1+\tfrac12(\phi_t+\phi_{t-1}).
\end{split}                                               \tag{5}
$$

Use $Kv^{(t)}=(I-J)\phi_{t-1}$ to check them. Averaging at the mark:

$$
\begin{split}
X_{+,T}(0)-X_{-,T}(0)
 &=\frac1{2T}\sum_{t=1}^T[v^{(t)}_0+v^{(t+1)}_0],\\
X_{+,T}(0)+X_{-,T}(0)
 &=\frac{\mu_T-\mu_0}{T}
       +\frac1{2T}\sum_{t=1}^T[\phi_t(0)+\phi_{t-1}(0)].
\end{split}                                               \tag{6}
$$

For fixed $\tau,T$, inherited fixed-depth marked cancellation gives
$v^{(t)}_0\to0$ through eligible primes and square orders. Since
$\mu_t=O_{\tau,T}(n^{-1/2})$, it follows that

$$X_{+,T}(0)\to1,\qquad X_{-,T}(0)\to1.                   \tag{7}$$

The arithmetic input is the previously established marked cancellation,
not an all-depth parity claim.
For growing $T=T_n$, a sufficient weaker condition is

$$
\frac1{T_n}\sum_{t=0}^{T_n+1}|v^{(t)}_0|^2\longrightarrow0. \tag{8}
$$

Use Cauchy--Schwarz and
$0\le\sqrt{x^2+4}-2\le x^2/4$ in (6).
The boundary term is $O_\tau(n^{-1/2})$, uniformly over $T\ge1$,
because $\mu_T\le\sqrt{W(T+1)/n}$ and
$\mu_0\le\sqrt{W/n}$. Thus (8) implies (7) too.
A proved simultaneous marked window suffices; no extension beyond
such a window is assumed.

## 4. A direct finish conditional on positive completion

Suppose an operation makes both $z_{\sigma,T}$ nonnegative while
preserving means, sectors and marked coordinates. It can be round 34's
clipped reflection when its hypotheses hold, or another verified
operation with those properties. Call the outputs $p,q$. Equations
(1), (3), and $p_0=X_{+,T}(0)/M_T$, $q_0=X_{-,T}(0)/M_T$ give

$$
\boxed{\frac{X_{+,T}(0)}{\sqrt{B_{n,T}}}
\le\frac{\theta_+}{\sqrt n}
\le\frac{\sqrt{B_{n,T}}}{X_{-,T}(0)}.}                    \tag{9}
$$

The marked denominator must be positive. If completion exists for all
sufficiently large primes at fixed $\tau,T$, (7) yields

$$
(1+\tau+1/T)^{-1/2}
\le\liminf_p\frac{\theta_+}{\sqrt n}
\le\limsup_p\frac{\theta_+}{\sqrt n}
\le(1+\tau+1/T)^{1/2}.                                   \tag{10}
$$

It suffices to prove these completions for a sequence
$\tau_j\downarrow0$, $T_j\to\infty$, taking the prime limit first.
Alternatively take growing $T_n\to\infty$ satisfying (8), prove
completion there, and then send the fixed floor to zero.

This does not prove completion at any required fixed or growing depth.
Averaging need not improve every negative coordinate. The signed
prime arithmetic feasibility remains unproved. The broader UI/HR
route retains its own separate obligations.

## 5. Square orders obstruct these prescribed marks

At $q=r^2$, $\theta_+=r-1$ and
$\theta_-=n/(r-1)=(r+1)/2$, so $\theta_-/\sqrt n\to1/\sqrt2$.
For fixed $\tau,T$ with $\tau+1/T<1$, (3), (7) force

$$
\liminf_{r\to\infty}\frac{z_{-,T}(0)}{\sqrt n}
\ge(1+\tau+1/T)^{-1/2}>1/\sqrt2.
$$

Consequently no nonnegative minus completion preserving this mark
exists at all sufficiently large square orders. The same holds along
growing depths with (8), $T_n\to\infty$, and $\tau<1$.
This is an obstruction for the prescribed proposals, not for conic
feasibility. Any successful completion theorem here needs prime input.

The saved round-34 square input gives the exact finite version

$$
q_0=\frac{\sum_k\texttt{minus\_coeff}_k}{2^{90}}
=267.6044017997648\ldots>195=\theta_-.
$$

No operation preserving mean one, the minus sector, and that mark
can make the row nonnegative. Its exact positive rational excess is
recorded in the certificate.

## 6. A conic gap also gives a marked comparison

For positive feasible $p,q$ and the actual normalized pair $u,v$,
round 33 gives $D=\mathbb E(\sqrt{uq}-\sqrt{vp})^2$.
Put $\gamma=\log A_0$, $h=\tfrac12\log(p_0/q_0)$,
$\alpha=p_0q_0/n$. Its marked summand proves

$$
D\ge4\sqrt{\alpha/W}\sinh^2((\gamma-h)/2),\qquad
\boxed{|\gamma-h|\le
2\operatorname{arsinh}\sqrt{\frac{D}{4\sqrt{\alpha/W}}}.}  \tag{11}
$$

The original gap's marked summand also gives
$D\ge(W^{-1/2}-\sqrt\alpha)^2$.
Thus $D\to0$ forces $\alpha\to1/W$ at a fixed floor;
with $h\to0$ it forces $\gamma\to0$. Here $D=o(\kappa)$ is
unnecessary. Direct theta bounds (1) can be stronger and need no gap.

## 7. Checks, comparison and scope

Run from the repository root:

    .venv/bin/python -B research/averaged-mark-35.py \
      > research/averaged-mark-35-certified.jsonl

Thirteen records contain one exact rational actual-prime-13
projector/mark/energy check, five Arb224 true small-orbit budget checks,
five derived theta intervals from round 34's accepted positive exact
inputs, one exact square no-completion certificate, and a success row.

The prime-$1000033$ depth-48 trial gives
$\theta_+/\sqrt n\in[.9767038058,1.0255433748]$.
These root-only intervals are weaker than earlier residual certificates;
their role is to exhibit a finish bypassing a fidelity objective.
The conic-gap marked comparison is retained for contrast.
No new large positivity transform or stationary solve is performed.
The five prime bounds explicitly depend on accepted Arb224 positivity
and root preservation from round 34. The small orbit checks verify
normalizations; the general statements rest on the written arguments.
No prime-uniform positivity or ETH26 proof is asserted.
