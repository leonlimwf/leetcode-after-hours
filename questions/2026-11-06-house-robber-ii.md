# 213. House Robber II

Assigned: **2026-11-06** · **Medium**

Topics: Array / Dynamic Programming

[Open on LeetCode](https://leetcode.com/problems/house-robber-ii/)

Status: **Assigned**

## Problem Statement

Houses are arranged in a circle, so the first and last houses are neighbors. Each house has a nonnegative amount of money, and robbing two neighboring houses triggers an alarm. Return the most money you can take without robbing neighboring houses.


## Input and Output

Input  An integer array nums; nums[i] is the amount of money in the ith house, arranged in a circle.

Output  Return the maximum amount that can be robbed without taking from neighboring houses.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [2,3,2] | 3 | The first and last houses are neighbors; taking the middle house gives 3. |
| 2 | nums = [1,2,3,1] | 4 | Taking the first and third houses gives 1 + 3 = 4. |

## Constraints

1 <= nums.length <= 100 • 0 <= nums[i] <= 1000


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
