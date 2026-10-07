# 110. Balanced Binary Tree

Easy · Tree / Depth-First Search / Binary Tree

[Original problem](https://leetcode.com/problems/balanced-binary-tree/) · Confirmed Accepted: 2026-10-03

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) in the worst case.

Space complexity: O(h) auxiliary, where h is the tree height; O(n) in the worst case.

Why: The helper visits each node at most once and may stop early on an imbalance; recursion uses one stack frame per active root-to-leaf path.
