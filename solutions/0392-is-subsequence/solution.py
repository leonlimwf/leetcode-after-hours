class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_t = 0
        left_s = 0
        while left_t < len(t) and left_s < len(s):
            if t[left_t] == s[left_s]:
                left_s+=1
            left_t+=1
        return left_s == len(s)
