# 74. Search a 2D Matrix

Medium · Array / Binary Search / Matrix

[Original problem](https://leetcode.com/problems/search-a-2d-matrix/) · Confirmed Accepted: 2026-10-13

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(log(m × n)).

Auxiliary space complexity: O(1).

Why: Each iteration halves the search range among the m × n cells and does constant work. The code stores only a fixed number of indices and values; it does not copy the matrix.
