# Coupling of a frequency cover to its exterior

Use the [marked stationary notation](marked-response.md#a-symmetric-operator-for-the-response) with bulk weights $w_i=\tau/n$. Strip the marked diagonal entry and keep its true values $D_i$ in the bulk. For disjoint bulk sets $S,T$ partitioning the bulk, write $D_S,D_T$ for the diagonal restricted to either set and zero elsewhere. For a diagonal $E$, write $X_E=(K-PEP)^{-1}P$, $x_E=X_E e$ and $m_E=\langle e,x_E\rangle$. Subscripts that are sets denote their restricted diagonals, so $x_\emptyset=K e$ and the full stripped inverse is $m_{S\cup T}$.

The finite-phase [mass gap](critical-coset-phases.md) excludes concentration of a stationary spectrum on a critical coset cover. The following identity specifies a distinct estimate required to combine responses on the cover and its exterior. An exact square model shows that the two responses can have an order-one interaction even when the exterior is uniformly separated from activation of absolute value one.

The [stationary deletion estimates](stationary-attenuation.md) control the exterior inverse on $S$ when the unnormalized energy $\lVert v_S\rVert_2^2$ is small. They also give a criterion in terms of the signed pairing of the exterior column with $v_S$.

## The exact interaction

Define the interaction $\mathcal I=m_{S\cup T}-m_S-m_T+m_\emptyset$. Here $m_\emptyset=\langle e,Ke\rangle=-1/n$ is the zero-diagonal inverse entry. The resolvent identity gives

$$\mathcal I=\langle x_{S\cup T},D_S(x_T-x_\emptyset)+D_T(x_S-x_\emptyset)\rangle.$$

Indeed $x_{S\cup T}-x_\emptyset=X_{D_S+D_T}(D_S+D_T)x_\emptyset$. Pair with $e$ and subtract the two separate increments $\langle x_S,D_S x_\emptyset\rangle+\langle x_T,D_T x_\emptyset\rangle$. Use $x_{S\cup T}-x_S=X_{D_S}D_T x_{S\cup T}$ and its counterpart with $S,T$ exchanged, then transpose the symmetric inverses. They act as zero on the constants, so the formula uses ordinary diagonal products.

For the actual stationary $D$, let $\Delta$ be the marked leverage difference and let $m$ denote the inverse before stripping. The [rank-one formula](response-locality.md#a-uniformly-bounded-background) and the exact leverage identity give

$$m_{S\cup T}=\frac{m}{1+D_0m}=\frac{D_0+\Delta}{1+D_0\Delta}=D_0+O(\tau).$$

Here $|\Delta|\le\tau$ and the error is uniform for $0<\tau\le1/2$. The weighted speed identity bounds the bulk norm $\|M x_{S\cup T}\|_{2,\mathrm{bulk}}\ll\sqrt\tau$, since stripping rescales the full inverse column by $1/(1+D_0m)$. With $M_i=\sqrt{1-D_i^2}$, we have $D_i/M_i=v_i/(2\sqrt{\tau/n})$ on the bulk. Therefore

$$|\mathcal I|\ll\sqrt n\left(\|\mathbf1_S v\,(x_T-x_\emptyset)\|_2+\|\mathbf1_T v\,(x_S-x_\emptyset)\|_2\right).$$

Products here are coordinatewise. At weights decreasing to zero, upper bounds of $o(1)$ on the two restricted marked entries and on these weighted cross terms would suffice for the stationary marker and hence the theta limit. The cross terms concern changes of the inverse columns on the opposite regions. An estimate on the stationary mass of the cover alone does not give such an estimate.

If the cover has a fixed compression gap, the term on the exterior can be bounded without a second inverse solve. Indeed the zero-background restriction gives $(x_S)_S=(I-K_{SS}D_S)^{-1}(Ke)_S$, whence $\|D_Sx_S\|_1\le |S|/(m_0\delta)$ for $\delta=1-\|K_{SS}\|$. As $x_S-x_\emptyset=K D_Sx_S$, its supremum is at most $|S|/(m_0^2\delta)$. Consequently the exterior term is $O_\delta(|S|n^{-1/4})$ at floors $\tau\le1/2$, using the elementary stationary bound $\|v\|_2=O(n^{1/4})$. This estimate removes one cross term for $|S|=o(n^{1/4})$. The [two-frequency example](exterior-column.md) shows that the other cross term still needs information about the stationary background.

For numerical evaluation, if an approximate column is $y$ and its residual is $r=e-(K-PEP)y$, the corrected scalar $\langle e,y\rangle+\langle y,r\rangle$ differs from $m_E$ by exactly $\langle r,X_E r\rangle$ for mean-zero $y$. The same identity with the inverse extended by the identity on constants applies to a computed column with roundoff in its mean. The absolute residual correction error is bounded by $\|r\|_2^2/(1-\|E\|)$. These estimates concern a given diagonal and exact matvec arithmetic.

## An exact interacting square model

At $q=r^2$ with odd prime $r$, let $S$ be the subfield annihilator without zero and $s=|S|=(r-1)/2$. Prescribe activation $d$ on $S$, $b$ on the remaining bulk, and zero at the mark. For $-1<b<1$ fixed, take $d=1-1/q$. The limits of the full, inside-only and outside-only entries are respectively $(2+b)/3$, $2/3$ and $b$. Thus the interaction tends to $-2b/3$, nonzero whenever $b\ne0$.

For the calculation start with the constant diagonal $b$ on all coordinates, for which $X_b=(K+bP)/(1-b^2)$. The [square Fourier entries](response-locality.md#square-order-test-of-the-formula) give the following three scalars:

$$m_b=\frac{b(1-1/n)-1/n}{1-b^2},\qquad c=\frac{r-b}{n(1-b^2)},\qquad \beta=\frac{(r(s-1)-1)/n+b(1-s/n)}{1-b^2}.$$

The restricted mark column has constant value $c$ on $S$, and $\beta$ is the eigenvalue of the restriction of $X_b$ on its constant vector. Changing the diagonal to $d$ on $S$ gives the entry $f=m_b+(d-b)sc^2/(1-(d-b)\beta)$ before stripping. Stripping the mark changes it to $f/(1+bf)$. For $d=1-1/q$ the increment in $f$ tends to $2/[(1-b^2)(3+b)]$, giving $(2+b)/3$ after stripping. Setting $b=0$ gives the inside-only value. Setting $d=0$ with $b$ fixed gives an increment tending to zero before stripping, so the outside-only value tends to $b$. At $b=-4/5$, for example, the full entry tends to $2/5$ while the interaction tends to $8/15$. These are prescribed diagonals. Forty finite-order comparisons over five square fields agreed with the direct inverse to $4.5\times10^{-15}$.

## The actual stationary diagonal

The [probe](../coset_activation_probe.py) maximizes each stationary spectrum's mass over unions of at most seven cosets of a common subgroup and size at most $1.1n/\sqrt q$. It solves the full, inside-only, and outside-only stripped linear systems for both selected covers. At floor $\tau=0.01$, the covers selected for the plus side give these results:

| Field order | Cover mass | Full entry | Inside only | Outside only | Interaction |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $97^2$ | 0.98087 | 0.32844 | 0.65734 | -0.86568 | 0.53657 |
| $9413$ | 0.03440 | 0.00045 | 0.00638 | -0.00899 | 0.00284 |
| $193^2$ | 0.98059 | 0.33306 | 0.66201 | -0.88036 | 0.55135 |
| $37253$ | 0.01052 | -0.00045 | 0.00127 | -0.00478 | 0.00301 |
| $389^2$ | 0.98037 | 0.33540 | 0.66436 | -0.88631 | 0.55734 |
| $153649$ | 0.00781 | -0.00124 | 0.00144 | -0.00341 | 0.00071 |

In the square controls the cover contains nearly all the plus mass, and the exterior and cross terms each contribute at constant scale. The sampled primes have small cross terms and small full entries. In the [36 recorded comparisons](../data/coset-activation.csv), the largest stationary residual was $1.0\times10^{-10}$, the largest linear residual was $2.4\times10^{-10}$, and the two computations of $\mathcal I$ agreed within $1.4\times10^{-11}$. The diagonal and the linear solves use floating point. There is no uniform prime-order estimate yet for the weighted cross terms.
