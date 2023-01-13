from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
        dist = 0
        visited = set()
        while queue:
            dist += 1
            l = len(queue)
            for _ in range(l):
                i, j = queue.pop(0)
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r = i + d[0]
                    c = j + d[1]
                    if 0 <= r < m and 0 <= c < n and mat[r][c] == 1 and (r, c) not in visited:
                        mat[r][c] = dist
                        visited.add((r, c))
                        queue.append((r, c))
        return mat
