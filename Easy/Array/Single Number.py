class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        setnums = set(nums)
        for i in setnums:
            nums.remove(i)

            if i in nums:
                nums.remove(i)
            else:
                return i
