class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        sec = float("inf")
        for i in nums:
            if i <= first:
                first = i
            elif i <= sec:
                sec = i
            else:
                return True
        return False