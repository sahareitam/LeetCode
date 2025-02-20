class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        def rec(stairs):
            if stairs == 0:
                return 1
            elif stairs < 0:
                return 0
            if stairs in dic:
                return dic[stairs]
            w1 = rec(stairs-1)
            w2 = rec(stairs-2)
            dic[stairs] = w1+w2
            return w1+w2
        return rec(n)


