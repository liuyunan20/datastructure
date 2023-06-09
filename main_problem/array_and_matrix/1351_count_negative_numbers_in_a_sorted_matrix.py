class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        counter = 0
        for i in range(m):
            if grid[i][0] < 0:
                counter += n * (m - i)
                return counter
            for j in range(n):
                if grid[i][j] < 0:
                    counter += n - j
                    break
        return counter
