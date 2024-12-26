class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        n = len(shortest)
        i = n
        words = len(strs)
        j = 0
        while i >= 0 and j < words:
            if shortest[0:i] == strs[j][0:i]:
                j += 1
            else:
                j = 0
                i -= 1

        if i >= 0:
            return shortest[:i]
        else:
            return ""