class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [i, seen[diff]]
            seen[num]=i
