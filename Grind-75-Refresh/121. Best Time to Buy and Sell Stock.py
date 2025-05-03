class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_prof = 0
        for p in prices:
            if p - min_price > max_prof:
                max_prof = p - min_price
            if p < min_price:
                min_price = p
        return max_prof