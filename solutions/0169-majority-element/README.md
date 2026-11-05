# 169. Majority Element

Easy · Array / Hash Table / Divide and Conquer / Sorting / Counting

[Original problem](https://leetcode.com/problems/majority-element/) · Confirmed Accepted: 2026-11-05

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) average; O(n²) in the pathological worst case for hash collisions.

Auxiliary space: O(k), where k is the number of distinct values; O(n) in the worst case.

Why: The loop performs one average O(1) dictionary update per number, and max scans the k distinct keys, so average time is O(n). Pathological hash collisions can make dictionary operations O(n²). The dictionary stores up to k entries; returning one key creates no output collection.
