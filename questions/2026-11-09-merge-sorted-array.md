# 88. Merge Sorted Array

Assigned: **2026-11-09** · **Easy**

Topics: Array / Two Pointers / Sorting

[Open on LeetCode](https://leetcode.com/problems/merge-sorted-array/)

Status: **Assigned**

## Problem Statement

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order, plus counts m and n for their meaningful values. Merge the values into nums1 so the result is sorted; nums1 has room for all m + n values, with its final n slots available for the merge.


## Input and Output

Input  nums1 and nums2, their meaningful lengths m and n, with nums1 containing m + n slots.

Output  Modify nums1 in place so it contains all values from nums1 and nums2 in non-decreasing order.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums1 = [1,2,3,0,0,0], m = 3; nums2 = [2,5,6], n = 3 | [1,2,2,3,5,6] | The values from both sorted arrays form one sorted array. |
| 2 | nums1 = [1], m = 1; nums2 = [], n = 0 | [1] | The second array has no values to add. |
| 3 | nums1 = [0], m = 0; nums2 = [1], n = 1 | [1] | There are no meaningful values in nums1. |

## Constraints

nums1.length == m + n • nums2.length == n • 0 <= m, n <= 200 • 1 <= m + n <= 200 • -10^9 <= nums1[i], nums2[i] <= 10^9


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
