# A one-sided energy certificate from a larger-width trial

The [one-width criterion](quadratic-fourth.md#a-one-sided-single-width-criterion) for Problem 26 needs the allowed energy of a true optimizer. A nonnegative anchored trial can bound this energy using its gradient on a capped mass set. A split of the gradient lets a large part use this cap while the rest is measured in the inverse quadratic metric. This yields certificates at widths near $q^{-1/3}$ from trials computed at a larger width. The estimates below do not require identifying the active set at the target width.

## A capped gradient split

Fix $Q=Q_\sigma(r)=J+rP_\sigma+r^{-1}P_{-\sigma}$, and let $b_*$ minimize $b^TQb$ subject to $b\ge0$ and $b_0=1$. Write $M=b_*^TQb_*$. Translation and rescaling give $b_{*,i}\le1$: a larger value elsewhere would give a strictly smaller anchored energy. Let $b$ be any trial with $b_0=1$, $0\le b\le1$, $U=b^TQb$, and $g=Qb$. Both $b$ and $b_*$ belong to the compact set

$$\mathcal B_U=\{z:z_0=1,\ 0\le z_i\le1,\ \sum_i z_i\le\sqrt{nU}\}.$$

The mass bound follows from the $J$ term of the quadratic energy. For a real vector $w$, put $D(w)=\max_{z\in\mathcal B_U}\langle w,b-z\rangle\ge0$. The scalar threshold formula is

$$D(w)=\inf_{t\ge0}\left[
 \sum_{i\ne0}w_i b_i+\sum_{i\ne0}(-w_i-t)_+
 +t(\sqrt{nU}-1)\right]. \tag{1}$$

Indeed the dual of maximizing the negative gradient on the bulk box and mass constraint has multiplier $t$ for the mass constraint. Equivalently sort the negative coefficients and fill unit capacities until the permitted mass is used. Any nonnegative threshold gives an upper bound.

Split $g=w+h$ and write $L=\|h\|_{Q^{-1}}$ and $D=D(w)$. Let $e=b_*-b$. Optimality at $b_*$ yields

$$\|e\|_Q^2\le -g^T e\le D+L\|e\|_Q.$$

The first inequality follows from $e^T Qb_*\le0$ by taking $b-b_*$ as a feasible direction. Expanding the energy at $b$ and using the second inequality gives

$$\|e\|_Q\le\frac{L+\sqrt{L^2+4D}}2,qquad
M\ge U-2D-L^2. \tag{2}$$

In particular the allowed energy of the *normalized* optimizer is bounded by

$$\boxed{\displaystyle
\|P_\sigma A_\sigma(r)\|^2 \le
\frac{\left(\|P_\sigma b\|+(L+\sqrt{L^2+4D})/(2\sqrt r)\right)^2}
{U-2D-L^2}}
\tag{3}$$

when the denominator is positive. Here $\sqrt r\|P_\sigma e\|\le\|e\|_Q$ and $A_\sigma(r)=b_*/\sqrt M$. The cap in (1) can absorb a finite exceptional set without charging its coefficients in the reciprocal metric. For example, suppose $w=w_0+k$, where $w_0$ is nonnegative and vanishes on the trial bulk support. Then $D(w)\le\sum_{i\ne0}|k_i|$, since $w_0^T(b-z)\le0$ and every coordinate difference is at most one in absolute value. Thus exceptional errors of such a form with total absolute magnitude $O(r)$ and remaining squared inverse-metric error $O(r)$ suffice for a bounded energy certificate when $U$ is bounded above and away from zero and $\|P_\sigma b\|$ stays bounded. No rate of this strength is proved here for prime orders.

The lower bound in (2) becomes exact if the split is unrestricted:

$$\frac{U-M}{2}=
\min_w\left[D(w)+\frac12\|g-w\|^2_{Q^{-1}}\right].\tag{4}$$

The preceding argument gives one inequality. For equality take $w=Qb_*$ and $h=-Qe$. By optimality the maximum in $D(w)$ is attained at $b_*$, and expansion gives the equality. Thus a useful certificate comes from constructing a split whose two costs can be estimated without solving for $b_*$. It is the capped cost of the signed supporting vector that matters.

## Transporting a trial between two widths

For a larger width $s\ge r$, choose $w=Q_\sigma(s)b$ and $h=(Q_\sigma(r)-Q_\sigma(s))b$. The inverse-metric error is known from the two sector norms of the single trial:

$$
L^2=\frac{(r-s)^2}{r}\|P_\sigma b\|^2
    +r(r^{-1}-s^{-1})^2\|P_{-\sigma}b\|^2. \tag{5}
$$

If $b$ is the exact anchored optimizer at $s$, then $D(w)=0$ at every target width, by the complementary sign condition and $b_0=z_0=1$. Let $E(s)$ denote the sum of the two actual allowed energies at $s$. The reciprocal relation at $s$ makes (5) equal to $(s-r)^2 M_\sigma(s) E(s)/r$. Thus the norm increment $L/\sqrt r$ grows linearly in $(s/r-1)$ for an exact predecessor, even when the active support changes. An inexact predecessor adds precisely the measured capped deficit to (2). Formula (5) charges both allowed energies of the reference pair, so a diverging reference energy can still prevent a uniform estimate at a much smaller width.

More generally $w=\lambda Q_\sigma(s)b$ for any $\lambda\ge0$ gives $D(w)=\lambda D(Q_\sigma(s)b)$. Write $U_s=b^TQ_\sigma(s)b$ and $W=\|Q_\sigma(s)b\|^2_{Q^{-1}}$. The value-error upper bound $2D(w)+L^2$ is a quadratic in $\lambda$, minimized at

$$\lambda=\max\left{0,\frac{U_s-D(Q_\sigma(s)b)}{W}\right}.$$

If $b$ is exact at $s$, the resulting value bound $M_\sigma(r)\ge U_s^2/W$ agrees with the earlier reciprocal lower certificate obtained from its opposite vector at $s$. The split formulation also applies when the signed reference gradient itself has negative entries. The code compares the unscaled transport $\lambda=1$ with the pure cap at the target width.

## Why a small coordinate residual is insufficient

For any capped trial with $Qb\ge0$, (1) simplifies to $D(Qb)=\sum_{i\ne0}b_i(Qb)_i$. The maximizing vector in the definition of $D$ is $e_0$. This cost can be large compared with $r$ even if the residual at every individual coordinate is $o(r)$.

For example, take [the prime Fejér perturbation](astra-sampling-14.md#4-a-sharper-genuine-prime-obstruction-for-local-kkt-residuals) with $x=A_\sigma(r)$, $a=x_0$, $u=x+\delta h$, $r=p^{-1/3}$, and $k$ and $\delta=k^{-1/4}$ as in that construction. Since $u$ is maximal at the mark, $b=u/u_0$ is a capped trial. Positivity and $Qh\ge0$ give

$$
D(Qb)\ge\frac{\delta^2}{u_0^2}\big(h^TQh-h_0(Qh)_0\big)\gtrsim\delta^2.
$$

Here $h^TQh\ge1$, $h_0(Qh)_0=o(1)$, and $u_0$ stays bounded above and away from zero. Also $u^TQu\ge1+\delta^2$ and $h_0=o(\delta)$, so the actual anchored energy error satisfies

$$
U-M=\frac{a^2(u^TQu-1)-2a\delta h_0-\delta^2 h_0^2}{a^2 u_0^2}\gtrsim\delta^2.
$$

By (4), every split of this same trial has $D+L^2/2\gtrsim\delta^2\gg r\log_2^*p$. This rules out converting that coordinatewise residual guarantee alone to the split cost needed for the one-width criterion. The argument allows any common mass of the exact optimizer.

## Interval replay

The [34 rows](../data/quadratic-gap.csv) cover both signs at nine primes through $1000033$ and eight prime squares through $997^2$. The target width is the binary rational generated by `q**(-1/3)` and the reference width is the binary rational generated by multiplying it by $1.5$. The [script](../quadratic_gap.py) rounds the reference anchored coordinates, then encloses (1), (3), and (5) with Arb. The column `numerical_target_energy` uses a separate floating-point solve at the target and can be omitted with `--skip-target-solve`.

| Order and sign | Numerical target energy | Direct cap upper bound | Split upper bound |
|---|---:|---:|---:|
| $61,+$ | 0.97905 | 9.28397 | 2.63881 |
| $9413,-$ | 2.31977 | 19.38623 | 6.40705 |
| $1000033,+$ | 2.70975 | 19.32533 | 7.78730 |
| $1000033,-$ | 2.70396 | 19.46353 | 7.77959 |
| $997^2,+$ | 4.35482 | 104.26168 | 9.51873 |
| $997^2,-$ | 2.66278 | 20.35791 | 8.12053 |

Displayed upper bounds are rounded upward. The split gives the smaller certified bound in every row in this fixed-ratio comparison. At $997^2$ rounding the trial coordinates increases the split upper bound by less than $0.00063$ on either sign. The square controls also have finite upper bounds at the sampled widths. The computations supply no uniform estimate in the order or a distinction between primes and squares at this scale.

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python quadratic_gap.py 13 61 97 401 1997 9413 37253 153649 1000033 --square-characteristics 7 11 19 43 97 193 389 997 --certify-max-order 1000033
.venv/bin/python quadratic_gap.py 13 97 401 --certify-max-order 401 --skip-target-solve
```
