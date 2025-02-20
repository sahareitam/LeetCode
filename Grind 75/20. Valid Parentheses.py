class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        fit = {")": "(", "}": "{", "]": "["}
        for i in s:
            if stack and i in fit and fit[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
