class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)
        n = max(s,t,key=len)
        for i in n:
            if countS[i] != countT[i]:
                return False
        return True