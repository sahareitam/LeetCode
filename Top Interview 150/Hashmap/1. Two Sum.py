class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hashmap:
                return[i,hashmap[temp]]
            hashmap[nums[i]] = i
        return []