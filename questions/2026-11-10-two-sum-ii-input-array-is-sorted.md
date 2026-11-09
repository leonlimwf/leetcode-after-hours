# 167. Two Sum II - Input Array Is Sorted

Assigned: **2026-11-10** · **Medium**

Topics: Array / Two Pointers / Binary Search

[Open on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Status: **Missed**

## Problem Statement

You are given an integer array numbers sorted in non-decreasing order and a target. Find the two values that add up to the target and return their indices using 1-based indexing. The pair is guaranteed to exist, and you may not use the same element twice. Use constant extra space. Try this independently before reading a solution.


## Input and Output

Input  A sorted integer array numbers and an integer target.

Output  The 1-based indices of the two values whose sum equals target.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | numbers = [2,7,11,15], target = 9 | [1,2] | numbers[0] + numbers[1] = 9. |
| 2 | numbers = [2,3,4], target = 6 | [1,3] | numbers[0] + numbers[2] = 6. |
| 3 | numbers = [-1,0], target = -1 | [1,2] | numbers[0] + numbers[1] = -1. |

## Constraints

2 <= numbers.length <= 3 * 10^4 • -1000 <= numbers[i] <= 1000 • numbers is sorted in non-decreasing order • Exactly one solution exists • Do not use the same element twice • Use constant extra space


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
