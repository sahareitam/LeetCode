class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        mid = (r + l) // 2

        while l <= r:
            if target == nums[mid]:
                return mid
            elif l == r:
                return -1
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1
            mid = (r + l) // 2

        return -1