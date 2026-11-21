"""Launch the three selected round-150 research calls with a bound before record."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import http.client
import json
import os
from pathlib import Path
import subprocess
import sys
from threading import Lock
import time


ROOT = Path(__file__).resolve().parents[2]
BATCH = "round-150"
CALLS = {'ordinary-prime-selected-defect-phase': ('gpt-6.2-astra',
                                          'Derive a genuinely prime-sensitive bound for the same '
                                          'selected actual b_j. Its normalized pinned projection is '
                                          'small, its completed root is at least (1-o(1))n/z0 and the '
                                          'bulk mass has favorable phase '
                                          'c_sigma(i)=-sigma*(n/sqrt(p))*K_i0 with mean at least '
                                          'n/(sqrt(p)*z0)-o(1). The coexisting exact true opponent '
                                          'cost stays order one. R20 excludes tight high-energy '
                                          'supports. Work on the remaining supercritical/diffuse or '
                                          'tight low-energy regime with genuine character sums, '
                                          'additive energy, or a new restriction induced by the actual '
                                          'iterates. Explicitly check whether exact opposite feasible '
                                          'rows already falsify a proposed abstract bound. Return a '
                                          'genuinely new quantitative restriction or precisely isolate '
                                          'an unavoidable missing estimate.'),
 'ordinary-prime-first-spill-dyadic': ('gpt-6.2-astra',
                                       'Attack the original first reflected pair and retain '
                                       'max(Z_i,u), mean and pin in the exact failure threshold. '
                                       'Separate one actual pair sector by d or by the output level '
                                       'and compute the signed kernel or true optimizer mass there '
                                       'with correct normalization. If appropriate exploit exact '
                                       'P_sigma F=0 or the common complementary zero set, but do not '
                                       'assume cancellation of an adaptive threshold merely from Weil '
                                       'bounds for fixed translated intersections. One selected T, one '
                                       'true optimizer and cutoff suffice. Identify exactly which '
                                       'dyadic range or multi-input correlation remains.'),
 'cold-signed-legendre-unit': ('claude-fable-5-1',
                               'Use the actual omission H_h=C_oth+Y_h and isolate its linear term at '
                               'S+alphaY. Resolve the Legendre-unit component before taking moduli. On '
                               'good characters Y=(N+N^chi)/2 where N,N^chi have determinant-one '
                               'rank-two factors. Check whether the unit multiplicity in Y^(2r) really '
                               'is 2^(-2r)*sum_{j=0}^r binom(2r,2j)*Catalan_j*Catalan_{r-j}, or '
                               'correct for characters/lifts. Collect its signed seed-Laurent scalar '
                               'explicitly at actual complex alpha(t) through Taylor order 13 and '
                               'bound the tail. Explain how to price the unit and nonunit parts in the '
                               'two-boundary P5000 norm, including t0=n. If possible find a checked '
                               'signed saving or same-row square estimate. Use the actual finite-field '
                               'labels and avoid treating an unsigned lower witness as an actual '
                               'lower.')}

def reference(path, root=ROOT):
    return {
        "path": str(path.relative_to(root)),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def output(root, script, *args):
    return subprocess.run(
        [sys.executable, "-B", str(root / "scripts" / script), *args],
        cwd=root, check=True, text=True, capture_output=True,
    ).stdout


def write_exclusive(path, data):
    with path.open("xb") as stream:
        stream.write(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validation-root", type=Path, required=True)
    parser.add_argument("--result-dir", type=Path, required=True)
    parser.add_argument("--assessment", type=Path, required=True)
    args = parser.parse_args()
    token = os.environ.get("PALEY_GATEWAY_API_KEY")
    if not token:
        raise SystemExit("The authorized gateway credential is unavailable.")
    checked = args.validation_root.resolve()
    result_dir = args.result_dir.resolve()
    coord_rel = "coordination/round-149.json"
    accepted_rel = "research/round-149-acceptance.json"
    checked_paths = [coord_rel, accepted_rel, "scripts/round_review.py"]
    for relative in checked_paths:
        if (checked / relative).read_bytes() != (ROOT / relative).read_bytes():
            raise SystemExit(f"The validation copy differs at {relative}")
    print(output(checked, "round_review.py", "check", "--current").strip(), flush=True)
    plan = json.loads((ROOT / coord_rel).read_bytes())
    proposals = {call["id"]: call for call in plan["next_calls"]}
    manifest_path = ROOT / "coordination" / f"{BATCH}-inflight.json"
    if manifest_path.exists():
        raise SystemExit("The dispatch manifest already exists.")

    missions_dir = ROOT / "coordination" / "missions" / BATCH
    missions_dir.mkdir(parents=True, exist_ok=True)
    result_dir.mkdir(mode=0o700, exist_ok=True)
    if any(result_dir.iterdir()):
        raise SystemExit("The result directory already contains dispatch output.")
    prepared = {}
    for call_id, (model, direction) in CALLS.items():
        mission = output(checked, "round_review.py", "mission", "--call", call_id)
        mission_path = missions_dir / f"{call_id}.md"
        if mission_path.exists():
            if mission_path.read_bytes() != mission.encode():
                raise SystemExit(f"The existing mission differs at {mission_path}")
        else:
            write_exclusive(mission_path, mission.encode())
        notes = []
        for evidence in proposals[call_id]["inputs"]:
            source = ROOT / evidence["path"]
            if reference(source) != evidence:
                raise SystemExit(f"The source changed at {evidence['path']}")
            notes.append(f"REFERENCE {evidence['path']}\n{source.read_text()}")
        content = "\n\n".join((mission, direction, *notes))
        payload = {
            "model": model, "max_completion_tokens": 7000,
            "messages": [
                {"role": "system", "content": "Independent mathematical research. Do not modify files. "
                 "Give a checked result or precise failure and two ranked next tests. "
                 "Keep the actual prime family, physical marking, norms and order of limits explicit."},
                {"role": "user", "content": content},
            ],
        }
        if model == "gpt-6.2-astra":
            payload["reasoning_effort"] = "high" if call_id == "ordinary-prime-selected-defect-phase" else "medium"
        prepared[call_id] = (mission_path, hashlib.sha256(content.encode()).hexdigest(), payload)

    capture_args = [arg for call_id in CALLS for arg in ("--call", call_id)]
    bound = json.loads(output(ROOT, "shared_obligations.py", "capture",
                             "--batch", BATCH, "--coordinator", coord_rel,
                             "--assessment", str(args.assessment.resolve()), *capture_args))
    before = ROOT / bound["path"]
    if reference(before) != bound:
        raise SystemExit("The captured before bytes changed.")
    snapshot = json.loads(before.read_bytes())
    manifest = {
        "round": 150,
        "dispatch_status": "launch timestamps recorded per call",
        "accepted_checkpoint": reference(ROOT / accepted_rel),
        "coordinator": reference(ROOT / coord_rel),
        "launcher": reference(Path(__file__).resolve()),
        "shared_obligations_before": bound,
        "lanes": [
            {
                "call_id": call_id, "model": payload["model"], "prompt_sha256": prompt_hash,
                "mission_file": reference(mission_path),
                "shared_candidate_ids": snapshot["candidate_ids_by_call"][call_id],
                "pending_receipt": str(result_dir / f"{call_id}-receipt.json"),
                "pending_candidate": str(result_dir / f"{call_id}-candidate.md"),
            }
            for call_id, (mission_path, prompt_hash, payload) in prepared.items()
        ],
    }
    write_exclusive(manifest_path, (json.dumps(manifest, indent=2)+"\n").encode())
    lock = Lock()

    def launch(lane):
        call_id = lane["call_id"]
        connection = http.client.HTTPSConnection("api.appintheloop.com", timeout=420)
        result = {"completion": False}
        try:
            with lock:
                lane["started_utc_epoch"] = time.time()
                scratch = manifest_path.with_suffix(".tmp")
                scratch.write_text(json.dumps(manifest, indent=2)+"\n")
                scratch.replace(manifest_path)
            print(call_id, "started", flush=True)
            connection.request("POST", "/v1/chat/completions",
                               json.dumps(prepared[call_id][2]),
                               {"Authorization": "Bearer "+token, "Content-Type": "application/json"})
            response = connection.getresponse()
            result["http_status"] = response.status
            if response.status == 200:
                data = json.loads(response.read(4_000_000))
                choice = data["choices"][0]
                answer = choice.get("message", {}).get("content")
                if isinstance(answer, str) and answer:
                    write_exclusive(Path(lane["pending_candidate"]), (answer+"\n").encode())
                    result["completion"] = True
                result["model_matches"] = data.get("model") == lane["model"]
                reason = choice.get("finish_reason")
                result["finish_reason"] = reason if reason in {"stop","length","content_filter"} else "other"
                result["usage"] = {k:v for k,v in data.get("usage", {}).items() if type(v) is int}
        except (OSError, ValueError, KeyError, IndexError, http.client.HTTPException) as error:
            result["error_class"] = type(error).__name__
        finally:
            connection.close()
        write_exclusive(Path(lane["pending_receipt"]), (json.dumps(result)+"\n").encode())
        print(call_id, result, flush=True)

    with ThreadPoolExecutor(max_workers=len(CALLS)) as executor:
        list(executor.map(launch, manifest["lanes"]))


if __name__ == "__main__":
    main()
