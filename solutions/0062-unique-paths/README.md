# 62. Unique Paths

Medium · Math / Dynamic Programming / Combinatorics

[Original problem](https://leetcode.com/problems/unique-paths/) · Confirmed Accepted: 2026-10-27

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(mn).

Auxiliary space complexity: O(mn).

Why: Creating the m by n DP table takes O(mn) time and space. The first-row and first-column loops take O(n + m); the nested loops visit each remaining cell once and do constant work, also O(mn). Returning dp[-1][-1] takes O(1).
