class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter_col = []
        counter_row = []
        for _ in range(n):
            counter_col.append([])

        for r in range(n):
            counter_row.append(str(grid[r]))
            for c in range(n):
                counter_col[c].append(grid[r][c])
        for c in range(n):
            counter_col[c] = str(counter_col[c])

        counter_row = Counter(counter_row)
        counter_col = Counter(counter_col)
        counter = 0
        for col in counter_col:
            if col in counter_row:
                counter += counter_col[col]*counter_row[col]
        return counter