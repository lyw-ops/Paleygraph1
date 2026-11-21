# Matching the energy defects of the core and its exterior

The genuine time-averaged repair gives an exact comparison between the core Jacobi energy defect and the defect of the discarded source. It also gives a nonzero centered opposite-sector defect of order \(n^{-1/2}\) in normalized second norm, concentrated off the persistent core. These conclusions use the late repair block on a marked obstruction at critical cap rate.

Use \(P,h_j,b^j,\bar h,i,l,L,C,H\) from [the core average](repair-core-average-110.md). Throughout, \(\langle\cdot,\cdot\rangle\) and \(\|\cdot\|\) use the normalized second norm. Put
\[
 u=1_C\bar h,\quad r=1_{C^c}\bar h,\quad m=\mathbb E_n\bar h,
 \quad B=I-\epsilon K,\quad D(x)=\langle x,Bx\rangle .
\]
The operator \(B\) is positive semidefinite with norm at most two. It satisfies \(D(\bar h)=2\|P\bar h\|^2-m^2=O(n^{-1})\) by the genuine late block.

## Exact defect comparison

Self-adjointness gives \(D(u)-D(r)=2\langle u,B\bar h\rangle-D(\bar h)\). The active-set average in the core gives
\[
 D(u)-D(r)
  = -D(\bar h)-2m\,\mathbb E_n u
         +\frac4L\langle u,h_i-h_l\rangle .                        \tag{1}
\]
This uses \(B\bar h=2P\bar h-m\mathbf1\), and \(u\) is supported on \(C\). In particular \(|D(u)-D(r)|=O(n^{-1}+n^{-3/4}L^{-1/2})\), using \(m^2=O(n^{-1})\), \(\|u\|=O(n^{-1/4})\), and the late squared difference telescope. For the fixed-threshold square-root-length block this is \(O(n^{-1})\). This retains the exterior as an actual quadratic defect rather than treating its transport by a triangle bound against the entire core.

On that same core one also has
\[
 \epsilon\langle u,K\bar h\rangle
      =\|u\|^2+m\mathbb E_n u+O(n^{-3/4}L^{-1/2}).
\]
The ratio to \(\|u\|^2\) is \(1+O(n^{-1/2})\) at the fixed-threshold square-root length. Using \(u\) rather than \(1_C\) removes the need to bound the core mass only by its minimum threshold times cardinality.

## Moving threshold with explicit powers

The constant in the flip estimate can be made explicit in the threshold: for \(s\in[\eta,2\eta]\), some common \(s\) on a length-\(L\) block satisfies
\[
 |H\setminus C|\le O(\eta^{-3/2} n^{1/4}\sqrt L).
\]
Indeed \(\{x:\max(h_j(x),h_{j+1}(x))>\eta\}\) contains \(O(\sqrt n/\eta)\) sites by the late mean bound. The normalized second-to-counting first norm conversion costs \(O(n^{3/4}\eta^{-1/2})\). Use the summed squared consecutive difference \(O(n^{-1})\) and divide the integral by its interval length \(\eta\). All implied constants here are independent of \(0<\eta\) below a fixed small bound. At these thresholds each high support has size at least \(c_1\sqrt n\) by the late \(O(1)\) entry bound and its squared mass.

Fix \(0<\beta<1/10\) and take \(\eta=n^{-\beta}\), \(L\) an integer of order \(\eta^5\sqrt n\). This fits inside the late window, and has \(L\to\infty\). Then \(|H\setminus C|=O(\eta\sqrt n)\), \(|C|\gtrsim\sqrt n\), and \(|C|=O(\sqrt n/\eta)\). Uniform amplitude and low squared-mass bounds show
\(\|r\|^2=O(\eta n^{-1/2})\). The time telescope gives \(\|\bar h-h_i\|=O(\eta^{5/2} n^{-1/4})\), so \(\|u\|^2\gtrsim n^{-1/2}\). Thus the genuinely truncated core has signed Rayleigh loss
\[
 \frac{D(u)}{\|u\|^2}
     =O(\eta+n^{-1/2}\eta^{-5/2})=O(n^{-\beta})
\]
by (1) and \(D(r)\le2\|r\|^2\). Its size bound is \(O(n^{1/2+\beta})\). Its effective support \(n(\mathbb E_n u)^2/\|u\|^2\) is still comparable to \(\sqrt n\). The upper follows from \(\mathbb E_n u\le m=O(n^{-1/2})\); the lower uses \(\|u\|_\infty=O(1)\) and the squared mass bound. This produces a power-small defect and a growing core window, while retaining the critical effective scale.

## A centered defect forced off the core

Set \(e=P\bar h-m\mathbf1\), in the exact centered \(-\epsilon\) sector. Write \(v_j=P h_j=b^{j+1}-b^j\). Since \(b^j h_j=-h_j^2\) pointwise,
\[
 \langle b^i,\bar h\rangle
 =-\frac1L\sum_{j=i}^{l-1}\|h_j\|^2
   -\frac{\|\sum_{j=i}^{l-1}v_j\|^2}{2L}
   +\frac1{2L}\sum_{j=i}^{l-1}\|v_j\|^2 .
\]
This is the expansion of the ordered pairs of repair displacements. Since \(P b^i=b^i\), also
\(\langle b^i,\bar h\rangle=\langle b^i,e\rangle+m\mathbb E_n b^i\).
The mean of \(b^i\) is positive. Thus \(\langle b^i,e\rangle\le-c n^{-1/2}\) for some \(c>0\) eventually, by the late lower norm and the \(O(n^{-1})\) displacement-squared bound. Nonexpansiveness of the repair toward zero gives \(\|b^i\|\le\|z\|=O_{t,M}(1)\). Therefore \(\|e\|\gtrsim n^{-1/2}\), and the upper \(\|e\|=O(n^{-1/2})\) follows by averaging the late projection bound.

On the selected core one has
\[
 \|1_C e\|\le \|1_C P\bar h\|+m\|1_C\|
        =O(n^{-3/4}\eta^{-5/2}+n^{-3/4}\eta^{-1/2})
        =o(n^{-1/2})
\]
for the moving thresholds just used. The same concentration off the core follows at fixed small threshold and square-root length. The opposite-sector error therefore contains a nontrivial centered component of the stated size outside the core, in addition to a constant mean. The estimates identify where a genuine arithmetic gap is required. They do not imply decay of the centered defect on the whole group.

1. Test \(D(1_C\bar h)-D(1_{C^c}\bar h)\) at the exact scale in (1) jointly with the genuine centered exterior defect. A generic near-minimum-size support theorem does not apply to the moving threshold without more effective-width structure.
2. Investigate whether the positive actual high-source part and this forced opposite-sector exterior can coexist with the true factor pairing in the same real prime subsequence.
