# 733. Flood Fill

Assigned: **2026-11-02** · **Easy**

Topics: Array / Depth-First Search / Breadth-First Search / Matrix

[Open on LeetCode](https://leetcode.com/problems/flood-fill/)

Status: **Assigned**

## Problem Statement

You are given an image represented by an m x n grid of integers, a starting row sr, a starting column sc, and a new color. Recolor the starting pixel and every pixel connected to it by a path of up, down, left, or right neighbors that originally have the same color. Return the modified image. Try it independently before reading a solution.


## Input and Output

Input  An m x n integer grid image, starting coordinates sr and sc, and the replacement color.

Output  Return the image after recoloring the four-directionally connected region containing image[sr][sc].


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2 | [[2,2,2],[2,2,0],[2,0,1]] | The 4-directionally connected 1s containing (1,1) change to 2; the diagonal 1 stays unchanged. |
| 2 | image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0 | [[0,0,0],[0,0,0]] | The starting pixel already has the requested color, so the image stays the same. |

## Constraints

1 <= m, n <= 50 • 0 <= image[i][j], color <= 65535 • 0 <= sr < m • 0 <= sc < n.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
