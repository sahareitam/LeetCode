class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        count_c = Counter(chars)
        for word in words:
            t_sum = 0
            seen = {}
            for c in word:
                if c in count_c and count_c[c] >= word.count(c):
                    if c not in seen:
                        t_sum += word.count(c)
                        seen[c]=0
                else:
                    t_sum = 0
                    break
            res += t_sum
        return res