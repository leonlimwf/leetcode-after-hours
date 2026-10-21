class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        res = [0]*len(nums)

        res[0] = nums[0]
        res[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            skip = res[i-1]
            rob = res[i-2] + nums[i]
            res[i] = max(skip,rob)
        return res[-1]
