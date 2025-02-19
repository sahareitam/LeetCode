class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Set = set(nums)
        dup_num = sum(nums)-sum(Set)

        return[dup_num, sum(range(1,len(nums)+1))-sum(Set)]