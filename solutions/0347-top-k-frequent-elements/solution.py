class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        bucket = [[] for i in range(len(nums)+1)]
        #frequency = {1: 3, 2: 2, 3: 1}
        for num,count in frequency.items():
            bucket[count].append(num)
        result = []
        for count in range(len(bucket)-1,0,-1):
            for num in bucket[count]:
                result.append(num)
                if len(result)==k:
                    return result
        return result
