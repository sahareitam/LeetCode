class Solution(object):
    def numIslands(self, grid):

        cols = len(grid[0])
        rows = len(grid)
        queue = deque()
        res = 0
        for ro in range(rows):
            for co in range(cols):
                if grid[ro][co] == "1":
                    queue.append((ro, co))
                    grid[ro][co] = "2"
                    while queue:
                        node = queue.popleft()
                        r = node[0]
                        c = node[1]

                        if 0 < c and grid[r][c - 1] == "1":
                            queue.append((r, c - 1))
                            grid[r][c - 1] = "2"
                        if c < cols - 1 and grid[r][c + 1] == "1":
                            queue.append((r, c + 1))
                            grid[r][c + 1] = "2"
                        if 0 < r and grid[r - 1][c] == "1":
                            queue.append((r - 1, c))
                            grid[r - 1][c] = "2"
                        if r < rows - 1 and grid[r + 1][c] == "1":
                            queue.append((r + 1, c))
                            grid[r + 1][c] = "2"
                    res += 1
        return res

