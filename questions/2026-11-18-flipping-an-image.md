# 832. Flipping an Image

Assigned: **2026-11-18** · **Easy**

Topics: Array / Two Pointers / Bit Manipulation / Matrix / Simulation

[Open on LeetCode](https://leetcode.com/problems/flipping-an-image/)

Status: **Assigned**

## Problem Statement

Given a square binary matrix image, flip each row horizontally, then invert every 0 and 1. Return the transformed matrix. Try this independently before reading a solution.


## Input and Output

Input  A square matrix image containing only 0s and 1s.

Output  Return the matrix after each row is reversed and every bit is inverted.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | image = [[1,1,0],[1,0,1],[0,0,0]] | [[1,0,0],[0,1,0],[1,1,1]] | Reverse each row, then invert every 0 and 1. |
| 2 | image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] | [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] | The rows are reversed and their bits are inverted. |

## Constraints

n == image.length == image[i].length • 1 <= n <= 20 • image[i][j] is 0 or 1


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
