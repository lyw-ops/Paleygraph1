# Short forbidden cycles on a nearly saturated prime subgroup

At a fixed larger-side gap the trapped sharp shortfall of [round 92](astra-height-92.md) carries at most \(0.462700+o(1)\) primary mass. For even order of the positional subgroup this improves to \(1/3+o(1)\) on the plus side and \(1/\sqrt5+o(1)\) on the minus side. A distinct self-inverse coset incurs an additional factor of two when the tests are applied to the annihilator of the subgroup and coset together. On every surviving candidate the optimizing cubic becomes uniform on a set specified by the physical pin alone.

## The joint test on the same physical pin

Write \(G=\widehat Q,\ n=(p-1)/2,\ a=\max q_0,\ \gamma=\sqrt n\,a\ge1+\delta\), where \(Q\) is the subgroup of nonzero squares and \(p\equiv1\bmod4\) is prime. Use the physical exterior mask \(P\), positive companion \(h_b\), actual quartic minimizer \(q\), \(u=q/a,\ S=\sum_Pu_i^3,\ \alpha=aS,\ \mu_i=1_P(i)u_i^3/S\) of rounds 88–92. In the trapped alternative \(\alpha\ge\zeta>0\), sharp efficiency tends to one, and every fixed convolution power has normalized root tending to one. There is a subgroup \(K\le G\) and a self-inverse coset \(C\) on which \(\mu(C)=1-o(1)\). Both \(K\) and \(C\) have average \(q\) equal to \((1-o(1))a\). Set
\[
 L=K\cup C,\quad t=[L:K]\in\{1,2\},\quad B=L^\perp,\quad b=|B|,\quad D_C=P\cap C .
\]
The set \(L\) is a subgroup since the coset has order at most two. For sign \(\sigma\) let \(\Theta_\sigma(B)\) be its ordinary restricted theta, so its quotient root cap is \(\Theta_\sigma(B)/b\). Averaging the row over \(L\) gives a quotient row of root \(q(L)=(1-o(1))a|L|\). Every quotient law lifts uniformly to a feasible full row, giving the reverse upper \(\Theta_\sigma(B)/b\le a|L|\). Thus \(\Theta_\sigma(B)=(1-o(1))na\) and \(b\ge(1-o(1))na\) by total mass. Since \(na\ge(1+\delta)\sqrt n\), this exceeds the prime clique ceiling \(c_p=\lfloor(1+\sqrt{1+4n})/2\rfloor\). Therefore some nontrivial pair in \(B\) has forbidden sign. Its orthogonal phase vectors imply \(q(L)\le1/2\), and hence
\[
                 b\ge(2-o(1))na,\qquad b>2c_p
\]
eventually. The same argument works for \(C=K\) and \(C\ne K\). [Restricted theta and uniform lift](coset-majorants.md) · [Prime clique ceiling, Hanson–Petridis](https://arxiv.org/abs/1905.09134)

The bounds \(\sum_{C}(1-u_i^3)\le3\sum_C(1-u_i)=o(|K|)\) and \(\sum_{P\setminus C}u_i^3=o(S)\) imply \(S=|D_C|+o(|K|)\). Both \(S\) and \(|D_C|\) are comparable to \(|K|\), since \(S=\alpha/a\) and \(a|K|\le1+o(1)\). On \(D_C\) the sum of the unnormalized absolute differences from the constant one is \(o(|K|)\). After normalization this gives
\[
 \|\mu-{\rm Unif}(D_C)\|_{\rm TV}=o(1),\qquad
 \boxed{\quad \alpha=(1+o(1))\frac{\Theta_\sigma(B)}{t b}
                   \frac{|P\cap C|}{|K|} .\quad}                         \tag{1}
\]
Consequently the unweighted mean \(x_i/a\) on \(D_C\) tends to one uniformly over *all* primary optimizing rows \(x\), by the first variation \(x(\mu)/a\ge\eta\to1\) and the common point cap. The right-hand side of (1), including the normalization \(1/t\), is evaluable without a full optimizing row. One can upper-bound the mask fraction using the single true companion's proportion on \(C\) of exterior heights exceeding \((2d-1)\delta/8\). [Actual delayed pin](astra-persistent-88.md) · [Cubic first variation](astra-discount-91.md)

## A prime-forced odd cycle on the positional subgroup

For any such \(B\) write \(s(x)=\chi(1-x)\), \(F=\{x\in B:s(x)=-\sigma\}\), \(f=|F|\). The simple Cayley graph on \(B\) with connection set \(F=F^{-1}\) is \(f\)-regular. Every independent set has order at most \(c_p\), since each nonzero difference has the allowed quadratic sign, and multiplication by a nonsquare handles the minus sign. Thus \(b>2c_p\) makes this graph nonbipartite. If its shortest odd cycle has length \(g\ge5\), any vertex has at most two neighbors on that cycle. A chord would make a shorter odd cycle. For an exterior vertex with three or more neighbors, arrange them cyclically. No consecutive gap is one, by triangle-freeness. An odd gap exists, and since the other gaps sum to at least four, this gap and the two incident edges give an odd cycle shorter than \(g\). Counting incidences therefore gives \(g f\le2b\); one can use the size of a single connected component in place of \(b\).

For any coset of \(L\), translate a feasible full probability to make that coset \(L\) and denote its mass there by \(w\). The unit character phase vectors for positions on the odd cycle are orthogonal across edges. Each has the same component on \(L\), of norm \(\sqrt w\). After subtracting this component, the residual vectors have squared norm \(1-w\) and neighboring inner product \(-w\). The adjacency matrix of a \(g\)-cycle has least eigenvalue \(-2\cos(\pi/g)\). Summing inner products against this matrix gives the finite restricted-theta bound
\[
         \Theta_\sigma(B)/b\ \le\ c(g):=\frac{\cos(\pi/g)}{1+\cos(\pi/g)} .       \tag{2}
\]
This applies to every feasible quotient law by the lift. An actual forbidden \(j\)-clique also gives the bound \(1/j\).

If \(b\) is even and \(\sigma=+1\), a triangle is unavoidable. Otherwise a negative \(s(x)\) forces \(s(x^2)=+1\) for \(x\ne\pm1\), by the three distinct vertices \(1,x,x^2\). This also applies to \(-x\). If both signs were positive, \(s(x^2)=s(x)s(-x)=+1\) directly. Thus the whole subgroup \(B^2=\{x^2:x\in B\}\) is allowed off the identity, yielding a Paley clique of order \(b/2>c_p\).

If \(b\) is even and \(\sigma=-1\), assume there is no odd cycle of length at most five. Write \(F^j\) for the \(j\)-fold product set. Then \(F\) misses \(F^2\) and \(F^4\) since intersecting either gives a closed odd walk of length three or five. For \(y\in F^2\setminus\{\pm1\}\), both \(s(y)\) and \(s(y^2)\) equal \(-1\), hence \(s(-y)=+1\). It follows that \(|F^2|\le f+2\). Here \(f\to\infty\) since \(2f\ge b-1-\sqrt p\) by Jacobi completion and \(b\ge(2-o(1))na\). The set \(J=F^2=FF^{-1}\) is a subgroup. Indeed for \(z\in FF^{-1}\), the corresponding two translates of \(F\) in \(F^2\) overlap by at least \(2f-|F^2|>f/2\). Hence \(F\cap zF\) occupies more than half of \(F\). These overlaps for \(z,w^{-1}\in J\) imply \(zw\in J\). The inverse-symmetric set \(F\) is contained in a single coset of \(J\). If the coset is nonidentity it has quotient order two and the graph is bipartite. If it is \(J\), then \(F^2=J\) intersects \(F\), a triangle. Thus \(g\le5\) for this sign.

## Ruling out the nine-cycle at odd order

Suppose \(b\) is odd and there is no forbidden triangle. The sets \(F\) and \(F^{1/2}:=\{x\in B:x^2\in F\}\) are disjoint, by the geometric triple \(1,x,x^2\), and both have size \(f\). Away from 1, \(s(-x)=s(x)s(x^2)\) equals \(-1\) exactly on their union. Write \(c=\chi(2)\). Thus
\[
 \sigma\sum_{x\in B}s(x)=b-1-2f,\qquad \sum_{x\in B}s(-x)=b-1-4f+c.
\]
For every character \(\psi\) of \(B\), the two sums \(S_\psi=\sum_Bs(x)\psi(x)\), \(T_\psi=\sum_Bs(-x)\psi(x)\) are real by inversion. The two extensions from \(B\) to \(B\cup(-B)\) give restricted character sums \(S_\psi\pm T_\psi\). Each has modulus at most \(\sqrt p\) by averaging all extensions to the full multiplicative group and applying the complete Jacobi bound. Consequently \(|S_\psi|+|T_\psi|\le\sqrt p\). The trivial character gives
\[
 \frac fb\ \ge\ \frac{2-(2-c+\sqrt p)/b}{6}\ \ge\ d_0-o(1),\qquad
 d_0=(2-1/\sqrt2)/6>0.21548 .                                            \tag{3}
\]
Here \(\limsup\sqrt p/b\le1/\sqrt2\) from the fixed-gap size bound. In particular \(g f\le2b\) gives \(g\le9\) eventually. [Jacobi completion on subgroups](fourier.md)

If \(g=9\), then \(F^3\) is independent since a forbidden ratio yields a closed odd walk of length seven. Let \(J\) be its stabilizer, \(m=[B:J]\), and \(k\) the number of \(J\)-cosets meeting \(F\). The triple product in the quotient has trivial stabilizer. Kneser's theorem gives
\[
       (3k-2)|J|\le|F^3|\le c_p<b/2,\qquad k\ge mf/b.
\]
Thus \(6k-4<m\le k/(d_0-o(1))\). For large primes \(k\ge3\) is impossible since \(d_0>3/14\). If \(k=1\), \(J\ne B\) and odd quotient order forces the single occupied inverse-symmetric coset to be \(J\). The odd cycle then lies in a component of size at most \(b/2\), conflicting with \(9f\le2|\mathrm{component}|\) and (3). If \(k=2\), \(m=9\), and the two inverse cosets must be generators of the quotient, since otherwise the same component-size contradiction applies. [Kneser's theorem](https://arxiv.org/abs/1303.3539)

Label these cosets \(\pm1\) in \(\mathbb Z/9\) and take the character \(\psi\) with value \(e^{8\pi i/9}\) at 1 in the quotient. Put \(r=\cos(\pi/9)\), \(z=\cos(4\pi/9)\). Inversion exchanges the two cosets, so \(\sum_F\psi=-fr\). The halves lie over \(\pm5\bmod9\), giving \(\sum_{F^{1/2}}\psi=fz\). Thus
\[
 \sigma S_\psi=2fr-1,\qquad T_\psi=2f(r-z)+c-1.
\]
The two-layer Jacobi bound now requires \(\sqrt p/b\ge 2(d_0-o(1))(2r-z)-O(1/b)>0.73510\) eventually. This contradicts \(\limsup\sqrt p/b\le1/\sqrt2\). Hence \(g\le7\). At all sufficiently large primes in a trapped sequence, the right-hand side of (1) is upper-bounded by the physical occupancy times \(c(7)/t\), the sharper \(1/(3t)\) for even-plus or \(1/(\sqrt5\,t)\) for even-minus, up to \(o(1)\).

## A smaller cap on the actual restricted optimum

For the nearly optimal quotient there is a stronger numerical restriction at odd order. Let \(w=\Theta_\sigma(B)/b\), \(\tau=\sqrt p/b\), and assume there is no forbidden triangle. Along the trapped sequence \(\tau\le\sqrt2\,w+o(1)\) since \(wb=(1-o(1))na\). Let \(v\) be an optimizing probability on \(\widehat B\), with \(v_0=w\), and put \(\lambda_\psi=f^{-1}\sum_{x\in F}\psi(x)\in[-1,1]\). The forbidden zeros yield \(\sum_\psi v_\psi\lambda_\psi=0\). Some nontrivial \(\psi\) thus has \(\lambda_\psi\le-r\), \(r=w/(1-w)\). Since \(b\) is odd, it has a unique square root character \(\xi\). By inversion symmetry and the double-angle identity,
\[
 |\lambda_\xi|\le \sqrt{\mathbb E_F(\operatorname{Re}\xi)^2}
 =\sqrt{(1+\lambda_\psi)/2}\le \sqrt{(1-r)/2}.
\]
For this character the two sums above are \(\sigma S_\psi=-1-2f\lambda_\psi\) and \(T_\psi=c-1-2f(\lambda_\psi+\lambda_\xi)\); indeed \(\sum_{F^{1/2}}\psi=f\lambda_\xi\). Thus \(\tau\ge (2f/b)(2r-\sqrt{(1-r)/2})-O(1/b)\). With (3), every positive subsequential limit \(w\) in the range \(2r-\sqrt{(1-r)/2}\ge0\) satisfies
\[
 \frac{2-\sqrt2\,w}{3}\left(2\frac{w}{1-w}
             -\sqrt{\frac{1-2w}{2(1-w)}}\right)\le\sqrt2\,w .             \tag{4}
\]
After dividing by \(w\), the left side is strictly increasing on \(0<w<1/2\). Its positive term is a constant multiple of \((2-\sqrt2\,w)/(1-w)\), which increases; the subtracted term is a product of positive decreasing factors. At \(w=4627/10000\) the left side of (4) exceeds the right by more than \(10^{-6}\). A triangle gives the stronger \(w\le1/3\) directly. Thus asymptotically the right side of (1) is at most \(0.462700\,|P\cap C|/(t|K|)+o(1)\) for odd \(b\). This also gives \(\limsup \tau<2/3\), hence \(f/b>2/9\) eventually in the triangle-free case and another proof of \(g\le7\) for the nearly optimal quotient. The index-nine exclusion above only needs the subgroup size bound and the prime clique ceiling.

## Finite tests and next estimates

For all 778 sign-and-proper-divisor cases at eligible primes \(p\le3000\) with \(2c_p<b\le6\sqrt n\), the restricted objective satisfies \(\Theta_\sigma(B)\le\sqrt n\). Explicit clique witnesses prove 775 of the comparisons. Rounded opposite quotient witnesses with rational diagonal repair prove the remaining three, at \((p,b,\sigma)=(97,16,-),(157,39,-),(229,57,-)\). At \(p=97,b=16,\sigma=-\) the forbidden graph really is triangle-free and has a five-cycle. On the actual length-eight, terminal-time-eleven plus mask the subgroup \(K=\{0,16,32\}\) has empty mask intersection. Its distinct self-inverse coset \(8+K\) contains two masked sites and has mean positive companion height \(1.773508756\ldots\). The joint score in (1) there is between \(0.097630\) and \(0.097632\). This finite calculation evaluates the diagnostic without assuming asymptotic confinement. [Arb and exact-integer replay](astra-coset-93-check.py) · [Three records](astra-coset-93-checks.jsonl)

1. On remaining divisors use the actual shape of \(P\cap C\), including its complete contact on *every* optimizing row, to bound the occupancy times the restricted theta fraction in (1) at one admissible physical length. An \(o(1)\) upper removes the trapped positive-mass branch there.
2. For odd \(b\) and odd girth seven, \(F^2\) must be an independent set of size at most \(c_p\), while \(f/b\ge d_0-o(1)\). Test its small doubling and the actual Fourier coefficients of \(F\) and \(F^{1/2}\) in the two-layer compression. The short-cycle results leave smaller positive trapped masses and the ordinary all-prime theta limit open.
