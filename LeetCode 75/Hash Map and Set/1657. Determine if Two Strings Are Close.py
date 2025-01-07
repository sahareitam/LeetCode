class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # compare length
        if len(word1) != len(word2):
            return False

        # compare chars
        if set(word1).union(set(word2)) != set(word2):
            return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        res = []
        for i in set(word1):
            res.append(counter1[i])
        for i in set(word2):
            if counter2[i] in res:
                res.remove(counter2[i])
        return res == []

