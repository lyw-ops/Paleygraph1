# Ordered changes of the stripped stationary diagonal

Suppose $K$ is the real Paley Fourier involution on the mean-zero space. Use the [stationary notation](stationary-attenuation.md). In particular $P=I-\mathbf1\mathbf1^{\mathsf T}/n$, $e=Pe_0$, $w_0=1$, $w_i=\tau/n$ for $i\ne0$, $W=\sum_i w_i$, and

$$
v=Ku,\qquad u_i^2-v_i^2=4w_i,\qquad D_i=v_i/u_i,\qquad
A_{\pm,i}=(u_i\pm v_i)/2.
$$

The two spectra have mean $\sqrt{W/n}$ and $K P A_\pm=\pm P A_\pm$. Let $F$ be the full stripped diagonal with $F_0=0$ and $F_i=D_i$ elsewhere. Assume $0<\tau\le1$. Fix $\sigma\in\{1,-1\}$ and a strict real diagonal $E$ with $E_0=0$ and $\sigma E_i\le\sigma F_i$ everywhere on the bulk. The opposite sign can approach saturation, including on coordinates whose activation was changed.

For $x_E=(K-PEP)^{-1}e$ put

$$
m_E=(x_E)_0,\qquad
L_E^2=\sum_{i\ne0}(1-E_i^2)(x_E)_i^2,\qquad
g=\sigma(m_F-m_E),\qquad t=1+\sigma m_E,\qquad r=\frac{A_{-\sigma,0}^2}{W}.
$$

The marked value is monotone in the diagonal coordinates since $\partial m_E/\partial E_i=(x_E)_i^2$. Thus $g\ge0$. The weighted bulk norm satisfies

$$
\boxed{\left|\frac{L_E}{\sqrt t}-\sqrt{(1+r)g}\right|\ll\sqrt\tau.} \tag{1}
$$

All constants are uniform in the field order, the sign, and the change. At small floors, a small weighted bulk norm alone does not force a small change in the mark. When $t\to0$, the weighted norm can vanish even for $g$ separated from zero.

## The opposite-spectrum identity

Let $b=A_{-\sigma}$ and $\kappa=n^{-1/2}\sum_i E_i(x_E)_i+1/\sqrt n$. The general [stripped norm identity](stationary-attenuation.md#two-source-identities) gives

$$
m_E^2+L_E^2+\kappa^2=1.
$$

In fact $|m_E|<1$. Equality would give $L_E=0$, so $x_E$ would vanish on the bulk by strictness of $E$. Its mean zero would then imply $m_E=0$. Since $KPb=-\sigma Pb$ and $\bar b=\sqrt{W/n}$, pairing

$$
(K-PEP)Pb=P[(-\sigma-E)b]+\bar b\,PE\mathbf1
$$

with $x_E$ gives

$$
\kappa=\frac{b_0}{\sqrt W}(1+\sigma m_E)+\frac{\sigma}{\sqrt W}\sum_{i\ne0}(1+\sigma E_i)b_i(x_E)_i.
$$

The order of the diagonal implies

$$
\frac{(1+\sigma E_i)b_i}{\sqrt{1-E_i^2}}
=b_i\sqrt{\frac{1+\sigma E_i}{1-\sigma E_i}}
\le b_i\sqrt{\frac{1+\sigma D_i}{1-\sigma D_i}}
=\sqrt{w_i}.
$$

Use Cauchy–Schwarz and write $\kappa=\sqrt r\,t+\xi$, with $|\xi|\le\epsilon L_E$ for $\epsilon=\sqrt{(W-1)/W}$. Set $y=L_E/\sqrt t$, $z=\xi/\sqrt t$, so $|z|\le\epsilon y$. The norm equation becomes

$$
2-t=y^2+(\sqrt{rt}+z)^2 .
$$

It follows that $0\le y\le\sqrt2$ and $\sqrt{rt}\le\sqrt2(1+\epsilon)$. Thus $|y^2-[2-(1+r)t]|\ll\epsilon y$. If $B=2-(1+r)t$ is nonnegative, divide by $y+\sqrt B$ to get $|y-\sqrt B|\ll\epsilon$, with both zero values trivial. If $B<0$, the bound gives $y\ll\epsilon$ directly. Hence

$$
\left|\frac{L_E}{\sqrt t}-\sqrt{[2-(1+r)t]_+}\right|\ll\sqrt\tau .
$$

At $E=F$, the stationary attenuation bound gives $|m_F-D_0|\le\tau$. Also $1+\sigma D_0=2/(1+b_0^2)$, since $A_{+,0}A_{-,0}=1$. The Paley entry bound $\max_{ij}|K_{ij}|\le\sqrt q/n$ together with $\sum_i u_i=2\sqrt{nW}$ bounds $u_0$ uniformly for $\tau\le1$, hence $r$ is bounded. Thus $2-(1+r)(1+\sigma m_F)=O(\tau)$. Using $t=1+\sigma m_F-g$ and taking square roots gives (1).

## Implications for deletion

Assume in addition $|E_i|\le|D_i|$ everywhere on the bulk. The second [stationary source](stationary-attenuation.md#transfer-in-weighted-squared-energy) implies $g\le \tau+(2\sqrt\tau+\sqrt{Q_E})L_E/2$, where

$$Q_E=\sum_{i\ne0}\frac{u_i^2(D_i-E_i)^2}{1-E_i^2}.$$

If $g\le2\tau$, there is no further term. If $g>2\tau$, substitute $L_E^2\ll t(g+\tau)$ from (1), isolate $g/2$, and square. This yields the uniform estimate

$$g\ll\tau+tQ_E. \tag{2}$$

For deletion on a same-sign set $S$ one has $Q_E=\lVert v_S\rVert_2^2$ and $\lVert(x_E)_S\rVert_2^2\le L_E^2\ll t(g+\tau)$. Consequently a deletion with a change bounded below at decreasing floors and $t\to0$ requires $\lVert v_S\rVert_2^2\gg 1/t$, even while the exterior column has vanishing norm on $S$.

There is also a restriction on the compressed exterior inverse. Let $X_E=(K-PEP)^{-1}P$, $C=\operatorname{diag}(\sqrt{|D_i|}:i\in S)$, $N=C(X_E)_{SS}C$, and $\delta=1-\lambda_{\max}(\sigma N)>0$. By the [same-sign deletion formula](parallel-coupling-2.md#stationary-column-and-same-sign-deletion),

$$
g=\langle C(x_E)_S,(I-\sigma N)^{-1}C(x_E)_S\rangle
\le \delta^{-1}\lVert C(x_E)_S\rVert_2^2.
$$

If $g>0$, then $\delta\ll t(1+\tau/g)$. In the [square control](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors), deleting the positive bulk gives $m_E\to-1$ and $g\to4/3$. Therefore the exterior inverse approaches the positive endpoint on the deleted set while its marked column there tends to zero. A prime-field bound keeping $\delta$ positive would exclude that endpoint mechanism for the corresponding deletion. A response change with $t$ bounded away from zero is left open.

## A one-sided reference criterion without diagonal order

For any strict real reference diagonal $E$ with $E_0=0$, retain $b=A_{-\sigma}$ and set

$$
T_\sigma(E)=\sum_{i\ne0} b_i^2\frac{1+\sigma E_i}{1-\sigma E_i}
=\frac{\tau}{n}\sum_{i\ne0}\exp\big(2\sigma[\operatorname{arctanh}(E_i)-\gamma_i]\big).
$$

The same source and Cauchy–Schwarz give $\kappa=\sqrt r\,t+\xi$ with $|\xi|\le\sqrt{T_\sigma(E)/W}\,L_E$, irrespective of the order of the diagonals. Apply Cauchy–Schwarz once more to $|\kappa-\xi|\le|\kappa|+\sqrt{T_\sigma(E)/W}\,L_E$. The norm identity gives

$$
r t^2\le\left(1+\frac{T_\sigma(E)}W\right)(1-m_E^2),
\qquad
A_{-\sigma,0}^2\le\big(W+T_\sigma(E)\big)\frac{1-\sigma m_E}{1+\sigma m_E}. \tag{3}
$$

Thus a family of references with $m_E=o(1)$ and $T_\sigma(E)=o(1)$ at floors tending to zero proves $\liminf \sigma\gamma_0\ge0$. The references can differ for the two signs. Equation (3) requires only one exponential ratio moment for each one-sided assertion. The sign and size of the perturbation on individual coordinates are unrestricted.

The true square comparison quantifies the cost at the obstructed sign. There $A_{+,0}^2\to 2$, so any family of references with $m_E=o(1)$ must have $\liminf T_-(E)\ge1$. At primes a balanced reference with the required ratio moment is still missing.

The reference must allow activation magnitudes approaching one. In fact if $\|E\|_\infty\le\rho<1$, then

$$
T_\sigma(E)\ge\frac{1-\rho}{1+\rho}\sum_{i\ne0} b_i^2
\ge\frac{1-\rho}{1+\rho}\frac{(\sqrt{nW}-b_0)^2}{n-1}.
$$

Since $b_0$ is bounded, this has a positive lower bound at fixed $\rho$ as $n$ grows. A fixed diagonal damping may be used as an intermediate limit, with the ratio estimate still required as damping is removed.

## A lower bound for the two full sign deletions

Let $F_+=\max(F,0)$ and $F_-=\min(F,0)$ coordinatewise. Deleting all activation of sign $+$ or $-$ incurs the corresponding cost $g_+=m_F-m_{F_-}$ or $g_-=m_{F_+}-m_F$. For $E$ supported on a bulk set $S$ and of a single sign, the shift formula with zero reference bounds the increment below by

$$
|m_E-m_{\varnothing}|\ge\frac12\sum_{i\in S}|E_i|(Ke)_i^2,
$$

where $m_{\varnothing}=\langle e,Ke\rangle$ is the inverse entry for the zero diagonal. Indeed the increment is the quadratic form of $(I-\sigma C K_{SS} C)^{-1}$ at $C(Ke)_S$, where $C$ has diagonal $\sqrt{|E|}$ and $I-\sigma C K_{SS} C\le2I$. Consequently

$$g_++g_-=m_{F_+}-m_{F_-}\ge\frac12\sum_{i\ne0}|D_i|K_{i0}^2. \tag{4}$$

In particular, along any family of Paley fields with $0<\tau\le1/8$ and $\|u\|_2^2\le B$ uniformly, the right side stays bounded below by a positive constant depending on $B$. To see this, the bulk set $S=\{i\ne0:\sqrt n\,u_i\ge1\}$ carries at least $\sqrt n/2$ in unnormalized $\ell_1$ mass for large $n$, since $\sum_i u_i=2\sqrt{nW}$ and $u_0$ is bounded. Cauchy–Schwarz gives $|S|\ge n/(4B)$. On $S$ one has $|D_i|\ge1/\sqrt2$. The empirical law of $\sqrt n K_{i0}$ is the rescaled arcsine law from [the two Jacobi lifts](smoothing.md#first-two-iteration-markers) and [Katz's Gauss moment estimate](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf). It has no atom at zero. Choose $a>0$ such that there are eventually fewer than $n/(8B)$ frequencies with $|\sqrt n K_{i0}|<a$. This gives $\sum_{i\in S}K_{i0}^2\ge a^2/(8B)$ in (4).

Thus negligibility of both full sign deletions would already exclude the regime of bounded stationary squared energy. Small deletion costs can still be sought for particular high sets. For the full sign deletions the signed difference and the sum of the two exterior entries are the relevant quantities for cancellation:

$$2m_F=m_{F_+}+m_{F_-}+g_+-g_-.$$

The [marked/constant comparison](stationary-mark-constant.md) gives a further relation for each signed exterior. It compares $1-\sigma m_{F\mathbf1_{I_\sigma}}$ with the analogous defect of the constant source, including on the half-angle diagonal.

## Numerical comparison

The [probe](../stationary_ordered.py) checks the opposite-spectrum identity, the stripped norm and the explicit error bound in (1) in [144 runs](../data/stationary-ordered.csv). The runs cover three prime and square pairs, three floors, both signs and four changes per case. The changes delete the whole sign or just coordinates with $\sigma\sqrt n\,v_i>3.5$, clip one side at $0.8$, or shift every bulk hyperbolic coordinate by $-\sigma/4$. The largest stationary and inverse residuals are $1.0\cdot10^{-10}$ and $2.3\cdot10^{-10}$, respectively. The peak discrepancy in the exact identities is $7.1\cdot10^{-10}$. A separate check of 360 small dense systems, including unordered diagonals, verified the source to within $2.4\cdot10^{-13}$ and found no violation of (3).

| Order at $\tau=0.0005$ | $m_F$ | After deleting $+$ | After deleting $-$ | $g_+$ | $g_-$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $97^2$ | 0.32436 | -0.95440 | 0.65739 | 1.27876 | 0.33303 |
| $9413$ | 0.00043 | -0.57208 | 0.57437 | 0.57251 | 0.57394 |
| $193^2$ | 0.32894 | -0.97398 | 0.66203 | 1.30292 | 0.33309 |
| $37253$ | -0.00041 | -0.57383 | 0.57341 | 0.57343 | 0.57382 |
| $389^2$ | 0.33127 | -0.98401 | 0.66437 | 1.31527 | 0.33311 |
| $153649$ | -0.00124 | -0.57647 | 0.57577 | 0.57523 | 0.57701 |

The three prime examples have large changes in both directions and a small difference of costs. In the square examples deleting the positive bulk moves the exterior mark increasingly close to $-1$, with weighted bulk norms $0.29661,0.22576,0.17768$ respectively. The table consists of floating-point finite orders at a common floor. The vanishing-norm assertion at decreasing floors uses the exact square argument and (1).
