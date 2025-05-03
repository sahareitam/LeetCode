class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in ransomNote:
            if i in dic and dic[i] >= 1:
                dic[i] -= 1
            else:
                return False
        return True
