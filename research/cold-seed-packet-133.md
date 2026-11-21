# A strict physical packet price for the seed block

Retain the original closed square and actual marked floor convention of [Round 132](cold-seed-block-132.md). Let \(S=2\sqrt n\,Ke_0\), and let \(D_{\rm seed}\) be the diagonal of the first derivative coefficient applied to \(S\), using \(S_i/(2\sqrt t)\) off the mark and \(S_0/(2\sqrt n)\) at the mark. Use the actual translated packet price \(P_\Lambda\) with \(\Lambda=5000\) and the fixed rational piecewise affine \(\pi\) from [Rounds 96 and 130](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step).

In the geometric calculation the seed multiplier has all its pooled absolute mass \(m\) at weights \(+1,-1\), in equal halves. Here
\[
 m=\frac{2\sqrt{p/n}}{2|\sqrt t|}\ \le\ 
 \frac{2.828428}{\sqrt{4\inf_Q\Re t}}
\]
for the sufficiently large eligible primes. Therefore the price ratio of a base column of index \(k\ge1\), per unit \(m\), is
\[
 \frac{k-1+\big(\pi(k+1)+\pi(k-1)\big)/2}{\pi(k)} .
\]
After the last stored weight, its numerator and denominator are affine in \(k\) and the ratio tends to \(1+1/\pi'_\infty\). The [rational replay](cold-seed-packet-133-check.py) checks all remaining columns and the limit, obtaining a base constant below \(1.505\). The additional base zeros for translated input cost exactly \(m\) per unit off-base first moment because \(\pi(1)=1\), and the off-base output multiplies its first moment by at most \(m\). Thus before exceptional corrections the translated price factor is at most \(m(q_0+1/5000)\), where \(q_0\) is the base constant in the exact comparison.

Restoring the bad lifts and the actual marked coefficient costs \(O_{5000}(n^{-1/2})\) in relative price. The changes in the product before \(K\) are supported on the base and the single input translated pair. Each is bounded by the product of the convolution dimensions times a fixed factor. Their post-\(K\) columns have price \(O_{5000}(n^{-1/2})\). This is the same two-boundary correction as in Round 96, applied here to a single designated seed term. The rational replay checks strict slack to \(0.535\) before the corrections. For sufficiently large eligible primes the exact seed step therefore has translated physical price rate below \(0.535\), uniformly on the square and in the translated pair. The exact marked seed–seed block on an actual negative packet has price rate below \(0.287\). This upgrades the position entry calculation for that contribution to a physical packet estimate. The remaining terms of the true block can change its price.

## The full block and the actual two-step residual in counting norm

Let \(s=2.828428\), \(b=1.971573\), and \(N=4\inf_Q\Re t\). For every endpoint through the physical height \(602\) in [the verified prefix](cold-positive-block-131.md), the dimension bound below \(4.8\) includes the designated seed of dimension \(2\sqrt{p/n}\ge\sqrt8\). Thus the remainder in the actual seed-centered disks has modulus at most \(b\), and the real seed is bounded by \(s\). The same disks contain the convex segments between successive verified endpoints.

For such a coordinate \(z\) of imaginary part \(y\) put \(u=\sqrt{1-y^2/b^2}\). On the bulk or marked sheet, whose floor has real part at least \(N/4\),
\[
 |z|^2\le F(u)=s^2+b^2+2sbu,\qquad
 \Re(4t_i+z^2)\ge |z|^2+C(u),\qquad C(u)=N-2b^2(1-u^2).
\]
Consequently the derivative square is at most \(F/(F+C)\). The rational comparison \(2sb(N-2b^2)>4b^2(s+b)^2\) makes this quotient increasing on \([0,1]\). Its upper endpoint comparison gives derivative modulus below \(0.516074\) on all these disks. In particular the genuine frozen height-601/602 block has counting rate below \(0.5145(0.516074)<0.26553\) on the whole closed square.

Let \(R_h=V_{h+1}-V_h\) and \(L_h=\int_0^1\operatorname{diag}\Phi_t'(V_h+uR_h)\,du\), with the marked floor used at the marked coordinate. The actual recurrence is
\[
 R_{602}=K L_{601} K L_{600}R_{600}.
\]
The [first actual secant](cold-actual-first-insertion-126.md#a-second-genuine-outgoing-counting-step) has counting rate below \(0.515\). The second lies on the verified disks above, hence
\[
 \|R_{602}\|_{2,n}\le 0.2658\,\|R_{600}\|_{2,n}
\]
uniformly on the square eventually. The exact signed position entry estimate of [Round 132](cold-seed-block-132.md#the-full-actual-block-on-the-physical-mean-zero-space) applies also to this secant pair on the physical mean-zero space. Its proof is uniform for each of the two convex predictor segments with the same dimensional mass bound, and integrating each derivative keeps the kernel estimate. These are fixed-depth statements. They leave the full signed physical packet price and an invariant ball through growing depth open.

The actual residual also has a small orthogonal Jacobi projection. Write \(a_h=\Phi_t(V_h)\) and \(\mu_h=\mathbb E_n a_h\). For \(1\le h\le602\),
\[
 \langle R_h,S\rangle_{2,n}
 =\frac{2}{\sqrt n}\bigl(a_{h,0}-a_{h-1,0}-\mu_h+\mu_{h-1}\bigr)
 =O(n^{-1/2})\|R_{h-1}\|_{2,n}.
\]
Here the first equality uses \(R_h=K(a_h-a_{h-1})\) and \(KS=2\sqrt n(e_0-\mathbf1/n)\). The marked derivative is \(O(n^{-1/2})\) on its bounded segment, and the normalized mean difference is bounded by the derivative second-norm estimate. Since \(\|S\|_{2,n}^2=4(1-1/n)\), the same bound controls the coefficient of the orthogonal projection of \(R_h\) onto this specific seed. It does not remove the other fields with weight \(1\) from a packet representation.

The [two saved records](cold-seed-packet-133-checks.jsonl) use exact rational arithmetic for the finite pricing list and for the disk comparisons. The accompanying algebra and inherited physical representation bounds give the stated scope through primes.
