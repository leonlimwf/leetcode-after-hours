# 3. Longest Substring Without Repeating Characters

Medium · Hash Table / String / Sliding Window

[Original problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · Confirmed Accepted: 2026-09-23

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n) amortized.

Space complexity: O(min(n, a)), where a is the character-set size; O(n) in the general case.

Why: Each character is added to and removed from the set at most once as the left and right pointers move forward, so the inner while loop is amortized linear.
