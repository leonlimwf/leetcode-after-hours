# 215. Kth Largest Element in an Array

Medium · Array / Divide and Conquer / Sorting / Heap / Quickselect

[Original problem](https://leetcode.com/problems/kth-largest-element-in-an-array/) · Confirmed Accepted: 2026-10-21

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n log k). Each of the n values is pushed into a min-heap capped at k items; heap operations take O(log k), and a push may be followed by a pop.

Auxiliary space complexity: O(k). The heap retains at most k values; the loop variables use O(1) extra space.

Why: The code scans all n values once. Keeping the heap at size k makes each push/pop logarithmic in k, while the heap itself stores at most k elements.
