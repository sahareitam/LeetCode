class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)

        min1 = min(nums)
        nums.remove(min1)
        min2 = min(nums)

        return(max1*max2)-(min1*min2)