# 746. Min Cost Climbing Stairs

Assigned: **2026-10-24** · **Easy**

Topics: Array / Dynamic Programming

[Open on LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/)

Status: **Assigned**

## Problem Statement

Each stair has a fee in cost[i]. You may begin at stair 0 or 1. After paying its fee, move up one or two stairs. Return the least total fee needed to reach the top just beyond the last stair. Try it before reading a solution.


## Input and Output

Input  An integer array cost, where cost[i] is the fee for stepping on stair i.

Output  Return the minimum total fee required to reach the top beyond the last stair.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | cost = [10,15,20] | 15 | Starting at stair 1 costs 15; a two-stair move reaches the top. |
| 2 | cost = [1,100,1,1,1,100,1,1,100,1] | 6 | A route that avoids the expensive stairs pays a total of 6. |

## Constraints

2 <= cost.length <= 1000 • 0 <= cost[i] <= 999


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
