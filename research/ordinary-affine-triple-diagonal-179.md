# The true physical diagonal and weighted affine triples

Use the actual \(g,w,G\), physical masks and nonzero interior of [Round 178](ordinary-parabolic-row-mean-square-178.md). In particular \(G=\sum g=O(\sqrt p)\), \(0\le g,w\le1\), and \(g\) is invariant under inversion on \(\mathbb F_p^\times\). All sums below use counting norms. The resulting bound for the actual whole positive diagonal is
\[
 \sum_s w(s)P_s^2=O(p^{9/4}).
\]
The reduction was found by native Astra agent /root/distinct_179. The sufficient \(O(p^{3/2})\) bound remains open.

## Two copies at equal physical output

In one copy put \(a=A,\ v=1/a,\ x=1/Y,\ u=1/C\), and \(f_0(v)=v(1-v)\). The genuine chart gives
\[
 (1-A)(1-D)=(1-C)(1-Y),\qquad D=sCY/A.
\]
Substitution yields
\[
 (a/C-1)(a/Y-1)=(a-1)(s-1),\qquad
 (x-v)(u-v)=f_0(v)(s-1),\qquad D=s/(a x u).
\]
All retained \(f_0(v),x-v,u-v,s-1\) are nonzero. At fixed \(v,x,u\), these equations determine \(s,D\), and the actual chart recovers the remaining physical parameters uniquely when the tuple is admissible. In particular all physical labels in these coordinates determine at most one tuple.

In a second copy of the same \(s\), use primes on the labels and put \(\lambda=f_0(v')/f_0(v)\). Then there is a unique \(k\ne0\) such that
\[
 x'=h_k(x),\qquad u'=h_{\lambda/k}(u),\qquad
 h_k(z)=v'+k(z-v).
\]
With these formulas the exact kernel retains both \(D,D'\), the physical masks, and \(w(s)\). For an upper bound we may majorize those three weights by one and enlarge the remaining domain. Let \(m(h)=\sum_z g(z)g(hz)\). By inversion symmetry the retained six amplitude factors yield the upper at fixed \(v,v'\)
\[
 g(v)g(v')\sum_{k\ne0}m(h_k)m(h_{\lambda/k})
 \le g(v)g(v')\sum_{k\ne0}m(h_k)^2.
\]
The inequality uses the involution \(k\mapsto\lambda/k\) and Cauchy–Schwarz. Since \(v'=h_k(v)\), the sum over the two centers is at most \(\sum_{h\in\mathrm{Aff}(\mathbb F_p)}m(h)^3\). This is a bound on the actual whole interior and therefore on the positive distinct-\(b\) part alone. It does not equate distinct \(b\) with distinct \(r\).

## Weighted affine triples

For a set \(S\), write \(U=|S|\) and \(m_S(h)=|S\cap h^{-1}S|\). Then
\[
 \sum_h m_S(h)=(p-1)U^2,\qquad
 \sum_h m_S(h)(m_S(h)-1)\le U^4,
\]
by transitivity and uniqueness of an affine map carrying two prescribed distinct inputs to two distinct outputs. The rich-line estimate of [Round 178](ordinary-weighted-slope-product-incidence-178.md), derived from [Rudnev–Shkredov, (22)](https://arxiv.org/pdf/1812.01671), counts \(O(U^5/t^4)\) maps when \(t\ge C(1+U^2/p)\). For \(U\ge1\), split at \(H=\max\{\sqrt U,C(1+U^2/p)\}\). Up to \(H\), use \(m^3=m+(m^2+m)(m-1)\le m+(H+1)m(m-1)\). The rich cubes cost \(O(U^5/H)\), by the threshold term and integrating the tail. Consequently
\[
 \sum_h m_S(h)^3=O(pU^2+U^{9/2}+U^6/p).
\]

For different levels \(S,T\), the corresponding mixed cubed sum is at most the geometric mean of the self sums. Indeed the cube of the overlap is the inner product of the indicator tensor cubes under the tensor-cube permutation representation of the affine group. Group averaging is an orthogonal projection, and Cauchy–Schwarz applies to the two projected tensor cubes. Take the counting third norm and use layer cake for both weights in \(m(h)\). With \(S_t=\{g>t\}\) this gives
\[
 \|m\|_3\le\left(\int_0^1
        \bigl(\sum_h m_{S_t}(h)^3\bigr)^{1/6}dt\right)^2.
\]
The integrated terms have exponents \(1/3,3/4,1\) in \(|S_t|\), and \(\int|S_t|=G\). Hence \(\sum_h m(h)^3=O(pG^2+G^{9/2}+G^6/p)=O(p^{9/4})\). The earlier priced physical endpoints return by the \(w\)-weighted triangle inequality.

## The one-role and prescribed-map classes

For the kernel \(K(s,a)\) with \(A=a\) fixed, the product identity bounds \(K(s,a)\) by \(g(a)(g_v*_\times g_v)(f_0(v)(s-1))\), where \(g_v(t)=g(v+t)\) on the nonzero multiplicative group and \(*_\times\) uses counting convolution. Inversion symmetry and the injectivity of \(s\mapsto f_0(v)(s-1)\) give
\[
 \sum_{s,a} K(s,a)^2\le \sum_v g(v)^2 E^\times(g_v).
\]
Here the multiplicative energy of a function is the squared second norm of its multiplicative convolution with itself.

For a level \(S\) of size \(U\), use center weights \(\gamma_v=g(v)^2\), with \(Z=\sum_v\gamma_v\le G\). Let \(m_v(k)\) count the pairs in \(S\setminus\{v\}\) under the dilation \(x\mapsto v+k(x-v)\). Its first mass over \(k\) is at most \(U^2\) per center. For \(k\ne1\) each map has a unique center, so the rich-line bound applies to the sum with weights \(\gamma_v\le1\). The identity contribution is at most \(ZU^2\). For \(Z>0,U>0\), split at \(H=\max\{C(1+U^2/p),U/Z^{1/3}\}\). Below this the cost is at most \(ZU^2 H\); the rich squares cost \(O(U^5/H^2)\), including the threshold term. Thus
\[
 \sum_v\gamma_v E^\times(1_{S-v}\text{ on }\mathbb F_p^\times)
 \ll ZU^2(1+U^2/p)+Z^{2/3}U^3 .
\]
The zero cases are immediate. Taking the fourth root is the weighted fourth norm in center and multiplicative Fourier character, with a fixed Fourier normalization. Layer cake and the triangle inequality give the weighted shifted energy bound \(O(G^3+G^5/p+G^{11/3})=O(p^{11/6})\). The physical role symmetries of [Round 177](ordinary-shifted-energy-four-factor-diagonal-177.md) preserve unweighted counting norms over \(s\), allowing slope inversion. Therefore any prescribed finite projective relation between a single pair of roles in two copies, with map allowed to depend on \(s\), costs \(O(p^{11/6})\) by Cauchy–Schwarz on the two role kernels. The actual \(w\le1\) only decreases this bound.

For a literal common \(A\), the companion dilation is \(k^{-1}\). The class with \(m_v(k)=\sum_{x\ne v}g(x)g(v+k(x-v))\le H\) for a fixed \(H\) costs \(O(HG^3)\), since \(m_v(k)=m_v(k^{-1})\) and \(\sum_k m_v(k)\le G^2\). The identity map costs \(O(G^3)\) separately. Another target-scale cut uses at most \(O(p^{3/418})\) prescribed maps between two ordered role pairs at each \(s\). The existing per-index weight bound two from [Round 173](ordinary-full-diagonal-two-pin-173.md) and the actual first mass \(O(p^{3/2-3/418})\) from Round 177 bound the sum by \(O(p^{3/2})\) whenever these maps on the pair labels are injective on the retained domain. For instance the relative map between the two inverted lines matches \(1/A\) and \(1/Y\) simultaneously at arguments \(X=1/s\) and \(X=1\).

## A shared invariant for the remaining coupled estimate

Write \(h_k(z)=kz+d\) and let its companion \(h_{\lambda/k}\) have slope \(k_2\) and intercept \(d_2\). For \(v'=kv+d\), direct substitution gives
\[
 d_2=\frac{v'(k+d-1)}{k(1-v)},\qquad
 k_2+d_2-1=\frac{d(1-v')}{kv}.
\]
Hence \(J(h)=d(k+d-1)/k\) is the same for both maps. To price a single \(J\), repeat the previous Cauchy bound within this invariant class, using \(g_0=g1_{\mathbb F_p\setminus\{0,1\}}\) for the six retained inputs. Given \(x,y\ne0,1\), \(h(x)=y\) on this class forces
\[
 (x-1)d^2+(y-x+J)d-Jy=0,
\]
so at most two maps occur. Thus \(\sum_{h:J}m_0(h)\le2G^2\) and the cubed sum is \(O(G^4)\). For \(J\ne0\), \(d\ne0\), so the true shifted affine overlap from [Round 173](ordinary-weighted-affine-vertical-saving-173.md) improves the uniform per-\(J\) price to \(O(p^{2-1/640})\). These estimates do not sum to the target. The exact conic relation and the computed \(D,D'\) weights give a particular remaining coupled test.
