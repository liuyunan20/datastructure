class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def find_land(x, y):
            for h, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                a = x + h
                b = y + v
                if 0 <= a < n and 0 <= b < n and grid[a][b] == 1 and (a, b) not in land:
                    land.add((a, b))
                    find_land(a, b)

        land = set()
        n = len(grid)
        found1 = False
        for i in range(n):
            if found1:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    land.add((i, j))
                    find_land(i, j)
                    found1 = True
                    break

        def shortestBridge(self, grid: List[List[int]]) -> int:
            def find_land(x, y):
                for h, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    a = x + h
                    b = y + v
                    if 0 <= a < n and 0 <= b < n and grid[a][b] == 1 and (a, b) not in land:
                        land.add((a, b))
                        find_land(a, b)

            land = set()
            n = len(grid)
            found1 = False
            for i in range(n):
                if found1:
                    break
                for j in range(n):
                    if grid[i][j] == 1:
                        land.add((i, j))
                        find_land(i, j)
                        found1 = True
                        break

            result = -1
            queue = list(land)
            visited = set()
            while queue:
                result += 1
                l = len(queue)
                for _ in range(l):
                    i, j = queue.pop(0)
                    for h, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        a = i + h
                        b = j + v
                        if 0 <= a < n and 0 <= b < n and (a, b) not in visited:
                            if grid[a][b] == 0:
                                queue.append((a, b))
                            if grid[a][b] == 1 and (a, b) not in land:
                                return result
                            visited.add((a, b))

