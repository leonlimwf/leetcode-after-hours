# 49. Group Anagrams

Medium · Array / Hash Table / String / Sorting

[Original problem](https://leetcode.com/problems/group-anagrams/) · Confirmed Accepted: 2026-09-24

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time Complexity O(S), where S is the total number of characters across all input strings. Each character is counted once, and each signature has a fixed 26 entries.

Space Complexity O(S) including the returned groups. The dictionary stores one fixed-size signature per distinct group and references to all input strings; the auxiliary signature space is O(G) when the alphabet size is treated as constant, where G is the number of groups.
