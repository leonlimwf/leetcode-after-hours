# 153. Find Minimum in Rotated Sorted Array

Assigned: **2026-10-12** · **Medium**

Topics: Array / Binary Search

[Open on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

Status: **Assigned**

## Problem Statement

Given a distinct integer array that was sorted in ascending order and then rotated, return its smallest value. Try it before reading a solution or hint.


## Input and Output

Input  An array nums of distinct integers that was sorted in ascending order and rotated.

Output  The minimum element in nums.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | nums = [3, 4, 5, 1, 2] | 1 | 1 is the smallest value in the rotated array. |
| 2 | nums = [4, 5, 6, 7, 0, 1, 2] | 0 | 0 is the smallest value in this rotated array. |
| 3 | nums = [11, 13, 15, 17] | 11 | The array is ascending, so 11 is its smallest value. |

## Constraints

1 <= n <= 5000 • -5000 <= nums[i] <= 5000 • All values are unique • nums is sorted and rotated between 1 and n times

First Instinct

What approach would you try first, and why?

class Solution:

    def findMin(self, nums: list[int]) -> int:

        left = 0

        right = len(nums)-1

        while left < right:

            mid = (left+right)//2

            if nums[mid]>nums[right]:

                left = mid+1

            else:

                right = mid

        return nums[left]

Completion Check

[ ] Attempted    [ ] Submitted    [ ] Accepted    [ ] Needs another attempt

Accepted on  ____________________

  One sentence to remember __________________________________________

Back to Contents


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
