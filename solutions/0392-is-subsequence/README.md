# 392. Is Subsequence

Easy · Two Pointers / String / Dynamic Programming

[Original problem](https://leetcode.com/problems/is-subsequence/) · Confirmed Accepted: date not recorded

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n), where n = len(t).

Auxiliary space complexity: O(1).

Why: left_t advances at most once for each character in t, and left_s advances only when characters match. The code stores two indexes and returns a boolean; it creates no input-sized data structure.
