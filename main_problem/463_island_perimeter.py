class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for h, v in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        a = i + h
                        b = j + v
                        if not (0 <= a < m and 0 <= b < n and grid[a][b] == 1):
                            result += 1

        return result
