from typing import List


class Solution:

    def shortestDistance_bfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        def move(now, direction):
            i, j = now
            count = 0
            if direction == "left":
                while j >= 0 and maze[i][j] == 0:
                    j -= 1
                    count += 1
                return [i, j + 1], count - 1
            if direction == "right":
                while j < n and maze[i][j] == 0:
                    j += 1
                    count += 1
                return [i, j - 1], count - 1
            if direction == "up":
                while i >= 0 and maze[i][j] == 0:
                    i -= 1
                    count += 1
                return [i + 1, j], count - 1
            if direction == "down":
                while i < m and maze[i][j] == 0:
                    i += 1
                    count += 1
                return [i - 1, j], count - 1

        queue = [(start, 0)]
        position_step = {}
        while queue:
            l = len(queue)
            while l > 0:
                l -= 1
                p, dist = queue.pop(0)
                if tuple(p) in position_step and position_step[tuple(p)] <= dist:
                    continue
                position_step[tuple(p)] = dist
                for d in ["down", "up", "left", "right"]:
                    cur_step = position_step[tuple(p)]
                    stop, mov_step = move(p, d)
                    cur_step += mov_step
                    queue.append((stop, cur_step))
        if tuple(destination) in position_step:
            return position_step[tuple(destination)]
        return -1
