# The actual slope fibers from two vertex quotient sets

Keep the original square-input physical sum, the actual probability \(\nu\) and characteristic function \(f\), and physical mark \(v\ne0\). Put \(N_0=\sqrt p\), and assume the selected prime-branch cap \(n\max\nu=O(N_0)\). Use the two fixed squared threshold levels
\[
 \mathcal A=\{A\in Q:|f(A)|^2\ge a\},\qquad
 \mathcal B=\{C\in Q:|f(C)|^2\ge b\},\qquad a,b>0 .
\]
For the new slope bound assume at least one threshold is above one half. Both levels have size \(O_{a,b}(N_0)\) by Parseval. At a level above one half, its whole quotient set has the same bound, by the [Round 163 covariance inequality](ordinary-shifted-layer-energy-saving-163.md). Its pointwise inverse set has the same amplitudes since \(f(z^{-1})=\overline{f(z)}\).

## A uniform affine intersection bound

Consider any set \(M\) whose elements lie in one of the two levels, and which maps into the other under \(z\mapsto c z+d\) with \(cd\ne0\). Either level can be replaced by its inverse. If both thresholds exceed one half, Zhelezov's theorem as in Round 163 gives \(|M|\ll p^{13/27}\), since both quotient sets have size \(O(N_0)\).

Now allow one of the fixed thresholds to be at most one half. Orient the affine map from the lower level to the higher one, reversing it if needed. Set \(m=|M|\), and trim to at most \(\lfloor\sqrt p\rfloor\) points at a constant-factor loss as needed. The hereditary fourth-moment bound of Round 163 gives \(E^\times(M)\gg m^4/N_0\). Apply the Reiher–Schoen theorem there with \(K=m^3/E^\times(M)\ll N_0/m\). There is a subset of size \(l\gg m^{3/2}/N_0^{1/2}\) whose quotient set has size \(O(K^4l)\). The higher-level image quotient set is still \(O(N_0)\). Rescaling the affine image and applying Zhelezov to the subset and the reciprocals of its source and translated sets gives
\[
 l^{1/26}\ll\max\{(N_0/m)^4,N_0/l\}.
\]
In the first case this yields \(m\ll N_0^{1-2/211}=p^{1/2-1/211}\) by substitution of the lower bound on \(l\). In the second case, \(l\ll N_0^{26/27}\) and \(m\ll N_0^{1-2/81}\), which is stronger. Constants depend only on the levels and the cap, uniformly in both nonzero affine coefficients. Set
\[
 \gamma=\begin{cases}
 1/54,&\min(a,b)>1/2,\\
 1/211,&\max(a,b)>1/2\text{ and }\min(a,b)\le1/2 .
 \end{cases}
\]
Then \(|M|\ll_{a,b}p^{1/2-\gamma}\). In the original \(u\)-slice apply this at \(A_x\mapsto C_x=uA_x+1-u\) for \(u\ne1\).

## Fixing the physical slope, with weights retained

Use \(A_x=1-vx\), \(C_x=1-vux\) and the analogous values at \(y\), with all four in their original nonzero levels. Put
\[
 r=A_y/A_x,\qquad s=C_y/C_x,\qquad t=s/r.
\]
In the true off-diagonal block, \(u\ne1\), \(x\ne y\), and \(t\ne1\), so \(r,s\ne1\) and \(r\ne s\). For fixed \(r,s\) the equality \(s(1-u+uA_x)=1-u+urA_x\) gives
\[
 C_x^{-1}=\frac{r-s}{r-1}+\frac{s-1}{r-1}A_x^{-1},
 \qquad
 \frac{u}{1-u}=\frac{s-1}{(r-s)A_x}.
\]
In particular both coefficients of the affine relation are nonzero. The first identity and the uniform intersection bound give at most \(O_{a,b}(p^{1/2-\gamma})\) contributing \(A_x\). The second identity determines at most one \(u\), and then \(x,y\) are unique. All square and sign restrictions can be imposed on this actual count.

At fixed \(t\), \(s=tr\). At least one of \(\mathcal A/\mathcal A\) and \(\mathcal B/\mathcal B\) has size \(O(N_0)\). Thus the number \(N_t\) of original contributing triples at that slope satisfies
\[
 N_t\ll_{a,b}p^{1-\gamma}.
\]
Alternatively the total off-diagonal count is at most \(\sum_{u\ne1} h(u)(h(u)-1)\), where \(h(u)\) is the true original overlap. The original \(u\)-slice bound and \(\sum_u h(u)\le |\mathcal A||\mathcal B|=O(p)\) give \(\sum_tN_t\ll_{a,b}p^{3/2-\gamma}\).

Consequently for any genuine slope submask \(D\), the actual restricted five-factor sum in absolute value is at most
\[
 O_{a,b}\!left(\min\left\{
  p^{1-\gamma}\sum_{t\in D}|f(t)|,\ 
  p^{3/2-\gamma}\sup_{t\in D}|f(t)|
 \right\}\right).
\]
Only the four physical vertex amplitudes were bounded by one. The actual slope cutoff and favorable phase stay in the count. In particular \(\sum_{t\in D}|f(t)|=O(p^\gamma)\) suffices even on a sparse moderate slope set. A band with \(|f(t)|^2\le p^{-\sigma}\) suffices for \(\sigma\ge1-2\gamma\), slightly extending the one-high-layer endpoint from Round 163. The unrestricted first mass can be much larger than the allowed scale, and the full moderate band remains open.

## The third level is a shifted reciprocal level

On \(a+b>1\), the original ratio \(r_u(x)=C_x/A_x\) also satisfies \(|f(r_u(x))|\ge\sqrt{ab}-\sqrt{(1-a)(1-b)}>0\). The same statement for \(y\) does not yield a positive lower for \(|f(t)|\) unless this bound exceeds \(1/\sqrt2\). The prime energy saving from Round 163 applies to a *shifted* level of this kind, not to its unshifted global level without further restrictions. One may instead use that \(r_u(x)=u+(1-u)A_x^{-1}\) is an actual affine image on each fixed \(u\), or use the slope quotient coordinates above.
