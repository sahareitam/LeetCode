class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = {}
        for i in range(len(s)):
            map1[i] = s.index(s[i])
            if map1[i] != t.index(t[i]):
                return False
        return True

