# 11. Container With Most Water

Assigned: **2026-10-17** · **Medium**

Topics: Array / Two Pointers / Greedy

[Open on LeetCode](https://leetcode.com/problems/container-with-most-water/)

Status: **Accepted**

## Problem Statement

Given an integer array of line heights, choose two vertical lines and the horizontal axis to form a container. Return the greatest amount of water it can hold. The container must stay upright; its sides cannot be tilted. Try the problem before reading a solution.


## Input and Output

Input  An integer array height where height[i] gives the height of the line at position i.

Output  Return one integer: the maximum amount of water any two lines can contain.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | height = [1, 8, 6, 2, 5, 4, 8, 3, 7] | 49 | The selected lines can hold 49 units of water. |
| 2 | height = [1, 1] | 1 | The two lines are one unit apart and each is one unit tall. |

## Constraints

2 <= height.length <= 10^5 • 0 <= height[i] <= 10^4

First Instinct

What approach would you try first, and why?

class Solution:

    def maxArea(self, height: list[int]) -> int:

        left = 0

        right = len(height)-1

        maxWater = 0

        while left<=right:

            width = right-left

            min_height = min(height[left],height[right])

            maxWater=max(maxWater, width*min_height)

            if height[left]<height[right]:

                left+=1

            else:

                right-=1

        return maxWater

Complexity Analysis

Time Complexity: O(n). Each iteration moves one pointer inward, so there are at most n iterations.

Auxiliary Space: O(1). The function uses only a fixed number of variables; extra space does not grow with the input.

Completion Check

[x] Attempted    [x] Submitted    [x] Accepted    [ ] Needs another attempt

Accepted on  October 17, 2026

  One sentence to remember __________________________________________

Back to Contents


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0011-container-with-most-water/README.md)
