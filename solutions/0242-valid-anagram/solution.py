class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_1 = {}
        s_2 = {}
        for char in s:
            s_1[char] = s_1.get(char, 0) + 1
        for char2 in t:
            s_2[char2] = s_2.get(char2, 0) + 1
        return s_1 == s_2
