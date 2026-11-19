# Propagation of the opposite-law shortfall and its exact flat case

The opposite-law ratio on the adaptive mask has a subclass whose maximum can be evaluated on every prime. If the numerator equals the total shortfall, the best fourth power is the number of masked sites that are at the cap on **every** primary optimizer. Those sites lie in a subgroup of size at most \(1/(2a)\) at a fixed prime gap. The same adaptive pin excludes this entire square-type mechanism on prime sequences with a sufficiently small cofactor. For general ratios there is a quantitative test on convolution powers of the *actual* shortfalls. Its root penalty can be made invariant under approach to a chosen opposite optimizer.

## Exactly efficient shortfalls

Let \(G=\widehat Q\) have order \(n=(p-1)/2\), and let \(P\subset G\setminus\{0\}\) be any exterior mask. Use the [quartic dual](astra-quartic-89.md) with true primary root \(a\), opposite root \(\beta=1/(na)\), and floor \(c>0\) outside \(P\) on the exterior. For an actual opposite law \(w\) write
\[
 s_i=(c-w_i)_+,\quad e_i=(w_i-c)_+\quad(i\ne0),\qquad s_0=e_0=0,
 \quad S=\sum_i s_i,\quad D=c(1-a)/a-(\beta-w_0).
\]
Only \(D>0\) matters. Then \(S>0\). For each primary optimizer write \(u_i=q_i/a\in[0,1]\). At every translate \(t\), sector orthogonality gives \(\sum_i w_i u_{t+i}=\beta\). At the root this says \(D=\sum_i(s_i-e_i)u_i\le S\). Call \(D=S\) exact efficiency. An optimizer of the quartic dual can have strict inequality here.

Put \(H_* = \{t:q_t=a\text{ for every }q\in\mathcal Q_a\}\). This is a subgroup. For each \(t\in H_*\), translation by \(t\) maps the marking face into itself. Its finite order gives equality of the translated face, and composition and inversion give the assertion. Exact efficiency implies \(\operatorname{supp}s\subseteq H_*\), by the preceding identity for *every* optimizer. In fact, with value zero allowed for an empty class,
\[
 \boxed{\quad \sup_{D=S>0}\left(\frac{D}{\|s\|_{4/3}}\right)^4=|P\cap H_*|.\quad}       \tag{1}
\]
Hölder proves the upper. For the converse take \(F=P\cap H_*\ne\varnothing\), exterior costs \(z=1_F\), and any opposite optimizer \(v\). Every primary optimum minimizes this linear cost, since \(q(F)=a|F|\) throughout its face. On the exterior zeros of \(v\) the [finite moment dual](astra-capacity-84.md) gives an opposite field \(U\le z\), equal to \(z\) wherever a chosen primary optimum is positive. In particular \(U=1\) on \(F\). Subtract a large multiple of \(v\) to arrange \(U\le0\) everywhere else outside its zero set and at the root. Normalize the nonnegative field \(1-U\) by its positive sum \(N\). Its law with floor \(1/N\) has shortfalls exactly \(1_F/N\), and its overshoots vanish on the positive exterior of the selected row. Hence \(D=S\). The same construction realizes arbitrary positive weights on \(F\) after increasing the initial constant if needed.

Let \(m_p\) be the smallest positive integer satisfying \(m_p(m_p+1)\ge n\). For *every* primary feasible law and every coset \(C\) of a frequency subgroup \(H\) of size \(h<m_p\),
\[
                         q(C)\le\tfrac12.                               \tag{2}
\]
Indeed, the uniform law on \(H\) is infeasible by the [prime affine support theorem](parallel-low-energy-7.md). Its positional transform is \(1_{H^\perp}\), so some forbidden position belongs to \(H^\perp\). Its character phases on \(C\) are identical and the remaining mass must cancel them. More generally, if \(x_1,\ldots,x_j\in H^\perp\) have every distinct quotient in the forbidden sector, then \(q(C)\le1/j\). The vectors of character values at these positions have Gram matrix \(I_j\) under \(q\). On \(C\) their rank-one contribution has operator norm \(j q(C)\).

At a fixed gap \(a\sqrt n\ge1+\delta\), eventually \(1/a<m_p\). The mass condition \(a|H_*|\le1\) and (2) give \( |H_*|\le1/(2a)\). Consequently, whenever a prime factor \(\ell\mid n\) exceeds \(1/(2a)\), the fourth power in (1) is at most \(n/\ell\), uniformly on all masks. For such orders the conjectured \(O(K^2)\) upper holds for the entire exactly efficient class if \(n/\ell=O(K^2)\). The determined part of the unrestricted quartic objective is additive:
\[
                  T_*(P)=|P\cap H_*|+T_*(P\setminus H_*).              \tag{3}
\]

There is a stronger necessary condition if a quartic minimizer at a [round-88 growing pin](astra-persistent-88.md) is binary on the mask, meaning \(u_i\in\{0,1\}\) for \(i\in P\), with unrestricted values off \(P\). The derivative of its quartic cost is supported on \(F=\{i\in P:u_i=1\}\), where it is constant. First variation gives \(\sum_F u'_i\ge |F|\) for every primary optimizer, so \(F=P\cap H_*\). Conversely, equality \(T_*(P)=|P\cap H_*|\) implies a minimizing row is binary on the mask by (3) and compactness. In the binary case the physical height price is concentrated on \(F\). Write \(h_b=(Z_b)_+\) on the exterior and zero at zero. The true pin gives \(a\sum_F h_b\gg_\delta d\). Since \(|F|\le1/a=O(\sqrt n)\), the [early bounded approximation](astra-quartic-89.md) gives \(\|h_b1_F\|_{2,n}=o(1/L)\) for every admitted \(L\ge2\) with \(\log_2^*L\le(12/13-\xi)\log_2^*p\) and fixed \(0<\xi<12/13\). Thus
\[
 d\ll_\delta a\sqrt n\sqrt{|F|}\,\|h_b1_F\|_{2,n},\qquad
          \frac{|P\cap H_*|}{d^2L^2}\longrightarrow\infty.             \tag{4}
\]
In particular this binary mechanism is impossible on prime sequences with \(\ell>1/(2a)\) and \(n/\ell=O(d^2L^2)\) for even one admitted \(L\). This includes bounded cofactors without assuming infinitely many primes of that form. At square order the unique subfield law has \(H_*=C\), mass one there, and attains (1) and (4) on the same masks. Its failure of (2) is exactly the missing forbidden character on the subfield.

The height conclusion also survives without assuming a binary minimizer. On those same cofactor sequences, every true row pays \(q(h_b1_{P\setminus H_*})\gg_\delta d\) and \(q(r_d1_{P\setminus H_*})\gg_\delta1\). Indeed the cap gives \(q(h_b1_{P\cap H_*})\le a\sqrt{n|H_*|}\|h_b1_{H_*}\|_{2,n}=o(d)\), and \(r_d\le h_b/(2d-1)\) on \(P\). A row in the relative interior of the primary face attains the cap precisely on \(H_*\), since an affine cap constraint that is tight there is tight on the full face. Mixing any quartic minimizer with an arbitrarily small positive fraction of that row therefore pays the surviving height at strict intermediate densities \(0<q_i<a\), and its quartic cost approaches \(T_*\). There is no uniform separation from \(a\) in this last statement.

## A finite-time bound for every actual opposite law

Set \(\mu_i=s_i/S\), \(\epsilon=1-D/S\). Fix any actual opposite maximizer \(v\) with root \(\beta\). Remove its exterior contribution by
\[
 \alpha=\min_{i\ne0:v_i>0} e_i/v_i,\qquad
 e'_i=e_i-\alpha v_i\quad(i\ne0),\quad e'_0=0,\qquad
 b=(w_0-c-\alpha\beta)/S,\quad B=\max(0,b).
\]
The positive exterior of \(v\) is nonempty for the field orders in question. For **every** actual primary optimizer, \(f(t)=1-u_t\in[0,1]\) satisfies
\[
 \sum_i\mu_i f(t+i)+\frac1S\sum_i e'_i u_{t+i}
                      =\epsilon+b f(t)  \quad(t\in G).                 \tag{5}
\]
Indeed expand \(\sum_i w_i u_{t+i}=\beta\) around the floor and use \(\sum_{i\ne0}v_i u_{t+i}=\beta(1-u_t)\). The root loss and the discarded overshoot have both been included.

If the strict shortfalls avoid the positive exterior of \(v\), replacing \(w,c\) by \((1-\tau)v+\tau w,\tau c\), \(0<\tau\le1\), scales \(s,D,S\) by \(\tau\) and changes \(\alpha\) to \(1-\tau+\tau\alpha\). Thus \(\epsilon,\mu,b\) and the normalized remaining overshoot are invariant. This disjointness holds for every sharp witness with \(T_*>0\) and every \(v\), by the cubic contact and complementary support. In particular approaching the optimal face in total variation alone does not weaken (5) for such witnesses.

Take the probability \(L=(\delta_0+(\mu+\check\mu)/2)/2\), where \(\check\mu_i=\mu_{-i}\). The reflected \(w,v\) also give (5) for all primary rows, with reflected costs, by reflection invariance of the sectors. This is valid even if \(P\) is not even, since (5) is a full-group identity. Dropping the remaining overshoot and averaging gives
\[
     L^{*k}(f)\le\epsilon J_k,\qquad
     J_k=\tfrac12\sum_{j=0}^{k-1}((1+B)/2)^j,\qquad k\ge1.            \tag{6}
\]
Here integration is at the root, where \(f(0)=0\). Let \(H=\langle\operatorname{supp}s\rangle\). Use \(m=1/2\) if \(|H|<m_p\), and \(m=1\) otherwise, or use the smaller Gram bound in (2). For a probability \(\nu\) on \(H\), let \(A(\nu,t)\) be the sum of its \(\lfloor t\rfloor\) largest atoms plus the fractional part of \(t\) times the next atom, capped at one when \(t\ge |H|\). Rearrangement using \(0\le u\le1\) and \(\sum_Hu\le m/a\) gives the unconditional upper
\[
 \boxed{\quad
 \frac{D}{\|s\|_{4/3}}
 \le \frac S{\|s\|_{4/3}}
 \left[1-\sup_{k\ge1}
       \frac{1-A(L^{*k},m/a)}{J_k}\right].\quad}                      \tag{7}
\]
This estimate uses the actual distribution of shortfalls and the corrected root coefficient. For instance if some \(L^{*k}\) is within total variation \(t\) of uniform on \(H\), then \(\epsilon J_k\ge[1-m/(a|H|)-t]_+\). When \(|H|\ge(1+\eta)/(2a)\), the lower before subtracting \(t\) is bounded away from zero at a fixed prime gap for every fixed \(\eta>0\), by the two choices of \(m\). A law with very high efficiency can therefore only generate such a group if spreading beyond \(m/a\) sites is slow on the scale set by \(J_k\). At a sharp witness efficiency is exactly \(\sum_Pu_i^4/\sum_Pu_i^3\); (7) is a restriction on the cubic contact profile of the true minimizing row. The full \(O(K^{1/2})\) ratio bound remains open when shortfalls have intermediate efficiency or propagate slowly.

## A prime quotient forces spreading of large shortfall profiles

There is an explicit version with no subgroup mixing hypothesis. Fix a prime \(\ell\mid n\), put \(g=n/\ell\), and push \(\mu\) to the cyclic quotient of order \(\ell\) to get \(\rho\). Then \(M=1/\|\rho\|_\infty\ge S/(g\|s\|_\infty)\). For \(M\ge4\) and every \(k\ge2\),
\[
 \boxed{\quad
 \epsilon\sum_{j=0}^{k-1}B^j\ \ge
 \left[1-\frac1{a\ell}
 -\frac{8/\sqrt{k+1}+(15/16)^{k-2}}{aM}\right]_+ .\quad}             \tag{8}
\]
Use the unmodified, possibly nonsymmetric walk \(\mu\) in (5). At zero its \(k\)-step mean of \(1-u\) is at most the left side. Its \(k\)-step mean of \(u\) is at most \(\|\rho^{*k}\|_\infty/a\), by total mass of \(u\) and positivity under projection.

For the convolution estimate, put \(\phi(t)=\mathbb E_\rho\chi_t(X)\). If \(0<x\le1/16\), let \(A_x=\{t:|\phi(t)|\ge1-x\}\) and \(j=\lfloor1/(2\sqrt x)\rfloor\). For independent \(X,Y\sim\rho\), each \(t\in A_x\) satisfies \(\|1-\chi_t(X-Y)\|_2\le2\sqrt x\). The product triangle inequality puts \(jA_x\) in \(\{|\phi|^2\ge1/2\}\), of size at most \(2\ell/M<\ell\) by Parseval. Cauchy–Davenport gives \(|A_x|\le1+2\ell/(Mj)\le1+8\ell\sqrt x/M\). Fourier inversion now bounds \(\ell\|\rho^{*k}\|_\infty\) by \(\sum|\phi|^k\). Truncating the layer integral at \(t=15/16\) costs at most \((15/16)^{k-2}\sum|\phi|^2\) below the cutoff, including the cutoff value of the entries above it. For the remainder integrate \(k t^{k-1}(1+8\ell\sqrt{1-t}/M)\). The square-root term has integral at most \(1/\sqrt{k+1}\) after removing its coefficient, by Jensen. This proves (8). [Cauchy–Davenport, proved in Tao](https://arxiv.org/abs/math/0308286)

In particular suppose \(a\ell\to\infty\), \(aS/(g\|s\|_\infty)\ge\zeta>0\), and the corrected \(B\le B_0\). Choosing a fixed \(k=k(\zeta)\) to make the last term in (8) at most \(1/4\) gives \(D/S\le1-c(\zeta,B_0)\) for all sufficiently large primes. At a sharp witness \(s_i=\lambda u_i^3 1_P(i)\), so \(S/\|s\|_\infty\ge T_*(P)\). Thus on bounded-cofactor prime sequences with \(T_*(P)\gg\sqrt n\), sharp efficiency tending to one forces the corrected root coefficient to diverge, including after the invariant mixture towards the specified optimizer. No restriction on the size of the generated subgroup or on the Fourier phases of the shortfall walk is required for (8). Its loss can shrink when \(T_*(P)=o(\sqrt n)\).

## Replay and next tests

At \(p=97\), length eight of the delayed pin charges the pair \(\{8,-8\}\) in \(G=\mathbb Z/48\). It generates the six-element subgroup. Its annihilator contains three positions with pairwise forbidden quotients, so the mass cap for this subgroup is \(1/3\). The two masked coordinates of every quartic minimizer are fixed at \(0.3581989458\ldots\) of the primary cap. The checker interpolates an actual sharp opposite law, verifies (5) at every translate, repeats the optimizer extraction after a mixture with weight \(1/128\), and computes the walk bounds from the exact lazy walk. Reflection gives the same minimum on the full face, and strict convexity fixes both masked values. The one-step test bounds efficiency above by \(0.651367616\). A separate exact convolution on the prime quotient of order 43 tests the spreading estimate, with the order-seven subgroup of \(\mathbb Z/49\) as composite control. [Arb384 checker](astra-dual-90-check.py) · [Outward record](astra-dual-90-checks.jsonl)

1. On sharp cubic witnesses outside \(H_*\), estimate the minimum corrected \(B\) over complementary optimizers and the sorted mass of a finite convolution power in (7) at the same physical length. The quantity to control is their quotient in (7), which allows \(B\) and the useful mixing time to vary together.
2. On the residual mask \(P\setminus H_*\), bound the corrected root coefficient for almost efficient cubics, starting with (8) on a largest prime quotient. The shared subgroup height bound already moves the price to strict intermediate densities for a near-minimizing row. A separation from the cap uniform in the prime remains to be proved.
