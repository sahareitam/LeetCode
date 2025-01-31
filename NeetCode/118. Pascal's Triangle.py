class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1],[1,1]]
        if numRows == 1:
            return [res[0]]
        elif numRows == 2:
            return res
        else:
            i = 1
            while i < numRows-1:
                temp = [1]
                for j in range(1,len(res[i])):
                    temp.append(res[i][j-1]+res[i][j])
                temp.append(1)
                i+=1
                res.append(temp)
        return res
