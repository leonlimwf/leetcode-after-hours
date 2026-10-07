# 238. Product of Array Except Self

Assigned: **2026-09-26** · **Medium**

Topics: Array / Prefix Sum

[Open on LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

Status: **Accepted**

## Problem Statement

Given an integer array nums, return an array answer where answer[i] equals the product of every value in nums except nums[i]. The answer must be produced without using division.


## Input and Output

Input  An integer array nums.

Output  An integer array answer of the same length, where each position contains the product of all other values.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [1, 2, 3, 4] | [24, 12, 8, 6] | Each position contains the product of the other three values. |
| 2 | nums = [-1, 1, 0, -3, 3] | [0, 0, 9, 0, 0] | Only the position containing zero excludes the zero from its product. |
| 3 | nums = [2, 3, 4] | [12, 8, 6] | Each output is the product of the two values at the other positions. |

## Constraints

2 <= nums.length <= 10^5 • -30 <= nums[i] <= 30 • The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0238-product-of-array-except-self/README.md)
