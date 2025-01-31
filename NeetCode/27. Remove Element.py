class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l=0
        k=0
        r=len(nums)-1
        if r==l:
            if nums[0]==val:
                return 0
            else:
                return 1
        while l<=r:
            if nums[l] == val:
                k+=1
                while nums[r] == val and l != r:
                    k+=1
                    r-=1
                nums[r], nums[l] = nums[l],nums[r]
                r-=1
            l+=1
        return len(nums)-k
