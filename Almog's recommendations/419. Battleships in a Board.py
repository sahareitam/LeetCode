class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        cols = len(board[0])
        def dfs(board,r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'X':
                return
            board[r][c] = '.'
            dfs(board,r,c+1)
            dfs(board,r,c-1)
            dfs(board,r+1,c)
            dfs(board,r-1,c)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    dfs(board,r,c)
                    count+=1
        return count

