class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_prof = 0
        min_num = float('inf')

        for num in prices:
            if min_num > num:
                min_num = num
            if max_prof < num - min_num:
                max_prof = num - min_num
        return max_prof
