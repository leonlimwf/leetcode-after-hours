# 238. Product of Array Except Self

Medium · Array / Prefix Sum

[Original problem](https://leetcode.com/problems/product-of-array-except-self/) · Confirmed Accepted: 2026-09-30

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n).

Space complexity: O(1) auxiliary, excluding the returned output array; O(n) including the output.

Why: Two linear passes compute prefix and suffix products, while only scalar products and the output list are stored.
