# 56. Merge Intervals

Assigned: **2026-10-18** · **Medium**

Topics: Array / Sorting

[Open on LeetCode](https://leetcode.com/problems/merge-intervals/)

Status: **Assigned**

## Problem Statement

Given a list of intervals, combine the ranges that overlap. Return intervals that do not overlap and cover the same values. Try this independently before reading a solution.


## Input and Output

Input  A list of intervals, each containing a start value and an end value.

Output  A list of intervals with overlapping ranges combined.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | intervals = [[1,3],[2,6],[8,10],[15,18]] | [[1,6],[8,10],[15,18]] | The returned ranges cover the same values without overlap. |
| 2 | intervals = [[1,4],[4,5]] | [[1,5]] | Intervals that share an endpoint count as overlapping. |
| 3 | intervals = [[4,7],[1,4]] | [[1,7]] | The two intervals share endpoint 4. |

## Constraints

1 <= intervals.length <= 10^4 • intervals[i].length == 2 • 0 <= start_i <= end_i <= 10^4


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
