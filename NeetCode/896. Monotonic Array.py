class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        i = 1

        while i < size:
            if nums[i-1] < nums[i]:
                while i < size:
                    if nums[i-1] > nums[i]:
                        return False
                    i+=1
            elif nums[i-1] > nums[i]:
                while i < size:
                    if nums[i-1] < nums[i]:
                        return False
                    i+=1
            else:
                i+=1
        return True