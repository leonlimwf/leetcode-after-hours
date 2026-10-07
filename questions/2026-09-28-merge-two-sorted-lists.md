# 21. Merge Two Sorted Lists

Assigned: **2026-09-28** · **Easy**

Topics: Linked List / Recursion

[Open on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

Status: **Accepted**

## Problem Statement

Given the heads of two sorted singly linked lists, merge them into one sorted list by reusing the existing nodes and return the head of the merged list.


## Input and Output

Input  The heads of two linked lists sorted in non-decreasing order.

Output  The head of one sorted linked list containing every node from both input lists.


## Examples

| # | Input | Output | Why it works |
| --- | --- | --- | --- |
| 1 | list1 = [1, 2, 4], list2 = [1, 3, 4] | [1, 1, 2, 3, 4, 4] | At each step, link the smaller current node. |
| 2 | list1 = [], list2 = [] | [] | Both lists are empty. |
| 3 | list1 = [], list2 = [0] | [0] | The non-empty list is already the merged result. |

## Constraints

0 <= number of nodes in list1, list2 <= 50 • -100 <= Node.val <= 100 • Both lists are sorted in non-decreasing order.


## First Instinct

What approach would you try first, and why?

Try it before reading a solution. Write your approach and code in your private journal.

[Archived solution and complexity](../solutions/0021-merge-two-sorted-lists/README.md)
