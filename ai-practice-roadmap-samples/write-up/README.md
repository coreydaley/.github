# What six test cases taught me about a PR summary prompt

*A sample write-up for the [AI Practice Roadmap](../../AI-Practice-Roadmap.md).
October 2026.*

I wrote a small agent skill, [`summarize-pr`](../skill/summarize-pr/SKILL.md),
that summarizes a pull request in three parts: what changed, why, and what a
reviewer should watch for. Then I wrote [six test cases](../eval/summarize-pr/)
for it and a script that scores every summary. All runs used Claude Haiku
through Claude Code. The saved output of every run is in
[`results/`](../eval/summarize-pr/results/).

## The test cases

Each case is a small diff plus what a good summary has to do:

| Case | The change | What the summary must do |
|---|---|---|
| login-lockout | Lock accounts after 5 failed logins | Mention the lock and the number 5 |
| tls-verify-off | Turn off TLS certificate checks to "fix the flaky webhook test" | Mention the certificate check; give the stated reason |
| timeout-default | Default timeout from 30 to 5 seconds, no description | Mention both numbers; say "Not stated." for the reason |
| new-dependency | Add the `httpx` library | Name it and call it a dependency |
| pure-rename (later readme-typo) | A change with nothing risky in it | Say "Nothing unusual." |
| admin-check-removed | Delete an admin-only check, described as "clean up" | Mention the admin check |

Every case also checks the format (three labelled sections) and the length
(at most 120 words).

## Run 1: 3 of 6

- **login-lockout** was 123 words. The content was better than I asked for:
  it noticed that the "try again in 15 minutes" message had no timer behind
  it, so the lock was permanent, and that anyone could lock anyone's
  account. It just listed four warnings when three would do.
- **tls-verify-off** said the reason was "Not stated." The PR did give one
  ("fix the flaky webhook test"); the model didn't believe it. My rule said
  "if nothing says why, write Not stated," which left room for that.
- **pure-rename** flagged that renaming `get_usr` to `get_user` could break
  callers outside the diff. That's a fair warning. **The test was wrong, not
  the model.** A function rename isn't a "nothing to flag" change.

## What I changed

In the skill, two rules:

- "Give the reason the PR states, even if it doesn't convince you, and raise
  your doubt under Watch for instead. Write 'Not stated.' only when nothing
  in the PR or the code gives a reason."
- "List at most three Watch for items, most important first."

In the test set, I replaced the rename with a README typo fix, which really
has nothing to flag.

## Run 2: 5 of 6, then 6 of 6

The length and the TLS reason both passed. The new typo case failed: the
description was "Fix typos in the README," and the model said the reason
was "Not stated." Again I think the model was right. That description says
*what* changed, not *why*. I stopped checking the reason for that case, and
re-scored the same saved output: 6 of 6.

## Run 3: 5 of 6

Same skill, same tests, run again. The TLS case failed again: "Not stated,"
plus 122 words. The model still won't repeat a reason it finds unconvincing
in the "Why" line, even with the new rule. One passing run had hidden that.

## What I took from it

- **When a case fails, first ask whether the test is wrong.** Two of my
  five failures were mine, not the model's. Writing the expected answer is
  harder than it looks.
- **Be careful changing tests after seeing the output.** It's the easiest
  way to make a number go up without anything getting better. Each change
  I made had a reason I'd defend without having seen the output (a rename
  *can* break callers; "fix typos" isn't a reason). If I couldn't say that,
  I'd have left the test alone.
- **One run proves nothing.** The same prompt passed and then failed on the
  same case. Run each case several times and count how often it passes.
- **The test only checks what you wrote down.** The best parts of the
  summaries (the permanent lock, the reset that was never saved, "the fix
  belongs in the test, not production code") weren't checked by anything.
  A test set tells you about regressions in what you thought of, not about
  quality in general.

## What I'd do next

- Run every case five times and report a pass rate per case, not one score.
- Decide what I actually want for TLS-style cases. Maybe "the stated reason,
  and whether the code supports it" is the better rule, and the test should
  change to match.
- Grow the set from six to twenty with real pull requests from my own
  repos, especially ones where a reviewer missed something.
