# 104. Maximum Depth of Binary Tree

Easy · Tree / Depth-First Search / Breadth-First Search / Binary Tree

[Original problem](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · Confirmed Accepted: 2026-10-01

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n).

Space complexity: O(h) auxiliary, where h is the tree height; O(n) in the worst case.

Why: The recursion visits each node once and stores at most h active calls on the call stack.
