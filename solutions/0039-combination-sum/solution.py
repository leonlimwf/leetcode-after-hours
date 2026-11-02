class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(start,remaining, path):
            if remaining==0:
                res.append(path.copy())
                return
            if remaining < 0:
                return
            for j in range(start, len(candidates)):
                # CHOOSE
                path.append(candidates[j])
                # RECURSE
                backtrack(j, remaining-candidates[j], path)
                # UNDO
                path.pop()
        backtrack(0, target, [])
        return res
