# Marked spectral mass and the stationary high frequencies

Use $q$, $n=(q-1)/2$, $K$, and $P=I-J$ as in the [smoothing notes](smoothing.md). Write $m_0=n/\sqrt q$, $w_0=1$, $w_i=\tau/n$ in the bulk, $W=\sum_iw_i$, and $\nu_i=\sqrt{w_i}$. At the exact stationary point set $v=v^*$, $u_i=\sqrt{v_i^2+4w_i}$, $D_i=v_i/u_i$, and $M_i=\sqrt{1-D_i^2}=2\nu_i/u_i$. The linearization on the mean-zero space is $H=K-PDP$, and the marked source is $e=Pe_0$.

## Quantitative compression on the high set

Suppose $\|y\|_2=1$, $Py=y$, $\|Hy\|_2\le\eta\le1$, and $|D_i|\le\rho<1$ off a set $S$. The isometry $K$ on $P$ gives

$$\|My\|_2^2+\|JDy\|_2^2=1-\|PDy\|_2^2\le2\eta.$$

In particular the tail $t=P_{S^c}y$ obeys $\|t\|_2^2\le 2\eta/(1-\rho^2)$. Let $z=P_S y$. Then $Jz=-Jt$, and $P_{S^c}Kz=P_{S^c}(Hy+PDy-Kt)$ has norm $O_\rho(\sqrt\eta)$. Since $\|Kz\|_2^2=\|z\|_2^2-\|Jz\|_2^2$, this gives the squared-norm estimate

$$\|K_{SS}z\|_2^2=\|z\|_2^2-O_\rho(\eta),\qquad \|K_{SS}\|\ge1-O_\rho(\eta).$$

The second inequality holds for sufficiently small $\eta$ at fixed $\rho$. If $\eta=O(1/m_0)$ and $|S|\le m_0+O(1)$, then the entry bound $|K_{ij}|\le1/m_0$ forces $m=|S|=m_0+O(1)$. The [mean Jacobi deficit](critical-sets.md) now satisfies

$$d(S)=1-\frac{m_0^2}{m^2}\|K_{SS}\|_{\mathrm F}^2=O_\rho(1/m_0).$$

The endpoint counting estimate there yields $E(S)\gg m^{5/2}$. More precisely, for every fixed $\epsilon>0$ there is a $c_\epsilon>0$ such that all but an $\epsilon$ fraction of pairs have differences of multiplicity at least $c_\epsilon\sqrt m$. Apply the multiplicity bound with cap threshold $T/m_0$, first taking $T$ large and then the multiplicity threshold $c_\epsilon\sqrt m$ with $c_\epsilon$ small. The hypotheses tie the size of the true high set and the spectral width to the square-root scale. [Xi's discrepancy bound](https://arxiv.org/abs/1809.04286)

A [signed compression estimate](signed-coset-bands.md) separates the two tails and uses only the high set $\{i:\sigma D_i>\rho\}$ for the sign of the eigenvalue. At prime order it excludes highly overlapping critical sets and critical coset unions.

## A strongly coupled narrow band forces stationary mass

The fixed-point identities $Ku=v$ and $Kv=Pu$ give the exact relation

$$Hv=P(u-Dv)=2PM\nu=a e+2PM\nu_{\rm bulk},\qquad a=2M_0=4/u_0,$$

where $\nu_{\rm bulk}$ deletes the marked entry and has norm at most $\sqrt\tau$. Let $E_\eta$ be the spectral projector of $H$ onto $[-\eta,\eta]$, and $\mu_\eta=\|E_\eta e\|_2^2$. Test the relation against $y=E_\eta e/\sqrt{\mu_\eta}$ when $\mu_\eta>0$. This unit vector has $\|Hy\|_2\le\eta$, $\langle y,e\rangle=\sqrt{\mu_\eta}$, and $\|My\|_2\le\sqrt{2\eta}$. Thus

$$\eta\|E_\eta v\|_2\ge \big(a\sqrt{\mu_\eta}-2\sqrt{2\tau\eta}\big)_+.$$

The bound $\|P_{S^c}y\|_2\le \sqrt{2\eta/(1-\rho^2)}$ holds for every unit vector in this spectral space. Testing it on $E_\eta v/\|E_\eta v\|_2$ gives

$$\|P_S v\|_2\ge\|E_\eta v\|_2-\sqrt{2\eta/(1-\rho^2)}\|v\|_2.$$

In particular, if $\eta=O(q^{-1/2})$ and $a\sqrt{\mu_\eta/\eta}-2\sqrt{2\tau}$ is bounded below by a positive constant, then $\|P_S v\|_2\gg\eta^{-1/2}$. The elementary estimates $\|v\|_2=O_\tau(q^{1/4})$ and $\|v\|_\infty=O_\tau(1)$ show that $\eta\gg q^{-1/2}$ in this case and

$$\frac1{\sqrt n}\sum_{i\in S}|v_i|\gg 1.$$

Thus a band at the critical width with enough coupling to the mark forces a positive amount of the stationary normalized $\ell_1$ mass on the high set. The criterion can also be applied to a single eigenvector, since its squared marked component is a lower bound on $\mu_\eta$ for $\eta$ at least its absolute eigenvalue.

## Removing narrower widths as the smoothing weight decreases

For $0<\tau\le1$ and $0<\eta\le1$, the same identity gives the dimension-uniform bound

$$\mu_\eta\ll \eta^2\|v\|_2^2+\tau\eta.$$

Here $a$ has a positive lower bound by $u_0=O(1)$. Every absolute eigenvalue of $H$ is at least $1-\|D\|\gg\tau/n$, since $u_i=O(1)$ and $1-|D_i|\ge2w_i/u_i^2$. Sum the preceding spectral-mass bound over the dyadic annuli below $\eta$ and stop at that eigenvalue floor. For the spectral measure $\mu$ at $e$ the resulting bound is

$$\int_{0<|\lambda|\le\eta}\frac{d\mu(\lambda)}{|\lambda|}\ll \eta\|v\|_2^2+\tau\big(1+\log_+(n\eta/\tau)\big).$$

If $\tau=\tau_q$ satisfies $\tau_q\log q\to0$, the absolute marked spectral integral below $\delta/\sqrt q$ is at most $O(\delta)+o(1)$. The logarithmic term goes to zero because $\tau_q\log(1/\tau_q)\to0$ as well. For each fixed $C$, an order-one absolute contribution below $C/\sqrt q$ then forces $\|v\|_2^2\gg\sqrt q$. In turn it forces positive normalized $\ell_1$ mass on a bulk set of order $\sqrt q$ on which $|v_i|\ge c>0$ for a fixed $c$. In fact $\sum_{|v_i|<c}v_i^2\le c\|v\|_1$ and $\|v\|_1=O(\sqrt n)$, so taking $c$ small leaves a positive fraction of the squared norm on $|v_i|\ge c$. There $\|v\|_\infty=O(1)$ converts squared norm into $\ell_1$ mass and the global $\ell_1$ bound controls cardinality. The single marked entry contributes only $O(1)$ to the squared norm.

Equivalently, at these decreasing weights, the weaker estimate $\|v\|_2^2=o(\sqrt q)$ suffices to remove the entire band $[-C/\sqrt q,C/\sqrt q]$ for each fixed $C$. The marked inverse can also receive contributions at larger widths.

## Near-zero directions of the numerical stationary equations

The [inverse-iteration probe](../stationary_modes.py) starts from $e$ and uses five solves with $H$ at a numerically converged smoothing iterate. For the resulting unit direction $y$, it reports $h=\|Hy\|_2$, the Rayleigh quotient $\zeta=\langle y,Hy\rangle$, and the eigenvector residual $\varepsilon=\|(H-\zeta)y\|_2$. Taking $\eta=2h$, spectral projection gives $\|(I-E_\eta)y\|_2\le \varepsilon/(\eta-|\zeta|)$ and hence

$$\frac{\mu_\eta}{\eta}\ge\frac1\eta\left(|y_0|-\frac{\varepsilon}{\eta-|\zeta|}\right)_+^2.$$

The table gives this lower estimate at $\tau=0.05$ and shows the mass of the high set $S=\{i\ne0:\sqrt n|v_i|>12\}$. The threshold required in the stationary mass test is $8\tau/a^2$, about $0.111$ in the three square cases. The three nearby prime runs have an empty $S$ and the projection lower estimate is zero. All values come from floating-point solves with recorded residuals. [Full results](../data/stationary-modes.csv)

| Field order | Size of $S$ | $\sum_{i\in S}|v_i|/\sqrt n$ | $\sqrt q\,h$ | Lower estimate for $\mu_{2h}/(2h)$ |
|---|---:|---:|---:|---:|
| $97^2$ | 48 | 0.91058 | 2.92548 | 0.27054 |
| $9413$ | 0 | 0 | 7.44319 | 0 |
| $193^2$ | 96 | 0.91902 | 2.92710 | 0.42634 |
| $37253$ | 0 | 0 | 14.77532 | 0 |
| $389^2$ | 194 | 0.92296 | 2.91692 | 0.45064 |
| $151337$ | 0 | 0 | 30.45598 | 0 |

At $389^2$ the direction has $98.61\%$ of its squared norm on $S$ and an eigenvector residual of about $1.86\times10^{-6}$. The three prime directions have larger eigenvector residuals relative to their widths, so these probes establish the observed square-order coupling and the measured stationary tails. Excluding strongly coupled prime bands uniformly is a separate spectral estimate.
