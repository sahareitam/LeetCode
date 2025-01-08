class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n-1
        the_max = 0
        while l<r:
            val = min(height[l],height[r])*(r-l)
            the_max = max(the_max,val)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return the_max