# Fixed projective relations between affine collision labels

Use the actual weighted affine lines and right action of [Round 174](ordinary-affine-difference-pins-174.md), with both square masks and the endpoint exclusions. Let \(0\le g\le1\), \(G=\sum g\), and \(G=O(\sqrt p)\) as in that round. For a fixed projective map \(T\in\mathrm{PGL}_2(\mathbb F_p)\), restrict one nonnegative right correlation to the condition that one of \(Y,D,Y',D'\) is the image under \(T\) of another, distinct role. Only finite labels at which the relation is defined are retained. The squared sum of this subcorrelation over all right differences is \(O(G^4)\), with an absolute constant uniform in \(T\).

Write \(h=(a,c)\) and
\[
 Y'=\frac{aY}{1-cY},\qquad
 D'=\frac{(a-Y')D+Y'-aY}{(a-1)D+1-aY}.
\]
For each retained \(Y,h\), the transformation in \(D\) is injective on its retained domain. It is induced by the composition of the three nonsingular fractional-linear maps \(D\mapsto r\mapsto ar\mapsto (Y'-ar)/(1-ar)\). In particular a projective relation between \(Y\) and \(D'\), or between \(Y'\) and \(D\), fixes at most one \(D\) for each \(Y\). Its restricted correlation is at most \(G\) at fixed \(h\). An intraline relation between \(Y,D\), or between \(Y',D'\), has the same bound using its own physical chart and the fact that the other line's weight is at most one.

For \(Y'=T(Y)\), the maps \(Y\mapsto aY/(1-cY)\) are pairwise distinct as projective maps. At most one \(h\) has equality identically. At all other \(h\), the degree-two equation for \(Y\) has at most two solutions and the pointwise correlation is at most \(2G\). The exceptional \(h\) has correlation at most \(G^2\).

For \(D'=T(D)\), the equation fixes at most two \(D\) for each \(Y\), except when the entire transformation in \(D\) equals \(T\). For \(h\ne(1,0)\) this identity can occur at at most two \(Y\):

- If \(a\ne1,c\ne0\), normalize the lower-left entry of the Möbius matrix to one. Its upper-right entry is \((Y'-aY)/(a-1)=acY^2/((a-1)(1-cY))\). Equality to the corresponding entry of \(T\) has degree at most two and is nonidentical. If \(T\) has zero lower-left entry, identity is impossible.
- If \(a\ne1,c=0\), use the same normalization. The lower-right entry \((1-aY)/(a-1)\) determines \(Y\).
- If \(a=1,c\ne0\), the map in \(D\) is affine with intercept \(cY^2/((1-cY)(1-Y))\). Equality to any fixed intercept is a nonidentical equation of degree at most two, as the denominator has constant term one and \(c\ne0\). A nonaffine \(T\) cannot equal this map.

The nonexceptional \(Y\) therefore cost at most \(2G\) together, and the exceptional \(Y\) at most another \(2G\), at each nonidentity \(h\). The identity itself contributes at most \(G^4\) to squared energy. The reversed orientations of these relations follow by replacing \(T\) with \(T^{-1}\).

Finally each ordered pair of physical lines occurs at exactly one right difference. For any cross-line relation, the two prescribed role marginals have first mass at most \(G^2\) and maximum at most \(G\), and \(T\) is injective. Thus the first mass of the restricted correlation is at most \(G^3\). For an intraline relation, that physical line has total restricted mass at most \(G\) and the other line set at most \(G^2\), giving the same bound. Multiplying first mass by the pointwise upper bound, and adding the at most one exceptional \(h\), proves the assertion.

In particular a fixed finite collection of such relations, including equality and the reciprocal map \(x\mapsto1/x\), is removable by the counting-norm triangle inequality at the target \(O(p^2)\) in squared energy. For \(T(x)=1/x\), the transformation in \(D\) equals \(T\) only at \(c=a-1, Y=1/a, Y'=a\) on the retained domain. The preceding fixed-\(Y\) estimate includes this case with the original weights. The constants for a union can grow with the number of maps. The general four-label energy and its implication for one match remain open.
