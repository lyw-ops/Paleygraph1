# Local continuation of the true stationary row through phase contact

At the candidate floor, an unforced first contact with phase diameter \(\pi/2\) admits a holomorphic continuation if **either extreme is attained on one inversion orbit**. The physical branch can pass such a contact even if its full Jacobian has an odd kernel. More generally the two extreme sets each support at least one more orbit than the dimension of the even kernel. At contacts with multiple orbits we obtain a bounded incoming slope and a sufficient transverse continuation test. The [all-order continuation argument](root-neutral-unfolding-86.md) treats the remaining straight-ray first contacts in the same chamber. The height-600 forcing path has a separate signed test involving the residual on the actual extreme sites. A positive common width at \(2031/128\) through unbounded primes remains open.

## The actual height-600 forcing and the marked phase

Let \(Q=\{|\Re t-2031/128|,|\Im t|\le2^{-17}\}\), \(n=(p-1)/2\ge10^{30}\), \(t_0=n\), \(t_i=t\) on the bulk and \(W=1+(1-1/n)t\). Write \(E\) for normalized counting. Along the actual real forcing segment from \(X=V_{600}(t)\), put \(R=K\Phi_t(X)-X\), \(q=1-\lambda\), so \(U=K\Phi_t(U)-qR\). Both \(ER=0\) and \(EU=0\), since \(X\) itself is an output of \(K\). Set \(A=\sqrt{t_i}e^{z_i}, B=\sqrt{t_i}e^{-z_i}\), \(U=A-B\), \(\Phi=A+B\), \(\phi_i=\Im z_i\), \(\rho_i=\Re z_i\). The completed factors
\[
          A^c=A+qR/2,\qquad B^c=B-qR/2
\]
lie in the two complementary real Fourier sectors plus constants and have common mean \(M\), since \(A^c-B^c=K(A^c+B^c)\).

Put \(\gamma=\arg W/2\), \(r=\Im(e^{-i\gamma}R)\), \(y=\Im(e^{-i\gamma}U)\) and \(b=(E|t_i|-|W|)/2\). Pair the imaginary parts of the two rotated completed factors. Their product has expectation \((\Im(e^{-i\gamma}M))^2\), and the individual uncompleted product is \(|t_i|[\sin^2(\arg(t_i)/2-\gamma)-\sin^2\phi_i]\). Thus the [earlier imaginary-part identity](astra-imaginary-84.md#a-conjugate-phase-identity-up-to-and-beyond-the-unit-derivative-threshold) in the orientation minimizing its deterministic term gives the exact signed source
\[
 E|t_i|\sin^2\phi_i+(\Im(e^{-i\gamma}M))^2+q^2E r^2/4
                 = b-q E(r y)/2.                                      \tag{1}
\]
This holds throughout the available forced path, including beyond first contact. On its segment in \(|\phi|\le\arctan(3/2)\) the [enlarged-sector secant bound](astra-imaginary-84.md#large-derivatives-at-height-600-beyond-unit-phase) implies
\[
 E |R(U-X)|\le(\sqrt{870}+9.57\lambda)\lambda\|R\|_2^2 .
\]
Indeed split at \(|U-X|=1\), using Cauchy–Schwarz below and \(\|R\|_\infty<0.011\) above. Also \(\|\Im(e^{-i\gamma}X)\|_\infty<2+4.768|\gamma|\). Consequently, with \(L=2031/128-2^{-17}\),
\[
 E|t_i|\sin^2\phi_i \le b+\tfrac q2[(2+4.768|\gamma|)\|R\|_2
                  +(\sqrt{870}+9.57\lambda)\lambda\|R\|_2^2] .
\]
Here \(b\le2^{-34}/[4L(1+L)]\), \(|\gamma|\le2^{-17}/(2L)\). The full upper bound is below \(0.014\). It gives \(|\phi_0|<0.12\) everywhere on this enlarged-sector segment. The field-first limsup of the excess over \(b\) is below \(3.07\cdot10^{-208}\), uniformly over the available parameters, by the [actual residual estimate](astra-dissipation-80.md#the-nonlinear-nine-center-secants). If the phase diameter reaches \(\pi/2\) here, each extreme has magnitude at least \(\pi/2-\arctan(3/2)>0.58\). Thus the mark is absent from both extremes. For an unforced physical contact on \(Q\) at any field the same fact follows directly from the [marked sector](parallel-cold-complex-36.md) and the bound on \(\gamma\).

## Compactness of full factor pairs beyond any phase sector

Fix a field. Over any compact set of floors in the open right half-plane the **unforced** rows on both mean sheets have bounded factors and bounded reciprocals, even after the logarithmic phase chamber or the square-root activation chart is left. To prove this, suppose \(t^{(j)}\to t_*\) and \(L_j=\|A^{(j)}\|_\infty\to\infty\). Passing to a subsequence gives \(A^{(j)}/L_j\to a\ne0\). The means are bounded since they square to \(W\), so \(a\) belongs to the mean-zero plus sector. Put \(S=\operatorname{supp}a\). Bilinear orthogonality against each \(B^{(j)}\) gives
\[
 0=L_j\sum_i a_i B_i^{(j)}
  =\sum_{i\in S}\frac{a_i L_j}{A_i^{(j)}}t_i^{(j)}
  \longrightarrow\sum_{i\in S}t_i(t_*).
\]
Every term in this nonempty last sum has positive real part. This contradiction, and the same argument with the two factors exchanged, give both upper bounds. Their products give the lower bounds. The polynomial factor family is closed and each fiber is a compact complex affine algebraic set, hence finite (each irreducible component has only constant coordinate functions by the maximum principle). This makes the projection proper with finite fibers in this half-plane. In particular every physical normalization point over it has two finite nonvanishing factors at every site. Any failure of the single-valued physical factor germ here comes from finite ramification. The compactness constants depend on the field, and \(\Phi_i=A_i+B_i\) can vanish in the activation chart.

At fixed \(t\) the **actual height-600 forcing line** also has compact full rows over compact forcing sets with \(q=1-\lambda\ne0\), with no sector restriction. Indeed the ordinary pairing of the completed factors gives
\[
 M^2=W-qE(RU)/2-q^2 E(R^2)/4 .
\]
If a sequence of these pairs were unbounded, choose the larger of the two factor norms as \(L_j\), and assume after substitution that it belongs to \(A^{(j)}\). Thus \(M/L_j\to0\), and the bounded completed-factor correction gives \(A^{(j)}/L_j\to a\) in the mean-zero plus sector on a subsequence. The opposite completed factor implies \(\sum a_i B_i^{(j)}=q_j\sum a_i R_i/2\). On \(S\), \(B_i^{(j)}\to0\); since \(q_j\to q_*\ne0\) and \(R\) is fixed at this floor, \(\sum a_i R_i=0\). Multiplying by \(L_j\) now reproduces the same impossible subset sum. The proof for \(B^{(j)}\) exchanges the two factors and reverses the sign of the correction. At \(q_j\to0\), an escaping sequence with the larger factor \(A^{(j)}\) would instead require
\[
   \sum_{i\in S}a_i R_i\ne0,\qquad
   q_j L_j\longrightarrow\frac{2\sum_{i\in S}t_i}{\sum_{i\in S}a_i R_i},
\]
with the opposite sign in the larger-\(B\) case. Along the real incoming forcing segment the limit must be positive real. These statements distinguish an unbounded forced limit at \(q=0\) from the compact genuine unforced fiber there.

## Separate signed sources on the two true extreme sets

At a spread contact in this sector let \(S_+,S_-\) be the sets where \(\phi_i=c\pm\pi/4\), respectively. For any null direction \(h=KDh\), \(D=\operatorname{diag}\tanh z\), put \(\omega=h/\Phi\). The [rotated contraction equality](relative-phase-rotation-85.md#exact-rotation-of-the-linear-problem) gives support in \(S=S_+\cup S_-\), \(Eh=0\) and \(E[(D-i\tan c)h]=0\). As a result \(E Dh=0\) also for a forced contact. The variations \(A\omega,-B\omega\) belong to the two respective mean-zero Fourier sectors since their difference is \(h\), their sum is \(Dh\), and \(h=KDh\). Their ordinary and Hermitian pairings yield
\[
  \sum_S\omega_i^2=0,\qquad
  \sum_{S_+}|\omega_i|^2=\sum_{S_-}|\omega_i|^2.                      \tag{2}
\]
All sites in these identities are bulk. Pair \(A\omega\) with \(B^c\) and its conjugate, and set \(v=i e^{2ic}\). Since \(e^{2i\phi_i}=\pm v\) on the two sets, ordinary counting sums satisfy
\[
 \sum_{S_s}\omega_i=\frac q4\sum_{i\in S} A_i\omega_i
       \left(\frac{R_i}{t}+s\frac{\bar R_i}{|t|v}\right),\qquad s=\pm1.        \tag{3}
\]
Pairing \(B\omega\) instead with \(A^c\) gives the same left side with \(-q B_i\omega_i/4\) and \(\bar v\) in place of \(v\). In particular, if an extreme is one inversion orbit of size \(k\) and there is a nonzero **even** kernel, (2) gives \(|\sum_{S_s}\omega_i|=\sqrt{k/2}\,\|\omega\|_{2,\mathrm{count}}\). Cauchy–Schwarz in (3) and its other-factor version requires
\[
 (1-\lambda)\min_{\epsilon=\pm1}
     \left(\sum_{i\in S}e^{2\epsilon\rho_i}|R_i|^2\right)^{1/2}
                      \ge\sqrt{2k|t|}>5.63\sqrt{k}.                   \tag{4}
\]
This test retains the amplitudes and the actual restricted residual. Equation (3) also retains both phase signs of that residual before the absolute-value bound. No all-prime upper estimate for (4) on the remaining forcing segment has been shown.

At \(q=0\), (3) gives **two separate complex zero sums**. Let \(k_+,k_-\) count the inversion orbits on the two extremes. The restriction of the even kernel to either sign is injective by (2), and its coordinates satisfy an orbit-cardinality-weighted zero sum there. Thus its dimension is at most \(\min(k_+-1,k_--1)\). The real-start solution is even by uniqueness at the real start and invariance of the physical equation under inversion. Any even contact with a single orbit on either side admits the local holomorphic continuation in the even coordinates by the ordinary implicit-function theorem. This argument also works at contacts outside the enlarged sector whenever the two mark-free extremes lie in \((-\pi/2,\pi/2)\). It addresses the contact itself.

## Incoming slope and a local test beyond the contact

At an unforced contact let \(s=|S|\). For any kernel log direction put \(y_i=\Im\omega_i\). By (2), \(\|y\|_2=\|\omega\|_2/\sqrt2\) in unnormalized Euclidean norm. Its separate sums on each sign vanish by (3). On a set of size \(m\), a zero-sum real vector with maximum \(u\) has norm at most \(\sqrt{m(m-1)}u\), as follows by bounding each coordinate below by \(-(m-1)u\) and summing \((u-y_i)(y_i+(m-1)u)\ge0\). Apply this on the upper set and to the negative of the lower set. In particular
\[
   \max_{S_+}\Im\omega_i-\min_{S_-}\Im\omega_i
                      \ge\|\omega\|_2/(\sqrt2 s).                     \tag{5}
\]
The same inequality holds after any scalar rotation of the direction.

Consider a physical unforced branch approaching a finite contact along a straight floor ray from phase spread at most \(\pi/2\). All factors at the contact are nonzero. The real-start germ belongs to an algebraic curve (the rational factor equations are polynomial after clearing the nonzero denominators, and its starting Jacobian is invertible). Its normalization consequently gives convergent Puiseux expansions, including for the local factor logs. If the first variation in those logs had order strictly less than one in \(|t-t_*|\), its nonzero coefficient would be a kernel direction, since the floor variation has higher order. The incoming diameter bound implies that the left side of (5) for this coefficient is nonpositive. This contradiction proves that \(dz/dt\) has a finite one-sided limit along the ray. This holds without a shrinking imaginary-width condition. This slope argument alone leaves higher fractional powers, which the [all-order analysis](root-neutral-unfolding-86.md) excludes on the same incoming ray.

There is also uniqueness on each unforced fiber in the closed phase chamber. Take two solutions on the common mean sheet \(M=\sqrt W\), with log phases \(\phi,\psi\) in the enlarged sector, each of diameter at most \(\pi/2\). Their two factor differences have zero mean and lie in opposite sectors, whence
\[
 \sum_i |t_i|e^{i(\phi_i+\psi_i)}
                  |\sinh((z_i-w_i)/2)|^2=0.                           \tag{6}
\]
If the phases of the coefficients lie on an arc of length strictly less than \(\pi\), positivity after rotation implies equality of the factors. Otherwise differences are supported only on simultaneous maxima and simultaneous minima, and both component diameters equal \(\pi/2\). The marked sector excludes the mark on these two sets. On them the log phase differences have a common value \(\delta\). Write \(d_i=A_i(z)/A_i(w)\). Pairing the first factor difference with the original opposite factor, in the ordinary and Hermitian ways, gives \(\sum(d_i-1)=0\) on each extreme separately, using the two opposite values of \(e^{2i\psi_i}\). The other factor gives \(\sum(d_i^{-1}-1)=0\) on each. All the ratios are \(e^{i\delta}\) times positive numbers. Their unit mean forces that phase to be one, and the equality of the arithmetic and harmonic means forces every ratio to be one. The argument only needs that the extremes are bulk in the closed/closed case, and the strict/strict case of (6) needs no absolute sector bound.

Let \(v_i=dz_i/dt\) denote the limiting tangent just established. If the convex hulls in \(\mathbb C\) of \(\{v_i:i\in S_+\}\) and \(\{v_j:j\in S_-\}\) are disjoint, separation gives a complex direction \(d\) with \(\max_{S_+}\Im(dv_i)<\min_{S_-}\Im(dv_j)\). All local Puiseux conjugates share the finite constant and the integer-order coefficient \(v\). Along \(t=t_*+\epsilon d\) for small positive \(\epsilon\), they all have strictly subcritical diameter, by this linear margin and the fixed gap for non-extreme sites. Equation (6) forces them to agree there, so the physical germ is unramified and continues holomorphically through the contact. Intersecting tangent hulls are the cases this linear test leaves to the [all-order argument](root-neutral-unfolding-86.md). The branch can subsequently leave the chamber or encounter later singularities.

## A three-row certificate on the unforced branch after contact

This test applies to **any** true unforced factor pair, beyond the right-angle contact or the activation-sector boundary. Fix a mean sheet \(M=\sqrt W\). One can take \(A=M+a\) with \(a\) in the plus sector as independent variables and set \(B_i=t_i/A_i\). Vanishing of the plus projection of \(B\) is a square system, and implies \(EB=E(AB)/M=M\). Its kernel consists of log variations \(\omega\) for which \(A\omega\) and \(B\omega\) are in the opposite mean-zero sectors. In fact the derivative of \(B\) has zero mean by differentiating the product and using ordinary complementary orthogonality. All these charts use only nonvanishing of the factors.

On an inversion orbit \(o\) of an even solution, let \(m_o\) be its cardinality, \(l_o=\sqrt{m_o|t_o|}\), and \(u_o=l_o\omega_o\). Form the three-by-orbit matrix \(N\) with column \(l_o(e^{2i\phi_o},e^{-2i\phi_o},t_o/|t_o|)^{\mathsf T}\). For every even factor kernel direction
\[
        Nu=0,\qquad \sum_o\cos(2\phi_o-\beta)|u_o|^2=0
                \quad (\beta\in\mathbb R).
\]
Indeed pair \(A\omega\) with \(B,\bar B\), then \(B\omega\) with \(\bar A\), in the ordinary bilinear convention. The last identity is the rotated real part of the Hermitian pairing of the two variations. Thus for any \(b\ge0\) the sufficient test
\[
       \operatorname{diag}\cos(2\phi_o-\beta)+bN^*N\succ0                \tag{7}
\]
certifies an invertible even factor Jacobian. All entries depend only on the weights and the actual phases. It is meaningful after some raw cosines have become negative; it also works when \(A_i+B_i=0\) at an individual site. A uniform cold-domain result would require control of this or another continuation test at all later points on the incoming physical branch.

## Finite crossing and next tests

At \(p=173\), from the positive stationary solution at \(\Re t=1/50\), the **first** spread crossing on the vertical floor ray occurs at
\[
              0.02158<\Im t_*<0.02161 .
\]
The sole maximal orbit is the fixed site 43 and the sole minimal orbit is \(\{29,57\}\). Throughout the bracket the spread derivative with respect to \(\Im t\) is strictly between 55 and 65. The phase enclosures lie in the enlarged sector through the crossing. The checker encloses the true row in the [validated continuation balls](astra-cold-37-monodromy.py), checks every phase on all earlier segments, and solves the differentiated even stationary equations with interval matrices on the crossing interval. At the later point \(t=1/50+11i/500\), the maximum phase has left the enlarged sector. For \(\beta=0.38\) the two raw cosines on orbits 29 and 43 are negative, while (7) with \(b=10\) has smallest eigenvalue greater than \(0.001\) on the entire even orbit space. A Cholesky preconditioner proposed in floating point is checked by an outward complex-ball norm after subtracting this gap. The previously validated mixed-phase test lies farther along this same finite ray. These finite numbers concern the stated small real floor. [Checker](astra-phase-86-check.py) · [Outward records](astra-phase-86-checks.jsonl)

1. After the [all-order first-contact continuation](root-neutral-unfolding-86.md), bound (7) along the genuine later segment at the cold floor. The conditional signed test permits both a negative raw cosine and exit from the enlarged sector.
2. Along the height-600 forcing segment estimate the two signed restricted sums in (3), particularly on repeated extreme orbits. At an isolated extreme orbit the concrete amplitude-weighted threshold in (4) suffices.
