from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def help(i, j):
            if i > 0 and j > 0:
                memo[(i, j)] = min(memo[(i - 1, j)] + grid[i][j], memo[(i, j - 1)] + grid[i][j])
            elif i > 0:
                memo[(i, j)] = memo[(i - 1, j)] + grid[i][j]
            elif j > 0:
                memo[(i, j)] = memo[(i, j - 1)] + grid[i][j]
            else:
                memo[(i, j)] = grid[i][j]

        for i in range(m):
            for j in range(n):
                help(i, j)
        return memo[(m - 1, n - 1)]
