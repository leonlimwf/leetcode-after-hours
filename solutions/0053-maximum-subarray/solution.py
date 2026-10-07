class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0
        for i in nums:
            curr_sum+=i
            if max_sum<curr_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum
