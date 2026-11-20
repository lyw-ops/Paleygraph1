"""Launch the three selected round-153 research calls with a bound before record."""

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
BATCH = "round-153"
CALLS = {'ordinary-prime-weighted-affine-fourth-moment': ('gpt-6.2-astra',
                                                  'Work with the exact near-critical actual retargeted '
                                                  'b and its true anchor law ν=b/Σb. Uniform anchors '
                                                  'exactly give O(p), while this ν-weighted sum is '
                                                  'forced to be ω(p) unless the near-critical branch '
                                                  'is excluded. Analyze the explicit off-diagonal '
                                                  'five-factor formula from R152. For example use '
                                                  'z=1−v x and T_u z=1−u+u z, then expand f in the '
                                                  'actual characters with weights ν. Conditional on u, '
                                                  'z and zprime sums may factor into two shifted '
                                                  'Jacobi sums with all quadratic lift conditions. '
                                                  'Classify the ensuing ν-weighted resonances and use '
                                                  'genuine ordinary-prime estimates on the actual '
                                                  'critical distribution. An O(p) upper here excludes '
                                                  'the branch. Give a precise partial arithmetic bound '
                                                  'or obstruction if no full estimate. Do not '
                                                  'substitute uniform anchors or assume additive '
                                                  'energy or periodicity.'),
 'ordinary-prime-first-spill-face-upper': ('gpt-6.2-astra',
                                           'Use exact R152 signed and clipped objectives on the '
                                           'original full high receiver and original true common '
                                           'complementary zeros, both roots and the diagonal excluded. '
                                           'Their face maxima differ by o(1). Prove a genuine '
                                           'prime-only upper on one maximum with a concrete feasible '
                                           'primal selection or bound over all dual minorants by '
                                           'actual phase/arithmetic. If no full bound, isolate a '
                                           'rigorous source or cost component using real adaptive '
                                           'geometry. Do not repeat the static minimum/maximum '
                                           'identity alone.'),
 'cold-three-center-actual-square-omission': ('gpt-6.2-astra',
                                              'B3 now uses all powers of the actual S, alphaY and '
                                              'betaW with exact W weights. The original marked Picard '
                                              'omissions outside B3 at heights 601,602 are '
                                              '<.4112/.4122. Need actual same-height signed difference '
                                              '<.50179639. Track the true fixed other centers and '
                                              'genuine residual separately. Seek a signed arithmetic '
                                              'overlap on all translated columns or an explicit '
                                              'leading gammaF4 or Picard slice with correct tail/mark. '
                                              'Retain B3 actual under both lifts; a positive-envelope '
                                              'obstruction alone is not a signed refutation.')}

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
    coord_rel = "coordination/round-152.json"
    accepted_rel = "research/round-152-acceptance.json"
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
            payload["reasoning_effort"] = "high" if call_id == "ordinary-prime-weighted-affine-fourth-moment" else "medium"
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
        "round": 153,
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
