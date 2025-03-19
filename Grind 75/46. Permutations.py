class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def rec(i,cur):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for num in nums:
                if num not in cur:
                    rec(i+1,cur + [num])
        rec(0,[])
        return res