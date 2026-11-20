"""Verify the signed true-prefix identity at a nonempty prime mask."""
import json
from pathlib import Path
import runpy
from flint import acb, arb, arb_mat, ctx

prior = runpy.run_path(str(Path(__file__).with_name("astra-recur-95-check.py")))
apply = prior["apply"]
interval = prior["enclose"]
ctx.prec = 384


def replay():
    p, T = 769, 10
    n, k = (p - 1) // 2, T - 2
    signs = list(map(int, prior["paley_sign"](p)))
    root = arb(n).sqrt()
    delta = [1] + [0] * (n - 1)
    column = apply(delta, signs)
    forbidden = apply(delta, [int(s < 0) for s in signs])
    S = list(range(0, n, 48))
    C = S[1::2]
    matrix = arb_mat([[column[(i-h) % n] for h in S] for i in S])
    kappa = sum(abs(matrix[0,j]) for j in range(len(S)))
    assert kappa < arb(1)/2
    y = [arb(0)] * n
    states, raw, means, betas = [], [], [], []
    for j in range(T + 2):
        states.append(y)
        source = list(map(abs, y))
        source[0] = (4*n+y[0]**2).sqrt()
        beta = (source[0]-abs(y[0]))/root
        betas.append(beta)
        means.append(sum(source)/(2*n))
        raw.append(apply([(v-z)/2 for v,z in zip(source,y)],
                         [int(s <= 0) for s in signs]))
        y = apply(source, signs)
    assert max(means[T-1:T+2]) < 4
    W = 2*T - 1
    pin = [(2*sum(row[i] for row in raw[1:T])+raw[T][i])/W for i in range(n)]
    allowance = arb(21)/20*pin[0]/root - sum(pin)/n
    assert allowance > 0
    repaired = [z+allowance*(1-h/forbidden[0]) for z,h in zip(pin,forbidden)]
    E = [i for i in C if repaired[i] < -arb(1)/100]
    assert E == [48,336] and all(repaired[i] > -arb(1)/100 for i in C if i not in E)
    B, minority, orientation, last = [], [], [], []
    for i in S:
        total = sum(abs(row[i]) for row in states[1:k+1])
        signed = sum(row[i] for row in states[1:k+1])
        assert total > 0 and (signed > 0 or signed < 0)
        B.append(total)
        orientation.append(1 if signed > 0 else -1)
        minority.append((total-abs(signed))/2)
        last.append((total-abs(states[k][i]))/total)
    rhs = arb_mat([[int(i in E)] for i in S])
    dual = arb_mat([[int(i==j)-orientation[j]*matrix[j,i]*last[i]
                     for j in range(len(S))] for i in range(len(S))]).solve(rhs)
    psi = [dual[j,0]*orientation[j] for j in range(len(S))]
    outside = [sum(abs(row[i]) for row in states[:k]) if i not in S else arb(0)
               for i in range(n)]
    D = apply(outside, signs)
    lhs = sum(B[j] for j,i in enumerate(S) if i in E)
    external = sum(w*D[i] for i,w in zip(S,psi))
    mark = sum(betas[:k])*root*sum(w*column[i] for i,w in zip(S,psi))
    mixed = 2*sum(dual[j,0]*v for j,v in enumerate(minority))
    assert (lhs-external-mark-mixed).contains(0)
    for i in E:
        wrong = sum((-row[i]).max(0) for row in states[1:T])
        h = sum(abs(row[i]) for row in states[T-1:T+2])
        assert 8*wrong+4*W/100 < 2*h+2*abs(states[1][i])+2*(means[T]+means[T-1])+4*means[0]
    physical_test = [arb(0)] * n
    for i, weight in zip(S, psi):
        physical_test[i] = weight
    freq_test = acb.dft(physical_test)
    freq_input = acb.dft(outside)
    spectral = acb(0)
    for z in range(len(S)):
        indices = range(z, n, len(S))
        assert sum(freq_input[j] for j in indices).contains(0)
        side = (-1)**z
        half = sum(freq_input[j] for j in indices if signs[j] == -side)
        spectral -= 2*side*freq_test[z].conjugate()*half/n
        if z == 0:
            spectral -= side*freq_test[z].conjugate()*freq_input[0]/n
    assert (spectral-external).contains(0)
    norm = k*len(E)
    return dict(prime=p, terminal=T, prefix=k, contracting_set=S, mask_in_coset=E,
                contraction=interval(kappa), normalized_history=interval(lhs/norm),
                signed_exterior=interval(external/norm), true_mark=interval(mark/norm),
                signed_minority=interval(mixed/norm), precision_bits=ctx.prec, units="1e-9")


if __name__ == "__main__":
    print(json.dumps(replay(), sort_keys=True))
