class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        nums.sort()
        res = []
        for i in range(size-1):
            if i > 0 and nums[i] == nums[i-1]:
               continue
            if nums[i] > 0:
                return res
            else:
                l = i+1
                r = size-1
                while  l < r:
                    threeSum = nums[i]+nums[l]+nums[r]
                    if threeSum == 0:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                    elif threeSum > 0:
                        r-=1
                    elif threeSum < 0:
                        l+=1
        return res