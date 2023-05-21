class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def find_land(x, y, land):
            for h, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                a = x + h
                b = y + v
                if 0 <= a < n and 0 <= b < n and grid[a][b] == 1 and (a, b) not in land:
                    land.add((a, b))
                    find_land(a, b, land)

        land1 = set()
        land2 = set()
        n = len(grid)
        land = 1
        for i in range(n):
            for j in range(n):
                if land == 2 and grid[i][j] == 1:
                    land2.add((i, j))
                    find_land(i, j, land2)
                if land == 1 and grid[i][j] == 1:
                    land1.add((i, j))
                    find_land(i, j, land1)
                    land = 2

        result = 2 * n
        for i, j in land1:
            for x, y in land2:
                distance = max(abs(i - x) - 1, 0) + max(abs(j - y) - 1, 0) + 1
                result = min(result, distance)
        return result

