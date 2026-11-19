# Attenuating a stationary diagonal

Let $K$ be the real symmetric Fourier operator with $K^2=P=I-\mathbf1\mathbf1^\top/n$ and $K\mathbf1=0$. Write $w_0=1$, $w_i=\tau/n$ on the bulk, and $W=\sum_iw_i$. At stationarity,

$$
v=Ku,\qquad u_i^2=v_i^2+4w_i,\qquad D_i=v_i/u_i,\qquad M_i^2=1-D_i^2.
$$

We take $u_i>0$ and $M_i>0$. The squared norm identity gives $\bar u=2\sqrt{W/n}$. The argument below uses these algebraic identities at both prime and square orders.

## Two source identities

Let $E$ be any real diagonal with $\|E\|_\infty<1$ and $E_0=0$. On the mean-zero space set $H_E=K-PEP$, $x=H_E^{-1}e$ for $e=Pe_0$, and $m=x_0$. The inverse exists since $K$ is an involution there and $\|PEP\|<1$. Define

$$
k=\frac{\sum_i E_i x_i}{\sqrt n},\qquad
L^2=\sum_{i\ne0}(1-E_i^2)x_i^2,\qquad
\beta=\sum_{i\ne0}(D_i-E_i)u_i x_i.
$$

Expanding $\|x\|_2^2=\|Kx\|_2^2=\|e+PE x\|_2^2$ gives

$$m^2+L^2+(k+1/\sqrt n)^2=1.$$

The first source equation is $H_E Pu=P(D-E)u+\bar u\,PE\mathbf1$. Pairing with $x$ gives $u_0-\bar u=v_0m+\beta+2\sqrt W\,k$. Substitute the resulting value of $k+1/\sqrt n$ into the norm equation. With $A=4W+v_0^2$ and $u_0^2=v_0^2+4$, completing the square yields

$$
\frac{A}{4W}\left(m-\frac{v_0(u_0-\beta)}{A}\right)^2+L^2
=\frac{4(W-1)+2u_0\beta-\beta^2}{A}.
$$

The second source equation is $H_Ev=P[(u-Dv)+(D-E)v]$. The coefficient at zero in the bracket is $4/u_0+D_0v_0=u_0$. On the bulk $u_i-D_iv_i=2\sqrt{\tau/n}\,M_i$, so pairing with $x$ gives

$$
u_0(D_0-m)=\sum_{i\ne0}\left(2\sqrt{\tau/n}\,M_i+(D_i-E_i)v_i\right)x_i.
$$

## Transfer in weighted squared energy

Define

$$
Q_E=\sum_{i\ne0}\frac{u_i^2(D_i-E_i)^2}{1-E_i^2},\qquad
R_E=\frac1n\sum_{i\ne0}\frac{1-D_i^2}{1-E_i^2}.
$$

Cauchy–Schwarz gives $|\beta|\le\sqrt{Q_E}L$. The first source and the norm equation give $A L^2\le 4(W-1)+2u_0\sqrt{Q_E}L$. The second source and $|v_i|\le u_i$ then give

$$
L\le \frac{u_0\sqrt{Q_E}+\sqrt{u_0^2Q_E+4A(W-1)}}{A},
\qquad
|m-D_0|\le\frac{2\sqrt{\tau R_E}+\sqrt{Q_E}}{u_0}L.
$$

If $|E_i|\le|D_i|$ on the bulk, then $R_E\le1$. Since $u_0\ge2$ and $A\ge u_0^2$, the bound on $L$ is at most $\sqrt{Q_E}+\sqrt\tau$. Thus

$$|m-D_0|\le \tau+\frac32\sqrt{\tau Q_E}+\frac12Q_E\le\frac74(\tau+Q_E).$$

For attenuation $E_i=\alpha_iD_i$ with each $0\le\alpha_i\le1$, one has

$$
Q_E=\sum_{i\ne0}\frac{(1-\alpha_i)^2v_i^2}{1-\alpha_i^2D_i^2}
\le \sum_{i\ne0}\frac{1-\alpha_i}{1+\alpha_i}\,v_i^2.
$$

For deletion on an arbitrary bulk set $S$, take $E_i=0$ on $S$ and $E_i=D_i$ on the other bulk coordinates. Then $Q_E=\|v_S\|_2^2$ exactly, and

$$
\|(x_E)_S\|_2\le L\ll\sqrt\tau+\|v_S\|_2,\qquad
|m_E-m_{S\cup T}|\ll\tau+\|v_S\|_2^2
$$

with $m_{S\cup T}$ the full stripped entry from the [cover calculation](coset-activation.md). These estimates use no bound on the cardinality of $S$ or the distance of the exterior diagonal from saturation. The full stripped diagonal has $Q_E=0$. The proof also permits changing signs under $|E_i|\le |D_i|$, with the cost measured by $Q_E$.

At decreasing $\tau$, a construction of $E$ with $|E|\le|D|$ on the bulk, $m_E=o(1)$, and $Q_E=o(1)$ would transfer cancellation to the stationary mark. Deleting a small proportion of the total stationary squared norm can still cost a positive $Q_E$ when the total grows. For a cover $S$, the [exterior-column estimate](exterior-column.md) has a direct answer when $\|v_S\|_2=o(1)$. The estimate leaves covers carrying a positive amount of unnormalized stationary squared mass.

For one-sided changes an [opposite-spectrum identity](stationary-ordered.md) controls the exterior weighted norm in terms of the signed marked change and the distance of the exterior mark from the opposite endpoint. It yields a stronger energy requirement for deletions where that distance is small.

Along the [hyperbolic attenuation path](stationary-secant.md#uniform-transfer-along-the-hyperbolic-path), the energy $Q_E$ is explicitly bounded throughout the interval of scaling factors $[1/2,1]$. At the half-angle the stripped inverse column is exactly proportional to the stationary spectrum difference.

## A signed criterion

The completed square also implies

$$
\beta\ge -2(W-1)/u_0,\qquad L^2\le \tau+\beta_+,\qquad
|m-D_0|\le \sqrt{\tau+\beta_+}+\tau+\tfrac14(\tau+\beta_+).
$$

For the last inequality compare the center of the square to $D_0$, using $v_0u_0/A=D_0u_0^2/A$ and $|v_0|/A\le1/(4\sqrt W)$. Thus just the upper bound $\beta_+=o(1)$ suffices at decreasing $\tau$, even for a diagonal with $Q_E$ large or $R_E>1$. For deletion $\beta=\langle v_S,(x_E)_S\rangle$. This is a single signed pairing of the exterior column with the removed spectrum.

## An alternative criterion using the full column

Let $F$ be the full stripped stationary diagonal, $E_i=\alpha_i F_i$ with $0\le\alpha_i\le1$, $V=F-E$, and $X_E=H_E^{-1}P$. Write $x_F=X_Fe$. The resolvent identity in both directions gives

$$m_F-m_E=\langle x_F,Vx_F\rangle-\langle Vx_F,X_E Vx_F\rangle.$$

The [weighted response contraction](response-locality.md#contraction-and-response-derivative) gives $X_E=B_E^{-1}(\mathcal R_E+E)B_E^{-1}$ with $B_E=(1-E^2)^{1/2}$ and $\|\mathcal R_E\|\le1$. The diagonal term after this substitution is $V(1-EF)/(1-E^2)$. The contraction term is bounded in absolute value by the quadratic form of $V^2/(1-E^2)$. Pointwise,

$$
|V|\le1-EF,\qquad
\frac{1-EF}{1-E^2}\le1
$$

where the first inequality holds for any strict $E,F$ and the second uses $E=\alpha F$. Hence

$$|m_F-m_E|\le2\sum_{i\ne0}(1-\alpha_i)|F_i|\,x_{F,i}^2.$$

This permits sitewise attenuation on both signs at once. For deletion on $S$ one also has

$$\sum_{i\in S}|F_i|\,x_{E,i}^2\le4\sum_{i\in S}|F_i|\,x_{F,i}^2.$$

Indeed $C=\operatorname{diag}(\sqrt{|F_i|}:i\in S)$ and $\|C(X_E)_{SS} C\|\le1$, since $E=0$ on $S$ and $(X_E)_{SS}=(\mathcal R_E)_{SS}$. The resolvent identity gives $C(x_E)_S=(I-C(X_E)_{SS}C\,\operatorname{sgn}(F_S))C(x_F)_S$. For a same-sign deletion the [one-sided argument](parallel-coupling-2.md#stationary-column-and-same-sign-deletion) also gives the sign of $m_F-m_E$ and a lower bound in terms of the exterior column. The criterion here controls the mixed-sign increment using the full column even where $Q_E$ is large.

### Increasing the floor in the diagonal

Keep the true stationary $v$ at floor $\tau$ and replace only the bulk diagonal by

$$E_i=\frac{v_i}{\sqrt{v_i^2+4(\tau+\eta_i)/n}},\qquad \eta_i\ge0.$$

With $u_i'=\sqrt{v_i^2+4(\tau+\eta_i)/n}$ one has

$$
Q_E=\sum_{i\ne0}\frac{v_i^2(u_i'-u_i)^2}{4(\tau+\eta_i)/n}
\le\frac1n\sum_{i\ne0}\frac{\eta_i^2}{\tau+\eta_i},
$$

using $u_i'+u_i\ge2|v_i|$. The full-column bound also gives a Lipschitz estimate

$$|m_E-m_F|\le \max_{i\ne0}\eta_i.$$

Indeed the magnitude of the derivative of $F_i$ with respect to its floor, keeping $v_i$ fixed, equals $(1-F_i^2)|F_i|/(2\tau)$ and decreases as the floor grows. The completed square at $E=F$ gives $\sum_{i\ne0}(1-F_i^2)x_{F,i}^2\le4(W-1)/A\le\tau$. Applying the full-column bound gives the estimate. In particular the floor can be increased to a common value $s\ge\tau$ at a cost at most $s-\tau$, uniformly even when $\|v\|_2$ grows. At any fixed $s>0$, entries with $n v_i^2\to\infty$ still approach saturation.

## Numerics at the actual stationary pair

The [probe](../stationary_attenuation.py) tests the first two sources and the norm identity in [108 comparisons](../data/stationary-attenuation.csv), at three pairs of prime and square orders and three floors. The cases are the full stripped diagonal, deletion of the 16 weakest or strongest bulk coordinates, deletion of either of the two covers from the [coset probe](../coset_activation_probe.py), and partial attenuation with $\alpha_i=1-0.02|D_i|$. The maximum discrepancy in the identities is $1.8\cdot10^{-9}$. The largest stationary and inverse residuals are $1.0\cdot10^{-10}$ and $2.4\cdot10^{-10}$, respectively. In a separate test of the first two bounds, 180 small dense solves using arbitrary strict diagonals and signed attenuations satisfied all three identities to within $1.0\cdot10^{-12}$.

At $\tau=0.002$ the strongest plus covers give the following results. Here $x$ is the exterior column and $m_F$ is the full stripped marked entry.

| Order | $Q_E$ | $\beta$ | $\lVert x_S\rVert_2$ | $m_F$ | $m_E$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $389^2$ | 383.719 | 2.73795 | 0.13978 | 0.33193 | -0.96713 |
| $153649$ | 0.01683 | 0.00846 | 0.06752 | -0.00124 | -0.00354 |

The square cover captures large squared energy and its deletion changes the marked value at constant scale. In the paired prime run, both $Q_E$ and the signed pairing are small. These are floating-point comparisons at finite orders.
