from _ast import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def change(x, y, m, n):
            neighbor = 0
            for h in range(-1, 2):
                for v in range(-1, 2):
                    if h == 0 and v == 0:
                        continue
                    a = x + h
                    b = y + v
                    if 0 <= a < m and 0 <= b < n and copy[a][b] == 1:
                        neighbor += 1
            if copy[x][y] == 0 and neighbor == 3:
                board[x][y] = 1
            if copy[x][y] == 1 and (neighbor > 3 or neighbor < 2):
                board[x][y] = 0

        copy = [list(row) for row in board]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                change(i, j, m, n)
