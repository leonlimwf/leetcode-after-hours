# 322. Coin Change

Assigned: **2026-11-12** · **Medium**

Topics: Array / Dynamic Programming / Breadth-First Search

[Open on LeetCode](https://leetcode.com/problems/coin-change/)

Status: **Assigned**

## Problem Statement

Given coin denominations and a target amount, find the fewest coins needed to make that amount. You may use each denomination any number of times. Return -1 if the amount cannot be made. Try this independently before reading a solution.


## Input and Output

Input  An integer array coins of distinct denominations and a non-negative integer amount.

Output  The fewest coins needed to make amount, or -1 if it cannot be made.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | coins = [1,2,5], amount = 11 | 3 | Use 5 + 5 + 1, which takes 3 coins. |
| 2 | coins = [2], amount = 3 | -1 | No number of 2-value coins totals 3. |
| 3 | coins = [1], amount = 0 | 0 | The target amount is already zero. |

## Constraints

1 <= coins.length <= 12 • 1 <= coins[i] <= 2^31 - 1 • 0 <= amount <= 10^4 • All coin values are distinct.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
