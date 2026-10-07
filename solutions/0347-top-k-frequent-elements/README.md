# 347. Top K Frequent Elements

Medium · Array / Hash Table / Heap / Sorting

[Original problem](https://leetcode.com/problems/top-k-frequent-elements/) · Confirmed Accepted: 2026-09-27

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) average.

Space complexity: O(n).

Why: Counting and bucket placement take O(n) average; the bucket array has n + 1 slots, and scanning the buckets visits at most n stored values.
