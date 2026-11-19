# A lower bound on the depth of exact mark-preserving completion

Round 38. The marked cancellation window extends uniformly to floors
$0\le\tau\le1$, including varying floors. For the exact undamped
Picard proposal with a vanishing floor through primes, a necessary
condition for a joint mean- and mark-preserving positive completion
within this window is

$$
\liminf_p T_p\tau_p\ \ge\ (1-2\sqrt2/\pi)^2.
$$

For $T_p\ge2$ the second iterate raises the lower bound to
$(1-m_1)^2+(1-b_2)^2$, with $m_1=2\sqrt2/\pi$ and
$b_2=m_1+(1-m_1^2)/(4m_1)$. The bound applies also to arbitrary
nonnegative decreasing weights
on the specified prefix. The obstruction concerns the proposed
marks and mean. Extra mean of order $1/T_p$ can bypass this
particular obstruction without by itself giving a positive row.

## 1. Uniformity of the marked arithmetic as the floor vanishes

Use the normalized-scale recurrence and the geometric closure
estimates (4), (7), and (9) of the
[growing-depth argument](parallel-depth-window-30.md). In particular,
for $Y_t=\sqrt n\,v_t$, the activation on the bulk is
$f_\tau(u)=\sqrt{u^2+4\tau}$ and the exceptional source coefficient
is retained exactly in $[0,2]$. The closure is valid for any even
polynomial with the indicated resource budget, independently of
$\tau$. The only positive-floor-dependent step of the approximation
is the choice of polynomial. For $0\le\tau\le1$, the functions
$f_\tau$ are uniformly one-Lipschitz on the real line, and
$|f_\tau(u)|\le U+2$ for $|u|\le U$.

For $U\ge2$, let $m=\lceil (U/\epsilon)^2\rceil$ and
$z=(u+U)/(2U)$. The Bernstein polynomial

$$
\sum_{j=0}^m f_\tau(-U+2Uj/m){m\choose j} z^j(1-z)^{m-j}
$$

has error at most $\epsilon$ on $[-U,U]$. Indeed it is a binomial
expectation and the Lipschitz error is at most
$2U\sqrt{z(1-z)/m}\le U/\sqrt m$. Average the polynomial at $u$ and
$-u$ to make it even. For $S_U(P)=\sum_k|[u^k]P|U^k$, both affine
factors have weighted coefficient sum one. Consequently the even
polynomial satisfies $S_U(P)\le (U+2)2^m$.

Retain the unweighted rank and conductor budget of (9), as well as
the weighted norm of (7). With $U\ge\epsilon^{-2}$, the degree is
$O(U^3)$ and the next budget can be taken as $2^{C U^4}$ for an
absolute $C$. This follows by taking logarithms of (9), where a word
of length $m$ contributes $O(m\log(U+2))$ to the logarithm of the
resource. Include the coefficient norm and the fixed base field
expressions in the same bound. No constant in this estimate depends
on $\tau\in[0,1]$.

For each fixed $B>0$ and $L=\log_2^* q$, put
$D(q)=\lfloor L-\log_2^*L-C_B\rfloor$ and
$\epsilon=D(q)^{-(B+2)}$. A tower $V_{j+1}=2^{V_j}$ with
$V_0=(U_0+C+2)^8$ dominates the resource via $U_j\le V_j^{1/8}$
once the absolute base constant is enlarged. Indeed
$C V_j^{1/2}\le V_j/8$ for all sufficiently large $V_j$.
The base has iterated logarithm $\le\log_2^*L+O_B(1)$.
Choosing $C_B$ to absorb the two look-ahead indices gives
$U_j\le q^{1/4}$ through $D(q)+2$. Equations (15)–(16) of the
growing-depth argument now give

$$
\boxed{\sup_{0\le\tau\le1}
\max_{0\le t\le D(q)+1}|v_{t,0}|=O_B(D(q)^{-B}).}
$$

This uses the same arithmetic as round 30, with an elementary real
polynomial estimate in place of the positive-floor ellipse. The
approximation error is propagated in normalized Euclidean norm by
the Lipschitz activation and $\|K\|\le1$. The marked pairing uses the
odd-word cancellation with the actual marked coefficient, so the
estimate applies simultaneously in time and in floor.

## 2. A necessary mean margin at the true marks

Set $g_t=\sqrt n\mu_t$, $E_t=\|v_t\|_2^2$, and $W=1+(n-1)\tau/n$.
For positive integer $T\le D(q)$, let
$\alpha_1\ge\cdots\ge\alpha_T\ge0$ be weights summing to one.
Write $m=\sum_t\alpha_t g_t$ for the scaled proposed mean and
$X_\pm(0)$ for the two unnormalized proposed marks. An actual
nonnegative completion preserving the two means and marks must
satisfy

$$
m^2\ge X_+(0)X_-(0).
$$

Indeed, the inner product of two completed rows in complementary
sectors is $n(m/\sqrt n)^2$ and all its summands are nonnegative.
For the actual projected proposals, the
[weighted endpoint identities](astra-averaged-positive-36.md#2-weighted-endpoint-identity-with-the-full-budget)
give $X_+(0)+X_-(0)\ge2$: each marked activation is at least two and
the weighted scalar reserve is nonnegative. The difference of these
marks has absolute value at most $\varepsilon_q$, the preceding
uniform maximum of $|v_{t,0}|$. Consequently

$$
X_+(0)X_-(0)\ge 1-\varepsilon_q^2/4.
$$

There is a uniform lower bound on endpoint energies over the window.
By the Picard identity, $E_{t+1}=\|\Phi(v_t)-2\mu_t1\|_2^2$.
The marked summand alone is at least $(2-2\mu_t)^2$ when
$\mu_t\le1$. The energy identity from zero gives
$\mu_t\le\sqrt{W(t+1)/n}$, so $E_{t+1}\ge4-O(\sqrt{D(q)/n})$
uniformly for $0\le t\le D(q)$. Meanwhile $E_1\le4$ exactly.
Summation by parts in $E_{t+1}-E_t=4W-4g_t^2$ now gives

$$
\sum_{t=1}^T\alpha_t g_t^2
\le W+O\!\left(\alpha_1\sqrt{D(q)/n}\right).
$$

The common constant four cancels between all the energy terms.
Using $2(1-m)=\sum_t\alpha_t(1-g_t)^2+
1-\sum_t\alpha_t g_t^2$, we obtain

$$
2(1-m)\ge
\alpha_1(1-g_1)^2-\tau-O\!\left(\alpha_1\sqrt{D(q)/n}\right).
$$

For uniform weights the exact endpoint loss in this inequality is
$(E_{T+1}-E_1)/(4T)$, and the exact variance contribution uses every
$(1-g_t)^2$. The one-step term is enough for the obstruction.

## 3. Prime input and the limit order

For $p$ prime and $\tau_p\to0$, the exact first iterate gives

$$
g_1=\frac{\Phi_0(v_1)}{2\sqrt n}+
\frac1n\sum_{i\ne0}\sqrt{\tau_p+
  (1-\sqrt{\tau_p/n})^2(\lambda_i/\sqrt n)^2},
\qquad \lambda_i=n K_{i0}.
$$

The normalized Jacobi eigenvalues $\lambda_i/\sqrt p$ have the
arcsine limit from the Gauss-ratio calculation in
[the Fourier witness note](fourier.md#joint-distribution-on-the-even-modes).
For this single marginal one may take the full-character family
$(\psi,\psi\chi)$ in Katz's equidistribution theorem. Its ratio is
Haar on the unit circle, and its real part gives $\lambda_i/\sqrt p$
up to the bounded number of exceptions. The cyclic restriction from
full characters to the square subgroup is two-to-one and leaves
that real part invariant. Coherence supplies the uniform bound
$|\lambda_i/\sqrt p|\le1$. Hence, allowing $\tau_p$ to vary to zero,
$g_1\to\sqrt2\,\mathbb E|\cos\Theta|=2\sqrt2/\pi$.

For the first lower bound, combine the two inequalities of Section 2 and use
$\alpha_1\ge1/T_p$. Taking $B>1$ ensures
$T_p\varepsilon_q^2=o(1)$ throughout the arithmetic window.
If completion succeeds on any prime subsequence with $\tau_p\to0$
and $1\le T_p\le D(p)$, then on that subsequence

$$
T_p\tau_p\ge (1-2\sqrt2/\pi)^2-o(1).
$$

In particular, for schedules with $\limsup_p T_p\tau_p$ strictly
below this constant, all sufficiently large primes have no such
completion. This includes $T_p\to\infty$ with $\tau_p=o(1/T_p)$.
If the same marks are retained with a larger common scaled mean
$\widetilde m$, then the same argument instead forces

$$
2T_p(\widetilde m-m)
\ \ge\ (1-2\sqrt2/\pi)^2-T_p\tau_p-o(1).
$$

This estimate concerns the exact orbit and arbitrary completions of
the prescribed marks. Fixed positive floors followed by depth tending
to infinity can satisfy the necessary depth condition. Deciding
positivity in that regime and establishing the ordinary theta limit
remain open.

## 4. The second iterate gives a further strict loss

Write $x=\sqrt n K e_0$, and use $\|\,\cdot\,\|_{2,n}$ for
normalized Euclidean norm. The actual recurrence in Section 1 gives

$$
\left\|Y_2/2-x-K|x|\right\|_{2,n}=o(1)
\qquad(\tau_p\to0).
$$

Indeed $Y_1/2=(1-\sqrt{\tau_p/n})x$, the second marked source
coefficient tends to two, and replacing the whole bulk activation
by absolute value costs at most $\sqrt{\tau_p}$ after division by
two. Consequently $g_2=\mathbb E_n |x+K(|x|)|+o(1)$. The exceptional
activation changes this latter mean by at most $1/\sqrt n$ in
addition to the bulk square-root error.

Let $X=\sqrt2\cos\Theta$ for uniform $\Theta$. For each fixed $H$,
use the first $H$ nonconstant even Chebyshev terms of $|x|$.
Its Chebyshev coefficients are bounded in absolute value by
$C(1+h)^{-2}$, by the Fourier series of $|\cos\Theta|$.
Applying $K$ to the truncation and dropping the constant gives
a field $Z_H$. The error
$\|K|x|-Z_H\|_{2,n}\le C/H$ is uniform in the prime.

For each such finite truncation the limiting law of $(x,Z_H)$
is a product with first marginal $X$. This is the full-character
joint trace argument of the [path-shape analysis](parallel-graph-shapes-23.md).
In more detail, the two lifts of each even-degree path term are
the compact symplectic factors computed there, prior to any
squaring pushforward. Adding the dimension-one Jacobi ratio
keeps the full product of symplectic groups in the geometric
derived subgroup and puts that derived subgroup in the kernel
of the Jacobi coordinate. Hence the path components are independent
of the Jacobi circle coordinate in the limiting trace law. The
identity-stalk calculation applies at each fixed $H$, before taking
$H$ to infinity. This uses the actual Paley path terms.

The limit of the variance of $Z_H$ follows without a tail
independence assertion. Since $K^2=I-J$, its normalized second
moment is the empirical variance of the truncated Chebyshev
polynomial, tending to the arcsine variance of that polynomial.
As $H\to\infty$ these variances tend to $1-m_1^2$.

For real $z$, $h(z)=\mathbb E|X+z|=\mathbb E\max(|X|,|z|)$.
For $0<z<\sqrt2$, $h'(z)=(2/\pi)\arcsin(z/\sqrt2)$.
It follows that $(h(z)-m_1)/z^2$ increases up to $\sqrt2$,
by writing it as $\int_0^1 h'(zs)/z\,ds$ and using the increasing
function $\arcsin(t)/t$. For $z\ge\sqrt2$, $h(z)=z$, and
$(z-m_1)/z^2\le1/(4m_1)$ by completing the square.
Thus $h(z)\le m_1+z^2/(4m_1)$ everywhere. Apply the bound to
the limiting independent $Z_H$, then send $H$ to infinity
using the uniform approximation error. This proves

$$
\limsup_p g_2\le b_2:=m_1+\frac{1-m_1^2}{4m_1}<1.
$$

For $T\ge2$, any decreasing nonnegative probability weights on
the prefix are a convex combination of the uniform weights on
prefixes of lengths $1,\ldots,T$. For the first two losses
$(1-g_1)^2$ and $(1-g_2)^2$, each prefix of length at least two
contributes their sum divided by its length. The length-one
prefix contributes just the first loss. Since
$(1-b_2)^2<(1-m_1)^2$, these observations bound the weighted
sum from below by
$[(1-m_1)^2+(1-b_2)^2-o(1)]/T$, uniformly over $T\ge2$.
Insert this bound in the exact mean identity of Section 2.
It gives the advertised larger lower bound on $T_p\tau_p$ and
the same improvement for the required mean inflation. The shortest
prefix, $T_p=1$, retains the first loss only.

## 5. The sharper budget also holds at unrestricted depth

For $0<\tau\le1$, the time-shift dissipation argument of
[round 37](astra-completion-37.md#every-unmodified-uniform-prefix-at-o_taunlog-n)
gives $\sup_t g_t=O(\log n)$ with an absolute constant.
The estimate holds at $\tau=0$ by continuity of every finite
prefix, since the bound is independent of $\tau$. Thus
$E_{t+1}\ge4-O(\log n/\sqrt n)$ uniformly in both time and floor.
The same summation by parts sharpens the mean budget at **every**
prefix length to

$$
m^2\le\sum_t\alpha_t g_t^2
\le W+O\!\left(\alpha_1\frac{\log n}{\sqrt n}\right).
$$

For a uniform prefix $\alpha_1=1/T$ the old term $1/T$ is
therefore replaced by $O(\log n/(T\sqrt n))$. This bound alone
does not supply the short-window mark constraint at long depth.

The subtracted energy terms can also be kept. Define
$V_t=\operatorname{Var}_{i\ne0}\sqrt{\tau+n v_t(i)^2/4}$
and $\beta_t=\alpha_t-\alpha_{t+1}$, with $\alpha_{T+1}=0$.
The between-group formula in
[the fixed-depth calculation](astra-prime-repair-38.md)
gives

$$
\frac{E_{t+1}}{4}=1+\frac{|v_{t,0}|^2}{4}+
\frac{n-1}{n}V_t+O\!\left(\frac{(\log n)^2}{\sqrt n}\right).
$$

The displayed remainder is uniform: the bulk mean of
$\sqrt{\tau+n v_t(i)^2/4}$ is $O(\log n)$ by the bound on
$g_t$, and the marked activation is $O(\log n)$ by
$|v_{t,0}|\le2\sqrt{q/n}\,g_{t-1}$ for $t\ge1$.
Insert the formula in the weighted energy telescope and use
$E_1/4=1+O(n^{-1/2})$ to obtain

$$
\sum_t\alpha_t g_t^2 =
W-\sum_t\beta_t\left[\frac{|v_{t,0}|^2}{4}
                    +\frac{n-1}{n}V_t\right]
+O\!\left(\alpha_1\frac{(\log n)^2}{\sqrt n}\right).
$$

This identity retains both the marked and the bulk charges
at arbitrary depth. The uniform window in Section 1 is used
only when the marks have to be close to one for the obstruction.
