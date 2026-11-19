# Fixed-order tests on the real stationary mark

Fix a physical floor interval $[a,T]$, $0<a<1$, $T=2048$, and write $L=\log(T/a)$. A field-first family of estimates on **signed scalar contractions** of the actual real stationary Hessian suffices to carry hot marked decay to $a$. Each estimate has fixed order when the field size tends to infinity. There is no required growth rate of derivative order with field size, and the bound permits derivative growth faster than that of an analytic function. Genuine ramification of the marked curve is allowed. For squares the test gives a violation within a finite order depending on the interval and the proposed bounds but independent of field size. The necessary prime arithmetic estimates remain open.

## Getting twice the scalar order from stationary jets

At a real base $x$, use $w_0=1$, $w_i=x/n$ off the mark, $W=1+(1-1/n)x$, and the mean-one positive stationary plus row $u$. In the notation of [round 38](astra-surface-38.md), $E$ is its relative tangent and $P$ is the $w$-orthogonal projection onto $E$. Write $c=Pe_0$. Locally set $z=1-x/t$ and $u(t)=u(1+h(z))$. Products are coordinatewise. The real analytic $E$-valued solution has $h(0)=0$ and obeys
$$
 h=P[h^2/(1+h)]-zc/(1+h_0).
$$
This determines each vector coefficient $h_j=[z^j]h$ from its predecessors; in particular $h_1=-c$ and $h_2=P(c^2-c_0e_0)$. For $J\ge0$ let $H_J=\sum_{j=1}^Jh_jz^j$, and form the scalar
$$
 S_J(z)=\sum_i w_i\log(1+(H_J)_i)-z\log(1+(H_J)_0).
$$
All logs near zero have value zero there. Denote $b(z)=\log(u_0(t)/u_0(x))$. Then
$$
 b(z)=-S_J'(z)-(J+1)\|h_{J+1}\|_w^2 z^{2J+1}
                +O(z^{2J+2}).                                      \tag{1}
$$
In particular $-S_J'$ gives all scalar coefficients through order $2J$ using just $J$ vector coefficients. Terms of a fixed order in $S_J$ require only finite products and signed weighted sums. There is no coordinatewise size estimate on the input jets.

Indeed write $S(z,H)$ for the same action with variable $H\in E$. Multiplying all weights at $t$ by $1-z$ changes the exceptional weight from $1$ to $1-z$ and restores every bulk weight to $x/n$. Thus $D_H S(z,h(z))=0$ on $E$. Differentiating $S(z,h(z))$ leaves just its explicit parameter derivative $-b(z)$. Its Hessian in $H$ at $(0,0)$ is minus the weighted inner product on $E$. Taylor expansion at $h(z)$, where the linear term vanishes, gives
$$
 S(z,h(z))-S_J(z)=\tfrac12\|h_{J+1}\|_w^2 z^{2J+2}+O(z^{2J+3}).
$$
The expansion on the real line suffices, and differentiation of these analytic germs proves (1). The norm here is the norm of the real coefficient, without complex conjugation of the formal parameter.

For example, with $M_r=\sum_i w_i c_i^r$, the first three coefficients of $b$ are
$$
 -c_0,\qquad M_3-\tfrac32c_0^2,\qquad
 \langle c^2,(I-2P)c^2\rangle_w+4c_0 M_3-\tfrac{10}3c_0^3.        \tag{2}
$$
For the cubic, (1) gives $M_4-4c_0^3/3-2\|P(c^2-c_0e_0)\|_w^2$. Expanding that square and using $\|c\|_w^2=c_0$ gives (2). In particular a large fourth moment can cancel against the projected energy in this actual marked jet.

The physically scaled mark $m(t)=\log(\sqrt{W_t/n}\,u_0(t))$ has increment
$$
 m(t)-m(x)=b(z)+\tfrac12\big[\log(1-z/W)-\log(1-z)\big].            \tag{3}
$$
Use the single global real parameter $s=\log(T/t)$, $0\le s\le L$, and put $f(s)=m(Te^{-s})$. At a center with floor $x$, substitute $z=1-e^v$ in (3), where $v$ is the increment in $s$. Multiplying the resulting coefficient $[v^j]$ by $j!$ gives $f^{(j)}(s)$. Formulas (1)–(3) express this number as a signed scalar calculation on real stationary rows at that floor. For order $j$ one may use $J=\lceil j/2\rceil$ and omit the remainder and norm term in (1).

## A finite real propagation inequality

Let $D_0,\ldots,D_N>0$ have nondecreasing ratios $r_j=D_j/D_{j-1}$. Suppose $|f^{(j)}(s)|\le D_j$ on the interval for $0\le j\le N$. Let
$$
 B(s)=\max_{0\le j\le N}\frac{|f^{(j)}(s)|}{e^jD_j}.
$$
For integers $0\le k<K\le N$,
$$
 B(0)\le e^{-K},\qquad \sum_{j=k+1}^K\frac1{r_j}>eL
 \quad\Longrightarrow\quad \sup_{[0,L]}|f|\le D_0e^{-k}.            \tag{4}
$$
This is the finite derivative-level argument of Bang. For context see [Nazarov, Sodin and Volberg](https://arxiv.org/abs/math/0208233). Here is a direct proof. Between levels $e^{-j}<B<e^{-(j-1)}$, every maximizing derivative has index $i<j$ since the terms at larger indices are at most $e^{-j}$. Its absolute slope is bounded by $e r_{i+1} B\le e r_jB$. The maximum of these finitely many locally Lipschitz functions therefore has $|(\log B)'|\le er_j$ almost everywhere in this open range. This uses no derivative of order $N+1$, since $i<j\le N$. To reach the higher level from the lower one takes length at least $1/(er_j)$, by limits from their interiors. Choose the last crossing of the lower level before the first crossing of the upper level. The successive level ranges have disjoint crossing intervals. Crossing from $e^{-K}$ to $e^{-k}$ would take more than $L$. The $i=0$ entry of $B$ gives (4).

For the actual mark and sufficiently large $n$, the entire disk $|s|\le1/2$ is within the [hot theorem's](parallel-complex-structure-35.md) domain under $t=Te^{-s}$ since $Te^{-1/2}>1024$, $Te^{1/2}<n$ and $|\arg t|\le1/2$. Hence
$$
 |f^{(j)}(0)|\le 4n^{-1/2}\,2^j j!                                  \tag{5}
$$
for every $j$. If $D_j\ge2^j j!$, we may take $K=\min(N,\lfloor\log(\sqrt n/4)\rfloor)$ whenever it is positive. For example, take $D_0\ge1$ and $r_j=A j\log(ej)$ for $A\ge2$. If the real bounds through $N$ hold, then for any $0<\beta<\exp(-eAL)$ and large $K$,
$$
 \sup|f|\le D_0\exp[-\lfloor K^\beta\rfloor].
$$
Indeed the tail sum from $\lfloor K^\beta\rfloor+1$ to $K$ tends to $A^{-1}\log(1/\beta)$. This example permits the Taylor-coefficient majorants $D_j/j!$ to have unbounded $j$-th root.

In particular assume some fixed infinite positive sequence $D_j$ as above satisfies $\sum_{j\ge1}1/r_j=\infty$, $D_j\ge2^j j!$, and for **each fixed** $j$,
$$
 \limsup_{p\to\infty}\sup_{0\le s\le L}|f_p^{(j)}(s)|\le D_j.       \tag{6}
$$
Then $\sup|f_p|\to0$. For given $k$ choose a finite $K$ with the strict sum in (4). For all sufficiently large primes the derivative bounds up to $K$ hold with $2D_j$ in place of $D_j$, simultaneously, and (5) supplies the hot endpoint condition. The ratios do not change. Let $k\to\infty$ after the prime limit. Applying this through a sequence $a\downarrow0$ gives the ordinary theta target by the [stationary bracket](complex-floor-33.md). Monodromy-free complex tubes, individual complex Hessian null estimates, and a specified field-dependent depth are unnecessary for this implication. Its arithmetic hypothesis concerns stationary coefficients and is unproved.

An integrated version can discard narrow peaks of a derivative. If for each fixed $j\ge0$ one has
$$
 \limsup_{p\to\infty}\int_0^L |f_p^{(j+1)}(s)|\,ds\le D_j,
$$
the fundamental theorem of calculus and (5) give (6) with the same $D_j$. The absolute value is taken **after** summing the signed spatial terms in (1)–(3).

## A fixed finite obstruction on actual squares

Let $d_a=\tfrac14\log(2/(1+a))>0$. The exact [square theta values and stationary bracket](complex-floor-33.md) give $f_{q}(L)>d_a$ for all sufficiently large squares. For any proposed envelope as in (6), choose $k$ with $D_0e^{-k}<d_a$, then any finite $K>k$ with $\sum_{j=k+1}^K1/r_j>eL$. For every sufficiently large square, at least one actual derivative of order at most $K$ exceeds its prescribed $D_j$ somewhere on this fixed real floor interval. This follows from (4)–(5). If desired one can take $D_0$ large enough to rule out the zeroth derivative, since the real leverage estimate $|f'|\le1/2$ and (5) give $|f|\le L/2+4/\sqrt n$.

There is also a finite integrated obstruction. For the same $k,K$, if $\int_0^L|f^{(j+1)}|\le D_j/2$ held for every $0\le j\le K$, (5) would give $\sup|f^{(j)}|\le D_j$ for all those fixed orders on all sufficiently large squares. Thus at least one of those integrated scalar contractions exceeds $D_j/2$ on every sufficiently large square. Both witnesses have field-independent order bounds, even if the offending order varies. The full-row jet obstruction in round 38 used an order bound growing with $n$. This result concerns the actual *marked scalar*, with a different envelope and potentially very large $K$.

In fact the obstructing order can be forced **above any prescribed index**. Given $j_0\ge1$, choose a constant $C\ge2$ so large that
$$
  1+2D_{j_0}L^{j_0-i}/(j_0-i)!\le C D_i\qquad(0\le i<j_0).
$$
Choose $k$ with $C D_0 e^{-k}<d_a$, and $K\ge j_0$, $K>k$, with the same strict divergent-tail condition. Suppose a sufficiently large square has $\int_0^L |f^{(j+1)}|\le D_j$ for $j_0\le j\le K$. Then (5) gives $\sup|f^{(j)}|\le2D_j$ over that block. For $i<j_0$ integrate the $j_0$-th derivative down from the hot endpoint. Its Taylor polynomial contribution from orders below $j_0$ has sup norm below one for all sufficiently large squares by (5), so the choice of $C$ gives $\sup|f^{(i)}|\le C D_i$. Applying (4) to $C D_j$ contradicts the cold mark. The very same reasoning works when the block assumption is directly $\sup|f^{(j)}|\le D_j$. Thus every large square violates each type of test at some order in $[j_0,K]$, with possibly different indices for the two types.

For instance set $U_j=j!\prod_{\ell=1}^j\log(e\ell)$. Taking $D_j=A^j U_j$ for arbitrary $A\ge2$ and taking disjoint finite blocks, pigeonholing inside each block gives the unconditional quantitative conclusion
$$
 \limsup_{j\to\infty}\left(
  \frac{\limsup_{q\to\infty,\ q\ {\rm square}}\sup_{s}|f_q^{(j)}(s)|}{U_j}
  \right)^{1/j}=\infty.                                          \tag{7}
$$
The identical conclusion holds replacing the supremum of the $j$-th derivative by the integral of the absolute $(j+1)$-st derivative. The field limit is taken first in each order. This requires actual marked irregularity at arbitrarily high fixed orders and is compatible with every individual order having a finite field limsup.

These statements concern the real physical curve at true stationary rows. The public [Jig #7](https://jig.so/p/7) criterion using complex phase exceptions and the [prime examples of marked monodromy](astra-cold-37.md) address different quantities. No prime-uniform estimate in (6), asymptotic bound on the number of prime branch points, or resolution of ETH Problem 26 follows here.

The [exact checker](astra-complex-39-check.py) independently generates the true prime-13 germ from its cubic at $x=30/19$. It verifies (1) with $J=0,\ldots,6$, including the first nonzero defect at order $2J+1$, and checks the three signed formulas (2). Run `.venv/bin/python -B research/astra-complex-39-check.py` from the repository root to reproduce the [two records](astra-complex-39-checks.jsonl).
