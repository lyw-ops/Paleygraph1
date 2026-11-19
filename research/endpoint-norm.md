# The marked projection and the cost of nonnegativity at theta endpoints

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), a uniform bound on the least squared norm on the larger-theta side would close the [quadratic-path argument](parallel-quadratic-limit-9.md#exactly-which-theta-witnesses-the-path-selects), given the fixed-width convergence. The least-norm endpoint has two exact descriptions. Its own norm is the reciprocal of a normalized marked kernel weight. The opposite norm is an inverse spectral moment plus a separate cost of nonnegative extension. Both descriptions use the support of the endpoint itself.

## Cone projection from an opposite optimizer

Let $P_+,P_-,J$ denote the three Fourier projections as in [the quadratic regularization](quadratic-theta.md). Put $j=\mathbf1/\sqrt n$ and $U_\sigma=\mathbb Rj\oplus\operatorname{ran}P_\sigma$. Let $X,Y$ be the least-norm complementary theta optima in $U_\sigma,U_{-\sigma}$, both with $\langle j,X\rangle=\langle j,Y\rangle=1$, and let $\alpha=X_0$, $Y_0=1/\alpha$. Feasible vectors of opposite signs always have inner product one at this normalization. In particular optima are complementary off the mark.

Any opposite optimum $Y$ fixes the entire plus optimal face, through $S_0=\{0\}\cup\{i:Y_i=0\}$. Every plus optimum vanishes outside $S_0$. Conversely, if $x\ge0$ is supported on $S_0$ and in $U_\sigma$, with $\langle j,x\rangle=1$, then $\langle Y,x\rangle=x_0/\alpha=1$ and $x$ is optimal. With $E_{S_0}$ the extension by zero and $N_0=\ker(P_{-\sigma}E_{S_0})$, project $j\vert_{S_0}$ onto the cone $N_0\cap\mathbb R_+^{S_0}$. Denote the projection by $w$. The cone projection identity $\langle j,w\rangle=\|w\|^2$ and Cauchy–Schwarz give $X\vert_{S_0}=w/\|w\|^2$. This gives a minimum norm computation from one arbitrary opposite LP optimum and a separate projection, even when positivity is active on the optimal face. In an orthonormal basis of $N_0$ the dual projection is a nonnegative least-squares calculation from the coordinate inequality multipliers.

## Quantities on the actual support

Now use the actual support $S=\{i:X_i>0\}$, let $T=P_{-\sigma}E_S$, $C=T^*T$, and $N=\ker C$. In formulas on $S$ write $j$ and $e$ for the restrictions of $j$ and $e_0$. For any $u\in N$, even signed, $\langle j,u\rangle=\langle Y,E_Su\rangle=u_0/\alpha$. Thus $e_N=\alpha j_N$ for the projections onto $N$. Also every signed direction in $N\cap j^\perp$ can be followed both ways locally from $X\vert_S$, by strict positivity on this support. First-order minimality of $\|X\|^2$ therefore gives

$$ X\vert_S=\frac{j_N}{\|j_N\|^2},\qquad
\|X\|^2=\frac{1}{\|j_N\|^2}=\frac{\alpha^2}{\|e_N\|^2}. \tag{1} $$

This is the actual endpoint version of the [terminal-support identity](parallel-quadratic-support-9.md#the-terminal-support-and-its-marked-schur-formula). It need not use the same set of coordinates as the terminal support at positive width. In particular the atom at zero in the spectral measure of $e$ controls the norm in (1), irrespective of the smallest **positive** eigenvalue.

The opposite mean-zero vector $u=Y-j$ satisfies $T^*u=(e-\alpha j)/\alpha=:v/\alpha$, since $Y\vert_S=e/\alpha$. Its minimum-norm linear extension is

$$ u_{\rm lin}=\alpha^{-1}TC^\dagger v. $$

The correction $k=u-u_{\rm lin}$ lies in $\operatorname{ran} P_{-\sigma}\cap\ker T^*$ and is perpendicular to $u_{\rm lin}$. The correct decomposition of the opposite norm is

$$ \|Y\|^2-1=\alpha^{-2}\sum_{\lambda>0}\frac{\|L_\lambda v\|^2}{\lambda}+\|k\|^2, \tag{2} $$

where $L_\lambda$ are the spectral projections of $C$. The least-norm opposite optimum minimizes $\|k\|^2$ subject to $j+u_{\rm lin}+k\ge0$. This follows since any such vector is opposite-feasible with the optimal mark. The correction vanishes precisely if $j+u_{\rm lin}$ is nonnegative. It is at least the squared norm of the negative part of $j+u_{\rm lin}$ whenever that part is present. In the terminal-support formula the path implies $P_{-\sigma}Y\in\operatorname{ran}T$. At the actual endpoint support, positivity of the linear extension needs its own check.

For example, (2) gives $\sum_{0<\lambda\le t}\|L_\lambda v\|^2\le\alpha^2 t(\|Y\|^2-1)$. Thus control of the opposite norm controls the **marked** low spectral mass of $v$, with no lower bound needed on the individual positive eigenvalues. The first term in (2) can be measured as a cumulative inverse moment, to distinguish a near-zero eigenvalue from one that contributes to the extension.

## The exact tangent width as a dual extension

For the [one-sided penalty](parallel-endpoint-10.md#the-finite-test-on-the-actual-endpoint) $x_0-t\|x\|^2$, the first-order condition at $X$ is that $e_0-2tX$ belong to the polar of $V_\sigma\cap\{d:d_{S^c}\ge0\}$. Here $V_\sigma=\operatorname{ran}P_\sigma$, and the polar is $U_{-\sigma}+\{u:u_S=0,u_{S^c}\le0\}$. This is the finite-dimensional cone sum formula for a linear subspace and a polyhedral cone. Equivalently there is $F\in U_{-\sigma}$ with $F_S=(e_0-2tX)_S$ and $F_{S^c}\ge0$. For any opposite optimum $Y$, write $F=\alpha Y-2tG$. Since $\alpha Y_S=e$, the exact certificate at any $t>0$ is

$$ G\in U_{-\sigma},\qquad G_S=X_S,\qquad
          G_i\le \frac{\alpha}{2t}Y_i\quad (i\notin S). \tag{3} $$

Thus the scaled reciprocal tangent width $\alpha/(2t_*)$ is the minimum nonnegative domination factor in this linear extension LP. The constraint for a shared zero $Y_i=0$ is simply $G_i\le0$. The chosen opposite optimizer changes the ratios in this LP while preserving its value by the first-order equivalence. On every extension in (3), orthogonality gives $\langle j,G\rangle=\langle X,G\rangle=\|X\|^2$. When $\|X\|^2>1$, summing the off-support inequality therefore gives

$$ 2t_*(\|X\|^2-1)\le \alpha-1/\sqrt n. \tag{4} $$

A lower estimate for $t_*$ would require constructing an extension with a sufficiently small domination factor, including its signs at the shared zeros. The minimum-norm linear extension is one test candidate. It is obtained by solving $T^*(G-\|X\|^2j)=(X-\|X\|^2j)_S$, with $G-\|X\|^2j\in\operatorname{ran}P_{-\sigma}$.

## An exact positive extension cost at $p=97$

For $p=97$, use the even representatives of the cyclic frequency group of order 48. The positive support of the two least-norm optima is, respectively,

$$\{0,2,3,5,6,7,8,11,13,14,18,19,22\},\qquad
\{0,1,4,9,12,15,16,17,20,23,24\}.$$

The [cyclotomic certificate](../endpoint_extension_certificate.py) solves the forbidden Fourier equations at anchor one in $\mathbb Q[Z]/(\Phi_{48})$ on both supports. Ball arithmetic certifies all active entries positive. Complementarity and the common mass after normalization prove that both vectors are optimal. The minus face has a one-dimensional support kernel on the full allowed set. On the plus face, the two allowed zero representatives are 10 and 21. With the mark held at one, their values determine all changes to the other coordinates. The squared norm has strictly positive directional derivative in each direction that increases one zero coordinate, holding the other fixed. Convexity then certifies the displayed plus vector as the least-norm optimizer.

For $S$ the **minus** optimal support, the linear plus extension $j+u_{\rm lin}$ has negative coordinates 10 and 38. In mean-one normalization they are about $-0.838135$, giving a certified lower bound $0.02926$ for the extra squared norm in (2), in the sum-$\sqrt n$ convention. Using the certified least-norm optimizer, the actual extra squared norm lies between $0.17278$ and $0.17280$. The marked inverse term by itself is therefore insufficient for the opposite norm already at a small prime.

## Finite spectral comparisons

[The numerical replay](../endpoint_norm.py) first solves both ordinary Fourier LPs, then projects onto the nonnegative support kernels using the opposite LP outputs. It performs the spectral calculations in the real even subspace with orthonormal orbit coordinates. The minimum-norm optima are even by inversion symmetry and uniqueness. Numeric ranks use a threshold of $10^{-11}$. When the two strictly complementary supports each give a square anchored Fourier system, it can instead enclose their solutions with ball arithmetic and certify the norms. In that case the solved supports and positivity prove endpoint optimality independently of the numerical rank threshold.

The [54 rows](../data/endpoint-norm.csv) in the [two files](../data/endpoint-norm-large.csv) cover 15 prime and 12 square orders up to 9413. Twenty-two prime rows have interval-certified norms. Here are selected comparisons for computing $\|X\|^2$ on the plus side.

| Order | $\|X\|^2$ | $\|e_N\|^2$ | Smallest positive eigenvalue | Opposite inverse energy from $\lambda\le1/n$ |
|---:|---:|---:|---:|---:|
| 1009 | 3.494029 | 0.281040 | $2.7653\cdot10^{-4}$ | 0.077158 |
| 1997 | 3.586928 | 0.277638 | $7.8474\cdot10^{-5}$ | 0.054308 |
| 4001 | 3.786380 | 0.262945 | $5.0822\cdot10^{-6}$ | 0.022927 |
| 9413 | 3.779003 | 0.264848 | $2.2971\cdot10^{-6}$ | 0.022010 |
| $97^2$ | $96$ | $1/49$ | about $0.510417$ | 0 |

The square norm and kernel weight in the last row also follow from [the exact square uniqueness result](square-endpoint-uniqueness.md). In the listed primes, the smallest positive eigenvalue shrinks while the norm stays near four and the measured inverse contribution below $1/n$ stays small. The finite comparisons leave open an all-prime lower bound on the marked kernel weight in (1) on the larger-theta side.
