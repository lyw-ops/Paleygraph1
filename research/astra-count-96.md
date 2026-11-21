# The real exterior forcing before the first comparison excess

Let an eligible prime have $n=(p-1)/2\ge10^{30}$. If the counting excess of the [round-95 near-flat comparison](astra-tie-95.md) ever becomes positive on a vertical ray in the closed square of half-width $2^{-17}$ about $2031/128$, the ray first meets a floor with an exact unit-bulk product and a signed exterior sum greater than **$4.89\cdot10^{-5}$**. Its linear operator is frozen at the actual height-100 arithmetic predictor on the real axis. The marked input and the hitting site's entire diagonal response have been removed. Even after erasing the hit and any fifteen more bulk sites, the exterior source has counting second norm above **$2.09\cdot10^{-5}$**. The remaining hyperbolic half-log error has counting second norm above **0.208**, while its full normalized second norm is below $1.8\cdot10^{-12}$. These are necessary conditions for attaining the R95 one-tie price $0.08128$. An upper on the signed test throughout the possible first boundary would give comparison excess exactly zero. Such an upper through primes remains open.

## Stop at the first boundary of the selected real profile

Write $t=T+iy, s=n/t=u+iv, e=1-\delta, \delta=10^{-8}$. On the R95 selected comparison let $A,B'$ be the reconstructed complex factors, $Q_i=A_i B'_i$ their positive bulk products, and $w_i=(\Re A_i)(\Re B'_i)$ the weights of their positive real parts. Their midpoint half log ratios are $\gamma_i=\tfrac12\log(\Re A_i/\Re B'_i)$. Put
\[
 B=\frac{v^2}{4w_0},\quad c=J_w e_0,\quad X=\sqrt{3B}\,c.
\]
The [real midpoint projection](real-phase-projection-89.md#the-exact-column-and-the-real-weight-equations) gives $Q_i-w_i=Bc_i^2$ on every bulk site, also for these nonunit products. Indeed the two imaginary rows have opposite relative tangents there, and the only imaginary product is at the mark. The R95 endpoint product equals $Q_i-3Bc_i^2$. The exact fixed-point clamp hence gives
\[
 Q_i=\max(1,e+X_i^2),\qquad
 w_i=Q_i-X_i^2/3,\qquad
 w_0=(u+\sqrt{u^2+v^2(1-c_0^2)})/2.                                   \tag{1}
\]
Thus the full counting excess is exactly $\|[\sqrt{e+X_B^2}-1]_+\|_2$. The last equation follows from the real and imaginary parts of the marked product as in the midpoint identity. All these data are continuous along the ray by the uniform real-profile contraction, positivity and the scalar mark equation. At $y=0$, $X=0$. Before any positive excess there is therefore a first floor where $\max_{i\ne0}|X_i|=\sqrt\delta$. At this floor every $Q_i=1$, every bulk $w_i=1-X_i^2/3$, and $\sum_{i\ne0}X_i^2\le 3B$, since $J_w$ is a contraction. The floor may precede the physical angle tie. The argument also allows a touch followed by retreat.

## Freeze the response on the ordinary real axis

Use the actual real nine-center $W=V_{100}(T)$, with real weights $t^0_0=n, t^0_i=T$ on the bulk. Put $g_i=\operatorname{arsinh}(W_i/(2\sqrt{t_i^0}))$, $D=\operatorname{diag}(\tanh g)$, $M=\operatorname{diag}(\operatorname{sech} g)$. Use the symmetric contraction
\[
 R=M(I-KD)^{-1}KM-D .
\]
The response at a stationary real diagonal $\gamma$ is $J_w$. The formula for an arbitrary strict real diagonal and its derivative $dR=R\operatorname{diag}(dg)R-\operatorname{diag}(dg)$ are the [real response identities](response-locality.md#contraction-and-response-derivative).

The arithmetic bound is $\sqrt n\,|R_{i0}|<89.158$ for every bulk $i$. In fact the [round-82 height-100 operator](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) has packet norm less than $0.984138$ for $KD$ on represented rows, and the actual input $\sqrt n K e_0$ has packet price at most $\sqrt{p/n}$. Its Neumann sum has sup norm at most $\sqrt{p/n}/(1-0.984138)$. The two exterior $M$ factors are contractions. This argument needs the represented input only at the mark.

For any set $S$ with $\mu|S|<1, \mu=\sqrt p/n$, its compression also satisfies
\[
 \|R_{SS}\|\le\kappa_S=\tanh\big(2L+\operatorname{arctanh}(\mu |S|)\big),
 \qquad L=\operatorname{arsinh}(4.768/(2\sqrt{2031/128-2^{-17}})).       \tag{2}
\]
To prove this, run the diagonal path from zero to $g$, where the [physical cap](astra-source-88.md#the-seed-centered-disks-on-the-complex-square) gives $\|g\|_\infty\le L$. At its start the response is $K$, with compression norm at most $\mu|S|$. At an eigenvector $f$ of the current compression with eigenvalue $\lambda$, extend the unit vector by zero. The compression derivative's Rayleigh quotient is
\[
 (\lambda^2-1)\sum_{j\in S} g_j f_j^2+\sum_{j\notin S}g_j (Rf)_j^2 .
\]
Contractivity bounds the absolute value by $2L(1-\lambda^2)$. Integrate for both extremal eigenvalues, using the same bound on every unit eigenvector at multiplicities. Thus (2) allows a set chosen after seeing all true amplitudes.

## The small tilt at the mark and its counting distribution

Let $h_j=2\sinh((\gamma_j-g_j)/2)$. At the first floor of (1),
\[
 |\gamma_0-g_0|<8\cdot10^{-12},\qquad
 \|h\|_{2,n}<1.8\cdot10^{-12},\qquad
 \|h\|_{2,n}^2=n^{-1}\sum_j h_j^2.                                      \tag{3}
\]
Here is the comparison to unit real bulk. Let $w^b=(n/T,1,\ldots,1)$. The norm over the bulk of $\sqrt w-\sqrt{w^b}$, in the normalization of (3), is at most
\[
 b=\frac{\sqrt\delta\,\sqrt{3B/n}}{3(1+\sqrt{1-\delta/3})},\qquad
 \sqrt{3B/n}\le\frac{\sqrt3\,|y|}{2T^{3/2}} .
\]
Indeed $(1-\sqrt{w_i})^2=X_i^4/[9(1+\sqrt{w_i})^2]$. At the mark (1) gives $u\le w_0\le n/T$, so the square-root error divided by $\sqrt n$ is at most $b_0=y^2/(2T^{5/2})$.

Complete the real predictor factors using $r=K\Phi_T(W)-W$. The rows $P^c,Q^c=(\Phi_T(W)\pm(W+r))/(2\sqrt T)$ are genuinely in the complementary sectors and have equal means. Their products are $w^c=w^b-(2Wr+r^2)/(4T)$. The arithmetic sup residual is below $0.001180$, and the [physical second-norm contraction](astra-source-88.md#the-seed-centered-disks-on-the-complex-square) through height 100 gives $r_n=\|r\|_{2,n}\le0.169724(0.51358)^{100}<3\cdot10^{-30}$. The two completed factors are positive since $\Phi_T(W)\ge2\sqrt T$ and $\|W+r\|_\infty<4.77$. In particular their real logs $g^c=\tfrac12\log(P^c/Q^c)$ correspond to the positive stationary pair at $w^c$. On all coordinates $w^c>0.9998$, and the difference-of-squares identity gives $\|\sqrt{w^c}-\sqrt{w^b}\|_{2,n}\le0.076r_n$. Thus $d=\|\sqrt w-\sqrt{w^c}\|_{2,n}\le\sqrt{b^2+b_0^2}+0.076r_n<1.75\cdot10^{-12}$.

The [two positive-pair Hellinger identity](astra-velocity-92.md#simultaneous-changes-to-the-real-weights) gives $\sum 4\sqrt{ww^c}\sinh^2((\gamma-g^c)/2)\le nd^2$. The marked weights both exceed $n/16$, so $ |\gamma_0-g^c_0|\le 4d$. At that site $ |g_0-g^c_0|\le 2\|r\|_\infty/\sqrt n$ by the two factor logs. In all coordinates the derivative of $z\mapsto\operatorname{arctanh}(z/\Phi_T(W)_i)$ on the segment from $W_i$ to $W_i+r_i$ has absolute value below $0.4$. For instance $\Phi_T(W)_i-|W_i+r_i|>2\sqrt T-4.77>3$, also at the mark. Thus $\|g-g^c\|_\infty<0.000472$; using the tighter derivative bound $1/(2\sqrt T-4.77)<0.32$ also gives $\|2\sinh((g-g^c)/2)\|_{2,n}\le0.4r_n$. The hyperbolic addition formula, or $\sinh(a+b)\le e^b\sinh a+\sinh b$ at $a,b\ge0$, now proves (3).

## Remove the entire observed block

Put $C=\operatorname{diag}(\cosh(\gamma-g)),\ H=\operatorname{diag}(\sinh(\gamma-g))$, and $\beta=C_{00}+H_{00}c_0$. The finite response identity is
\[
                   R(Ce_0+Hc)=He_0+Cc .                                 \tag{4}
\]
Indeed, under a displacement $g\mapsto\gamma$ of the logarithmic diagonal, the response becomes $(CR-H)(C-HR)^{-1}$ by the matrix differential above, integrated along the segment. The inverse exists since $\|C^{-1}H\|<1$ and $R$ contracts. Applying the inverse displacement to the pair $(e_0,c)$ gives (4). This holds for general real trial diagonals at the reference.

For any bulk set $S$ put $D_S^{\rm ext}=P_S R P_{(S\cup\{0\})^c}HX$, restricting the output to individual sites. Equation (4) reads
\[
 C_S X_S-R_{SS}H_S X_S
      =\beta\sqrt{3B}\, R_{S0}+D_S^{\rm ext}.
\]
Since $C^2-H^2=I$, its left norm is at least
$\sqrt{\|X_S\|_2^2+\|H_S X_S\|_2^2}-\kappa_S\|H_S X_S\|_2\ge\sqrt{1-\kappa_S^2}\|X_S\|_2$. If $S$ contains $k\ge1$ sites at the first threshold, then
\[
 \boxed{\quad
 \|D_S^{\rm ext}\|_2\ge\sqrt{1-\kappa_S^2}\sqrt{k\delta}
 -e^{8\cdot10^{-12}}\frac{\sqrt{p/n}}{1-0.984138}
               \sqrt{3B/n}\sqrt{|S|}.\quad}                              \tag{5}
\]
All three occurrences of a second norm in this block argument are unnormalized. The marked column's contribution was bounded separately even when the set depends on the unknown row. The conclusions include the following.

* For a single threshold site $i$, the **signed** sum $\operatorname{sgn}(X_i)\sum_{j\ne0,i}R_{ij}\sinh(\gamma_j-g_j)X_j>4.89\cdot10^{-5}$, since $C_{ii}-R_{ii}H_{ii}\ge\sqrt{1-R_{ii}^2}>0$.
* Take the hit and any fifteen other bulk sites. Formula (5) gives $\|D_S^{\rm ext}\|_2>2.098\cdot10^{-5}$. In particular $\|P_{(S\cup\{0\})^c}HX\|_2$ exceeds the same value. With $U=\|P_{(S\cup\{0\})^c}h\|_2$, the first threshold bound gives $\|P_{(S\cup\{0\})^c}HX\|_2^2\le\delta(U^2+U^4/4)$, since $H_{jj}^2=h_j^2+h_j^4/4$. Consequently $U>0.2086$. The fifteen omitted sites can be the largest remaining half-log errors. Even after any 38 additional deletions the exterior source norm still exceeds $5.7\cdot10^{-8}$.
* More generally, for $|S|\le16k$ and $\mu |S|\le0.1$, the exterior norm is greater than $1.63\cdot10^{-5}\sqrt k$. This prices simultaneous first-threshold sites after up to fifteen additional erasures per hit.

For all sufficiently large eligible primes the [translated-source bound](shifted-resolvent-96.md) also gives $|[(I-KD)^{-1}K]_{ij}|<178/\sqrt n$ for every entry at height 100. Thus (5) holds with $\kappa_S$ replaced by $\tanh L+178|S|/\sqrt n$ whenever this is below one, by $R_{SS}=-D_S+M_S[(I-KD)^{-1}K]_{SS}M_S$. For a singleton the resulting signed exterior lower exceeds $7.648\cdot10^{-5}$. Every exterior matrix entry is off diagonal, so its source satisfies
\[
  \sum_{j\ne0,i}|\sinh(\gamma_j-g_j)X_j|>4.296\cdot10^{-7}\sqrt n .
\]
Taking $|S|=84$ in the same bound leaves exterior second norm above $3.84\cdot10^{-7}$ after deleting the hit and any 83 additional bulk sites. These three bounds use the eventual all-source estimate in addition to the finite-prime marked-column estimate.

At $p=173, t=2031/128+i/131072$ the known interior physical row sets its own comparison threshold $\delta=\max_{i\ne0}3\sin^2\phi_i\in(2.24795,2.24796)\cdot10^{-14}$; only inversion orbit 16 attains it. Equation (4) at that boundary site gives an exterior sum between $-7.571\cdot10^{-22}$ and $-7.570\cdot10^{-22}$ for the genuine unit-bulk real stationary reference, and between $-3.913\cdot10^{-9}$ and $-3.912\cdot10^{-9}$ for the bare Jacobi seed. Full individual matrices retain the inverse partner as an exterior site. This check covers the physical column transport at a tailored cutoff. The large-prime arithmetic margin uses height 100 and $\delta=10^{-8}$. [Arb checker](astra-count-96-check.py) · [Three outward records](astra-count-96-checks.jsonl)

1. Test the signed singleton exterior on the first boundary, using $X_j^2=3(1-w_j)$ and the frozen height-100 real response. An upper below $4.89\cdot10^{-5}$ for each candidate excludes even the start of positive comparison excess.
2. If a few large real amplitude errors dominate an absolute bound, erase them with the observed block in (5). Controlling just the residual exterior source after fifteen such erasures suffices for a singleton, and the block version covers simultaneous hits.
