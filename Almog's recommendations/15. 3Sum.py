class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m = l + 1
            r = len(nums) - 1
            while m < r:
                zero = nums[l] + nums[m] + nums[r]
                if zero == 0:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1

                if zero < 0:
                    m += 1
                if zero > 0:
                    r -= 1

        return res