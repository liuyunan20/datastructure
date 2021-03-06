from typing import List


class Solution:
    # TLE version
    def numIslands_TLE1(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = []
        result = 0
        for i in range(m):
            for j in range(n):
                current_island = []
                if (i, j) not in visited and grid[i][j] == '1':
                    result += 1
                    current_island.append((i, j))
                    visited.append((i, j))
                    while current_island:
                        island_edge = []
                        for x, y in current_island:
                            if x - 1 >= 0 and grid[x - 1][y] == '1' and (x - 1, y) not in visited:
                                island_edge.append((x - 1, y))
                                visited.append((x - 1, y))
                            if x + 1 < m and grid[x + 1][y] == '1' and (x + 1, y) not in visited:
                                visited.append((x + 1, y))
                                island_edge.append((x + 1, y))
                            if y - 1 >= 0 and grid[x][y - 1] == '1' and (x, y - 1) not in visited:
                                visited.append((x, y - 1))
                                island_edge.append((x, y - 1))
                            if y + 1 < n and grid[x][y + 1] == '1' and (x, y + 1) not in visited:
                                visited.append((x, y + 1))
                                island_edge.append((x, y + 1))
                        current_island = island_edge
        return result

    def numIslands_TLE2(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        lands = []
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    lands.append((i, j))
        while lands:
            i, j = lands.pop(0)
            current_island = []
            result += 1
            current_island.append((i, j))
            while current_island:
                island_edge = []
                for x, y in current_island:
                    if x - 1 >= 0 and grid[x - 1][y] == '1' and (x - 1, y) in lands:
                        island_edge.append((x - 1, y))
                        lands.remove((x - 1, y))
                    if x + 1 < m and grid[x + 1][y] == '1' and (x + 1, y) in lands:
                        lands.remove((x + 1, y))
                        island_edge.append((x + 1, y))
                    if y - 1 >= 0 and grid[x][y - 1] == '1' and (x, y - 1) in lands:
                        island_edge.append((x, y - 1))
                        lands.remove((x, y - 1))
                    if y + 1 < n and grid[x][y + 1] == '1' and (x, y + 1) in lands:
                        lands.remove((x, y + 1))
                        island_edge.append((x, y + 1))
                current_island = island_edge

        return result

    # change every visited '1' to '0'
    def numIslands_correct(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                current_island = []
                if grid[i][j] == '1':
                    result += 1
                    current_island.append((i, j))
                    grid[i][j] = "0"
                    while current_island:
                        island_edge = []
                        for x, y in current_island:
                            if x - 1 >= 0 and grid[x - 1][y] == '1':
                                island_edge.append((x - 1, y))
                                grid[x - 1][y] = '0'
                            if x + 1 < m and grid[x + 1][y] == '1':
                                island_edge.append((x + 1, y))
                                grid[x + 1][y] = '0'
                            if y - 1 >= 0 and grid[x][y - 1] == '1':
                                island_edge.append((x, y - 1))
                                grid[x][y - 1] = '0'
                            if y + 1 < n and grid[x][y + 1] == '1':
                                island_edge.append((x, y + 1))
                                grid[x][y + 1] = '0'
                        current_island = island_edge
        return result

    # use recursion to implement DFS
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return
            if grid[i][j] == '0':
                return
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)

        m = len(grid)
        n = len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    dfs(grid, i, j)
        return result
