class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        suff = 1
        pref = 1
        suff_list = []
        pref_list = []
        for i in range(n-1):
            suff *=nums[i]
            answer[i] = suff
        for i in range(1,n):
            answer[n-i] = answer[n-i-1]*pref
            pref *=nums[n-i]
            if i == n-1:
                answer[0] = pref
        return(answer)