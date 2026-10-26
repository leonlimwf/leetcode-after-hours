# 1143. Longest Common Subsequence

Assigned: **2026-10-27** · **Medium**

Topics: String / Dynamic Programming

[Open on LeetCode](https://leetcode.com/problems/longest-common-subsequence/)

Status: **In Progress**

## Problem Statement

Given two strings text1 and text2, return the length of their longest common subsequence. A subsequence keeps the original order of characters but may omit some characters. Return 0 if there is no common subsequence.


## Input and Output

Input  Two strings, text1 and text2.

Output  Return the length of the longest subsequence shared by text1 and text2.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | text1 = "abcde", text2 = "ace" | 3 | The subsequence ace appears in order in both strings. |
| 2 | text1 = "abc", text2 = "abc" | 3 | All three characters match in order. |
| 3 | text1 = "abc", text2 = "def" | 0 | The strings have no common subsequence. |

## Constraints

1 <= text1.length, text2.length <= 1000 • text1 and text2 contain only lowercase English letters.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
