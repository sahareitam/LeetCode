class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')', '{':'}','[':']'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            elif stack and dic[stack[-1]] == c:
                stack.pop()
            else:
                return False
        return True if not stack else False
