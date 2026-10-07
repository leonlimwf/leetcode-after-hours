# 226. Invert Binary Tree

Assigned: **2026-09-30** · **Easy**

Topics: Tree / Depth-First Search / Breadth-First Search / Binary Tree

[Open on LeetCode](https://leetcode.com/problems/invert-binary-tree/)

Status: **Accepted**

## Problem Statement

Given the root of a binary tree, invert the tree by swapping the left and right child of every node, then return the root.


## Input and Output

Input  The root of a binary tree, which may be empty.

Output  The root of the inverted binary tree.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | root = [4, 2, 7, 1, 3, 6, 9] | [4, 7, 2, 9, 6, 3, 1] | Each node has its left and right children swapped. |
| 2 | root = [2, 1, 3] | [2, 3, 1] | The children of 2 are exchanged. |
| 3 | root = [] | [] | An empty tree remains empty. |

## Constraints

0 <= number of nodes <= 100 • -100 <= Node.val <= 100


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0226-invert-binary-tree/README.md)
