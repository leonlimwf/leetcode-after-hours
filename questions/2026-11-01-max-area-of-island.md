# 695. Max Area of Island

Assigned: **2026-11-01** · **Medium**

Topics: Array / Depth-First Search / Breadth-First Search / Matrix

[Open on LeetCode](https://leetcode.com/problems/max-area-of-island/)

Status: **Assigned**

## Problem Statement

Given an m-by-n binary grid, treat each 1 as land and each 0 as water. Land cells belong to the same island when they connect horizontally or vertically. Return the area of the largest island, or 0 if the grid contains no land. Try it independently before reading a solution.


## Input and Output

Input  An m-by-n grid named grid, with each cell equal to 0 or 1.

Output  Return the number of cells in the largest four-directionally connected group of 1s; return 0 if there is no island.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | grid = [[1,1],[1,0]] | 3 | The three side-connected land cells form an island of area 3. |
| 2 | grid = [[0,0],[0,0]] | 0 | There are no land cells, so there is no island. |
| 3 | grid = [[1,0],[0,1]] | 1 | Diagonal cells do not connect, so the largest island has area 1. |

## Constraints

1 <= m, n <= 50 • m == grid.length • n == grid[i].length • Each grid[i][j] is 0 or 1.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
