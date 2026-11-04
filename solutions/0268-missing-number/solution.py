class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        summation = (n*(n+1)) // 2
        return summation-sum(nums)
