# 235. Lowest Common Ancestor of a Binary Search Tree

Medium · Tree / Depth-First Search / Binary Search Tree / Binary Tree

[Original problem](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · Confirmed Accepted: 2026-10-04

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time  O(h), where h is the tree height. The loop follows one root-to-leaf path: O(log n) for a balanced tree and O(n) in the worst-case skewed tree.

Space  O(1) auxiliary space. The iterative approach keeps only a current-node pointer and does not use recursion or an extra data structure.
