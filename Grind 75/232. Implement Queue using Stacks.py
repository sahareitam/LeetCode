class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return temp

    def peek(self):
        """
        :rtype: int
        """
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        self.s1.append(temp)
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()