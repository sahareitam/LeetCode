class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        last_sum = sum(nums[:k])
        max_sum = last_sum
        for i in range(len(nums)-k):
            last_sum = last_sum - nums[i] + nums[k+i]
            max_sum = max(max_sum,last_sum)
        return max_sum/k
