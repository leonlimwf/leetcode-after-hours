# Daily publishing workflow

All scheduled times use **Asia/Singapore (UTC+08:00)**. Midnight is 16:00 UTC on the preceding calendar date; 5am is 21:00 UTC on the preceding calendar date.

The ChatGPT/Codex local task is the scheduler. It chooses and records questions at midnight, checks completion and analyzes code at 5am, and runs the publisher after those steps succeed. Existing tolerance, profile checks, explicit acceptance confirmation, and journal baseline checks still apply.

## Midnight

1. Run the read-only coach preflight to convert the original heartbeat timestamp to Singapore time and resolve the intended date. Explicit scheduler phase/date metadata overrides automatic inference. Ten-minute early delivery is allowed; otherwise the latest due slot is used, with no hard lateness cutoff.
2. Reuse an existing assignment for that date. Otherwise randomly select one suitable new Easy or Medium problem, excluding every previously assigned, skipped, accepted, or observed solved slug.
3. Save the brief in the private journal and ledger; render-check journal changes and record the immutable midnight baseline.
4. Run `python3 scripts/sync.py --phase midnight --since 2026-09-16 --ledger /path/to/ledger.json --journal /path/to/journal.docx --publish` from this repository.
5. Notify the learner with the question, whether publishing succeeds or fails.

## 5am

1. Compare the pre-edit journal hash with the midnight baseline.
2. Inspect the assigned problem's actual code, even if already Accepted, and add or update the journal's Complexity Analysis block. Report no code when appropriate.
3. Check the live LeetCode profile before marking an unchanged entry missed. Keep profile acceptance separate from learner-confirmed acceptance.
4. Synchronize the journal tracker and ledger, preserving previously confirmed Accepted status.
5. Run `python3 scripts/sync.py --phase check --since 2026-09-16 --ledger /path/to/ledger.json --journal /path/to/journal.docx --publish`.
6. Report completion, complexity-analysis outcome, and GitHub publishing outcome separately.

The publisher does not determine Big-O, choose questions, confirm acceptance, or change the private journal or ledger. Those are the coach's responsibilities. It exports existing records, copies confirmed code without changing its algorithm, and reports missing analysis explicitly. A single leading space on a top-level `class` or `def` copied from Word is removed for Python syntax; internal indentation is preserved.

The learner approved publishing the existing solution archives and completion history on 8 October 2026. Always use `--since 2026-09-16` to retain that approved history alongside new assignments. Only the small allowlisted export is public; the source journal and full ledger remain local.

## Publishing safeguards

- Only this repository's allowlisted public paths are staged. Private source files are never copied.
- Every sync scans those paths for likely tokens, private keys, credentials in URLs, email addresses, local home/attachment paths, private filenames, unexpected file types, and symlinks. A match stops publishing without printing the matching value. Pattern checks supplement review; they cannot recognize every possible secret.
- The remote must be `leonlimwf/leetcode-after-hours`, and publishing uses `main`.
- An OS file lock prevents overlapping syncs and is automatically released if the publisher crashes. Dirty tracked changes or conflicts stop publishing with a visible error.
- Each publishing run fetches remote updates and fast-forwards only when behind. A prior unpushed local commit is retained; diverged histories stop for review.
- Source/output hashes let unchanged exports skip archive regeneration. Privacy checks still run on every attempt. No extra commit or push occurs when origin is already current.
- Exports are generated and validated in a temporary candidate directory before changed files replace the public snapshot. Concurrent private-input changes abort the export. Cache state contains only fingerprints in ignored `.sync.lock/`.
- A failed push remains retryable on the next run. Git commands have a 45-second timeout; the publisher never loops indefinitely or force-pushes.
- No force pushes, history rewriting, backdated commits, or automatic replacement of learner solutions.
- Python is syntax-checked, not executed. LeetCode supplies its tree/list node types at submission time.

## Manual preview and recovery

Requires Python 3.11 or later, Git, and a GitHub account with write access. Authenticate using `gh auth login`, then `gh auth setup-git` if needed. Never put a token in a file or remote URL.

```bash
python3 scripts/sync.py --phase check \
  --since 2026-09-16 \
  --ledger /path/to/ledger.json \
  --journal /path/to/journal.docx

git diff

python3 scripts/validate.py
```

Add `--publish` to commit and push. Preview mode updates only the generated public files. Resolve any unrelated Git changes before a publish run; the publisher will not stash or discard them.

The desktop computer must remain available for the local task. If it is asleep, the app is closed, authentication expires, or a network operation fails, automatic publishing cannot be guaranteed. The coach must report the failure and retry safely rather than claim the repository was updated.

## Fast coach preflight

```bash
python3 scripts/workflow.py inspect \
  --triggered-at 2026-10-07T21:00:00Z \
  --ledger /path/to/ledger.json --journal /path/to/journal.docx

python3 scripts/workflow.py profile --username leonlimwf \
  --ledger /path/to/ledger.json --record
```

The inspection returns the resolved slot, immutable baseline comparison, existing check, all unavailable problem slugs, a code/analysis inventory, and the exact current entry with code/analysis fingerprints. It never changes private files. Its output is private working context: do not commit it, upload it as a CI artifact, or copy free-form learner notes into public files. Use `--slug` to inspect a particular archived answer. If the scheduler explicitly identifies a phase and date, pass `--phase midnight` or `--phase check` and `--date YYYY-MM-DD`.

For a verified candidate shortlist, use `workflow.py pick --ledger /path/to/ledger.json --candidates /path/to/candidates.json --date YYYY-MM-DD`. Candidate JSON is an array of problem objects containing at least `slug` and `difficulty`. The selector excludes all assigned/accepted/skipped/observed history and reuses any saved assignment. A fresh random selection is read-only; save it in the ledger before repeating the command. It does not verify problem statements or constraints; the coach checks those against the original problem page.

The profile command reads only public solved counts and the most recent 20 Accepted submissions, with a bounded timeout and no login cookies. This is not complete solved history and cannot retrieve private submitted source code. It returns `browser_fallback_required` when unavailable; the coach must then inspect the public profile in the in-app browser. A failed lookup is not evidence of a missed session. Optional `--record --ledger` saves only successful observations in the private ledger, retaining earlier slugs and preserving every learner status, confirmation, check, and midnight baseline. Without `--record` it is read-only. Observation-timestamp or private-note changes alone do not invalidate the public export cache.

Code comes from the journal, not an invented ideal answer or a private LeetCode submission. Explicit code fences and labeled trailing notes are respected. Invalid Python is not shortened until it parses. If more than one `Solution` version is present, publishing stops until the learner identifies the submitted version. The coach still reviews clear pseudocode for complexity when Python extraction is unavailable.

## Continuous validation

The [GitHub workflow](../.github/workflows/validate.yml) runs regression tests and public validation on pushes, pull requests, and manual dispatch. Official action versions are commit-pinned, repository access is read-only, checkout credentials are not retained, and no private source material is provided. CI syntax-checks learner solutions; it does not execute them or pretend to verify LeetCode acceptance. Local checks are still mandatory before publishing: CI is a second check after upload, not a substitute for the pre-push privacy gate.
