class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        elif n == 0:
            return 0
        dic = {}

        def rec_rob(i):
            if i > n - 1:
                return 0
            if i in dic:
                return dic[i]
            step2 = rec_rob(i + 2)
            step3 = rec_rob(i + 3)

            dic[i] = max(step2 + nums[i], step3 + nums[i])
            return dic[i]

        return max(rec_rob(0), rec_rob(1))