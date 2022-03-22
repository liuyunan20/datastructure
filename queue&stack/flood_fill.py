from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        def dfs(i, m, n, sr, sc, newColor, visited):
            if sr < 0 or sr >= m:
                return
            if sc < 0 or sc >= n:
                return
            if (sr, sc) not in visited and image[sr][sc] == i:
                visited.append((sr, sc))
                image[sr][sc] = newColor
                dfs(i, m, n, sr + 1, sc, newColor, visited)
                dfs(i, m, n, sr - 1, sc, newColor, visited)
                dfs(i, m, n, sr, sc + 1, newColor, visited)
                dfs(i, m, n, sr, sc - 1, newColor, visited)

        dfs(image[sr][sc], m, n, sr, sc, newColor, [])
        return image
