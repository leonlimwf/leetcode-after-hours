# 153. Find Minimum in Rotated Sorted Array

Medium · Array / Binary Search

[Original problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) · Confirmed Accepted: 2026-10-13

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(log n).

Auxiliary space complexity: O(1).

Why: Each loop iteration reduces the search interval by about half, and each iteration does constant work. Only a fixed number of indices are stored; the input list is not copied.
