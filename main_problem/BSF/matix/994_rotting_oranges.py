from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        visited = set()
        fresh = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh = True
        if not queue and not fresh:
            return 0
        minute = -1
        while queue:
            minute += 1
            l = len(queue)
            for _ in range(l):
                i, j = queue.pop(0)
                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    r = i + d[0]
                    c = j + d[1]
                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r, c))
                        visited.add((r, c))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minute
