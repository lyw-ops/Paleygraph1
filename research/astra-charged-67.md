# A growing-degree obstruction on the larger true face and an exact tilted marginal

At every sufficiently large eligible prime, every mean-one row on the larger optimal face has normalized RMS distance at least $1/100$ from every polynomial of degree $M=o(p^{1/6})$ in the Jacobi eigenvalue, even after arbitrary changes at the mark and at $k=o(\sqrt p)$ other sites. The edited sites may be chosen after seeing the true row. The coefficients are unrestricted and may depend on the prime, time and row. An exactly sector-feasible row in this class is affine on the bulk. The obstruction uses the full positional Fourier equations on the forbidden mask. It holds before any terminal score is evaluated, so selecting the best trial of this form at $L+1$ does not bypass it.

There is also a way to move a strictly positive trial onto an **exact** optimal face. At the predetermined time $t=L+1$, two perturbations of the unrestricted Fourier LP recover the signed marginal minimum, with the primary mark canceling. A single smooth, strictly positive trial for a perturbed problem gives a row on the actual face with a quantified error after conditioning its vertex decomposition. These statements give no all-prime upper estimate for the resulting marginal.

## The masked Gram estimate

Let $Q=\mathbb F_p^{\times2}$, $n=(p-1)/2$, $G=\widehat Q$, $s(a)=\chi(1-a)$, and $D_\nu=\{a\in Q:s(a)=\nu\}$. Put $X_i=\widehat s(i)/\sqrt p$. Write $F^{-1}$ for the inverse Fourier transform with factor $1/n$, so $\|y\|_{2,n}^2=n^{-1}\sum_i|y_i|^2=\sum_a|(F^{-1}y)(a)|^2$. Mean-one sign-$\sigma$ rows satisfy $F^{-1}y=0$ on $D_{-\sigma}$. The root has $X_0=-1/\sqrt p$, and the mean of $X$ is zero.

For $j\ge2$ let $h_j=p^{1/2-j} H_j$ be the weight-zero trace of the disjoint-parameter hypergeometric with $j$ trivial upstairs and $j$ quadratic downstairs parameters, in the trace convention of the path-column calculation. A common sign convention on each column leaves all norm estimates unchanged. For $T_j$ the Chebyshev polynomial the exact transform is
\[
 F^{-1}T_j(X)(a)=-p^{-1/2} h_j(a)+\delta_j/n,\quad
 \delta_j=T_j(-1/\sqrt p)-(-1/\sqrt p)^j .
\]
This follows by Fourier inversion of the powers of the two conjugate normalized Jacobi sums, correcting the trivial mode. [Exact trace formula](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain)

Adjoin the constant column $h_*=1$ of rank $r_*=1$, and put $r_j=j$. On either sign mask the unnormalized Gram matrix satisfies
\[
 \left|\sum_{a\in D_\nu}h_j(a)\overline{h_k(a)}
                         -\frac p4\mathbf1_{j=k}\right|
                  \le (r_jr_k+1)\sqrt p .
 \tag{1}
\]
Here and below a weight normalization of the sheaves can equivalently be performed after taking the trace. On $U=\mathbb P^1\setminus\{0,1,\infty\}$ expand the mask as
$(1+\chi(a))(1+\nu\chi(1-a))/4$. For each of the four twists the weight-zero tensor with the dual has rank $r_jr_k$ and is tame. Its geometric coinvariants vanish for unequal ranks by irreducibility. For equal ranks those coinvariants are a single scalar with Frobenius eigenvalue one for the trivial twist. A twist containing $\chi(a)$ changes the sole eigenvalue at zero from $+1$ to $-1$. For the remaining nontrivial twist $\chi(1-a)$, the untwisted inertia at one is a pseudoreflection of determinant $(-1)^j$. Its eigenvalue multiplicities for $+1,-1$ are $(j,0)$ for even $j$ and $(j-1,1)$ for odd $j\ge3$. The twist exchanges these unequal multiplicities. For the constant column the nontrivial twists are geometrically nontrivial. These local arguments exclude every additional coinvariant. The compactly supported zeroth group vanishes and the tame Euler characteristic on $U$ is $-r_jr_k$. Thus $\dim H_c^1\le r_jr_k+1$, and Deligne's weight bound in the trace formula proves (1) with the displayed uniform rank dependence. [Katz, §2 on disjoint parameters and inertia](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf) · [Earlier fixed-degree masked correlation calculation](smoothing.md)

For local corrections, adjoin arbitrary nontrivial character columns of \(Q\), one for each of \(k\) distinct edited frequency sites besides the root. Use any one lift of each to \(\mathbb F_p^\times\), taking inverse characters as required by the Fourier convention. These columns have rank one and are all distinct on \(Q\). Two distinct sites cannot become isomorphic via either the trivial twist or \(\chi(a)\), since such a coincidence would make their restrictions equal. A twist involving \(\chi(1-a)\) introduces nontrivial inertia at one in the ratio of two Kummer columns, whose ratio was lisse there. On a diagonal only the trivial twist contributes, and ranks separate the Kummer columns from every \(h_j\), \(j\ge2\). Thus (1) holds unchanged on the enlarged list, even for site sets selected from the data.

The operator norm of the Gram error is at most $2\sqrt p\sum_jr_j^2$ over the enlarged list by the rank-one majorant $2r_jr_k\sqrt p$. Hence for $1+k+\sum_{j=2}^M j^2=o(\sqrt p)$ both Grams lie between $pI/8$ and $3pI/8$ eventually. This includes $M=o(p^{1/6})$, $k=o(\sqrt p)$. A sparse degree list may omit unused terms from the rank budget, even permitting a single degree $o(p^{1/4})$. The same bounds hold whenever the explicit error is at most $p/8$. This proves a restriction estimate simultaneously for all coefficient vectors without any growing-dimensional equidistribution assumption.

## Transferring a trial onto the exact affine sector

Take a real row
\[
 y=A+BX+C e_0+\sum_{j=2}^M c_jT_j(X)+\sum_{\ell\in I}D_\ell e_\ell,
\]
with arbitrary coefficients and any set $I$ of $k$ edited nonroot sites. Suppose $x$ is any mean-one sign-$\sigma$ row and $\|x-y\|_{2,n}\le\epsilon$. Define a second affine row
\[
 y'=1-C'/n+BX+C'e_0,\qquad C'=\sigma n B/\sqrt p .
\]
It has mean one and satisfies every forbidden Fourier equation exactly. Off the positional identity,
\[
 F^{-1}(y-y')(a)=p^{-1/2}\left(d-\sum_{j=2}^M c_jh_j(a)+\sum_{\ell\in I}\frac{\sqrt p}{n}D_\ell\,\overline{\ell(a)}\right),
 \quad d=\sqrt p(C-C'+\sum_{j=2}^M c_j\delta_j)/n .
\]
On $D_{-\sigma}$ its squared norm is at most $\epsilon^2$ because $x,y'$ both vanish there in positional coordinates. The lower Gram bound gives $|d|^2+\sum_j|c_j|^2+(p/n^2)\sum_\ell|D_\ell|^2\le8\epsilon^2$. The squared norm on both masks together is then at most $6\epsilon^2$. At the identity the mean error is bounded by $\epsilon$ using $x$. It follows that
\[
                  \|x-y'\|_{2,n}\le(1+\sqrt7)\epsilon .          \tag{2}
\]
In particular, when $y=x$ the lower bound forces all nonlinear coefficients and supplementary edits to vanish. If $x$ is nonnegative, this affine class has maximum normalized mark tending to $1/\sqrt2$. Indeed on the bulk $y'=1-\sigma B/\sqrt p+BX$. The actual arcsine law provides sites arbitrarily near either endpoint of $[-1,1]$, forcing $|B|\le1+o(1)$. Conversely $B=\sigma/(1+1/\sqrt p)$ is feasible by the Jacobi bound. The mark relation is exactly
\[
                 y'_0=1+B[\sigma(n-1)-1]/\sqrt p .
\]

For the quantitative distance assertion let $x\ge0$ have mark $x_0/\sqrt n\ge1$, as every larger-face row does. The sector equation at the root and the Jacobi estimate give an upper bound of $1/\sqrt n+\sqrt{p/n}$. If $\epsilon\le1/100$ in (2), then $y'_0/\sqrt n\ge1-(1+\sqrt7)/100$ and $y'_0/\sqrt n=O(1)$. The mark relation implies $|B|\ge1.35$ eventually and $B=O(1)$. On the bulk where $\operatorname{sgn}(B)X<-0.9$, the row $y'$ is eventually less than $-0.20$. By the arcsine law that set has asymptotic density $\arccos(0.9)/\pi>0.14$, for either choice of sign. Its contribution alone forces $\|x-y'\|_{2,n}>0.07$, contradicting (2). This proves the claimed uniform obstruction for every indicated degree and edit budget, including the marked-window degree $M=L+1$ with $o(\sqrt p)$ data-dependent edits. The allowed error is normalized RMS of a mean-one row, equivalently counting Euclidean distance after dividing the row by $\sqrt n$. Projecting a polynomial first introduces new fields $KT_j(X)$, which are outside this class. [Jacobi arcsine law and entry bounds](fourier.md)

## Recovering the signed marginal without knowing the exposed support or primary mark

Use probability normalization in this section. Let \(\mathcal C_\sigma\) consist of nonnegative probability rows with the full sign Fourier equations. Put \(\gamma(q)=\sqrt n\,q_0\), \(\alpha_\sigma=\max_{\mathcal C_\sigma}\gamma(q)\) and \(F_\sigma=\{\gamma=\alpha_\sigma\}\). At any positive integer cold time \(t\), put
\[
 c(q)=\mathbb E_q[\sigma Y_t]-E_t/4,\qquad c_*=\min_{F_\sigma}c .
\]
Since \(E_t\le4t\), the range of \(c\) throughout \(\mathcal C_\sigma\) has length at most \(R=4\sqrt{nt}\). The one-step equation is also useful here. For every \(q\in\mathcal C_\sigma\) one has
\[
 \mathbb E_q[\sigma Y_t]=\mathbb E_q|Y_{t-1}|+b_{t-1}\gamma(q)-2g_{t-1}.
\]
Consequently the two sign problems can use the **same nonnegative bulk price** \(|Y_{t-1}|\) in place of their oriented terminal scores, adjusting the root coefficient and constant. The full charge must be retained when interpreting either value. [Cold increment and energy identities](astra-charged-66.md)

A bound on the minimum positive normalized mark gap between distinct vertices is
\[
 \Delta=(2n^{2n})^{-d},\qquad d=[\mathbb Q(\zeta_n+\zeta_n^{-1}):\mathbb Q].
\]
Indeed put \(B=n(I-P_\sigma)\), with \(P_\sigma\) the nonconstant sign projector. The feasibility equations on a probability are \(Bq=\mathbf1\). At a vertex with support \(S\) of size \(a\), the columns of \(B\) on \(S\) are independent by the two-sided perturbation test, and the principal matrix \(B_{SS}\) is positive definite since \(B\) is a scaled orthogonal projector. Its entries are real cyclotomic integers. All conjugates of \(B/n\) are orthogonal projectors, as the forbidden character sets are permuted by Galois and closed under inversion. Write the vertex root as a Cramer quotient \(N/D\), including \(0/D\) if the root is outside \(S\). In every embedding \(D\) is bounded by \(n^a\) and \(|N|\le\sqrt a\,n^{a-1}\le n^a\) by Hadamard. For unequal roots the cross numerator is a nonzero algebraic integer bounded by \(2n^{2n}\) at every embedding. Its integer norm and the bound on the two denominators give a gap at least \(\Delta\) already before multiplying by \(\sqrt n\). This coarse bound also covers repeated roots by comparing only unequal values. [Related projection minor estimates](astra-cold-43.md#an-arithmetic-bound-independent-of-the-faces)

Choose \(h=\Delta/[4(1+R)]\). Over the full polytope compute
\[
 V(u)=\max_{q\in\mathcal C_\sigma}\{\gamma(q)-u c(q)\},\qquad u=h,\ 2h .
\]
Each vertex outside \(F_\sigma\) scores at least \(\Delta-uR\ge\Delta/2\) below an optimal vertex on that face. Thus the maximizing sets at **both** tilts equal the set of exact signed-marginal minimizers on the primary face, and
\[
                  c_*=\frac{V(h)-V(2h)}h.                       \tag{3}
\]
This arithmetic scale is only a sufficient one. In particular (3) alone gives neither the asymptotic value nor a practical numerical conditioning guarantee.

For a canonical strictly positive trial solve at either tilt
\[
 z_u=\arg\max_{q\in\mathcal C_\sigma,\ q>0}
 \left\{\gamma(q)-u c(q)+\frac h n\sum_i\log(nq_i)\right\}.
\]
The uniform row is strictly positive, the domain is bounded, and strict concavity gives a unique maximizer. Stationarity tested towards any feasible \(w\) bounds the linear objective improvement by
\(h[1-n^{-1}\sum_i w_i/z_{u,i}]\le h\). Hence evaluating only the **linear** objectives at \(z_h,z_{2h}\) in (3) changes the answer by at most one. The two errors belong to \([0,h]\), so their difference has modulus at most \(h\). Also
\[
                 2V(h)-V(2h)=\alpha_\sigma .
\]
Using the linear values at the positive trials instead puts the reconstructed mark minus its true value in \([-2h,h]\). The numerator and denominator bounds proving \(\Delta\) apply to roots of vertices from *different* sign polytopes as well, using the same real cyclotomic field. Thus whenever the two primary marks differ, their gap is at least \(\Delta\). Use the common \(R,h\) on both sides. Since \(3h<\Delta\), selecting the larger of the two reconstructed marks gives the true larger sign. In a true tie either sign is eligible.

There is a constructive face extraction even when the face has positive dimension. Decompose \(z_h\) into vertices of the full probability polytope. This can be done by following null directions of the active equations in both directions until a coordinate vanishes and recursing on the resulting smaller supports. Every such decomposition assigns total weight \(\rho\le2h/\Delta<1/2\) to vertices outside \(F_\sigma\), since each costs at least \(\Delta/2\) in the tilted objective. Consequently the largest mark among the vertices in this decomposition **is** the true global mark, so their marks suffice to decide which vertices to retain. Normalize the weights on those tied at that largest mark to obtain \(z_F\). All mass, positivity, support and Fourier equations of the exact optimal face now hold. On each retained vertex the tilted gap is precisely \(h(c-c_*)\), and every discarded gap is nonnegative. It follows that
\[
                       c_*\le c(z_F)\le c_*+\frac1{1-\rho}\le c_*+2 .
\]
In particular the extraction and the two smooth solves both have vanishing error after division by \(L+1\), uniformly through primes. They do not require resolving gaps between secondary scores.

The extraction also admits a test for existing, untilted analytic trials. Let \(z\) be any positive sign-feasible probability supplied together with any opposite sign-feasible probability \(\bar z\) of positive mark. Opposite-sector orthogonality and positivity give \(\alpha_\sigma\le1/\gamma(\bar z)\). In any vertex decomposition of \(z\),
\[
   \rho\le \frac{1/\gamma(\bar z)-\gamma(z)}{\Delta}.
\]
Whenever this is less than one, conditioning as above lands on the exact primary face. For the actual reciprocal pair at bulk floor \(\tau>0\), one has \(\gamma(z)\gamma(\bar z)=1/W\), \(W=1+(1-1/n)\tau\). The numerator is \((W-1)\gamma(z)=O(\tau)\) uniformly. For any sign-feasible probability the exact cold identity gives
\(c(q)=(2t-B_t)\gamma(q)-2t+A_t+H_{\sigma,t}(q)\ge-2t\). Thus conditioning obeys the one-sided, dimension-free transfer
\[
                   (1-\rho)c(z_F)\le c(z)+2t\rho .                 \tag{4}
\]
The same extracted row satisfies this inequality for every time in its cold history. At \(\tau=o(\Delta)\), an \(o(t)\) upper estimate on an actual reciprocal row's signed charge passes to an exact optimizer of the **primary mark**. This last row need not minimize the secondary price. A signed estimate for that positive stationary row at these floors is still missing. [Reciprocal stationary normalization](astra-scalar-40.md)

## Ranked tests

1. At \(t=L+1\) upper-bound the difference of the two whole-polytope linear values in (3) by \(o(ht)\) on the larger sign. Equivalently use their two positive barrier trials with the stated unit error after division by \(h\). This suffices for ordinary theta via the marked cold identity, and the same estimate on both signs supplies a whole pair at \(L\). A positive normalized lower bound for this difference divided by \(ht\) on a prime subsequence rejects the corresponding one-time marginal test.
2. For an untilted reciprocal trial use \(\tau=o(\Delta)\), or prove directly that its discarded weight is \(o(1)\) at a larger floor. Then test \(c(z)\le o(L)\) at \(L+1\) and condition using (4). A positive normalized lower bound for the charge of the specified trial rejects that sufficient test. A repaired larger-face row within \(1/100\) normalized RMS of a marked scalar Jacobi polynomial of degree \(o(p^{1/6})\) is already excluded even after an additional \(o(\sqrt p)\) edited sites, regardless of its proposed charge.
