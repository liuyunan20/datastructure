class Solution:
    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        counter = 0
        queue = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    counter += 1
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        a, b = queue.pop(0)
                        grid[a][b] = "0"
                        if a+1 < m and (a+1, b) not in visited and grid[a+1][b] == "1":
                            queue.append((a+1, b))
                            visited.add((a+1, b))
                        if a-1 >= 0 and (a-1, b) not in visited and grid[a-1][b] == "1":
                            queue.append((a-1, b))
                            visited.add((a-1, b))
                        if b+1 < n and (a, b+1) not in visited and grid[a][b+1] == "1":
                            queue.append((a, b+1))
                            visited.add((a, b+1))
                        if b-1 >= 0 and (a, b-1) not in visited and grid[a][b-1] == "1":
                            queue.append((a, b-1))
                            visited.add((a, b-1))
        return counter

    def numIslands_DFS(self, grid: List[List[str]]) -> int:
        def dsf(i, j, m, n):
            val = grid[i][j]
            if grid[i][j] != "1":
                return 0
            if grid[i][j] == "1":
                island = [(i, j)]
                while island:
                    x, y = island.pop()
                    for h, v in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                        a = x + h
                        b = y + v
                        if 0 <= a < m and 0 <= b < n and grid[a][b] == "1":
                            grid[a][b] = -1
                            island.append((a, b))
                return 1
        m = len(grid)
        n = len(grid[0])
        result = 0
        for p in range(m):
            for q in range(n):
                result += dsf(p, q, m, n)
        return result
