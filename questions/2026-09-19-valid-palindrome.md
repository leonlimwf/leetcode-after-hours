# 125. Valid Palindrome

Assigned: **2026-09-19** · **Easy**

Topics: Two Pointers / String

[Open on LeetCode](https://leetcode.com/problems/valid-palindrome/)

Status: **Accepted**

## Problem Statement

A phrase is a palindrome after uppercase letters are converted to lowercase and all non-alphanumeric characters are ignored. Given a string s, return true if the remaining text reads the same forward and backward; otherwise return false.


## Input and Output

Input  A string s containing only printable ASCII characters.

Output  Return true if the normalized string reads the same forward and backward; otherwise return false.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | s = "A man, a plan, a canal: Panama" | true | After ignoring punctuation and case, the text reads the same both ways. |
| 2 | s = "race a car" | false | After ignoring the space and case, the text is not a palindrome. |
| 3 | s = " " | true | Removing non-alphanumeric characters leaves an empty string, which is a palindrome. |

## Constraints

1 <= s.length <= 2 * 10^5 • s consists only of printable ASCII characters.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0125-valid-palindrome/README.md)
