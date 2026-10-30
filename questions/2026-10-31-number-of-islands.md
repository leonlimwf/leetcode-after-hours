# 200. Number of Islands

Assigned: **2026-10-31** · **Medium**

Topics: Array / Depth-First Search / Breadth-First Search / Matrix / Union Find

[Open on LeetCode](https://leetcode.com/problems/number-of-islands/)

Status: **Assigned**

## Problem Statement

Given a grid of land cells ('1') and water cells ('0'), count the islands. Land is connected only horizontally or vertically; assume the grid's outer border is water. Try it independently before reading a solution.


## Input and Output

Input  An m-by-n grid of characters, each either '1' (land) or '0' (water).

Output  Return the number of islands in the grid.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | grid = [["1","1"],["0","1"]] | 1 | The three land cells touch by sides, so they form one island. |
| 2 | grid = [["1","0","1"],["0","1","0"]] | 3 | The land cells are separated horizontally and vertically, so there are three islands. |

## Constraints

1 <= m, n <= 300 • m == grid.length • n == grid[i].length • Each cell is '0' or '1'.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
