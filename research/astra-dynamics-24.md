# Bounded root-preserving dynamics at the exact mark

This note gives a field-uniform **optimization error bound**, an exact finite-radius dual, and a square obstruction. It does not prove the prime estimate in [astra-secant-23](astra-secant-23.md):

\[
\lim_{\lambda\to\infty}\lambda\limsup_p\mathcal H_p(\lambda)=0.
\tag{1}
\]

The useful distinction is between optimizing inside a prescribed correction ball and proving that this ball contains a sufficiently good repair. The former now costs a field-independent number of iterations at the natural radius; the latter remains arithmetic. No claim about a new bound on ordinary theta is made.

## 1. Keep the exact mark, mean, and smoothing caps

Use the geometry and capacities of [soft-tail-21](soft-tail-21.md):

\[
P=P_{-\sigma},\quad \ell=Pe_0,\quad \kappa=P_{00},\quad
L=P-\ell\ell^T/\kappa,\quad M=1-\ell/\kappa,\quad b_i=M_i/h_i.
\]

All off-root coordinates have positive \(M_i,h_i\), for sufficiently large orders. Choose any initial row \(Y^0\) in the allowed sector with **exactly** \(Y^0_0=\sqrt n\), \(\overline{Y^0}=1\). Define

\[
\mathcal H_{q,R}(\lambda)=
\min_{x\in\operatorname{im}L,\ \|x\|_2\le R}\Phi_\lambda(Y^0+x).
\tag{2}
\]

This is a compact minimization, and \(\mathcal H_q\le\mathcal H_{q,R}\). The seed can be the output of a fixed-width solve, followed by the exact affine adjustment. Explicitly, if that output is \(X\), with mean \(c\) and root \(a\), take

\[
Y^0=X+(1-c)\mathbf1+(\sqrt n-a-1+c)\ell/\kappa.
\tag{3}
\]

Its correction need not be small. In particular a root deficit of order \(s\sqrt n\) costs order \(s\sqrt n\) in Euclidean norm when repaired by the root column. It must not be charged as \(O_s(n^{1/4})\). The conclusions below apply to any chosen seed, but do not assert that a fixed-width seed has the required radius property.

## 2. Exact dual with a price for nonstationarity

Let \(C=\{0\le v_i\le b_i,\ \sum_{i\ne0}v_i\le1\}\), and put \(w_0=0\), \(w_i=v_i/M_i\). Compact convex minimax gives

\[
\boxed{
\mathcal H_{q,R}(\lambda)=\max_{v\in C}
\left[-\langle w,Y^0\rangle
-\frac\lambda2\sum_{i\ne0}M_i h_iw_i^2
-R\|Lw\|_2\right].}
\tag{4}
\]

Indeed the minimum of \(-\langle w,x\rangle\) on the correction ball is \(-R\|Lw\|\). Unlike the unlimited-slice dual, (4) retains **all** capped nonnegative profiles, and charges rather than discards their nonstationarity.

For any trial \(x\) in the ball, let \(v\) be its exact scalar-threshold maximizer from soft-tail-21. Its dual value in (4) has the exact gap

\[
\boxed{\quad
\Phi_\lambda(Y^0+x)-D_R(v)
=R\|Lw\|-\langle Lw,x\rangle\ge0.\quad}
\tag{5}
\]

Thus one can stop a finite-radius solve with a primal-dual certificate without assuming that a small gradient is an exact Fourier witness. At a boundary optimum the gradient need not vanish: equality means \(x=RLw/\|Lw\|\) when \(Lw\ne0\). A boundary stall must not be reported as an obstruction to the unrestricted repair.

For the scaled target put \(\xi=\lambda w\). Then

\[
\boxed{
\lambda\mathcal H_{q,R}(\lambda)=
\max_{\substack{\xi_0=0,\ \xi_i\ge0\\
M_i\xi_i\le\lambda b_i,\ \sum M_i\xi_i\le\lambda}}
\left[-\langle\xi,Y^0\rangle
-\frac12\sum M_ih_i\xi_i^2-R\|L\xi\|\right].}
\tag{6}
\]

The objective is independent of \(\lambda\); only its feasible set expands. This makes the large-penalty question a question about the **gain minus nonstationarity price** of increasing capped cones. It preserves both caps essential to the field-first limit.

## 3. Field-uniform finite-time dynamics

Write

\[
A_q=\max_{i\ne0}\frac{b_i}{M_i^2}
=\max_{i\ne0}\frac1{M_i h_i}=O(n^{-1/2}).
\]

The smooth objective on \(\operatorname{im}L\) has gradient \(-Lw\) and Lipschitz constant at most \(A_q/\lambda\). Starting with \(x_0=0\), perform

\[
z_{k+1}=x_k+\frac\lambda{A_q}Lw(Y^0+x_k),\qquad
x_{k+1}=z_{k+1}\min\{1,R/\|z_{k+1}\|\}.
\tag{7}
\]

Use factor one when \(z_{k+1}=0\). Every iterate preserves the exact mean and root. Standard projected-gradient descent, proved below, gives

\[
0\le\lambda\bigl[\Phi_\lambda(Y^0+x_k)-\mathcal H_{q,R}(\lambda)\bigr]
\le\frac{A_qR^2}{2k}.
\tag{8}
\]

In particular, for \(R=r n^{1/4}\),

\[
\boxed{\quad
\lambda\Phi_\lambda(Y^0+x_k)
\le\lambda\mathcal H_{q,r n^{1/4}}(\lambda)+\frac{C r^2}{2k},
\quad k\ge1,\quad}
\tag{9}
\]

with \(C\) independent of the field, sign, and penalty. This is an iteration bound, not a constant-time algorithm: each projection still requires the field-size Fourier computation.

For completeness, let \(f(x)=\Phi_\lambda(Y^0+x)\), \(a=A_q/\lambda\), and let \(x_*\) minimize it on the ball. Projection optimality combined with convexity and the descent lemma yields

\[
f(x_{j+1})-f(x_*)\le
\frac a2\bigl(\|x_j-x_*\|^2-\|x_{j+1}-x_*\|^2\bigr).
\]

The same descent lemma shows that the objective is nonincreasing. Summing and using \(\|x_0-x_*\|\le R\) proves (8). Thus (9) requires neither a support-size restriction nor a restricted spectral gap, and remains valid through support switching and changes in the active budget threshold.

### What arithmetic input would complete this route?

For a specified family of exact-mark seeds, it suffices to find finite radii \(r(\lambda)\), independent of \(p\), such that the explicit maximum in (6), with \(R=r(\lambda)n^{1/4}\), satisfies

\[
\limsup_p\lambda\mathcal H_{p,r(\lambda)n^{1/4}}(\lambda)
\le\eta(\lambda),\qquad \eta(\lambda)\longrightarrow0.
\tag{10}
\]

Then (1) follows directly; (9) also constructs finite-depth upper trials with an additional error \(Cr(\lambda)^2/(2k)\). This is only a sufficient radius condition; necessity is not established. The advance is removal of a prime-uniform convergence-rate assumption **inside** that radius. Establishing (10), or a suitable bound on the maximizing near-kernel profiles in (6), remains the critical-support problem.

## 4. Square controls survive every correction radius

At \(q=t^2\) on square plus, take the exact subfield witness \(V=\mathbf1_I/h\), with \(h=(t+1)/2\), and set

\[
d=\sqrt n/h-1>0,\qquad B=h_I/h,\qquad h_I=h-2+2/(h-1).
\]

Its off-root profile satisfies \(LV_{\rm off}=0\). In (6), use \(\xi=(d/B)V_{\rm off}\). Whenever \(\lambda\ge d/B\), this profile obeys both caps (it is the off-root part of a feasible subfield dual of mass at most one before scaling). Pairing with any exact-mark, mean-one seed gives

\[
\boxed{\quad
\lambda\mathcal H_{t^2,R}(\lambda)\ge\frac{d^2}{2B},
\qquad\text{for every }R\ge0.\quad}
\tag{11}
\]

Consequently the limiting lower coefficient is \((\sqrt2-1)^2/2=3/2-\sqrt2\). No assertion of equality at all square orders is needed. Increasing the radius or the iteration count cannot remove this term, since its nonstationarity price is exactly zero. A finite-radius square optimizer may have an even larger objective.

## 5. Why plain squared-defect dynamics can overreach the target

Define the unrestricted weighted squared defect

\[
E_q=\min_Y\sum_{i\ne0}\frac{((-Y_i)_+)^2}{M_i h_i},
\quad Y_0=\sqrt n,\quad\overline Y=1.
\]

Weighted least-squares duality gives

\[
\frac{E_q}{2}=\sup_{\xi\ge0,\ \xi_0=0,\ L\xi=0}
\left[-\langle\xi,Y^0\rangle-\frac12\sum M_i h_i\xi_i^2\right]
=\lim_{\lambda\to\infty}\lambda\mathcal H_q(\lambda).
\tag{12}
\]

The first equality follows either by Fenchel duality or the stationary weighted defect, which completes to a nonnegative opposite witness whenever its value is positive. The second follows by exhaustion of the two caps in (6), after restricting to \(L\xi=0\) as in the unlimited-slice dual. Each fixed field has a finite optimizer; hence its caps eventually cease to bind.

However, (1) takes the field limit **before** removing these caps. In general

\[
\lim_{\lambda\to\infty}\limsup_q\lambda\mathcal H_q(\lambda)
\le\limsup_q E_q/2,
\tag{13}
\]

and equality is not justified. A scalar dual model shows the mechanism: take one positive-margin mass-one profile with margin \(\delta_j=\epsilon_j\downarrow0\) and quadratic cost \(B_j=\epsilon_j^2\), and allow masses \(0\le u\le1\). Then

\[
H_j(\lambda)=\max_{0\le u\le1}(u\epsilon_j-\lambda u^2\epsilon_j^2/2).
\]

For every fixed \(\lambda\), \(\lim_j\lambda H_j(\lambda)=0\), whereas for every fixed \(j\), \(\lim_{\lambda\to\infty}\lambda H_j(\lambda)=1/2\). This is an abstract dual model, **not a realized Paley or Fourier-cone counterexample**. It proves that the proposed limit exchange is unavailable from the scalar optimization and uniform upper energy cap alone. Proving that exact-mark squared-defect descent vanishes would be sufficient, but may impose unnecessary control on vanishing-margin broad profiles. The capped dynamics (7) avoids making that exchange.

## Verification

`astra-dynamics-24-check.py` independently solves the bounded primal in an orthonormal basis of \(\operatorname{im}L\), evaluates the dual certificate (4), and checks the finite-time bound against that feasible dual. It uses the actual prime Fourier signs at orders 61 and 97 and square controls at orders 49 and 121, both signs, penalties 1/2 and 4, and radii 0.1 and 0.4 times \(n^{1/4}\). All 32 primal/dual comparisons and all 2,048 iteration inequalities passed. The seed is the exact-form canonical row \(1+(\sqrt n-1)\ell/\kappa\); this small-order algebra check does not claim to replay the fixed-width solver. Values are floating point, not interval certificates or prime-uniform evidence.

Replay:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-dynamics-24-check.py > research/astra-dynamics-24-check.json
```

Only `research/astra-dynamics-24*` is written by this work. No shared sources, commits, or pushes are changed.
