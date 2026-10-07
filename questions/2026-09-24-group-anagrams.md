# 49. Group Anagrams

Assigned: **2026-09-24** · **Medium**

Topics: Array / Hash Table / String / Sorting

[Open on LeetCode](https://leetcode.com/problems/group-anagrams/)

Status: **Accepted**

## Problem Statement

Given an array of strings, group together the strings that are anagrams of one another. Return the groups in any order.


## Input and Output

Input  An array of strings strs.

Output  A list of groups, where each group contains strings made from the same character counts.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | strs = ["eat", "tea", "tan", "ate", "nat", "bat"] | [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]] | Each group contains strings with the same character counts. |
| 2 | strs = [""] | [[""]] | The empty string forms one group. |
| 3 | strs = ["a"] | [["a"]] | The single string forms one group. |

## Constraints

1 <= strs.length <= 10^4 • 0 <= strs[i].length <= 100 • strs[i] consists of lowercase English letters.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0049-group-anagrams/README.md)
