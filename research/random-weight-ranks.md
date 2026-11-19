# A rank expansion over random frequency weights

Let $n=(q-1)/2$ and take the full real Fourier spaces $U_\sigma=\mathbb R\mathbf1\oplus V_\sigma$ from the [marked-response calculation](marked-response.md). The weights can be asymmetric, so both the sine and cosine components are available. Define

$$\mathcal P_\sigma=\{P\in U_\sigma:P\ge0,\ \overline P=1\},\qquad
F_\sigma(w)=\max_{P\in\mathcal P_\sigma}\sum_{i:w_i>0}w_i\log P_i.$$

Set $F=F_+-F_-$ and $W=\sum_iw_i$. For $w=e_i$, translation of frequencies gives

$$F(e_i)=\log(\theta_+/\theta_-)=2\log(\theta_+/\sqrt n),\qquad \theta_+=\vartheta(\overline H),\quad \theta_-=\vartheta(H).$$

Indeed, the maximum of $P_i$ is independent of $i$. At $i=0$, reversal averaging gives an even spectrum with the same marked value, so the optimum is the [ordinary Fourier theta LP](fourier.md). At uniform weights $F_\sigma(\mathbf1/n)=0$ by Jensen's inequality and feasibility of the constant spectrum.

## Curvature at weights with zeros

Each $F_\sigma$ is convex and homogeneous of degree one, as a supremum of linear functions of $w$. It is continuous on the closed simplex. To see this, use only spectra with $P_i\ge\varepsilon$ in the maximization. Replacing any candidate by $(1-\varepsilon)P+\varepsilon\mathbf1$ loses at most $-W\log(1-\varepsilon)$ in the objective and makes its entries at least $\varepsilon$. The resulting restricted optimum is continuous and converges uniformly on the simplex.

For positive weights the optimizers satisfy $P_iQ_i=nw_i/W$, by the [complementary projection argument](marked-response.md#weighted-complementary-projections). Continuity therefore extends the entropy identity to all nonnegative nonzero $w$:

$$F_+(w)+F_-(w)=\sum_{i:w_i>0} w_i\log(nw_i/W).$$

Fix the support $S=\{i:w_i>0\}$. Project $\mathcal P_\sigma$ onto those coordinates. There is a unique maximizer $P$ in the projected polytope by strict concavity on $S$, with $P_i>0$ on $S$. Let $r_\sigma(w)$ be the dimension of its minimal face **in that projected polytope**. This dimension can differ from the dimension of the optimal face in the full frequency space.

On the open positive orthant on $S$, the sum of the two convex functions has smooth Hessian $\operatorname{diag}(1/w_i)-\mathbf1\mathbf1^{\mathsf T}/W$. On every compact subset of that orthant, the two distributional Hessians are positive semidefinite and are dominated by this smooth matrix. Thus both gradients are locally Lipschitz, for instance by convolution with smooth kernels on smaller open sets. The gradient of $F_\sigma$ is $(\log P_i)_{i\in S}$ by uniqueness and the envelope formula. In particular $P$ is locally Lipschitz and differentiable almost everywhere.

Let $T$ be the direction space of the minimal face at such a differentiability point. Feasibility on both sides of $w$ makes every derivative $\dot P$ lie in $T$, by the active linear inequalities. Also, the nearby minimal faces contain the current minimal face. Every closed face omitting the current maximizer is a positive distance from it, and there are finitely many faces. Therefore the first-order equation against any fixed $h\in T$ holds throughout a neighborhood:

$$\sum_{i\in S}w_i h_i/P_i=0.$$

Differentiate this equation and write $\nu_i=\sqrt{w_i}$. It says that $\operatorname{diag}(\nu/P)\dot P$ is the orthogonal projection of $\operatorname{diag}(1/\nu)\dot w$ onto $E=\operatorname{diag}(\nu/P)T$. Thus almost everywhere on each face of the weight simplex,

$$D^2 F_\sigma(w)=\operatorname{diag}(1/\nu)\Pi_E\operatorname{diag}(1/\nu),\qquad
\sum_{i\in S}w_i (F_\sigma)_{ii}(w)=r_\sigma(w).$$

Homogeneity gives $D^2F_\sigma(w)w=0$ and makes the exceptional set conic, so the almost-everywhere formula also holds on the simplex. Taking the weighted trace of the entropy identity gives $r_+(w)+r_-(w)=|S|-1$. On the full simplex interior all optimizers are strictly positive and $r_+-r_-=\sum_{x\in Q}s(x)=-1$. On a vertex the two ranks are zero.

## An integral identity for finitely many labels

For $k\ge1$, choose $X_1,\dots,X_k$ independently and uniformly from the $n$ frequency labels, allowing repetitions. Independently choose $Y$ uniformly on the $(k-1)$-simplex and set $W^{(k)}=\sum_jY_j e_{X_j}$. Write

$$a_k=\mathbb E F(W^{(k)}),\qquad d_k=\mathbb E\big[r_+(W^{(k)})-r_-(W^{(k)})\big].$$

Condition on the labels and put $G(y)=F(\sum_jy_je_{X_j})$. Let $\mathcal L_k=\sum_{i,j}(y_i\delta_{ij}-y_iy_j)\partial_{ij}$ in simplex coordinates, with the homogeneous extension available for $G$. Under the linear aggregation of repeated labels, the covariance matrix $\operatorname{diag}(y)-yy^{\mathsf T}$ pushes forward to $\operatorname{diag}(w)-ww^{\mathsf T}$. The weighted trace formula gives $\mathcal L_kG=r_+(w)-r_-(w)$ almost everywhere. Aggregation maps the positive simplex onto the face with the chosen labels and has full rank onto that face, so exceptional null sets pull back to null sets.

For the uniform measure on the simplex, integration by parts gives

$$\mathbb E_y \mathcal L_k G=k(k-1)\left(\frac1k\sum_{j=1}^k\mathbb E_{y_j=0}G-\mathbb E_yG\right).$$

To check the factors, use coordinates $y_1,\dots,y_{k-1}$ with $y_k=1-\sum_{i<k}y_i$. The diffusion matrix annihilates each boundary normal. Its divergence has entries $1-ky_i$ and its second divergence is $-k(k-1)$. The outward flux of the first divergence on each facet is $-(k-1)$ after normalizing the simplex volume and expressing the facet integral as an average. Two integrations by parts give the formula. For the log optimum one can first shrink into the simplex by $y\mapsto z=(1-\varepsilon)y+\varepsilon\mathbf1/k$. The shrunk functions have Lipschitz gradients on the closed simplex, so the integrations apply. For each sign, $0\le\mathcal L_k G_\sigma\le k-1$ in the interior. The covariance at $z$ dominates $(1-\varepsilon)$ times the covariance at $y$, so the shrunk functions retain this bound. Changing variables to $z$ on compact subsets of the interior and bounding the remaining boundary layer by $k-1$ proves convergence of the left side. Continuity gives convergence of the right side.

Averaging over the labels deletes one independent label at each facet. Therefore $d_k=k(k-1)(a_{k-1}-a_k)$. For each fixed $n$, $W^{(k)}$ converges in probability to uniform as $k\to\infty$, since $\mathbb E\|W^{(k)}-\mathbf1/n\|_2^2=2(1-1/n)/(k+1)$. Continuity gives $a_k\to0$. Telescoping proves the exact expansion

$$2\log(\theta_+/\sqrt n)=\sum_{k=2}^{\infty}\frac{d_k}{k(k-1)}.$$

The series is absolutely convergent at every fixed field order because $|d_k|\le n-1$. The truncation after $k=K$ has remainder $a_K$. The dimension lost from each sign obeys $\dim V_\sigma-r_\sigma(w)\ge0$, since projection onto a set cannot increase the dimension of a polytope. The sum of the two losses is $n-|S|$, so

$$|(r_+(w)-r_-(w))+1|\le n-|S|,\qquad |d_k+1|\le n(1-1/n)^k.$$

The second bound counts labels missed in $k$ draws. Summing the series from $K+1$ gives

$$\left|a_K+\frac1K\right|\le\frac{n^2(1-1/n)^{K+1}}{K(K+1)}.$$

In particular, truncation at $K=\lceil Cn\rceil$ has error at most $1/K+e^{-C}/C^2$, uniformly in the field order at any fixed $C>0$. At fixed $K$ this argument gives no small remainder as $n$ grows. Balance of each fixed-$k$ mean rank alone would therefore leave the conjecture open.

## The term with two random labels

For distinct labels, project either feasible polytope onto the two marked coordinates. For a positive outward normal $(u,v)$, an exposed edge on $u x+v y=c$ accounts for rank one precisely on the interval of weights $t$ where $x=tc/u$, $y=(1-t)c/v$ lies inside the edge. That interval has length $u|x_{m right}-x_{m left}|/c$. All remaining weights select vertices with rank zero, up to endpoints of measure zero. For coincident labels the two ranks are zero.

The [small-order comparison](../face_ranks.py) evaluates the two-label term by these edge lengths. It integrates the optimized log objective separately and compares to $a_1-a_2=d_2/2$ using the full theta values from the ordinary LPs. In the [eight floating-point comparisons](../data/face-ranks.csv), the largest discrepancy in this identity was $1.2\times 10^{-11}$. At $p=41$ the total is zero, with the first term about $0.01636$ and $a_2$ about $-0.01636$. At $q=25$ the first term is about $0.29167$ and the total about $0.28768$.

At $p=5$ the plus polytope consists of the constant spectrum and the minus polytope is the full nonnegative interval of mean-one spectra. Thus $d_k=-1+2^{1-k}$ for every $k\ge2$, with the second term coming from all labels coinciding. Summing gives $-\log 2$, using $\sum_{k\ge2}z^k/[k(k-1)]=z+(1-z)\log(1-z)$, in agreement with $\theta_+=1$ and $n=2$.

The first term alone is bounded by $(1-1/n)/2$, because two independent labels coincide with probability $1/n$. On the prime-square sequence, the [exact theta value](square-order-control.md) therefore forces $\liminf a_2\ge\log 2-1/2>0$. Thus supports with more than two labels contribute even in the square control.

The [exterior partition formula](rank-partitions.md) decomposes each rank difference into the signs of the unweighted coordinates and the dimensions of localized eigenspaces. This gives a Fourier arithmetic restriction on the latter, a dense-sampling comparison, and experiments beyond two labels.

The [sparse-mark geometry](sparse-mark-geometry.md) bounds the first rank term by common two-mark heights from linear programs and gives a dimension-free fluctuation estimate for the randomized log objective.
