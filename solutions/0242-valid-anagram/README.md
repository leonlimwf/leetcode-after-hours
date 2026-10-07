# 242. Valid Anagram

Easy · Hash Table / String / Sorting

[Original problem](https://leetcode.com/problems/valid-anagram/) · Confirmed Accepted: 2026-09-20

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n + m), where n = len(s) and m = len(t).

Space complexity: O(k), where k is the number of distinct characters; under the lowercase-English-letter constraint, this is effectively O(1).

Why: Each string is traversed once, and dictionary operations are average O(1). The dictionaries store character frequencies.
