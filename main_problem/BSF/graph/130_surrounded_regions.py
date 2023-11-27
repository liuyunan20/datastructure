from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    capture = True
                    region = [(i, j)]
                    visited.add((i, j))
                    p = 0
                    while p < len(region):
                        a, b = region[p]
                        p += 1
                        for h, v in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            x = a + h
                            y = b + v
                            if x == -1 or x == m or y == -1 or y == n:
                               capture = False
                            if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x, y) not in visited:
                                region.append((x, y))
                                visited.add((x, y))
                    if capture:
                        for x, y in region:
                            board[x][y] = 'X'
