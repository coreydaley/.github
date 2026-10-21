#!/usr/bin/env python3
"""Test the summarize-pr skill against a fixed set of pull requests.

Each case in cases.json is a small diff plus what a good summary must do:
mention certain things, say "Not stated." when no reason is given, and flag
(or not flag) something for the reviewer. The script runs the skill on every
case, checks each summary, and prints a score.

Run it:
    python3 run_eval.py                      # uses Claude Code (`claude -p`)
    python3 run_eval.py --model haiku        # pick the model
    python3 run_eval.py --rescore results/<file>.json   # re-check saved output

Needs Claude Code installed and signed in. Only the standard library is used.
"""

import argparse
import datetime
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
SKILL = HERE.parent.parent / "skill" / "summarize-pr" / "SKILL.md"
MAX_WORDS = 120


def skill_instructions() -> str:
    text = SKILL.read_text()
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)  # drop front matter


def summarize(case: dict, model: str) -> str:
    prompt = (
        "Summarize this pull request. Answer with the summary only.\n\n"
        f"PR description: {case['description'] or '(none)'}\n\n"
        f"Diff:\n```diff\n{case['diff']}```\n"
    )
    out = subprocess.run(
        # The prompt goes in on stdin: --tools takes a list and would swallow it.
        ["claude", "-p", "--model", model, "--system-prompt", skill_instructions(),
         "--no-session-persistence", "--tools", ""],
        input=prompt, capture_output=True, text=True, timeout=180,
        cwd=tempfile.gettempdir(),  # keep this repo's CLAUDE.md files out of the run
    )
    if out.returncode != 0:
        sys.exit(f"claude failed on {case['id']}: {(out.stderr or out.stdout).strip()}")
    return out.stdout.strip()


def field(summary: str, name: str) -> str:
    m = re.search(rf"\*\*{name}:\*\*(.*?)(?=\n\*\*|\Z)", summary, flags=re.S)
    return m.group(1).strip() if m else ""


def check(case: dict, summary: str) -> list[str]:
    """Return the problems found; an empty list means the case passed."""
    problems = []
    low = summary.lower()
    for name in ("What changed", "Why", "Watch for"):
        if f"**{name}:**" not in summary:
            problems.append(f"missing the '{name}' section")
    words = len(summary.split())
    if words > MAX_WORDS:
        problems.append(f"{words} words (limit {MAX_WORDS})")
    for group in case["must_mention"]:
        if not any(term.lower() in low for term in group):
            problems.append(f"doesn't mention any of: {', '.join(group)}")
    why = field(summary, "Why").lower()
    if case["why_stated"] is False and "not stated" not in why:
        problems.append("guessed a reason; should say 'Not stated.'")
    if case["why_stated"] is True and "not stated" in why:
        problems.append("said 'Not stated.' but the PR gives a reason")
    nothing = "nothing unusual" in field(summary, "Watch for").lower()
    if case["expect_watch_items"] and nothing:
        problems.append("said 'Nothing unusual.' but there's something to flag")
    if not case["expect_watch_items"] and not nothing:
        problems.append("flagged something on a change with nothing to flag")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--rescore", type=Path, help="check a saved results file instead of calling the model")
    args = ap.parse_args()

    cases = json.loads((HERE / "cases.json").read_text())
    if args.rescore:
        summaries = json.loads(args.rescore.read_text())["summaries"]
    else:
        summaries = {}
        for case in cases:
            print(f"running {case['id']}…", file=sys.stderr)
            summaries[case["id"]] = summarize(case, args.model)
        results = HERE / "results"
        results.mkdir(exist_ok=True)
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        saved = results / f"{stamp}-{args.model}.json"
        saved.write_text(json.dumps({"model": args.model, "summaries": summaries}, indent=2) + "\n")
        print(f"saved {saved.relative_to(HERE)}", file=sys.stderr)

    cases = [c for c in cases if c["id"] in summaries]  # older runs may predate a case
    passed = 0
    for case in cases:
        problems = check(case, summaries[case["id"]])
        passed += not problems
        print(f"{'PASS' if not problems else 'FAIL'}  {case['id']}")
        for p in problems:
            print(f"      - {p}")
    print(f"\n{passed} of {len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
