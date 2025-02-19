class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        hmap = {}
        res = -1
        for i,c in enumerate(s):
            if c not in hmap:
                hmap[c] = [i]
            else:
                hmap[c].append(i)
                res = max(res,hmap[c][-1]-hmap[c][0]-1)
        return res