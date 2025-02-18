class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suml = 0
        sumr = sum(nums)
        for i in range(len(nums)):
            sumr -= nums[i]
            if suml == sumr:
                return i
            else:
                suml += nums[i]

        return -1