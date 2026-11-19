# Prime defects for complex twists of lattice-valued order

Let \(p\equiv1\bmod4\) be prime, \(B\le Q\) an order-\(b\) subgroup of the nonzero squares, and \(d\) a character of \(B\) of exact order \(k\in\{3,4,6\}\). For fixed \(C,\epsilon>0\), uniformly over \(b\le C\sqrt p\), \(d\), and \(a\in\mathbb F_p^\times\), there is the absolute deficit bound

\[
\sqrt p-\left|\sum_{x\in B}d(x)\chi(1-ax)\right|
\gg_{C,\epsilon}(\log\log\log p)^{1/(4+\epsilon)}.                \tag{1}
\]

The bound applies to cosets inside \(Q\) and outside it. A change of representative multiplies the sum by a unit phase. The new issue compared with [the quadratic twist](twisted-coset-defect-40.md) is that the residual values are in a lattice in \(\mathbb C\). A nonzero residue of size \(O(\sqrt p)\) in this lattice can vanish at a prime over \(p\). Reflection symmetry puts the **total residue at the chosen pole** on a fixed lattice line, which precludes this.

## The peak and the lattice residual

Put \(p-1=2bm\), take a generator \(g\), and write \(\xi=e^{2\pi i/(2km)}\), \(\zeta=\xi^{2m}\), and \(d(g^{2m})=\zeta^e\) with \((e,k)=1\), \(1\le e<k\). Define \(f_j=\sum_{x\in B}d(x)\chi(1-g^j x)\). Write \(R=\mathbb Z[\zeta]\); it is a rank-two lattice in the chosen complex embedding for all three orders. Direct substitution gives

\[
f_{j+2m}=\zeta^{-e} f_j,\qquad f_{-j}=(-1)^j\overline{f_j}.
\]

The positive-exponent Fourier transform on \(\mathbb Z/(2km)\mathbb Z\) is \(kJ_t\) on \(t\equiv e\bmod k\) and zero elsewhere, where \(J_t=J(\eta_t,\chi)\) and \(\eta_t(g)=\xi^t\). On the indicated support both characters needed for the nontrivial Jacobi estimate are nontrivial. Thus \(|J_t|=\sqrt p\), and Parseval yields \(\sum_{0\le j<2m}|f_j|^2=p\).

If \(x=\sqrt p-\Delta\) is a peak with \(\Delta=o(\sqrt p)\), its coset is self-inverse in \(\mathbb F_p^\times/B\), else two entries exceed \(\sqrt{p/2}\) in magnitude. Choose its index \(a_0=0\) or \(m\) and put \(u_h=f_{a_0+2h}\) on \(\mathbb Z/(km)\mathbb Z\), \(F=f_{a_0}\), \(\omega=(-1)^{a_0}\zeta^{-e a_0/m}\). Then

\[
u_{-h}=\omega\overline{u_h},\qquad F=\omega\bar F,\qquad
\widehat u_t=\frac{k}{2}\xi^{-t a_0}\big(J_t+(-1)^{a_0}J_{t+km}\big)
\quad(t\equiv e\bmod k).
\]

The other coefficients vanish. A unit scalar rotates \(F\) to \(x>0\) and all \(\widehat u_t\) to real values because of the reflection relation. Their rotated upper bound is \(k\sqrt p\). Subtract the peak vector taking value \(F\zeta^{-e\ell}\) at \(h=\ell m\), \(0\le\ell<k\), and zero elsewhere, to obtain an \(R\)-valued residual \(r\). Its rotated Fourier coefficients are bounded above by \(k\Delta\), have sum zero, and are supported in one residue class modulo \(k\). In particular the normalized Fourier algebra norm is at most \(2\Delta\).

The two lattice coordinate functions of \(r\) in the basis \(1,\zeta\) are integer-valued with Fourier algebra norm \(O_k(\Delta)\). Indeed each coordinate is a fixed linear combination of \(r,\bar r\). Applying [Sanders's quantitative idempotent theorem](https://arxiv.org/abs/1610.07092) to the two coordinates, and then projecting back by the reflection relation, gives

\[
r(h)=\frac12\sum_{i=1}^s
\left(\lambda_i\mathbf1_{W_i}(h)+\omega\bar\lambda_i\mathbf1_{-W_i}(h)\right),
\quad
\lambda_i\in\{\pm1,\pm\zeta\},\quad
s\le \exp\big(O_{k,\epsilon}((1+\Delta)^{4+\epsilon})\big).          \tag{2}
\]

Here \(W_i\) are subgroup cosets in the even-index group and both members of each pair have the same subgroup size.

## A pole on a fixed lattice line

Reduce by \(\xi\mapsto\xi_p=g^{b/k}\), so \(\zeta\mapsto \xi_p^{2m}\). All Jacobi coefficients \(J_t\) with \(1\le t<km\) on the transform support vanish modulo \(p\), by expanding
\(\sum_{y\ne0}y^{bt/k}(1-y)^{bm}\). Every resulting power lies between \(1\) and \(p-2\). For \(j\) of parity opposite to \(a_0\), write \(Z_j=\xi_p^{a_0-j}\), so \(Z_j^{km}=-1\). Inverting the full transform and retaining only its upper half gives

\[
-km f_j=\sum_{\substack{1\le t<km\\ t\equiv e\bmod k}}\widehat u_t Z_j^t. \tag{3}
\]

The peak contributes \(2kF Z_j^e/(1-Z_j^k)\). A subgroup coset of size \(h\) represented by \(c\) gives zero if \((h,k)>1\). Otherwise \(h\mid m\), and its contribution is

\[
\frac{2h W^{\ell_0}}{1-W^k},\qquad W=(\xi_p^{2c}Z_j)^h,\qquad
1\le\ell_0<k,\quad h\ell_0\equiv e\bmod k.
\]

These are finite geometric sums using \(W^{km/h}=-1\). No denominator vanishes on the tested points. At \(Z=1\) a coset term has a pole exactly when \(W(1)^k=1\). Its residue there is \(-2W(1)^{\ell_0}/k\). The reflected coset has the inverse value of \(W(1)\), so either both terms have a pole or neither does. If they do, set \(\eta\in\langle\zeta\rangle\) to be the unique lift of \(W(1)^{\ell_0}\) to a \(k\)-th root in \(R\). Multiplying the residue of (3) by \(k\) gives the reduction of

\[
-2kF-\sum_{i\ {\rm at\ pole}}
(\lambda_i\eta_i+\omega\overline{\lambda_i\eta_i}).              \tag{4}
\]

The formula also applies after discarding any collection of whole residual pairs. This expression lies on \(L_\omega=\{v\in R:v=\omega\bar v\}\), a rank-one lattice. It contains a nonzero lattice point such as \(1+\omega\) if \(\omega\ne-1\), or \(\zeta-\bar\zeta\) otherwise. A generator \(v_\omega\) has fixed nonzero norm in the imaginary quadratic field, so it reduces to a nonzero element for sufficiently large \(p\). If \(s=o(\sqrt p)\), (4) is a nonzero integer multiple of \(v_\omega\) of magnitude \(O_k(\sqrt p+s)\), since its correction has complex modulus at most \(2s\). Its reduction modulo \(p\) is therefore nonzero.

## Repetition on one progression

Suppose (1) fails along a sequence with \(\Delta=o((\log\log\log p)^{1/(4+\epsilon)})\). The peak and \(b\le C\sqrt p\) imply \(b,m\asymp_C\sqrt p\). The mean square on the opposite parity in a \(2m\) interval is \(O_C(1+\Delta)\), by Parseval with the peak excluded. Choose a radius \(T_0\ge1\) of order \(\sqrt{1+\Delta}\) whose square is at least twice this mean square. There are at most \(M=O_k(1+T_0^2)\) elements of \(R\) in that disk.

Put \(A=16k M(s+1)\). Starting at \(D=1\), include each active index \(m/h_i\) in increasing order in the least common multiple \(D\) while it is at most \(AD\), stopping at the first failure. Thus \(D\mid m\), \(D\le A^{2^s-1}\), and unprocessed sizes are below \(m/(AD)\). Partition the opposite-parity \(j\)'s modulo \(2kD\) and choose one class with mean square no larger than the opposite-parity mean. On this class the processed terms are constant since \(m\mid D h_i\). One of the \(M\) disk values of \(f_j\) is repeated at least \(m/(2DM)\) times.

In (3) discard the constant processed terms. The remaining rational function has numerator and denominator degrees at most \(k+2ksm/(AD)\), and its residue at \(Z=1\) is nonzero by (4). In fact \(s\le (\log\log p)^{o(1)}\) or is bounded, so \(\log(16 k MD)\le \log(16 k M)+2^s\log A=(\log p)^{o(1)}\) or is bounded. Hence the repetition count exceeds the degree. The numerator after subtracting the repeated value must vanish identically over \(\mathbb F_p\), contradicting the pole. This proves (1).

## Faster rates for some quotient factorizations

Let \(m_{[k]}\) be the largest divisor of \(m\) whose prime factors divide \(k\). These two improvements also apply to the quadratic proof of [round 40](twisted-coset-defect-40.md).

- If \(m/m_{[k]}\) is one or a prime power, all the active indices \(m/h_i\) are nested by divisibility. At each inclusion \(D\) becomes at most \(A D_{\rm old}\), hence \(D\le A^s\). Under an assumed violation with \(\Delta=o((\log\log p)^{1/(4+\epsilon)})\), we have \(s\le(\log p)^{o(1)}\) or bounded. Thus \(\log(16k MD)=O((s+1)\log A)=o(\log p)\) and the same repetition contradiction proves the lower bound at this larger scale.
- If \(m_{[k]}\ge p^\delta\) for a fixed \(\delta>0\), then all the active indices are at least \(p^\delta\). In an assumed violation with \(\Delta=o((\log p)^{1/(4+\epsilon)})\), we have \(s,A=p^{o(1)}\), so \(D=1\) and the degree and pole conditions again hold. This proves the logarithmic lower bound under the stated factorization hypothesis.

The [exact modular replay](twisted-lattice-defect-41-check.py) checks transform support, conjugate reflection, half-transform vanishing, and the rational terms at both centers for all three orders at \(p=97,241\). The [six records](twisted-lattice-defect-41-checks.jsonl) also check the reflected residues in both embeddings. They check finite algebra, while the deficit is an ordinary proof.

## Scope and a route that stopped

This gives a uniform deficit for the corresponding positional entries of cross blocks of a common frequency subgroup when its annihilator has bounded square-root size. The loss after dividing by \(b\) may still tend to zero. A statement for all twist orders would require an additional argument, since the single complex embedding of \(\mathbb Z[\zeta_k]\) is not a discrete lattice for other \(k>2\). This proof does not give simultaneous positivity or a cold continuation domain.

For the order-two near-alignment hypothesis, the reciprocal shifted set \((1-B)^{-1}\) is almost monochromatic for differences. It has the useful multiplicative correlation tail of \(1-B\), by inversion. But its two square classes each carry about half the mass. Restricting to one class loses the near-unit Rayleigh quotient needed for the smooth cap. Translating by an anchor restores the sign concentration and brings back the unresolved [cross-ratio tail](parallel-crossratio-21.md). The [multiplicative irreducibility theorem for shifted subgroups](https://arxiv.org/abs/2602.20919) rules out exact ratio-set representations. The counts needed here concern approximate high correlations of an anchor translate and do not follow from that conclusion.
