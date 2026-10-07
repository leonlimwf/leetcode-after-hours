# 102. Binary Tree Level Order Traversal

Assigned: **2026-10-05** · **Medium**

Topics: Tree / Breadth-First Search / Binary Tree

[Open on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

Status: **Missed**

## Problem Statement

Given the root of a binary tree, return the level order traversal of its node values: from left to right, level by level. Try the problem before reading a solution or hint.


## Input and Output

Input  The root of a binary tree, which may be empty.

Output  A list of lists, where each inner list contains the node values at one depth from left to right.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | root = [3, 9, 20, null, null, 15, 7] | [[3], [9, 20], [15, 7]] | Values are grouped by depth from left to right. |
| 2 | root = [1] | [[1]] | A single node forms one level. |
| 3 | root = [] | [] | An empty tree has no levels. |

## Constraints

0 <= number of nodes <= 2000 • -1000 <= Node.val <= 1000


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
