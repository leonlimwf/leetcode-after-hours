class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        res = [0]*(len(cost)+1)
        res[0] = 0
        res[1] = 0

        for i in range(2,len(cost)+1):
            res[i] = min(res[i-1]+cost[i-1], res[i-2]+cost[i-2])
        return res[-1]
