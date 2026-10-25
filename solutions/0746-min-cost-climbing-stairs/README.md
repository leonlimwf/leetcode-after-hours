# 746. Min Cost Climbing Stairs

Easy · Array / Dynamic Programming

[Original problem](https://leetcode.com/problems/min-cost-climbing-stairs/) · Confirmed Accepted: 2026-10-25

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n), where n = len(cost).

Auxiliary space complexity: O(n).

Why: The loop visits each position from 2 through n once and does constant work per position. The res array stores n + 1 values; the returned output is a single integer.
