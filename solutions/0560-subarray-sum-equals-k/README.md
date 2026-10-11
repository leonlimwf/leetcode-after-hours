# 560. Subarray Sum Equals K

Medium · Array / Hash Table / Prefix Sum

[Original problem](https://leetcode.com/problems/subarray-sum-equals-k/) · Confirmed Accepted: 2026-10-11

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) average; O(n²) worst case if dictionary operations degrade under collisions.

Auxiliary space: O(n), for the prefix list, its slice, and the frequency dictionary.

Why: The code makes two linear passes; each dictionary lookup/update is average O(1), but can be O(n) in the worst case.
