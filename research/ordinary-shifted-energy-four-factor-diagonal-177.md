# A four-factor improvement from the true shifted row mass

Use the actual physical interior and positive diagonal \(P_s\) of [Rounds 173 and 176](ordinary-inverted-vertical-power-saving-176.md), with \(g=|f|^2\), \(w=g(1-g)\), \(G=\sum g=O(\sqrt p)\) and the true cap. The resulting weighted full diagonal satisfies
\[
 \sum_s w(s)P_s^2
 =O\!\left(p^{37/16-1/4320-1/512}\right).
\]
The physical \(s=1\) exclusion and previously priced zero endpoints are treated as in those rounds.

## Shifted energy for a set with few quotients

Let \(B\subset\mathbb F_p^\times\setminus\{1\}\), \(N=|B|\le\sqrt p\), and \(|B/B|=KN\). Write
\[
 m(u)=|\{(x,y)\in B^2:1-y=u(1-x)\}|,\qquad u\in\mathbb F_p^\times .
\]
Then \(\sum m=N^2\) and
\[
 E^\times(1-B)=\sum m(u)^2\ll K^{16/13}N^{36/13}.
\]
To prove this, for the set \(T\) of parameters having \(m(u)>h\), write \(t=|T|\) and \(U=B/B\). Consider the lines
\[
 L_{u,v}(x)=v(ux+1-u),\qquad (u,v)\in T\times U .
\]
The slope and intercept together determine \(u,v\), since their sum is \(v\ne0\). The vertical parameter-plane multiplicity is at most \(\min(t,KN)\). A line through the origin contains the points of at most one fixed \(u\), while a line avoiding the origin meets each line of fixed \(u\) in at most one point. Hence the arbitrary parameter-plane line multiplicity is at most \(\max(t,KN)\). Each solution \(y=ux+1-u\) and choice \(z\in B\) gives an incidence \(L_{u,z/y}(x)=z\) in \(B\times B\). From an incidence recover \(u,v\) and \(y=z/v\), so altogether there are at least \(Nht\) incidences.

Apply [Petridis–Roche-Newton–Rudnev–Warren, (4) and Theorem 2.1](https://arxiv.org/pdf/1911.03401), using its all-level prime-field extension as in Round 172, including the energy term \(m_{\mathcal L}|\mathcal L|^3/p\). Dividing by \(Nt\) and using \(N\le\sqrt p\) gives for \(t>0\)
\[
 \begin{split}
 h &\ll K^{7/8}N t^{-3/16}
       +K^{7/8}N t^{-1/4}+K^{3/4}N^{7/8}t^{-1/8}
       +K N^{9/8}p^{-1/8}t^{-1/8}
       +K N^{1/2}\\
   &\ll KN t^{-3/16}+KN^{7/8}t^{-1/8}+KN^{1/2}.
 \end{split}
\]
The terms before simplification come respectively from the vertical energy term, the two parts of the arbitrary-line term, the extra prime-field term, and the secondary incidence term. For \(h\ge C K N^{1/2}\) with a sufficiently large absolute \(C\), this implies
\[
 t\ll (KN/h)^{16/3}+(KN^{7/8}/h)^8 .
\]
Split the squared-energy tail at \(H=C K^{16/13}N^{10/13}\). The identity uses \(\sum_u\min\{m(u),H\}^2\le HN^2\) and \(2\int_H^\infty h\,t(h)\,dh\). The two tail terms give \(O(K^{16/13}N^{36/13})\) and \(O(K^{8/13}N^{31/13})\), respectively. If \(H>N\), the first-mass upper alone suffices.

## Decompose an actual high level

Take \(\epsilon=1/1024\), \(\delta=1/512\) and \(\tau=p^{-\epsilon}\). Let \(S=\{x\ne1:g(x)\ge\tau\}\) on the physical nonzero domain. Its size is \(O(p^{1/2+\epsilon})\). Repeatedly extract a subset \(B_j\) from the remaining level set as long as there are at least \(\lceil p^{1/2-\delta}\rceil\) elements. Each time let \(M_j\) be a maximal-size subset of the current remainder with \(|M_j|\le\lfloor\sqrt p\rfloor\), and put \(m_j=|M_j|\). The hereditary energy estimate of [Round 173](ordinary-weighted-affine-vertical-saving-173.md) gives
\[
 E^\times(M_j)\gg \tau^2 m_j^4/\sqrt p .
\]
With \(Q_0=p^{1/2+2\epsilon}\), Reiher–Schoen's BSG extraction as used there gives \(|B_j|\gg m_j K_j^{-1/2}\) and \(|B_j/B_j|\ll K_j^4|B_j|\) with \(K_j\asymp Q_0/m_j\). Only \(B_j\) is removed from the remainder. The pieces are disjoint. Denote their union by \(S_{\rm str}\) and the leftover by \(S_{\rm small}\), with \(|S_{\rm small}|=O(p^{1/2-\delta})\).

The fourth root of multiplicative energy is a norm on the shifted indicator, by Mellin Parseval. To keep the size dependence of each extraction, use the shifted energy lemma and charge it per removed point:
\[
 \frac{E^\times(1-B_j)^{1/4}}{|B_j|}
 \ll K_j^{16/13}|B_j|^{-4/13}
 \ll Q_0^{18/13}m_j^{-22/13}.
\]
During the portion with more than \(\lfloor\sqrt p\rfloor\) elements in the remainder, \(m_j=\lfloor\sqrt p\rfloor\). Multiplying this price by the total size \(O(p^{1/2+\epsilon})\) bounds its norm contribution by \(O(p^{9/26+49\epsilon/13})\). After that, \(m_j\) is the remainder size. For \(m_j\) in a dyadic range \([M,2M)\), the sum of removed sizes is at most \(2M\), giving norm cost \(O(Q_0^{18/13}M^{-9/13})\). Sum the geometric series down to \(M\asymp p^{1/2-\delta}\) to get \(O(p^{9/26+(36\epsilon+9\delta)/13})\). By the norm triangle inequality this proves
\[
 E^\times(1-S_{\rm str})=O(p^{\alpha}),\qquad
 \alpha=\frac{18}{13}+\frac4{13}\max\{49\epsilon,36\epsilon+9\delta\}
       =\frac{2331}{1664}.
\]

## Transfer with all four input weights

In the exact chart, \(Y=r+(1-r)D\) and \(A=r+(1-r)C\). Thus on the portion with all four arguments in \(S_{\rm str}\), dropping their numerical weights after this joint restriction gives
\[
 \sum_s P_s(S_{\rm str})\le
 \sum_{r\ne0,1}
 \left|\{(Y,D)\in S_{\rm str}^2:1-Y=(1-r)(1-D)\}\right|^2
 \le E^\times(1-S_{\rm str}) .
\]
Indeed each choice of both pairs at fixed \(r\) specifies at most one physical tuple and slope \(s=AD/(CY)\), and the physical masks only decrease the count. Equivalently, for each shared \(r\), the row \(U_r(b)=g(Y)g(D)\) in \(b=(Y-r)/Y\) contributes its multiplicative autocorrelation at slope \(s\), because \(b/s=(A-r)/A\). The two pairs use the same restrictions when all four labels are required in \(S_{\rm str}\). The sum above is a first-mass bound on the genuine four-factor portion.

Partition the original positive kernel by taking the following restrictions as positive uppers for a cover. Use the counting triangle inequality with measure \(w\).
 
1. If any one argument has \(g<\tau\), send its role to \(C\) by swapping the two physical vertices, or by inverting the physical affine step \(u\) and exchanging its starting and ending arguments, or by composing those symmetries. The only change of slope is \(s\leftrightarrow1/s\), preserving \(w\) by inversion symmetry. With \(g(C)\le\tau\), the same Round 176 positive upper and its monomial-row bound give squared cost \(O(\tau^2 p^{37/16-1/4320})\) per role.
2. If any argument lies in \(S_{\rm small}\), send its role to \(A\) by the same symmetries. For the Round 176 output-first estimate on the remaining line family, the square root of the \(g(A)\) level size integrates to at most \(O(p^{1/4-\delta/2})\). This improves its leading coefficient \(p^{35/32-1/8640}\) by \(p^{-\delta/2}\). The other energy terms are at most their old \(O(p^{17/16})\) coefficient and the secondary term is also at most its old bound. The removed monomial row has squared cost \(O(p^{3/2})\), as before. Rearranging and using the actual \(w\) therefore gives \(O(p^{37/16-1/4320-\delta})\) per role.
3. For the all-\(S_{\rm str}\) kernel remove the same monomial row at squared cost \(O(p^{3/2})\). Its first mass stays \(O(p^\alpha)\). For the first \(\lfloor p^{63/128}\rfloor\) positions in its decreasing rearrangement, use the Round 176 output-first estimate, giving \(O(p^{37/16-1/4320-1/512}+p^{9/4})\) for the squared sum there. On later positions use \(O(p^\alpha/k)\) for the \(k\)-th value, giving squared sum \(O(p^{2\alpha-63/128})\). The latter exponent is below \(37/16-1/4320-1/512\) by \(737/898560>0\). These estimates also apply with the actual outer weight \(w\le1\). The first-mass argument uses all four memberships.

Since \(2\epsilon=\delta\), all three pieces fit the new whole bound, after restoring the priced physical boundary. It also bounds any positive distinct- or common-pole subpart, though the previous separate common-pole estimate is stronger. The sufficient \(O(p^{3/2})\) full bound remains open.

## Full weighted shifted row energies

The same extraction with different parameters gives a uniform bound on the actual shifted row energy for all weights. For just this purpose take \(\epsilon=3/418,\ \delta=1/418\). Put \(h(z)=g(1-z)\) on \(\mathbb F_p^\times\). The extracted part is bounded by its indicator in the positive energy, so the preceding general extraction expression gives exponent
\[
 \tfrac{18}{13}+\tfrac4{13}\max\{49\epsilon,36\epsilon+9\delta\}
 =\tfrac32-\tfrac3{418}.
\]
The leftover and the light part use \(E^\times(v)\le\|v\|_1^2\|v\|_2^2\) by Young's convolution inequality. For the leftover use \(|S_{\rm small}|^3=O(p^{3/2-3\delta})\), and for the light part use \(\tau G^3=O(p^{3/2-\epsilon})\). The fourth-root energy norm triangle inequality proves \(E^\times(h)=O(p^{3/2-3/418})\).

Consequently the true interior full-diagonal first mass and the squared \(r\)-row mass both have this scale. The first is bounded by the second by summing the row autocorrelations in \(s\). The parameter \(1-r\) then bounds the squared \(r\)-row mass by \(E^\times(h)\). The squared \(b\)-row mass has the same bound, since \(b=(1/Y-1)/(1/D-1)\) and \(g\) is inversion symmetric.

At any fixed \(a\ne0\), the first mass of the right correlation over \(c\) is \(\sum_r m_r m_{ar}\) for the actual \(r\)-row masses \(m_r\), at most \(\sum_r m_r^2\). This improves the fixed-\(a\) budget for the full weighted right correlation, and hence for the generic subcorrelation. Likewise the first mass of all pure dilations is bounded by the squared \(b\)-row mass. With the pointwise bounds of [Round 174](ordinary-affine-difference-pins-174.md), the nonidentity pure translation and pure dilation squared energies are at most \(O(p^{5/2-3/418-2/1280})\) and \(O(p^{5/2-3/418-1/1280})\), respectively. A transverse bound for the whole generic distribution still remains.

For either shared physical parameter \(r\) or \(b\), the positive common-row kernel at any output is bounded by the row mass \(m\), and its first mass over outputs is \(O(p^{1/2-1/1280}m)\) by the per-line estimate of [Round 173](ordinary-full-diagonal-two-pin-173.md). Its weighted squared norm is bounded by the same factor times \(m^2\), and summing the improved squared row masses gives \(O(p^{2-3/418-1/1280})\) for either whole common-parameter class.
