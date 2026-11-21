# Round 180 independent audit

Auditor: Claude (agent audit, adversarial). This is not human acceptance or mathematical certification. No repository file was modified.

My own scripts are in `scratchpad/audit180/`: `a1.py`, `a2.py` and `a3.py`. They use pure python3 with exact modular arithmetic, `fractions` and `decimal`. NumPy is absent, so none of the candidates' NumPy model or FFT runs were re-run. Every claim that rests on those runs stays (c), unverified by me.

## Sources read

- `coordination/round-179.json`
- `coordination/missions/round-180/cold-prime-signed-growing-prefix.md`
- `research/round-179-acceptance.json` (head)
- Ordinary-route notes, in full:
  - `ordinary-weighted-slope-product-incidence-178.md`
  - `ordinary-parabolic-row-mean-square-178.md`
  - `ordinary-affine-triple-diagonal-179.md`
  - `ordinary-weighted-affine-vertical-saving-173.md`
- Ordinary-route notes, relevant parts only:
  - `ordinary-shifted-energy-four-factor-diagonal-177.md` (head, and lines 91–95)
  - `ordinary-affine-line-energy-171.md` (chart)
  - `ordinary-two-torus-projective-overlap-176.md` (lines 39–61)
  - `ordinary-full-diagonal-two-pin-173.md` (line 76)
- Cold-route notes, in full:
  - `cold-fixed-counting-source-obstruction-179.md`
  - `cold-logarithmic-finite-tube-173.md`
  - `cold-seed-centered-larger-tube-177.md`
  - `cold-height-602-frozen-kernel-162.md`
  - `astra-dissipation-80.md`
- Cold-route notes, relevant parts only:
  - `astra-direction-83.md` (lines 1–68)
  - `cold-first-prefix-step-174.md` (the line that gives 0.01272)
- Stevens–de Zeeuw: I read the text of arXiv:1609.06284v4 in `r180/pdf/sdz.txt`, including the Theorem 4 statement (lines 110–113), Theorem 6 (Rudnev), and the proof of Theorem 4 (lines 260–305). The research agent extracted that file. I did not fetch the paper independently. The text is internally consistent and matches the statement as I know it.

---

## Report 1: mixed row autocorrelation and the slope-product sum

### R1.1 Lemma: sup over λ≠1 of C(λ) = O(p^{11/8}). Verdict: CONFIRMED

**Chart and completion.** These agree with the Round 171 chart: r=(Y−D)/(1−D), b=D(1−Y)/(Y(1−D)), and Y=r+(1−r)D. Hence m ≤ m♯ ≤ G pointwise.

**Line family.** The line is (1−D3)(X−D1)=λ(1−D1)(Z−D3). Its slope is nonzero and finite. It passes through (D1,D3) and meets Z=1 at X=λ+(1−λ)D1.
- I verified by hand that the line determines (D1,D3).
- I checked exhaustively at p=13, 17, 29, 37 and every λ∉{0,1}: the lines are distinct, and each meets every row and every column exactly once (`a1.py`).

**Each variable is determined by the other three.**
- By hand: the D1-coefficient vanishing forces Y1=1. The D3-coefficient vanishing leaves the constant (Y1−D1)(1−Y3)≠0.
- Exhaustively at p=13 to 37, over all tuples of Ω_λ: no two tuples agree in any three coordinates.
- The identity C♯(λ)=Σ_r m♯(r)m♯(λr) equals the tuple sum exactly, with random integer weights.
- Σ_λ C² = Σ_ξ W² holds exactly for the masked m.

**Stevens–de Zeeuw Theorem 4.** The statement is exactly as quoted:
- hypotheses a≤b, ab²≤n³, and an≪p²;
- conclusion I ≪ a^{3/4}b^{1/2}n^{3/4}+n.

In the proof, A is the x-coordinate set (vertical lines are removed). The swap of coordinates when |U1|>|U3| is therefore needed, and it is valid. The lines are also non-horizontal.

**Complement case ab²>n³.** I ≤ an. I checked by hand that an ≤ a^{3/4}b^{1/2}n^{3/4}, using a≤b. This is the same device as SdZ's own b²>an step.

**Other steps.**
- min^{3/4}·max^{1/2} ≤ (ab)^{5/8}: correct.
- The layer cake g1_{g>τ}=∫1[g>max(t,τ)]dt is correct. |U(t)| ≤ G/τ, and Jensen gives ∫|U|^θ ≤ G^θ.
- an ≤ (G/τ)³ = O(p^{15/8}) ≤ c·p² for large p.
- The light-part bound is ≤ Σ_i (role i light) ≤ 4τG³, by the determination property.
- Exponents: G^{11/4} = τG³ = p^{11/8}.

### R1.2 E^×(m)=O(p^{27/8}). Verdict: CONFIRMED

E^× ≤ C(1)² + sup·M1², with C(1) ≤ G·M1 ≤ G³.

### R1.3 Σ_ξ W_ξ^{3/2} ≤ M1·E^{1/2} = O(p^{43/16}). Verdict: CONFIRMED

The gain 197/3344 was checked with `Fraction`. W_ξ is monotone in the weight, so the bound holds for Round 178's reduced weight.

### R1.4 Propagation through Round 178. Verdict: CONFIRMED

Round 178's per-ξ bound is O(W_ξ²/p + W_ξ^{3/2} + G(1+log p)W_ξ), with the same W_ξ as the mass of both points and planes. The energy therefore depends on the ξ-distribution only through ΣW²/p, ΣW^{3/2} and ΣW=M1². The substitution is verbatim.

| Quantity | Exponent | Check |
|---|---|---|
| 𝓔(μ) | 43/16 | 19/8 and 5/2+log are smaller |
| H_α second norm | 147/128 | 5/16+43/128+1/2 |
| Σ w\|H\|² | 179/64 | |
| One-match covariance | 115/64 | gain 197/13376 |

All these exponents were checked exactly. The match with Round 178's E(μ_*)=O(p^{43/16}) is correct.

### R1.5 Limits of the route. Verdict: CONFIRMED-WITH-CORRECTION

The inequalities are correct:
- ΣW^{3/2} ≥ M1³/√(p−1), by Jensen over p−1 values of ξ.
- 𝓔 ≥ M1⁴/(p(p−1)), by Cauchy–Schwarz over |Aff|.

The threshold "M1 ≫ p^{7/8+ε}" mixes two normalizations. It keeps the cap M1≤p in the linear M1 factor of the output p^{1/8}·E^{1/4}·M1, but uses the actual M1 in E ≥ M1⁴/p².
- If the actual M1 is kept throughout, the obstruction threshold is M1 ≫ p^{15/16}.
- Both versions give p^{13/8} when M1≍p.
- M1≍p itself is not known.

The final "Equivalently Σ_h Δ(h)(m_U−|U|²/p)=O(p²)" and the level-bound reformulation are asserted, not proved. Read them as sufficient heuristics, not equivalences.

### R1.6 Fixed-slope corollary. Verdict: CONFIRMED

Σ_c Δ(a,c) = Σ_r m_r m_{ar} is stated in Round 177 (line 93) and Round 176 (line 59). Round 176's generic maximum is for a,c≠0 and a≠1. Multiplying gives the exponent 19/8−1/1280−1/840.

### R1 (c) evidence. Verdict: NOT RE-RUN

NumPy is unavailable. My exact checks replace the "exact" part. The synthetic-weight FFT figures are unverified and are not the actual g.

---

## Report 2: paired J fibres

### R2.1 J is a cross-ratio, and h_k = j_{e'}∘j_e^{-1} is independent of s. Verdict: CONFIRMED

**Labels.** I checked that Lemma 1's labels agree with the Round 178 chart (parabolic note, "at fixed s,k" display, with k=r/b and u=1/b): A=rs/(s−b), C=rb/((1−r)(s−b)), Y=r/(1−b), D=rb/((1−r)(1−b)).

**Exact checks** (`a2.py`):
- p=13, 17, 29: all ordered pairs of interior lines at every s, about 10⁷ pairs.
- p=101: 2·10⁵ random pairs.
- For each pair I computed k=(x'−v')/(x−v) and d=v'−kv directly from Round 179's definitions. J = d(k+d−1)/k equals [π';π,ρ,ρ'] in every case.
- Lemma 1 holds in every case.
- Round 179's companion u' = v'+(λ/k)(u−v) also holds.

### R2.2 Exact characterization of J=0 and J=1. Verdict: CONFIRMED

J=0 ⇔ π'=π or ρ'=ρ, and J=1 ⇔ π'=ρ or ρ'=π. These held as exact equivalences on all the pairs above. The algebra J−1=(d−1)(d+k)/k was checked by hand.

### R2.3 𝓓0+𝓓1 ≤ 4R_*𝓜_w = O(p^{2399/1280}). Verdict: CONFIRMED-WITH-CORRECTION

**R_*.** Round 173 proves |X| = O(p^{1/2−1/640}) for X={g(x),g(Tx)≥τ}, τ=p^{−1/1280}, uniformly in cd≠0. The split then gives R_* = O(p^{1/2−1/1280}). This matches two-pin-173 line 76.

**Rows.** 1/D' = πz+1−π and 1/A' = cz+1−c, with c=(X−ρ)/(1−ρ)∉{0,1}. I checked both exhaustively at p=101 over interior (π,ρ,X). Inversion symmetry g(z)=g(1/z) is stated in two-pin-173, and w=g(1−g) in Round 171/177.

**𝓜_w.** Σw ≤ G holds since w ≤ g. Round 179 proves Σ_s w P_s² = O(p^{9/4}) for the whole diagonal, endpoints included, and the interior P_s is smaller. Hence 𝓜_w ≤ G^{1/2}·p^{9/8} = O(p^{11/8}).

**Exponents.** 2399/1280 is correct, as are the superseded 2429/1280, 2439/1280 and 243/128 (`a3.py`). The file's corrected version is consistent.

**Correction.** The headline "w, D and the whole first copy are kept" is true only for the Prop. 5 step. The factor 𝓜_w comes from Round 179, which bounds D, D', the masks and w by one internally. The final bound therefore does not retain D and w in the mission's sense. The report's Section 5 table discloses this, but the summary bullet overstates it.

### R2.4 Each generic 𝓓_J ≤ 2G𝓜_w = O(p^{15/8}), and these do not sum. Verdict: CONFIRMED

**Lemma 8.**
- The identity αβ−πρ = J(1−J)(ρ−π)² was checked by hand.
- (u+β)(t+α) − c with c≠0 is absolutely irreducible.
- Exhaustively at p=29 and 37, over all lines and all J∉{0,1}, each value 1/Y' occurs at most twice in a fibre.

The non-summability remark is correct.

### R2.5 Criterion 7 (b). Verdict: CONFIRMED

The arithmetic checks out:
- 4R_*·p^{1+1/1280} = O(p^{3/2}).
- 𝓓=O(p^{3/2}) implies 𝓜_w=O(p).
- The generic class would become p^{3/2+1/1280}.

### R2.6 Normal form (Section 4.2). Verdict: CONFIRMED

At every generic pair above, I checked:
- all eight table entries;
- the recovery formulas for X, π, ρ and π';
- that the z's are distinct and avoid {0,1,J}.

By hand I checked that the map is onto: γ⁻¹ is a bijection of ℙ¹, so the eight images are distinct. Only (c)-type remarks depend on the unchecked model runs.

---

## Report 3: signed growing prefix (cold route)

### R3.1(a) Upper bound: limsup over p, sup over Q of ‖R_602‖_{2,n} < 9.07·10^{-209}. Verdict: CONFIRMED-WITH-CAVEAT

**Round 80's statement.** Round 80 states verbatim that the "complex normalized residual at that row [600] has limsup at most 4(0.449922)^{600}".
- This is for physical rows from the nine-center start.
- It uses the complex-square factor (b=B=1.94 caps), fixed-prefix transfer "on the closed square", vanishing physical-mark correction, and uniformity in the limsup over the floor.
- It is therefore a physical, complex-square, limsup (ineffective) statement, not merely a statement about the compact or real floor.
- The indexing matches: R_600 = V_601−V_600, R_600 is priced at 0.011, and R_601 at 0.012 (Rounds 126 and 162).

**Steps 600→602.** Round 177's seed-centred derivative bound needs |z−S_i| ≤ 2.338. The segments have |z−S_i| ≤ 1.94+0.011+0.012=1.963 (Round 177's own display), and the mark derivative is O(n^{−1/2}). This step holds pointwise for large p.

**Constants.** Recomputed with 60-digit decimals:
- 4·0.449922^{600} = 3.0507·10^{−208};
- multiplied by 0.545², this gives 9.0613·10^{−209} < 9.07·10^{−209}.

**Caveat.** Round 80's text does not explicitly say "both lifts" for this residual. Round 179's later transfer does, and Round 162's estimates are stated uniform over both lifts, so the inheritance is consistent but not verbatim.

### R3.1(a) Lower bound: liminf over p, inf over Q of ‖R_602‖_{2,n} > 0. Verdict: CONFIRMED

Round 179 proves the normalized bound liminf inf_Q ‖R_611‖_{2,n} > 0. Round 177 keeps V_602 through V_612 inside the 3/8 polydisks. Hence ‖R_611‖ ≤ 0.545⁹‖R_602‖ pointwise, and the inequalities point the right way.

**Wording.** The summary says Round 179's c√n lower bound "applies only to the unnormalized counting norm". This misreads Round 179: its primary statement is the normalized liminf, and c√n is its unnormalized corollary. The proof in §1 uses Round 179 correctly.

### R3.2(a) Exact identity R_{h+1,i} = (√n/2)·E_n[(τ_i S)·D̃_h·R_h]. Verdict: CONFIRMED

K is a real symmetric circulant, since χ(−1)=1 makes the multiplier even, so K_{ik} = S_{k−i}/(2√n). The secant along [V_h, V_{h+1}] is valid inside the disks. The "Parseval" statement is a trivial rescaling.

**ERROR in the accompanying claim.** The claim reads: "Confinement requires the maximum … within a bounded factor of the RMS … may grow at most like γ^k with γ<1/q." As a necessity statement this is false. Confinement only needs the signed cumulative sums Σ_h R_{h,i} to stay below ρ. Two counterexamples:
- Sup decay ρ/(k+2)² with RMS ~ q^k is summable, but the ratio grows like q^{−k}, i.e. γ=1/q.
- The true RMS rate may be well below q; the numerics give 0.24. Then a sup decay like 0.5^k has ratio growth (0.5/0.24)^k > 1/q.

The condition is only what Criterion D needs (sufficiency). The same applies to summary item 1's "must be independent of n": this holds for the D-route, not for confinement itself.

### R3.4(a) Norm-only estimates lose √n. Verdict: CONFIRMED-WITH-CORRECTION

The Hölder exponent bookkeeping (1/r − ½(1−2/r') = ½) and the flat-row extremizer are correct as a statement about the available data.

**Correction.** The entrywise bound ‖(KD)^jK‖_max ≪ n^{−1/2}(1.066)^j in Round 162 is for the frozen D_602, not for products of the moving secants D̃_h as written in §4. It is also only "≪ min{…, 0.518^j}" with a summed form. This is a meta-statement about the method, not a theorem about the actual rows.

### R3.5(b) Criterion D(Λ,γ). Verdict: CONFIRMED (the implication)

The induction is correct:
- convexity of the polydisk gives ‖R_{602+i}‖ ≤ q^i·ε';
- the triangle inequality gives a sup-displacement bound of Λε'/(1−qγ) < ρ−η;
- the Round 173 tail applies, and 0.545⁸ < 2^{−7} was checked exactly.

The budgets 6.546·10^{205}, 1.282·10^{206} and 9.406·10^{206} were recomputed.

### R3.6(a) Method obstructions. Verdict by item

| Item | Verdict | Reason |
|---|---|---|
| (i) Λ_n→∞ (also from any later fixed height) | CONFIRMED | The sufficient bound in D diverges because liminf ‖R_602‖ > 0. This is an obstruction to the D-route only, not to confinement. |
| (ii) Unsigned rate B≥1 diverges | CONFIRMED-WITH-CORRECTION | The logic is right (k_n·P(R_602) → ∞, with P ≥ sup ≥ RMS bounded below). Thresholds κ<0.96608 and 0.4912 are correct. See below. |
| (iii) Moving predictor "only restates the same signed sum, not an independent route" | GAP | Only the frozen Newton correction is analysed. Its sup bound via the Round 162 resolvent is n^{0.545}·RMS, which is correct. No argument covers arbitrary moving predictors, so this is a heuristic, not (a). |

Corrections to item (ii):
- "A price route closes **iff** …" should read "if".
- Round 83's expanding records (>1.0000173) concern the fully collected single-vertex lower-kernel rule for the forcing homotopy from the nine-center row C at the real floor. They do not concern the secant price rate on 𝒫_ρ about V_602, so they are only analogous evidence.

### R3.7 Larger radius. Verdict: CONFIRMED-WITH-CORRECTION

The labelling should change as follows:
- q(ρ)<1 for every ρ < √(N/2)−1.963 = 3.670 is actually provable: C(u) ≥ N−2B² > 0 and A is bounded. This part can be (a).
- The table values for ρ ≥ 0.75 come from floating-point grid maxima and are (c).
- For ρ = 0.025, 0.05, 3/8 and 0.3906, I verified that the monotonicity condition A'C−AC' > 0 holds, so the maximum is at u=1. The values 0.5174, 0.5193 and 0.5441 follow, as does q(0.3906) ≈ 0.54526 ≈ 2^{−7/8}.
- The 0.025 and 0.05 values are new seed-centred values, not "inherited rational checks". Inherited are 0.525 and 0.535.

### R3 (c) numerics. Verdict: NOT RE-RUN

NumPy is unavailable. The runs use a Jacobi-seed start, not the nine-center row, do not separate the lifts, and stop at heights ≤ 40. They say nothing about height 602. No (a) claim depends on them, except the §7 curve, which is flagged above.

---

## Overall

- **Report 1:** the main lemma and the whole propagation are correct. The only correction is to the method-limit threshold in R1.5 (p^{7/8} versus p^{15/16}).
- **Report 2:** all identities and bounds are correct. The headline overstates what is "retained", because 𝓜_w passes through Round 179's majorization.
- **Report 3:** the (a) bounds at height 602 and the Criterion D implication are correct, with the ineffective Round 80 transfer as caveat. Three claims overstate necessity or scope:
  - "confinement requires a bounded or γ<1/q ratio";
  - the moving-predictor no-go;
  - the price-route "iff".

  The Round 162 and Round 83 citations are stretched beyond their scope.
