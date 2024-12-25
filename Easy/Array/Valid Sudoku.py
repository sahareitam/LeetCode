class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = {}
        row = {}
        box = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if c not in col:
                    col[c] = []
                if r not in row:
                    row[r] = []
                if (r // 3, c // 3) not in box:
                    box[(r // 3, c // 3)] = []

                if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in box[(r // 3, c // 3)]:
                    return False
                col[c].append(board[r][c])
                row[r].append(board[r][c])
                box[(r // 3, c // 3)].append(board[r][c])
        return True
