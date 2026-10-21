# AI Practice Roadmap samples

Small, working examples of the four kinds of output described in the
[AI Practice Roadmap](../AI-Practice-Roadmap.md). They're built around one
everyday job, summarizing pull requests, so you can see how the pieces fit
together:

| Sample | What it is | Roadmap area |
|---|---|---|
| [`skill/summarize-pr`](skill/summarize-pr/SKILL.md) | An **agent skill**: instructions an agent loads when asked to summarize a pull request | What you'll build |
| [`workflow/release-notes`](workflow/release-notes/SKILL.md) | A **workflow**: four fixed steps (collect, draft, independent review, revise) with a file handed from each step to the next. It uses the skill above in step 1. | 5. Multi-agent orchestration |
| [`eval/summarize-pr`](eval/summarize-pr/) | A **test set**: six pull requests, what a good summary of each must do, and a script that runs the skill on all six and scores it | 1. Evals |
| [`write-up`](write-up/README.md) | A **write-up** of running that test set: what failed, what I changed, and the numbers before and after | Public work |

## Using them

The skill and the workflow are [Claude Code](https://claude.com/claude-code)
skills: a folder with a `SKILL.md` file. To try one, copy its folder into
`~/.claude/skills/` (for all your projects) or `.claude/skills/` inside one
project, then ask Claude Code to "summarize this PR" or "write release notes
since the last tag".

The eval needs Python 3 and Claude Code installed and signed in:

```sh
cd eval/summarize-pr
python3 run_eval.py --model haiku
```

It calls the model once per test case, saves the summaries under `results/`,
and prints a score. `python3 run_eval.py --rescore results/<file>.json`
re-checks a saved run without calling the model again.

These are teaching samples: small on purpose, and not meant to be
complete tools.
