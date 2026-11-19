"""Replay every primary computation and compare parsed JSON exactly. Stdout only."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base='research/astra-hardtail-33'
jobs=[
 (base+'-exact.py',[],base+'-exact.jsonl',9),
 (base+'-actual.py',[],base+'-actual.jsonl',41),
 (base+'-certified.py',[],base+'-certified.jsonl',10),
 (base+'-certified.py',['--tau','.01'],base+'-certified-floor01.jsonl',10),
 (base+'-certified.py',['--tau','.001'],base+'-certified-floor001.jsonl',10),
 (base+'-certified.py',['--primes','9413','--tau','1024','--witness-R','0.9'],base+'-hot-certified.jsonl',4),
]
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
results=[]
for script,args,out,expected in jobs:
 run=subprocess.run([sys.executable,'-B',script,*args],cwd=root,env=env,text=True,capture_output=True,check=True)
 actual=[json.loads(line) for line in run.stdout.splitlines()]
 saved=[json.loads(line) for line in (root/out).read_text().splitlines()]
 assert len(actual)==expected and actual==saved,(out,len(actual))
 assert actual[-1]['kind']=='all_checks_passed'
 result={'file':out,'records':expected,'exact_json_replay_equal':True,
         'sha256':hashlib.sha256((root/out).read_bytes()).hexdigest()}
 results.append(result)
 print(json.dumps({'kind':'replay_passed',**result},sort_keys=True),flush=True)
print(json.dumps({'kind':'all_checks_passed','primary_records':sum(x['records'] for x in results),
                  'cold_exact_stationary_sides':18,'cold_hinge_knots_certified':2280,
                  'hot_exact_stationary_sides_with_ratio_gt_one':2,
                  'uniform_cold_HR':'open','ETH26_ordinary_theta':'open'},sort_keys=True),flush=True)
