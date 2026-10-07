# 217. Contains Duplicate

Easy · Hash Table / Array

[Original problem](https://leetcode.com/problems/contains-duplicate/) · Confirmed Accepted: 2026-09-22

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) average; O(n^2) in the pathological worst case for hash collisions.

Space complexity: O(n) in the worst case.

Why: The array is scanned once, and set membership checks and insertions are average O(1). The set can store up to n distinct values. The O(n^2) bound is the theoretical collision-heavy hash-table case.
