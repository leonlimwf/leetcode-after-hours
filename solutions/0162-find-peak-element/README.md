# 162. Find Peak Element

Medium · Array / Binary Search

[Original problem](https://leetcode.com/problems/find-peak-element/) · Confirmed Accepted: 2026-10-11

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(log n).

Auxiliary space: O(1).

Why: Each loop iteration halves the remaining interval; the code stores only a fixed set of indices and pointers.
