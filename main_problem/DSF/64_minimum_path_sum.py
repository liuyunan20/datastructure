from typing import List


class Solution:
    def minPathSum_tle(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = []

        def backtrack(path, i, j):
            if i == m - 1 and j == n - 1:
                result.append(path + grid[i][j])
                return
            elif i < m - 1 and j < n - 1:
                backtrack(path + grid[i][j], i + 1, j)
                backtrack(path + grid[i][j], i, j + 1)
            elif i < m - 1:
                backtrack(path + grid[i][j], i + 1, j)
            elif j < n - 1:
                backtrack(path + grid[i][j], i, j + 1)

        backtrack(0, 0, 0)
        return min(result)
