# 74. Search a 2D Matrix

Assigned: **2026-10-13** · **Medium**

Topics: Array / Binary Search / Matrix

[Open on LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)

Status: **Assigned**

## Problem Statement

You are given an m × n matrix whose rows are sorted in ascending order, and each row starts with a value greater than the previous row's last value. Return true if target is in the matrix; otherwise return false. Try the problem before reading a solution or hint.


## Input and Output

Input  An m × n integer matrix and an integer target.

Output  A boolean: true if target is present; false otherwise.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 | true | The target appears in the first row. |
| 2 | matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 | false | The target does not appear in the matrix. |
| 3 | matrix = [[1]], target = 1 | true | The single matrix value matches the target. |

## Constraints

1 <= m, n <= 100 • -10^4 <= matrix[i][j], target <= 10^4 • Each row is sorted; each row's first value is greater than the previous row's last value.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
