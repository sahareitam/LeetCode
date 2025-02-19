class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        size = len(sort)
        last=-1
        for i,x in enumerate(sort):
            if x >= size-i and size-i > last:
                return size-i
            last = x
        return-1