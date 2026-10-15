# 36. Valid Sudoku

Assigned: **2026-10-16** · **Medium**

Topics: Array / Hash Table / Matrix

[Open on LeetCode](https://leetcode.com/problems/valid-sudoku/)

Status: **Missed**

## Problem Statement

Determine whether a partially filled 9 × 9 Sudoku board obeys the no-repeat rule in every row, column, and 3 × 3 box. Ignore empty cells. A valid board does not have to be solvable. Try the problem before reading a solution.


## Input and Output

Input  A 9 × 9 grid; each cell is a digit '1' through '9' or '.' for empty.

Output  Return true if no filled digit repeats in any row, column, or 3 × 3 box; otherwise return false.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | board = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"] | true | No filled digit repeats in a row, column, or 3 × 3 box. |
| 2 | board = ["83..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"] | false | The upper-left 3 × 3 box contains two 8s. |

## Constraints

board.length == 9 • board[i].length == 9 • board[i][j] is a digit '1' through '9' or '.'


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
