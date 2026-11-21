# Pairing the intermediate position in the actual same-row square

Let \(G=\mathbb F_p^{\times2}\), let \(n=|G|\), and use position coordinates on \(G\) for the frequency operator \(K\). In these coordinates \(K\) multiplies by \(s(x)=\chi(1-x)\). Write \(D,D^{\mathrm J}\) for the actual derivative diagonals at the fixed height \(601\) and at the pure Jacobi seed, with the original closed square and \(t_0=n\). Denote their inverse Fourier rows by \(d,j\), with the normalization that diagonal multiplication by \(D\) becomes convolution with kernel \(d(x/y)\). Both frequency diagonals are inversion-even, so \(d(x)=d(x^{-1})\) and likewise for \(j\). The marked derivative is included in these rows.

## Exact cancellation rule

At positions \(x,y\in G\), set \(c=xy\). The kernel of \((KD)^2-(KD^{\mathrm J})^2\) is exactly
\[
 \frac{s(x)}2\sum_{z\in G}\bigl(s(z)+s(c/z)\bigr)
          \bigl(d(x/z)d(z/y)-j(x/z)j(z/y)\bigr).                    \tag{1}
\]
Indeed the change of variable \(z\mapsto c/z\) interchanges the two convolution factors in each product. Averaging the original expansion and its image proves (1). For the same-row anticommutator with \(e=d-j\), the exact kernel is
\[
 s(x)\sum_{z\in G}\bigl(s(z)+s(c/z)\bigr)e(x/z)j(z/y).           \tag{2}
\]
Here the same change of variable takes the second convolution order into the first. These identities hold at the exceptional characters and for complex parameters because they use the full physical Fourier rows and ordinary transposition. They also hold at fixed positions of the involution. When the two nonzero intermediate signs are opposite, the paired coefficient vanishes exactly. At \(xy=1\), the signs agree for every \(z\) because \(\chi(-1)=1\) and \(z\) is square, so the pairing gives no saving on those entries.

## Exact exceptional-position count

For \(c\ne1\), let \(a_p(c)=p+1-\# E_c(\mathbb F_p)\) for the Legendre curve \(E_c:Y^2=X(X-1)(X-c)\). The [Legendre identity](paired-legendre-cubic-116.md#conversion-to-a-restricted-legendre-family) gives
\[
 \sum_{z\in G}s(z)s(c/z)=-1-\frac{a_p(c)}2 .
\]
There are exactly two points with a zero sign, \(z=1,c\), each contributing a coefficient of modulus one. Among the other \(n-2\) points, the number with the two signs equal is
\[
 \frac{n-3}{2}-\frac{a_p(c)}4 .
\]
Thus the number of nonzero entries of the inner sign mask is \((n+1)/2-a_p(c)/4=n/2+O(\sqrt p)\) uniformly for \(xy\ne1\). Its exact squared norm is \(2n-4-a_p(c)\). For \(xy=1\) it is \(4(n-1)\). The outer factor \(s(x)\) makes the full row zero when \(x=1\).

This is a signed identity for the actual two-step operator and a uniform count for its intermediate sign mask. For example (2) gives the actual counting estimate on a single entry by multiplying \(|s(x)|\) and the square root of this mask norm by the counting second norm of \(z\mapsto e(x/z)j(z/y)\). The weighted products in (1) and (2) can concentrate on the surviving points, and the inverse line \(xy=1\) has no sign cancellation. The count alone gives no \(P_{5000}\) bound. The remaining arithmetic task is to price the weighted paired terms as physical packets, including the inverse line or a smaller exact contribution carried by it.

## Rational parametrization of the surviving signed terms

For \(c\ne1\) and any weight \(F:G\to\mathbb C\), define \(z_c(r)=(r^2-c)/(r^2-1)\) for \(r^2\notin\{1,c\}\). Extend \(F\) by zero to nonsquares wherever it is evaluated below. Then
\[
\begin{aligned}
 \sum_{z\in G}(s(z)+s(c/z))F(z)
 ={}&s(c)F(1)\\
 &+\frac{s(c)}2\sum_{r\in\mathbb F_p,\,r^2\notin\{1,c\}}
      \bigl(\chi(r^2-1)+\chi(r^2-c)\bigr)F(z_c(r)).
\end{aligned}                                                       \tag{3}
\]
To prove this, at \(z\ne1\) the paired sign is \(s(z)(1+\chi((z-1)(z-c)))\). The second factor counts the solutions of \(r^2=(z-c)/(z-1)\), with one root at \(z=c\). The term at \(z=1\) is \(s(c)F(1)\). On the allowed parameter set, \(s(z_c(r))=s(c)\chi(r^2-1)\). Inserting the square indicator \((1+\chi(z_c(r)))/2\) gives the two quadratic characters in (3). This gives a second exact form for a weighted trace calculation away from the inverse line. A bound uniform in the translated packet data still requires an estimate for the two rational pullbacks of the actual convolution weights.
