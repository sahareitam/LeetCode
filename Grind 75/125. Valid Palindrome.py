class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        for c in set(s):
            if c.isalpha() == False and c.isdigit() == False:
               s = s.replace(c,"")

        l = 0
        r =len(s)-1
        while l < r:
            if s[l] == s[r]:
                r-=1
                l+=1
            else:
                return False
        return True