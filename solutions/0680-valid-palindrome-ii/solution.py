class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome_range(i,j):
            while i < j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        left,right = 0, len(s)-1
        while left < right:
            if s[left]!=s[right]:
                return ispalindrome_range(left+1, right) or ispalindrome_range(left,right-1)
            left+=1
            right-=1
        return True
