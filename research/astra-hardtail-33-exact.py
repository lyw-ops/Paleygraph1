"""Exact rational replay of the cyclic dyadic obstruction. Stdout only."""
from fractions import Fraction as F
import json

def emit(x):print(json.dumps(x,sort_keys=True),flush=True)
def rat(x):return str(x)
def dyadic(k,tau=F(1,20)):
 assert k>=4 and k%2==0
 n=2**k;c=tau/n;W=1+(n-1)*c;rho=tau/W;kap=(1-c)/W
 ts=[rho+kap*2**j for j in range(k+1)]
 U=[F(1)];V=[F(1)];us=[];vs=[]
 for j in range(1,k+1):
  if j%2==0:
   us.append(rho/V[-1]);vs.append(V[-1]);U.append(ts[j]/V[-1]);V.append(V[-1])
  else:
   us.append(U[-1]);vs.append(rho/U[-1]);U.append(U[-1]);V.append(ts[j]/U[-1])
 us.append(U[-1]);vs.append(V[-1]);sizes=[2**(k-j) for j in range(1,k+1)]+[1]
 assert sum(sizes)==n and sum(m*x for m,x in zip(sizes,us))==n
 assert sum(m*x for m,x in zip(sizes,vs))==n
 assert all(us[i]*vs[i]==rho for i in range(k)) and us[k]*vs[k]==F(n,1)/W
 def proj(f,parity):
  rootmeans=[sum(sizes[i]*f[i] for i in range(j,k+1))/F(2**(k-j)) for j in range(k+1)]
  out=[]
  for l in range(k+1):
   val=F(0)
   for j in range(1,k+1):
    if j%2!=parity:continue
    ej=rootmeans[j] if j<=l else f[l]
    ep=rootmeans[j-1] if j-1<=l else f[l]
    val+=ej-ep
   out.append(val)
  return out
 assert proj(us,1)==[0]*(k+1) and proj(vs,0)==[0]*(k+1)
 R=U[k-4];L=U[k-2]-R
 f=[max(x-R,F(0)) for x in us];f[k]=0
 assert [(i,sizes[i]) for i in range(k) if f[i]>0]==[(k-2,2)]
 assert f[k-2]==L
 z=proj(f,1);d=[rho/x for x in us];eta=sum(m*x for m,x in zip(sizes,f))/n
 H2=W/n*sum(m*di*zi*zi for m,di,zi in zip(sizes,d,z));ratio=H2/eta
 assert eta==2*L/n and z[k-1]==-L*F(n+2,3*n)
 lower=W*L*V[k-1]*F((n+2)**2,18*n*n)
 assert ratio>=lower
 assert lower==W*ts[k-1]*(1-ts[k-3]/ts[k-2])*F((n+2)**2,18*n*n)
 energies=[W/n*sum(m*(x-1)**2 for m,x in zip(sizes,src)) for src in [us,vs]]
 assert all(e<=W*(k+1) for e in energies)
 # Dyadic u/v bounds used in the exact UI proof; squared to avoid radicals.
 for j in range(1,k+1):
  assert us[j-1]**2<=2**j and vs[j-1]**2<=2**j
 assert us[k]**2<=n and vs[k]**2<=n
 # Full exact spatial replay at the first two dimensions independently audits
 # the conditional-expectation projector and every shifted cross correlation.
 dense_checks=False
 if k<=6:
  def shell(i):return k if i==0 else (i&-i).bit_length()-1
  uf=[us[shell(i)] for i in range(n)];vf=[vs[shell(i)] for i in range(n)];ff=[f[shell(i)] for i in range(n)]
  for shift in range(n):assert sum(uf[(i+shift)%n]*vf[i] for i in range(n))==n
  for i in range(n):
   value=F(0)
   for j in range(1,k+1,2):
    ej=sum(ff[h] for h in range(i%2**j,n,2**j))/F(n//2**j)
    ep=sum(ff[h] for h in range(i%2**(j-1),n,2**(j-1)))/F(n//2**(j-1))
    value+=ej-ep
   assert value==z[shell(i)]
  dense_checks=True
 emit({'kind':'exact_cyclic_UI_obstruction','k':k,'n':n,'tau':rat(tau),
       'R':rat(R),'eta':rat(eta),'H2':rat(H2),'ratio':rat(ratio),
       'ratio_over_n_decimal':float(ratio/n),'lower_over_n_decimal':float(lower/n),
       'rigorous_ratio_lower':rat(lower),'limiting_lower_over_n':'1/72',
       'energy_A_decimal':float(energies[0]),'energy_B_decimal':float(energies[1]),
       'exact_sector_product_mass_checks':True,'exact_dense_checks':dense_checks,
       'K_diagonal':rat(F(n-1,3*n)),
       'scope':'cyclic even reflection; lacks Paley coherence and sector dimensions'})
if __name__=='__main__':
 for k in [4,6,8,10,12,16,20,24]:dyadic(k)
 emit({'kind':'all_checks_passed','arithmetic':'fractions.Fraction; all identities and inequalities exact','records':8})
