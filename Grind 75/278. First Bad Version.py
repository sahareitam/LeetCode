# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        mid = (l+r)//2
        badv = 0
        while l < r:
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
            mid = (l+r)//2
        return r