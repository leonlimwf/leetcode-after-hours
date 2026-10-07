class Solution:
    def isValid(self, s: str) -> bool:
        expected = {"(": ")", "{": "}", "[": "]"}
        ls = []
        for char in s:
            if char in expected:
                ls.append(expected[char])
            else:
                if not ls or ls.pop() != char:
                    return False
        return not ls
