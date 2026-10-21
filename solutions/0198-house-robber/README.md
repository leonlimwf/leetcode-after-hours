# 198. House Robber

Medium · Array / Dynamic Programming

[Original problem](https://leetcode.com/problems/house-robber/) · Confirmed Accepted: 2026-10-21

[Python solution](solution.py)

Code is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.

## Complexity Analysis

Time complexity: O(n). The DP list initialization and the single pass over the houses each take linear time; the empty and one-house checks are constant time.

Auxiliary space complexity: O(n). The res list stores one DP value per house; the remaining variables use O(1) extra space.

Why: For each house from index 2 onward, the code compares skipping it with taking it plus the best total two houses back. Each iteration is constant work, and the DP list grows with the input length.
