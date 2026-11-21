# Round 182 native Claude draft: shifted multiplicative energy of the actual level sets

- **call_id:** `ordinary-prime-shifted-level-energy`
- **agent_label:** `session/r182-shifted-energy`
- **Mission:** `coordination/missions/round-182/ordinary-prime-shifted-level-energy.md` (record `coordination/round-181.json`, SHA-256 `f237fdab…5c2d51`)
- **Inputs read (hashes matched the mission):** `research/round-180-acceptance.json`, `research/round-181-acceptance.json`, `research/native-claude-ordinary-prime-direct-first-mass-181.md`, `research/paley-181-first-mass-check.py`, `research/ordinary-paired-J-cross-ratio-180.md`, `research/ordinary-shifted-energy-four-factor-diagonal-177.md`, `research/ordinary-affine-triple-diagonal-179.md`. Also consulted (accepted, earlier rounds): Rounds 163, 173, 178.
- **Scripts:** `research/paley-182-shifted-energy-rowpair-check.py`, `research/paley-182-shifted-energy-exponents.py`, `research/paley-182-shifted-energy-logint.py`.
- Agent assessment only (native Claude research session). Not an audit, not human acceptance.

## Result summary

**Outcome: inconclusive for the target \(\mathcal M_w=O(p^{1+1/1280})\); supported for the secondary question (an exponent below 36/13).**

1. **Re-proved (Round 181 claim).** The exact row-pair formula for \(\mathcal M_w\) over \(\kappa=1-r\). The masks \(b\ne1\), \(s\ne b\) are vacuous, and \(s=1\) holds exactly on the diagonal pairs. Consequently \(\mathcal M_w\le\frac14(E_Q(h)-\text{diag})\le\frac14E^\times(h)\) with \(h(z)=g(1-z)\) (Proposition 1).
2. **New lemma, below 36/13.** Let \(B\subset\mathbb F_p\setminus\{0,1\}\) with \(|B|=N\le\sqrt p\). Let \(V\subset\mathbb F_p^\times\) with \(|V|=N\), and put \(K=|VB|/N\). Then
\[E^\times(1-B)\le C\,K^{2/3}N^{8/3}.\]
   The proof uses Stevens–de Zeeuw, Theorem 4. This replaces Round 177's \(K^{16/13}N^{36/13}\) (with \(V=B^{-1}\)) and is better in both \(N\) and \(K\) (Lemma SE). For log-intervals \(P_N\), the mission's first model, it gives \(E^\times(1-P_N)=O(N^{8/3})\) (Corollary SE).
3. **New, improves an accepted input.** BSG extraction carried out level by level with layer cake, plus Lemma SE, gives
\[E^\times(h)=O(p^{3/2-1/46})=O(p^{34/23}).\]
   Round 177 had \(O(p^{3/2-3/418})\) (Proposition 3). Two consequences:
   - the trivial multiplicative frequency of \(w\) costs \(O(p^{45/46})\) in \(\mathcal M_w\) (Proposition 2);
   - the squared \(r\)-row mass is \(O(p^{34/23})\).
4. **No improvement of \(\mathcal M_w\) itself.** \(\mathcal M_w\le E^\times(h)/4=O(p^{34/23})\) is still weaker than the existing \(O(p^{11/8})\).
5. **A method cap.** Suppose an argument extracts small-doubling BSG pieces of level sets, bounds each piece's shifted energy, and pays the light levels by Young's inequality. Then it cannot give better than \(E^\times(h)=O(p^{4/3})\), even with a sharp \(K\)-free piece lemma \(E^\times(1-B)\ll N^2\) (Proposition 4). The target needs a level-set input with no BSG size loss; that is criterion (b1).
6. **Evidence.** Shifted energies are near-sharp in every model tested, with \(E^\times(1-P)/N^2\in[2.2,3.5]\) and no visible power growth up to \(p\approx4\cdot10^6\). The models were:
   - generic log-intervals of \(Q\);
   - exact subgroups of order \(\approx\sqrt p\);
   - halves of subgroups of order \(\approx2\sqrt p\).

## Setup recalled

**Hypotheses on the actual weight.** These are accepted in Rounds 163, 173 and 178–180 and are used exactly as stated there.
- (H1) \(p\equiv1\pmod 4\) is an eligible prime. \(Q\) is the group of nonzero squares and \(n=|Q|=(p-1)/2\).
- (H1) \(\nu\) is the actual near-critical probability on \(\widehat Q\), and \(f(x)=\sum_{\eta\in\widehat Q}\nu_\eta\,\eta(x)\) on \(Q\), with \(f=0\) off \(Q\).
- (H1) \(g=|f|^2\). The cap is \(n\max\nu\le C_{\rm cap}\sqrt p\).
- (H2) \(0\le g\le1\), \(g(1)=f(1)^2=1\), \(\operatorname{supp}g\subseteq Q\), and \(G=\sum_xg(x)=n\sum\nu^2\le n\max\nu=O(\sqrt p)\).
- (H3) Inversion symmetry: \(g(1/z)=g(z)\). This is not needed below.
- (H4) \(w=g(1-g)\), so \(0\le w\le\min(g,1/4)\), \(w(1)=0\) and \(\sum_s w(s)\le G-1\).
- Counting norms are used throughout.

**Chart.** This is the chart of Rounds 178–180: \(s,b\in Q\setminus\{1\}\), \(r\in\mathbb F_p\setminus\{0,1\}\), \(s\ne b\), with labels
\[A=\frac{rs}{s-b},\quad C=\frac{rb}{(1-r)(s-b)},\quad Y=\frac{r}{1-b},\quad D=\frac{rb}{(1-r)(1-b)},\]
all required to lie in \(Q\setminus\{1\}\) (the nonzero interior). Then \(P_s=\sum_{(r,b)}g(A)g(C)g(Y)g(D)\) and \(\mathcal M_w=\sum_s w(s)P_s\).

**Shifted function and energies.**
- \(h(z)=g(1-z)\) for \(z\in\mathbb F_p^\times\), so \(h\) never sees \(x=1\).
- For \(v:\mathbb F_p^\times\to\mathbb R_{\ge0}\), put \(c_v(\kappa)=\sum_z v(z)v(\kappa z)\) and \(E^\times(v)=\sum_{\kappa\in\mathbb F_p^\times}c_v(\kappa)^2=\frac1{p-1}\sum_\chi|\hat v(\chi)|^4\), where \(\hat v(\chi)=\sum_z v(z)\chi(z)\).
- \(\mathcal N(v)=E^\times(v)^{1/4}\) is, up to a constant, the \(\ell^4\) norm of the Mellin transform. It is therefore a norm (triangle inequality and layer cake), and it is monotone on nonnegative functions.
- \(E_Q(h)=\sum_{\kappa\in Q\setminus\{1\}}c_h(\kappa)^2\).
- \(E^\times(1-S)=E^\times(1_{1-S})\).
- Level sets are \(S_t=\{x\ne1:g(x)\ge t\}\) (or \(>t\) in layer cake). Each has \(|S_t|\le G/t\).
- \(\Gamma_2=\sum_{x\ne1}g(x)^2\).

## Argument

### 1. Row-pair reformulation (Round 181 claim, re-proved)

**Proposition 1.** For \(\kappa\in\mathbb F_p\setminus\{0,1\}\) let \(R_\kappa=\{(Y,D)\in(Q\setminus\{1\})^2:\ 1-Y=\kappa(1-D)\}\) and \(\mu(Y,D)=g(Y)g(D)\). Then:
\[\mathcal M_w=\sum_{\kappa\in Q\setminus\{1\}}\ \sum_{P=(Y,D),\,P'=(A,C)\in R_\kappa} \mu(P)\mu(P')\,w\!\Big(\frac{AD}{CY}\Big).\]
In addition:
- (i) on \(R_\kappa\) the masks \(b\ne1\) and \(s\ne b\) are vacuous;
- (ii) \(s=AD/(CY)=1\) if and only if \(P=P'\);
- (iii) on each row, \(Y/D\) determines \(P\);
- (iv) \(\mathcal M_w\le\frac14\big(E_Q(h)-\sum_\kappa\sum_{P\in R_\kappa}\mu(P)^2\big)\le\frac14E^\times(h)\).

*Proof.*

*From the chart to rows.* From the labels,
\[1-Y=\frac{1-b-r}{1-b},\qquad 1-D=\frac{1-r-b}{(1-r)(1-b)},\]
so \(1-Y=\kappa(1-D)\) with \(\kappa=1-r\). Likewise \(1-A=\frac{s-b-rs}{s-b}=\kappa(1-C)\). The labels also give \(A/C=s(1-r)/b\) and \(Y/D=(1-r)/b\), hence \(s=(A/C)/(Y/D)\) and \(b=\kappa D/Y\). Since \(D,Y\in Q\), the condition \(b\in Q\) is equivalent to \(\kappa\in Q\).

*From rows to the chart.* Take \(\kappa\in Q\setminus\{1\}\) and \(P,P'\in R_\kappa\), and put \(r=1-\kappa\), \(b=\kappa D/Y\), \(s=AD/(CY)\). The row relation gives \(Y-\kappa D=1-\kappa\neq0\), so \(b\neq1\). Hence \(r/(1-b)=(1-\kappa)Y/(Y-\kappa D)=Y\), and similarly the formula for \(D\) holds. Next,
\[s-b=\frac{D(A-\kappa C)}{CY},\qquad A-\kappa C=1-\kappa\ne0 .\]
So \(s\ne b\) and \(rs/(s-b)=A\); the formula for \(C\) follows in the same way. The labels determine \((s,r,b)\) and conversely, so the correspondence is a bijection. The masks \(b\ne1\) and \(s\ne b\) hold automatically, which proves (i).

*(ii).* Suppose \(Y/D=A/C=\lambda\) on row \(\kappa\). Then \(1-\lambda D=\kappa-\kappa D\), so \(D(\kappa-\lambda)=\kappa-1\). The case \(\lambda=\kappa\) would force \(\kappa=1\). Otherwise \(D\) is determined by \(\lambda\), which gives both (ii) and (iii).

*(iv).* The diagonal carries \(w(1)=0\). Every other term has \(w\le1/4\), and \(\sum_{P,P'}\mu\mu'=c_h(\kappa)^2\), because \(\mu(Y,D)=h(1-Y)h(1-D)\) with \(1-Y=\kappa(1-D)\). ∎

The script checks (i)–(iv) and the identity exactly with Fractions at \(p=13,17,29,37,41\), also with an arbitrary weight in place of \(w\).

### 2. Multiplicative Fourier form of \(\mathcal M_w\) (retains \(w\))

**Proposition 2.** Let \(F_\kappa(\chi)=\sum_{P\in R_\kappa}\mu(P)\chi(Y/D)\) and \(\Phi(\chi)=\sum_{\kappa\in Q\setminus\{1\}}|F_\kappa(\chi)|^2\ge0\). Then
\[\mathcal M_w=\frac1{p-1}\sum_\chi\hat w(\chi)\Phi(\chi),\qquad
\mathcal M_w\le\frac{(G-1)\,E_Q(h)}{p-1}+\max_{\chi\ne1}|\hat w(\chi)|\cdot\sum_\kappa\sum_{P\in R_\kappa}\mu(P)^2 .\]
The last sum is at most \(\Gamma_2^2\).

*Proof.*
- Expand \(w(s)=\frac1{p-1}\sum_\chi\hat w(\chi)\bar\chi(s)\) with \(\bar\chi(s)=\bar\chi(A/C)\chi(Y/D)\). The double sum over a row then becomes \(|F_\kappa(\chi)|^2\).
- The trivial character gives \(\hat w(1)\Phi(1)/(p-1)\), with \(\hat w(1)\le G-1\) and \(\Phi(1)=E_Q(h)\).
- For the other characters, Parseval in \(\chi\) and Proposition 1(iii) give \(\frac1{p-1}\sum_\chi\Phi(\chi)=\sum_\kappa\sum_P\mu(P)^2\). ∎

With Proposition 3 below, the trivial frequency costs \(O(p^{1/2+34/23-1})=O(p^{45/46})\). This re-proves and improves the Round 181 claim \(O(p^{1-3/418})\). The nontrivial part needs \(\max_{\chi\ne1}|\hat w|\cdot\Gamma_2^2=O(p^{1+1/1280})\). That fails in subgroup-mixture models, where both factors are large (\(\approx\sqrt p\) and \(\approx p\)), so (b2) below is recorded only as a correct implication.

### 3. Structural lemmas about \(g\) and its level sets

These are stated for comparison with the sibling one-match session.

**Lemma S1 (hereditary multiplicative energy; Rounds 163/173, re-derived).** For \(t>0\) and any \(W\subseteq\{x\in Q:g(x)\ge t\}\),
\[E^\times(W)\ \ge\ \frac{t^2|W|^4}{n\max\nu}\ \ge\ \frac{t^2|W|^4}{C_{\rm cap}\sqrt p}.\]

*Proof.*
1. Choose unit \(e_x\) with \(e_xf(x)=|f(x)|\ge\sqrt t\). Then \(\sqrt t|W|\le\big|\mathbb E_{\eta\sim\nu}\sum_xe_x\eta(x)\big|\).
2. Jensen gives \(t^2|W|^4\le\mathbb E_\nu|\sum_xe_x\eta(x)|^4\le\max\nu\sum_{\eta\in\widehat Q}|\sum_xe_x\eta(x)|^4\).
3. By orthogonality, the last sum is \(n\) times a phase-weighted count of the quadruples \(x_1x_2=x_3x_4\), so it is at most \(nE^\times(W)\). ∎

**Lemma S2 (Fourier uniformity of the shifted weight; exact).** For every nontrivial multiplicative character \(\chi\) of \(\mathbb F_p^\times\),
\[\Big|\hat h(\chi)\Big|=\Big|\sum_{x\in\mathbb F_p\setminus\{0,1\}}g(x)\chi(1-x)\Big|\le\sqrt p,\qquad \hat h(1)=G-1 .\]

*Proof.*
- On \(Q\), \(g=\sum_\eta c_\eta\eta\) with \(c_\eta=\sum_{\eta_1\bar\eta_2=\eta}\nu_{\eta_1}\nu_{\eta_2}\ge0\) and \(\sum c_\eta=1\).
- Lifting \(1_Q\eta=\frac12(\psi_0+\psi_0\lambda)\), where \(\lambda\) is the Legendre symbol and \(\psi_0\) lifts \(\eta\), gives \(g=\sum_{\psi}a_\psi\psi\) on \(\mathbb F_p^\times\) with \(a_\psi\ge0\) and \(\sum a_\psi=1\). This expansion also vanishes correctly off \(Q\).
- Hence \(\hat h(\chi)=\sum_\psi a_\psi J(\psi,\chi)\), where \(J\) is the Jacobi sum and all characters vanish at \(0\). For \(\chi\ne1\), \(|J(\psi,\chi)|\in\{1,\sqrt p\}\). ∎

*Remark.* Round 181's hand-back said light levels "would need character-sum equidistribution, which is not available for a general \(g\)". Lemma S2 shows that this equidistribution is available for the actual \(g=|f|^2\). It gives \(E^\times(h)\le(G-1)^4/(p-1)+p\,\Gamma_2\). However, Young's inequality \(E^\times(v)\le\|v\|_1^2\|v\|_2^2\) already gives \((G-1)^2\Gamma_2\), which is at least as good whenever \(G\le\sqrt p+1\). So the obstruction at light levels is the Young barrier itself, not a missing character-sum estimate. Lemma S2 does not help below.

### 4. Shifted energy of sets with a small product set

**External input (checked against arXiv:1609.06284v4).** This is Stevens–de Zeeuw, Theorem 4, verbatim:

> "Let \(A,B\subset\mathbb F\) be sets with \(|A|=a\), \(|B|=b\), \(a\le b\) and \(ab^2\le n^3\). Let \(\mathcal L\) be a finite set of lines of size \(n\). If \(\mathbb F\) has positive characteristic \(p\), assume \(an\ll p^2\). Then \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\)."

The condition \(an\ll p^2\) means \(an\le c_0p^2\) for an absolute \(c_0>0\). The proof of the theorem goes through Rudnev's point–plane bound, which is used only inside it.

**Lemma SE.** Let \(B\subset\mathbb F_p\setminus\{0,1\}\) and \(V\subset\mathbb F_p^\times\) with \(|B|=|V|=N\le\sqrt p\), and put \(K=|VB|/N\ge1\). Then
\[E^\times(1-B)=\sum_{u\in\mathbb F_p^\times}m(u)^2\le C\,K^{2/3}N^{8/3},\qquad m(u)=\#\{(x,y)\in B^2:1-y=u(1-x)\},\]
with \(C\) absolute.

*Proof.*

*Lines, points and incidences.* For \((u,v)\in\mathbb F_p^\times\times V\), let \(\ell_{u,v}\) be the line \(Z=v(uX+1-u)\). The pair \((u,v)\) determines the slope \(vu\) and the intercept \(v(1-u)\). Their sum is \(v\ne0\), so \((u,v)\mapsto\ell_{u,v}\) is injective. For each row solution \((x,y)\) of \(u\) and each \(v\in V\), the point \((x,vy)\in B\times VB\) lies on \(\ell_{u,v}\). The map \((u,v,x,y)\mapsto(\ell_{u,v},(x,vy))\) is injective, because \(y=(vy)/v\). Part B of the script checks these injectivities exactly.

*Rich lines.* Let \(T_h=\{u\ne1:m(u)\ge h\}\) with \(t=|T_h|\), and use the lines \(\{\ell_{u,v}:u\in T_h,v\in V\}\), so \(n=tN\).
- Then \(I\ge hNt\). Take \(a=N\le b=KN\).
- The condition \(ab^2\le n^3\) is equivalent to \(K^2\le t^3\).
- Since \(\sum_u m(u)\le N^2\), we have \(t\le N^2/h\), hence \(an=N^2t\le N^4/h\le p^2/h\le c_0p^2\) once \(h\ge1/c_0\).
- If \(t\ge K^{2/3}\), Theorem 4 gives \(hNt\le C_1(K^{1/2}N^2t^{3/4}+tN)\). For \(h\ge2C_1\) this yields \(t\le16C_1^4K^2N^4/h^4\).
- Hence, for \(h\ge H_0:=\max(2C_1,1/c_0)\),
\[t(h)\le K^{2/3}+C_2K^2N^4/h^4 .\]

*Energy.* The row \(u=1\) contributes \(N^2\), and every \(m(u)\le N\). Split at \(H=\max(H_0,K^{2/3}N^{2/3})\):
- rows with \(m<H\) contribute at most \(HN^2\);
- for dyadic \(h_i=2^iH\le N\), the rows with \(m\in[h_i,2h_i)\) contribute at most \(4h_i^2t(h_i)\);
- summing gives at most \(6K^{2/3}N^2+6C_2K^2N^4/H^2\).

Therefore \(E^\times(1-B)\ll K^{2/3}N^{8/3}\). ∎

**Comparison.** With \(V=B^{-1}\), \(K=|B/B|/N\). Round 177's lemma is \(K^{16/13}N^{36/13}\) under the same \(N\le\sqrt p\), so Lemma SE improves both exponents (\(8/3<36/13\), \(2/3<16/13\)). This is the "exponent below 36/13" asked for in the mission.

**Corollary SE (log-intervals, subgroups).**
- Let \(P=\{\theta^k:k_0\le k<k_0+N\}\subset\mathbb F_p\setminus\{0,1\}\) with \(N\le\sqrt p\), and any \(\theta\). With \(V=\{\theta^{-k}\}\) over the same range, \(|VP|\le2N-1\), so \(E^\times(1-P)\le C2^{2/3}N^{8/3}\).
- The same bound holds for any \(B\) of size \(N\le\sqrt p\) contained in a coset \(xH\) of a subgroup with \(|H|\le KN\). Take \(V=x^{-1}B'\) for any \(B'\subseteq H\) with \(|B'|=N\); then \(VB\subseteq H\).

This does not reach the near-sharp \(N^{2+o(1)}\). That bound is supported numerically in Section (c) but not proved.

### 5. Layer-cake extraction for the actual \(h\)

**Proposition 3.** \(E^\times(h)=O(p^{3/2-1/46})=O(p^{34/23})\).

*Proof.* Fix \(\tau=p^{-\varepsilon}\) and \(\delta\), to be chosen below.

*Decomposition.* Write \(h=h_{<}+h_{\ge}\), splitting at \(g(1-z)<\tau\).
- The light part satisfies \(\mathcal N(h_<)^4\le\|h_<\|_1^2\|h_<\|_2^2\le G^2\cdot\tau G=O(p^{3/2-\varepsilon})\) by Young's inequality.
- For the heavy part, layer cake (a finite sum, since \(g\) takes finitely many values) and the triangle inequality for \(\mathcal N\) give
\[\mathcal N(h_{\ge})\le\tau\,\mathcal N(1_{1-S_\tau})+\int_\tau^1\mathcal N(1_{1-S_t})\,dt .\]

*Extraction at one level \(t\).* This repeats Round 177's construction at the single level \(t\):
- Repeatedly take \(M_j\) of size \(m_j=\min(\lfloor\sqrt p\rfloor,|\text{remainder}|)\) from the remainder of \(S_t\).
- Lemma S1 gives \(K_j:=m_j^3/E^\times(M_j)\le C_{\rm cap}\sqrt p/(t^2m_j)=Q_0/m_j\) with \(Q_0=C_{\rm cap}\sqrt p\,t^{-2}\).
- The Reiher–Schoen BSG form already used in the accepted Rounds 163, 173 and 177 gives \(B_j\subseteq M_j\) with \(|B_j|\gg m_jK_j^{-1/2}\) and \(|B_j/B_j|\ll K_j^4|B_j|\). The statement was not re-checked against the paper here, because the fetch failed; it is an accepted input of those rounds.
- Remove \(B_j\) and stop when the remainder \(S_t^{\rm small}\) has fewer than \(p^{1/2-\delta}\) elements.

*Price per point.* Lemma SE with \(V=B_j^{-1}\) gives
\[\mathcal N(1_{1-B_j})/|B_j|\ll K_j^{2/3}|B_j|^{-1/3}\ll K_j^{5/6}m_j^{-1/3}\ll Q_0^{5/6}m_j^{-7/6}.\]

*Two phases.*
- Phase 1 (\(m_j=\lfloor\sqrt p\rfloor\)): the total size is at most \(G/t\), so the contribution is \(\ll p^{1/3}t^{-8/3}\).
- Phase 2 (dyadic \(M\le m_j<2M\)): the removed mass is at most \(2M\). The terms sum to \(\ll Q_0^{5/6}p^{-(1/2-\delta)/6}=p^{1/3}t^{-5/3}p^{\delta/6}\).
- The leftover gives \(\mathcal N\le|S^{\rm small}_t|^{3/4}\le p^{3/8-3\delta/4}\).

*Integration.* Integrating over \(t\in[\tau,1]\) (the term \(\tau\mathcal N(1_{1-S_\tau})\) is of the same order):
\[\mathcal N(h)\ll p^{1/3+5\varepsilon/3}+p^{1/3+2\varepsilon/3+\delta/6}+p^{3/8-3\delta/4}+p^{3/8-\varepsilon/4}.\]
Take \(\delta=\varepsilon/3\) and \(\varepsilon=1/46\), so that \(1/3+5\varepsilon/3=3/8-\varepsilon/4=17/46\). The remaining term has exponent \(289/828<17/46\). Hence \(E^\times(h)=O(p^{68/46})=O(p^{34/23})\). ∎

**Ledger** (all values in `paley-182-shifted-energy-exponents.py`, exact Fractions):
- Round 177's own single-level accounting gives \(3/2-3/418\).
- Lemma SE at a single level gives \(3/2-1/70\).
- Round 177's lemma with layer cake gives \(3/2-3/314\).
- Lemma SE with layer cake gives \(3/2-1/46\).

**Consequences.**
- The squared \(r\)-row mass \(\sum_\kappa c_h(\kappa)^2\le E^\times(h)\) is \(O(p^{34/23})\). Round 177 notes that this quantity also bounds the interior full-diagonal first mass.
- The trivial frequency in Proposition 2 costs \(O(p^{45/46})\).
- \(\mathcal M_w\le E^\times(h)/4=O(p^{34/23})\) does **not** improve the existing \(\mathcal M_w=O(p^{11/8})\) (Round 180, by Cauchy–Schwarz against Round 179), since \(34/23>11/8\). Downstream exponents of Rounds 178–179 that used \(3/2-3/418\) were not re-derived here.

### 6. Why this route cannot reach the target

**Proposition 4 (method statement).** Suppose a per-piece bound has the form \(\mathcal N(1_{1-B})\le C K_j^c|B|^{\beta/4}\) and is fed into the extraction of Section 5. Put \(a=c+(1-\beta/4)/2\), which is the exponent of \(Q_0\) in the price per point.
- Phase 1 at level \(t\) costs \(p^{\beta/8}t^{-1-2a}\).
- After layer cake, the balance with Young's light part gives \(E^\times(h)=O(p^{3/2-\varepsilon})\) with \(\varepsilon=(3/8-\beta/8)/(2a+1/4)\).
- A sharp, \(K\)-free piece lemma (\(\beta=2\), \(c=0\)) still has \(a=1/4\), coming only from the BSG size loss \(|B_j|\gg m_jK_j^{-1/2}\). It gives \(\varepsilon=1/6\), that is, at best \(E^\times(h)=O(p^{4/3})\).

So even a perfect small-doubling lemma would give \(\mathcal M_w=O(p^{4/3})\), slightly better than \(11/8\), and never \(O(p^{1+1/1280})\). The loss sits in two places: the size loss of BSG, \(a>0\), and the Young bound on light levels. Reaching \(p^{1+o(1)}\) requires \(a=0\): a per-level bound \(E^\times(1-S_t)\le p^{o(1)}(|S_t|^2+|S_t|^4/p)\) for the whole level set, valid down to \(t=p^{-1/2}\) where \(|S_t|\) is up to \(p\). This is a statement about the bookkeeping of this route. It is not a lower bound for \(E^\times(h)\).

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here** (ordinary arguments; exact identities checked with Fractions or exact modular arithmetic at small \(p\)):
- (a1) Proposition 1: the row-pair reformulation, vacuous masks, \(s=1\iff P=P'\), \(Y/D\) injective on rows, and \(\mathcal M_w\le\frac14(E_Q(h)-\mathrm{diag})\le\frac14E^\times(h)\). This re-proves the Round 181 claim in full.
- (a2) Proposition 2: the multiplicative Fourier form of \(\mathcal M_w\) with \(w\) retained, and the trivial-frequency cost \(O(p^{45/46})\). This re-proves and improves the Round 181 claim \(O(p^{1-3/418})\).
- (a3) Lemma S1: hereditary energy \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\). Re-derived; accepted in Rounds 163/173.
- (a4) Lemma S2: \(|\sum_xg(x)\chi(1-x)|\le\sqrt p\) for \(\chi\ne1\). Exact. It is no stronger than Young's inequality for \(E^\times(h)\) when \(G\le\sqrt p+1\).
- (a5) Lemma SE: \(E^\times(1-B)\ll K^{2/3}N^{8/3}\) for \(N\le\sqrt p\), \(K=|VB|/N\). The input is Stevens–de Zeeuw, Theorem 4, with its hypotheses verified for these sets. This improves Round 177's \(K^{16/13}N^{36/13}\).
- (a6) Corollary SE: \(E^\times(1-P_N)\ll N^{8/3}\) for every log-interval with \(N\le\sqrt p\), and for subsets of small cosets.
- (a7) Proposition 3: \(E^\times(h)=O(p^{34/23})=O(p^{3/2-1/46})\). This improves Round 177's \(O(p^{3/2-3/418})\). It also bounds the squared \(r\)-row mass.
- (a8) Proposition 4 as a method statement: the BSG-plus-Young route caps at \(E^\times(h)=O(p^{4/3})\) even with a sharp piece lemma.

**(b) Conditional:**
- (b1) Suppose that for some \(\eta<1/1280\) and every \(t\in[p^{-1/2},1]\),
\[E^\times(1-S_t)\le Cp^{\eta}\big(|S_t|^2+|S_t|^4/p\big).\]
  Then \(E^\times(h)=O(p^{1+\eta}\log^4p)\), and so \(\mathcal M_w=O(p^{1+1/1280})\).

  *Proof.*
  - Young gives \(\mathcal N(h_{<p^{-1/2}})^4\le p^{-1/2}G^3=O(p)\).
  - By layer cake, \(\int_{p^{-1/2}}^1(Cp^\eta)^{1/4}\big((G/t)^{1/2}+(G/t)p^{-1/4}\big)dt\ll p^{\eta/4}p^{1/4}\log p\).

  With Round 180, this closes the classes \(J\in\{0,1\}\): \(\mathcal D_0+\mathcal D_1\le4R_*\mathcal M_w=O(p^{3/2})\). By the Round 180 bound \(\mathcal D_J\le2G\mathcal M_w\), it also gives each generic class at \(O(p^{3/2+1/1280})\). This re-proves the Round 181 conditional in a sharper form: only levels \(t\ge p^{-1/2}\) are needed, and the \(|S_t|^4/p\) term is allowed for large levels.
- (b2) If \(\max_{\chi\ne1}|\hat w(\chi)|\cdot\sum_\kappa\sum_{P\in R_\kappa}\mu(P)^2=O(p^{1+1/1280})\), then the target holds (Proposition 2). This is false in subgroup-mixture models, so it is not a viable route.

**(c) Evidence** (finite computations; exact integer counts per prime, but evidence only for the asymptotic question):
- (c1) `paley-182-shifted-energy-logint.py 4000000`. For log-intervals \(P_N\) of a generator of \(Q\) with \(N=\lfloor\sqrt p\rfloor\), \(E^\times(1-P_N)/N^2\) lies in 2.78–3.00 for \(p\) from \(10^3\) to \(4\cdot10^6\). This matches random subsets of \(Q\) (2.77–3.00). \(E/N^{8/3}\) decreases from 0.28 to 0.019.
- (c1) For exact subgroups \(H\) with \(|H|\approx\sqrt p\), \(E^\times(1-H)/|H|^2\) lies in 2.18–3.42 and \(E/(|H|^2\log|H|)\) decreases from 0.70 to 0.44. For halves of subgroups of order \(\approx2\sqrt p\), these are 2.52–3.53 and 0.76–0.37. The largest nontrivial row has at most 10 entries. No power growth is visible.
- (c2) `paley-182-shifted-energy-rowpair-check.py` part C (floating). For \(g=|f|^2\) built from random and interval probabilities \(\nu\) at \(p=29,53,101\):
  - \(\max_{\chi\ne1}|\hat h(\chi)|^2/p\le0.021\), consistent with Lemma S2;
  - the Proposition 2 inequality holds.
- The Round 181 floating evidence (\(\mathcal M_w/G^2\) in 0.047–0.096 for subgroup mixtures) is unchanged and was not re-run.

**Inputs not used.** Stepanov's method, Shkredov's Theorem 6 (arXiv:1504.04522) and Zhelezov's theorem are not used. In particular, the Round 181 coset-model claim is not re-proved here and remains unproved. Rudnev's point–plane theorem enters only through the proof of Stevens–de Zeeuw.

## Exact remaining gap

- **Target.** The target is \(\mathcal M_w=O(p^{1+1/1280})\). The best proved bound remains \(O(p^{11/8})\) (Round 180). The best bound through shifted energy is \(O(p^{34/23})\).
- **What closes it.** Criterion (b1): a per-level near-sharp bound \(E^\times(1-S_t)\le p^{\eta}(|S_t|^2+|S_t|^4/p)\) with \(\eta<1/1280\), for all levels \(p^{-1/2}\le t\le1\) of the actual \(g\). Equivalently, \(\mathcal N(1_{1-S_t})\le p^{\eta/4}(|S_t|^{1/2}+|S_t|p^{-1/4})\).
  - Heavy levels \(t\ge p^{-1/46}\), with \(|S_t|\le p^{1/2+1/46}\): the proved per-piece bound is \(K^{2/3}N^{8/3}\), which is above \(N^2\) by \(N^{2/3}\).
  - Intermediate levels \(p^{-1/2}\le t\le p^{-1/46}\), with \(|S_t|\) up to \(p\): only Young's bound is available, and Lemma S1's hereditary energy (\(K\approx t^{-2}\)) is too weak for BSG to give usable structure once \(t\le p^{-1/4}\).
- **Method cap.** By Proposition 4, no argument that passes through BSG pieces and Young can go below \(E^\times(h)=O(p^{4/3})\). The required input must treat whole level sets, with no size loss.
- **Unused retained weights.** The bound \(\mathcal M_w\le E^\times(h)/4\) discards \(w\) (keeping only \(w\le1/4\)). The fifth factor \(w(s)\) is used only in Proposition 2, where its nontrivial spectrum is not controlled.
- **Hypotheses used.** (H1)–(H4) only; inversion symmetry (H3) is not needed. Finite evidence, conditional criteria and proved statements are kept separate as above. No statement here proves the original ordinary theta-limit target.

## Two ranked next tests

1. **Whole-level shifted energy with no BSG loss (criterion b1).**
   - Prove or refute: if \(W\subseteq\mathbb F_p^\times\setminus\{1\}\) with \(|W|\le C\sqrt p/t\) satisfies the hereditary property \(E^\times(W')\ge t^2|W'|^4/\sqrt p\) for every \(W'\subseteq W\), then \(E^\times(1-W)\le p^{o(1)}(|W|^2+|W|^4/p)\).
   - Start numerically with admissible structured families beyond those in (c1): rank-two multiplicative progressions \(\{\theta_1^a\theta_2^b\}\), unions of short log-intervals in several subgroups, and Fejér level sets of \(g=|f|^2\) for interval \(\nu\). Look for power growth of \(E^\times(1-W)/|W|^2\).
   - A family with growth that is realisable as a level set of some \(g=|f|^2\) satisfying the cap would refute the positivity route. Note that a monotone sub-test is free: any \(B\) inside a coset \(xH\) of a subgroup with \(|H|\le\sqrt p\) has \(E^\times(1-B)\le E^\times(1-xH)\), so exact cosets are the extremal case of that family.
2. **Keep \(w\): the Fourier side of \(\mathcal M_w\).**
   - In subgroup-mixture and Fejér models, compute \(\Phi(\chi)=\sum_\kappa|F_\kappa(\chi)|^2\) on the large spectrum of \(w\), that is, on the \(\chi\) with \(|\hat w(\chi)|\ge p^{-\theta}G\).
   - If \(\Phi\) is \(O(p^{1/2+o(1)})\) there, then Proposition 2 with a spectral split would give \(\mathcal M_w=O(p^{1+o(1)})\) without any near-sharp energy for light levels. Proposition 4 shows that light levels are where the energy route must fail.
   - Report the exponent of \(\max_{\chi\in\mathrm{Spec}}\Phi(\chi)\) against \(p\).

## Replay

```bash
python3 -B research/paley-182-shifted-energy-rowpair-check.py
```
Output (rc 0, under 1 s, about 17 MB):
```
A p=13: chart==rows (6 tuples), masks vacuous, s=1<->P=P', Y/D injective, 4M_w=0.5749 <= E_Q-diag=0.7280 <= E^x(h)=13.4880  OK
A p=17: chart==rows (30 tuples), ... 4M_w=2.7036 <= E_Q-diag=7.7109 <= E^x(h)=33.9468  OK
A p=29: chart==rows (330 tuples), ... 4M_w=8.7119 <= E_Q-diag=20.0747 <= E^x(h)=112.0659  OK
A p=37: chart==rows (840 tuples), ... 4M_w=150.5739 <= E_Q-diag=203.5264 <= E^x(h)=609.3813  OK
A p=41: chart==rows (1224 tuples), ... 4M_w=0.0000 <= E_Q-diag=20.4688 <= E^x(h)=120.8296  OK
B p=31/61/101: incidence encoding injective, lines distinct  OK
C p=29 random  : max_chi!=1 |h^(chi)|^2/p = 0.0097 (<=1), M_w=0.0000 <= Fourier bound 0.0107; ...
C p=101 interval: max_chi!=1 |h^(chi)|^2/p = 0.0207 (<=1), M_w=0.0062 <= Fourier bound 0.6248; E^x(h)=1.051 <= ... 81.588
ALL OK
```

```bash
python3 -B research/paley-182-shifted-energy-exponents.py
```
Output (rc 0):
```
Round 177 lemma, single level (as in R177)   : E^x(h) = O(p^(312/209)) = p^(3/2 - 3/418)
Lemma SE, single level                       : E^x(h) = O(p^(52/35)) = p^(3/2 - 1/70)
Round 177 lemma + layer cake                 : a=18/13, eps=3/314, delta=1/314, E^x(h)=O(p^(234/157)) = p^(3/2 - 3/314)
Lemma SE (8/3) + layer cake                  : a=5/6, eps=1/46, delta=1/138, E^x(h)=O(p^(34/23)) = p^(3/2 - 1/46)
hypothetical sharp lemma N^2, K-free         : a=1/4, eps=1/6, delta=1/18, E^x(h)=O(p^(4/3)) = p^(3/2 - 1/6)
hypothetical: no BSG loss (a=0), beta=2      : E^x(h) = O(p^(1)) up to logs (the conditional route)
trivial multiplicative frequency of w: O(p^(45/46))  [Round 181 claimed 1-3/418]
route cap with a sharp K-free lemma: p^(4/3) < p^(11/8); target p^(1+1/1280) needs a=0
Lemma SE exponent algebra OK; SdZ hypothesis translation recorded
ALL OK
```

```bash
python3 -B research/paley-182-shifted-energy-logint.py 4000000
```
Output (rc 0, about 4 s; one array of \(p\) unsigned ints):
```
 p        N     E/N^2   E/N^(8/3)  E/N^(36/13) maxrow   | random: E/N^2  maxrow
    1009    31   2.7752    0.28123     0.19774      4   |   2.7732      6
    4001    63   2.8952    0.18286     0.11956      6   |   2.9113      8
   16001   126   2.9656    0.11800     0.07185      6   |   2.9398      5
   64013   253   2.9932    0.07483     0.04242      7   |   2.9832      7
  256021   505   2.9856    0.04708     0.02486      7   |   2.9827      8
 1000033  1000   2.9849    0.02985     0.01470      8   |   2.9989      8
 4000037  2000   2.9984    0.01889     0.00866      9   |   2.9965      9
 p        d     N    kind   E/N^2   E/(N^2 log N)  maxrow
    1009    24    23 sub     2.1834     0.6963         2
    1009    56    28 half    2.5204     0.7564         3
    4001    50    49 sub     2.5269     0.6493         4
    4001   125    62 half    2.8496     0.6905         5
   16001   100    99 sub     2.5556     0.5561         4
   16001   250   125 half    2.9254     0.6059         6
   64033   184   183 sub     2.4799     0.4760         5
   64033   464   232 half    2.8254     0.5187         6
  256021   502   501 sub     2.9653     0.4770         7
  256021  1255   627 half    3.5288     0.5479        10
 1000033   947   946 sub     2.8869     0.4213         7
 1000033  1894   947 half    2.8995     0.4231         8
 4000081  2381  2380 sub     3.4181     0.4396         9
 4000037  3413  1706 half    2.7258     0.3663         8
```
