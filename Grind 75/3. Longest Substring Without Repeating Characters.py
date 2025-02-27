class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dic = {}
        start = 0
        for i in range(len(s)):
            if s[i] not in dic or dic[s[i]] < start:
                dic[s[i]] = i
            else:
                start = dic[s[i]]+1
                dic[s[i]] = i
            res = max(res,i+1-start)
        return res

