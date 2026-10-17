# 36. Valid Sudoku

Medium · Array / Hash Table / Matrix

[Original problem](https://leetcode.com/problems/valid-sudoku/) · Confirmed Accepted: 2026-10-16

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(1) for the fixed 9 × 9 board (equivalently O(R × C) if generalized).

Auxiliary space: O(1) for the fixed board; the 27 sets hold only digits 1–9.

Why: The nested loops inspect each of the 81 cells once. Set checks and inserts are average O(1); the fixed-size board and fixed-size sets keep extra space constant.
