class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minarr = []
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min = min(self.min, val)
        self.stack.append(val)
        self.minarr.append(self.min)

    def pop(self):
        """
        :rtype: None
        """
        self.minarr.pop()
        self.stack.pop()
        if self.minarr:
            self.min = self.minarr[-1]
        else:
            self.min = float('inf')

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minarr[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()