class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for i in range(n):
            grid[i] = tuple(grid[i])

        counter = Counter(grid)
        count = 0
        for col in zip(*grid):
            count += counter[col]
        return count