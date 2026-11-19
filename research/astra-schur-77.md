# Signed Schur prices after deleting different neighbours in every masked row

A true supercritical endpoint must retain signed interaction of order its **full** clipped collision on every selected negative mask, even after removing the root, other large coordinates and a sparse list of neighbours chosen separately for each masked site. A common exceptional coordinate keeps its own diagonal when its row is tested. This removes the earlier loss from large masked collision on the exceptional sites. The coefficients on surviving pairs must be recomputed after deletion. Four certified endpoints show a substantial difference between recomputation and simply dropping expensive pairs.

## A uniform row estimate

Write \(n=(p-1)/2\), let \(q\) be any feasible probability in the sign-\(\sigma\) sector, and let \(P\) be the orthogonal Fourier projection on the forbidden positions. Then \(Pq=0\), \(P_{ii}=1/2+O(1/n)\) and \(|P_{ij}|\le C/\sqrt n\) for \(i\ne j\). All norms below use counting measure. Fix a set \(S\), a cutoff \(B\ge0\), and put
\[
 x_i=(q_i-B/n)_+,\qquad z=q-x,\qquad
 y_i=x_i\mathbf1_S(i),\qquad L=n\|y\|_2^2 .
\]
The set and all the choices below may depend on \(q\). The Jacobi bounds and the standard Schur projector are given in [round 76](astra-masked-76.md).

There are absolute constants \(c,C>0\) with the following property for sufficiently large primes. Choose a common set \(A\) of at most \(2c\sqrt n\) sites. At each \(i\in S\) choose a list \(N_i\) of at most \(c\sqrt n\) sites, excluding \(i\). Put \(U_i=(A\cup N_i)\setminus\{i\}\). For each row separately form
\[
 H^{U}=P-P_{:,U}P_{UU}^{-1}P_{U,:},\qquad R_{ij}=H^{U_i}_{ij}.
\]
Use \(H^\varnothing=P\). Thus \(Rq=0\), \(R_{ij}=0\) for \(j\in U_i\), and \(R_{ii}=1/2+O(n^{-1/2})\) uniformly. Define the incoming weights and signed remaining price by
\[
 w_j=\sum_{i\in S:\,j\in N_i} y_i,\qquad
 \Pi=-n\operatorname{Re}\sum_{i\in S}\sum_{j\ne i}y_i R_{ij}x_j .
\]
The simultaneous estimate is
\[
 \boxed{\left|\Pi-n\sum_{i\in S}R_{ii}y_i^2\right|
 \le C\sqrt{BL}+C\sqrt B\,\|w_{A^c}\|_2.}                 \tag{1}
\]
In particular, a common set alone has error \(O(\sqrt{BL})\) regardless of its share of the masked hinge. The rectangular matrix of selected rows is generally asymmetric.

**Proof.** Every principal block of \(P\) on at most \(3c\sqrt n\) indices is strictly diagonally dominant with margin bounded below by an absolute constant for sufficiently small \(c\). Solving \(P_{UU}b=P_{U,i}\) by the maximum-coordinate inequality gives \(\|b\|_\infty\le C/\sqrt n\) when \(i\notin U\). Thus the Schur diagonal differs from \(P_{ii}\) by \(O(|U|/n)\). Also \(H^A\) restricted to \(A^c\) has diagonal \(1/2+O(n^{-1/2})\) and off-diagonal entries \(O(1/\sqrt n)\). The constants in these latter bounds may be chosen uniformly for all sufficiently small \(c\).

For \(i\in A\cap S\) the row applied to \(z\) is \((Pz)_i-b_i^*(Pz)_{U_i}\). The matrix of the correction coefficients has at most \(|A|\cdot 3c\sqrt n=O(n)\) nonzero entries of size \(O(1/\sqrt n)\), hence bounded Frobenius norm. It follows that the vector of these retained rows on \(z\) has norm \(O(\|z\|_2)\), even when the lists of neighbours overlap completely.

For \(i\in S\setminus A\) first eliminate \(A\), and write \(H=H^A\), \(V_i=N_i\setminus A\). Then
\[
 (Rz)_i=(Hz)_i-b_i^*(Hz)_{V_i},\qquad b_i=H_{V_iV_i}^{-1}H_{V_i,i}.
\]
Indeed the further projection removes the span of the columns \(He_j\) for \(j\in V_i\), imposing exactly the remaining vanishing conditions. Strict diagonal dominance again gives \(\|b_i\|_\infty\le C/\sqrt n\), after reducing \(c\) if needed. The weighted correction over these exterior rows is therefore at most
\[
 (C/\sqrt n)\sum_{j\notin A} w_j |(Hz)_j|
 \le (C/\sqrt n)\|w_{A^c}\|_2\|z\|_2 .
\]
The other contributions, including all rows in \(A\), cost \(O(\|y\|_2\|z\|_2)\). Now \(n\|z\|_2^2\le B\sum_i z_i\le B\). Taking the scalar product of \(Rq=0\) with \(ny\) gives \(\Pi=n\sum_i R_{ii}y_i^2+n\operatorname{Re}\langle y,Rz\rangle\), proving (1).

## Choosing the shared columns from the actual directed pairs

Start with any top or root set \(A_0\) of size at most \(c\sqrt n\). Add the \(h=\lfloor c\sqrt n\rfloor\) largest \(w_j\) outside it, or all positive entries if fewer. For
\[
 J=\sum_{i\in S} y_i|N_i|=\sum_j w_j
\]
we have \(\|w_{A^c}\|_2^2\le(\max_{j\notin A}w_j)\sum_{j\notin A}w_j\le J^2/h\). Formula (1) now costs \(O(\sqrt{BL}+p^{-1/4}\sqrt B\,J)\). This allows highly repeated outgoing targets and costs nothing at the diagonal of a newly added common site beyond its \(O(n^{-1/2})\) Schur shift.

On a [selected smooth window](smooth-windows-72.md), take \(S=\{i\ne0:R_{-\sigma}(i)<-\delta/8\}\). Here \(R_{-\sigma}\) denotes the scalar cold-window proposal. If \(\sqrt n q_0\ge1+\delta\), \(d\to\infty\), \(d=o(D(p))\) and \(B=o(d)\), the round-72 lower bound yields \(L\gg_\delta d\). Hence, on **each** such window,
\[
 \sqrt B\,J=o(p^{1/4}d)\quad\Longrightarrow\quad
              \Pi=(1/2+o(1))L .                              \tag{2}
\]
For example when \(B=1\) one may delete \(o(p^{1/4}d)\) private neighbours per row subject to the local \(c\sqrt n\) ceiling, because \(\sum_i y_i\le1\). Lists with large outdegree on sites with small \(x_i\) may obey the weighted condition as well. Both (1) and (2) also hold for \(B=0\), when there is no low-part error. The proof uses the genuine selected mask for the hinge lower bound. The projector estimate itself holds for other masks and over eligible prime powers satisfying the same coherence bound.

## A cap set by the exterior clipped mass

Put \(E=A^c\), \(M_E=\sum_{j\in E}x_j\), \(Z_E=\sum_{j\in E}z_j\), and \(K_{ij}=H^{A\setminus\{i\}}_{ij}\) for **every** \(i\in G\). There are absolute \(C_0,C_1\) such that
\[
 \boxed{\quad n\sum_{i\in G}(q_i-C_0M_E/\sqrt n)_+^2
                      \le C_1 B Z_E .\quad}                     \tag{3}
\]
For \(|A|=o(\sqrt n)\) one may use \(C_0=\sqrt2+o(1)\). This applies to the full probability, including the root and every other common site.

To prove (3), the rows in \(E\) of \(K\) equal rows of the contraction \(H^A\), while the rows in \(A\) have bounded operator norm by the Frobenius argument in (1) with empty private lists. Thus \(\|K\|\le C\). Its diagonal is bounded below and \(|K_{ij}|\le C/\sqrt n\) on surviving off-diagonals. From \(Kq=0\) we have
\[
 q_i\le t_i M_E+|v_i|,\quad
 t_i=\max_{j\in E,\,j\ne i} \frac{(-\operatorname{Re}K_{ij})_+}{K_{ii}},
 \quad v_i=K_{ii}^{-1}\sum_{j\in E,\,j\ne i}K_{ij}z_j . 
\]
Use zero for an empty maximum. Since \(\|v\|_2\le C\|z_E\|_2\) by deleting the diagonal of \(K\) and using its diagonal lower bound, (3) follows. The maximum may be restricted to sites with \(x_j>0\). For \(|A|=o(\sqrt n)\), all modified off-diagonal entries differ from their original Jacobi entries by \(O(|A|/n)=o(n^{-1/2})\) on surviving pairs. The Jacobi coherence \((1+\sqrt p)/(2n)\) and \(K_{ii}=1/2+o(1)\) give \(t_i\sqrt n\le\sqrt2+o(1)\).

On every supercritical selected mask with \(B=o(d)\), the sites with \(q_i>2C_0 M_E/\sqrt n\) carry only \(O(BZ_E)=o(d)\) normalized collision, since \(q_i^2\le4(q_i-C_0M_E/\sqrt n)_+^2\) there. Round 72 forces \(\gg_\delta d\) normalized collision on \(i\in S\) with \(nq_i>c_\delta d\). Subtracting the just bounded part gives the same order of collision on the two-sided density band
\[
 i\in S,\qquad c_\delta d/n < q_i\le 2 C_0M_E/\sqrt n .
\]
Consequently this actual intermediate band contains \(\gg_\delta d/M_E^2\) sites whenever the fixed supercritical gap holds. The cutoff \(B\) used to determine \(M_E\) can be chosen independently of the lower density threshold \(c_\delta d\).

## Absolute sparse prices for the original root/top kernel

The original entries can also be kept, for a separate estimate that allows **arbitrary private degrees**. Take any collection of directed pairs from rows in \(S\) to distinct heads in \(E\) other than the row itself. Write \(w_j\) for their incoming clipped weights as before, \(J=\sum_j w_j\), and \(M_S=\sum_i y_i\). Then
\[
 n\sum_{i\to j} y_i |K_{ij}|x_j
 \ \le\ C\big[M_E J+\sqrt{B Z_E}\,\|w\|_2\big]
 \ \le\ C\big[M_E J+\sqrt{B Z_E M_S J}\big].                   \tag{4}
\]
Indeed \(x_j\le q_j\le C M_E/\sqrt n+|v_j|\) by (3)'s pointwise proof, and \(\|v\|_2\le C\sqrt{BZ_E/n}\). Apply \(|K_{ij}|\le C/\sqrt n\) followed by Cauchy–Schwarz. The last inequality uses \(w_j\le M_S\). Repeated heads in different rows are allowed.

For \(M=\sum_i x_i\), the sufficient condition \(MJ=o(d)\) at \(B=o(d)\) makes (4) \(o(d)\). Thus the unmodified root/top kernel still has signed price \((1/2+o(1))L\) on surviving pairs. Lists may contain the largest **positive** individual prices in their respective rows. Even the sum of absolute prices on those lists is negligible at this scale. For lists of length at most \(k\), it suffices that \(kM_SM=o(d)\). This can permit many more than \(d\) priced pairs per row when the clipped masses are small. In contrast, (2) applies to the recomputed kernel and can remain effective when old entries change substantially.

There is a direct signed rectangle test on the actual level sets. For \(u,v\ge0\) put \(I_u=\{i\in S:x_i>u\}\), \(T_v=\{j:x_j>v\}\) and
\[
 \Phi(I,T)=-\operatorname{Re}\sum_{i\in I,\,j\in T,\,j\ne i}R_{ij}.
\]
After fixing the lists and common columns the price is exactly \(n\int_0^\infty\int_0^\infty\Phi(I_u,T_v)\,du\,dv\). With the clipped masses above, (2) forces some nonempty actual rectangle to satisfy
\[
 \frac{\Phi(I_u,T_v)}{|I_u|\,|T_v|}
 \ \ge\ (1/2-o(1))\,\frac{L}{nM_SM}.
\]
Indeed \(|I_u||T_v|\,du\,dv/(M_SM)\) is a probability measure on nonempty rectangles and its weighted mean gives the stated comparison. Tiny exceptional rectangles can make the maximum too large, so the signed integral can give a sharper upper test.

## Four finite checks

On the four certified larger-side even endpoints from round 76, use exactly its five-site cold windows, allowance \(1/1000\), threshold \(1/40\), cutoff \(B=1\) and root/top sets. For the initial kernel each masked top site retains its diagonal, so its initial signed price includes contributions omitted from the exterior-only comparison in round 76. In each positive clipped masked row the two private heads are chosen from positive individual prices in that initial kernel. Two additional common sites are chosen by incoming clipped weight. Numerical ranking specifies the lists, and interval calculations enclose the exact resulting interactions. All figures here are finite-window checks, with no assertion of asymptotic selection for these four starts.

| Prime | Full / top-site masked hinge | Initial signed price | Initial price on all newly blocked pairs | Recomputed signed price | Recomputed diagonal |
|---:|---:|---:|---:|---:|---:|
| 101 | 0.74896 / 0.15666 | 0.31141 | 0.20764 | 0.21471 | 0.24826 |
| 257 | 1.00044 / 0.16672 | 0.45210 | 0.18964 | 0.40110 | 0.44933 |
| 409 | 1.16385 / 0.30994 | 0.51430 | 0.18230 | 0.46727 | 0.53238 |
| 769 | 0.71342 / 0.16832 | 0.32691 | 0.07203 | 0.31047 | 0.34324 |

At 101 the initial price on the surviving pairs is below \(0.10378\), whereas their recomputed price exceeds \(0.21470\). Thus a sparse explanation based on dropping terms of a fixed signed kernel can substantially underestimate the price required after exact elimination. The [Arb768 checker](astra-schur-77-check.py) encloses the complementary positive endpoints and threshold decisions, verifies each local solve and its deleted entries, and checks the signed diagonal identity. The [four outward records](astra-schur-77-checks.jsonl) retain the low inner products as well. The corresponding exterior clipped masses are \(0.40053,0.43104,0.44433,0.46865\) to five decimal places. On all four windows the checker certifies \(q_i\le t_i M_E\) at every clipped masked site using the per-row support-aware \(t_i\) of (3). Thus the cap's excess is exactly zero there, even though the signed low terms need not vanish.

1. Count the actual intermediate-band incidences after removing the root/top coordinates from the exterior clipped mass as in (3). A count \(o(d/M_E^2)\) on one selected window for a larger-side optimizer excludes a fixed supercritical sequence. The count concerns true cold deficits, actual primary masses, and a two-sided density interval.
2. If this band is sufficiently populous, take the largest positive individual prices on its actual support. Bound their absolute sum by (4), then use (2) and the signed rectangle integral after common and private elimination where the fixed-entry bound is insufficient. A recomputed price below \((1/2-\varepsilon)L\) for fixed \(\varepsilon>0\) under the hypotheses of (2) excludes supercriticality. The genuine prime-uniform upper estimate on these remaining interactions is open.
