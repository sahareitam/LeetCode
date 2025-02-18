class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = "0"
        flag = False
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                flag = True
                if res[0] < num[i]:
                    res = num[i]
        if flag:
            return res*3
        else:
            return ""