class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b_count = Counter("balloon")
        str_count = Counter(text)
        times = len(text)
        for char in b_count:
            if (char in str_count):
                if times > str_count[char]/b_count[char]:
                    times = str_count[char]/b_count[char]
            else:
                return 0
        return times