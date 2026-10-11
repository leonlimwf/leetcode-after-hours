# 162. Find Peak Element

Assigned: **2026-10-11** · **Medium**

Topics: Array / Binary Search

[Open on LeetCode](https://leetcode.com/problems/find-peak-element/)

Status: **Accepted**

## Problem Statement

Given an integer array nums with no equal adjacent values, return the index of any peak element. A peak is greater than its neighboring values; an endpoint may be a peak relative to the outside boundary. Try the problem before reading a solution or hint.


## Input and Output

Input  A zero-indexed integer array nums with unequal adjacent values.

Output  The index of any peak element in nums.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [1, 2, 3, 1] | 2 | The value 3 at index 2 is greater than its neighbors. |
| 2 | nums = [1, 2, 1, 3, 5, 6, 4] | 1 or 5 | Both returned indices identify a value greater than its neighbors. |

## Constraints

1 <= nums.length <= 1000 • -2^31 <= nums[i] <= 2^31 - 1 • nums[i] != nums[i + 1] for all valid i


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0162-find-peak-element/README.md)
