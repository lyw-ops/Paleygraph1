# Difference multiplicities at the actual supercritical coordinates

Fix a sign and a feasible probability \(q\). Write \(G\) for the cyclic group of \(n\) frequency sites. For fixed \(\delta>0\), take a nonempty subset \(A\) of the sites with \(\sqrt n\,q_h\ge1+\delta\). Put \(a=|A|\) and \(v_i=a^{-1}\sum_{h\in A}q_{i+h}\). Translation preserves positivity, mass and Fourier zeros. Thus \(v\) is feasible on the same sign with \(\sqrt n\,v_0\ge1+\delta\). If \(A\) consists of exact maximizers of a primary optimum \(q\), then \(v\) stays on the actual primary face.

On any of the opposite selected windows of width \(d\to\infty\), \(d=o(D)\), fix \(u=\delta/8\) and take \(B\to\infty\), \(B=o(d)\). The feasible-row hinge comparison from [round 72](smooth-windows-72.md) gives
\[
 C_{s,u,B}(v)\ge c_\delta d. \tag{1}
\]
Indeed the marked factor tends to one and the mean allowance to zero. This estimate works on each selected window, with constants independent of \(q\) and \(A\).

Write \(x_i=(q_i-B/n)_+\), \(M=\sum_i x_i\), and \(R_A(t)=|A\cap(A+t)|\). Convexity gives \((v_i-B/n)_+\le a^{-1}\sum_{h\in A}x_{i+h}\). If \(S\) is the actual opposite fixed-deficit set, the hinge of \(v\) has the upper certificate
\[
 C_{s,u,B}(v)\le \frac{n}{a^2}\sum_{y,z}x_y x_z
               |S\cap(y-A)\cap(z-A)|. \tag{2}
\]
Only original high-density pairs contribute. The diagonal term is at most \(n\sum_i x_i^2/a\). Dropping \(S\) for the other terms and setting \(L=\max_{t\ne0}R_A(t)\) gives
\[
 c_\delta d\le \frac{n}{a}\sum_i x_i^2+
        \frac{nL}{a^2}\left(M^2-\sum_i x_i^2\right)
 \le \frac{C\sqrt n}{a}+\frac{nL}{a^2}. \tag{3}
\]
The bound \(q_i\le C/\sqrt n\) is the ordinary endpoint cap on either side. The middle expression sharpens the test when little mass survives truncation. Equation (2) requires no invariance of \(S\) under translation. For exact cap sites of a primary optimum, (2) is an upper bound on the true-face minimum on this window.

Consequently on the actual prime sequence every supercritical set \(A\) with bounded nonzero difference multiplicity \(L\) has
\[
 |A|=O_{\delta,L}(\sqrt{n/D}). \tag{4}
\]
Along any purported subsequence violating (4), put \(f=a\sqrt{D/n}\to\infty\). Take \(d=\lfloor D/g\rfloor\) with \(g\to\infty\), \(g=o(f^2)\), and \(g=o(D)\), for example \(g=\min(\sqrt D,\sqrt f)\). The two terms in the rightmost bound of (3) are then \(o(d)\), a contradiction. In particular a Sidon subset of supercritical sites of growing size relative to \(\sqrt{n/D}\) is excluded. The result applies to sites a fixed amount above the target even when recentering reduces the mark. Period subgroups have \(L=a\) for \(a>1\). A singleton root also satisfies this test. The unconditional \(o(d)\) upper on the full hinge minimum remains open.

1. Test the masked difference counts in (2) for cap-centered translates of a noncanonical optimizer. If every cap shift is a period (as for the least-norm row), these averages reproduce \(q\). Nonperiodic cap shifts can change the actual row.
2. On a near-cap \(A\), keep the popular differences under the truncated law \(x\) and intersect with the actual translated mask. After subtracting the exact masked diagonal contribution from \(c_\delta d a^2/n\), the lower bound applies to the remaining ordered pairs in (2). When the diagonal cost is \(o(d)\), those off-diagonal terms have total at least a constant times \(d a^2/n\) before normalization. Periodic or isolated sites require a separate estimate.
