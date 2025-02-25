class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = {}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen[nums[i]] = 0
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    l += 1

        return res
