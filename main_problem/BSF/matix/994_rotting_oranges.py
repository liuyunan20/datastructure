from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        queue = []
        step = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                    step = -1
                if grid[i][j] == 1:
                    step = -1

        while queue:
            l = len(queue)
            step += 1
            for _ in range(l):
                i, j = queue.pop(0)
                for h, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    a = i + h
                    b = j + v
                    if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                        grid[a][b] = 2
                        queue.append((a, b))
                        visited.add((a, b))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return step
