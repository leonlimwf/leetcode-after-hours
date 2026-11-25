# 994. Rotting Oranges

Assigned: **2026-11-26** · **Medium**

Topics: Array / Breadth-First Search / Matrix

[Open on LeetCode](https://leetcode.com/problems/rotting-oranges/)

Status: **Assigned**

## Problem Statement

An m x n grid contains empty cells, fresh oranges, and rotten oranges. Each minute, a fresh orange next to a rotten one in one of the four cardinal directions becomes rotten. Return the minutes until no fresh orange remains, or -1 if some fresh orange can never rot. Try this independently before reading a solution.


## Input and Output

Input  An m x n grid whose cells are 0 (empty), 1 (fresh), or 2 (rotten).

Output  The minimum minutes until no fresh orange remains, or -1 if that is impossible.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | grid = [[2,1,1],[1,1,0],[0,1,1]] | 4 | The rot spreads one cell farther each minute. |
| 2 | grid = [[2,1,1],[0,1,1],[1,0,1]] | -1 | The bottom-left fresh orange is not reachable in four directions. |
| 3 | grid = [[0,2]] | 0 | No fresh orange is present. |

## Constraints

1 <= m, n <= 10. Each grid cell is 0, 1, or 2.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
