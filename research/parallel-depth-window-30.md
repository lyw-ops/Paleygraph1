# Growing Mellin depth, marked cancellation, and source-tail precision

Round 30, 2026-11-18. **The prime ordinary-theta asymptotic remains open.**
A checkpoint was saved before the detailed derivation and replay.

This note gives a quantitative growing-depth consequence of the actual
Mellin/convolution closure estimates: at each fixed floor, the actual marks
vanish uniformly up to

\[
T(q)=\log_2^*q-\log_2^*\log_2^*q-O_{\tau,B}(1),
\qquad \max_{t\le T(q)}|v_{t,0}|=O_{\tau,B}(T(q)^{-B}).       \tag{1}
\]

It applies to primes **and** square orders. In particular it upgrades the
square terminal-source obstruction to this explicit growing horizon:

\[
\liminf_{q=r^2\to\infty}
 {\operatorname{Top}_{k_n}(\widehat g_{T(q),\rm bulk})\over T(q)}
 \ge {\rho c_\tau\over C_\tau}>0.                          \tag{2}
\]

The underlying local-inertia and middle-convolution statements are the
geometric package audited in [round 13](parallel-fixed-width-13.md) and
[round 14](parallel-complexity-14.md); their precise quantitative use is
reproduced below. No new formal verification of that package is claimed.
The degree, dimension, rank, and conductor costs are kept explicit, rather
than inferring (1) from fixed-depth convergence.

The terminal-source approximation has a different precision requirement.
Normalized RMS error `delta` costs `sqrt(k) delta` in the **unscaled**
top-`k` source mass. At `k~sqrt(n)` this is `n^(1/4) delta`, and that loss
is sharp without localization information. Sections 6–8 give alternatives
using the actual top-tail error, a uniform-plus-L1 decomposition, or a
joint increment-weighted cutoff. They do not prove the missing prime bound.

The other inputs are [the positive-floor fixed-depth draft](uniform-fixed-depth.md),
[inertia parity](iteration-parity.md), [round 26's actual increment theorem](parallel-activation-26.md),
[round 29's exact terminal source](astra-source-window-29.md), and
[its root-dependent certificate](root-coupled-tail-29.md).
No Gaussian replacement or identification of prime and square arithmetic
laws is made.

## 1. The exact marked forcing must stay in the recurrence

Let `q=2n+1`, `K=K^T`, `K^2=I-J`, `K1=0`, `K_00=-1/n`. For fixed
`0<tau<1` consider the actual relaxed orbit

\[
z_0=0,\qquad z_{t+1}=(1-\rho)z_t+\rho K\Phi(z_t),\quad
\Phi_i(z)=\sqrt{z_i^2+4w_i},\quad
w_0=1,\quad w_{i\ne0}=\tau/n,\quad0<\rho\le1.                \tag{3}
\]

Write `Y_t=sqrt(n) z_t`, `a_t=z_(t,0)`,
`x=sqrt(n) K e_0`, `phi_tau(u)=sqrt(u^2+4tau)`, and

\[
b_t=\sqrt{4+a_t^2}-\sqrt{a_t^2+4\tau/n}\in[0,2].
\]

Then **exactly**, with no bulk replacement at the root,

\[
Y_{t+1}=(1-\rho)Y_t+\rho\{b_tx+K\phi_\tau(Y_t)\},\qquad
a_{t+1}=(1-\rho)a_t+\rho\{-b_t/n+\mathbb E_n x\phi_\tau(Y_t)\}.
                                                               \tag{4}
\]

Here `E_n` is the normalized counting mean. Also
`||x||_(2,n)<=1`, `||x||_infinity<2`, and `||K||_(2->2)<=1`.
The scalar `b_t` is allowed to depend on the field and the actual orbit.
All estimates below are uniform over its whole interval `[0,2]`. Thus we
never compare to a recurrence in which the marked forcing has already
been set equal to two. Either sign of `K` works, changing the displayed
root forcing sign but none of the absolute bounds.

## 2. Quantitative closure and a separate geometric ledger

Use the pure, semisimple, everywhere tame middle-convolution objects with
singularities and punctual constituents only at `1` in `G_m`. A negative
object has quadratic inertia at `1` and no punctual part; an even product
is positive. An odd product has no geometric punctual constituent at `1`.
The quadratic twist of the nonpunctual part of a positive object is
negative. These are the inherited parity statements.

The original sources were checked again: [Katz, Chapters 2 and 4,
especially Corollary 4.2](https://web.math.princeton.edu/~nmk/mellin331.pdf)
give the tensor-compatible good-character fiber functors;
[Rojas-León, Theorem 5.1 and Corollaries 5.7 and 5.9](https://arxiv.org/pdf/1106.1398)
give the local tame convolution rule used by the parity argument. These
sources provide the geometric inputs; the growing-depth bookkeeping here
is a deduction, not a quoted theorem of either source.

Let `D(M)` be convolution dimension and `R(M)` generic rank. The tame
generic-fiber calculation, including the punctual summands, gives

\[
D(M\star N)=D(M)D(N),\qquad
R(M\star N)\le R(M)D(N)+D(M)R(N).                            \tag{5}
\]

For completeness, the two interior singularities on a generic multiplication
fiber are distinct. A geometrically constant summand would identify a
constituent with one lisse at both of those points and tame at both
boundaries, hence with a discarded Kummer constituent. The tame Euler
characteristic therefore has no extra constant-sheaf `H_c^2` term. This is
the stronger generic-fiber bound used in round 14, not the older coarse
bound with an additional `R(M)R(N)`.

For a chosen real negative expression
`F=Re sum c_i A(M_i)`, where `A` is the two-lift Mellin average, put

\[
\mathcal W_2(F)=\sum_i|c_i|(D(M_i)+R(M_i))^2.                 \tag{6}
\]

This is a certificate for the chosen expression, not a minimum over all
representations. Its weight is submultiplicative by (5), dominates the
everywhere sup norm, and increases by at most four under the positive-to-
negative twist, since the latter has dimension and rank both equal to the
old generic rank. It is slightly stronger than round 14's exponent `3/2`;
the advantage is control of unnormalized L1 exceptional errors as well.

For an even real polynomial `P=sum p_j u^j`, define
`S_U(P)=sum |p_j| U^j`. If `W_2(F)<=U`, closure gives a real negative `G`
such that

\[
\begin{split}
\mathcal W_2(G)&\le4S_U(P),\\
\|KP(F)-G\|_{2,n}&\le C S_U(P)/\sqrt q,\\
|\mathbb E_n xP(F)|&\le C S_U(P)/\sqrt q.                    \tag{7}
\end{split}
\]

Here and below the bounded base expression `x` is absorbed in the absolute
constant. To see the actual error cost, for a word of factors `(D_i,R_i)`
the convolution replacement is wrong at at most `2 sum R_i` full
characters, by at most `2 product D_i` at each. Thus its normalized L2
error is at most

\[
{C\over\sqrt q}\Big(\prod D_i\Big)\sqrt{\sum R_i}
\le {C\over\sqrt q}\prod(D_i+R_i)^2.                         \tag{8}
\]

Its **unnormalized** L1 error is at most
`C product(D_i+R_i)^2`. The odd-word mean is the trace at `1`, bounded by
`R(word)/sqrt(q)`, plus its bad-character correction. The punctual trace
there is zero by parity. Expand the two-lift averages and real parts
before applying these statements. The lift choices have total coefficient
weight one, so no exponential lift factor enters (7). Applying `K` is a
normalized L2 contraction. The constant term is killed by `K`.

An unweighted geometric ledger is useful in addition to (6). Suppose the
input list has `N` objects, each with `D<=D_*`, `R<=R_*`, including duals
and the two Kummer lifts if needed. A degree-`m` step can be expanded with
the conservative bounds

\[
\begin{split}
N'&\le4+4N+4(m+1)(4\max(1,N))^m,\\
D_*',R_*'&\le\max\{D_*,R_*,C_0,
                  m\max(1,R_*)\max(1,D_*)^{m-1}\}.           \tag{9}
\end{split}
\]

Indeed a length-`j` word has dimension at most `D_*^j` and rank at most
`j R_* D_*^(j-1)`; after the twist both output dimension and rank are at
most that latter number. Retaining the old terms handles relaxation.
There are no Swan conductors. If conductor means rank plus all Artin
drops at `0,1,infinity`, each nonpunctual object has conductor at most
`4R`; thus the direct-sum conductor is at most `4N R_*`, and its number of
bad full characters at most `2N R_*`. Punctual parts are recorded by `D`
and discarded before the twist. These are bounds for the actual formal
construction, not dimensions of a hypothetical limiting Gaussian space.

## 3. Positive-floor approximation is cheaper than absolute value

Take `U>=max(2,2sqrt(tau))`, `0<epsilon<1`, and set

\[
\varrho=1+\sqrt\tau/U,\quad M=U+3\sqrt\tau,\quad
m=2\left\lceil{\log(2M/(\epsilon(\varrho-1)))\over
                            2\log\varrho}\right\rceil.     \tag{10}
\]

There is an even polynomial `P` of degree at most `m` with

\[
\|P-\phi_\tau\|_{[-U,U],\infty}\le\epsilon,\qquad
S_U(P)\le4M(1+\sqrt2)^{m+1},\qquad
m\le C_\tau U\log(C_\tau U/\epsilon).                       \tag{11}
\]

Proof: in the Bernstein ellipse of parameter `varrho` for `[-U,U]`, the
imaginary part has magnitude less than `sqrt(tau)`. Consequently
`Re(z^2+4tau)>0` there, the principal square root is analytic, and its
modulus is at most `M`. Its Chebyshev coefficients satisfy
`|a_j|<=2M varrho^(-j)`, with odd coefficients zero. Truncating after the
even index `m` costs at most

\[
2M\varrho^{-m}/(\varrho-1)\le\epsilon.
\]

The absolute monomial coefficient sum of `T_j` is at most
`(1+sqrt(2))^j`; summing the geometric majorant gives the second bound
in (11). This proves all constants in (10) are effective. In particular
the precision cost is logarithmic, in place of the `U/epsilon` degree
for absolute value in round 14.

The dependence on the *incoming expression budget* remains costly. Combine
(9)–(11) with (7). If a single resource `U` dominates `W_2(F)`, the sum
of `D+R` over its listed objects, their count, and the base constants, a
valid outgoing resource is bounded by

\[
U'\le\exp\{C_\tau U[\log(C_\tau U/\epsilon)]^2\}.           \tag{12}
\]

This includes the unweighted rank/conductor ledger, even when a very small
coefficient multiplies an object of large rank. Weight alone would not
bound that object's individual rank. A convenient larger recurrence is

\[
U_0\ge\max(C_\tau,\epsilon^{-2}),\qquad
U_{t+1}=2^{C_\tau U_t^2}.                                   \tag{13}
\]

All constants can be enlarged once for the fixed floor, not separately
after seeing a field. Each step's degree is given by (10), the ranks and
dimensions by (9), and the total conductor by the subsequent `O(U)` bound.
The product of the step degrees bounds the expression tree's leaf degree.
Repeated quadratic twists prevent treating that tree as tensor powers of
one fixed base generator.

## 4. A quantitative growing-depth marked theorem

Choose a target horizon `T` and a common accuracy `epsilon`. Starting with
`F_0=0`, construct `F_(t+1)` from the even polynomial in section 3, its
negative replacement in (7), and the **actual** coefficient `b_t` in (4).
For relaxation retain `(1-rho)F_t`. If the resources in (13) satisfy

\[
U_{T+1}\le q^{1/4},                                         \tag{14}
\]

then, by induction,

\[
\delta_t:=\|Y_t-F_t\|_{2,n}
   \le C t(\epsilon+q^{-1/4}),\qquad t\le T.                 \tag{15}
\]

The proof uses only `phi_tau` being one-Lipschitz on the real line,
`||K||<=1`, the polynomial approximation on the bounded field `F_t`, and
(7). It never needs a sup bound on the actual `Y_t`.

For the scalar test use `||x||_(2,n)<=1` to obtain

\[
\begin{split}
|\mathbb E_n x\phi_\tau(Y_t)|
&\le\delta_t+\epsilon+C S_{U_t}(P_t)/\sqrt q,\\
\max_{s\le T}|a_s|
&\le C\{T\epsilon+Tq^{-1/4}+n^{-1}\}.                       \tag{16}
\end{split}
\]

For `rho<1` the marked recurrence in (4) is a convex recursion, so its
maximum is bounded by the maximum of the scalar forcing bounds; no extra
factor `T` is introduced. This estimate is uniform over fixed or even
field-dependent `rho in (0,1]`. The later source lower bound uses fixed
positive `rho`.

Here is the explicit depth count. Set `L=log_2^* q`, fix `B>=1`, and take

\[
T=\lfloor L-\log_2^*L-c_{\tau,B}\rfloor,\qquad
\epsilon=T^{-(B+2)}.                                       \tag{17}
\]

For all sufficiently large `q`, a fixed `c_(tau,B)` makes (14) hold.
Indeed dominate (13) by `V_(j+1)=2^(V_j)` with
`V_0=(U_0+C_tau+2)^4`. Increasing the base constant ensures
`U_j<=V_j^(1/4)` by induction, because
`C_tau sqrt(V_j)<=V_j/4`. Since `U_0` is polynomial in `T`,
`log_2^* V_0<=log_2^* L+O_(tau,B)(1)`. Equation (17) makes
`log_2^* V_(T+1)<=L-2`, hence `V_(T+1)<q` and (14).
Equations (15)–(17) prove (1), including the harmless `Tq^(-1/4)` term.

This is a genuine simultaneous estimate for every depth through `T(q)`.
It uses the same rank/precision majorant on the whole window. It is not a
diagonal selection with an unspecified prime threshold for each depth.
The constants are extremely large; no practical positive window at the
sampled finite fields is asserted.

## 5. How far this is from round 26

Round 26's actual increment envelope

\[
A_{q,t}\le C(t+1)^\alpha,\quad\alpha<1,
\]

would need a horizon of order
`(log q)^(1/(1-alpha))` to reach residual `o(q^(-1/4))`.
For bounded amplitude it already needs `T(q)` proportional to `log q`.
The depth (17) is much smaller. Even a hypothetical resource improvement
`U_(t+1)<=C U_t^a`, `a>1`, with polynomial accuracy costs would generally
certify only `O(log log q)` depths under (14). A resource growing
geometrically with depth, with sufficiently small exponent relative to
the allowed field power, could reach a logarithmic window. Neither such
a resource bound nor a prime increment envelope is proved here.

There is no need for arithmetic marked estimates all the way to the long
round-26 horizon *if* a field-uniform summable increment envelope is proved:
round 26, equation (23), already transfers fixed early marked cancellation
to a later marker. Thus (1) improves the explicit arithmetic window but
does not supply the central missing amplitude input by itself.

## 6. The exact top-tail precision requirement

For fractional `0<=k<=n-1`, write `Top_k` using weights in `[0,1]` of
total mass `k`. Let `Y,F` be scaled endpoint fields and

\[
G_i=\phi_\tau(Y_i)-2\sqrt\tau,\qquad
\widetilde G_i=\phi_\tau(F_i)-2\sqrt\tau,\quad i\ne0.
\]

The actual unscaled source is `g_i=G_i/sqrt(n)`. For `e=Y-F`,

\[
\left|\operatorname{Top}_k(g)-
             \operatorname{Top}_k(\widetilde G/\sqrt n)\right|
 \le {\operatorname{Top}_k(|e|)\over\sqrt n}
 \le\sqrt{k}\,\|e\|_{2,n}.                                 \tag{18}
\]

The first inequality follows from the support-function definition of the
top sum and coordinatewise one-Lipschitz continuity. The second is weighted
Cauchy–Schwarz. The same bound applies to the terminal geometric source
`hat g_T` by convexity, summing the endpoint errors with weights
`rho(1-rho)^(T-1-j)`, whose total is at most one. The root is handled
separately and never charged as a bulk coordinate.

For `k~kappa sqrt(n)`, fixed normalized RMS accuracy is insufficient:

\[
\text{source error}\ \lesssim\sqrt\kappa\,n^{1/4}\delta.
                                                               \tag{19}
\]

This exponent is sharp for unrestricted error vectors: put the same
nonzero error on exactly `k` coordinates and zero elsewhere. Equality
holds in the second inequality of (18). For activation differences the
ratio approaches one as the common positive background tends to infinity.
These are stability examples, not assertions about the actual Paley orbit.

More generally for `2<=r<=infinity`, Hölder gives

\[
{\operatorname{Top}_k(|e|)\over\sqrt n}
 \le k^{1-1/r}n^{1/r-1/2}\|e\|_{r,n}
 \asymp\kappa^{1-1/r}n^{1/(2r)}\|e\|_{r,n}.                 \tag{20}
\]

A fixed finite moment does not remove the field loss. Taking `r` of order
`log n` would do so, but would require moment estimates at growing tensor
degree and the corresponding rank/conductor budget; fixed-word convergence
does not supply them.

Using just (15) to transfer a source statement after division by `T` yields

\[
{\text{source approximation error}\over T}
 \le C\sqrt{k}\{\epsilon+U_{T+1}/\sqrt q\}.                 \tag{21}
\]

Consequently this proof would need `epsilon=o(q^(-1/4))` and
`U_(T+1)=o(q^(1/4))`. The polynomial-in-`T` accuracy used for (1) fails
the first requirement. Replacing it by a field-power accuracy invalidates
the tower-depth calculation: in the convenient majorant (13), already
`U_0>=epsilon^(-2)` exceeds the permitted cap. This shows why **this
particular sufficient budget** does not establish growing-depth source
approximation. It is not a lower bound on the minimal complexity of a
better construction.

In contrast, uniform scaled error `epsilon` costs only
`k epsilon/sqrt(n)=O(epsilon)` in (18). The precise intermediate target
is the localized error `Top_k(|Y-F|)/sqrt(n)=o(T)`, not a global sup norm.

## 7. Sparse exceptions are cheaper; analytic propagation is not free

Suppose a scaled error admits `e=h+eta` with
`||h||_infinity<=epsilon` and unnormalized `||eta||_1<=L`. Then

\[
\text{source error}\le {k\epsilon+L\over\sqrt n}.           \tag{22}
\]

Thus a bounded number of exceptional characters can be harmless even
when their values do not converge pointwise. The L1 word estimate after
(8) is useful here. If the exception is first propagated by `K`, then

\[
\|K\eta\|_\infty\le{\sqrt q\over n}\|\eta\|_1,
\qquad {\operatorname{Top}_k(|K\eta|)\over\sqrt n}
 \le {k\sqrt q\over n\sqrt n}L=O(L/\sqrt n)                 \tag{23}
\]

at `k=O(sqrt(n))`. Accordingly it is wasteful to convert every sparse
Mellin mismatch into a global normalized L2 error and then incur (19).

What remains is the dense *analytic* error. Even when
`||phi_tau(F)-P(F)||_infinity<=epsilon`, applying `K` only guarantees
normalized L2 error `epsilon`, hence a possible `sqrt(k)epsilon` top-tail
cost. Nonexpansiveness says nothing stronger for that localized seminorm.
Repeated dense errors must be controlled in a convolution-stable algebra
or against the actual recipient, or with an additional local estimate.
Keeping sparse corrections exact does not resolve that issue.

There is now a quantitative obstruction to treating the local top-tail
seminorm as a closed replacement norm. [The independent top-tail note,
section 3](top-tail-transfer-30.md#3-the-local-top-seminorm-is-not-stable-under-the-reflection)
proves the following elementary statement. If `|K_ij|<=mu/sqrt(n)`, then
for every integer `1<=k<=n/2` there is a mean-zero error `e` such that

\[
{\operatorname{Top}_k(|(Ke)_{\rm bulk}|)\over
 \operatorname{Top}_k(|e_{\rm bulk}|)}
\ge {1-k/n\over\mu\sqrt{2k\log(4n)/n}}.                    \tag{23a}
\]

To verify it, choose a `k`-sparse Rademacher vector `y` supported off the
root. Hoeffding and a union bound leave a realization with
`||Ky||_infinity<=mu sqrt(2k log(4n)/n)`. Set `e=Ky`. Then
`Ke=P y`, whose absolute value is at least `1-k/n` on all `k` support
coordinates. The denominator is at most `k||e||_infinity`. This proves
(23a), including mean zero since `K1=0`. With common signs on nonroot
inverse pairs, both errors can also be inversion-even; the denominator
constant becomes `2mu sqrt(k log(4n)/n)`. At `k~sqrt(n)` the ratio diverges
at least as `n^(1/4)/sqrt(log n)`.

This verifies an obstruction for unrestricted errors on the mean-zero
space, including the even subspace relevant here. It does not show that
the actual nonlinear Mellin approximation errors realize these vectors.
Thus the localized target after (21) is a valid **transfer condition**,
but it cannot be propagated using a dimension-independent `K` bound on
that seminorm alone. Additional structure of the actual errors must be
retained.

The Banach-algebra argument in `uniform-fixed-depth.md` does control the
full analytic functional calculus at fixed depth. Its spectral-radius
proof, however, is qualitative in the generator and supplies no uniform
growing-depth norm bound. The source precision cannot be inferred from
its existence assertion alone.

Here is a quantitative check on the tempting compact-group improvement.
Let `V` be a fixed direct-sum generator, of fiber dimension `d`, total
generic rank `r`, and let `R` be a constituent of a tensor word of length
at most `m` in `V,V*`. The packing argument of that draft gives, for an
effective constant `A_d`,

\[
R(R)\le A_d(r+1)(m+2)^{3d^2+3},\qquad
\sum_{R\text{ occurring}}D(R)^2\le A_d(m+2)^{2d^2}.          \tag{24}
\]

To track the exponent: set `U=(1+V)(1+V*)`, of dimension `(d+1)^2`, and
`a(g)=|1+tr V(g)|^2/(d+1)^2`. Then
`1-a(g)>=||V(g)-I||_F^2/(d+1)^2`. The Haar mass of a radius-`s` ball is
at least `c_d s^(2d^2)`. With
`N=C_d m^2 log(m+2)`, the multiplicity of `R` in `U^N` is at least
`c_d (d+1)^(2N) D(R) N^(-d^2)`. Comparing total generic ranks bounds
`R(R)` by `C_d(r+1)N^(d^2+1)/D(R)`. Enlarge constants and use
`N<=C_d(m+2)^3` to obtain the first bound in (24). Mutually orthogonal
matrix-coefficient spaces lie in polynomials of degree at most `m` in
`2d^2` matrix entries, proving the second. Constants can, for example,
be bounded by `exp(C(d+1)^6 log(d+2))` by ambient ball packing; their
precise size is immaterial to the following limitation.

After twisting those constituents, a sufficient **new generator dimension**
is bounded by

\[
d'\le A_d(r+1)(m+2)^{5d^2+3},                               \tag{25}
\]

with harmless constants for the two lifts. This is polynomial in `m`
only while the old `d` is fixed. The new generator has the dimensions of
the old generic ranks, and the next polynomial exponent depends on that
new dimension. This estimate supplies no polynomial-in-depth generator
bound and hence no polylogarithmic horizon. It is an upper-majorant
limitation; it does **not** prove the actual generators must grow so fast.

There is a smaller genuine obstruction to constant absolute coefficient
cost: when `U>2sqrt(tau)`, no polynomials converging uniformly to `phi_tau`
on `[-U,U]` can have bounded `S_U`. A bounded such norm gives a normal
family on the complex disk `|z|<U`. A subsequential holomorphic limit
would equal `sqrt(z^2+4tau)` near the real interval, contradicting its
branch points at `+/-2i sqrt(tau)` inside that disk. This proves divergence
with accuracy for that norm, not the tower rate (13). Round 14's first
dimension-one harmonic feedback is an explicit example where collecting
constituents beats naive monomial bookkeeping. A stable counterpart after
successive twists remains missing.

## 8. A joint stability condition for increment-weighted small balls

Round 26's small-ball alternative can avoid estimating an unbounded
weighted second moment. For bulk scaled endpoints `X,Y`, set `D=Y-X`.
Choose any cutoff `0<=f(X,Y)<=1` with

\[
|f(X,Y)-f(\widetilde X,\widetilde Y)|
 \le L(|X-\widetilde X|+|Y-\widetilde Y|).
\]

Write
`M=E_n D^2 f / E_n D^2`, and use tildes for an approximation. Norms here
restrict to the bulk but retain normalization by `n`. With
`d=||D||_(2,n)>0`, `dtilde=||Dtilde||_(2,n)>0`,
`e_D=||D-Dtilde||_(2,n)`, and endpoint errors `e_X,e_Y`,

\[
|M-\widetilde M|
\le {2(d+\widetilde d)e_D+
 L\|\widetilde D\|_{4,n}^2(e_X+e_Y)\over d^2}.              \tag{26}
\]

Proof: change the numerator weights, then the cutoff, then the denominator.
The two weight/denominator changes cost at most
`2 E_n|D^2-Dtilde^2|/d^2`, bounded by the first term. Hölder bounds the
cutoff term by the second. No coordinate maximum is used.

The full sufficient joint rates furnished by (26) are

\[
e_D=o(d),\qquad
L\,{\|\widetilde D\|_{4,n}^2\over d^2}(e_X+e_Y)=o(1).
                                                               \tag{26a}
\]

The first rate implies `dtilde/d->1`. In the useful bounded-kurtosis case,
the **normalized increment direction** obeys
`||Dtilde/dtilde||_(4,n)=O(1)`, equivalently
`E_n|Dtilde|^4/(E_n|Dtilde|^2)^2=O(1)`. Then
`||Dtilde||_(4,n)=O(d)`, and for fixed cutoff Lipschitz constant `L` the
second rate reduces to `e_X+e_Y=o(1)`. This is stronger than merely
bounding the absolute normalized-counting fourth moment of `Dtilde`.

If one knows only `||Dtilde||_(4,n)=O(1)`, with no bound on its ratio to
`d`, a sufficient endpoint rate for fixed `L` is instead
`e_X+e_Y=o(d^2)`. For `d` comparable to `q^(-1/4)`, this requires
`o(q^(-1/2))` endpoint precision; if `d` is smaller the required precision
can be smaller still. Relative increment precision plus arbitrary
`o(1)` endpoint precision therefore does not suffice under the absolute
fourth-moment bound alone.

Near the critical round-26 residual, approximating increments by
subtracting two endpoint approximations would also require endpoint
errors `o(d)` merely to get `e_D=o(d)`. A direct normalized-increment
closure estimate could avoid that subtraction, but neither its bounded
kurtosis nor its prime-uniform small-ball mass is proved here. The
algebraic fact that an increment is source-generated does not establish
either condition. If the cutoff or floor varies with the field, its
factor `L` must remain explicitly in (26a).

## 9. An actual growing-window square obstruction

For clarity all terms needed to apply (1) to the existing finite square
inequality are listed. Let

\[
\begin{gathered}
W=1+(n-1)\tau/n,\quad a=2\sqrt{\tau/n},\quad
B_n=2\sqrt{nW}-na,\quad k_n={B_n\over2-a}-1,\\
C=(1+\sqrt q)\sqrt{W/n},\quad C_n=C+C^{-1},\\
\widehat u_T=\rho\sum_{j<T}(1-\rho)^{T-1-j}\Phi(z_j),\quad
\beta_T=1-(1-\rho)^T,\quad \widehat g_T=\widehat u_T-\beta_T\Phi(0),\\
\bar\eta={1\over T}\sum_{t<T}\operatorname{arsinh}(z_{t,0}/2),\quad
\ell_{q,\tau}=\log{r-1\over\sqrt{nW}}\quad(q=r^2).
\end{gathered}
\]

The exact square theta is `r-1`. The marked discrepancy is therefore at
least `4{cosh((ell_(q,tau)-bar eta)_+)-1}`. The exact norm telescope and
the stationary mass/cap pairing give the finite necessary bound from
round 29:

\[
\begin{split}
\operatorname{Top}_{k_n}(\widehat g_{T,\rm bulk})\ge
{\rho T\over C_n}\left[
4\{\cosh((\ell_{q,\tau}-\bar\eta)_+)-1\}
 +{\|z_T\|^2\over2\rho T}+{1\over T}\sum_{t<T}R_t\right]
-\widehat u_{T,0}-k_n\beta_Ta,\\
R_t={1-\rho\over2}\|z_t-K\Phi(z_t)\|^2
       +\tfrac12\{n^{-1/2}\textstyle\sum_i\Phi_i(z_t)-2\sqrt W\}^2\ge0.
                                                               \tag{27}
\end{split}
\]

This retains the actual scalar reserve and root. Briefly,
`bar b=P hat u_T/(rho T)` and
`bar Delta=-||z_T||^2/(2rho T)-mean R+<P hat u_T,u*>/(rho T)`.
The stationary source has mass `2sqrt(nW)`, baseline `a`, root
`2<=u_0*<=C_n`, and every bulk coordinate at most `u_0*`. Allocating its
remaining mass under that common cap gives
`<P hat u_T,u*><=C_n(hat u_(T,0)+Top_(k_n)(hat u_(T,bulk)))`.
Combining with the marked lower bound proves (27).

Now take `T(q)` from (17), **simultaneously with `q`**, not after fixing
`T`. Equation (1) makes `bar eta=o(1)` and
`hat u_(T,0)=2 beta_T+o(1)=O(1)`. Also

\[
\begin{gathered}
k_n/\sqrt n\to\kappa_\tau=\sqrt{1+\tau}-\sqrt\tau,\quad
k_na\to2\sqrt\tau\kappa_\tau,\\
C_n\to C_\tau=\sqrt{2(1+\tau)}+1/\sqrt{2(1+\tau)},\\
c_\tau=4\left\{\cosh\left(\tfrac12\log{2\over1+\tau}\right)-1\right\}>0.
\end{gathered}
\]

Drop only the nonnegative energy and reserve in (27), divide by `T(q)`,
and let square orders grow. This proves (2). The same proof works for any
`T(q)->infinity` not exceeding the marked window (17). At `tau=.05`,
`c_tau/C_tau` is approximately `0.0978868`. In particular the actual square
terminal source is not `o(T)` anywhere on this entire certified family of
growing horizons. No claim is made for horizons beyond that family or
for a prime/square matching law. At fixed finite square order, late marked
values can approach a nonzero stationary mark, so no contradiction with
eventual convergence is involved.

## 10. Replay and what remains

The standalone [script](parallel-depth-window-30.py) writes only JSONL.
The [33 saved records](parallel-depth-window-30-check.jsonl) contain:

* Exact rational checks of the top-tail Cauchy–Schwarz equality at four
  sizes, the uniform-plus-L1 bound, and three word rank/weight recursions.
* Eight floating Chebyshev checks at `tau=.05,.5`, `U=2,8`, and
  `epsilon=.01,.0001`, with the explicit ellipse bound (10). These use
  quadrature approximations of the Chebyshev coefficients and a grid;
  they are not interval certificates of the analytic lemma.
* Twenty-four floating actual-prefix checks for `q=61,9413,7^2,97^2`,
  `rho=1,1/2`, and `T=8,32,64`. They verify the exact split (4), the
  finite square bound (27), source-tail stability, and the cutoff bound
  (26). No stationary solution is computed.

The largest normalized recurrence-split discrepancy is `2.23e-15`
rounded upward. The deliberately concentrated source perturbation attains
up to `99.85%` of its RMS upper bound, illustrating why the precision loss
should not be silently discarded. The perturbed arrays are used only to
test stability inequalities, not as proposed arithmetic trajectories.

At `rho=1,T=64,tau=.05`, the recorded terminal-source top masses are
`3.91901` at `9413` and `32.99203` at `97^2`; the finite square necessary
lower bound is `8.34560`. These are selected finite-field diagnostics,
not evidence that the enormous threshold in (17) has been reached.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-depth-window-30.py --exact-only

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-depth-window-30.py \
  > research/parallel-depth-window-30-check.jsonl
```

The main arithmetic budget bottleneck is now explicit: degree logarithmic
in accuracy is available at positive floor, but twisting the new tensor
constituents changes the next generator, and the controlled expression
resource still has an exponential feedback. It is not proved that this
feedback is intrinsic to the orbit. The separate source-transfer bottleneck
is sharp in normalized L2 but can be avoided by a genuine localized or
uniform-plus-L1 estimate. A localized norm alone is not stable under `K`,
as the arbitrary-error lower bound (23a) makes quantitative. The unresolved
prime task is to prove such an
estimate on the actual sources, or a compatible relative-increment
small-ball estimate, at a horizon sufficient for the endpoint certificate.
The root-dependent quadratic enclosure of round 29 does not itself give
that missing arithmetic tail estimate.
