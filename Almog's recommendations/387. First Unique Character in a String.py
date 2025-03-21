class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i,c in enumerate(s):
            if c in dic:
                continue
            if s.count(c) == 1:
                return i
            dic[c] = s.count(c)
        return -1