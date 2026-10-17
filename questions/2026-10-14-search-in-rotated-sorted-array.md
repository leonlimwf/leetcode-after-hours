# 33. Search in Rotated Sorted Array

Assigned: **2026-10-14** · **Medium**

Topics: Array / Binary Search

[Open on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Status: **Accepted**

## Problem Statement

An ascending array of distinct integers may have been rotated at a pivot. Given this possibly rotated nums and target, return the target's index if present, or -1 if it is absent. Try the problem before reading a solution.


## Input and Output

Input  A distinct-integer array nums, originally sorted ascending and possibly rotated, and an integer target.

Output  The index of target in nums, or -1 if target is absent.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [4, 5, 6, 7, 0, 1, 2], target = 0 | 4 | The target is at index 4. |
| 2 | nums = [4, 5, 6, 7, 0, 1, 2], target = 3 | -1 | The target does not appear in the array. |
| 3 | nums = [1], target = 0 | -1 | The only element is not the target. |

## Constraints

1 <= nums.length <= 5000 • -10^4 <= nums[i] <= 10^4 • All values are distinct • nums was sorted ascending and may be rotated • -10^4 <= target <= 10^4


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0033-search-in-rotated-sorted-array/README.md)
