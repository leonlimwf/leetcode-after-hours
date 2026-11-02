# 91. Decode Ways

Medium · String / Dynamic Programming

[Original problem](https://leetcode.com/problems/decode-ways/) · Confirmed Accepted: 2026-10-26

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n), where n = len(s).

Auxiliary space complexity: O(n).

Why: The loop processes each index once. Each iteration performs constant-time DP updates; the two-character slice and integer conversion are bounded to at most two characters. The dp list stores n + 1 values.
