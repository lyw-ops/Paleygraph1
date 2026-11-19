# A nonexpansive clipped Paley equation and its canonical total correction

At each floor of the cold square the even clipped rows of [round 89](real-phase-projection-89.md) all have the same two factors at the mark, the same complex mean and the same total bulk product correction. These statements also hold without the even restriction. An iteration from an arbitrary row finds such a solution. For the cap $\tan\phi_*=1/\sqrt2$, the actual height-600 residual bounds the normalized total correction by $1.84$ times its normalized second norm. The density of coordinates reaching the cap, including their square-root product cost, is quadratic in that residual. These are estimates at an everywhere existing fixed point on the whole square, independent of the availability of the original unforced branch.

## A scalar extension and fixed-point rigidity

Write $s=n/t=u+iv$, normalize both factors by $\sqrt t$, and use $U=A-B$, $S=A+B$ for the normalized rows. A complementary pair with equal means satisfies $U=KS$. Fix $a=1/\sqrt\kappa\in(0,1)$, $\phi_*=\arctan a$, and on the complex plane use the real Hilbert norm $|z|_a^2=a^2(\Re z)^2+(\Im z)^2$. At a bulk site put
\[
 F(z)=\begin{cases}
 \sqrt{4+z^2},& |\Im z|^2\le 4\sin^2\phi_*+a^2(\Re z)^2,\\
 |\Im z|/a+i a\operatorname{sgn}(\Im z)\Re z,&\text{otherwise}.
 \end{cases}                                                        \tag{1}
\]
The square root is the positive-real-part branch. In the first region write $z=2\sinh(g+i\phi)$, $g,\phi$ real, $|\phi|\le\phi_*$. Its slices at fixed real part follow from $(\Im z)^2=4\sin^2\phi+(\Re z)^2\tan^2\phi$, which increases with $|\phi|$. On the second region write $z=2\sqrt q\sinh(g+i\sigma\phi_*)$, $\sigma=\operatorname{sgn}(\Im z)$, with
\[
 q=(\Im z)^2/(4\sin^2\phi_*)-(\Re z)^2/(4\cos^2\phi_*)>1.
\]
Then $F=2\sqrt q\cosh(g+i\sigma\phi_*)$. Both rules agree on the boundary. Thus $(F+z)/2,(F-z)/2$ have positive real parts, opposite bulk phases, and product $q=1+e$ with $e\ge0$ and $e>0$ only at the angle cap. Conversely these conditions, including angle at most the cap, determine precisely (1). Indeed at a boundary site $D=\tan\phi=\pm a$, so $w=q\cos^2\phi=\kappa wD^2$. By the actual marked column formula $wD^2=Bc_i^2$. At an unsaturated site $q=1$ gives $w=1-Bc_i^2$. This is exactly the clipped rule including its tie.

The map $F$ is globally nonexpansive in $|\cdot|_a$. Multiplication by $d\in\mathbb C$ is contractive in this norm if $1-|d|^2\ge|a-a^{-1}||\Im d|$. Indeed in Euclidean coordinates it has matrix $D=\bigl(\begin{smallmatrix}\Re d&-a\Im d\\a^{-1}\Im d&\Re d\end{smallmatrix}\bigr)$, with determinant $|d|^2$ and
\[
 \det(I-D^*D)=(1-|d|^2)^2-(a-a^{-1})^2(\Im d)^2.                  \tag{2}
\]
The product of its singular values is $|d|^2$, which decides the inequality when combined with this determinant (the case $|d|=1$ here forces $\Im d=0$). Inside (1), $d=\tanh(g+i\phi)$, $1-|d|^2=\cos(2\phi)/|\cosh(g+i\phi)|^2$, $\Im d=\sin(2\phi)/(2|\cosh(g+i\phi)|^2)$. The test holds exactly up to $|\phi|=\phi_*$ in this chart, strictly below the cap. Outside, the real linear map on each sign is an isometry. Integrate along the straight segment, partitioned by the two hyperbola branches. The strict criterion applies at every finite interior point.

Hereafter take $a=1/\sqrt2$, $n=(p-1)/2\ge10^{30}$, and $|\Re t-2031/128|,|\Im t|\le2^{-17}$. For the mark put $V=U_0/\sqrt s$, with the positive sheet. Every genuine clipped mark lies in the interior of $|\Re V|\le20$, $|\Im V|\le1/4$. To verify this, let $W=\sum w_i$, $m=\sqrt{W/n}$ and $B=v^2/(4w_0)$. The [clipped weight and mean equations](real-phase-projection-89.md#an-everywhere-positive-clipped-construction) give $W\le n+u+4v^2/(4u)$, since $W\ge w_0\ge u$. Thus $m<1.04$. At the mark the two normalized factor tangents have modulus at most $|v|/u<6\cdot10^{-7}$, by $D_0=P_0c_0$ and $2w_0P_0=v$. Everywhere the two normalized factors have arguments of modulus at most $\phi_*$. Since $|K_{ij}|\le\sqrt p/n$ and their real-part sums are both $nm$, this gives $|V|\le2m\sec\phi_*\sqrt{p|t|/n}<15$. For half their phase difference $\phi_0$ we have $|\phi_0|<6\cdot10^{-7}$. The identity $V=2\sinh(g_0+i\phi_0)$ gives $|\Im V|\le\sqrt{4+|V|^2}\,|\sin\phi_0|<10^{-5}$.

Let $C$ be this closed rectangle multiplied by $\sqrt s$ in the physical $U_0$ plane. Use $|\cdot|_a$ metric projection $P_C$ and define $F_0(z)=\sqrt s\sqrt{4+(P_C z/\sqrt s)^2}$. On $C$ the derivative before projection is $\tanh(g+i\phi)$ with $|\sin\phi|\le1/8$. Compactness and (2) give strict contraction there, with some Lipschitz constant less than one. Metric projection onto a closed convex set is nonexpansive in this Hilbert norm. Thus $F_0$ is globally strictly contractive. The rotation of $C$ with $s$ is included in the metric projection. The derivative of the two holomorphic scalings cancels before evaluating (2).

Write $\mathcal F$ for (1) on the bulk and $F_0$ at the mark. The real $K$ satisfies $K^2=I-J$, where $J$ is averaging. Thus $T=K\mathcal F$ is nonexpansive in the counting Hilbert sum of $|\cdot|_a^2$. A genuine even fixed point exists by round 89 and is a fixed point of this extension. If $U,U'$ are any two fixed points, the nonnegative sitewise losses satisfy
\[
  \sum_i\bigl(|U_i-U_i'|_a^2-|\mathcal F_i(U_i)-\mathcal F_i(U_i')|_a^2\bigr)
    +n\,|E(\mathcal F(U)-\mathcal F(U'))|_a^2=0.                   \tag{3}
\]
Here $E$ is the average over all $n$ sites. Strict contraction at the mark gives equal marks, and the second term gives equal means. Comparison to the existing genuine solution puts the common mark inside $C$, so **all fixed points of the extension are genuine clipped rows**. Indeed $(\mathcal F(U)\pm U)/2$ are the complementary factors with the physical marked product and common mean. Their real parts are positive and the round-89 projection identity recovers the clipped weights. Formula (3) also implies that any site strictly inside (1) at one fixed point is identical at every fixed point, by strict contraction on the initial part of a nonzero connecting segment.

Set $M=E\mathcal F(U)/2$, $M_0^2=(n-1+s)/n$ and
\[
                  \epsilon=M^2-M_0^2=E_{\rm full}(e_i\mathbf1_{i\ne0})\ge0 .               \tag{4}
\]
Bilinear orthogonality of the two sectors gives the equality. Thus $\epsilon$ is intrinsic even if the fixed point is nonunique. It vanishes exactly when there exists an original unforced pair on the positive sheet in the clipped sector (bulk angle at most $\phi_*$ and positive real-part chart at the mark). In that case every clipped solution has zero correction. At a bulk tie there is still strict margin to $\pi/4$, since $\phi_*=\arctan(1/\sqrt2)$. Vanishing on a common open tube would give the unforced section by uniqueness and the implicit function theorem there, as in round 89.

For a constructive selection iterate $Z_{k+1}=(Z_k+TZ_k)/2$. Squaring its distance to any fixed point bounds the decrease below by $|Z_k-TZ_k|_{2,a}^2/4$. Hence iterates are bounded and the residual tends to zero. A convergent subsequence in finite dimension has a fixed-point limit. Applying the same distance decrease to that limit proves convergence of the full sequence. The argument has no uniform iteration-count bound for detecting $\epsilon=0$.

## A residual bound and the price of all cap sites

Take the actual height-600 row $X=V_{600}(t)$ in the original normalization and its outgoing residual $R=K\Phi_t(X)-X$. Set $Z=X/\sqrt t$, $R'=R/\sqrt t$, $r'=\|R'\|_{2,n}$ in the usual normalized complex Euclidean norm, and $r=\|R\|_{2,n}$. On the cold square the [predictor](phase-action-84.md#exact-secant-comparison-in-logarithmic-coordinates) gives $|Z_i|<1.20$, $|\Im Z_i|<0.504$, and $\|R'\|_\infty<0.0028$ (use $|\sqrt t|>3.98$, $|\arg\sqrt t|<10^{-6}$). These bounds give the physical square roots throughout the predictor and $TZ=Z+R'$.

On each $|\cdot|_a$ ball of radius $0.15$ about a bulk $Z_i$ the derivative norm of $F$ is below $0.90$. Indeed there $|\Im z|<0.654$, $|\Re z|<1.413$, so $|\sin\phi|<0.327$, $|\sinh g|<0.75$, $\cos(2\phi)>0.786$, $|\sin(2\phi)|<0.654$. Formula (2) then gives $\det(I-D^*D)>(0.786^2-0.654^2/8)/(1+0.75^2)^2>0.20$, where $\lvert a-1/a\rvert^2=1/2$. Since $0\preceq I-D^*D\preceq I$, its smaller eigenvalue is at least this determinant. The ball at the mark after division by $\sqrt s$ is contained in $|V|<10^{-12}$, strictly inside $C/\sqrt s$, with a still smaller derivative norm. Using the strongly contractive part of the initial line segment, followed by global nonexpansiveness on the rest, gives for every fixed point $U$, with $d_i=|U_i-Z_i|_a$,
\[
 d_i^2-|\mathcal F_i(U_i)-\mathcal F_i(Z_i)|_a^2\ge0.10\,d_i\min(d_i,0.15).             \tag{5}
\]
In fact the output distance is at most $d_i-0.10\min(d_i,0.15)$. The strict initial allowance applies for arbitrarily large $d_i$ on saturated sites.

Write $A=\{d_i\le0.15\}$ and $\delta S=\mathcal F(U)-\mathcal F(Z)$. The exact Hilbert identity with residual has right side $2E\langle U-Z,R'\rangle_a-E|R'|_a^2$ in place of zero in the normalized (3). On $A$ use $2d_i |R_i'|\le0.05 d_i^2+20|R_i'|^2$, and on its complement use $2|R_i'|<0.0056$. Consequently
\[
 0.05E\mathbf1_A d_i^2+0.0094E\mathbf1_{A^c}d_i+|E\delta S|_a^2\le20(r')^2 .             \tag{6}
\]
The notation $E\mathbf1_A f$ always divides by the full $n$. For every bulk site in $H=\{|\phi_i|=\phi_*\}$, including ties with zero correction, $|\Im U_i|\ge2/\sqrt3$ and $d_i>0.65$. The upper branch or lower branch of (1) then gives
\[
 \sqrt{1+e_i}\le (\sqrt3/2)|\Im U_i|\le(\sqrt3/2)(d_i+0.504)<1.55d_i.
\]
In particular the entire cap set obeys the uniform price and counting bound
\[
                  |H|/n\le E\mathbf1_H\sqrt{1+e_i}<3400(r')^2                             \tag{7}
\]
for $r'>0$, with the zero bound at $r'=0$. This replaces the $O((\Im t)^2)$ bound on the number of positive corrections by a second, predictor-based bound which counts every exact tie as well.

Let $M_Z=E\mathcal F(Z)/2$. From (6), $|M-M_Z|\le\sqrt{10}\,r'$. Also $\Re M=m<1.04$ and $2n m\Im M=v$ by (4), giving $|M|<1.05$. The predictor has the original coordinate products, so ordinary bilinear pairing gives
\[
 M_Z^2-M_0^2=(E Z^2-E(Z+R')^2)/4,\qquad |M_Z^2-M_0^2|<0.602r'
\]
when $r'>0$. Combining this with (4) yields
\[
                 0\le\epsilon<7.3r'<1.84r.                                             \tag{8}
\]
Here one may use $r'<0.0028$ in $(2|M|+\sqrt{10}r')\sqrt{10}+0.602<7.3$. The bound is zero when $r'=0$. The [finite cold estimate](astra-source-88.md) $r<3.932\,10^{-175}$ and the [uniform field-first estimate](astra-dissipation-80.md) $\limsup_p\sup_t r<3.06\,10^{-208}$ give respectively $\epsilon<7.24\,10^{-175}$ and $\limsup_p\sup_t\epsilon<5.64\,10^{-208}$. Large values of the unweighted column maximum are still possible on a very sparse cap set. A fixed positive tolerance on (4), even the stated one, leaves exact removal and the original prime limit open.

These estimates localize the actual marked column at the clipping threshold. For $y=\Im t\ne0$ put $c_i=(J_w)_{i0}$ at any clipped fixed point. Its entire saturated tail is $H=\{i\ne0:3Bc_i^2\ge1\}$, with $1+e_i=3Bc_i^2$ there. Since $w_0\le(u+\sqrt{u^2+v^2})/2$ we have $B/n\ge y^2/[2|t|^2(\Re t+|t|)]>y^2/16384$. Consequently
\[
 \sum_{i\in H}c_i^2=\frac{n\epsilon+|H|}{3B}
      \le\min\!\left(1,\frac{10104\,r}{y^2}\right),\qquad
 E\mathbf1_H\sqrt n\,|c_i|\le\frac{16000\,r^2}{|y|}.                                  \tag{8a}
\]
For the first bound use $1.84r+3400(r/3.98)^2\le1.85r$ at the available residual, and for the second use (7) divided by $\sqrt{3B/n}$. The bound of one uses $\|J_w\|\le1$. For instance on either horizontal edge $|y|=2^{-17}$ the true clipped column has less than $6.84\,10^{-161}$ squared mass at and beyond its threshold for every stated prime. A nonempty tail of tiny mass can still contain a violating site through unbounded $n$.

## A positive unavoidable correction at a genuine prime

Take $p=173$, $t=1/50+(2161/100000)i$, $\kappa=2$, where the physical unforced root has already passed its [first spread crossing](astra-phase-86-checks.jsonl). At every clipped solution the normalized marked angles both have the sign of $v$, since their tangents are $P_0(1\pm c_0)$ and $|c_0|\le1$. Their sum equals $\arg s$ on the positive chart, so $|\phi_0|\le|\arg t|/2<0.42<\phi_*$. For any two genuine clipped marks the physical square-root secant is the complex scalar $\tanh((z_0+z_0')/2)$, with $U_0=2\sqrt s\sinh z_0$ and the corresponding marked sums. Formula (2) makes this strictly contractive. Equation (3) and the scalar uniqueness thus still hold at this floor, without using the cold mark rectangle.

At these exact parameters the [outward checker](astra-column-90-check.py) certifies
\[
            0.054069769445562523<\epsilon<0.054069769445562525 .                         \tag{9}
\]
Here the price is averaged over all 86 coordinates. In particular every clipped fixed point has positive correction. To check it directly, form an even candidate $Z$ by averaged iteration and two real Newton refinements of (1), enclosing the genuine Paley kernel and the resulting residual afresh in 192-bit Arb. The final residual has sup norm $\rho<10^{-48}$ and the proposed mark has $|\Im\operatorname{arsinh}(Z_0/(2\sqrt s))|<\phi_*$. Thus its secant to every genuine clipped mark is contractive by the same argument. Analytically $m^2<1+(u^2+v^2)/(nu)=51$, every factor has positive real part and argument of magnitude at most $\max(\phi_*,|\arg s|)<\pi/3$. Hence $E|U|<4m<32$. The checker verifies $E|Z|<40$. The residual version of (3) then gives $|M-E\mathcal F(Z)/2|\le\sqrt{72\rho}$. Substitution of that mean enclosure in (4) proves (9) for every clipped solution, including noneven ones. [Outward records](astra-column-90-checks.jsonl)

There is also a qualitative check independent of the numerical clipped solve. The certified real-start row has spread in $(1.57159,1.57160)$. A zero-correction clipped solution would have spread at most $2\phi_*$. These widths sum to less than $\pi$, and the means of both original pairs would equal $M_0$ on the same sheet. The [Hermitian secant identity](astra-phase-86.md#separate-signed-sources-on-the-two-true-extreme-sets) (equation (6) there) forces equality by rotating its coefficient arc to positive real part. This contradicts the two spread bounds. This finite obstruction occurs at the specified small real floor; exact positivity on the nominated cold square is unresolved.

1. Test exact vanishing of the single scalar (4), using the monotone residual decrease for averaged iterates together with the physical predictor. It is enough to detect a single cap-free feasible fixed point at each floor. A possible positive price has all of its square-root mass on the set in (7).
2. On that cap set use $U_i=2\sqrt{1+e_i}\sinh(g_i+i\sigma_i\phi_*)$ and the linear isometry in (1). The complementary Fourier equations are linear at all saturated sites of a prescribed sign. A prime-uniform exclusion of positive product correction there would give the desired common original section; the estimates above do not yet exclude it.
