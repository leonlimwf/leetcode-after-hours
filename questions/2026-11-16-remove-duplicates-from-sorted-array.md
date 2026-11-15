# 26. Remove Duplicates from Sorted Array

Assigned: **2026-11-16** · **Easy**

Topics: Array / Two Pointers

[Open on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Status: **Assigned**

## Problem Statement

Given an integer array nums sorted in non-decreasing order, remove duplicates in place so each distinct value appears once while keeping their order. Return the number of distinct values. Try this independently before reading a solution.


## Input and Output

Input  A non-decreasing integer array nums.

Output  Return the number of distinct values, with those values in sorted order at the front of nums.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [1,1,2] | 2; [1,2] | Keep one copy of each value; the unused tail does not matter. |
| 2 | nums = [0,0,1,1,1,2,2,3,3,4] | 5; [0,1,2,3,4] | The first five positions contain the distinct values in sorted order. |

## Constraints

1 <= nums.length <= 3 * 10^4 • -100 <= nums[i] <= 100 • nums is sorted in non-decreasing order.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
