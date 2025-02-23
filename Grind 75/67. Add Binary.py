class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(reversed(a))
        b = list(reversed(b))
        num_a = 0
        num_b = 0
        i = 0
        for A in a:
            num_a += int(A)*(2**i)
            i+=1
        i = 0
        for B in b:
            num_b += int(B)*(2**i)
            i+=1
        num = abs (num_a+num_b)
        if num == 0:
            return "0"
        res = ""
        while num > 0:
            to_add = num % 2
            res = str(to_add)+res
            num = (num - to_add) / 2
        return res