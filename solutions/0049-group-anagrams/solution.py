class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for word in strs:
            counts = [0]*26
            for char in word:
                counts[ord(char)-ord("a")]+=1
            key = tuple(counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())
