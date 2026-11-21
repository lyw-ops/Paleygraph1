# Round 183 native Claude draft: the first mass as a fibre dilation correlation

- **call_id:** `ordinary-prime-first-mass-fibre-dilation`
- **agent_label:** `session/r183-fibre-dilation` (native Claude Opus 5.5 research session, started by the Round 183 coordinator session)
- **Mission:** `coordination/missions/round-183/ordinary-prime-first-mass-fibre-dilation.md`, exported from `coordination/round-182.json` (SHA-256 `bd56aa4c…dd40680f`, matched).
- **Inputs read (all SHA-256 values matched the mission):** `research/round-181-acceptance.json`, `research/round-182-acceptance.json`, `research/native-claude-ordinary-prime-shifted-level-energy-182.md`, `research/native-claude-audit-182.md`, `research/paley-182-audit-shifted-energy-check.py`, `research/ordinary-paired-J-cross-ratio-180.md`, `research/ordinary-mixed-row-autocorrelation-180.md`. Also `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-182.md`.
- **External input (new):** I. D. Shkredov, *On tripling constant of multiplicative subgroups*, arXiv:1504.04522**v1** (the only version), Theorem 6. It was read in the arXiv HTML rendering of v1 through a fetch subagent. The statement below is a transcription, not a verbatim quote (the fetch tool caps quotations), and the paper's proof (which the paper itself calls short, via its Proposition 3 and Remark 4) was **not** re-checked here. Rounds 181/182 cite this arXiv number as "Shkredov's Theorem 6" for coset models; this is the first time its statement is recorded with hypotheses.
- **Scripts:** `research/paley-183-fibre-identity-check.py` (exact), `research/paley-183-fibre-models.py` (floating), `research/paley-183-fibre-subgroup-energy.py` (exact integer counts).
- Agent assessment only. Not an audit, not human acceptance, not a mathematical certification.

## Result summary

**Outcome: inconclusive.** \(\mathcal M_w=O(p^{1+1/1280})\) is neither proved nor refuted. The fibre form does not by itself avoid the energy problem, but it localises it.

1. **Identity re-derived (Proposition A).** From the accepted Round 182 row-pair formula and the Round 171 chart, \(\mathcal M_w=\sum_r\sum_{b\ne b'}\mu(r,b)\mu(r,b')w(b/b')\). Equivalently, with \(h(z)=g(1-z)\),
\[\mathcal M_w=\sum_{\substack{x_1x_2=x_3x_4\\ x_3/x_2\in Q\setminus\{1\}}}h(x_1)h(x_2)h(x_3)h(x_4)\,w\!\Big(\frac{(1-x_3)(1-x_4)}{(1-x_1)(1-x_2)}\Big).\]
   This is the restricted multiplicative energy \(E_Q(h)\) with every energy quadruple weighted by \(w\). The fibre mass is \(m(\kappa)=c_h(\kappa)\). Checked exactly against the Rounds 178–180 chart at \(p=37,73,89\).
2. **Bounded fibres are free (Proposition B).** For every \(\tau\ge0\), \(\mathcal M_w\le\frac\tau4(G-1)^2+\frac14\sum_{m(\kappa)>\tau}m(\kappa)^2\). So the target follows from the **rich-fibre criterion** (RF): \(\sum_{\kappa:\,c_h(\kappa)>p^{1/1280}}c_h(\kappa)^2=O(p^{1+1/1280})\). Every fibre class of bounded (or \(p^{o(1)}\)) mass is closed. In all tested models the largest fibre grows slowly, like a logarithm or a small power: at most 17 points in the exact subgroup family at \(p\approx4\cdot10^6\), and weighted mass at most about 5 in the Fejér-type models at \(p\approx8\cdot10^4\).
3. **Keeping \(w\) gives only a constant in an admissible coset family (Proposition C).** For every subgroup \(H\le Q\), \(g_H=\delta_1+\frac14 1_{H\setminus\{1\}}\) is \(|f|^2\) for the probability \(\nu=\frac12\mathrm{unif}(H^\perp)+\frac12\mathrm{unif}(\widehat Q)\), with \(n\max\nu=(|H|+1)/2\). In this family, exactly,
\[\mathcal M_w(g_H)=\tfrac{3}{4096}E_{\rm off}(H)=\tfrac34\cdot\tfrac14\big(E_Q(h)-\mathrm{diag}\big).\]
   So any proof of the target from the recorded constraints (H1)–(H4) must prove a near-sharp shifted energy \(E_{\rm off}(H)=O(p^{1+1/1280})\) for every subgroup \(H\le Q\) with \(|H|\le2C_{\rm cap}\sqrt p-1\).
4. **Coset classes closed when \(|H|<\sqrt p\).** Shkredov's Theorem 6 gives \(\mathcal M_w\ll k^4\max_i|H_i|^2\log p\) whenever \(\operatorname{supp}g\) lies in \(k\) cosets \(\xi_iH_i\) with \(|H_i|^2<p\) (Corollary C2). This records Round 181's coset claim with a stated external input and the sharper hypothesis \(|H|^2<p\).
5. **Shifted cosets cannot sit in level sets (Proposition D, a level-set input).** If \(1+\xi\Gamma\subseteq S_t\), where \(\Gamma\) is a subgroup with \(|\Gamma|^2<p\), then \(|\Gamma|\ll t^{-1}(C_{\rm cap}\sqrt p\log p)^{1/2}\). Shifted cosets are what produce rich fibres of "coset type". Proposition D caps the energy this structure can force at \(O(p^{3/4}\log^{3/2}p)\), so this refutation mechanism is excluded.
6. **Two ways of keeping \(w\) are capped in the family \(g_H\)** (method statements, exact):
   - the Round 182 spectral route: on \(\operatorname{Spec}(w)=H^\perp\), \(\Phi(\chi)=\Phi(1)=E_Q(h)\gg|H|^2\), not \(O(p^{1/2+o(1)})\) (Proposition E);
   - every per-fibre Hölder bound \(\|w\|_q\sum_\kappa\|\nu_\kappa\star\tilde\nu_\kappa\|_{q'}\) is \(\gg|H|^{2+1/q}\). For \(q=2\), the per-fibre multiplicative energy, this is \(p^{5/4}\) (Proposition F).
7. **Floating evidence** (five admissible model families, \(p\) up to 80021) and **exact integer evidence** (\(g_H\), \(p\) up to \(4.1\cdot10^6\)):
   - \(\mathcal M_w/p\) stays bounded;
   - the \(w\)-saving factor \(\mathcal M_w/(E_{\rm off}/4)\) lies in 0.11–0.75 with no decay;
   - the per-fibre Hölder bound over \(p\) grows like \(p^{\approx1/4}\);
   - \(E_{\rm off}(H)/p\approx7\)–\(9\) for \(|H|\approx2\sqrt p\), i.e. near-sharp even outside Theorem 6's hypothesis.

**Where it fails (the inconclusive return).** The open class is the rich slope fibres \(\kappa\in Q\setminus\{1\}\) with mass \(c_h(\kappa)\in(p^{1/1280},R_*]\), where the multiplicative structure of the labels \(b\) is not controlled. There:
- the needed bound is \(\sum c_h(\kappa)^2=O(p^{1+1/1280})\);
- the verified bound is \(O(p^{34/23})\) (Round 182), with \(\mathcal M_w=O(p^{11/8})\) overall (Round 180).

Inside the exact coset subclass, the open part is subgroups with \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p-1\). There all observed fibres are bounded, and the verified bound is \(O(p^{4/3})\) (Lemma SE pieces). This subclass is empty if \(C_{\rm cap}<1/2\).

## Setup and hypotheses

The same as Round 182's shifted-level-energy report, used exactly as stated there.
- (H1) \(p\equiv1\pmod4\) is an eligible prime, \(Q\) is the group of nonzero squares, \(n=(p-1)/2\). \(\nu\) is a probability on \(\widehat Q\), \(f=\sum_\eta\nu_\eta\eta\) on \(Q\), \(f=0\) off \(Q\), \(g=|f|^2\). The cap is \(n\max\nu\le C_{\rm cap}\sqrt p\). For the actual near-critical \(\nu\), \(C_{\rm cap}\) is an unspecified absolute constant ("\(O(\sqrt p)\)" in Rounds 163–182).
- (H2) \(0\le g\le1\), \(g(1)=1\), \(\operatorname{supp}g\subseteq Q\), \(G=\sum g\le C_{\rm cap}\sqrt p\).
- (H4) \(w=g(1-g)\), so \(0\le w\le\min(g,1/4)\) and \(w(1)=0\).
- (H3), inversion symmetry, is **not** used anywhere below.
- Counting norms are used throughout.
- \(h(z)=g(1-z)\) for \(z\in\mathbb F_p^\times\), and \(c_h(\kappa)=\sum_z h(z)h(\kappa z)\).
- \(E^\times(v)=\sum_\kappa c_v(\kappa)^2\), and \(\mathcal N(v)=E^\times(v)^{1/4}\) is a monotone norm on nonnegative functions (Round 182, accepted).
- \(E_Q(h)=\sum_{\kappa\in Q\setminus\{1\}}c_h(\kappa)^2\). \(\Gamma_2=\sum_{x\ne1}g(x)^2\). \(S_t=\{x\ne1:g(x)\ge t\}\).

"Admissible" below means: satisfies (H1), (H2) and (H4) for some probability \(\nu\) with the stated cap. It is **not** a claim that the family is the actual near-critical optimiser. This is the class named by the mission's refutation clause ("consistent with the proved constraints on \(g\)").

## 1. The identity (re-derived; \(w\) kept)

**Round 171 chart.** \((Y,D)\in(Q\setminus\{1\})^2\), \(Y\ne D\), with
\[r=\frac{Y-D}{1-D},\qquad b=\frac{D(1-Y)}{Y(1-D)},\]
mask \(b\in Q\), and \(\mu(r,b)=g(Y)g(D)\).

**Proposition A.** Put \(\kappa=1-r\) and \(R_\kappa=\{(Y,D)\in(Q\setminus\{1\})^2:\ 1-Y=\kappa(1-D)\}\). Then:
- (A1) The fibre \(\{r\}\) of the chart is exactly \(R_\kappa\) when \(\kappa\in Q\setminus\{1\}\), and is empty otherwise. On it, \(b=\kappa D/Y\), and \(b\) determines \((Y,D)\).
- (A2) For \(P=(Y,D)\) and \(P'=(A,C)\) in \(R_\kappa\), \(b_P/b_{P'}=AD/(CY)=s\). Also \(s=1\iff P=P'\).
- (A3) \(\mathcal M_w=\sum_r\sum_{b\ne b'}\mu(r,b)\mu(r,b')w(b/b')=\sum_{\kappa\in Q\setminus\{1\}}\langle\nu_\kappa,\nu_\kappa*w\rangle\), where \(\nu_\kappa(b)=\mu(1-\kappa,b)\) and \(*\) is multiplicative convolution. The fibre mass is \(m(\kappa)=\sum_b\nu_\kappa(b)=c_h(\kappa)\).
- (A4) The four-variable form displayed in the summary holds.

*Proof.*

*(A1).* \(1-r=(1-D-Y+D)/(1-D)=(1-Y)/(1-D)=\kappa\), and
\[b=\frac{D(1-Y)}{Y(1-D)}=\frac{\kappa D}{Y}.\]
- Since \(D,Y\in Q\), the mask \(b\in Q\) holds exactly when \(\kappa\in Q\).
- With \(D\ne1\), \(Y\ne D\) holds exactly when \(\kappa\ne1\).
- Conversely, on \(R_\kappa\) we have \(Y-\kappa D=1-\kappa\ne0\), so \(b\ne1\), and
\[D=\frac{b(1-\kappa)}{\kappa(1-b)}\]
  is recovered from \(b\).

*(A2).* \(b_P/b_{P'}=(\kappa D/Y)/(\kappa C/A)=AD/(CY)\). By injectivity, \(b_P=b_{P'}\) iff \(P=P'\).

*(A3).* By (A1)–(A2), the right-hand side is \(\sum_{\kappa\in Q\setminus\{1\}}\sum_{P,P'\in R_\kappa}\mu(P)\mu(P')w(AD/(CY))\). The diagonal terms carry \(w(1)=0\). This is Round 182's Proposition 1 row-pair formula, accepted in Round 182. The fibre mass is \(m(\kappa)=\sum_{D}g(D)g(1-\kappa(1-D))=\sum_{z\ne0}h(z)h(\kappa z)\) with \(z=1-D\).

*(A4).* Put \(x_1=1-Y\), \(x_4=1-D\), \(x_3=1-A\), \(x_2=1-C\). Then:
- the two row equations say \(x_1=\kappa x_4\) and \(x_3=\kappa x_2\), i.e. \(x_1x_2=x_3x_4\) with \(\kappa=x_3/x_2\);
- conversely, \(x_1x_2=x_3x_4\) with all \(x_i\ne0\) defines \(\kappa=x_3/x_2=x_1/x_4\);
- \(g(Y)=h(x_1)\), and similarly for the other three labels;
- \(s=AD/(CY)=(1-x_3)(1-x_4)/((1-x_1)(1-x_2))\).

The exclusions \(Y,D,A,C\ne1\) are \(x_i\ne0\). Membership of the labels in \(Q\) is enforced by \(\operatorname{supp}g\). ∎

*Check.* Part I of `paley-183-fibre-identity-check.py` evaluates four expressions with exact Fractions at \(p=37,73,89\) (73 and 89 were not used in Rounds 181–182), with random rational \(g\) on \(Q\), \(g(1)=1\) and no symmetry. The four expressions are the chart sum over \((s,r,b)\) of Rounds 178–180, the fibre form, the row form and the four-variable form. They agree exactly. The script also checks injectivity of \(b\) on fibres and \(s=1\iff P=P'\).

**Retained weights.** Proposition A is an identity. It keeps \(w\), all four amplitudes, both masks and every exclusion.

## 2. Bounded fibres cost nothing (\(w\) majorized by 1/4 only)

**Proposition B.** For every \(\tau\ge0\):
\[\mathcal M_w(\kappa):=\langle\nu_\kappa,\nu_\kappa*w\rangle\le\tfrac14\big(m(\kappa)^2-\|\nu_\kappa\|_2^2\big),\qquad
\mathcal M_w\le\frac\tau4\,(G-1)^2+\frac14\sum_{\kappa\in Q\setminus\{1\}:\ m(\kappa)>\tau}m(\kappa)^2 .\]
Also \(\mathcal M_w\le\frac14\max_\kappa m(\kappa)\,(G-1)^2\), and \(\mathcal M_w\le\|w\|_1\sum_\kappa\|\nu_\kappa\|_2^2\le(G-1)\Gamma_2^2\).

*Proof.*
- The off-diagonal terms have \(w\le1/4\), which gives the first inequality.
- If \(m(\kappa)\le\tau\), then \(m^2\le\tau m\).
- \(M_1=\sum_\kappa m(\kappa)=\sum_{\rm masked}g(Y)g(D)\le(\sum_{x\ne1}g)^2=(G-1)^2\).
- For the last bound, \(\nu(b)\nu(b')\le\frac12(\nu(b)^2+\nu(b')^2)\) and symmetry give \(\langle\nu,\nu*w\rangle\le\|w\|_1\|\nu\|_2^2\). Also \(\sum_\kappa\|\nu_\kappa\|_2^2=\sum_{\rm masked}g(Y)^2g(D)^2\le\Gamma_2^2\). ∎

**Corollary B (conditional criteria; from (H2), \(G\le C_{\rm cap}\sqrt p\)).** Each of the following implies \(\mathcal M_w=O(p^{1+1/1280})\):
- (RF) \(\sum_{\kappa\in Q\setminus\{1\}:\,c_h(\kappa)>p^{1/1280}}c_h(\kappa)^2=O(p^{1+1/1280})\). A sufficient dyadic form is \(\#\{\kappa:c_h(\kappa)\ge\tau\}\ll p^{1+1/1280}/(\tau^2\log p)\) for \(\tau\ge p^{1/1280}\).
- (MF) \(\max_{\kappa\in Q\setminus\{1\}}c_h(\kappa)=O(p^{1/1280})\). The accepted bound is \(R_*=O(p^{1/2-1/1280})\) (Round 173), since \(c_h(\kappa)=\sum_Dg(D)g(\kappa D+1-\kappa)\) is an affine correlation with \(c=\kappa\ne0\), \(d=1-\kappa\ne0\).
- (G2) \(\Gamma_2=\sum_{x\ne1}g(x)^2=O(p^{1/4+1/2560})\). This is false in every model below (\(\Gamma_2/\sqrt p\in[0.03,0.66]\)).

(RF) is weaker than both (MF) and Round 182's (b1). The fibres with \(c_h(\kappa)\le p^{1/1280}\) are paid for in full by Proposition B. Within the BSG/Lemma SE bookkeeping, the split in the proof of Lemma SE at \(H=K^{2/3}N^{2/3}\) is exactly this split. The loss there comes from the middle range \(p^{o(1)}<c_h(\kappa)<N^{2/3}\), where Stevens–de Zeeuw gives \(\#\{\kappa:m\ge\tau\}\ll K^2N^4/\tau^4\). That count is above the needed \(N^2/\tau^2\) for every \(\tau<N\).

## 3. The admissible coset family: what keeping \(w\) can and cannot do

**Proposition C.** Let \(H\le Q\) be a subgroup with \(|H|\ge3\).
1. Put \(\nu=\frac12\mathrm{unif}(H^\perp)+\frac12\mathrm{unif}(\widehat Q)\), where \(H^\perp\) is the set of characters of \(Q\) trivial on \(H\). Then:
   - \(f=\frac12 1_H+\frac12\delta_1\), and \(g_H=|f|^2=\delta_1+\frac14 1_{H\setminus\{1\}}\);
   - \(n\max\nu=(|H|+1)/2\) and \(G=(|H|+3)/4\);
   - so \(g_H\) is admissible exactly when \(|H|\le2C_{\rm cap}\sqrt p-1\).
2. \(\mathcal M_w(g_H)=\frac{3}{4096}E_{\rm off}(H)\), where
\[E_{\rm off}(H)=\sum_{\kappa\in Q\setminus\{1\}}\big(c(\kappa)^2-c(\kappa)\big),\qquad c(\kappa)=\#\{(Y,D)\in(H\setminus\{1\})^2:1-Y=\kappa(1-D)\}.\]
   Moreover \(\frac14(E_Q(h)-\mathrm{diag})=\frac1{1024}E_{\rm off}(H)\), so the \(w\)-saving factor is exactly \(3/4\).

*Proof.*
1. By orthogonality on \(Q\), \(\sum_{\eta\in H^\perp}\eta(x)=|H^\perp|1_H(x)\) and \(\sum_{\eta\in\widehat Q}\eta(x)=n\,1_{x=1}\). This gives \(f\), hence \(g_H\). The largest atom of \(\nu\) is at the trivial character, \(\frac1{2|H^\perp|}+\frac1{2n}=\frac{|H|+1}{2n}\).
2. Every chart label with nonzero weight lies in \(H\setminus\{1\}\), so \(\mu(P)\mu(P')=4^{-4}\). Then \(s=AD/(CY)\in H\), and off the diagonal \(s\in H\setminus\{1\}\), so \(w(s)=\frac14\cdot\frac34\). Proposition A gives the count. ∎

Part III of the identity script checks (1)–(2) exactly for every subgroup of \(Q\) at \(p=73,89,97,101,109,113\).

**Corollary C1 (necessity; \(w\) kept).** Suppose an argument proves \(\mathcal M_w=O(p^{1+1/1280})\) using only (H1), (H2) and (H4) with cap constant \(C_{\rm cap}\). Then it proves \(E_{\rm off}(H)=O(p^{1+1/1280})\) for every subgroup \(H\le Q\) with \(|H|\le2C_{\rm cap}\sqrt p-1\).

In this family the fibre dilation correlation is \(3/4\) of the trivially majorized one, so keeping \(w\) gains a constant and nothing more. The reason is that every ratio \(b/b'\) inside a fibre falls in \(H\setminus\{1\}=\operatorname{supp}w\).

**External input (Shkredov, arXiv:1504.04522v1, Theorem 6; transcription).** Let \(\Gamma,\Pi\) be multiplicative subgroups of \(\mathbb F_p^*\) with \(|\Gamma||\Pi|<p\). Then for all \(x,y\ne0\),
\[E^\times(\Gamma+x,\Pi+y)\ll|\Gamma||\Pi|\log(\min\{|\Gamma|,|\Pi|\})+|\Gamma|^2+|\Pi|^2 .\]
With \(\Gamma=\Pi\) this reads \(E^\times(\Gamma+x)\ll|\Gamma|^2\log|\Gamma|\) for \(|\Gamma|^2<p\). The proof was not re-checked. Removing the point \(0\) from \(\Gamma+x\) can only decrease the count, so the bound applies to sets in \(\mathbb F_p^\times\).

**Corollary C2 (coset supports, \(|H_i|^2<p\)).** Suppose \(\operatorname{supp}g\subseteq\bigcup_{i\le k}\xi_iH_i\) with subgroups \(|H_i|^2<p\). Then
\[\mathcal M_w\le\tfrac14E^\times(h)\ll k^4\max_i|H_i|^2\log p .\]
In particular \(\mathcal M_w=O(k^4p\log p)\), which meets the target for bounded \(k\).

*Proof.*
- \(\mathcal M_w\le\frac14E^\times(h)\) is Round 182's Proposition 1(iv).
- Since \(0\le g\le1\), \(h\le\sum_i1_{1-\xi_iH_i}\) on \(\mathbb F_p^\times\).
- By monotonicity and the triangle inequality for \(\mathcal N\), \(E^\times(h)\le k^4\max_iE^\times(1-\xi_iH_i)\).
- Finally \(E^\times(1-\xi H)=E^\times(H-\xi^{-1})\), by the dilation \(z\mapsto-\xi^{-1}z\). Apply Theorem 6 with \(x=-\xi^{-1}\ne0\). ∎

This re-proves, from a stated input, the Round 181 coset-model claim (which Round 181 recorded as lost). The hypothesis it needs is \(|H|^2<p\).

**Corollary C3 (the coset subclass that stays open).** For \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\), Theorem 6 as stated does not apply. The best bound available here is
\[E_{\rm off}(H)\le E^\times(1-(H\setminus\{1\}))\ll_{C_{\rm cap}}p^{4/3}.\]

*Proof.*
- Split \(H\setminus\{1\}\) into \(k=\lceil(|H|-1)/\lfloor\sqrt p\rfloor\rceil\le2C_{\rm cap}+1\) pieces \(B_i\) of size \(N_i\le\sqrt p\), each \(\ge\lfloor(|H|-1)/k\rfloor\).
- Take \(V_i\subseteq H\) with \(|V_i|=N_i\). Then \(V_iB_i\subseteq H\) and \(K_i\le|H|/N_i=O(1)\).
- Lemma SE (Round 182, accepted) gives \(E^\times(1-B_i)\ll N_i^{8/3}\le p^{4/3}\).
- Combine the pieces by the triangle inequality. ∎

This subclass is nonempty only if \(C_{\rm cap}\ge1/2\). The exact counts in §6 show \(E_{\rm off}(H)/p\approx7\)–\(9\) for \(|H|\approx2\sqrt p\), up to \(p\approx4.1\cdot10^6\), with every fibre of size at most 17. That is evidence of near-sharpness, \(E_{\rm off}\ll|H|^2+|H|^4/p\) up to logarithms, not a proof.

## 4. A level-set input: shifted cosets inside level sets

**Proposition D.** Let \(t>0\), let \(\Gamma\le\mathbb F_p^\times\) be a subgroup with \(|\Gamma|^2<p\), let \(\xi\ne0\), and let \(W\subseteq S_t\cap(1+\xi\Gamma)\). Then
\[|W|^4\ll\frac{C_{\rm cap}\sqrt p\,|\Gamma|^2\log|\Gamma|}{t^2}.\]
In particular, if the whole shifted coset \(1+\xi\Gamma\) lies in \(S_t\), then \(|\Gamma|\ll t^{-1}(C_{\rm cap}\sqrt p\log p)^{1/2}\).

*Proof.*
- Lemma S1 (Rounds 163/173; re-derived in Round 182, audit CONFIRMED) gives \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\ge t^2|W|^4/(C_{\rm cap}\sqrt p)\).
- By monotonicity and dilation invariance, \(E^\times(W)\le E^\times(1+\xi\Gamma)=E^\times(\Gamma+\xi^{-1})\).
- Theorem 6 bounds the last quantity by \(\ll|\Gamma|^2\log|\Gamma|\). ∎

**Why it matters for the fibres.** If \(1+\xi\Gamma\subseteq S_t\), then \(T_\kappa(D)=1+\kappa(D-1)\) maps \(1+\xi\Gamma\) to itself for \(\kappa\in\Gamma\). So every \(\kappa\in(\Gamma\cap Q)\setminus\{1\}\) is a rich fibre with \(c_h(\kappa)\ge t^2(|\Gamma|-1)\). This is the coset-type rich fibre, the obvious way to make (RF) fail. The rich-fibre energy that this structure **forces**, about \(t^4|\Gamma|^3\), is by Proposition D at most
\[t^4|\Gamma|^3\ll t\,(C_{\rm cap}\sqrt p\log p)^{3/2}=O(p^{3/4}\log^{3/2}p).\]
So this mechanism cannot force \(\mathcal M_w\ge p^{1+\delta}\). This is a statement about the mechanism, not an upper bound on the actual fibres.

Proposition D says nothing about subsets of a shifted coset that are themselves only approximately structured, or about \(|\Gamma|\ge\sqrt p\). It does not bound \(\sum g^2\) (see the closeout note below).

## 5. Two ways of keeping \(w\) that are capped (method statements)

Both are exact statements about the admissible family \(g_H\) of Proposition C. They are statements about methods, not lower bounds for the actual \(\mathcal M_w\).

**Proposition E (spectral restriction; Round 182 next test 2).** Let \(\Phi(\chi)=\sum_\kappa|F_\kappa(\chi)|^2\) with \(F_\kappa(\chi)=\sum_{P\in R_\kappa}\mu(P)\chi(Y/D)\). This is Round 182's Proposition 2, accepted, over the characters of \(\mathbb F_p^\times\). For \(g_H\):
- \(\hat w(\chi)=\frac3{16}\big(|H|1[\chi|_H=1]-1\big)\). So for \(|H|>p^\theta+1\), the large spectrum \(\operatorname{Spec}_\theta(w)=\{\chi:|\hat w(\chi)|\ge p^{-\theta}\hat w(1)\}\) is exactly \(\{\chi:\chi|_H=1\}\).
- On it, \(\Phi(\chi)=\Phi(1)=E_Q(h)\), because every supported pair has \(Y/D\in H\) (checked in Part III).
- \(E_Q(h)\ge\sum_P\mu(P)^2\ge\frac1{256}\big(\frac12(|H|-1)^2-(|H|-1)\big)\). The \(Y\ne D\) pairs with \(\chi_2(1-Y)=\chi_2(1-D)\), where \(\chi_2\) is the Legendre symbol, number \(a^2+b^2-(|H|-1)\) with \(a+b=|H|-1\).

So \(\max_{\operatorname{Spec}}\Phi\gg|H|^2\asymp p\) for \(|H|\asymp\sqrt p\). The sufficient condition "\(\Phi=O(p^{1/2+o(1)})\) on \(\operatorname{Spec}(w)\)" therefore fails in an admissible family. In that same family the target is true when \(|H|^2<p\) (Corollary C2).

**Proposition F (per-fibre Hölder).** For \(1\le q<\infty\), Hölder in each fibre gives
\[\mathcal M_w\le\|w\|_q\sum_\kappa\|\nu_\kappa\star\tilde\nu_\kappa\|_{q'},\qquad (\nu\star\tilde\nu)(s)=\sum_b\nu(b)\nu(b/s).\]
For \(g_H\) the right side is at least
\[\tfrac3{16}(|H|-1)^{1/q}\sum_P\mu(P)^2\gg|H|^{2+1/q},\]
because \(\|\nu\star\tilde\nu\|_{q'}\ge(\nu\star\tilde\nu)(1)=\|\nu\|_2^2\).
- For \(q=2\), \(\|\nu\star\tilde\nu\|_2^2=E^\times(\nu_\kappa)\) is the per-fibre multiplicative energy, and the bound is \(\gg p^{5/4}\) at \(|H|\asymp\sqrt p\).
- Reaching \(p^{1+1/1280}\) this way needs \(q\ge640\), which is in effect the sup-bound of Proposition B.

## 6. Evidence

### 6.1 Floating models (`paley-183-fibre-models.py`; numpy float64; evidence about admissible models only, not about the actual optimiser)

Every model is \(g=|f|^2\) for an explicit probability \(\nu\) on \(\widehat Q\). Hence \(g(1)=1\), \(0\le g\le1\), and \(g\) is positive definite. The cap ratio \(n\max\nu/\sqrt p\) is printed.

| Model | \(\nu\) | Structure of \(g\) |
|---|---|---|
| `dir c` | uniform on \(L\approx n/(c\sqrt p)\) consecutive characters | Fejér-type log-interval kernel |
| `fej c` | triangular on \((-L,L)\) | Fejér\(^2\) |
| `sub` | \(g_H\) as in Proposition C | exact coset family |
| `mix2` | \(\frac12\mathrm{unif}(H_1^\perp)+\frac12\mathrm{unif}(H_2^\perp)\), \(|H_i|\approx\sqrt p\), \(\gcd\le2\) | two-subgroup mixture |
| `cosfej` | triangular on the multiples of \(s\approx p^{1/4}\) | invariant under the subgroup of order \(s\), a smeared coset \(H_sP\) |

Selected rows (full output in the replay section):

| model | p | cap | \(\mathcal M_w/p\) | \((E_{\rm off}/4)/p\) | saving | max \(m\) [pts] | share \(m\le2\) | Hölder\(_{q=2}\)/p | \(\max_{\rm Spec_{1/4}\setminus1}\Phi/\Phi(1)\) | \(\max_{\rm Spec}\Phi/\sqrt p\) |
|---|---|---|---|---|---|---|---|---|---|---|
| `dir c=0.5` | 2017 | 0.50 | 0.00179 | 0.00474 | 0.378 | 2.092 [3] | 0.706 | 0.046 | 0.967 | 2.7 |
| `fej c=0.5` | 2017 | 0.50 | 0.00059 | 0.00092 | 0.649 | 1.434 [3] | 1.000 | 0.018 | 1.000 | 1.1 |
| `dir c=1.0` | 2017 | 1.02 | 0.04079 | 0.13180 | 0.310 | 3.776 [11] | 0.571 | 0.371 | 0.880 | 29.4 |
| `fej c=1.0` | 2017 | 1.02 | 0.00720 | 0.01952 | 0.369 | 2.515 [3] | 0.761 | 0.139 | 0.993 | 8.1 |
| `sub ord H=42` | 2017 | 0.48 | 0.00015 | 0.00020 | 0.750 | 0.188 [3] | 1.000 | 0.002 | 1.000 | 0.1 |
| `sub ord H=84` | 2017 | 0.95 | 0.00398 | 0.00530 | 0.750 | 0.438 [7] | 1.000 | 0.015 | 1.000 | 1.2 |
| `mix2 38,54` | 2053 | 1.02 | 0.00110 | 0.00742 | 0.149 | 0.625 [7] | 1.000 | 0.022 | 0.363 | 0.6 |
| `cosfej s=6 c=0.5` | 2017 | 0.50 | 0.00003 | 0.00016 | 0.206 | 1.002 [1] | 1.000 | 0.018 | 1.000 | 0.9 |
| `cosfej s=6 c=1.0` | 2017 | 1.02 | 0.00637 | 0.01569 | 0.406 | 1.684 [5] | 1.000 | 0.138 | 0.993 | 7.4 |
| `dir c=0.5` | 20021 | 0.50 | 0.00241 | 0.00698 | 0.346 | 2.373 [3] | 0.934 | 0.100 | 0.990 | 11.3 |
| `fej c=0.5` | 20021 | 0.50 | 0.00046 | 0.00108 | 0.428 | 1.900 [3] | 1.000 | 0.042 | 1.000 | 4.3 |
| `dir c=1.0` | 20021 | 1.00 | 0.03901 | 0.11867 | 0.329 | 5.181 [14] | 0.534 | 0.651 | 0.962 | 94.2 |
| `fej c=1.0` | 20021 | 1.00 | 0.01027 | 0.02327 | 0.441 | 3.426 [8] | 0.807 | 0.267 | 0.999 | 28.8 |
| `sub ord H=130` | 20021 | 0.46 | 0.00021 | 0.00028 | 0.750 | 0.312 [5] | 1.000 | 0.004 | 1.000 | 0.4 |
| `sub ord H=286` | 20021 | 1.01 | 0.00584 | 0.00778 | 0.750 | 0.688 [11] | 1.000 | 0.034 | 1.000 | 5.5 |
| `mix2 110,182` | 20021 | 1.03 | 0.00127 | 0.00874 | 0.145 | 1.250 [17] | 1.000 | 0.037 | 0.337 | 2.1 |
| `cosfej s=10 c=0.5` | 20021 | 0.50 | 0.00045 | 0.00123 | 0.368 | 1.785 [3] | 1.000 | 0.042 | 1.000 | 4.4 |
| `cosfej s=10 c=1.0` | 20021 | 1.00 | 0.00954 | 0.02105 | 0.453 | 2.633 [4] | 0.801 | 0.261 | 0.999 | 27.3 |
| `dir c=0.5` | 80021 | 0.50 | 0.00279 | 0.00814 | 0.342 | 3.230 [8] | 0.853 | 0.147 | 0.995 | 24.5 |
| `fej c=0.5` | 80021 | 0.50 | 0.00077 | 0.00166 | 0.463 | 2.105 [5] | 0.977 | 0.063 | 1.000 | 9.8 |
| `dir c=1.0` | 80021 | 1.00 | 0.04214 | 0.12681 | 0.332 | 4.909 [13] | 0.477 | 0.946 | 0.981 | 202.5 |
| `fej c=1.0` | 80021 | 1.00 | 0.01167 | 0.02592 | 0.450 | 3.973 [6] | 0.718 | 0.395 | 1.000 | 61.7 |
| `sub ord H=262` | 80173 | 0.46 | 0.00026 | 0.00034 | 0.750 | 0.312 [5] | 1.000 | 0.006 | 1.000 | 0.9 |
| `sub ord H=557` | 80209 | 0.99 | 0.00532 | 0.00709 | 0.750 | 0.812 [13] | 1.000 | 0.044 | 1.000 | 10.2 |
| `mix2 262,306` | 80173 | 1.00 | 0.00084 | 0.00792 | 0.106 | 1.250 [17] | 1.000 | 0.048 | 0.284 | 3.2 |
| `cosfej s=17 c=0.5` | 80173 | 0.50 | 0.00058 | 0.00134 | 0.431 | 2.352 [5] | 0.988 | 0.061 | 1.000 | 9.3 |
| `cosfej s=17 c=1.0` | 80173 | 1.00 | 0.01058 | 0.02315 | 0.457 | 4.045 [5] | 0.827 | 0.382 | 1.000 | 57.8 |

`max m` is the weighted fibre mass, and [pts] is the number of entries at least 1% of the largest on that fibre. For `sub` each pair weighs 1/16, so 0.812 means 13 pairs. `ord H` is \(|H|\).

Readings (evidence only):
- \(\mathcal M_w/p\) is flat in \(p\) in every family. No power growth is visible, so nothing points towards refutation.
- The \(w\)-saving factor is bounded below: exactly 0.75 for `sub`, 0.11–0.16 for `mix2`, 0.21–0.65 for the Fejér-type families (0.32–0.47 for \(p\ge5000\)). It does not decay with \(p\). Keeping \(w\) buys a constant.
- The largest fibre mass grows slowly: `dir c=1` stays in 3.8–5.2 over a 40-fold range of \(p\). For \(m\le2\) the share of \(\mathcal M_w\) is 0.45–1.0. All of \(\mathcal M_w\) comes from fibres of mass \(\le8\).
- The per-fibre Hölder bound (\(q=2\)) divided by \(p\) grows like \(p^{0.25}\)–\(p^{0.29}\) (`dir c=1`: 0.37 → 0.95; `sub`: 0.015 → 0.044), as Proposition F predicts.
- On \(\operatorname{Spec}(w)\), \(\Phi\approx\Phi(1)\): the ratio is 0.88–1.00 except for `mix2`, where it is about 0.33. \(\max\Phi/\sqrt p\) grows like \(\sqrt p\). The spectral restriction over-counts (share > 1), because the off-spectrum part is negative.

### 6.2 Exact subgroup class (`paley-183-fibre-subgroup-energy.py`; exact integers)

| p | \|H\| | \|H\|/√p | E_off/\|H\|² | E_off/(\|H\|² log\|H\|) | max fibre c(κ) | E_off/p |
|---|---|---|---|---|---|---|
| 1021 | 30 | 0.939 | 0.3867 | 0.1137 | 3 | 0.3408 |
| 1009 | 63 | 1.983 | 1.7294 | 0.4174 | 8 | 6.8028 |
| 4013 | 59 | 0.931 | 0.3844 | 0.0943 | 5 | 0.3334 |
| 4001 | 125 | 1.976 | 1.7499 | 0.3624 | 8 | 6.8338 |
| 16001 | 125 | 0.988 | 0.4447 | 0.0921 | 5 | 0.4342 |
| 16001 | 250 | 1.976 | 1.8772 | 0.3400 | 10 | 7.3323 |
| 64033 | 232 | 0.917 | 0.3764 | 0.0691 | 5 | 0.3164 |
| 64033 | 464 | 1.834 | 1.6273 | 0.2650 | 11 | 5.4715 |
| 256021 | 502 | 0.992 | 0.4836 | 0.0778 | 7 | 0.4760 |
| 256033 | 1008 | 1.992 | 1.9794 | 0.2862 | 13 | 7.8551 |
| 1024321 | 970 | 0.958 | 0.4519 | 0.0657 | 7 | 0.4151 |
| 1024313 | 2099 | 2.074 | 2.1400 | 0.2798 | 16 | 9.2044 |
| 4096489 | 1947 | 0.962 | 0.4611 | 0.0609 | 7 | 0.4266 |
| 4096273 | 4197 | 2.074 | 2.1442 | 0.2570 | 17 | 9.2204 |

- For \(|H|\approx\sqrt p\), Theorem 6 applies at least for \(|H|<\sqrt p\). The counts are consistent with it: \(E_{\rm off}/(|H|^2\log|H|)\) decreases from 0.11 to 0.06.
- For \(|H|\approx2\sqrt p\), outside the theorem's hypothesis, \(E_{\rm off}/p\) stays between 5.5 and 9.3. The ratio \(E_{\rm off}/|H|^2\approx2\) is just the random term \(|H|^4/p\). The largest fibre has 8–17 points.
- In this family, \(\mathcal M_w(g_H)/p=\frac3{4096}E_{\rm off}/p\le0.007\).

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here** (ordinary arguments; the exact identities are checked with Fractions or integers at small \(p\)):
- (a1) Proposition A: the fibre form and the four-variable form of \(\mathcal M_w\), with \(w\) kept. Re-derived from the accepted Round 182 row-pair formula and the Round 171 chart, and checked against the original chart at \(p=37,73,89\).
- (a2) Proposition B: \(\mathcal M_w\le\frac\tau4(G-1)^2+\frac14\sum_{m>\tau}m^2\), \(\mathcal M_w\le\frac14\max m\,(G-1)^2\), and \(\mathcal M_w\le(G-1)\Gamma_2^2\). Here \(w\) is majorized by \(1/4\) in the first two and by \(\|w\|_1\) in the third.
- (a3) Proposition C: the admissible family \(g_H\) and the exact identity \(\mathcal M_w(g_H)=\frac3{4096}E_{\rm off}(H)\), with \(w\) kept. Corollary C1 (necessity) follows.
- (a4) Corollary C2: coset supports with \(|H_i|^2<p\) give \(\mathcal M_w\ll k^4p\log p\). This uses **Shkredov arXiv:1504.04522v1 Theorem 6** (transcribed, proof not re-checked) and Round 182's Proposition 1(iv), which majorizes \(w\le1/4\).
- (a5) Corollary C3: \(E_{\rm off}(H)\ll p^{4/3}\) for \(|H|\le2C_{\rm cap}\sqrt p\), from Lemma SE (Round 182, accepted).
- (a6) Proposition D: the level-set input \(|S_t\cap(1+\xi\Gamma)|^4\ll C_{\rm cap}\sqrt p|\Gamma|^2\log|\Gamma|/t^2\) for \(|\Gamma|^2<p\), from Lemma S1 and Theorem 6.
- (a7) Propositions E and F: method statements in the family \(g_H\). The spectral route has \(\Phi\gg|H|^2\) on \(\operatorname{Spec}(w)\), and per-fibre Hölder is \(\gg|H|^{2+1/q}\).

**(b) Conditional criteria:**
- (b1) (RF) ⇒ target. (MF) ⇒ target. \(\Gamma_2=O(p^{1/4+1/2560})\) ⇒ target, but this last one is false in all models.
- (b2) \(C_{\rm cap}<1/2\) ⇒ every exact coset family of Proposition C has \(|H|<\sqrt p\) and satisfies the target (Corollary C2). Whether it holds for the actual law is unknown.
- With Round 180: target ⇒ \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\) and \(\mathcal D_J=O(p^{3/2+1/1280})\). This is unchanged and re-stated, not re-proved.

**(c) Evidence.** §6.1 is floating evidence about five admissible model families. §6.2 is exact integer counts for the \(g_H\) family. Neither is evidence about the actual near-critical optimiser beyond the fact that these families satisfy the recorded constraints.

## Exact remaining gap

- **Target.** \(\mathcal M_w=O(p^{1+1/1280})\). The best proved bound is still \(O(p^{11/8})\) (Round 180). No headline exponent moves in this report.
- **Fibre class where the bound fails.**
  - Slopes: rich slope fibres \(\kappa\in Q\setminus\{1\}\) with \(c_h(\kappa)\in(p^{1/1280},R_*]\), where \(R_*=O(p^{1/2-1/1280})\).
  - Fibre size: more than \(p^{1/1280}\) weighted points on the line \(1-Y=\kappa(1-D)\) through \((1,1)\).
  - Multiplicative structure of \(b=\kappa D/Y\): arbitrary. The shifted-coset structure with \(|\Gamma|^2<p\) is excluded by Proposition D.
  - Needed: \(\sum c_h(\kappa)^2=O(p^{1+1/1280})\) over this class.
  - Verified: \(\le E^\times(h)=O(p^{34/23})\) (Round 182), and \(\le R_*(G-1)^2=O(p^{3/2-1/1280})\).
- **Why the fibre form does not help by itself.** Lines through \((1,1)\) form a pencil, and a pencil has no incidence saving: each point lies on one line of it. Lemma SE escapes by dilating by \(V\), which needs a small product set and hence BSG. Keeping \(w\) cannot replace this: in the admissible family \(g_H\), every in-fibre ratio lies in \(\operatorname{supp}w\), so \(w\) is worth exactly the constant \(3/4\) (Proposition C), and every finite-\(q\) norm of \(w\) loses a power (Proposition F).
- **Coset subclass.** It is closed for \(|H|<\sqrt p\) (Corollary C2) and open for \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\). There the verified bound is \(O(p^{4/3})\), and the exact counts are about \(9p\).
- **Hypotheses used.** (H1), (H2), (H4) and the cap. (H3) is not used. External inputs: Stevens–de Zeeuw Theorem 4 (through Lemma SE, Round 182) and Shkredov Theorem 6 (new here, transcription). No statement here proves the ordinary theta-limit target.

## Note for the closeout (shared-obligation check)

The only fibre-size or level-set inputs proved here are Proposition D (shifted cosets in level sets) and Proposition B (the bounded-fibre split, an elementary inequality).

Neither bounds \(\sum g^2\), and neither concerns the translation discrepancy of slope-closed six-words. So neither is the input the row-deleted one-match call needs.

The one shared **hypothesis** is the one Round 182's audit already identified, at a different scale:
- here \(\Gamma_2=O(p^{1/4+1/2560})\) would suffice (Proposition B);
- for (b1‴) any \(\Gamma_2=o(\sqrt p)\) relaxes the one-match target.

The object \(\mu\) is shared. Here its slope-fibre masses enter with a **plus** sign (\(\sum_{\rm rich}m^2\)). In the one-match trace identity, \(\sum_r m(r)^2=T_1^\times(m)\) is subtracted.

## Two ranked next tests

1. **Rich-dilation count for level sets (criterion RF).** Prove or refute, for \(W\) a level set of an admissible \(g\) (the hereditary-energy property of Lemma S1, \(|W|\le C\sqrt p/t\)):
\[\#\{\kappa\ne1:\ |W\cap T_\kappa^{-1}W|\ge\tau\}\ll p^{o(1)}\,\frac{|W|^2}{\tau^2},\qquad \tau\ge p^{o(1)}\max(1,|W|^2/p),\]
where \(T_\kappa(D)=\kappa D+1-\kappa\).
   This is a "rich lines through one point" statement for \(W\times W\). The transfer from level sets to (RF) for \(h\) through layer cake is not done here. It would cost at least logarithms, and probably a level-pairing argument, since \(c_h(\kappa)\ge\tau\) does not localise to a single level. It is the exact place where both Lemma SE (via dilations and BSG) and the fibre form stall. A first test: exact counts of \(\max_\kappa|W\cap T_\kappa^{-1}W|\) and of the rich-count profile for level sets of the `dir`/`cosfej` models at \(p\ge10^6\) (the sparse level sets make this cheap). Look for power growth of the maximal fibre.
2. **Close the exact coset subclass \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\).** Either extract an explicit \(C_{\rm cap}<1/2\) from the near-critical construction (then Corollary C2 closes it), or find a published shifted-subgroup energy bound valid for \(|\Gamma|\le C\sqrt p\). Shkredov–Vyugin, Mat. Sb. 203:6 (2012), and Mit'kin's incidence lemma are the candidates. Fetch and quote the exact hypotheses before use.

## Replay

```bash
.venv/bin/python -B research/paley-183-fibre-identity-check.py
```
(rc 0, about 1 s, standard library only). The output ends:
```
I  p=89: chart == fibre == row == four-variable form, M_w=129.478922; b injective on fibres; s=1 <-> P=P'  OK
II p=89: M_w(kappa) <= (m^2-|nu|^2)/4 on every fibre; M_w <= tau M_1/4 + sum_(m>tau) m^2/4 for tau in {0,1/2,1,2,4,max m}  OK (M_1=208.9722, max m=6.9722)
III p=113 |H|= 56: M_w = (3/4096) E_off(H) = 27.250488 (E_off=37206); g_H = |f|^2 exact; n*max(nu) = 28.50; Y/D in H on support  OK
ALL OK
```

```bash
.venv/bin/python -B research/paley-183-fibre-subgroup-energy.py 4100000
```
(rc 0, a few seconds, peak about 680 MB). Output: the table in §6.2.

```bash
.venv/bin/python -B research/paley-183-fibre-models.py 2000,5000,10000,20000,40000,80000
```
(rc 0, 9 min wall clock on this machine, peak about 3198 MB; floating). It prints one line per model and prime: a header and 60 model lines for the six target primes. The table in §6.1 selects the rows at p≈2000, 20000, 80000, with columns m≤2 share, Hölder (q=2) and the θ=1/4 spectral columns. Smaller arguments, such as `2000,5000`, give a quick replay.

## Verdict

**Inconclusive.** The fibre dilation form keeps \(w\) and every amplitude (Proposition A), but in the admissible coset family \(w\) is worth exactly \(3/4\) (Proposition C).

The bounded-fibre classes are closed outright (Proposition B). Exact coset supports with \(|H|^2<p\) are closed by Shkredov's Theorem 6 (Corollary C2). Coset-type rich fibres are excluded by Proposition D.

The bound fails on:
- the rich slope fibres \(c_h(\kappa)>p^{1/1280}\) with uncontrolled multiplicative structure of \(b\): needed \(\sum c_h^2=O(p^{1+1/1280})\), verified \(O(p^{34/23})\), with \(\mathcal M_w=O(p^{11/8})\) overall;
- the exact subgroups with \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\): needed \(O(p^{1+1/1280})\), verified \(O(p^{4/3})\), observed about \(9p\).

No admissible family with power growth of \(\mathcal M_w/p\) was found.
