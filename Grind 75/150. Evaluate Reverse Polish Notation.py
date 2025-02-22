class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        i = 2
        stack = []
        for token in tokens:
            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                op = token

                if op == "+":
                    result = a + b
                elif op == "-":
                    result = a - b
                elif op == "*":
                    result = a * b
                elif op == "/":

                    result = int(float(a) / b)
                stack.append(result)
            else:
                stack.append(int(token))
        return int(stack[0])