# 70. Climbing Stairs

Easy · Math / Dynamic Programming / Memoization

[Original problem](https://leetcode.com/problems/climbing-stairs/) · Confirmed Accepted: 2026-10-22

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) average; O(n^2) worst case.

Auxiliary space complexity: O(n).

Why: The loop runs from step 3 through n, so it performs O(n) iterations. Each iteration makes two dictionary lookups and one insertion: average O(1) per operation, but worst-case O(n) with collisions, giving O(n^2) overall. The memo dictionary stores counts for steps 1 through n, using O(n) auxiliary space.
