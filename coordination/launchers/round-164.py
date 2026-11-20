"""Launch the three selected round-164 research calls with a bound before record."""

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
BATCH = "round-164"
CALLS = {
    "ordinary-prime-signed-cofactor-exchange": (
        "gpt-6.2-astra",
        "Work on actual zero columns U prime. For each k-1 row set I use "
        "its cofactor Fourier polynomial g_I, and the exact signed Jacobi "
        "mass half of (||v_I||^2 + epsilon <v_I,K v_I> - |g_I(1)|^2). "
        "Key test is lower aggregate replacement mass well above (k/T)B "
        "where B sums constant-row weights. The cofactor adjugate identity "
        "without a new estimate is circular. Aim for a genuine signed "
        "cofactor estimate at actual high rank or a quantifiable actual "
        "leakage bound with correct witness mean and norm."
    ),
    "ordinary-prime-weighted-affine-ratio": (
        "gpt-6.2-astra",
        "Keep genuine physical X,Y and original slope f(t). If a+b>1, "
        "the ratio r_u(x)=u+(1-u)/A_x has a fixed positive characteristic "
        "amplitude by the actual covariance inequality; the slope is "
        "r_u(y)/r_u(x). Try to combine this third high set with the first "
        "two through affine or inverse incidence, or use its conditional "
        "weighted spectrum. Seek a slice beyond sigma>=26/27 in the "
        "high-high case or an explicit signed saving with fixed moderate slopes."
    ),
    "cold-prime-quadratic-source-block": (
        "gpt-6.2-astra",
        "Choose a specific short block on the true even-word Taylor "
        "source with its two actual R factors. Test a signed invariant "
        "or a label-by-label gain for powers of the genuine D602 on this "
        "source. Keep both lifts, actual mark and original Q. Distinguish "
        "inverse times Kr from inverse times K squared r before claiming "
        "a nonlinear transfer. A repeat of the divergent absolute "
        "majorant does not address the new question."
    ),
}

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
    coord_rel = "coordination/round-163.json"
    accepted_rel = "research/round-163-acceptance.json"
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
            payload["reasoning_effort"] = "high" if call_id == "ordinary-prime-signed-cofactor-exchange" else "medium"
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
        "round": 164,
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
