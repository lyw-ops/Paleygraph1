# A diverging prime defect for the order-two twisted coset

Round 40. Let \(p\equiv1\bmod 4\) be prime, \(Q\) its nonzero
squares, \(B\le Q\) of even order \(b\), and \(d\) the nontrivial
quadratic character of \(B\). For \(aB\) in the full multiplicative
group set

$$
F_d(aB;a)=\sum_{x\in B}d(x)\chi(1-ax).
$$

Changing representative can flip its sign. For any fixed \(C>0\)
and \(\epsilon>0\), uniformly over \(b\le C\sqrt p\) and the cosets,

$$
\boxed{\quad
\sqrt p-|F_d(aB;a)|\gg_{C,\epsilon}
(\log\log\log p)^{1/(4+\epsilon)}.
\quad}                                                        \tag{1}
$$

Thus a bounded absolute deficit in the alternating critical-coset
case is excluded over primes. The proof extends the
[untwisted bounded-defect argument](coset-defects.md) using the
cyclic expansion in which the weight \(d\) becomes antiperiodic.
This reaches the order \(1/\sqrt p\) gap scale in the prescribed
signed cross block. The relative gap needed for every near-unit
alternating rectangle remains open.

## Fourier expansion and the location of an extreme value

Put \(p-1=2bm\), choose a primitive \(g\in\mathbb F_p^\times\), and
set \(f_j=\sum_{x\in B}d(x)\chi(1-g^j x)\) on
\(\mathbb Z/(4m)\mathbb Z\). Since \(d(g^{2m})=-1\), we have

$$
f_{j+2m}=-f_j,\qquad f_{-j}=(-1)^j f_j .
$$

For the second identity invert \(x\) and use \(B\le Q\) and
\(\chi(-1)=1\). Let \(\xi=e^{2\pi i/(4m)}\), and \(J_t\) denote
the Jacobi sum \(J(\eta_t,\chi)\), with \(\eta_t(g)=\xi^t\).
The unnormalized transform of \(f\) at \(t\) is \(2J_t\) for odd
\(t\) and zero for even \(t\). In fact for odd \(t\),
\(\eta_t|_B=d\) and the sum over one half period, with multiplier
\(\xi^{tj}\), is \(J_t\). Both \(\eta_t\) and \(\eta_t\chi\) are
nontrivial for odd \(t\), so \(|J_t|=\sqrt p\) and
\(J_{t+2m}=\overline{J_t}\). Parseval gives

$$
\sum_{j=0}^{2m-1} f_j^2=p.                                    \tag{2}
$$

In a putative counterexample to (1), an entry of magnitude
\(x=\sqrt p-\Delta\), with \(\Delta=o(\sqrt p)\), occurs in a
self-inverse coset modulo \(2m\). Otherwise (2) would count two
entries of that magnitude. Its index \(a_0\) can be taken to be \(0\)
or \(m\). In the latter case \(f_{-m}=-f_m\) implies \(m\) is odd.
Set \(\sigma=\operatorname{sgn}f_{a_0}\) and \(u_h=\sigma f_{a_0+2h}\)
on \(\mathbb Z/(2m)\mathbb Z\). Then \(u\) is even, satisfies
\(u_{h+m}=-u_h\), and has \(u_0=x\). With the positive-exponent
Fourier convention,

$$
\widehat u_t=\sigma\xi^{-t a_0}
   \big(J_t+(-1)^{a_0}J_{t+2m}\big)\quad(t\text{ odd}).
$$

All even coefficients vanish. The odd coefficients are real and
bounded above by \(2\sqrt p\). Subtract the peak
\(x(\mathbf1_{\{0\}}-\mathbf1_{\{m\}})\) to get a residual \(r\).
Its odd coefficients are real, bounded above by \(2\Delta\), and
sum to zero because \(r(0)=0\). Consequently its probability
normalized Fourier algebra norm is at most \(2\Delta\).
[Sanders's quantitative idempotent theorem](https://arxiv.org/abs/1610.07092)
writes this integer-valued residual as

$$
r=\sum_{i=1}^s\varepsilon_i\mathbf1_{W_i},\qquad
\varepsilon_i=\pm1,\qquad
s\le \exp(O_\epsilon((1+\Delta)^{4+\epsilon})),
$$

with \(W_i\) cosets in \(\mathbb Z/(2m)\mathbb Z\). The trivial
residual is included with \(s=0\).

## The modular pole on the opposite parity

Now work in \(\mathbb F_p\) with \(\xi_p=g^{b/2}\) of order \(4m\).
Integer-vector transforms reduce by replacing \(\xi\) with \(\xi_p\).
For lower-half odd \(t\), \(1\le t<2m\), the modular Jacobi sum is

$$
J_t=\sum_{y\in\mathbb F_p^\times}
    y^{(b/2)t}(1-y)^{bm}=0.
$$

Indeed all powers after expansion lie strictly between \(0\) and
\(p-1\). The vanished half here consists of odd frequencies that
extend \(d\). If \(j\) has parity opposite to \(a_0\), full Fourier
inversion and the formula for \(\widehat u_t\) give

$$
-2m\,\sigma f_j=
\sum_{\substack{1\le t<2m\\t\ {\rm odd}}}
\widehat u_t Z_j^t,\qquad Z_j=\xi_p^{a_0-j}.                     \tag{3}
$$

In particular \(Z_j^{2m}=-1\). The peak contributes
\(4x Z_j/(1-Z_j^2)\) in (3). A subgroup coset of size \(h\)
with representative \(c\) contributes nothing on the right
when \(h\) is even. When \(h\) is odd, \(h\mid m\), and its
contribution is

$$
\frac{2h w_j}{1-w_j^2},\qquad
w_j=(\xi_p^{2c} Z_j)^h.
$$

This is the finite geometric series over odd multiples of \(h\),
since \(w_j^{2m/h}=-1\). Every denominator is nonzero at the
tested points. The rational function of \(Z\) for the peak has
residue \(-2x\) at \(Z=1\), while a coset term has either no pole
there or residue of magnitude one, namely
\(-(\xi_p^{2c})^h\in\{\pm1\}\).

For the quantitative step, suppose that
\(\Delta=o((\log\log\log p)^{1/(4+\epsilon)})\) along a violating
sequence. Since \(x\le b-1\) and \(b\le C\sqrt p\), we have
\(b,m\asymp_C\sqrt p\). By (2), the mean square of \(f_j\) on
the parity opposite to \(a_0\) is \(O_C(1+\Delta)\). Indeed that
parity, in one half period, excludes the peak and has \(m\) entries.

Choose an integer \(T_0\ge1\) of size \(O_C(\sqrt{1+\Delta})\)
with \(T_0^2\) at least twice this mean square. Put \(M=2T_0+1\)
and \(A=16 M(s+1)\). Retain only odd subgroup sizes \(h_i\).
Starting with \(D=1\), process the indices \(m/h_i\) in
increasing order. Include the next index in the least common
multiple \(D\) while it is at most \(AD\), and stop upon first
failure. Then \(D\mid m\), \(D\le A^{2^s-1}\), and every
unprocessed subgroup size is below \(m/(AD)\).

Select a residue class of the opposite-parity \(j\)'s modulo
\(4D\) with mean square no larger than the full opposite-parity
mean square. It has \(m/D\) elements modulo \(4m\).
All processed terms are constant there because \(D\) is
divisible by \(m/h_i\). At least half of the selected \(f_j\)'s
have \(|f_j|\le T_0\), so one integer value occurs on at least
\(m/(2DM)\) points. After absorbing the processed terms, the
remaining rational function in (3) has numerator and denominator
degree at most \(2+2sm/(AD)\), and its residue at \(1\) differs
from \(-2x\) by at most \(s\) as an integer modulo \(p\).

Here \(s=(\log\log p)^{o(1)}\) or smaller. It follows that
\(\log(16MD)\le\log(16M)+2^s\log A=(\log p)^{o(1)}\) or is
bounded. In particular \(m>16MD\) and \(2x>s\) for all large
members. Also \(2x+s<p\). The residue is nonzero, while the
repetition count exceeds the numerator degree after subtracting
the repeated value. This would force the rational function to be
constant, a contradiction. This proves (1).

## Signed cross blocks at the critical rate

Let \(G=B^\perp\le\widehat Q\) and let \(A_1,A_2\) be two cosets
of \(G\) whose difference restricts to the order-two character
\(d\) on \(B\). The off-diagonal block \(K_{A_2,A_1}\) is
diagonal between its positional-coset bases, with entries
\(b^{-1}\sum_{x\in aB}\chi(1-x)\gamma(x)\), where \(\gamma|_B=d\).
The phase \(\gamma(a)\) is harmless. It follows from (1) that
for \(b=\sqrt p+o((\log\log\log p)^{1/(4+\epsilon)})\), this
signed cross block has norm at most

$$
1-\Omega_\epsilon\!\left(
        p^{-1/2}(\log\log\log p)^{1/(4+\epsilon)}\right).
$$

In particular it cannot saturate at deficit \(O(p^{-1/2})\)
in this size window. This is stronger at that rate than excluding
exact saturation. A relative deficit bounded away from zero, a
gap for absolute-value entries, and the needed control of the true
multi-step repair in its short arithmetic window are separate
questions. The square norm-one torus realizes zero absolute
deficit by the exact calculation in
[the fiber note](twisted-coset-occupancy-39.md). For a prime
subgroup in the range of (1), that note's exact opposite-cell
second moment at \(a=1\) now has the lower bound
\(\Omega_{C,\epsilon}(\sqrt p\,L(p))\), where
\(L(p)=(\log\log\log p)^{1/(4+\epsilon)}\).
This lower bound on the weighted moment does not establish an
order-\(p\) count of odd cells.

The [integer replay](twisted-coset-defect-40-check.py) verifies
\((2)\), the modular vanishing and inversion in (3), and the
single-coset rational identities, including a nonsquare center
when \(m\) is odd. Its records check finite algebra and do not
certify a numerical asymptotic constant in (1).

## Excluding highly overlapping flat alternating transfers

Let \(m_0=n/\sqrt p\), where \(n=(p-1)/2\), and fix
\(\gamma>0\), \(\epsilon>0\). Put
\(L(p)=(\log\log\log p)^{1/(4+\epsilon)}\).
There is no sequence of prime rectangles \(A,C\subset\widehat Q\)
satisfying all three conditions

$$
|A|,|C|=m_0+o(L(p)),\qquad
\frac{\mathbf1_C^\mathsf{T}\sigma K\mathbf1_A}
     {\sqrt{|A||C|}}\ge1-o(L(p)/m_0),\qquad
E(A,C)\ge(1/2+\gamma)m_0^3,
$$

where \(\sigma\in\{\pm1\}\) can vary and
\(E(A,C)=\sum_t|A\cap(C+t)|^2\).
The same exclusion holds if the signed entries in the second
condition are replaced by their positive parts. It reaches the
near-unit transfer rate \(1-O(p^{-1/2})\) on highly overlapping
flat rectangles. The low-energy regime remains open.

Write \(u_X=\mathbf1_X/\sqrt{|X|}\) for nonempty \(X\).
Let \(\delta\) be the sum of the two relative size errors, \(1/m_0\),
and a nonnegative upper bound on the gain loss. Thus
\(\delta=o(L(p)/m_0)\). The same pair with both sets translated,
and with their order exchanged if desired, is denoted \((B',D')\).
For \((A,C)\) and \((B',D')\), the nonconstant involution bound
\(\|K\|_{2\to2}\le1\) gives

$$
\|\sigma Ku_A-u_C\|_2+\|\sigma Ku_C-u_A\|_2
+\|\sigma Ku_{B'}-u_{D'}\|_2
+\|\sigma Ku_{D'}-u_{B'}\|_2=O(\sqrt\delta).
$$

In particular the normalized overlaps of the source and
receiver sets differ by \(O(\sqrt\delta)\), since \(K^2=I-J\)
and the constant-mode pairings of these indicators are
\(O(1/m_0)\). More precision is possible at a large overlap.
Set \(r=|A\cap B'|/m_0\), \(w=|C\setminus D'|/m_0\).
The total shortfall of \(\sigma m_0 K_{ij}\) from one on
\(C\times A\) is \(O(\delta m_0^2)\), by normalization of the
gain. Sum \(\sigma m_0 K_{ij}\) on
\((C\setminus D')\times B'\). The columns in \(A\cap B'\)
contribute their count minus at most this total shortfall.
Each of the remaining entries is at least \(-1\).
The upper bound follows by testing \(\sigma Ku_{B'}\) on the
indicator of the receiver difference, on which \(u_{D'}=0\).
Dividing by \(m_0^2\) yields

$$
w(2r-|B'|/m_0)\le O(\delta)+O(\sqrt{\delta w}).
$$

For \(r>c>1/2\) fixed this implies \(w=O_c(\delta)\).
The receiver overlap is then \(1+O_c(\delta)\) after
normalization by \(m_0\). Apply the same argument with the
directions reversed. Both symmetric differences are
\(O_c(\delta m_0)\).

Choose \(1/2<c<1/2+\gamma\), with \(c<1\). The set \(H\)
of shifts \(t\) with \(|A\cap(A+t)|>c m_0\) is also the
corresponding set for \(C\), by the large-overlap bound.
Both translated symmetric differences on \(H\) are
\(O_c(\delta m_0)\). The triangle inequality for these
differences makes \(H\) an exact subgroup for sufficiently
large orders. Furthermore the source and receiver
auto-overlaps differ by \(O(\sqrt\delta\,m_0)\) uniformly in
the shifts. The identity expressing cross energy as the
scalar product of the two auto-overlap counts thus gives
\(E(A,A)=E(A,C)+O(\sqrt\delta\,m_0^3)\). Summing the squared
auto-overlaps on \(H\) and off it shows
\(E(A,A)/m_0^3\le c+(1-c)|H|/m_0+o(1)\).
So \(|H|\gg_\gamma m_0\).

Average the symmetric differences over \(H\), separately for
the two sets. Rounding the density on each \(H\)-coset to its
nearest element of \(\{0,1\}\) changes
\(O_c(\delta m_0)\) entries in each set. This follows from the
averaged discrepancy \(2\sum_V |H|\rho_V(1-\rho_V)\) for
coset densities \(\rho_V\).
Denote the two unions by \(A_*,C_*\).
The cross energy also implies some shift \(t\) with
\(|A\cap(C+t)|>c m_0\). Apply the same large-overlap bound
with the two orders exchanged after this shift.
Both rounded relations \(A_*=C_*+t\) and \(C_*=A_*+t\)
are exact, since the rounding errors are \(o(|H|)\).
In addition \(2t\in H\), because an exact period of \(A_*\)
gives an \(o(m_0)\) symmetric difference for \(A\).

Put \(B_*=H^\perp\), \(b_*=|B_*|\), and write each rounded
set as a union of \(r_*=O_\gamma(1)\) cosets, of total size
\(m_0+O(\delta m_0)\). The normalized signed gain is a sum
of \(r_*^2\) twisted positional sums, each divided by
\(r_*b_*\). Each absolute positional sum is at most \(\sqrt p\)
by averaging the Jacobi bound over \(H\). For the \(r_*\)
pairs of cosets matched by the translation \(t\), the
restriction of the displacement to \(B_*\) is trivial or
has order two. In the trivial case the
[untwisted prime defect bound](coset-defects.md) applies.
In the order-two case apply (1), with \(b_*=O_\gamma(\sqrt p)\).
The rounded gain is therefore at most

$$
\frac{r_*\sqrt p-\Omega_{\gamma,\epsilon}(L(p))}{b_*}
\le 1-\Omega_{\gamma,\epsilon}(L(p)/m_0)+O_\gamma(\delta).
$$

Changing the \(O_\gamma(\delta m_0)\) entries in the source
and receiver alters the normalized gain by \(O_\gamma(\delta)\)
using \(|K_{ij}|\le1/m_0\) and the size normalization.
This contradicts the stated near-unit gain. Finally, if the
positive-part entries have near-unit gain, then the shortfall
of \((\sigma m_0 K_{ij})_+\) from one averages \(O(\delta)\).
The inequality \(1-x\le2(1-x_+)\) on \([-1,1]\) transfers that
bound to the signed entries.

Two additional exact replay records compare the direct Fourier
rectangle sum with its four positional sums in a translation that
matches two cosets per side. The identity is checked at a primitive
\(n\)-th root in \(\mathbb F_p\) at \(p=61,101\).
