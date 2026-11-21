# 383. Ransom Note

Assigned: **2026-11-22** · **Easy**

Topics: Hash Table / String / Counting

[Open on LeetCode](https://leetcode.com/problems/ransom-note/)

Status: **Assigned**

## Problem Statement

Given strings ransomNote and magazine, return true if ransomNote can be formed using letters from magazine. Each letter from magazine can be used only once. Return false otherwise. Try this independently before reading a solution.


## Input and Output

Input  Two lowercase English strings, ransomNote and magazine.

Output  Return true if ransomNote can be formed from magazine; otherwise return false.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | ransomNote = "a", magazine = "b" | false | The magazine does not contain the letter a. |
| 2 | ransomNote = "aa", magazine = "ab" | false | There is only one a available in the magazine. |
| 3 | ransomNote = "aa", magazine = "aab" | true | The magazine has two copies of a. |

## Constraints

1 <= ransomNote.length, magazine.length <= 10^5 • ransomNote and magazine consist of lowercase English letters.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
