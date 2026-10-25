class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest = 0

        for i,jump in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest,i+jump)
        return True
