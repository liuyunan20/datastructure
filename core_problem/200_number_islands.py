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
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    counter += 1
        return counter
