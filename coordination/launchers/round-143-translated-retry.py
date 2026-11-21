"""Retry the unchanged round-143 translated mission with Astra after a gateway 429."""

import argparse
import hashlib
import http.client
import json
import os
from pathlib import Path
import runpy
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validation-root", type=Path, required=True)
    args = parser.parse_args()
    original = runpy.run_path(str(Path(__file__).with_name("round-143.py")))
    root, reference = original["ROOT"], original["reference"]
    output, write_exclusive = original["output"], original["write_exclusive"]
    token = os.environ["PALEY_GATEWAY_API_KEY"]
    source = root / "coordination/round-143-inflight.json"
    manifest = json.loads(source.read_bytes())
    original_call = "cold-translated-label-intersection"
    lane = next(item for item in manifest["lanes"] if item["call_id"] == original_call)
    assert json.loads(Path(lane["pending_receipt"]).read_bytes())["http_status"] == 429
    plan = json.loads((root / manifest["coordinator"]["path"]).read_bytes())
    assert reference(root / manifest["coordinator"]["path"]) == manifest["coordinator"]
    print(output(args.validation_root, "round_review.py", "check", "--current").strip(), flush=True)
    mission = output(args.validation_root, "round_review.py", "mission", "--call", original_call)
    assert (root / lane["mission_file"]["path"]).read_text() == mission
    direction = original["CALLS"][original_call][1]
    proposal = next(item for item in plan["next_calls"] if item["id"] == original_call)
    inputs = []
    for item in proposal["inputs"]:
        path = root / item["path"]
        assert reference(path) == item
        inputs.append(f"REFERENCE {item['path']}\n{path.read_text()}")
    content = "\n\n".join((mission, direction, *inputs))
    assert hashlib.sha256(content.encode()).hexdigest() == lane["prompt_sha256"]
    model = "gpt-6.2-astra"
    payload = {
        "model": model, "max_completion_tokens": 7000, "reasoning_effort": "medium",
        "messages": [
            {"role": "system", "content": "Independent mathematical research. Do not modify files. "
             "Give a checked result or precise failure and two ranked next tests. "
             "Keep the actual prime family, physical marking, norms and order of limits explicit."},
            {"role": "user", "content": content},
        ],
    }
    result_dir = Path(lane["pending_receipt"]).parent
    result_path = result_dir / f"{original_call}-astra-retry-receipt.json"
    candidate = result_dir / f"{original_call}-astra-retry-candidate.md"
    assert not result_path.exists() and not candidate.exists()
    retry_ref = root / "coordination/round-143-translated-retry.json"
    write_exclusive(retry_ref, (json.dumps({
        "original_dispatch": reference(source),
        "original_http_status": 429,
        "call_id": original_call,
        "model": model,
        "prompt_sha256": lane["prompt_sha256"],
        "launcher": reference(Path(__file__).resolve()),
        "started_utc_epoch": time.time(),
        "pending_receipt": str(result_path),
        "pending_candidate": str(candidate),
    }, indent=2)+"\n").encode())
    print(original_call, "Astra retry started", flush=True)
    result = {"completion": False}
    connection = http.client.HTTPSConnection("api.appintheloop.com", timeout=420)
    try:
        connection.request("POST", "/v1/chat/completions", json.dumps(payload),
                           {"Authorization": "Bearer "+token, "Content-Type": "application/json"})
        response = connection.getresponse()
        result["http_status"] = response.status
        if response.status == 200:
            data = json.loads(response.read(4_000_000))
            choice = data["choices"][0]
            answer = choice.get("message", {}).get("content")
            if isinstance(answer, str) and answer:
                write_exclusive(candidate, (answer+"\n").encode())
                result["completion"] = True
            result["model_matches"] = data.get("model") == model
            reason = choice.get("finish_reason")
            result["finish_reason"] = reason if reason in {"stop", "length", "content_filter"} else "other"
            result["usage"] = {k: v for k, v in data.get("usage", {}).items() if type(v) is int}
    except (OSError, ValueError, KeyError, IndexError, http.client.HTTPException) as error:
        result["error_class"] = type(error).__name__
    finally:
        connection.close()
    write_exclusive(result_path, (json.dumps(result)+"\n").encode())
    print(original_call, "Astra retry", result, flush=True)


if __name__ == "__main__":
    main()
