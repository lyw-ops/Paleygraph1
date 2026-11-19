# Reciprocal quadratic regularization at zero bulk floor

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the zero-floor problem has an exact regularization by two strictly convex quadratic programs. They are reciprocal at every positive parameter. At the endpoint they give ordinary theta. The regularized problem also equals zero-floor damping, with an a posteriori bracket controlled quadratically by its residual. The endpoint comparison reduces the conjecture to a family of moving widths of order $p^{-1/2}$.

## A reciprocal pair of nonnegative quadratic programs

Write $n=(q-1)/2$, $J=\mathbf1\mathbf1^*/n$, $K^2=I-J$, $K\mathbf1=0$, and $P_\sigma=(I-J+\sigma K)/2$. For $0<r\le1$ put

$$ Q_\sigma(r)=J+rP_\sigma+r^{-1}P_{-\sigma},\qquad
M_\sigma(r)=\min_{b\ge0,\ b_0=1}\langle b,Q_\sigma(r)b\rangle. \tag{1} $$

The strict convexity gives a unique minimizer $b$. Its KKT conditions say $\alpha=Q_\sigma(r)b\ge0$ off the mark, with $\alpha_i b_i=0$ there. In particular $\alpha_0=M_\sigma(r)>0$. Since $Q_{-\sigma}=Q_\sigma^{-1}$, the vector $\alpha/M_\sigma$ has anchor one, is nonnegative, and satisfies the opposite KKT conditions: its image under $Q_{-\sigma}$ is $b/M_\sigma$. Therefore

$$ M_+(r)M_-(r)=1. \tag{2} $$

Let $A_\sigma(r)$ be the minimizer at anchor one divided by $\sqrt{M_\sigma(r)}$. The two spectra satisfy

$$ A_{-\sigma}=Q_\sigma A_\sigma,\quad
A_{+,0}A_{-,0}=1,\quad A_{+,i}A_{-,i}=0\ (i\ne0),\quad
\langle A_\sigma,Q_\sigma A_\sigma\rangle=1. \tag{3} $$

Their common normalized mass is $c(r)=\langle \mathbf1/\sqrt n,A_\sigma\rangle$, since $JQ_\sigma=J$.

## Endpoint and the moving width

Let $\theta_\sigma$ denote the ordinary theta value in sector $\sigma$. At the endpoint $M_\sigma(0):=n/\theta_\sigma^2$ is the minimum of $\|Jb\|_2^2$ over $b\ge0,\ b_0=1,\ P_{-\sigma}b=0$. A minimizing endpoint vector can be chosen with $b_i\le1$ for all $i$. In fact any such minimizer has this bound: translating its highest value to the mark preserves the feasible Fourier sector, and renormalizing a value larger than one would strictly improve the objective.

Testing (1) on that minimizer gives

$$ M_\sigma(r)\le M_\sigma(0)+r\|P_\sigma b\|_2^2
\le M_\sigma(0)+r\sqrt{n M_\sigma(0)}. \tag{4} $$

The last inequality uses $\|b\|_2^2\le\sum_i b_i$. Apply (4) to the opposite sign and invert using (2) and $\theta_+\theta_-=n$. The elementary $\theta_\sigma\le1+\sqrt q$ from the Jacobi entry bound gives $M_\sigma(0)$ uniformly bounded away from zero. Thus

$$ |\log M_\sigma(r)-\log M_\sigma(0)|\le C r\sqrt q. \tag{5} $$

This gives continuity at zero at each field and an endpoint approximation uniform in the field at widths $o(q^{-1/2})$. In particular the original conjecture is equivalent to

$$ \lim_{c\downarrow0}\limsup_{p\to\infty}
        |\log M_+(c/\sqrt p)|=0. \tag{6} $$

The square obstruction survives at the same scale. At $q=s^2$ let $H$ be the frequency annihilator of $\mathbb F_s^\times$, of size $(s+1)/2$. The anchored positive vector $b=\mathbf1_H$ is feasible in the plus sector because its inverse Fourier support is the positional subfield. It gives the exact test

$$ M_+(r)\le \frac{|H|^2}{n}+r\left(|H|-\frac{|H|^2}{n}\right). \tag{7} $$

Consequently $\limsup_{s\to\infty} M_+(c/s)\le(1+c)/2$. This already separates squares from the desired value for each fixed $c<1$. At $r=o(1/s)$, (5) recovers $M_+(r)\to1/2$ using $\theta_+=s-1$.

## Damped fixed point and an exact residual bracket

Let $\Phi(z)_i=|z_i|$ off the mark and $\Phi(z)_0=\sqrt{z_0^2+4}$, and set $d=(1-r)/(1+r)$. The spectra in (3) give $z=A_+-A_-$, which is mean zero, and $u=A_++A_-=\Phi(z)$. The relation $A_-=Q_+ A_+$ gives $z=dKu$ separately on the two sectors. Conversely any fixed point of this equation yields (3) by resolving the same relation in both sectors, then using pointwise products $A_{+,0}A_{-,0}=1$ and $A_{+,i}A_{-,i}=0$ on the bulk. The contraction constant is $d$ at positive $r$. Also $\|z\|_2^2\le4d^2/(1-d^2)$ follows from $\|u\|_2^2=\|z\|_2^2+4$. The [fixed-width proof](parallel-fixed-width-13.md) verifies the local-inertia and Mellin inputs and passes through the zero bulk floor directly by even-polynomial approximation in normalized $\ell_2$. It proves $M_\sigma(r)\to1$ locally uniformly for $r>0$ through primes and squares. A [quantified extension](slow-width.md) allows a slowly decreasing cutoff. The scale in (6) remains open.

For any approximate mean-zero $z$, form $A_\pm=(\Phi(z)\pm z)/2$ and $E_\sigma=\langle A_\sigma,Q_\sigma A_\sigma\rangle$. With the residual $e=z-dK\Phi(z)$, the following identities and inequalities are exact:

$$ E_++E_--2=\frac{(1+r)^2}{4r}\|e\|_2^2=:\varepsilon,
\qquad E_+E_-\ge1. \tag{8} $$

Indeed $E_++E_--2=\|A_+-Q_-A_-\|_{Q_+}^2$ since $\langle A_+,A_-\rangle=1$. On the plus subspace the difference inside the norm equals $(1+r^{-1})P_+e/2$ and on the minus subspace it equals $(1+r)P_-e/2$. Applying the metric gives the equal factors in (8). The product inequality is Cauchy–Schwarz in the two inverse metrics.

The positive trials are admissible after division by their marked entries. Equation (2) therefore gives, for $m(r)=-\frac12\log M_+(r)$ and $m(z)=\operatorname{arsinh}(z_0/2)$,

$$ m(z)-\tfrac12\log E_+\le m(r)\le m(z)+\tfrac12\log E_-. \tag{9} $$

The bracket has width at most $\log(1+\varepsilon/2)$ by (8). This is a finite-order certificate for the **regularized** value, which can be combined with (5) for an ordinary theta bound. For exact arithmetic the energies in (9) can instead be computed from any positive anchored trial pair using two Parseval sums and no verification of iterates.

## Signed energy at the endpoint

The unique minimizers of (1) vary continuously for $r>0$, by strict convexity and local uniform coercivity. The derivative of the value is the partial derivative of the objective at its minimizer. Using (3) and converting to the normalized spectra gives

$$ \frac{d m(r)}{d\log r}=\tfrac12 (S_-(r)-S_+(r)),\qquad
S_\sigma(r)=r\|P_\sigma A_\sigma(r)\|_2^2,
\qquad S_+(r)+S_-(r)=1-c(r)^2. \tag{10} $$

Here $P_{-\sigma}A_\sigma=rP_{-\sigma}A_{-\sigma}$. The energy relation follows by expanding the last identity in (3). For $m(1)=0$, integration of (10) recovers the endpoint $m(0)=\log(\theta_+/\sqrt n)$. The density in (10) is bounded, but the log-width interval is unbounded. Removing the contribution below $c/\sqrt p$ costs at most $O(c)$ by (5). Through primes, the remaining estimate is on the signed integral beyond this moving cutoff. The two nonnegative energies separately need not be small.

On any fixed support $S$ of the normalized minimizer in (1), the exact expression is $M_\sigma(r)^{-1}=(Q_{\sigma,SS}(r)^{-1})_{00}$. The compressed metric has the form

$$ Q_{\sigma,SS}(r)=\frac{1-r^2}{r}\left[(P_{-\sigma})_{SS}
 +\frac{r^2}{1-r^2}I_S+\frac r{1+r}J_{SS}\right]. $$

The support can change with $r$. A spectral estimate used on this formula must apply to the actual compression or certify the support against its KKT inequalities. Even when most eigenvalues are far from zero, the resolvent can be dominated by a marked overlap in the small spectral window.

## Switching loss between two regularization widths

For $0<r<1$, write $X_r=z(r)/(1-r)$ and $U_r=(c(r),\sqrt r X_r)$ in $\mathbb R\oplus\mathbb R^n$. Equation (3) becomes

$$
 A_+(r)=c(r)j+P_+X_r-rP_-X_r,\qquad
 A_-(r)=c(r)j+rP_+X_r-P_-X_r,
 \qquad \|U_r\|_2=1,
$$

where $j=\mathbf1/\sqrt n$. For two widths $r,s$ define the nonnegative switching cost

$$ F_{r,s}=\sum_{i\ne0}\big(A_{+,i}(r)A_{-,i}(s)+A_{-,i}(r)A_{+,i}(s)\big). $$

At a bulk coordinate this is nonzero only for opposite signs of $z_i(r)$ and $z_i(s)$. Expanding the two cross-products over the Fourier sectors gives

$$ \cosh(m(r)-m(s))+\tfrac12F_{r,s}
 =c(r)c(s)+\tfrac{r+s}{2}\langle X_r,X_s\rangle. $$

Since $\|U_r\|=\|U_s\|=1$, the equality can be written as the loss identity

$$ \boxed{\quad
 2(\cosh(m(r)-m(s))-1)+F_{r,s}+\|U_r-U_s\|_2^2
  =(\sqrt r-\sqrt s)^2\langle X_r,X_s\rangle .\quad} \tag{11} $$

This gives a finite lower test for the energy used by changes away from the mark. It also gives width monotonicities for the total, unsigned spectrum. Use $c(r)^2=1-r\|X_r\|^2$ in the cross-product equality and drop its positive deficits. Then

$$ (\|X_r\|_2-\|X_s\|_2)(r\|X_r\|_2-s\|X_s\|_2)\le -(c(r)-c(s))^2. $$

It follows that $\|X_r\|_2$ decreases with $r$ and $r\|X_r\|_2$ increases with $r$. This controls the total mass regimes without deciding the difference of the two sign energies in (10).

Within a support interval the switching cost is zero for nearby $r,s$. There are only finitely many such intervals at each finite order. Indeed the candidate on every support is a rational function of $r$ from the compressed inverse, and its KKT inequalities partition $(0,1)$ into finitely many intervals and points. Letting $s\to r$ in (11) gives at almost every width

$$ \left\|\frac{dU_r}{d\log r}\right\|_2^2+
       \left(\frac{dm}{d\log r}\right)^2=\frac{1-c(r)^2}{4}. \tag{12} $$

Thus a lower bound on the length in squared norm of the true bulk path can force small movement of the marked scalar. This is a zero-floor alternative to the [cross-floor variance budget](parallel-floor-8.md#centered-log-slopes-measured-on-a-mesh). Widths can vary over a diverging log interval, so (12) alone does not justify discarding the part of the path between a fixed width and $c/\sqrt p$.

## Numerical and interval replay

[The FFT probe](../quadratic_theta.py) uses the positive and negative parts of an approximate damped fixed point. It reports their bracket from (9), retaining finite-width information even when the residual is above the target solve tolerance. Trial supports and trial derivatives are labeled separately. With `--certify-max-order`, it rounds each positive anchored vector in the original coordinates, then evaluates its two Parseval sums with complex ball arithmetic. The exact width is the binary rational used by the program. One upper energy and the reciprocal of the other enclose $M_+(r)$ without a residual or support assumption.

There are [96 numerical rows](../data/quadratic-theta.csv) and [32 rational brackets](../data/quadratic-theta-certified.csv). In the first run the residual identity agrees to within $1.4\cdot10^{-15}$, and the largest numerical log-marker bracket has width about $0.000306$. The rational $M_+(r)$ brackets all have width less than $2.2\cdot10^{-12}$. At $r\sqrt q=1/4$ the matching comparisons are as follows.

| Prime order | $m(r)$ | Nearby square | $m(r)$ |
|---:|---:|---:|---:|
| 9413 | $0.0004771355$ | $97^2$ | $0.2283794926$ |
| 37253 | approximately $-0.0004034$ | $193^2$ | between $0.23167$ and $0.23179$ |
| 153649 | approximately $-0.0012361$ | $389^2$ | between $0.23335$ and $0.23366$ |

The first pair comes from the rational brackets. The other rows are numerical. A separate [two-round prime trial](../data/quadratic-theta-large-prime.csv) at $p=1000033$ gives a wide log-marker bracket, about $[-0.01180,0.01348]$ at scaled width $1/4$. The [large square pilot](../data/quadratic-theta-large-square.csv) records the completed width-$4$ row at $997^2$. The interval checker and a dense nonnegative least-squares check at $61,121,401$ independently verify the regularized values. None of the finite comparisons is an all-prime estimate at moving width.
