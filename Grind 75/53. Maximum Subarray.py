class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(float('-inf'), nums[0])
        before = nums[0]
        for i in range(1, len(nums)):
            if before < 0:
                before = nums[i]
            else:
                before += nums[i]
            res = max(res, before)
        return res



