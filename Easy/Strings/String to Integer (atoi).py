class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        res = "0"
        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1
        while i < n and s[i].isdigit():
            res = res + s[i]
            i += 1
        if int(res) * sign > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif int(res) * sign < -2 ** 31:
            return -(2 ** 31)

        return int(res) * sign
