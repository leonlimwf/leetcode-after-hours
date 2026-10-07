# 150. Evaluate Reverse Polish Notation

Assigned: **2026-10-08** · **Medium**

Topics: Array / Math / Stack

[Open on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

Status: **Accepted**

## Problem Statement

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, and /. Each operand may be an integer or another expression. Division truncates toward zero. Try the problem before reading a solution or hint.


## Input and Output

Input  A list of tokens representing a valid Reverse Polish Notation expression.

Output  The integer result of evaluating the expression.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | tokens = ["2", "1", "+", "3", "*"] | 9 | The expression (2 + 1) * 3 evaluates to 9. |
| 2 | tokens = ["4", "13", "5", "/", "+"] | 6 | 13 / 5 truncates toward zero to 2, then 4 + 2 = 6. |
| 3 | tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] | 22 | The valid expression evaluates to 22 when the operators are applied in order. |

## Constraints

1 <= tokens.length <= 10000 • tokens[i] is an integer or one of +, -, *, / • integer tokens are in the range -200 to 200 • division truncates toward zero • the expression is valid


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0150-evaluate-reverse-polish-notation/README.md)
