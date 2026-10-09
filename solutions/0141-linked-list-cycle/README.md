# 141. Linked List Cycle

Easy · Linked List / Two Pointers

[Original problem](https://leetcode.com/problems/linked-list-cycle/) · Confirmed Accepted: 2026-10-07

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n), where n is the number of distinct reachable nodes.

Auxiliary space complexity: O(1).

Why: Slow advances one link and fast two per iteration. An acyclic list ends in O(n) steps; with a cycle, they meet in O(mu + lambda) steps (prefix length mu, cycle length lambda). Only two pointers are stored.
