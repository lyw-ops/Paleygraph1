# Review of the anchored input-mark response

The [returned draft](api-astra-overflow-114.txt) identifies the anchored Jacobi transport as the remaining marked statistic and correctly bounds the input-mark contribution by \(O(n^{-1})\) using the entry bound. The [completion receipt](api-astra-114-receipt.json) records the response label and the original input note digest.

The transform normalization in the draft is incorrect. For \(f=P(h)g\), the actual matrix is \(K_{xy}=\lambda_{x-y}/n\), so
\[
 \mathbb E_n(fz)=\epsilon Kf(0)/\sqrt p.
\]
In particular \(c_-\mathbb E_n(fz)=\epsilon g_-(0)Kf(0)/n\), and the absolute small-o condition for the isolated contribution is \(Kf(0)=o(1)\), rather than the draft's \(o(\sqrt n)\). Also \(\lambda_0=-1\). The input at zero is absent because \(h(0)=0\) and \(P(0)=0\). The ordinary \(O\)-bound does not give a useful one-sided sign; the full-moment positivity in Round 113 still holds exactly at its proved scope.

The [reviewed local work](reciprocal-input-marks-114.md) instead uses the trimmed factor transforms and the square of their resulting signed coefficient \(W\). At \(0<t\le1/4\) this confines failure of two signed bounds to genuine Jacobi-level concentration and a separate negative first moment on sites with low favored factor. The isolated mark might still contribute at order \(n^{-1}\). Neither the normalized anchored transform nor the unmarked tuple sums have the prime-uniform improvement needed to close the obstruction.
