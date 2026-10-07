# Daily publishing workflow

All scheduled times use **Asia/Singapore (UTC+08:00)**. Midnight is 16:00 UTC on the preceding calendar date; 5am is 21:00 UTC on the preceding calendar date.

The ChatGPT/Codex local task is the scheduler. It chooses and records questions at midnight, checks completion and analyzes code at 5am, and runs the publisher after those steps succeed. Existing tolerance, profile checks, explicit acceptance confirmation, and journal baseline checks still apply.

## Midnight

1. Convert the heartbeat timestamp to Singapore time and resolve the intended date.
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
- A local lock prevents overlapping syncs. Dirty tracked changes or conflicts stop publishing with a visible error.
- Each publishing run fetches remote updates with `git pull --ff-only` before generating the snapshot.
- Identical content creates no extra commit. A failed push remains retryable on the next run.
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
