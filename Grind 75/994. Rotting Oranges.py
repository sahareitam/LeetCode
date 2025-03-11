class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        stack = []
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    stack.append((r, c))
                if grid[r][c] == 1:
                    count += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mins = -1

        while stack:
            stack_to_add = []
            mins += 1
            while stack:
                cur = stack.pop()
                r = cur[0]
                c = cur[1]

                for d in directions:
                    rw = r + d[0]
                    cl = c + d[1]

                    if 0 <= rw < rows and 0 <= cl < cols and grid[rw][cl] == 1:
                        grid[rw][cl] = 2
                        stack_to_add.append((rw, cl))
                        count -= 1
            stack = stack_to_add

        if count > 0:
            return -1
        return mins + 1 if mins < 0 else mins