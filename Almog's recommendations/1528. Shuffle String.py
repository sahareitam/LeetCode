class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res= [0]* len(s)
        for c,i in zip(s,indices):
            res[i] = c
        return ''.join(res)