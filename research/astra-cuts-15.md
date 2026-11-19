# Signed cuts at the actual potential level set

At the requested width
`r=p^(-1/3)`, the actual common mass satisfies

\[
\boxed{c^2\ge \tfrac12-O(p^{-1/6}).}
\tag{A}
\]

This closes the low-mass alternative left in
[round 14](astra-sampling-14.md#3-the-existing-prime-phase-packing-hierarchy-is-trivial-in-a-broad-mass-range).
In particular, that scalar Hanson–Petridis moment hierarchy is automatically
vacuous on **every actual pair**, for all sufficiently large primes at this
width. The mass floor also shows that a large inverse-density term cannot
be hidden by small mass.

The energy question can be localized to **one high-level cut of the actual
opposite potential**, with threshold `x_i>lambda/sqrt(n)` for any fixed
positive `lambda`. The required arithmetic estimate is the cancellation

\[
\boxed{
\operatorname{Cut}(U)-2\|Nx_U\|^2
       -\frac{2r}{1+r}\frac{L_U^2}{n}
       =o\bigl(p^{-2/3}\log_2^*p\bigr).
}
\tag{B}
\]

On that particular cut, (B) is necessary and sufficient for the requested
`A=o(log_2^* p)`. It retains signs and controls the density and centered
terms together. This note does **not** prove (B) at primes.

Fejér near-optimizers at prime orders satisfy **all indicator-cut laws
simultaneously with error `o(r)`** and have allowed energy much greater
than `log_2^* p`. A bounded **soft cut** gives a negative signed Jacobi
Dirichlet form for these pairs. The form is positive for actual optimizers,
including square orders.

The [ETH problem statement](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/)
was checked on 2026-11-17. The final energy target uses the sign with larger
**ordinary theta**.

## 1. A common-mass floor from the two signed Jacobi rows

The argument works for prime powers `q=1 mod 4`, including the square
controls. Put `n=(q-1)/2`, `j=1/sqrt(n)`, and use

\[
P=P_\sigma,\quad N=P_{-\sigma},\quad
Q=J+rP+r^{-1}N,\quad y=Qx,
\]

where the actual normalized pair obeys

\[
x,y\ge0,\quad x_0=a,\quad y_0=a^{-1},\quad
x_i y_i=0\ (i\ne0),\quad j^Tx=j^Ty=c,
\]

\[
A=\|Px\|^2,\quad B=\|Ny\|^2,\quad
r(A+B)=1-c^2,\quad Nx=rNy,\quad Py=rPx.
\tag{1}
\]

The [Jacobi bound](fourier.md#joint-distribution-on-the-even-modes) used in the preceding notes is
`|K_ij|<=sqrt(q)/n`, with `K_ii=-1/n`.
Consequently the two projection diagonals are

\[
\{d_N,d_P\}=\{1/2,1/2-1/n\},\qquad
N_{0i},P_{0i}\ge-\kappa\quad(i\ne0),
\qquad \kappa=\frac{\sqrt q+1}{2n}.
\tag{2}
\]

Keep the signs in these lower row estimates. Nonnegativity gives

\[
(Nx)_0\ge(d_N+\kappa)a-\kappa c\sqrt n,
\qquad
(Py)_0\ge(d_P+\kappa)a^{-1}-\kappa c\sqrt n.
\tag{3}
\]

Their sum is at least
`2 sqrt((d_N+kappa)(d_P+kappa))-2 kappa c sqrt(n)` by AM–GM.
On the other hand, the projection identities and (1) imply

\[
\begin{aligned}
(Nx)_0+(Py)_0
&\le\sqrt{d_N}\|Nx\|+\sqrt{d_P}\|Py\|\\
&\le\sqrt{(1-1/n)r(1-c^2)}.
\end{aligned}
\]

Define

\[
b_q=\sqrt{(1/2+\kappa)(1/2-1/n+\kappa)},\qquad
\lambda_q=\kappa\sqrt n,\qquad
\epsilon_{q,r}=\tfrac12\sqrt{r(1-1/n)}.
\]

We have proved the finite-order inequality

\[
\boxed{
b_q\le\lambda_q c+\epsilon_{q,r}\sqrt{1-c^2},
\qquad
c\ge\frac{(b_q-\epsilon_{q,r})_+}{\lambda_q}.
}
\tag{4}
\]

Here `b_q=1/2+O(q^(-1/2))` and
`lambda_q=1/sqrt(2)+O(q^(-1/2))`. For `q->infinity, r->0`,

\[
c\ge 1/\sqrt2-O(\sqrt r+q^{-1/2}),\qquad
c^2\ge1/2-O(\sqrt r+q^{-1/2}).
\tag{5}
\]

No root bound was assumed to obtain this. In fact (3) also proves the
uniform root bounds directly: use `c<=1`,
`(Nx)_0<=sqrt(d_N r)` and `(Py)_0<=sqrt(d_P r)` to obtain

\[
a\le\frac{\lambda_q+\sqrt{d_Nr}}{d_N+\kappa},
\qquad
a^{-1}\le\frac{\lambda_q+\sqrt{d_Pr}}{d_P+\kappa}.
\tag{6}
\]

Both right sides tend to `sqrt(2)` as `q->infinity, r->0`.
The use of both root equations matters: keeping only the upper absolute
entry bound on one of them does not produce (4).

At `r=p^(-1/3)`, (5) is (A). The sufficient vacuity threshold from round 14
is `c^2 >= 1/(1+r(T_p-1)) ~ sqrt(2) p^(-1/6)`, where
`T_p=floor((1+sqrt(1+4n))/2)`. Thus it is eventually satisfied without an
extra hypothesis on the actual mass. This conclusion concerns the scalar
phase-packing hierarchy used there, not every possible use of the
Hanson–Petridis theorem.

Let `I={i!=0:x_i>0}`, `m=|I|`, `L=sum_I x_i=c sqrt(n)-a`, and
`D=sum_I(x_i-L/m)^2`. Equations (5)–(6) give, uniformly along the moving
width,

\[
L\asymp\sqrt n,\qquad \frac{L^2}{m}\asymp\frac nm.
\tag{7}
\]

Together with the energy split in round 13, this proves

\[
A=o(\log_2^*p)
\quad\Longleftrightarrow\quad
\frac nm+D=o(\log_2^*p).
\tag{8}
\]

In particular the target requires `m >> n/log_2^*p`. This is a necessary
density bound, not a proof of it. The mass floor does not bound `D`.

## 2. One signed source test controls both terms

There is a convenient uncentered version of the round-13 source test.
It avoids estimating the two terms in (8) separately. Set

\[
\eta=\frac{r^2}{1-r^2},\qquad \beta=\frac r{1+r},\qquad
C_I=N_{II}+\frac\beta n\mathbf1_I\mathbf1_I^T,
\qquad f_I=-a\left(N_{I0}+\frac\beta n\mathbf1_I\right).
\tag{9}
\]

The matrix `C_I` is positive semidefinite; it is not necessary to assert
that it is a contraction. On the **entire actual positive support**,

\[
\boxed{(C_I+\eta I)x_I=f_I.}
\tag{10}
\]

Indeed `Q=(1/r-r)(N+eta I+beta J)`, and `(Qx)_I=0`.
The source includes the signed Jacobi root column and the constant root
correction. No mean parameter is fitted or discarded.

For an arbitrary **signed** vector `h in R^I`, the same resolvent argument
as in round 13 gives

\[
\boxed{
\|x_I\|\le\|h\|+\eta^{-1}\|f_I-C_Ih\|.
}
\tag{11}
\]

Neither a zero-sum condition nor positivity is required of `h`. The proof
uses only the norms of `(C_I+eta I)^(-1) C_I` and
`eta(C_I+eta I)^(-1)`, which are at most one. If

\[
\mathcal K_I=\inf_h\bigl(\|h\|+\eta^{-1}\|f_I-C_Ih\|\bigr),
\]

then

\[
\|x_I\|\le\mathcal K_I\le2\|x_I\|.
\tag{12}
\]

The upper bound uses `h=x_I` only to prove equivalence, not to propose an
independent arithmetic certificate. In particular, at the requested
width a sufficient and, up to constants, necessary **single** source target
on the larger ordinary-theta side is

\[
\boxed{
\|h_p\|=o(\sqrt{\log_2^*p}),\qquad
\|f_{I_p}-C_{I_p}h_p\|
       =o(p^{-2/3}\sqrt{\log_2^*p}).
}
\tag{13}
\]

This controls inverse density and centered energy simultaneously. The
open arithmetic issue is to construct such a trial from the actual
Jacobi column and the actual level set, without already solving for the
unknown large response. The numerical interval example below verifies
that (11) works with a separately rounded signed trial; it does not solve
this uniform construction problem.

## 3. Optimize high–low cuts without losing the signed surplus

For `U subset I`, put `u=x_U`, `L_U=sum_U x_i`, `E_U=||u||^2`, and

\[
\operatorname{Cut}(U)=
\sum_{i\in U,\ j\in\{0\}\cup I\setminus U}
x_i x_j\left(\sigma K_{ij}+\frac{1-r}{(1+r)n}\right).
\]

The sum counts a cross pair once. The exact weighted Jacobi law from
round 14 is

\[
\operatorname{Cut}(U)
=2\|Nu\|^2+2\eta E_U+2\beta L_U^2/n.
\tag{14}
\]

Call the following **signed surplus**, retaining the subtraction of both
large terms,

\[
\mathcal R(U)=\operatorname{Cut}(U)
             -2\|Nx_U\|^2-2\beta L_U^2/n=2\eta E_U.
\tag{15}
\]

For `tau>=0` take `U_tau={i!=0:x_i>tau}`. The low part has energy at most
`tau L`, so

\[
\boxed{
\|x_I\|^2\le\tau L+\frac{\mathcal R(U_\tau)}{2\eta},
\qquad
A\le a^2+\inf_{\tau\ge0}
       \left(\tau L+\frac{\mathcal R(U_\tau)}{2\eta}\right).
}
\tag{16}
\]

There are only finitely many distinct level sets, so finite cut
optimization is possible. If the actual cut values are known exactly,
the expression at `tau=0` is just the bulk energy; this identity by itself
does not improve the energy bound. The use of (16) is to allow an
arithmetic estimate on a cut above a controlled low-energy background.

For any fixed `lambda>0`, use `tau=lambda/sqrt(n)`. Since `L<=sqrt(n)`,

\[
0\le\|x_I\|^2-E_{U_\tau}\le\lambda.
\]

Also `A-||x_I||^2=a^2-c^2-r^2B=O(1)`. Consequently, for either sign,

\[
\boxed{
A=o(\log_2^*p)
\quad\Longleftrightarrow\quad
\mathcal R(U_{\lambda/\sqrt n})
       =o(\eta\log_2^*p).
}
\tag{17}
\]

One can also let `lambda_p=o(log_2^*p)` in the sufficient direction.
This deals with dispersed energy without requiring a spectral band to
carry a fixed proportion of it.

These are actual opposite-potential level sets. With the notation of
round 14,

\[
H=D+(1-r^2)B,\quad t=(1-r)c/(r\sqrt n),\quad
d=-Nx/(\eta H),
\]

we have, whenever `H>0`,

\[
U_\tau=\{i\ne0:d_i>(t+\tau)/H\}.
\tag{18}
\]

Thus (B) specifies the weights, the cut, and the necessary accuracy.
The raw cut is positive, but its positivity only gives a lower energy
inequality. Taking absolute values of the Jacobi conductances, or
discarding `2||Nx_U||^2`, destroys the cancellation in (15).
The entry estimate in (2) does not establish the upper bound in (17).
The term `2 beta L_U^2/n` can itself be of order `r`, already much larger
than the required `r^2 log_2^*p` accuracy.

## 4. Every-cut approximate laws fail; a soft signed cut detects why

Use the genuine-prime Fejér construction from
[round 14, Section 4](astra-sampling-14.md#4-a-sharper-genuine-prime-obstruction-for-local-kkt-residuals).
For either sign and every sufficiently large prime $p\equiv1\pmod4$, take
`k=floor(log_2(p)/4)`, a permitted step of order greater than `2k`, and the
nonnegative even kernel `h` satisfying

\[
Jh=j,\quad Nh=0,\quad h_0=(k+1)/\sqrt n,\quad
Qh=rh+(1-r)j,\quad
E_k=\|Ph\|^2=\frac{k(2k+1)}{3(k+1)}.
\tag{19}
\]

For the actual pair let

\[
\delta=k^{-1/4},\quad u=x+\delta h,\quad
w=y+\delta Qh=Qu,\quad E=u^Tw,\quad
\Omega=\sum_{i\ne0}u_iw_i.
\tag{20}
\]

The previous construction proves `E=1+O(delta)`, relative rooted
objective error `O(delta)`, maxima at the mark, and allowed energy of
`u/sqrt(E)` at least a constant times `sqrt(k)`. Here `r=p^(-1/3)`.
The new floor (5) and root bounds (6) give, in addition,

\[
\boxed{\Omega\asymp\delta.}
\tag{21}
\]

For the lower bound write

\[
E=1+2\delta\langle x,Qh\rangle+\delta^2(1+rE_k),\qquad
\langle x,Qh\rangle
=r\langle x,h\rangle+(1-r)c\ge(1-r)c.
\]

The root product is `u_0w_0=1+O(delta k/sqrt(n))`, and `c` is bounded
below by (5). The upper bound follows from `Omega<=E-1=O(delta)`.

For **any** subset `U` of the bulk, define the cut with weights `u_i u_j`
and the same Jacobi conductance, allowing all coordinates in the
complement. The defect in the actual-cut formula is exactly

\[
\begin{aligned}
&\frac{2r}{1-r^2}\langle u_U,Q u_U\rangle
      -\operatorname{Cut}_u(U)\\
&\hspace{15mm}=\frac{2r}{1-r^2}\sum_{i\in U}u_i w_i.
\end{aligned}
\tag{22}
\]

Every summand on the right is nonnegative. Taking **all bulk coordinates**
attains the supremum, so there is no union bound over cuts:

\[
\boxed{
\sup_U\left|
\frac{2r}{1-r^2}\langle u_U,Q u_U\rangle
-\operatorname{Cut}_u(U)\right|
=\frac{2r}{1-r^2}\Omega
\asymp r\delta=o(r).
}
\tag{23}
\]

Normalization by `sqrt(E)` scales both sides by `1/E` and changes none of
these orders. The normalized allowed energy is `gg sqrt(log p)`, much
larger than `log_2^*p`. Thus **even simultaneous** `o(r)` indicator-cut
accuracy and relative near-optimality do not establish the desired bound.
This does not refute the much sharper estimate (B) on actual optimizers.

There is a stronger signed test of these near-optimizers. Define the
bounded bulk multiplier

\[
z_0=0,\qquad z_i=\frac{\delta h_i}{u_i}\quad(i\ne0),
\qquad 0\le z_i\le1,
\]

with the ratio zero at simultaneous zeros, and let
`v=uz=delta(h-h_0e_0)`. The ground-state expansion for a general reciprocal
pair is

\[
\boxed{
\langle v,Qv\rangle-\sum_i u_iw_i z_i^2
=\frac{1-r^2}{4r}
\sum_{i,j}u_i u_j
\left(\sigma K_{ij}+\frac{1-r}{(1+r)n}\right)(z_i-z_j)^2.
}
\tag{24}
\]

For an **actual** pair and any multiplier with `z_0=0`, the overlap term
is zero, so the right side is at least `r||xz||^2>=0`.

For (20), weighted Cauchy–Schwarz instead gives

\[
\sum_{i\ne0}u_iw_i z_i^2
\ge\frac{\bigl(\sum_{i\ne0}w_i v_i\bigr)^2}{\Omega}.
\tag{25}
\]

The numerator's square root is

\[
\sum_{i\ne0}w_i v_i
=\delta\bigl(\langle x,Qh\rangle
             +\delta(1+rE_k)-w_0h_0\bigr)\gg\delta.
\]

Equations (21) and (25) therefore lower-bound the overlap term by a
positive constant times `delta`. Meanwhile

\[
\langle v,Qv\rangle
\le\delta^2\bigl(1+rE_k+h_0^2Q_{00}\bigr)=O(\delta^2),
\tag{26}
\]

since the omitted cross term is nonpositive,
`Qh>=0`, and `h_0^2 Q_00=O(k^2/(nr))=o(1)`.
It follows that the left side of (24) is at most `-c_0 delta` for an
absolute `c_0>0` at all sufficiently large primes. The unscaled Jacobi
sum on the right is negative of order `r delta`.

This soft signed quadratic condition retains information that a relaxed
indicator-cut error discards. Positivity of all indicator cuts alone
does not in general imply positivity of a signed Dirichlet quadratic
form, so a positive-edge Cheeger argument is not justified here. The
statement proved above is the negative soft form and the uniform
approximate cut law; it does **not** assert that every indicator cut of
the Fejér perturbation is positive.

### The actual potential threshold is also unstable under this perturbation

This can be seen exactly, rather than from a residual norm. With
`t_x=(1-r)c/(r sqrt(n))` and
`t_u=(1-r)(c+delta)/(r sqrt(n))`,

\[
u-r^{-1}w+t_u\mathbf1=x-r^{-1}y+t_x\mathbf1.
\tag{27}
\]

Adding a pure allowed kernel has left the unscaled opposite potential
unchanged but has raised its threshold. Its bulk level set is now

\[
\{i\ne0:u_i-w_i/r>0\}
=\left\{i\ne0:x_i>
       \frac{\delta(1-r)}{r\sqrt n}\right\}.
\tag{28}
\]

At `p^(-1/3)` the new cutoff in `x_i` is of order
`delta p^(-1/6)`, larger than `1/sqrt(n)` by a factor of order
`delta/r -> infinity`. Thus one cannot identify the support of a
near-optimizer with the actual potential level set merely from its small
coordinatewise KKT residual. The finite examples below often have an
empty set in (28) at the asymptotic choice of `delta`; no asymptotic
emptiness assertion is needed for this argument.

## 5. Square controls fail the target at this exact width

The identities, mass floor, and positive signed quadratic condition all
hold over squares. More quantitatively, the preceding work already
forces

\[
\boxed{
A_+(q^{-1/3})\ge c\log_2^*q
\quad\text{for all sufficiently large }q=\ell^2,
}
\tag{29}
\]

where `ell` is an odd prime and plus is the larger ordinary-theta side.
Here is the deduction, using the round-14 moving-width theorem as stated.
Let `T=log_2^*q-log_2^*(log_2^*q)-4` and `s=2/T`.
[Round 14](parallel-complexity-14.md) gives

\[
M_+(s)\ge\exp\left[-2/\sqrt{e^8-1}-o(1)\right].
\]

The exact square value is `theta_+=ell-1`, so
`M_+(0)=n/(ell-1)^2 -> 1/2`.
If `A_+(q^(-1/3))<=T/4`, the
[one-sided comparison](quadratic-fourth.md#a-one-sided-single-width-criterion)
would give

\[
\sqrt{M_+(0)}\ge
\sqrt{\frac{\exp[-2/\sqrt{e^8-1}-o(1)]}{3/2}}
-O(q^{-1/12}\sqrt T).
\]

The right side tends to a number greater than `0.80`, whereas the left
side tends to `1/sqrt(2)<0.71`. This is impossible. Thus one may take
`A_+(q^(-1/3))>T/4` eventually, which implies (29).

For every fixed high–low threshold in (17), the square signed surplus
therefore is at least a positive constant times
`q^(-2/3) log_2^*q`. Any proposed proof of (B) using only finite-field
Jacobi entry bounds, exact cut identities, the mass floor, or positive
signed ground-state forms would also apply to squares and cannot work.
The missing input must distinguish primes on the actual adaptive cut or
on the signed source in (13).

## 6. Replay, certificates, and remaining estimate

[astra-cuts-15.py](astra-cuts-15.py) replays 50 numerical sign/field cases:
15 primes through 153649 and ten prime squares through `389^2`, all at
`r=q^(-1/3)`. Both signs are retained; numerical data do not certify the
ordinary-theta side. The
[JSONL](astra-cuts-15-results.jsonl) records the mass floor, the uncentered
source equation, high-coordinate cuts, high–low bounds, and three Fejér
perturbations per case. It checks all high-coordinate prefixes on small
fields and 32 prefix sizes on larger ones. The universal all-subset
statement (23) is proved algebraically; the script also checks its exact
defect on three representative subsets.

The largest checked numerical identity discrepancy is below `3.2e-12`,
and the largest reported QP residual is below `2e-11`.
Supports use threshold `1e-8`; these floating-point solves are not support
certificates. Selected actual values are:

| `q`, sign | Actual `c^2` | Proved finite lower bound (4), rounded down | `L^2/m` | `D` | `A` |
|---|---:|---:|---:|---:|---:|
| `4001,+` | 0.72718 | 0.29526 | 1.38210 | 0.51564 | 2.15538 |
| `9413,+` | 0.78052 | 0.31583 | 1.50991 | 0.58833 | 2.31434 |
| `153649,+` | 0.90269 | 0.37519 | 1.78795 | 0.71762 | 2.59969 |
| `153649,-` | 0.90269 | 0.37519 | 1.79552 | 0.71781 | 2.61200 |
| `97^2,+` | 0.75204 | 0.31582 | 1.47324 | 1.28160 | 3.02784 |
| `389^2,+` | 0.88100 | 0.37491 | 1.75384 | 1.90178 | 3.79479 |

For example, at `153649,+` the signed soft form on the left of (24) is
approximately `-0.08577` for `delta=0.1`, and `-0.02217` for
`delta=0.025`. At `389^2,+` the corresponding values are `-0.05808` and
`-0.01813`. The finite asymptotic-choice perturbations have only modest
Fejér degrees, so neither energy divergence nor eventual soft negativity
is inferred from small-degree trends; the arguments (19)–(26) prove them
for the genuine-prime construction as `p->infinity`.

The separate `--certificate` mode uses 192-bit Arb at the algebraic width
`r=13^(-1/3)`, checks every strict bulk sign and `|gamma|<1`, and verifies
(10) within `1e-45` on the certified actual supports. It certifies a
positive slack in (4), approximately `0.04560193`.
It then rounds an independently regularized source trial at denominator
`10^12` and applies (11), without a positivity check on the trial. The
minus trial has two negative entries. The resulting bounds for total
bulk energy are `0.41257000` on plus and `12.23536079` on minus, rounded
up; the corresponding actual bulk energies are approximately `0.21608431`
and `0.21558657`. The minus bound is deliberately reported as loose,
not as evidence for a sharp uniform estimate. Full intervals and rational
numerators are in [the certificate JSONL](astra-cuts-15-certificate.jsonl).

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-cuts-15.py --large \
  > research/astra-cuts-15-results.jsonl
.venv/bin/python -B research/astra-cuts-15.py --certificate \
  > research/astra-cuts-15-certificate.jsonl
```

**Localized remaining task.** On the larger ordinary-theta prime side,
prove the signed surplus estimate (B) on the actual set (18), or construct
the signed full-support source approximation (13). The former needs
cancellation at scale `p^(-2/3) log_2^*p`; the latter needs compressed error
`o(p^(-2/3) sqrt(log_2^*p))`. The universal mass floor closes a loophole but
does not give either estimate. Simultaneous `o(r)` cut laws are too weak,
and the exact signed conditions survive the square obstruction. No
prime-only allowed-energy theorem or proof of Problem 26 is claimed.
