class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        for i in range(rowIndex):
            idx = 1
            new_row = [1]
            while idx <= i:
                new_row.append(cur_row[idx-1]+cur_row[idx])
                idx+=1
            cur_row = new_row +[1]
        return cur_row
