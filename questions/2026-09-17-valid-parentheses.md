# 20. Valid Parentheses

Assigned: **2026-09-17** · **Easy**

Topics: String / Stack / Bracket Sequences

[Open on LeetCode](https://leetcode.com/problems/valid-parentheses/)

Status: **Accepted**

## Problem Statement

Given a string made only of round, square, and curly brackets, decide whether the whole sequence is valid. Each opening bracket must be closed by its matching type, the brackets must close in the correct order, and every closing bracket must have a matching opening bracket.


## Input and Output

Input  A string s containing only the six bracket characters.

Output  Return true if the entire sequence is valid; otherwise return false.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | s = "()" | true | The opening bracket is closed. |
| 2 | s = "()[]{}" | true | Each bracket has a matching pair. |
| 3 | s = "(]" | false | The bracket types do not match. |
| 4 | s = "([])" | true | The pairs are nested in order. |
| 5 | s = "([)]" | false | The closing order is invalid. |

## Constraints

1 <= s.length <= 10^4 • s contains only the characters (, ), [, ], {, and }.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0020-valid-parentheses/README.md)
