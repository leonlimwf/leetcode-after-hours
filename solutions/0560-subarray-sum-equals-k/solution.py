class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = [0]
        seen = {0:1}
        count = 0
        total_sum=0
        for num in nums:
            total_sum+=num
            res.append(total_sum)

        for prefix in res[1:]:
            need = prefix-k
            count += seen.get(need,0)
            seen[prefix] = seen.get(prefix,0)+1
        return count
