# 139. Word Break

Assigned: **2026-11-13** · **Medium**

Topics: Array / Hash Table / String / Dynamic Programming / Trie / Memoization

[Open on LeetCode](https://leetcode.com/problems/word-break/)

Status: **Assigned**

## Problem Statement

Given a string s and a dictionary wordDict, decide whether s can be split into one or more dictionary words. A dictionary word may be reused. Try this independently before reading a solution.


## Input and Output

Input  A string s and a list of dictionary words wordDict.

Output  True if s can be segmented into words from wordDict; otherwise, false.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | s = "leetcode", wordDict = ["leet","code"] | true | The string splits into "leet" and "code". |
| 2 | s = "applepenapple", wordDict = ["apple","pen"] | true | The word "apple" can be reused. |
| 3 | s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] | false | No sequence of dictionary words covers the full string. |

## Constraints

1 <= s.length <= 300 • 1 <= wordDict.length <= 1000 • 1 <= wordDict[i].length <= 20 • s and wordDict words contain lowercase English letters • All wordDict strings are unique.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
