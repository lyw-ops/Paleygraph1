# Signed rank-four returns and relative phases of the physical forcing path

Let \(a=2031/128\), \(Q=\{|\Re t-a|,|\Im t|\le2^{-17}\}\), \(n=(p-1)/2\ge10^{30}\), and \(p\equiv1\bmod4\) be prime. Put \(T=K\Phi_t\), where \(\Phi_i(x)=\sqrt{4t_i+x^2}\), \(t_0=n,\ t_i=t\) off zero. For the actual nine-center row \(C\) and \(R=T(C)-C\), use the same forced equation
\[
                   U=T(U)-(1-\lambda)R,\qquad U(0)=C.
\]
On \(Q\) its physical branch now reaches \(|\lambda|\le0.9989815\) with coordinate cap \(4.654\). At the genuine parameter \(\lambda=1\) there is a common stationary rectangle
\[
  16640260<2^{20}\Re t<16640292,\qquad 2^{20}|\Im t|<2 .
\]
It joins the [round-83 domain](astra-direction-83.md), lowers its real endpoint by \(29.5/2^{20}\), and has \(|m_p(t)|<3/\sqrt n\). On every closed real subinterval of this new rectangle one can also choose a common positive imaginary width for **all** eligible primes: at each of the finitely many \(n<10^{30}\), the strictly positive real stationary rows have an invertible Jacobian and compactness gives a neighborhood of that interval. Taking the minimum of finitely many widths proves this statement, with no numerical width for the smaller fields. The rectangle lies above the cold center. The estimates below also constrain all sites of any attempted continuation from the cold forced domain, including those with large real amplitude. They leave the common cold stationary section and the ordinary theta limit open.

## Two signed coincidences in the nine-center polynomial

Use the [old rank-four factor](astra-rankfour-57.md) \(F=\frac18\sum(X_i+X_i^\vee)\) from four standard rank-four representations, with its actual determinant shifts, and its old analytic amplitude \(\gamma\). Use the precise truncated old rank-three prefix \(L=4,A=5,E=9,J=8\) from [round 64](astra-joint-64.md). In that prefix, retain only its rank-three scalar and all Legendre labels \(u+v\le5\). Write \(c_{r,u,v,e}\) for the old signed coefficient with shared Jacobi exponent \(e\), including the root amendments. These coefficients stay separate in the old upper calculation, except for the explicitly excluded pools below. We perform the following additional collections within the terms with no input from the later rank-five, mixed, dual or symplectic centers.

* The square of \(F\) contains \(8/64=1/8\) copies of the scalar after normalization. For arity \(j\), combine \(c_j\) with \(\binom{j+2}{2}\gamma^2 c_{j+2}/8\) for each common old label.
* In the cube, each of the eight standard/dual summands occurs at least 24 times at its **own arithmetic exponent**. After normalization this gives \(24/64=3/8\) times \(F\). Combine \((j+1)\gamma c_{j+1}\) with \(3\binom{j+3}{3}\gamma^3c_{j+3}/8\), carrying the full \(F\) fiber. Extra copies and other determinant exponents keep their original positive prices.

The finite Pieri tables check both multiplicities. In both collections we restrict to \(|e|\le9,\ 0\le j\le6\) and source arities at most eight. Skip the first collection for the old scalar \(u=v=0,\ |e|\le5\), whose rank-four returns have already been combined. At \(j=0\) also skip the first for \(e=0\) and \((u,v)=(1,1),(2,0),(0,2)\), and the second for \(u=v=0,\ |e|=1\). This keeps the root subtractions defining the later centers intact, including the \(m^{\pm4}\) scalar and the partial \(C_1F\) source. The two pools use disjoint numbers of \(F\) inputs. The later mixed and dual signed savings use positive numbers of their respective new inputs, disjoint from all terms used here. The rank-four root amendment inside the smaller prefix is on a rank-three standard at \(L=1\), which has no scalar summand.

For two selected coefficients \(x,y\) subtract the nonnegative lower bound for
\[
       |x|+|y|-|x+y|=
       2\bigl(|x||y|-\Re(x\bar y)\bigr)/\bigl(|x|+|y|+|x+y|\bigr).
\]
Use zero if the denominator enclosure meets zero. Each Legendre shift \(s=-2u,-2u+4,\ldots,2u\) has multiplicity \(v+1\), with boundary location \(s-e\). For the second collection convolve with the old rank-four boundary measure, which is twist invariant as it sums the entire fiber of the eight inputs. Deduct the smaller of the two reflected lower savings on both sides. At \(\lambda\ne1\) multiply the improved arity-zero row by \(|\lambda|\) after collection. Every complementary degree, arithmetic label, repeated shift, and exceptional marked-column correction retains its positive upper price.

The warm enclosure uses 16 real cells on its rectangle and conjugation on the imaginary interval. The cold enclosure uses eight real cells and four upper-half imaginary cells. The nonnegative degree-28 polynomials and the raw binomial powers from orders 15 to 22 feed the [round-83 tilted-tail test](astra-direction-83-invariant.py) at 58 packets, with \(2\cdot10^{-10}\) tilted residual and \(10^{-12}\) allowance for the physical exceptional column. The coordinate caps give the usual counting contraction of physical Picard on the convex coordinate disks. Thus the iterations from \(C\) converge for each field, uniformly in both parameters, to the physical branch. Positivity of \((\Phi(U)\pm U)/(2\sqrt n)\) at real genuine parameters identifies the true stationary pair. The real overlap with the previous warm section contains \((16640289.5,16640290)/2^{20}\). The polynomial and binomial enclosures use Arb at 192 bits. Floating iterations supplied only the fixed rational caps. [Checker](astra-imaginary-84-check.py) · [Frozen caps](astra-imaginary-84-caps.json) · [Outward interval records](astra-imaginary-84-checks.jsonl)

## A conjugate phase identity up to and beyond the unit derivative threshold

From \(r=0.9989815\) continue along real \(\lambda\) towards one at fixed \(t\in Q\). Set \(\sigma=1-\lambda\), \(\eta=|\Im t|\), \(\theta_i=\arg t_i\), \(A_i=(\Phi_i+U_i)/2,\ B_i=(\Phi_i-U_i)/2\). In these formulas the factors are scaled and \(A_iB_i=t_i\). Write
\[
 A_i=\sqrt{t_i}\exp z_i,\quad B_i=\sqrt{t_i}\exp(-z_i),\quad
 \phi_i=\Im z_i,\quad D_i=\tanh z_i=\Phi_i'(U_i).
\]
Take the physical square root and the lift of the logarithm from the bounded forced solution. It starts in \(|\phi_i|<\pi/4\) on the cold square: its imaginary coordinate cap is \(4.654-2.8284\) after removing the real seed; \(\Re(U_i^2/t_i)>-2\) follows directly, including the small rotation of a nonreal floor. Continuity from the real seed along the forced disk fixes the component. In particular \(|D_i|<1\) exactly in this phase range on that component. Equivalently the strict unit-derivative test is \((\Im(U_i/\sqrt{t_i}))^2-(\Re(U_i/\sqrt{t_i}))^2<2\).

Let \(x+iy=U,\ g+ih=\Phi_t(U)\), and use normalized counting expectation \(E\). The isometry modulo constants gives
\[
 \boxed{\quad
 4E|t_i|\sin^2\phi_i+(Eh)^2
 =4E|t_i|\sin^2(\theta_i/2)
             -2\sigma E[y\,\Im R]-\sigma^2E(\Im R)^2 .\quad}          \tag{1}
\]
Indeed \(y+\sigma\Im R=Kh\), and pointwise \(y_i^2-h_i^2=-4\Im A_i\Im B_i=4|t_i|(\sin^2\phi_i-\sin^2(\theta_i/2))\). Here \(E(\Im R)^2\) denotes the expectation of the coordinate squares.

On the wider closed square of half-width \(1/32\) about \(a\), the **actual** source has coordinate norm \(<0.142\). Its polynomial cost is \(\sum_{k\ge1}kU_0(k)\). In the analytic tail a \(2l\)-fold center product has boundary index at most \(10l\); summing the first omitted binomial coefficient times the geometric majorant with these linear weights gives the enclosure in the checker. The physical \(10^{-12}\) first-packet allowance still suffices on the wider square. Indeed the full center dimension is below five, the raw absolute binomial coefficient sum is below 17, the marked discrepancy is below 11, and the bounded center preimage corrections cost less than 16 before multiplication by \(\sqrt p/n\), as in the [exceptional column calculation](astra-adjoint-82.md). The center coefficients are holomorphic and real on real floors. Cauchy's estimate throughout \(Q\), then integration vertically, gives \(\|\Im R\|_\infty<4.52\eta\) for \(\eta>0\), with equality zero on the real slice.

As long as \(|\phi_i|\le\arctan(3/2)\) for all sites, both factors have positive real part, \(|x_i|\le g_i\), and \(|y_i|\le1.50001g_i\). Since \(g_i^2-x_i^2=4\Re A_i\Re B_i\le4|t_i|\), the real isometry gives
\[
 (Eg)^2\le 4E|t_i|+2\sigma\|\Re R\|_\infty Eg,\qquad Eg<8.23 .
\]
Hence \(E|y|<12.35\) throughout this enlarged sector. With \(L=\inf_Q\Re t\), (1) proves
\[
        4E|t_i|\sin^2\phi_i+(Eh)^2
          \le \eta^2/L+111.65\,\sigma\eta .                            \tag{2}
\]
This bounds the fraction of sites with \(|\phi_i|\ge\pi/6\) by \(\eta^2/L^2+111.65\sigma\eta/L\), below \(5.5\cdot 10^{-8}\) everywhere on the remaining segment up to first exit from the enlarged sector. At the genuine endpoint the bound is below \(2.32\cdot10^{-13}\) if reached there in the sector. The identity includes the actual marked site with weight \(n\), as well as the signed correlation with the true forcing. It bounds each instantaneous exceptional fraction, without taking a union over times.

## Allowing some derivatives larger than one

At a point of this continuation let \(B\) be any subset of sites, \(G=B^c\), \(k=\|K_{BB}\|_{2\to2}\), and assume \(\|D_G\|\le d<1,\ \|D_B\|\le b\). The physical Jacobian \(I-KD\) is invertible if
\[
                      b\,\frac{k+d}{1+kd}<1.                          \tag{3}
\]
For a diagonal \(V\) with \(\|V\|\le1\), put
\[
 S(z)=K_{BB}+K_{BG}\,zV(I-K_{GG}zV)^{-1}K_{GB}.
\]
It is a contraction for \(|z|<1\): send input \((v_B,zVw_G)\) through \(K\) and solve for its exterior output \(w_G\). The full contraction of \(K\) gives \(\|S(z)v_B\|^2+(1-|z|^2)\|w_G\|^2\le\|v_B\|^2\). Apply scalar Schwarz–Pick to \(\langle u,S(z)v\rangle\) for arbitrary unit vectors and use \(|\langle u,S(0)v\rangle|\le k\). Taking \(V=D_G/d,\ z=d\) gives \(\|S(d)\|\le(k+d)/(1+kd)\) (use \(z=0\) when \(d=0\)). Eliminating the \(G\) coordinates of \(I-KD\) now gives \(I-S(d)D_B\), proving (3).

For example, on the class \(|\phi|\le\arctan(3/2)\) one has \(|D|\le3/2\). Take \(B=\{i:|D_i|>3/5\}\). If \(|B|\le n/(10\sqrt p)\), the Jacobi entry bound gives \(k\le1/10\), so the product in (3) is at most \(105/106\). These conditions along the remaining segment suffice for genuine cold continuation. At each fixed \(n\), \(Eg<8.23\) bounds every \(g_i\), hence both factors and their inverses; their real parts stay strictly positive and their sum never vanishes there. Subsequence compactness, the strict Jacobian margin, and local implicit uniqueness therefore continue the physical branch up to one. The same argument works at first contact with \(|\phi|=\pi/4\): if the contacting sites have compression norm less than one, the complement has \(d<1\) at fixed field and (3) holds with \(b=1\). A singular Jacobian at first contact would require at least \(n/\sqrt p\) contacting sites. Bound (2) controls angles only. Large real amplitudes can also produce \(|D|>3/5\), and a small positive density need not have a small Jacobi compression.

## Large derivatives at height 600 beyond unit phase

For the different physical recentering \(X=V_{600}(t)\), \(R_X=T(X)-X\), take the real forcing path from \(\lambda=0\) at \(X\) up to \(\lambda=1\) or first exit from \(|\phi_i|\le\arctan(3/2)\). The [height-600 action proof](phase-action-84.md) gives \(\|X\|_\infty<4.768,\ \|\Im X\|_\infty<2,\ \|R_X\|_\infty<0.011\), and its starting logarithm \(w_i\) satisfies \(|\Im w_i|<0.26,\ e^{|\Re w_i|}<1.77\). Although the local derivative can exceed one in this larger region, the **secant from the predictor** remains dissipative. Indeed for \(\Delta=U-X,\ M_i=\tanh((z_i+w_i)/2)\) one has
\[
  1-|M_i|^2=\frac{\cos(\phi_i+\Im w_i)}{|\cosh((z_i+w_i)/2)|^2}
       \ge \frac{1}{13+1.4|\Delta_i|}.
\]
Here the cosine exceeds 0.32, while the denominator is at most \(1.77[1+(4.768+|\Delta_i|)/3.98]<3.90+0.445|\Delta_i|\). Thus the loss times \(|\Delta_i|^2\) is at least \(\min(|\Delta_i|^2,|\Delta_i|)/15\). In the exact complex secant identity, price \(2\lambda|\Delta_i R_{X,i}|\) on \(|\Delta_i|\le1\) by \(|\Delta_i|^2/30+30\lambda^2|R_{X,i}|^2\), and on its complement by \(0.022|\Delta_i|\). Subtract the full \(\lambda^2\|R_X\|_2^2\) from the resulting upper bound. This yields
\[
 E\min(|\Delta|^2,|\Delta|)\le870\lambda^2\|R_X\|_2^2 .
\]
Every site with \(|\Delta_i|\le1/2\) has \(|U_i|\le5.268,\ |\Im U_i|\le2.5\). There \(|D_i|\le5.268/\sqrt{4L+5.268^2-2(2.5)^2}<3/5\), also at the mark. Consequently the actual exceptional set in the scattering test satisfies
\[
           |B|/n\le3480\lambda^2\|R_X\|_2^2,\qquad
           B=\{i:|\Phi_i'(U_i)|>3/5\}.
\]
The [field-first physical residual bound](astra-dissipation-80.md#the-nonlinear-nine-center-secants) gives uniform limsup below \(3.27\cdot10^{-412}\) for this fraction on the available enlarged-sector segments. It includes derivatives close to saturation on sites with large real amplitude and small relative phase. The estimate is instantaneous and has no effective lower prime threshold for the improved limiting constant. It does not bound the compression of this set at unbounded field order.

1. On the genuine remaining segment, bound the compression of the actual large-derivative sites against their attained \(d,b\) in (3), including sites with large real amplitude. At first unit contact only the sites at the boundary enter the compression.
2. In (1) bound \(E[y\,\Im R]\) by resolving the true source against the high-phase sites. A prime-uniform relative-phase or compression upper along the whole segment would change the status of the cold section.
