class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == right_sum - num:
                return i
            left_sum += num
            right_sum -= num
        return -1