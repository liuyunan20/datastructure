from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        queue = [(sr, sc)]
        color_start = image[sr][sc]
        image[sr][sc] = color
        visited = set()
        while queue:
            l = len(queue)
            for _ in range(l):
                i, j = queue.pop(0)
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r = i + d[0]
                    c = j + d[1]
                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited and image[r][c] == color_start:
                        image[r][c] = color
                        queue.append((r, c))
                        visited.add((r, c))
        return image
