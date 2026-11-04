# 680. Valid Palindrome II

Easy · Two Pointers / String / Greedy

[Original problem](https://leetcode.com/problems/valid-palindrome-ii/) · Confirmed Accepted: None

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n).

Auxiliary space: O(1).

Why: The two-pointer scan is linear. At the first mismatch, the helper tests at most two ranges; together those checks are still O(n), and the code uses only a fixed number of indexes and booleans.
