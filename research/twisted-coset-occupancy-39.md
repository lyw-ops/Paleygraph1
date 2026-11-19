# An exact cell count for the twisted critical coset

Consider the alternating critical-coset obstruction to signed repair
discussed in [round 21](parallel-crossratio-21.md). A near-unit twisted
rectangle forces an almost two-to-one map on half of the actual
field, with a prescribed parity on each two-point fiber. This is a
counting constraint on \(x\mapsto(x^b,(x-1)^b)\), where \(b\) is
the subgroup size. The identity below yields a direct prime gap
if a positive fraction of its opposite-sign fibers have odd size.
That prime counting estimate remains open.

## The signed second moment

Let \(q\equiv1\bmod 4\) be an odd field order, \(\chi\) its quadratic
character, and \(B\) an even subgroup of the nonzero squares of
order \(b\), with nontrivial quadratic character \(d\). Set

$$
S=\sum_{r\in B} d(r)\chi(r-1).
$$

For multiplicative \(B\)-cosets \(C,D\) in the full field units let
\(F_{C,D}=\{x:x\in C,\ x-1\in D\}\). Call a cell opposite if
\(\chi(C)\chi(D)=-1\), where \(\chi\) is constant on each coset.
Fix representatives \(c\in C\), \(d_0\in D\) to give each point in
the cell its internal sign
\(\epsilon_x=d(x/c)d((x-1)/d_0)\). Replacing the representatives
only flips all signs in a cell. Define \(R_{C,D}=\sum_{x\in F_{C,D}}\epsilon_x\).
Then

$$
\boxed{\qquad
\sum_{C,D\ {\rm opposite}} R_{C,D}^2 =\frac{q-S^2}{2}.
\qquad}                                                     \tag{1}
$$

The diagonal terms of the squared sum count the
\((q-1)/2\) points with \(\chi(x(x-1))=-1\). Here
\(\sum_x\chi(x(x-1))=-1\) by the nondegenerate quadratic sum.
For distinct points \(x,y\) in the same cell set
\(r=x/y\) and \(s=(x-1)/(y-1)\). The map is a bijection between the
ordered pairs in these cells, before the opposite restriction, and
\(r,s\in B\setminus\{1\}\) with \(r\ne s\). Its inverse is

$$
y=\frac{1-s}{r-s},\qquad x=ry.
$$

In particular \(y-1=(1-r)/(r-s)\), so the cell is opposite exactly
when \(\chi(r-1)\chi(s-1)=-1\). Also
\(\epsilon_x\epsilon_y=d(r)d(s)\). The off-diagonal sum thus equals

$$
\frac12\sum_{r,s\in B\setminus\{1\}}
d(r)d(s)(1-\chi(r-1)\chi(s-1))
=\frac{1-S^2}{2}.
$$

The terms \(r=s\) vanish. We used \(\sum_{r\ne1}d(r)=-1\).
This proves (1). The same enumeration with the plus indicator and
the omitted off-diagonal terms restored gives

$$
\sum_{C,D\ {\rm same}}R_{C,D}^2=\frac{q+S^2}{2}-b.
$$

The combination of the two formulas gives the independent total
\(q-b\).

## A necessary fiber profile at the critical size

Let \(O\) be the number of opposite cells of odd cardinality.
Each has \(|R_{C,D}|\ge1\), so

$$
|S|\le\sqrt{q-2O}.                                           \tag{2}
$$

No sign-alignment hypothesis is needed for (2).
In particular a bound \(O\ge c p\), with a fixed \(c>0\) through
the prime fields and the eligible \(b\sim\sqrt p\), would give a
fixed gap for the twisted single-coset rectangle on primes. It
would require no strong \(3/2\) moment of the cross-ratio
distribution.

There is also a point-counting conclusion. Choose \(\sigma\) to make
\(\sigma S=|S|\), and write
\(e=(b-1-|S|)/2\), the number of \(r\ne1\) where
\(\chi(r-1)\ne \sigma d(r)\).
Let \(U\) be the number of points in opposite cells whose internal
sign populations are different from \((1,1)\). Then

$$
U\le\frac{q-S^2}{2}+2be.                                     \tag{3}
$$

For a cell with populations \(N_+,N_-\), let
\(A=N_+(N_+-1)+N_-(N_--1)\), the number of same-sign ordered pairs.
Its population, if nonzero and not \((1,1)\), is at most
\(R^2+2A\). For population one or two this follows by inspection.
For \(N=N_++N_-\ge3\), use \(2A=N^2+R^2-2N\ge N\).
In an opposite cell all same-sign off-diagonal pairs correspond to
\(r,s\) having the same \(d\) but opposite \(\chi(r-1),\chi(s-1)\).
For each \(d\) class of size \(b/2\) or \(b/2-1\), if \(e_d\)
elements mismatch \(\sigma d\), its contribution is
\(2e_d(\#\text{class}-e_d)\). Thus \(\sum A\le b e\).
Equation (1) gives the other term in (3).

Suppose \(b/\sqrt q\to1\) and \(|S|/b\to1\).
Then \(e=o(b)\), \(O=o(q)\), and \(U=o(q)\). In particular
all but \(o(q)\) of the \((q-1)/2\) opposite points have exactly
one other point in their fiber, with the opposite internal sign.
In fact the two-point conclusion holds off the \((+,+)\) cells.
The map \(x\mapsto1/x\) bijects the \((-,-)\) cells with
\((-,+)\) cells, sending \((C,D)\) to \((C^{-1},D/C)\) because
\(-1\in B\). The other two classes were already opposite.
Thus \(3(q-1)/4-o(q)\) field elements lie in two-point fibers.

One can also identify the two separate parity changes, apart
from \(O(be)\) ordered collisions across all cells. For the pair
ratios \(r,s\) above, testing the near-twisted relation at \(r,s\)
gives \(d(r)d(s)=\chi(C)\chi(D)\) unless one lies in the exception
set. Applying the same test to the inverted pair uses ratios
\((r^{-1},s/r)\) and gives \(d(s)=\chi(D)\). Inversion permutes the
ordered collisions, so the excluded pairs cost at most \(4be\)
in total. The resulting parity law is

$$
d(x/y)=\chi(C),\qquad d((x-1)/(y-1))=\chi(D).
$$

In particular, if the map is refined by replacing \(B\) by its
index-two subgroup, almost all of these two-point fibers separate
into singletons. In the \((+,+)\) class almost all ordered
collisions instead survive this refinement.

The count identifies a particular prime obstruction to prove.
Small individual Möbius intersections alone give no lower bound
for \(O\) or \(U\), since they allow all these fibers to have size two.
Nor do the first two unsigned cell moments force any odd cell on
that scale.

## Square control and exact checks

For \(q=r^2\) and the norm-one subgroup of order \(r+1\), use
the exact twisted identity from [round 21](parallel-crossratio-21.md).
Here \(|S|=r=\sqrt q\), and (1) and (3) give \(O=U=0\).
Equivalently, the two norm coordinates of \(x\) and \(x-1\)
determine the trace and norm of \(x\), so any fiber contains at
most a conjugate pair. This is an actual square example,
compatible with all the field-uniform identities above.

The [integer replay](twisted-coset-occupancy-39-check.py) enumerates
cells using cyclic coordinates. It checks (1)–(3) and the total
moment at the selected critical prime subgroups and square
norm-one subgroups. The [records](twisted-coset-occupancy-39-checks.jsonl)
are exact finite counts. Positive odd-cell fractions in the prime
tests give no all-prime lower bound. This calculation only addresses
the alternating single-coset obstruction. The actual unstructured
repair and ETH26 remain open.
