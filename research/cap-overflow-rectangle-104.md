# A critical rectangle from the real cap overflow

At a fixed real floor, if the mean cap defect is \(O(n^{-1/2})\) yet the true mark stays nonzero, the signed overflow forces a rectangle of dimensions comparable to \(\sqrt n\) by \(\sqrt n\). Its receiving set consists of genuinely large coordinates of the true stationary positive source. Its sending set is one bounded signed level of the actual capped overflow.

Use the definitions of [the signed exterior test](real-cap-exterior-103.md), with fixed \(t,M>0\). In particular \(b_i=\Phi_t(Y)_i\), \(g_i=b_i-2\sqrt t\ge0\), \(G=K\tau\), and \(\mathbb E_n g\le B_0:=2\sqrt{1+t}\). Suppose along a prime subsequence that
\[
 |\gamma|\ge\delta>0,\qquad
 \alpha\le B/\sqrt n
\]
with fixed \(B>0\). Since \(\gamma_c\to0\) and \(s_0/n\to1\), the first inequality of the cross comparison forces
\[
 \mathbb E_n G_i g_i\ge c:=\cosh\delta-1>0
\]
eventually. Let \(d=c/(2B_0)\) and \(T=\{i:G_i\ge d\}\). Then
\[
 \mathbb E_n 1_T G_i g_i\ge c/2,\qquad |T|\le B d^{-2}\sqrt n .
\]
For the second inequality use \(\|K\tau\|_{2,n}^2\le\|\tau\|_{2,n}^2\le\alpha\). The entry bound and the cap-defect estimate give \(\|G\|_\infty\le C_0:=\sqrt3 B/(2\sqrt{M^2+4t})\). Thus \(\sum_T g_i\ge cn/(2C_0)\). Also \(g_i\le C_1\sqrt n\) with \(C_1=2+\sqrt3 B_0\), since \(Y=Kb\) and \(\mathbb E_n b\le B_0\).

Choose a fixed \(\lambda>0\) with \(\lambda B d^{-2}\le c/(8C_0)\). Discard the mark and the coordinates with \(g_i<\lambda\sqrt n\) in \(T\). The first deletion costs at most \(C_1\sqrt n\) in first mass and the second at most \(cn/(8C_0)\). The remaining set \(T'\) still has \(g_i\ge\lambda\sqrt n\) on every site and size comparable to \(\sqrt n\), with constants depending only on \(t,M,B,\delta\).

The sending set for \(G\) lies in \(S=\{i:\tau_i\ne0\}\), with \(|S|\le B\sqrt n/(4t)\) because each such site pays cap defect at least \(4t\). For fixed \(0<\ell<L\), retain only the values of \(\tau\) with \(\ell\le|\tau_i|\le L\), obtaining \(\tau'\). The discarded first mass is at most
\[
 |S|\ell+L^{-1}\|\tau\|_2^2
 \le B\sqrt n\,(\ell/(4t)+L^{-1}),
\]
where the second norm is unnormalized. Hence
\(\|K(\tau-\tau')\|_\infty\le\sqrt3 B(\ell/(4t)+L^{-1})\). Choose \(\ell,L\) so this is at most \(d/2\). Then \(K\tau'\ge d/2\) on every site of \(T'\). Layer cake, after averaging over \(T'\), supplies a sign \(\sigma\) and a single strict threshold \(s\in[0,L)\) on that truncated send row for which \(S'=\{i:\sigma\tau'_i>s\}\) satisfies
\[
 \sigma\,\frac1{|T'|}\sum_{j\in T',\,i\in S'}K_{ji}\ge\frac{d}{4L}.
\]
Averages over finitely many cut values include their largest prefix. The upper bound on the kernel entries forces \(|S'|\ge d\sqrt n/(4\sqrt3L)\), while \(|S'|\le|S|\). This gives the claimed oriented rectangle with genuine sending and receiving data. The argument uses only the real capped and stationary equations and the entry bound. It provides no prime arithmetic cancellation of that rectangle.

1. Test a prime-uniform signed rectangle estimate specifically for the clipped signed sending level and the actual high stationary receiving set.
2. Try deriving \(\alpha=O(n^{-1/2})\) in the first place at the desired real floors. A qualitative vanishing mean defect gives no comparable critical-size upper for this rectangle.
