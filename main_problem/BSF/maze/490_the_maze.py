from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        directions = {}
        for i in range(m):
            for j in range(n):
                directions[(i, j)] = set()

        def find_direction(i, j):
            d = []
            if i + 1 < m and maze[i + 1][j] == 0 and "down" not in directions[(i, j)]:
                d.append("down")
            if i - 1 >= 0 and maze[i - 1][j] == 0 and "up" not in directions[(i, j)]:
                d.append("up")
            if j + 1 < n and maze[i][j + 1] == 0 and "right" not in directions[(i, j)]:
                d.append("right")
            if j - 1 >= 0 and maze[i][j - 1] == 0 and "left" not in directions[(i, j)]:
                d.append("left")
            return d

        def move(now, direction):
            i, j = now
            directions[(i, j)].add(direction)
            if direction == "left":
                while j >= 0 and maze[i][j] == 0:
                    j -= 1
                directions[(i, j + 1)].add("right")
                return [i, j + 1]
            if direction == "right":
                while j < n and maze[i][j] == 0:
                    j += 1
                directions[(i, j - 1)].add("left")
                return [i, j - 1]
            if direction == "up":
                while i >= 0 and maze[i][j] == 0:
                    i -= 1
                directions[(i + 1, j)].add("down")
                return [i + 1, j]
            if direction == "down":
                while i < m and maze[i][j] == 0:
                    i += 1
                directions[(i - 1, j)].add("up")
                return [i - 1, j]

        queue = [start]
        visited = set()
        while queue:
            p = queue.pop(0)
            i, j = p
            ds = find_direction(i, j)
            if not ds:
                continue
            for d in ds:
                stop = move(p, d)
                if stop == destination:
                    return True
                i, j = stop
                if find_direction(i, j):
                    queue.append(stop)
        return False
