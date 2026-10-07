# 141. Linked List Cycle

Assigned: **2026-10-07** · **Easy**

Topics: Linked List / Two Pointers

[Open on LeetCode](https://leetcode.com/problems/linked-list-cycle/)

Status: **Profile Accepted · pending confirmation**

## Problem Statement

Given the head of a linked list, determine whether the linked list contains a cycle. Return true if a cycle exists, otherwise return false. Try the problem before reading a solution or hint.


## Input and Output

Input  The head of a singly linked list, which may be empty and may contain a cycle.

Output  A boolean indicating whether following next pointers eventually revisits a node.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | head = [3, 2, 0, -4], pos = 1 | true | The tail points back to the node at index 1, so traversal revisits a node. |
| 2 | head = [1, 2], pos = 0 | true | The last node points back to the head, forming a cycle. |
| 3 | head = [1], pos = -1 | false | The only node points to null, so no node is revisited. |

## Constraints

0 <= number of nodes <= 10000 • -100000 <= Node.val <= 100000 • pos is -1 or a valid node index


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.
