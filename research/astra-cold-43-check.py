"""Exact signed endpoint cubic checked on independent Paley elimination curves."""
import json

import sympy as sp


def check(q):
    root13 = sp.sqrt(13)
    field = sp.QQ.algebraic_field(root13)
    F = field.from_sympy
    cv = lambda x: field.convert(x)
    t, r, h = sp.symbols("t r h")
    if q == 13:
        n = 6
        init = 1
        poly = (6+5*t)*r**3+(t-6)*r**2-(24+8*t)*r+24-4*t
        mark = 1+r
        g = [sp.Rational(x, 2) for x in (2, 1, -1, -2, -1, 1)]
        center = [1+x for x in g]
        transversal = [-x/3 for x in g]
    else:
        n = 12
        h0 = (7+root13)/18
        init = sp.simplify(1/h0-1)
        poly = ((5*t**2+12*t)*r**5+(-4*t**2+36*t+144)*r**4
                +(-34*t**2-384*t-864)*r**3+(-20*t**2+144*t+1152)*r**2
                +(21*t**2+360*t-432)*r+16*t**2-192*t)
        b0 = 12-t-(12+t)*r
        num = -r*b0-8*t*(1-r*r)
        den = r*b0-3*(4+t)*(1-r*r)
        mark = sp.cancel(3*(1+r)*den/(den+num))
        center = [3,3*(1-h)/2,3*(1-h),3*h,0,3*(1-h)/2,3*(2*h-1),
                  3*(1-h)/2,0,3*h,3*(1-h),3*(1-h)/2]
        transversal = [-sp.Rational(x, 4) for x in (2,0,1,0,-1,0,-2,0,-1,0,1,0)]
    active = [i for i in range(1,n) if center[i] != 0]
    inactive = n-1-len(active)
    b, c = cv(sp.Rational(inactive,n)), cv(sp.Rational(n-1,n))
    def scalar(expr):
        return F(sp.sympify(expr).subs(h, (7+root13)/18))
    a = [scalar(transversal[i]/center[i]) for i in active]
    if q == 25:
        tang = [scalar(sp.diff(center[i],h)/center[i]) for i in active]
        coef = sum(x*y for x,y in zip(a,tang))/sum(x*x for x in tang)
        a = [x-coef*y for x,y in zip(a,tang)]
    # The two inactive square coordinates are one orbit. Since 1 is in K
    # and L is invariant, L*1 is constant there. The prime has one such site.
    rr = sum(a)/inactive-b
    predicted = (sum(x*x for x in a)-inactive*rr*rr)/n+2*b**3/3+c**3/6

    def product(A,B):
        return [sum((A[j]*B[i-j] for j in range(i+1)),cv(0)) for i in range(4)]
    def evaluate(expr, series):
        ans = [cv(0)]*4
        for (i,j), coeff in sp.Poly(expr,t,r).terms():
            term = [cv(coeff)]+[cv(0)]*3
            for _ in range(j):
                term = product(term,series)
            for k in range(i,4):
                ans[k] += term[k-i]
        return ans
    series = [scalar(init)]+[cv(0)]*3
    deriv = evaluate(poly.diff(r),series)[0]
    for i in range(1,4):
        series[i] = -evaluate(poly,series)[i]/deriv
    assert not any(evaluate(poly,series))
    numerator, denominator = map(lambda z: evaluate(z,series), sp.fraction(mark))
    coeff = []
    for j in range(4):
        coeff.append((numerator[j]-sum(denominator[j-i]*coeff[i] for i in range(j)))/denominator[0])
    x,y,z = [v/coeff[0] for v in coeff[1:]]
    actual = z-x*y+x**3/3+c**3/6
    assert actual == predicted
    print(json.dumps(dict(field=q,side="plus" if q==13 else "minus",
                          cubic=str(field.to_sympy(actual)),bulk_J=inactive),
                     sort_keys=True))


if __name__ == "__main__":
    for q in [13,25]:
        check(q)
