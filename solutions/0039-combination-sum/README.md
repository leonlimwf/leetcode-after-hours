# 39. Combination Sum

Medium · Array / Backtracking

[Original problem](https://leetcode.com/problems/combination-sum/) · Confirmed Accepted: 2026-10-29

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(N * C(N + D, D) + S * D), where N is the number of candidates, D is at most floor(target / min(candidates)) + 1, and S is the number of returned combinations.

Auxiliary space complexity: O(D), excluding returned results. The recursive call stack and mutable path grow with the path depth; the result list uses O(S * D) output space.

Why: Each nonterminal call scans candidate indices from start to the end, up to N choices, and recursively explores nondecreasing index sequences up to depth D. C(N + D, D) bounds the number of partial sequences. Each successful path.copy() copies up to D values.
