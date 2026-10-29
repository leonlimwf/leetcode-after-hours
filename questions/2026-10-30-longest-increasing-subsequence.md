# 300. Longest Increasing Subsequence

Assigned: **2026-10-30** · **Medium**

Topics: Array / Binary Search / Dynamic Programming

[Open on LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/)

Status: **Assigned**

## Problem Statement

Given an integer array nums, return the length of its longest strictly increasing subsequence. A subsequence keeps the original order but may skip elements; each selected value must be greater than the previous one.


## Input and Output

Input  An integer array nums.

Output  Return the length of a longest strictly increasing subsequence.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [10, 9, 2, 5, 3, 7, 101, 18] | 4 | One longest strictly increasing subsequence is [2, 3, 7, 101]. |
| 2 | nums = [0, 1, 0, 3, 2, 3] | 4 | For example, [0, 1, 2, 3] keeps order and increases at every step. |
| 3 | nums = [7, 7, 7, 7, 7, 7, 7] | 1 | Equal values cannot extend a strictly increasing subsequence. |

## Constraints

1 <= nums.length <= 2500 • -10^4 <= nums[i] <= 10^4


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
