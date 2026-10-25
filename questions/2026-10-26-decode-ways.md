# 91. Decode Ways

Assigned: **2026-10-26** · **Medium**

Topics: String / Dynamic Programming

[Open on LeetCode](https://leetcode.com/problems/decode-ways/)

Status: **Missed**

## Problem Statement

A digit string can be split into letter codes where 1 maps to A through 26 maps to Z. Count the valid ways to decode the entire string. A code cannot begin with 0; return 0 if no valid decoding exists. Try independently before reading a solution.


## Input and Output

Input  A string s containing only digits; it may contain leading zeros.

Output  Return the number of valid decodings, or 0 if the string cannot be decoded.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | s = "12" | 2 | It can be decoded as 1 and 2, or together as 12. |
| 2 | s = "226" | 3 | There are three valid ways to group the digits. |
| 3 | s = "06" | 0 | A valid code cannot start with 0. |

## Constraints

1 <= s.length <= 100 • s contains only digits and may contain leading zeros • The answer fits in a 32-bit integer.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
