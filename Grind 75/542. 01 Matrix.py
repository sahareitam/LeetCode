class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1

        while queue:
            cur = queue.popleft()
            r = cur[0]
            c = cur[1]

            if c > 0 and mat[r][c - 1] == -1:
                mat[r][c - 1] = mat[r][c] + 1
                queue.append((r, c - 1))

            if c < cols - 1 and mat[r][c + 1] == -1:
                mat[r][c + 1] = mat[r][c] + 1
                queue.append((r, c + 1))

            if r > 0 and mat[r - 1][c] == -1:
                mat[r - 1][c] = mat[r][c] + 1
                queue.append((r - 1, c))

            if r < rows - 1 and mat[r + 1][c] == -1:
                mat[r + 1][c] = mat[r][c] + 1
                queue.append((r + 1, c))
        return mat