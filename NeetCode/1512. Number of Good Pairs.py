import math


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        res = 0

        def nCr(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        for key in count:
            if count[key] >= 2:
                res += nCr(count[key], 2)
        return res