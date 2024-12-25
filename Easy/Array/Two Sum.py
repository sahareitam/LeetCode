class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hmap:
                return [i,hmap[target - nums[i]]]
            hmap[nums[i]] = i