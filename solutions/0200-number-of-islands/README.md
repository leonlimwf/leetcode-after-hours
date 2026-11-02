# 200. Number of Islands

Medium · Array / Depth-First Search / Breadth-First Search / Matrix / Union Find

[Original problem](https://leetcode.com/problems/number-of-islands/) · Confirmed Accepted: 2026-10-31

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(m × n) on average. The nested loops inspect each cell, and DFS visits each land cell once while checking four neighbors. Set membership is average O(1).

Worst-case note: Pathological hash collisions can make a set operation O(m × n), giving a theoretical O((m × n)²) time bound.

Auxiliary space: O(m × n). The visited set can hold every cell, and recursive DFS can reach O(m × n) depth for one large island.
