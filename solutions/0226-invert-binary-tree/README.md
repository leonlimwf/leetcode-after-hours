# 226. Invert Binary Tree

Easy · Tree / Depth-First Search / Breadth-First Search / Binary Tree

[Original problem](https://leetcode.com/problems/invert-binary-tree/) · Confirmed Accepted: 2026-09-30

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n).

Space complexity: O(h) auxiliary, where h is the tree height; O(n) in the worst case.

Why: Every node is visited once, and the recursive calls occupy one stack frame per active root-to-leaf path.
