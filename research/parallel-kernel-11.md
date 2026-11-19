# The marked kernel as an opposite-sector leakage problem

For Randomstrasse101 Problem 26, the squared norm of the least-norm theta optimizer on its actual support is the reciprocal of the marked kernel atom, times the square of its mark. The paired optimum gives an exact dual test for this norm. On the actual bulk support one can separate a density term from a centered sampling term. On the zero set of any opposite optimum there is also a single linear program that bounds the norm with a prescribed multiplicative accuracy and a small additive error. Both tests use exact sector equations and avoid any threshold on positive eigenvalues. [Problem statement](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) · [Marked kernel identity](endpoint-norm.md#quantities-on-the-actual-support)

## An exact opposite-sector test

Use the [Fourier convention](fourier.md), with cyclic frequency group of order \(n\), \(j=\mathbf1/\sqrt n\), \(V_\sigma=\operatorname{ran}P_\sigma\) and \(U_\sigma=\mathbb Rj\oplus V_\sigma\). Let \(X\) be the least-norm theta optimum of sign \(\sigma\), with mean normalization \(j^TX=1\) and mark \(\alpha=X_0\). Take any opposite optimum \(Y\), in the same normalization, so \(Y_0=1/\alpha\). Put

\[
 b=X/\alpha,\qquad I=\{i\ne0:b_i>0\},\qquad B=\{i:Y_i=0\},\qquad
 H=\|b_I\|^2,\qquad L=\sqrt n/\alpha-1 .
\]

Thus \(I\subseteq B\), \(b_0=1\), \(\sum_I b_i=L\), and \(0\le b_i\le1\) since translating any larger coordinate to the mark would improve the mark. Every vector \(z\in U_\sigma\) supported on \(\{0\}\cup B\) with \(z_0=1\), even signed, has \(j^Tz=z^TY=\alpha^{-1}\). Consequently \(b_B\) minimizes \(\|z_B\|^2\) among the nonnegative solutions of \(P_{-\sigma}z=0\) with this support and mark. The minimum on the actual support \(I\) is the same even if its bulk variables are signed. Indeed, on \(I\) any anchored direction in the kernel can be followed both ways from \(b\) for sufficiently small steps.

For every zero-mean opposite direction \(d\in V_{-\sigma}\), orthogonality gives \(-d_0=b_I^T d_I\). There is a direction \(d^*\in V_{-\sigma}\) such that

\[
 d_I^*=b_I,\qquad d_{B\setminus I}^*\le0,\qquad -d_0^*=H.                 \tag{1}
\]

To see this, minimize \(\tfrac12\|z_B\|^2\) with \(z_B\ge0\) and \(P_{-\sigma}E_B z_B=-P_{-\sigma}e_0\), where \(E_B\) extends by zero. The negative normal of the affine constraint gives \(d^*\), and the coordinate normals of constraints active at zero give \(d_i^*\le0\) there. More explicitly, the polar of the feasible tangent cone is the sum of the equality row space and the nonpositive coordinate normals on \(B\setminus I\). Apply this to \(-b_B\) and use \(-d_0^*=b_I^Td_I^*\). This argument needs neither independent equality rows nor strict complementarity.

The directional and quadratic versions of the test are

\[
\boxed{\begin{aligned}
 \sqrt H
 &=\max\{-d_0:d\in V_{-\sigma},\ \|(d_B)_+\|\le1\}
  =\max\{-d_0:d\in V_{-\sigma},\ \|d_I\|\le1\},\\
 H&=\max_{d\in V_{-\sigma}}\bigl\{-2d_0-\|(d_B)_+\|^2\bigr\}.
\end{aligned}}                                                          \tag{2}
\]

The upper bounds use \(-d_0\le b_I^T(d_I)_+\le\sqrt H\|(d_B)_+\|\) and the corresponding Cauchy bound on \(I\). Equation (1), or its normalized version, gives equality. If \(H=0\), the mark of every opposite direction is zero and all three values are zero. For \(H>0\) the least \(\ell_2\) positive leakage on \(B\) of an opposite direction with \(d_0=-1\) is \(1/\sqrt H\). It is attained with positive leakage \(b_B/H\), whose coordinates are at most \(1/H\) and whose sum is \(L/H\).

Writing \(N=\ker(P_{-\sigma}E_{\{0\}\cup I})\), the marked weight is \(\|\Pi_N e_0\|^2=1/(1+H)\), since \(b\) is the signed least-norm anchored interpolator there. Therefore a uniform bound for (2) on the larger-theta side would supply the endpoint input to the [reciprocal quadratic path](parallel-quadratic-limit-9.md#exactly-which-theta-witnesses-the-path-selects). In particular a diverging endpoint forces a unit mark-loss opposite direction with vanishing positive leakage, even with the coordinate and mass bounds above. The direction can have negative entries at common zeros of the endpoint pair.

## Centering on the actual bulk support

For \(m=|I|>0\), there is an exact split

\[
\boxed{\quad
 H=\frac{L^2}{m}+D,\qquad
 D=\max\{(-d_0)^2:d\in V_{-\sigma},\ \mathbf1_I^Td_I=0,\ \|d_I\|\le1\}.
 \quad}                                                               \tag{3}
\]

In fact \(u=\sqrt n(j-Y)\in V_{-\sigma}\), \(u_I=\mathbf1_I\), and \(u_0=-L\). Thus \(d^*-(L/m)u\) has restriction \(b_I-(L/m)\mathbf1_I\), and its mark is \(-H+L^2/m\). Every sample with zero sum on \(I\) pairs only with \(b_I-(L/m)\mathbf1_I\). Cauchy–Schwarz followed by the centered direction proves (3), with \(D=\|b_I-(L/m)\mathbf1_I\|^2\). For \(m=0\) set both terms to zero.

In particular, along any sequence with bulk support density bounded below and \(\|X\|\to\infty\), the bounded mark and \(L=O(\sqrt n)\) force \(D\to\infty\). There is then an opposite direction with mark \(-1\) satisfying all of

\[
 \mathbf1_I^T d_I=0,\qquad
 \|d_I\|=D^{-1/2},\qquad
 -\,\frac{L}{mD}\ \le d_i\le\frac{1-L/m}{D}\quad(i\in I).
                                                                         \tag{4}
\]

Choose \(d=(d^*-(L/m)u)/D\). The negative sample depth is \(O(1/(\sqrt n\,D))\) under the density premise. The uniform question reduces to a lower bound on \(m/n\) and a bound on the centered mark functional in (3). More precisely, since \(\alpha\) is uniformly bounded above and below by the [constant Fourier witnesses and the product identity](fourier.md), for large fields the norm is uniformly bounded if and only if the density is bounded below and \(D\) is bounded. The previously proved [affine support bound](parallel-low-energy-7.md) at primes gives a lower bound at the \(\sqrt n\) scale. The passage to positive density remains open.

At \(q=h^2\), the exact plus endpoint is \(\alpha\mathbf1_{H_0}\), where \(|H_0|=(h+1)/2\). Thus \(b_I=\mathbf1_I\), \(m=L=(h-1)/2\), and \(D=0\). Its full squared norm is \(h-1\), and the marked kernel weight is \(2/(h+1)\). The square obstruction in (3) comes entirely from the density term, including on squares with additional zeros in \(Y\). This gives an exact contrast with any hypothetical diverging sequence of prime endpoints of positive support density.

### A density bound from a large prime factor of the cyclic order

Let \(\ell\) be any prime divisor of \(n\), and let \(A\le Q\) be the positional subgroup of order \(\ell\). Push a nonzero nonnegative feasible spectrum forward by restricting its characters to \(A\), adding coefficients that have the same restriction. The resulting spectrum on \(\widehat A\) is nonzero and its support has size at most \(m+1\) if the original spectrum has \(m\) active bulk coordinates and a nonzero mark. Its positional transform is the original transform restricted to \(A\), so it vanishes at every \(t\in A\) with \(\chi(1-t)=-\sigma\). The prime cyclic uncertainty principle implies

\[
m\ge \#\{t\in A:\chi(1-t)=-\sigma\}
=\frac{\ell-1-\sigma\sum_{t\in A}\chi(1-t)}{2}
\ge \frac{\ell-1-\sqrt p}{2}.
\]

For the last inequality, expand the subgroup indicator in the \((p-1)/\ell\) multiplicative characters trivial on \(A\). Each resulting complete Jacobi sum against the quadratic character has modulus at most \(\sqrt p\), including the trivial and quadratic exceptions of modulus one. For the uncertainty estimate see [Tao, Theorem 1.1](https://arxiv.org/abs/math/0308286).

If \(n=d\ell\) with bounded \(d\), this gives \(m/n\ge 1/(2d)-O(p^{-1/2})\) and bounds the first term of (3) uniformly along those primes. For example, at \(p=1997\) the subgroup has order 499 and the exact sign counts force \(m\ge242\) on plus and \(m\ge256\) on minus. This leaves the centered response even in the bounded-cofactor case and gives no positive density estimate when the largest prime factor is sublinear in \(n\).

## Genuine nonnegative opposite perturbations

Equality in (2) can change when the opposite direction is constrained to move into the nonnegative cone at every zero of \(Y\). Put

\[
 \rho_B=\max\{-d_0:d\in V_{-\sigma},\ d_B\ge0,\ \|d_B\|\le1\}.
\]

This is the greatest mark-loss per unit \(\ell_2\) leakage over the originally zero coordinates of a genuinely opposite-feasible perturbation. Indeed each admissible direction gives such a perturbation \(Y+\epsilon d\) for small enough \(\epsilon>0\); any opposite-feasible spectrum with the same mean has difference from \(Y\) in that cone. The image \(\{d_B:d\in V_{-\sigma}\}\) is a subspace and the maximum over its intersection with the nonnegative unit ball is attained. For \(H>0\),

\[
 \rho_B\le\sqrt H,\qquad
 \rho_B=\sqrt H
 \quad\Longleftrightarrow\quad b_B\in\{d_B:d\in V_{-\sigma}\}.              \tag{5}
\]

Cauchy–Schwarz gives necessity, including that the maximizing sample must vanish at \(B\setminus I\). Sufficiency follows by taking the sample \(b_B/\sqrt H\). Equivalently, equality is the condition that \(b_B\) minimize squared norm over the signed anchored solutions on \(\{0\}\cup B\). This follows by orthogonality to the kernel of \(P_{-\sigma}E_B\). In particular \(B=I\) suffices for equality.

More quantitatively, for \(K_B=\{d_B:d\in V_{-\sigma}\}\), the cone projection of \(b_B\) onto \(K_B\cap\mathbb R_+^B\) has norm \(\rho_B\). The projection identity gives

\[
 H-\rho_B^2=\operatorname{dist}(b_B,K_B\cap\mathbb R_+^B)^2
 \ \ge\ \frac{(b_B^Th)^2}{\|h\|^2}
 \quad\bigl(0\ne h\in\ker(P_{-\sigma}E_B)\bigr).
\]

Thus a single signed anchored direction certifies a positive gap if its derivative of the squared norm is nonzero.

There is a strict prime example at \(p=97\) on the plus side. In the certified pair, the two even shared zeros are 10 and 21. The exact cyclotomic replay certifies a strictly positive squared-norm derivative in each anchored direction that increases one shared zero and holds the other fixed. With the direction that increases coordinate 10 by one, the lower bound \((b_B^Th)^2/\|h\|^2\) is enclosed by ball arithmetic and gives \(H-\rho_B^2>0.17097\). The solve is over \(\mathbb Q[Z]/(\Phi_{48})\) and counts both coordinates of each inversion pair. [Certified supports and derivative signs](endpoint-norm.md#an-exact-positive-extension-cost-at-p97) · [Gap calculation](../parallel_kernel_11.py)

In the square control both signs satisfy (5) for the canonical pair. For plus, the [forbidden-cell proof](square-endpoint-uniqueness.md#from-pure-jacobi-sums-to-three-types-of-positional-functions) forces every signed spectrum supported on the saturated set \(E=\{0\}\cup B\) and lying in \(U_+\) to have its positional inverse supported on the subfield subgroup. The forbidden-cell steps only use the linear zero equations. Thus its spectrum is constant on each \(H_0\)-coset. No \(H_0\)-coset disjoint from zero can lie wholly in \(E\): its indicator would be in \(U_+\), would pair to zero with the canonical minus \(Y\), and would have positive mean, a contradiction. The signed support kernel therefore has dimension one. At the small square characteristics the same rank follows directly from the [exact modular checks](square-endpoint-uniqueness.md#exhausting-the-small-characteristics). For minus, the canonical minus spectrum already minimizes norm on the full signed slice of its own sector with prescribed mark and mean. Anchoring on the complement of the plus spectrum forces that same mean by pairing.

## A rank-free LP for upper and lower bounds

Fix any exact opposite optimum \(Y\) and its zero set \(B\). Write \(z=e_0+E_B t\), with \(0\le t_i\le1\). For a grid \(0=t_0<t_1<\cdots<t_k=1\) let \(\psi\) be the piecewise linear chord interpolant of \(t^2\). The LP is

\[
 C=\min_{t,\xi}\left\{
 \sum_{i\in B}\xi_i:
 P_{-\sigma}E_B t=-P_{-\sigma}e_0,\quad
 0\le t_i\le1,\quad
 \xi_i\ge(t_\ell+t_{\ell+1})t_i-t_\ell t_{\ell+1}\quad(0\le\ell<k)
 \right\}.
\]

Suppose \(t_{\ell+1}/t_\ell\le r\) for all \(\ell\ge1\). On each positive interval \([a,b]\) the ratio of the chord to \(t^2\) is at most \((a+b)^2/(4ab)\le\gamma=(1+r)^2/(4r)\). On \([0,t_1]\) the additive error is at most \(t_1^2/4\). Hence

\[
 \frac{(C-|B|t_1^2/4)_+}{\gamma}\le H\le C.
                                                                         \tag{6}
\]

Inverting \(1+H\) gives the corresponding lower and upper bounds for the marked kernel atom. Using \(t_1=\varepsilon/\sqrt n\) makes the additive numerator error at most \(\varepsilon^2/4\), independent of field size. A geometric grid needs \(O_r(\log(\sqrt n/\varepsilon))\) chords. LP duality gives the opposite-sector objective

\[
 C=\max_{d\in V_{-\sigma}}
 \left\{ -d_0-\sum_{i\in B}\max_{0\le\ell\le k}(t_\ell d_i-t_\ell^2)\right\}.
                                                                         \tag{7}
\]

It follows by taking the conjugate of \(\psi\) on \([0,1]\), whose maximum can be evaluated at the knots, with the sign of the equality multiplier chosen to give \(-d_0\). Alternatively, any feasible \(t\) gives an upper bound through its chord cost and any opposite direction \(d\) gives a lower bound through (7) and (6). This form allows independently checked bounds from exact Fourier equations and scalar inequalities. If \(Y\) is known only numerically, identification of its zero set is still a separate verification step.

## Prime and square checks

The replay runs both signs at 15 primes through \(4001\) and 11 prime squares through \(61^2\). It uses the previous numerical minimum-endpoint routine for prime candidates and the exact square formulas evaluated in floating point for square candidates. The chord LP starts from the zero set of an ordinary opposite LP optimizer at primes, so this bound computation uses no eigenvalue threshold. Its equality multipliers replay (7). A further linear feasibility solve on the minimum-norm pair checks (1), then subtracts the paired constant direction and checks the mark and energy in (3). At shared zeros it minimizes the maximum absolute residual there with the prescribed sample \(b_I\) and mark \(-H\). The cosine equations in the replay are written in even representatives and the objective counts the full inversion-orbit sizes. The numerical prime support assignments use tolerances. Equation (6) is an exact bound for the corresponding exact LP. The LP endpoints in the table are floating-point estimates. [Replay script](../parallel_kernel_11.py)

With \(r=1.5\) and \(\varepsilon=0.05\), all 52 numerical norms satisfy their LP intervals. The largest observed primal–dual chord discrepancy was \(1.1\cdot10^{-11}\). The bracket in the selected larger-theta rows is for the anchored bulk energy \(H=\|X\|^2/\alpha^2-1\).

| Field order and sign | Actual bulk size \(m\) | \(\|X\|^2\) | \(L^2/m\) | \(D\) | LP bracket for \(H\) |
|---|---:|---:|---:|---:|---:|
| \(97,+\) | 24 | 3.068133 | 1.454454 | 0.595993 | [2.034366, 2.119496] |
| \(173,+\) | 44 | 3.651198 | 1.539739 | 1.077937 | [2.570292, 2.677708] |
| \(401,-\) | 99 | 3.612257 | 1.687868 | 0.815159 | [2.463805, 2.566773] |
| \(1009,-\) | 252 | 3.558946 | 1.791329 | 0.703415 | [2.466474, 2.569556] |
| \(1997,-\) | 498 | 3.736704 | 1.871130 | 0.850126 | [2.685816, 2.798037] |
| \(4001,-\) | 999 | 3.707730 | 1.904881 | 0.786576 | [2.654152, 2.765053] |
| \(19^2,+\) | 9 | 18 | 9 | 0 | [8.639930, 9.000000] |
| \(43^2,+\) | 21 | 42 | 21 | 0 | [20.159971, 21.000000] |
| \(61^2,+\) | 30 | 60 | 30 | 0 | [28.799990, 30.000000] |

The shared-zero test gave an absolute residual of approximately \(0.72236\) for \(p=97,+\) when trying to realize the equality case of (5). All other tested directions could realize that case to the solver tolerance, including \(p=97,-\) and the square cases with extra shared zeros. Reproduce with

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python parallel_kernel_11.py \
  5 13 17 29 41 61 73 97 101 173 257 401 1009 1997 4001 \
  --square-characteristics 3 5 7 11 17 19 23 31 41 43 61
.venv/bin/python endpoint_extension_certificate.py
.venv/bin/python parallel_kernel_11.py --certify-p97-gap
```

The finite results support the split into density and centered leakage. A uniform bound through primes still needs a prime arithmetic estimate that controls both terms in (3), or one that directly excludes the small one-sided leakage in (2).
