# Prescribed marks at the square order \(389^2\)

Let \(q=389^2\), \(n=(q-1)/2=75660\), and let \(I\) be the subfield annihilator with \(h=|I|=195\). On the plus witness side, the [pinned defect](one-sided-quadratic-22.md#a-direct-certificate-at-the-prescribed-mark) minimizes \(\|Y_-\|_2\) over \(Y\in U_-\) of ordinary mean one and mark \(a\sqrt n\). The certificate gives

$$d_q(a,1)=\frac{(a\sqrt n-h)_+}{\sqrt{h-1}}\qquad(0\le a\le1).$$

Since \(\mathbf1_I\in U_+\), every such \(Y\) has \(\sum_I Y_i=h\). Cauchy–Schwarz on \(I\setminus\{0\}\) gives the lower bound. Equality holds if \(Y\) is constant there and nonnegative off \(I\). At \(a=1\) the row below has strictly positive exterior. Interpolation with the [square minus optimum](square-order-control.md#a-square-order-comparison) of mean one and mark \(h\) gives equality throughout \(h/\sqrt n\le a\le1\). For smaller \(a\) interpolate the minus optimum with the nonnegative row \(M=\mathbf1-\ell/\kappa\) of mean one and mark zero.

The exact row starts from \(\mathbf1+(a\sqrt n-1)\ell/\kappa\), where \(P=P_-\), \(\ell=Pe_0\), and \(\kappa=P_{00}\). It adds a mean-zero even Fourier row in \(\operatorname{im}P\), reconstructed from rounded integer coefficients, and pins that correction with \(L=P-\ell\ell^{\mathsf T}/\kappa\). Write \(C\) for orthogonal projection onto vectors supported on \(I\setminus\{0\}\) and summing to zero there. The square subfield entries give \(CLC=\kappa hC/(h-1)\), so subtracting \(LCY/(\kappa h/(h-1))\) makes the subfield bulk constant without changing the mark or mean. Accelerated projection of exterior violations proposes the row. Arb checks every exterior entry after the exact reconstruction.

| Normalized mark \(a\) | Exterior slack lower bound | Exact defect, rounded |
|---:|---:|---:|
| \(49/50\) | \(0.00141578\) | \(5.35326521\) |
| \(1\) | \(0.00100306\) | \(5.74823357\) |

## Subfield saturation in the one-sided problem

A mean-one row \(Y\in U_-\) with mark \(h+(h-1)v\), bulk subfield entries \(-v\), and nonnegative exterior is equivalent to optimality of \(\mathbf1_I\) for \(A_+(r)\) at \(r=hv/(n+hv)\), for \(v>0\). Indeed \(b=(Y+v\mathbf1_I)/(h+hv)\) is anchored and nonnegative. Because \(P_+Y=0\) and \(r^{-1}vh=n+vh\), its image under \(J+r^{-1}P_+\) is \(B\mathbf1_I\) with \(B=(h^2/n+r(h-h^2/n))^{-1}\). This verifies the reciprocal optimality conditions. Conversely if \(\mathbf1_I\) minimizes \(A_+(r)\), the reciprocal minimizer satisfies \(b_i=0\) for \(i\in I\setminus\{0\}\) and \((J+r^{-1}P_+)b=B\mathbf1_I\). Subtract \(rB\mathbf1_I\) and divide by \(Bh(1-r)/n\) to recover \(Y\).

The mark-one row therefore certifies the exact subfield value for \(0<r\le r_*\), where

$$v_*=\frac{\sqrt n-h}{h-1},\qquad r_*=\frac{h v_*}{n+h v_*},\qquad r_*\sqrt n>0.29226263069516.$$

This range includes \(r=(1/4)/\sqrt n\).

The [replay](square-pinned-22.py) reproduces the two [interval records](square-pinned-22-certified.jsonl).

```sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/square-pinned-22.py \
  > research/square-pinned-22-certified.jsonl
```
