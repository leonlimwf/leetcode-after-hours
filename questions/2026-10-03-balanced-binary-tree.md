# 110. Balanced Binary Tree

Assigned: **2026-10-03** · **Easy**

Topics: Tree / Depth-First Search / Binary Tree

[Open on LeetCode](https://leetcode.com/problems/balanced-binary-tree/)

Status: **Accepted**

## Problem Statement

Given the root of a binary tree, determine whether it is height-balanced: at every node, the left and right subtree heights differ by no more than one.


## Input and Output

Input  The root of a binary tree, which may be empty.

Output  A boolean: True if the tree is height-balanced; otherwise False.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | root = [3, 9, 20, null, null, 15, 7] | True | Every node's subtree heights differ by at most 1. |
| 2 | root = [1, 2, 2, 3, 3, null, null, 4, 4] | False | The left subtree becomes too deep. |
| 3 | root = [] | True | An empty tree is balanced. |

## Constraints

0 <= number of nodes <= 5000 • -10^4 <= Node.val <= 10^4


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0110-balanced-binary-tree/README.md)
