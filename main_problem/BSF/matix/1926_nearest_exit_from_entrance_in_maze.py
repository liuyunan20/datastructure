from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        queue = []
        visited = {tuple(entrance),}
        i, j = entrance
        for h, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            a = i + h
            b = j + v
            if 0 <= a < m and 0 <= b < n and maze[a][b] == ".":
                queue.append((a, b))
        if not queue:
            return -1
        step = 0
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                i, j = queue.pop(0)
                for h, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    a = i + h
                    b = j + v
                    if (a, b) not in visited and a < 0 or a == m or b < 0 or b == n:
                        return step
                    if (a, b) not in visited and maze[a][b] == ".":
                        queue.append((a, b))
                        visited.add((a, b))
        return -1
