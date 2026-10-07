# 235. Lowest Common Ancestor of a Binary Search Tree

Assigned: **2026-10-04** · **Medium**

Topics: Tree / Depth-First Search / Binary Search Tree / Binary Tree

[Open on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

Status: **Accepted**

## Problem Statement

Given the root of a binary search tree and two distinct nodes p and q that exist in it, return their lowest common ancestor (LCA). The LCA is the lowest node in the tree that has both p and q in its subtree, allowing a node to be a descendant of itself. Try the problem before reading a solution or hint.


## Input and Output

Input  The root of a binary search tree, plus two existing nodes p and q.

Output  The TreeNode that is the lowest common ancestor of p and q.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8 | 6 | 6 is the first node where p and q split into different subtrees. |
| 2 | root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4 | 2 | 4 lies inside 2's subtree, so 2 is the lowest common ancestor. |
| 3 | root = [2, 1], p = 2, q = 1 | 2 | One node is the ancestor of the other. |

## Constraints

2 <= number of nodes <= 10^5 • -10^9 <= Node.val <= 10^9 • All node values are unique • p != q • p and q both exist in the tree.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0235-lowest-common-ancestor-of-a-binary-search-tree/README.md)
