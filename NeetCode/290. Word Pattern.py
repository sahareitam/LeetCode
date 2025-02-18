class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic ={}
        str_s = s.split()
        i=0
        if len(str_s) != len(pattern):
            return False
        for c, s in zip(pattern, str_s):
            if c not in dic and s not in str_s[0:i]:
                dic[c] = s
            elif c not in dic and s in str_s[0:i]:
                return False
            if c in dic and dic[c] != s:
                return False
            i+=1
        return True

