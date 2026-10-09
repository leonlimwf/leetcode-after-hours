# 739. Daily Temperatures

Medium · Array / Stack / Monotonic Stack

[Original problem](https://leetcode.com/problems/daily-temperatures/) · Confirmed Accepted: 2026-10-09

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n), where n is the number of temperatures.

Auxiliary space complexity: O(n) for the stack of unresolved day indices. The required result array also uses O(n) output space.

Why: Each index is pushed once and popped at most once. Although the while loop is nested inside the for loop, all stack operations together are linear, so total time is O(n).
