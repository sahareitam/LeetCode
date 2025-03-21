class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        adj = {'{': '}', '(': ')', '[': ']'}
        for i in s:
            if stack and stack[-1] in adj and adj[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0