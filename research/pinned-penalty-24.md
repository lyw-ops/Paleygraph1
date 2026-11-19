# An exact penalty curve for the fixed-mark defect

The [scaled smoothed-tail criterion](astra-secant-23.md) is equivalent to ordinary theta convergence for [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). Its finite-field objective has an exact scalar description using one-sided quadratic values. The description also identifies precisely when the mass cap stops binding, and replaces the field-first penalty limit by a field-first limit with a small mean slack.

## Exact scalar formula for the minimum defect

Use the Fourier sectors and repair geometry in [anchored repair](anchored-repair-20.md) and [soft tail](soft-tail-21.md). Put $P=P_{-\sigma}$, $\ell=Pe_0$, $\kappa=P_{00}$, $L=P-\ell\ell^\mathsf T/\kappa$, and $M=\mathbf1-\ell/\kappa$. The affine row $Y$ is in $U_{-\sigma}$, with $Y_0=a\sqrt n$ and $\overline Y=\mu$, where $a,\mu>0$. Off the mark the numbers $M_i,h_i$ are the padding and heights from the soft-tail geometry. We use fields with both nonconstant sectors nonempty and with positive padding off the mark.

Let $W\in U_\sigma$ be nonnegative with $W_0=1$, and write $\nu(W)=\sum W/\sqrt n$. The following table gives two normalizations of the off-mark energy and the corresponding minimum defect. All sums omit the mark.

| Energy $e(W)$ | Minimum squared defect $D_q(a,\mu)^2$ |
|---|---|
| $\sum W_i^2/\sqrt n$ | $\min_Y\|Y_-\|_2^2/\sqrt n$ |
| $\sum M_i h_i W_i^2/n$ | $\min_Y\sum ((-Y_i)_+)^2/(M_i h_i)$ |

In either case the exact dual is

$$
D_q(a,\mu)=\max_{W\ge0,\ W_0=1,\ W\in U_\sigma}
\frac{(a-\mu\nu(W))_+}{\sqrt{e(W)}}.
\tag{1}
$$

The upper bound on the ratio is Cauchy–Schwarz using $\langle W,Y\rangle=\mu\sum W$. For the weighted case, minimize the squared norm of the possible dominating nonnegative defect vectors, a closed polyhedron as in anchored repair. A minimizing row obeys $Lw=0$ for $w_i=(-Y_i)_+/(M_i h_i)$ off the mark and $w_0=0$. Put $\gamma=-\ell^\mathsf T w/\kappa$, so $w+\gamma e_0\in U_\sigma$. Pairing this vector with $Y$ gives

$$
\sum_{i\ne0}\frac{((-Y_i)_+)^2}{M_i h_i}
=\gamma(a\sqrt n-\mu)-\mu\sum w.
$$

If the defect is positive and $a\sqrt n>\mu$, then $\gamma>0$. Divide by $\gamma$ to obtain the attaining witness for (1). For $a\sqrt n\le\mu$, the constant row and the nonnegative zero-mark padding $M$ give the target by interpolation. The ordinary norm proof is the same with constant weights. The denominator in (1) is positive because $e_0\notin U_\sigma$.

Define $V_q(R)=\min_W(\nu(W)^2+R e(W))$, with the same anchored constraint and $R\ge0$. Then

$$
\boxed{\quad D_q(a,\mu)^2=\mu^2\sup_{R>0}R\left[\frac{(a/\mu)^2}{V_q(R)}-1\right]_+.\quad}
\tag{2}
$$

For fixed positive $\nu,e$, the maximum of $R(A^2/(\nu^2+R e)-1)$ over $R\ge0$ is $(A-\nu)_+^2/e$. If $A>\nu$, it is attained at $R=\nu(A-\nu)/e$. In (2), $1/V_q(R)$ is a maximum over $W$. Swapping the two suprema and using this scalar maximization proves the formula. For the ordinary energy, the $A_\sigma$ of the [one-sided quadratic](one-sided-quadratic-22.md) obeys $A_\sigma(r)=r+(1-r)V_q(R)$ with $R=r\sqrt n/(1-r)$ for $0<r<1$.

## Contact points and their dependence on the width

For $R>0$ the quadratic has a unique minimizer $W_R$. Write $\nu_R=\nu(W_R)$, $e_R=e(W_R)$, and $A_q(R)=V_q(R)/\nu_R$. The mass term makes feasible sublevels compact and the energy is strictly convex on the off-mark coordinates, which gives continuity of $W_R$. Consequently $V_q'(R)=e_R$ and $V_q(R)-R V_q'(R)=\nu_R^2$. Comparing to any anchored trial by the first-order inequality, then applying Cauchy–Schwarz to the energy cross term, gives

$$
\nu_R\nu(W)+R\sqrt{e_Re(W)}\ge V_q(R).
\tag{3}
$$

For the target $a/\mu=A_q(R)$, (3) proves that $W_R$ attains (1), with

$$
D_q(a,\mu)=\mu\frac{R\sqrt{e_R}}{\nu_R}.
\tag{4}
$$

The contact function $A_q(R)$ is strictly increasing, continuous, and piecewise affine. To see the local formula, on a support face where the sum can vary, the minimum energy at fixed $\nu$ on that face's affine span is $c_2\nu^2-2c_1\nu+c_0$, with $c_2>0$ and $c_2c_0-c_1^2>0$. This follows by projecting in the off-mark energy metric on the affine equations. The least energy on the affine span is positive because it excludes $e_0$. At the interior minimizer, $\nu_R=Rc_1/(1+Rc_2)$, hence $c_1>0$ and

$$
A_q(R)=\frac{c_0+R(c_2c_0-c_1^2)}{c_1}.
$$

If the sum is fixed on the face, both $\nu_R$ and $e_R$ are constant there and $A_q(R)=\nu_R+R e_R/\nu_R$. The fixed-support equality solution is rational in $R$ and its active-set conditions are semialgebraic, so there are finitely many support intervals. The positive slopes and continuity prove strict increase. As $R\downarrow0$, the mass tends to $\nu_*:=\min_W\nu(W)$ and the energy stays bounded at fixed field. As $R\to\infty$ the energy has a strictly positive lower bound at fixed field and $\nu_R$ stays bounded, by comparison to the smallest-energy anchored trial. Thus $A_q$ runs from $\nu_*$ to infinity. For every positive defect there is a unique maximizing width in (2), determined by $A_q(R)=a/\mu$. At zero defect no positive-width contact is needed.

## Exact mass cutoff and mean slack

In this section use the weighted energy and defect. Let $\mathcal H_{q,a,\mu}(\lambda)$ be the smoothed optimum at the specified mark and mean. Scaling the soft-tail dual row by $\lambda$ gives

$$
\lambda\mathcal H_{q,a,\mu}(\lambda)
=\max_{Z\in U_\sigma,\ Z\ge0,\ \sum Z\le\lambda}
\left[a\sqrt n Z_0-\mu\sum Z-\tfrac12\sum_{i\ne0} M_i h_i Z_i^2\right].
\tag{5}
$$

The nonnegative Lagrange multiplier $t$ for the mass bound changes the mean to $\mu+t$. There is strict feasibility for the mass bound at a small positive constant row, so convex duality applies. In the unconstrained mass problem, write $Z=vW/\sqrt n$ with $W_0=1$. The resulting maximum over $v\ge0$ is $(a-(\mu+t)\nu)_+^2/(2e)$. Therefore

$$
\boxed{\quad
\lambda\mathcal H_{q,a,\mu}(\lambda)=
\inf_{t\ge0}\left\{\lambda t+\tfrac12D_q(a,\mu+t)^2\right\}.
\quad}
\tag{6}
$$

For a positive defect let $R_*$ be the unique contact width at mean $\mu$. The unconstrained optimizer has mass

$$
\lambda_* = \frac{(a-\mu\nu_{R_*})\nu_{R_*}}{e_{R_*}}=\mu R_*.
\tag{7}
$$

Thus (5) equals $D_q(a,\mu)^2/2$ exactly for $\lambda\ge\lambda_*$. For the converse, the quadratic in (5) is strictly concave in the off-mark coordinates, and those coordinates determine the mark since $e_0\notin U_\sigma$. The unconstrained optimizer is unique, so the value is strictly smaller if it exceeds the allowed mass. At zero defect both values are zero and $\lambda_*=0$. The identity $\lambda_*=D_q(a,\mu)^2/(a/\nu_{R_*}-\mu)$ shows how a nonvanishing exact-mark squared defect can coexist with vanishing finite-penalty tails if the endpoint margin itself tends to zero.

The cutoff can be enclosed without identifying the contact support. For $f(\mu)=D_q(a,\mu)^2/2$, the unconstrained form of (5) is a maximum of affine functions of $\mu$, so $f$ is convex. Its optimizer varies continuously on compact positive-mean intervals by uniqueness and coercivity in the off-mark coordinates. Comparing the two optimizers at nearby means gives $f'(\mu)=-\lambda_*$ from the mass term. In particular, finite difference bounds give

$$
\frac{f(\mu)-f(\mu+\epsilon)}{\epsilon}
\le\lambda_*
\le\frac{f(\mu-\epsilon)-f(\mu)}{\epsilon},
\qquad 0<\epsilon<\mu.
$$

In place of exchanging the two limits noted in [Astra's finite-radius comparison](astra-dynamics-24.md), there is an exact field-first identity:

$$
\boxed{\quad
\lim_{\lambda\to\infty}\limsup_q\lambda\mathcal H_{q,a,\mu}(\lambda)
=\lim_{\epsilon\downarrow0}\limsup_q\tfrac12 D_q(a,\mu+\epsilon)^2.
\quad}
\tag{8}
$$

Indeed, the choice $t=\epsilon$ in (6) gives an upper bound $\lambda\epsilon+D_q(a,\mu+\epsilon)^2/2$. At fixed $\lambda$ take the field limsup and then let $\epsilon\downarrow0$. In the other direction, split the infimum at $\epsilon$. Since the squared defect is nonincreasing in the mean by (1), the infimum is at least $\min\{\lambda\epsilon,D_q(a,\mu+\epsilon)^2/2\}$. Take the field limsup and then $\lambda\to\infty$ at fixed $\epsilon$. Finally let $\epsilon\downarrow0$. The same argument works with liminf. These identities leave the mean slack in the field-first limit. A proof that the relaxed squared defect tends to zero on both prime signs would establish Problem 26. Its uniform arithmetic estimate remains open.

## A barrier to small corrections from the simplest exact-mark row

The unrestricted weighted descent below starts from the exact row $Y^0=\mu\mathbf1+(a\sqrt n-\mu)\ell/\kappa$. This starting point cannot support a successful repair restricted to a correction radius $o(\sqrt n)$ when $\mu<a\sqrt2$. In fact let $\mathcal H_{q,R}$ denote the [finite-radius optimum](astra-dynamics-24.md) from $Y^0$, with $a,\mu$ fixed. On both signs, as $q\to\infty$ through primes or squares,

$$
\lim_q \mathcal H_{q,R(q)}(\lambda(q))=(a\sqrt2-\mu)_+
\quad\text{if }R(q)=o(\sqrt n),\quad 0<\lambda(q)=o(\sqrt n).
\tag{9}
$$

Off the mark, $\ell_i=-(1+\sigma\lambda_i)/(2n)$ with $\lambda_i=\widehat s(i)$. Consequently the canonical scores $g_i^0=-Y_i^0/M_i$ are $a\sqrt2\,\sigma\lambda_i/\sqrt q-\mu+o(1)$ uniformly, by $\kappa\to1/2$ and the Jacobi bound. The same bound gives an upper limit $(a\sqrt2-\mu)_+$ by taking zero correction. For $0<t<a\sqrt2-\mu$, the [arcsine law of the normalized Jacobi real part](parallel-graph-shapes-23.md) gives a positive density of off-mark positions $S_t=\{i:g_i^0>t\}$. At large $q$ the mass-one selector $v_i=\mathbf1_{S_t}(i)/|S_t|$ satisfies the capacities $v_i\le b_i$, which are of order $n^{-1/2}$. Put $b_{\min}=\min_{i\ne0}b_i$ and $M_{\min}=\min_{i\ne0}M_i$. The smoothed objective on every trial with correction norm at most $R$ is at least

$$
t-\frac{\lambda}{2|S_t|b_{\min}}-\frac{R}{M_{\min}\sqrt{|S_t|}}.
\tag{10}
$$

Indeed use that selector in the objective and Cauchy–Schwarz on its correction pairing. The two errors tend to zero. Sending $t$ to $a\sqrt2-\mu$ proves (9); if that number is nonpositive the upper limit and the zero selector suffice.

A quantitative radius requirement follows by using $E_t=(-Y^0-tM)_+$ off the mark and the mass-one selector $v_i=M_i E_{t,i}/\sum M_j E_{t,j}$ instead. For fixed $t<a\sqrt2-\mu$ its entries are $O(1/n)$, hence admissible. This selector can use negative $t$. The pairing with the starting row is $t+\sum E_{t,i}^2/\sum M_iE_{t,i}$, and since corrections belong to $\operatorname{im}L$, the correction costs at most $R\|L E_t\|_2/\sum M_iE_{t,i}$. The quadratic penalty tends to zero at fixed $\lambda$. For $R=\rho\sqrt n$, this gives

$$
\liminf_q\mathcal H_{q,R}(\lambda)
\ge t+\frac{B(t)^2-\rho C(t)}{\mathbb E_\omega g_t},
\quad
g_t(x)=(a\sqrt2 x-\mu-t)_+,
$$

where $\omega$ is the arcsine law, $B(t)^2=\mathbb E_\omega g_t^2$, and

$$
C(t)^2=\lim_q\|L E_t\|_2^2/n
=\tfrac12\operatorname{Var}_\omega(g_t)-(\mathbb E_\omega[x g_t(x)])^2.
$$

For this limit, write $X=\widehat s/\sqrt q$. The vector $E_t$ is approximated in normalized $\ell_2$ by $g_t(\sigma X)$. Its marked entry was excluded and the off-mark comparison follows uniformly from the canonical scores. The quadratic form $E_t^\mathsf T K E_t/n$ tends to zero. Approximate $g_t$ by fixed polynomials and use $\|K\|\le1$. In the Chebyshev basis, $K$ kills the constant and maps the linear term $X$ to $(n e_0-\mathbf1)/\sqrt q$, whose paired contribution is $O(q^{-1/2})$ for bounded polynomial companions. For higher degrees the [joint Mellin trace proof](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain), applied before the square pushforward, gives asymptotic independence of $K T_m(X)$ from $X$ and zero mean for each such trace. Now use $P=(I-J-\sigma K)/2$ and subtract the root projection. The former gives $\|P E_t\|^2/n\to\operatorname{Var}_\omega(g_t)/2$. The latter costs $(\ell^\mathsf T E_t)^2/(\kappa n)\to(\mathbb E_\omega[x g_t])^2$ by the off-mark column formula.

In particular when $a=\mu=1$, take $t=\sqrt2/3-1$, so $g_t(x)=\sqrt2(x-1/3)_+$. Evaluating the arcsine moments gives $(t\mathbb E g_t+B(t)^2)/C(t)>0.38719$. Hence vanishing of the canonical bounded-radius objective at any fixed positive $\lambda$ requires a radius of at least $0.38719\sqrt n$ asymptotically. This lower bound applies to the canonical starting row. A seed already much closer to a repair is needed for the field-uniform iteration estimate at radius of order $n^{1/4}$.

## Replay at the exact mark

The [script](pinned-penalty-24.py) proposes an exact-mark affine row using accelerated projected gradient for the weighted squared defect. It rounds the correction in the allowed Fourier sector, restores the mark with $\ell$, and encloses the objective with Arb. The same rounded row, with a scalar threshold from the budget equation, certifies upper bounds for (5) at several penalties. A rounded nonnegative witness or the exact square subfield row supplies the lower bounds. The starting mark here is $a\sqrt n$ with $a=1$, independent of any damped reference.

The [main sweep](pinned-penalty-24-certified.jsonl), [million-order sweep](pinned-penalty-24-million-certified.jsonl), [four-million-order sweep](pinned-penalty-24-four-million-certified.jsonl), and [relaxed-mean sweep](pinned-penalty-24-relaxed-certified.jsonl) use the same unrestricted descent. The [separate endpoint runs](pinned-penalty-24-endpoint-certified.jsonl) find dual witnesses by the dense theta LP and round them independently. The [adjacent-mean runs](pinned-penalty-24-cutoff-certified.jsonl), at $\mu=1\pm1/1000$, give cutoff enclosures by the two difference quotients. At $(p,\sigma)=(61,-)$ this yields $\lambda_*\in[0.47725481,0.48133027]$. At $(97,+)$ it yields $[0.01213729,0.01720581]$. The field `dual_mass_threshold_lower` in the JSON records concerns the proposed dual trial. The difference-quotient brackets concern the true optimum.

Representative interval bounds below use $a=\mu=1$ and $\lambda=1$, except for the marked relaxed case. The last column concerns the canonical seed with correction radius $n^{1/4}$. Its bound uses (10) at $t=1/4$, with an interval check of each selected index.

| Field and witness sign | Mean | Lower for $\lambda\mathcal H$ | Upper for $\lambda\mathcal H$ | Lower at the canonical radius |
|---:|---:|---:|---:|---:|
| $9413,+$ | $1$ | $3.28552\cdot10^{-6}$ | $4.34322\cdot10^{-6}$ | $0$ |
| $153649,-$ | $1$ | $0$ | $1.17410\cdot10^{-4}$ | $0.08924$ |
| $1000033,+$ | $1$ | $0$ | $1.74295\cdot10^{-4}$ | $0.15109$ |
| $1000033,-$ | $1$ | $0$ | $9.78763\cdot10^{-10}$ | $0.15077$ |
| $1000033,+$ | $1.003$ | $0$ | $2.07720\cdot10^{-11}$ | $0.15065$ |
| $4000037,+$ | $1$ | $0$ | $1.01453\cdot10^{-4}$ | $0.18071$ |
| $4000037,-$ | $1$ | $0$ | $1.60556\cdot10^{-4}$ | $0.18075$ |
| $389^2,+$ | $1$ | $0.08515799523$ | $0.08515799524$ | $0.08574$ |

At $389^2$ the [exact flat pinned row](square-pinned-22.md) attains equality against the subfield witness in the weighted norm as well. The weight is constant on its negative support. With $h=195$ and $h_I=h-2+2/(h-1)$, the exact cutoff is $(\sqrt n/h-1)/(h_I/h)$, approximately $0.41481530$. At the million-order prime the enclosures for the two signs are finite-field results. The mean-relaxation proof in (8) still needs an estimate uniform over primes.

Independent dense solves checked (2) in eight cases covering both norms and both signs at $61$ and $97$, with maximum error below $2\cdot10^{-14}$. Eight more dense comparisons checked (6) and the onset of (7) at $61$, with maximum error below $3\cdot10^{-13}$. The [earlier smoothed-tail replay](soft-tail-21.py) reuses the rounded dual constructor, and its 24 earlier small-prime records replayed unchanged.

```sh
export VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
.venv/bin/python -B research/pinned-penalty-24.py 9413 37633 153649 \
  --square-roots 97 193 389 --steps 1024 --certify-max-order 153649
.venv/bin/python -B research/pinned-penalty-24.py 1000033 \
  --steps 768 --certify-max-order 1000033
.venv/bin/python -B research/pinned-penalty-24.py 4000037 \
  --steps 512 --certify-max-order 4000037
.venv/bin/python -B research/pinned-penalty-24.py 153649 1000033 \
  --steps 768 --mean 1003/1000 --certify-max-order 1000033
.venv/bin/python -B research/pinned-penalty-24.py 61 97 101 401 809 1997 9413 \
  --steps 1536 --endpoint-dual --certify-max-order 9413
for mean in 999/1000 1001/1000; do
  .venv/bin/python -B research/pinned-penalty-24.py 61 97 \
    --mean "$mean" --steps 1536 --endpoint-dual --certify-max-order 97
done
```
