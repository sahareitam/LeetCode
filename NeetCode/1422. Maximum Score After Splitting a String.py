class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = s.count('1')
        res = 0
        for i in range(len(s)-1):
            if s[i] == "0":
               left+=1
            else:
                right-=1
            res = max(res,left+right)
        return res