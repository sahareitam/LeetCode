class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        res = len(s)
        for i in set(s):
            if s.count(i) % 2 == 1:
                odds += 1

        return res - (odds - 1) if odds > 1 else res