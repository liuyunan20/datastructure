from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        copy = [x[:] for x in board]
        def change(i, j):
            counter = -copy[i][j]
            for v in [-1, 0, 1]:
                for h in [-1, 0, 1]:
                    a, b = i + v, j + h
                    if 0 <= a < m and 0<= b < n and copy[a][b] == 1:
                        counter += 1
            if counter < 2 or counter > 3:
                board[i][j] = 0
            if counter == 3:
                board[i][j] = 1
        for i in range(m):
            for j in range(n):
                change(i, j)
