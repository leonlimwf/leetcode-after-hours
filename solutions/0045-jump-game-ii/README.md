# 45. Jump Game II

Medium · Array / Dynamic Programming / Greedy

[Original problem](https://leetcode.com/problems/jump-game-ii/) · Confirmed Accepted: 2026-11-02

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n). The loop visits each index before the last once, and each iteration performs constant work.

Auxiliary space: O(1). The function keeps only three counters; it creates no input-sized data structure.

Why: The range has n - 1 iterations, and the code updates only jumps, current_end, and farthest. No recursion or extra collection grows with n.
