class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            dic[num] = i
