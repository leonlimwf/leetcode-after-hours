# 704. Binary Search

Easy · Array / Binary Search

[Original problem](https://leetcode.com/problems/binary-search/) · Confirmed Accepted: 2026-09-21

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(log n).

Space complexity: O(1).

Why: Each loop iteration discards half of the remaining search range, so there are O(log n) iterations. The code stores only left, right, mid, and target-related values, so extra space is O(1).
