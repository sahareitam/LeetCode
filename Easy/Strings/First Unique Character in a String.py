class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_counter = Counter(s)
        n = len(s)
        for i in range(n):
            if hash_counter[s[i]] == 1:
                return i
        return -1