class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        all_str = "".join(words)
        count = Counter(all_str)

        for key in count:
            if count[key] % len(words) != 0:
                return False
        return True