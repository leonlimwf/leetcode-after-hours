# 150. Evaluate Reverse Polish Notation

Medium · Array / Math / Stack

[Original problem](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · Confirmed Accepted: 2026-10-08

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n), where n is the number of tokens.

Auxiliary space complexity: O(n) in the worst case.

Why: One pass over n tokens; the operator list has four entries. Pops are O(1) and appends amortized O(1). The stack may hold O(n) operands; arithmetic is bounded by the problem constraints.
