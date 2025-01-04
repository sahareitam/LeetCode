class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = len(matrix)
        flag = False
        if 0 in matrix[0]:
            flag = True
        for r in range(1, m):
            if 0 in matrix[r]:
                while 0 in matrix[r]:
                    i_of_zero = matrix[r].index(0)
                    matrix[0][i_of_zero] = 0
                    matrix[r][i_of_zero] = 1
                matrix[r][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
            else:
                for z in range(n):
                    if matrix[0][z] == 0:
                        matrix[i][z] = 0
        if flag == True:
            for z in range(n):
                matrix[0][z] = 0


