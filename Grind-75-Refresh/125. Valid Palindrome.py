class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha_list = []
        for c in s:
            if c.isalpha() or c.isdigit():
                alpha_list.append(lower(c))

        return "".join(alpha_list) == "".join(alpha_list[::-1])