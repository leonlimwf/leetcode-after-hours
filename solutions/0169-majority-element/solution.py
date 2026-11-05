class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        return max(count, key=count.get)
