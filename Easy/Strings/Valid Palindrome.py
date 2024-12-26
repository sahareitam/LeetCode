class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = s.lower()
        abc = "abcdefghijklmnopqrstuvwxyz0123456789"
        res = []
        for i in p:
            if i in abc:
                res.append(i)

        return res == res[::-1]