class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            p = 0
            i = 0
            n = len(haystack)
            while i < n:
                if haystack[i] == needle[p]:
                    p += 1
                    i += 1
                    if p == len(needle):
                        return i - p
                else:
                    i += 1
                    i = i - p
                    p = 0

        return -1
