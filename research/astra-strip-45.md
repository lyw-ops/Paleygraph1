# Fourier certificates for the physical strip and its signed derivatives

For each field below, the actual plus marked logarithm has a physical section on $1/32\le |t|\le2048$, $|\arg t|<0.065$. All four fields satisfy the hot theorem throughout the Cayley disk of radius $1/4$ about 2048: its moduli range from $6144/5$ to $10240/3$, strictly between 1024 and each $n$. The following intervals bound the integrals of the absolute values of **signed scalar derivatives** for $f(s)=m(2048e^{-s})$, $0\le s\le16\log2$.

| Order | $n$ | $m(1/32)$ (rounded) | $\int \lvert f'''\rvert$ | $\int \lvert f^{(4)}\rvert$ |
|---|---:|---:|---:|---:|
| Prime 7681 | 3840 | −0.01021145 | (0.0063038, 0.0064109) | (0.0117348, 0.0121848) |
| Prime 12289 | 6144 | −0.00565251 | (0.0031584, 0.0032115) | (0.0048650, 0.0051698) |
| Prime 40961 | 20480 | −0.00237705 | (0.0032570, 0.0033122) | (0.0060138, 0.0064517) |
| Square 7921 | 3960 | +0.32031327 | (0.60314, 0.61680) | (2.3837, 2.4758) |

The square's cubic integral is more than 94 times the neighboring prime 7681's; its fourth-order integral is more than 195 times the prime's. The last two prime intervals are disjoint in the direction of *increasing* variation at both orders. A criterion imposing monotonicity in the prime order on these finite intervals would already fail. The finite strip lower bounds and integrals give no all-prime envelope or ordinary-theta limit.

## Certifying a chart without inverting a stationary Hessian

Let $x>0$, $z=1-x/t=Ry$, and $w=(1,x/n,\ldots,x/n)$, $W=\sum w_i$. In the plus affine Fourier space the row has mean one and its remaining frequencies have sign $+1$. Its tangent $T_+$ omits the constant. Construct real polynomials $U,V$ in $y$ of degree $N$; $U$ has mean identically one and only plus frequencies off zero, while $V$ has only minus frequencies off zero and unrestricted mean. The relation to approximate is the coordinatewise product
\[
 U(y)V(y)\simeq w-z e_0.
\]
The residual certificate below applies to arbitrary such polynomial rows, independently of their origin.

Put $u=U(0)>0$, $H=U/u-1$, and $P$ equal to weighted orthogonal projection onto $E=\operatorname{diag}(1/u)T_+$ using $w$. All these spaces are complexified from real spaces. With $h\in E$, stationarity is $P[(1-ze_0)/(1+h)]=0$, or the fixed point equation $h=\Psi_z(h)=h+P[(1-ze_0)/(1+h)]$. This uses the exact normalization $w_0=1$. We need not assume that $u$ is the physical center row. The projected constant $P1$ may be nonzero. Because $P[uV/w]=0$ by complementary Fourier supports, the residual at $H$ has norm at most
\[
 e=\left(\sum_i w_i\left[
 \frac{\sum_k|[y^k](w_i-Ry\mathbf 1_{i=0}-U_iV_i)|}
 {w_i(1-b_i)}
 \right]^2\right)^{1/2},\qquad
 b_i=\sum_{k\ge1}|[y^k]U_i|/u_i .
\]
The formula controls all $|y|\le1$ and uses only coordinate products and Fourier support. Let $d=1/64$, $b=\max b_i+d$, $r=d\sqrt{\min w_i}$, and $\lambda=(1+R)/(1-b)^2-1$. On the weighted radius-$r$ ball about $H$, each coordinate has modulus $\le b$. Writing $\Psi_z(h)=P[1+h^2/(1+h)-ze_0/(1+h_0)]$ shows that its derivative has norm at most $\lambda$. Thus
\[
 b<1,\qquad \lambda<1,\qquad e<(1-\lambda)r
\]
give a unique local branch in this ball and logarithmic marked prediction error $\Delta=e/((1-\lambda)(1-b))$. Uniform contraction of holomorphic iterates gives holomorphy. All real members are positive stationary rows, hence agree with the unique physical rows. Disk intersections in the $t$-plane are convex, invariant under conjugation and intersect the positive real line whenever nonempty, so the physical charts glue.

For reproducibility, the preprocessor uses the quadratic system $s^2-(Ks)^2=4(w-z e_0)$ and FFT applications of $K$ in numerical Krylov solves. The candidate factors are $(s\pm Ks)/2$, with the plus mean divided out and transferred to the minus factor. The checker takes the first half of each real floating coefficient array as exact binary inputs and reflects it to an even row. It corrects each row implicitly by deleting its forbidden Fourier coefficients and enforcing the prescribed plus mean. An Arb DFT bounds every time-coordinate correction by the discarded Fourier $\ell^1$ sum divided by $n$, including the constant change. Enclosure of the product residual then uses Arb polynomials at 128 bits. Floating solves select candidates only. No numerical inverse, interval dense Hessian, or claim about uncomputed Fourier entries is used to certify stationarity.

Every field passes with $R=1/12$, $N=10$, and the same 118 centers of consecutive ratio at most $11/10$. The round-44 geometric inequality $(\sqrt{11/10}-1)^2+\sqrt{11/10}(13/200)^2<(1/12)^2$ proves the stated angle. Along a cell put $v=\log(x/t)$. If $F(y)=U_0(y)$, $C(y)=1-Ry/W$, $J(y)=1-Ry$, the physical log is within $\Delta$ of
\[
 \log F(y)+\tfrac12\log(C(y)/J(y))+\tfrac12\log(W/n),\qquad
 y=(1-e^v)/R .
\]
For either order $j=3,4$, Cauchy bounds the derivative error by $j!\Delta/(\log(1+R)-\max_{\rm cell}|v|)^j$. The checker combines the cubic terms over denominator $(CF)^3$ before evaluating. If the cubic numerator is $G$, the differentiated fourth-order numerator is $(CF)DG-3G D(CF)$ over $(CF)^4$, with $D=-(J/R)\,d/dy$. Real interval quadrature uses 32 closed subdivisions per cell, with midpoint evaluations also bounding each supremum from below. The four records include rigorous supremum enclosures and both endpoint marks.

## Testing for an actual marked obstruction with real data

For the square, a separate Schur test excludes the physical Cayley disk $|(t-c)/(t+c)|<3/5$ at $c=(5/4)^{13}/32$ (equivalently $1220703125/2147483648$). Its radial extremes $c/4,4c$ lie in $[1/32,2048]$. The largest absolute argument is $2\arctan(3/5)<1.081$. Thus a strip of half-angle $1.081$ cannot carry a physical marked section for square 7921.

To see why this detects the *marked* branch, write $a_n=(n-1)/n$ and $W(t)=1+a_nt$. On a physical section the inherited sector bound is $|\Im m|\le|\arg W(t)|/2$. A Cayley disk of radius $h$ about $c$ has Euclidean center $c(1+h^2)/(1-h^2)$ and radius $2ch/(1-h^2)$. Consequently $|\arg W|\le\phi$ with
\[
 \sin\phi=\frac{2a_nch}{1-h^2+a_nc(1+h^2)} .
\]
The presumed section yields a disk self-map $g=\tanh(\pi m/(2\phi))$ in the normalized coordinate $u=(t-c)/(h(t+c))$. Given its real interpolation values, eliminate each real node $u_i$ by replacing $g$ by $[(g-g_i)/(1-g_i g)]/[(u-u_i)/(1-u_i u)]$. Schwarz's lemma forces every reduced function to remain in the closed unit disk. The nine certified real marks in the square record instead give a final enclosure strictly above $1.1134$. If the component of the normalized marked surface over the proposed disk were unramified, properness and simple connectivity would give the contradicted section. There is therefore accessible marked ramification. The test locates no particular branch value.

There is also a converse for a single proposed disk using *ordinary* Pick matrices. Choose an infinite sequence of distinct nodes dense in its real diameter, let $g_i=\tanh(\pi m(t_i)/(2\phi))$ be the exact physical real values, and form
\[
 M_{ij}=\frac{1-g_i g_j}{1-u_i u_j}.
\]
A physical **marked** section exists over the disk if and only if all finite principal matrices are positive semidefinite. Necessity follows from the disk Pick kernel. For sufficiency, finite Nevanlinna–Pick interpolation gives a disk self-map for each initial node set. Montel's theorem and a diagonal subsequence supply a common limit interpolating every node. An interior real value has modulus strictly less than one, so the limit takes values in the open disk by the maximum principle. Its inverse transform $(2\phi/\pi)\operatorname{arctanh}g$ is holomorphic and agrees with the actual mark on the real diameter by density. The identity theorem gives the physical germ at each real point. The associated graph in the algebraic marked coordinates $(t,\exp(m)\sqrt{n/W})$ satisfies the physical algebraic equation throughout by the identity theorem and lifts to its normalization, including isolated singular points by the local normalization and removable singularity theorem. This converse concerns the normalized marked surface; the positive full-row estimates above give a stronger certificate for its section. In particular, failure of marked extension on this disk has *some finite real-data witness* on any prescribed dense node sequence. No computable upper bound on the required witness size follows here. The theorem is an application of classical interpolation; the model-specific inputs are the sector constant and the exact physical real data.

The additional upper half-disk test uses $H_{\pm}(t)=\tfrac12\log W(t)\pm m(t)$. On the upper half of any proposed disk both imaginary parts are nonnegative by the same sector inequality. The map $\xi=((1+u)/(1-u))^2$ conformally identifies the upper half-disk with the upper half-plane. For real interpolation points define the real Loewner matrix with off-diagonal entries $(H_i-H_j)/(\xi_i-\xi_j)$ and diagonal $dH_i/d\xi_i$. Its positive semidefiniteness follows from positivity of the half-plane Pick kernel and passage to the real boundary using analytic continuation through these real points. A strictly negative Arb quadratic form on an integer vector consequently gives another genuine marked obstruction. Derivatives at the nodes are obtained by Cauchy on a verified chart. For square 7921 the plus test with nine nodes at the same center already has a negative quadratic form at radius $1/2$, giving the stronger angular upper bound $2\arctan(1/2)<0.928$. For all three primes the finite scans were inconclusive. The test routines never interpret an unsuccessful search or rejected chart as a singularity.

## Replay

The four chain records use [the Fourier checker](astra-strip-45-check.py). The two obstruction scans have separate [Schur](astra-strip-45-pick.py) and [Loewner](astra-strip-45-loewner.py) checkers. From the root run the following for each checker, setting `script` to its path.

~~~sh
export OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
for p in 7681 12289 40961; do
  .venv/bin/python -B "$script" --prime "$p"
done
.venv/bin/python -B "$script" --prime 89 --square
~~~

The records follow `astra-strip-45-qORDER.jsonl`, `astra-strip-45-pick-qORDER.jsonl` and `astra-strip-45-loewner-qORDER.jsonl`. The reported angles, integral bounds and negative quadratics use Arb enclosures; a floating eigenvector only selects an integer vector which the Loewner checker evaluates afresh in Arb.

## Ranked next tests

1. Prove a prime-uniform estimate on the displayed complementary polynomial product residual and relative coordinate motion, allowing a locally varying mesh. The quantitative target is a physical lifted distance $\le\log\log n-\omega(1)$ through every sufficiently large eligible prime. A genuine obstruction to a proposed disk is a certified Schur or Loewner violation; a failure of the residual inequality only rejects those polynomial factors.
2. Test higher signed orders against a specified common integrated envelope with the divergent quotient sum of round 39, beginning with the four fields and a comparable square sequence. A certified lower integral above a proposed bound is a counterexample at that field; excluding an *eventual* envelope requires such violations on arbitrarily large primes. Orders three and four alone do not imply quasi-analyticity.
