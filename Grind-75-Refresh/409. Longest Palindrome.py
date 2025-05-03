class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        count = 0
        flag = False
        for k in dic:
            if dic[k] % 2 == 0:
                count += dic[k]
            else:
                flag = True
                count += dic[k]-1
        return count if not flag else count + 1