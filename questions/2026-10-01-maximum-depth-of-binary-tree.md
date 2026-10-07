# 104. Maximum Depth of Binary Tree

Assigned: **2026-10-01** · **Easy**

Topics: Tree / Depth-First Search / Breadth-First Search / Binary Tree

[Open on LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Status: **Accepted**

## Problem Statement

Given the root of a binary tree, return the length of the longest path from the root down to any leaf node.


## Input and Output

Input  The root of a binary tree, which may be empty.

Output  An integer representing the tree height measured in nodes.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | root = [3, 9, 20, null, null, 15, 7] | 3 | The longest root-to-leaf path is 3 → 20 → 15 or 7. |
| 2 | root = [1, null, 2] | 2 | The path 1 → 2 contains two nodes. |
| 3 | root = [] | 0 | An empty tree has depth zero. |

## Constraints

0 <= number of nodes <= 10^4 • -100 <= Node.val <= 100


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0104-maximum-depth-of-binary-tree/README.md)
