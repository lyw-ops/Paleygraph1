# The physical complex germ at zero and its signed cubic

Write \(n=(q-1)/2,\ c=(n-1)/n\), and use the mean-one stationary rows and marked logarithm of [round 40](astra-scalar-40.md). For either sign there is an explicit complex disk centered at **zero**, computed from one linear lifting map on the two complementary faces. Its construction gives a signed difference of squared norms for the physical cubic coefficient, including when the optimal face has positive dimension. Cyclotomic minor bounds give an unconditional, very small disk at every order. On that disk the actual prime slope retains the prime support improvement at zero. This does not give access from the hot component at a fixed positive floor.

## The two face spaces

Let \(u,v\) be the sign and opposite-sign optimal face analytic centers, \(u_0=\theta,\ v_0=n/\theta\), and let \(I,J\) be their respective unmarked positive supports. These partition the unmarked coordinates. Let \(V\) be the real mean-zero tangent sector of the chosen sign. For \(k\in V\), orthogonality to \(v\) gives \(k_0/\theta=-\sum_J v_jk_j/n\). Use ordinary Euclidean products separately on the two sets, including all multiplicities. Set
\[
 H=\{(k_i/u_i)_{i\in I}: k\in V,\ k_J=0\},\qquad
 K=\{(v_jk_j)_{j\in J}: k\in V\}.
\]
The face-center equation gives \(\mathbf1_I\perp H\), and the [transversal at zero](astra-scalar-40.md) gives \(\mathbf1_J\in K\). For \(z\in K\), lift to any \(k\in V\) with \(v_Jk_J=z\), and set \(Lz=(1-P_H)(k_I/u_I)\), where \(P_H\) is orthogonal projection. This defines a linear map into \(H^\perp\) independent of the lift. The projection amounts to choosing the lift of least weighted norm on \(I\). Define \(D=\|L\|_{2\to2}\) and \(b=|J|/n\).

In variables \(p\in H,s\in K\), parametrize the affine feasible row near zero by
\[
 P_0=\theta(1-t\beta),\quad P_I=u_I(1+p+tL(1+s)),\quad
 P_J=(t/v_J)(1+s),\qquad \beta=n^{-1}\sum_J(1+s_j).
\]
Each symbol 1 has the size of its block. For real \(t\ne0\) this parametrizes the entire affine space. Put \(y=p+tL(1+s)\) and \(g(z)=z^2/(1+z)\) entrywise. Differentiate the weighted log objective after dividing by \(t\). The two stationarity equations are the fixed-point equations
\[
 p=P_H g(y),\qquad
 s=P_K g(s)+tL^*(1+y)^{-1}
        -\big[(1-t\beta)^{-1}-1\big]\mathbf1_J.                 \tag{1}
\]
Indeed the two gradients are the projections of \((1+y)^{-1}\) and of \((1+s)^{-1}+tL^*(1+y)^{-1}-(1-t\beta)^{-1}\mathbf1_J\). Expand \((1+z)^{-1}=1-z+g(z)\), using \(P_H L=0\).

## A quantitative actual disk

Take \(R=[128\sqrt n(1+D)]^{-1}\). On \(|t|\le R\), use the closed complex ball \(\max(\|p\|_2,\|s\|_2)\le 1/8\). There \(\|y\|_2<1/6,\ |\beta|<2\). The right side of (1) is a contraction of Lipschitz constant below \(1/2\): the scalar derivative of \(g\) on \(|z|\le h\) is bounded by \((1-h)^{-2}-1\), and \(\|dy\|_2\le(1+|t|D)\max(\|dp\|_2,\|ds\|_2)\). The additional derivatives in the second equation have norms at most \(|t|D(1+|t|D)(1-1/6)^{-2}\) and \(|t|(1-2|t|)^{-2}\). At the origin the maximum of the two outputs is at most \(4|t|\sqrt n(1+D)\le1/32\), by the same elementary denominator bounds. The map thus preserves the ball. Its iterates give an analytic solution there with
\[
 \max(\|p\|_2,\|s\|_2)\le8|t|\sqrt n(1+D).
\]
At small positive real \(t\) all entries are strictly positive, so stationarity identifies the physical optimum. The explicit logarithm is
\[
 F(t)=\sigma m_q(t)=\log(\theta/\sqrt n)+\log(1-t\beta)+\tfrac12\log(1+ct).
\]
Since \(|\beta-b|\le\|s\|_2/\sqrt n\), the logarithm series gives
\[
 |F(t)-F(0)-(c/2-b)t|\le16(1+D)|t|^2.                             \tag{2}
\]
Consequently \(|[t^j]F|\le16(1+D)R^{2-j}\) for every \(j\ge2\); on \(0\le t\le R/2\) the Taylor series gives \(|F'(t)-(c/2-b)|\le96(1+D)t\).

For the signed cubic let \(a=L\mathbf1_J\), \(r=L^*\mathbf1_I-b\mathbf1_J\), and \(\bar r=n^{-1}\sum_J r_j\). Equation (1) gives \(p=O(t^2)\) and
\[
 s=tr+t^2\{P_K(r^2)-L^*a-(\bar r+b^2)\mathbf1_J\}+O(t^3).
\]
Sum this expansion on \(J\), using \(\mathbf1_J\in K\) and \(\langle \mathbf1_J,L^*a\rangle=\|a\|^2\). Inserting it into the marked logarithm yields the exact expression
\[
 \boxed{[t^3](\sigma m_q)=
       (\|a\|_2^2-\|r\|_2^2)/n+2b^3/3+c^3/6.}                    \tag{3}
\]
This uses the minimum-norm lift in the definition of \(a\). An arbitrary transversal representative on \(I\) would change the squared norm. Empty blocks have their ordinary zero-dimensional interpretation.

## An arithmetic bound independent of the faces

Let \(\Pi\) project onto \(V\); its entries are sums of \(n\)-th roots of unity divided by \(n\). Each embedding of the cyclotomic field, of degree \(d\le n\), carries it to another orthogonal projection, by permuting Fourier characters. At any vertex of the feasible polytope with support \(S\) of size \(h\), the columns of \(1-\Pi\) in \(S\) have full rank (otherwise perturb in both signs). Here \(1-\Pi\) denotes the identity operator minus the projection. The corresponding principal block \(B\) thus has positive determinant and \(B x_S=\mathbf1_S\). Cramer's numerator obtained by replacing a column by ones has modulus at most \(\sqrt h\) at every embedding, since the other columns have norms at most one. After multiplication by \(n^h\) it is an algebraic integer. Any nonzero numerator has modulus at least \(n^{-hd}h^{-(d-1)/2}\). The denominator \(\det B\le1\). For each positive face coordinate some vertex of that face, hence of the whole polytope, is positive there. Stationarity of the face log center against that vertex gives \(\sum_I x_i/u_i=|I|\). Both face centers therefore have every active bulk coordinate at least \(\delta=n^{-n^2-n-1}\).

For the coordinate restriction from \(V\) to \(J\), the nonzero squared singular values are the positive eigenvalues of \(\Pi_{JJ}\). Let its rank be \(h\). The product of these eigenvalues is the sum of its principal minors of size \(h\). It becomes an algebraic integer after multiplication by \(n^h\), and at each embedding the product is at most one: the rank is preserved and all eigenvalues lie in \([0,1]\). The least nonzero squared singular value is therefore at least \(n^{-hd}\). A minimum Euclidean lift from the restriction costs at most \(n^{n^2/2}\); dividing by active entries on the two sides and projecting away \(H\) gives
\[
 D\le \delta^{-2}n^{n^2/2}\le n^{3n^2}\qquad(n\ge6).
\]
This proves a uniform-in-the-input formula with a rapidly shrinking radius. For any \(0\le t_q\le n^{-4n^2}\), equation (2) and its derivative bound give
\[
 F'(t_q)=\frac{|I|-|J|}{2n}+O(n^{-n^2})
\]
as \(n\to\infty\). In particular the [prime affine rank bound](parallel-low-energy-7.md) improves the maximal absolute slope by \((1-o(1))/\sqrt n\) throughout this moving interval. For \(n=2\ell\) with \(\ell\) prime, the [two-coset folding bound](parallel-sampling-12.md) puts both bulk support densities above \(3/8-O(p^{-1/2})\); hence \(|m'_p(t_p)|\le1/8+O(p^{-1/2})\) there. This latter assertion is restricted to the specified factorization and assumes no infinitude for it. For prime squares \(q=h^2\), the [unique plus face](square-endpoint-uniqueness.md) instead gives \(m'_q(t_q)=-1/2+h/(2n)+O(n^{-n^2})\).

Equations (1)–(3) give finite-field results at the actual endpoint. Neither the size bound on the disk nor the signed cubic formula controls the continuation from zero to any fixed floor uniformly through primes. The ordinary theta limit remains open.

The [exact checker](astra-cold-43-check.py) computes the left side of (3) independently from the physical prime-13 cubic and square-25 quintic. For the latter it projects the transversal orthogonally to the full tangent fixed by the endpoint symmetries. The invariant optimal face is a line with the parameter used in [round 40](astra-scalar-40.md); orthogonal projection of an invariant vector onto the full tangent is invariant. The opposite supported indices are one orbit. At 13 the even optimal face is a point. The [two exact records](astra-cold-43-checks.jsonl) use the coefficient of the Taylor series, i.e. one sixth of the third derivative. Replay with `uv run --no-project --with sympy==1.14.0 python -B research/astra-cold-43-check.py`.
