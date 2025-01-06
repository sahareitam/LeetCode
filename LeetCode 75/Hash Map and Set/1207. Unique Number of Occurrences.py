class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        dic = {}
        for i in counter:
            if counter[i] in dic:
                return False
            dic[counter[i]] = 0
        return True