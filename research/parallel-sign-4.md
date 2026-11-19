# A common signed time integral for the stripped response

For [Randomstrasse 101, Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the two full sign deletions of the true stationary diagonal can both have large cost. The [ordered comparison](stationary-ordered.md) measures these costs on two different exteriors. Here the positive and negative responses run on a single time axis with a common damping weight. The signed tail has an exact formula, and a quadratic form can certify its cancellation even when the two unsigned tails are large. In the true square family the signed tail stays large: for every fixed cutoff $T$, its limit is $4/3-e^{-T}$.

## Common time and the signed response

Use the [stationary notation](stationary-attenuation.md): $K=K^{\mathsf T}$, $K^2=P$ is the projection off constants, $e=Pe_0$, $v=Ku$, and $u_i^2-v_i^2=4w_i$. Put $D_i=v_i/u_i$, $w_0=1$, $w_i=\tau/n$ on the bulk, and let $F$ be $D$ with the marked entry set to zero. For any strict stripped diagonal $E$ write $m_E=\langle e,(K-PEP)^{-1}e\rangle$, with the inverse on the mean-zero space. Write $m_0$ for the **zero diagonal** entry, $K_{00}=-1/n$, and $z=Ke$.

The following algebra holds for any strict real $F$ with $F_0=0$, so the sign split can be taken directly from the true stationary solution without a separation from saturation. Use
$$
V=|F|^{1/2},\qquad S=\operatorname{sgn}F,\qquad
N=V K V,\qquad c=Vz,\qquad b=Sc,\qquad
B=SN,\qquad A=I-B.
$$
Give $S$ the value $+1$ on zero entries; they stay zero in all trajectories starting at $b$. Then $S^2=I$, $A^{\mathsf T}S=SA$, and $\|B\|\le\|F\|_\infty<1$. Let
$$
y(s)=\exp(-sA/2)b,\qquad
j(s)=\|y_+(s)\|_2^2-\|y_-(s)\|_2^2
     =y(s)^{\mathsf T}S y(s),
$$
where $y_+,y_-$ are the coordinates with the corresponding sign of $S$. For $0<t\le1$, put $\varepsilon=t^{-1}-1$. Then
$$
\boxed{\displaystyle
m_{tF}-m_0=\int_0^\infty e^{-\varepsilon s}
\big(\|y_+(s)\|_2^2-\|y_-(s)\|_2^2\big)\,ds .} \tag{1}
$$
Thus the orbit, source, and integration weight for the two squared masses are the same. This uses linear damping of the stripped diagonal, as in [diagonal damping](diagonal-damping.md), with no change of the hyperbolic coordinates.

To prove (1), put $x_t=(K-tPFP)^{-1}e$. Multiplying the inverse equation by $K$ gives $x_t=z+tKF x_t$. Multiplication by $SV$ then gives
$$
(I-tB)SVx_t=b,\qquad
m_{tF}-m_0=t\,z^{\mathsf T}Fx_t=t\,c^{\mathsf T}SVx_t
=c^{\mathsf T}(A+\varepsilon I)^{-1}b .
$$
Because $A^{\mathsf T}S=SA$, one has $j(s)=b^{\mathsf T}S e^{-sA}b=c^{\mathsf T}e^{-sA}b$. Also $\|e^{-sA}\|\le e^{-s(1-\|F\|_\infty)}$, by expanding the exponential of $B$. Integrate this matrix exponential with the additional damping $e^{-\varepsilon s}$ to get (1).

Here is the connection with the two full sign deletion costs. Define $F_+=\max(F,0)$, $F_-=\min(F,0)$, and $L_+=I-N_{++}$, $L_-=I+N_{--}$. On a diagonal retaining only one sign, the other side and the off-diagonal blocks drop out of the preceding inverse. Its unsigned increment from zero is
$$
U_\sigma=\int_0^\infty\|e^{-sL_\sigma/2}b_\sigma\|_2^2\,ds
=c_\sigma^{\mathsf T}L_\sigma^{-1}c_\sigma .
$$
If $I=\int_0^\infty j(s)\,ds$, the costs of adding the missing plus or minus sign to the respective exterior are $g_+=I+U_-$ and $g_-=U_+-I$. In particular, near equality of $g_+$ and $g_-$ only implies near cancellation of the full response if the uncoupled imbalance $U_+-U_-$ is also small. Equation (1) works directly with the coupled response.

## Exact tail and certificates for cancellation

At any $T\ge0$, the signed tail is
$$
J_T=\int_T^\infty j(s)\,ds
=y(T)^{\mathsf T}SA^{-1}y(T)
=\langle y(2T),Vx_1\rangle . \tag{2}
$$
The first equality after the integral follows by restarting the orbit at $y(T)$; the second uses $A^{-1}b=SVx_1$ and $e^{-TA^{\mathsf T}}S=Se^{-TA}$. In particular a single marked inverse plus propagation to $2T$ evaluates the tail without quadrature near saturation.

One can instead certify the tail without the undamped inverse. The symmetric part of $A$ is $L=L_+\oplus L_-\succ0$. Differentiating the ordinary squared norm gives
$$
\int_T^\infty y(s)^{\mathsf T}Ly(s)\,ds=\|y(T)\|_2^2. \tag{3}
$$
For any real symmetric test matrix $Q$, define $R_Q=S-(A^{\mathsf T}Q+QA)/2$. Then
$$
J_T=y(T)^{\mathsf T}Qy(T)+\int_T^\infty y(s)^{\mathsf T}R_Q y(s)\,ds .
$$
Indeed the derivative of $y^{\mathsf T}Qy$ is $-y^{\mathsf T}(A^{\mathsf T}Q+QA)y/2$, and $y(s)$ tends to zero at each finite order. This proves the computable two-sided certificate
$$
-\eta_-L\preceq R_Q\preceq \eta_+L
\quad\Longrightarrow\quad
-\eta_-\|y(T)\|_2^2\le J_T-y(T)^{\mathsf T}Qy(T)
\le \eta_+\|y(T)\|_2^2. \tag{4}
$$
The slacks may be checked by generalized eigenvalues with respect to $L$. They need only be small after multiplication by the surviving mass $\|y(T)\|_2^2$. One can also check the forms just on the cyclic subspace spanned by $b,Ab,A^2b,\ldots$, which contains the entire orbit. Taking $Q=0$ bounds the sides independently; a nonzero test matrix can absorb a large signed contribution into a boundary term.

For example, write
$$
A=\begin{pmatrix}L_+&-C\\ C^{\mathsf T}&L_-\end{pmatrix},\qquad C=N_{+-}.
$$
Select singular pairs $(p_k,q_k,d_k)$ of $C$ with $d_k>0$, put $U=\sum_k p_k q_k^{\mathsf T}/d_k$, and let $\Pi_+,\Pi_-$ be the projections onto the selected left and right singular spaces. With $Q=\begin{pmatrix}0&U\\U^{\mathsf T}&0\end{pmatrix}$, multiplication gives
$$
\frac{A^{\mathsf T}Q+QA}{2}
=\begin{pmatrix}
\Pi_+ & (L_+U+UL_-)/2\\
(L_+U+UL_-)^{\mathsf T}/2 & -\Pi_-
\end{pmatrix}.
$$
Thus the signed mass on the selected channels becomes the boundary term plus an error weighted by dissipation:
$$
\begin{aligned}
J_T={}&2\langle y_+(T),Uy_-(T)\rangle\\
 &+\int_T^\infty\big(\|(I-\Pi_+)y_+\|_2^2-\|(I-\Pi_-)y_-\|_2^2\big)\,ds\\
 &-\int_T^\infty\langle y_+,(L_+U+UL_-)y_-\rangle\,ds .
\end{aligned} \tag{5}
$$
For instance, suppose $I-\Pi_\sigma\preceq \rho L_\sigma$ for both signs. By (3) and $2ab\le a^2+b^2$, the absolute error after the boundary term in (5) is at most
$$
\left(\rho+\tfrac12\big\|L_+^{-1/2}(L_+U+UL_-)L_-^{-1/2}\big\|\right)\|y(T)\|_2^2 .
$$
Alternatively, retain the unmatched term with its sign. The criterion tests whether the surviving slow modes can exchange mass through $C$; the two unsigned integrals need not be bounded by quantities tending to zero.

A two-dimensional calculation illustrates that distinction. Take $L_+=L_-=\ell$, $C=\sqrt\ell$, $b=(\sqrt{\ell/2},0)$ with $0<\ell<1/2$. This is an admissible contraction model: $N=\begin{pmatrix}1-\ell&\sqrt\ell\\\sqrt\ell&-1+\ell\end{pmatrix}$ has $N^2=(1-\ell+\ell^2)I$, and $bb^{\mathsf T}\preceq I-N^2$. The trajectory is $\sqrt{\ell/2}e^{-\ell s/2}(\cos(\sqrt\ell s/2),-\sin(\sqrt\ell s/2))$. The two unsigned integrals each tend to $1/4$; the difference is $\ell/[2(1+\ell)]$. In (5) the unmatched term and boundary term at $T=0$ vanish, and the relative dissipation bound gives an error at most $\sqrt\ell/2$. This is an example of what the certificate can capture, with no claim that the Paley slow subspaces have this form.

## Finite time versus the arithmetic limit

Write $a_k=c^{\mathsf T}B^k b=z^{\mathsf T}F(KF)^k z$. The product equality follows from $VSV=F$ at each occurrence. Then
$$
j(s)=e^{-s}\sum_{k\ge0}\frac{s^k}{k!}a_k,\qquad
m_{tF}-m_0=t\sum_{k\ge0}t^k a_k\quad(0<t<1),\qquad |a_k|\le 1 .
$$
These are the same moments in two different sums. Along any sequence of strict stripped diagonals, cancellation of $m_{tF}-m_0$ for every fixed $0<t<1$ is equivalent to $j\to0$ uniformly on each bounded time interval. For the forward implication take a subsequence with every coefficient converging; the geometric series converges in the limit by the uniform bound on $a_k$. Its vanishing for $0<t<1$ forces all its coefficients to vanish. This applies to every convergent coefficient subsequence, hence each coefficient tends to zero, and the exponential series then converges uniformly to zero on compact intervals. The reverse implication follows from (1) for $\varepsilon>0$ using $|j(s)|\le\|b\|_2^2\le1$.

For a prime sequence with floors $\tau_p\downarrow0$, it therefore suffices to establish fixed-damping cancellation on the true diagonals and
$$
\lim_{T\to\infty}\limsup_{p\to\infty}|J_T|=0 . \tag{6}
$$
Then $m_F\to0$ by (1), and $|m_F-D_0|\le\tau_p$ and the [theta bracket](smoothing.md) give the desired normalized theta limit. One can also prove both hypotheses with the field limit taken at each of a sequence of fixed floors tending to zero: at each such floor the remaining error at the mark is $O(\tau)$, uniformly in the order. Under the fixed-damping assumption, (6) is equivalent to the required undamped cancellation. Formula (4) or (5) gives sufficient conditions expressed entirely in terms of the damped history at a finite cutoff and a matrix inequality. For this formulation, $y(T)$ itself is computable from bounded powers: truncating
$$
y(s)=e^{-s/2}\sum_{k\ge0}\frac{(s/2)^k}{k!} B^k b
$$
at $k=M$ has norm error at most $\|b\|_2\Pr(\operatorname{Pois}(s/2)>M)$. No lower bound on $1-\|F\|_\infty$ enters this finite-time error. The [fixed-depth parity argument](diagonal-damping.md#what-parity-proves-at-fixed-damping) supplies the first hypothesis for fixed-depth diagonals at fixed floor, and explains the separate approximation needed for true stationarity. It does not give that hypothesis for arbitrary decreasing floors. No prime-field bound for (4), (5) or (6) is proved here.

## True square-order obstruction

Take $q=r^2$ with odd prime $r\to\infty$ and any positive floors $\tau_q\to0$. The [exact square control and bulk limit](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors) give $m_F\to1/3$ and $n^{-1}\sum_i(1+F_i)^2\to0$. The elementary Jacobi bound $\|z\|_\infty\le\sqrt q/n$, together with $Kz=e$, then gives
$$
\|b_+\|_2\to0,\quad \|b_-\|_2^2\to1,\qquad
\|Bb\|_2=\|SVK F z\|_2\le\|(F+I)z\|_2+\|Ve\|_2=o(1).
$$
For the first limit use that the plus set has density $o(1)$, and for the second use $\|z\|_2^2=1-1/n$ and $1-|F_i|\le1+F_i$. For the last bound, $V_0=0$ and the bulk of $e$ is constant $-1/n$. Since $B$ is a contraction,
$\|y(s)-e^{-s/2}b\|_2\le(1-e^{-s/2})\|Bb\|_2$.
Consequently on every bounded time interval the plus density tends uniformly to zero and the minus density to $e^{-s}$. The fixed-time signed integral tends to $-1+e^{-T}$, and the exact total in (1) tends to $1/3$. Therefore
$$
\lim_{r\to\infty}J_T=\frac43-e^{-T},\qquad
\lim_{T\to\infty}\lim_{r\to\infty}J_T=\frac43 .
$$
In this family the long-time imbalance is positive and persists even though the positive support has vanishing density and contributes nothing at any fixed time in the limit. The positive late mass is at least this signed tail, so the full positive integral has limit inferior at least $4/3$. This calculation identifies a distinct obstruction from a fixed-time imbalance, which is negative in this family.

## Finite-order replay

The table uses the actual numerical stationary pair at $\tau=0.0005$. The two prefix columns integrate the indicated squared norm on the **same** interval $[0,32]$. The signed tail is from (2). It is added to the prefix difference to get $m_F-m_0$.

| Field order | Plus prefix | Minus prefix | Signed tail | $m_F$ |
| ---: | ---: | ---: | ---: | ---: |
| $97^2$ | 1.0683000 | 0.9276755 | 0.1839449 | 0.3243569 |
| $9413$ | 0.6582497 | 0.6578514 | 0.0002432 | 0.0004291 |
| $193^2$ | 0.7877444 | 0.9542078 | 0.4954573 | 0.3289402 |
| $37253$ | 0.6573239 | 0.6582952 | 0.0006166 | -0.0004084 |
| $389^2$ | 0.4867281 | 0.9705733 | 0.8151261 | 0.3312676 |
| $153649$ | 0.6599442 | 0.6610890 | -0.0000818 | -0.0012396 |

At the largest pair and cutoff $T=8$, the plus and minus prefixes are $(0.6101719,0.6115490)$ at the prime and $(0.1205695,0.9679435)$ at the square. The signed tails at that cutoff are $0.0001505$ and $1.1786548$, respectively. Thus the prime example does not require a large signed tail to cancel its prefix; the square does. A small signed tail by itself does not measure the two unsigned tails. For example at $p=853$ the full integrals are $(0.69419338,0.69357320)$; the unsigned masses after $T=32$ are about $(0.02659,0.02520)$, with signed tail $0.00139$.

A scan using (5) with leading singular vectors of $C$ did not give a sharp certificate on the full space. At $p=173,853$, with the same floor and $T=32$, the best bounds for $|J_T|$ among the tested truncations were about $0.205$ and $0.720$, versus actual absolute tails $0.00086$ and $0.00139$. The scan used rank zero, rank one, all available nonzero singular values, and truncations to 10, 25, 50, 75 and 90 percent of the smaller block dimension, skipping cuts with a retained value below $10^{-8}$. It evaluated the norm of $L^{-1/2}R_QL^{-1/2}$ directly. Thus the two-mode example explains a possible mechanism, but this untailored choice of channels does not account for the observed prime cancellation.

To replay, obtain $v,u$ by `weighted_iterate` in [poisson_weights.py](../poisson_weights.py) and $x_1$ by `solve_mark` in [coset_activation_probe.py](../coset_activation_probe.py) on the stripped diagonal. Generate $B^k b$ by the FFT action $y\mapsto SVK(Vy)$. The table uses $k=0,\ldots,95$ with Poisson coefficients for $s\le64$ (omitted probability less than $10^{-18}$), 24-point Gauss–Legendre quadrature on each of $[0,2],[2,8],[8,32]$, and $y(2T)^{\mathsf T}Vx_1$ for $T=2,8,32$. Across the six displayed orders the stationary and inverse residuals are below $7.5\cdot10^{-11}$ and $2.0\cdot10^{-10}$; the prefix difference plus exact-tail formula agrees with $m_F-m_0$ to within $4.5\cdot10^{-12}$. For an independent dense check at $q=169,173,841,853$ and $\tau=0.0005,0.05$, solve $AG+GA^{\mathsf T}=2bb^{\mathsf T}$. The unique solution is $G=\int_0^\infty yy^{\mathsf T}\,ds$, by integrating its derivative and using decay. Its diagonal gives the unsigned totals, while $\operatorname{tr}(SG)$ and $\operatorname{tr}(LG)$ reproduce the signed response and (3) to within $1.1\cdot10^{-14}$. These are floating-point checks, not interval certificates.

The missing prime argument is a bound on the signed survival of the actual slow source. Fixed-time parity does not provide it. One concrete option is to find a test matrix $Q$ with small boundary term and small residual in (4) when applied after the cutoff; the singular-channel choice (5) explains how opposite contributions can cancel, but the geometry of the true prime stationary modes still has to justify such a choice.

For the half-angle diagonal, the [marked contraction defect](stationary-defect-tail.md) bounds the time-averaged high-mode tail and leaves a signed pairing on the low dissipation modes. Its rank bound uses the size of the true near-saturation set.
