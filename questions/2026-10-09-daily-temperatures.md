# 739. Daily Temperatures

Assigned: **2026-10-09** · **Medium**

Topics: Array / Stack / Monotonic Stack

[Open on LeetCode](https://leetcode.com/problems/daily-temperatures/)

Status: **Accepted**

## Problem Statement

For each day in a list of temperatures, report how many days pass before a strictly warmer temperature occurs. Use 0 if no later day is warmer. Try the problem before reading a solution or hint.


## Input and Output

Input  An integer array temperatures with one temperature per day.

Output  A same-length array of waiting times; use 0 when no warmer future day exists.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | temperatures = [73, 74, 75, 71, 69, 72, 76, 73] | [1, 1, 4, 2, 1, 1, 0, 0] | Day 3 waits four days for 76; the last two days have no warmer day ahead. |
| 2 | temperatures = [30, 40, 50, 60] | [1, 1, 1, 0] | Each day except the last has a warmer temperature the next day. |
| 3 | temperatures = [30, 60, 90] | [1, 1, 0] | The first two days wait one day; the final day waits zero. |

## Constraints

1 <= temperatures.length <= 100000 • 30 <= temperatures[i] <= 100


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0739-daily-temperatures/README.md)
