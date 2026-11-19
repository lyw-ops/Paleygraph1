# Access to the physical marked sheet through finitely many branch scales

Let $I=[a,T]$, with $0<a<1$ fixed and $T=2048$. For the actual normalized marked surface $Y$ of [round 37](marked-surface-37.md), a bounded number of nearby branch values can be accommodated even when their distance to $I$ is much smaller than the width required by a branch-free tube. There is also a cold directional certificate using finitely many jets of the real stationary Hessian. Neither the count-and-separation condition nor the jet estimates are established uniformly for primes here.

## A distance bound allowing marked monodromy

Put $L=T-a$, $\rho=a/8$, and $U=\{t:\operatorname{dist}(t,I)<2\rho\}$. Let $Z$ be the component of $\tau_Y^{-1}(U)$ containing the physical lift of $I$, and $S$ the set of **distinct branch values of this component** in $U$. Denote its cardinality by $k$. The finite proper parameter map gives a finite set. Real positive fibers of the actual stationary problem are simple. For completeness, the marked normalization itself has no ramification over the positive real axis. The sector inequality makes the marked plane coordinate real over real parameters. Generically $(t,u_0)$ determines its normalized point, so on both sides of any exceptional real parameter all nearby fibers are fixed pointwise by conjugation. An exceptional point is real by continuity. In a conjugation-real local coordinate a real analytic map with local degree $e>1$ cannot have only real inverse images on both sides of its real critical value (take a real analytic root of the nonzero unit after fixing its sign). This excludes such $e$. Real-fiber simplicity is used here as background.

Let $\eta=\min(\{\rho\}\cup\{\operatorname{dist}(s,I):s\in S\})>0$. In the curvature-minus-one convention the physical endpoints obey

$$
 \boxed{d_Y(y_a,y_T)\le {2L\over\rho}+4k+
 16k(k+1)\log\!\left(1+{\log(\rho/\eta)\over 2(k+1)}\right).}       \tag{1}
$$

Only the physical interval needs to lift to the indicated endpoints. After removal of the branch fibers, the projection from $Z$ is an unramified covering of $U\setminus S$. Its Poincaré density is the pullback of the base density by disk uniformization. Inclusion of that covering surface into $Y$ decreases the metric. It suffices to bound the length of the **real path itself** in $U\setminus S$, retaining its homotopy class and hence its prescribed terminal lift.

For $k=0$, the centered disks of radius $\rho$ prove (1). Otherwise assign each branch value $s$ its nearest point $c_s\in I$ by orthogonal projection and clamping to the endpoints. Split $I$ into the real Voronoi intervals of the distinct centers, then split each interval at its center. On each of at most $2k$ rays put $r=|x-c|$, with $c$ its center. For **every** $s$, $|x-s|\ge |x-c_s|\ge r$, and also $|x-s|\ge\eta$. Centered disks give density at most $2/\rho$ on the union of the regions $r\ge\rho$, contributing at most $2L/\rho$ in total. They give density at most $2/\eta$ on $r\le\eta$, contributing at most $2$ per ray.

Between $\eta$ and $\rho$, partition the radii at all the distinct values $|s-c|$ strictly between the endpoints. There are at most $k+1$ gaps. In each gap $(r_0,r_1)$ the annulus $r_0<|t-c|<r_1$ embeds in $U\setminus S$. Write $u=\log(r/r_0)$ and $b=\log(r_1/r_0)$. The annular length element along a radius is

$$
 {\pi\,du\over b\sin(\pi u/b)}.
$$

This follows by lifting to the strip $0<\Re z<b$, then mapping the strip to a half-plane by $z\mapsto\exp(i\pi z/b)$. The competing centered disk of radius $r$ gives $2\,du$. The smaller bound is at most $4\,du/(1+\min(u,b-u))$, by the chord lower bound on the sine. The whole gap costs at most $8\log(1+b/2)$, including when only a portion lies on the ray. Pad the gap list with zero lengths to $k+1$. The sum of its logarithmic widths is $\log(\rho/\eta)$, so concavity of the logarithm and summation over rays give (1).

If $k\le K_a$ uniformly and $\log(\rho/\eta)\le(\log n)^{o(1)}$, then $d_Y=o(\log\log n)$. This would give actual marked decay at that cold point by [round 37](marked-surface-37.md), even with nontrivial monodromy in $U$. Separation of at least $\exp[-(\log\log n)^C]$ suffices under bounded count. Equation (1) also applies to a growing count when its right side is at most $\log\log n-\omega(1)$.

Conversely, the actual square lower bound $d_Y\ge\log\log n-O_a(1)$ proves a stronger dichotomy. On any sequence of squares with count $k\le K$, for fixed $K\ge1$, all sufficiently large members have at least one branch value in this physical component and

$$
 \eta\le\rho\exp\{-c_{a,K}(\log n)^{1/(16K(K+1))}\}.              \tag{2}
$$

Use $k(k+1)\le K(K+1)$ and bound the logarithm in (1) by $\log(1+\log(\rho/\eta))$ before exponentiating. Thus bounded nearby branch count forces values closer than any inverse power of $\log n$. The earlier unconditional $O_a(1/\log\log n)$ tube obstruction did not give this conditional alternative. No assertion here bounds $k$ for the actual squares or primes.

## A conjugate branch pair can create a neck of double-logarithmic length

This explicit algebraic model checks the scale of (1). It is not a Paley stationary solution. Write $t_* = \sqrt{aT}$, $b=(t-t_*)/(t+t_*)$ so $b(a)=-s$, $b(T)=s$, $0<s<1$. On the degree-two cover of $|b|<1$ defined by $w^2=b^2+\epsilon^2$, put $z=b+w$. On the physical real arc choose $w>0$. The only branch values are $b=\pm i\epsilon$, and

$$
 b=\tfrac12(z-\epsilon^2/z),\qquad
 z_T= s+\sqrt{s^2+\epsilon^2},\qquad z_a=\epsilon^2/z_T.
$$

For $R_-\in(2s,2)$ and $R_+=3$, the domain $Y_\epsilon=\{|z-\epsilon^2/z|<2\}$ contains $A_-=\{\epsilon^2/R_-<|z|<R_-\}$ and is contained in $A_+$ defined with $R_+$, for small enough $\epsilon$. For the inner inclusion maximize $r+\epsilon^2/r$ at the two radial endpoints. For the outer inclusion use $|r-\epsilon^2/r|<2$. Both annuli contain both physical points for small $\epsilon$. The distance in either annulus equals the integral of the displayed radial density between those points. The positive radial segment minimizes length since the density is radial. The primitive in logarithmic coordinates is $\log\tan(\pi u/(2b_0))$, where $b_0=\log(R^2/\epsilon^2)$. At the cold endpoint $u=\log(R/z_T)$ stays bounded away from zero and infinity, and at the hot endpoint $b_0-u$ has that same value. The two annuli therefore squeeze the distance to

$$
             d_{Y_\epsilon}(z_a,z_T)=2\log\log(1/\epsilon)+O_a(1).  \tag{3}
$$

Thus degree two and a single conjugate branch pair permit diverging distance.

This model also admits an algebraic marker with the actual phase and hot-decay bounds. Put $F=1+\kappa\epsilon^2/z$, for a sufficiently small constant $\kappa>0$ depending on $a$. It separates the sheets. For $c=1-1/n\in[1/2,1)$, $W=1+ct$, the exterior annulus gives $\Re F\ge1-3\kappa$. The identity for $b$ gives $|\Im(\epsilon^2/z)|\le2|\Im b|$. Furthermore

$$
 |\sin(\arg W)|=
 {2ct_*|\Im b|\over |1-b|\,|1-b+ct_*(1+b)|}
 \ge {t_*\over4(1+t_*)}|\Im b|.
$$

It follows on the entire cover that $|\arg F|\le |\arg W|/2$ if $2\kappa/(1-3\kappa)\le t_*/[8(1+t_*)]$. On the physical sheet over $1024<|t|<n$, $\Re t>0$, $b$ stays uniformly away from zero since $t_*<46$. The continuation $w=b(1+\epsilon^2/b^2)^{1/2}$ gives $F=1+O_a(\kappa\epsilon^2)$ uniformly. With $\epsilon=n^{-1/4}$ the marked log is $O_a(n^{-1/2})$ there, while $F(z_a)\to1+2\kappa s>1$. Taking $\kappa$ smaller also gives the inherited numerical hot constant if desired. This realizes sector control, all-real fibers on the positive axis, a bounded branch count, and a nonzero cold mark in one cover. Its distance growth comes from the narrow neck in (3). These properties alone cannot prove a prime result.

## A finite directional Hessian certificate on the actual real path

At a positive real floor $x\in I$, fix the actual positive normalized row $u$ on one sector. Let $B$ span its real even tangent before division by $u$. Let $P$ be the orthogonal projection, for $\langle f,g\rangle_w=\sum_iw_i\overline{f_i}g_i$, onto the complexified relative tangent $E=\operatorname{diag}(1/u)\operatorname{ran}(B)$. With $V=\operatorname{diag}(1/u)B$ and $\mathcal W=\operatorname{diag}(w)$, it is the Hessian projection $P=V(V^T\mathcal W V)^{-1}V^T\mathcal W$. Stationarity gives $P\mathbf1=0$. Write $c=P e_0$, $\underline w=\min(1,x/n)$ and $W=\sum_i w_i$. Thus $\|P\|_{w\to w}=1$, $\|c\|_w\le1$ and $|v_0|\le\|v\|_w$.

Use a scalar parameter $z=1-x/t$ at $t=x$. After multiplying all weights at $t$ by $1-z$, only the exceptional weight changes, from $1$ to $1-z$. Write $u(t)=u(1+h(z))$ coordinatewise with $h\in E$. The exact stationarity condition, wherever the rows are nonzero, becomes

$$
 h=\Psi_z(h):=P\frac{h^2}{1+h}-\frac{z\,c}{1+h_0}.               \tag{4}
$$

Indeed project $(\mathbf1-z e_0)/(1+h)$ onto $E$ and expand $(1+h)^{-1}=1-h+h^2/(1+h)$. The map has zero derivative in $h$ at $(z,h)=(0,0)$. The coefficients $h_j$ for the actual Taylor series $h=\sum_{j\ge1}h_j z^j$ are determined to arbitrary finite order from (4), beginning with $h_1=-c$. Each higher coefficient uses only previous coefficients, pointwise products, the same real projection, and the marked coordinate. This retains the signs of the projected products.

For any $N\ge1$ set $D_N(x)=\max(1,\max_{1\le j\le N}\|h_j\|_\infty^{1/j})$. For any $b\ge2$ with

$$
                  b^{N+1}\ge32\sqrt{W/\underline w},               \tag{5}
$$

the full physical row has a holomorphic section on $|z|<1/(32 b D_N(x))$. Only these **first $N$ directional coefficients** enter the bound. In particular no bound on $P$ as a map in the coordinate supremum norm is needed.

To prove this, let $H(z)=\sum_{j=1}^N h_jz^j$, and let $R=1/(32D_N(x))$. On $|z|\le R$ we have $\|H(z)\|_\infty\le1/31$. The residual $\Psi_z(H)-H$ is holomorphic there and vanishes to order $N+1$ at zero. Its weighted norm on the circle is at most
$\sqrt W(1/930+1/31)+(1/32)(31/30)<\sqrt W$, using $W\ge1$. Applying the maximum principle after dividing by $z^{N+1}$ (or testing against arbitrary fixed unit vectors) gives residual at most $\sqrt W\,b^{-N-1}\le\sqrt{\underline w}/32$ on $|z|\le R/b$.

There, centered at $H(z)$ take a weighted ball of radius $\sqrt{\underline w}/16$. The supremum norm of any member is at most $1/31+1/16<1/8$. For $f(y)=y^2/(1+y)$ we have $f'(y)=1-(1+y)^{-2}$, so on this ball the weighted derivative of (4) has norm at most

$$
        \big[(1-1/8)^{-2}-1\big]+|z|(1-1/8)^{-2}<1/2.
$$

In the rank-one term we used the unit bounds on $c$ and marked evaluation. The ball is mapped into itself, and uniform contraction starting from its moving polynomial center gives the holomorphic section. All coordinates $1+h_i$ remain nonzero. On a real subinterval it gives a positive stationary row, hence the physical one by uniqueness. The normalization $\sqrt{W(t)/n}$ is holomorphic on the indicated $t$-disks below. This constructs a section of the actual marked normalization as well: the meromorphic plane graph from the actual germ lifts to its normalization, including isolated exceptional points by the removable singularity theorem in a local branch coordinate.

The local disk $|t-x|<x/(64bD_N(x))$ maps within $|z|<R/b$ by $z=(t-x)/t$. Its pullback section bounds the hyperbolic metric along the lifted real line. Thus for any $b,N$ satisfying (5) throughout $I$,

$$
                  d_Y(y_a,y_T)\le128b\int_a^T D_N(x)\,{dx\over x}. \tag{6}
$$

If $n>T$ the largest $W/\underline w$ on $I$ is $n/a+n-1$. In particular $b=2$ and $N=\lceil\log_2(32\sqrt{n/a+n-1})\rceil$ suffice. An integrated directional bound $\int_a^T D_N(x)\,dx/x=o(\log\log n)$ at this finite order would give the prime decay. The actual square obstruction proves the reverse necessary bound $\int_a^T D_N(x)\,dx/x\ge(\log\log n-O_a(1))/256$ at this same explicit order. In particular some order $j\le N$, some real $x\in I$, and some coordinate of that actual jet attain magnitude at least $(c_a\log\log n)^j$ for large squares.

There is a useful depth tradeoff. Fix $\delta>0$ and use natural logarithms. If the directional integral were bounded at depth $N=\lceil(1/2+\delta)\log n/\log\log\log n\rceil$, choose $b=(\log\log n)^\beta$ with $(1+2\delta)^{-1}<\beta<1$. Then (5) holds eventually and (6) yields $d_Y=o(\log\log n)$. This is a finite-depth criterion on the **actual stationary real tangent**, which differs from controlling jets of a fixed-depth Picard approximation. Ordinary Euclidean leverage gives only $\|c\|_w\le1$ and allows individual bulk entries as large as $\sqrt{n/x}$. Bounding successive products in (4) by unrestricted projection norms recovers dimension loss already at the first step. The known finite-depth Paley-word trace estimates do not evaluate this stationary Hessian projection applied to all of the required jets. I do not obtain the required prime arithmetic cancellation.

The distance estimate (1), the two square consequences (2) and (6), and the model (3) use ordinary mathematical proofs. They supply neither an all-prime branch separation bound nor all-prime directional control. The ordinary theta limit remains open.

An [exact replay](astra-surface-38-check.py) evaluates (4) on the nonconstant physical prime-13 normalized row $u_i=1+\tfrac12\cos(\pi i/3)$ at $x=30/19$. The projective recurrence has first marked relative jet $-95/388$, and its first twelve orders annihilate the independently known [prime-13 cubic](complex-floor-33.md). The same replay checks the rational constants in the contraction proof. Run from the repository root with the following command. The [two saved records](astra-surface-38-checks.jsonl) are deterministic.

~~~sh
.venv/bin/python -B research/astra-surface-38-check.py
~~~
