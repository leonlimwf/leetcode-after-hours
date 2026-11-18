# 977. Squares of a Sorted Array

Assigned: **2026-11-19** · **Easy**

Topics: Array / Two Pointers / Sorting

[Open on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)

Status: **Assigned**

## Problem Statement

Given an integer array nums sorted in non-decreasing order, return an array of each number squared, also sorted in non-decreasing order. Follow-up: Can you do this in O(n) time without sorting the squared values? Try this independently before reading a solution.


## Input and Output

Input  A non-decreasing integer array nums.

Output  An array containing each nums[i] squared, sorted in non-decreasing order.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [-4,-1,0,3,10] | [0,1,9,16,100] | The squared values are [16,1,0,9,100], then returned in sorted order. |
| 2 | nums = [-7,-3,2,3,11] | [4,9,9,49,121] | Squaring each value and ordering the results gives [4,9,9,49,121]. |

## Constraints

1 <= nums.length <= 10^4 • -10^4 <= nums[i] <= 10^4 • nums is sorted in non-decreasing order


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
