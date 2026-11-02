# 1143. Longest Common Subsequence

Medium · String / Dynamic Programming

[Original problem](https://leetcode.com/problems/longest-common-subsequence/) · Confirmed Accepted: 2026-10-26

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(mn), where m = len(text1) and n = len(text2).

Auxiliary space complexity: O(mn).

Why: The outer loop visits each character in text2 and the inner loop visits each character in text1. Each character pair is compared once with constant-time table updates. The DP matrix has (m + 1) by (n + 1) entries.
