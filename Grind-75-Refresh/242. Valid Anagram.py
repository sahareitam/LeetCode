class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        else:
            dic = {}
            for T in t:
                if T in dic:
                    dic[T] += 1
                else:
                    dic[T] = 1
            for S in s:
                if S not in dic:
                    return False
                else:
                    dic[S] -= 1
            for k in dic:
                if dic[k] != 0:
                    return False
            return True



