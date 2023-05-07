from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def backtrack(i, current, diagonal, rdiagonal, col):
            if i == n:
                result.append(list(current))
                return
            # find_space = False
            for j in range(n):
                if j not in col and (i + j) not in rdiagonal and (i - j) not in diagonal:
                    # find_space = True
                    current.append((i, j))
                    rdiagonal.append(i + j)
                    diagonal.append(i - j)
                    col.append(j)
                    backtrack(i + 1, current, diagonal, rdiagonal, col)
                    current.pop()
                    diagonal.pop()
                    rdiagonal.pop()
                    col.pop()
            # if not find_space:
            #     return

        backtrack(0, [], [], [], [])
        res = []
        for queens in result:
            board = [["."] * n for _ in range(n)]
            for i, j in queens:
                board[i][j] = "Q"
                board[i] = "".join(board[i])
            res.append(board)
        return res
