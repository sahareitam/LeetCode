class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        """
        pref = 1
        size = len(nums)
        ans = [None] * size
        for i, num in enumerate(nums):
            pref *= num
            ans[i] = pref
        suf = 1
        for i in range(size):
            if size - i - 2 < 0:
                ans[size - i - 1] = suf
            else:
                ans[size - i - 1] = suf * ans[size - i - 2]
                suf *= nums[size - i - 1]
        return ans


