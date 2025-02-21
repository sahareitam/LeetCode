class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for c in set(nums):
            if nums.count(c) > len(nums)//2:
                return c