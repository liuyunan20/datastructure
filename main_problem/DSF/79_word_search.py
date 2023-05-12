from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def look_for_next(i, j, p, visited):
            if p == wl:
                return True
            res = []
            for hd, vd in [(1, 0), (-1, 0), (0 ,1), (0, -1)]:
                a = i + hd
                b = j + vd
                if m > a >= 0 and n > b >= 0 and not visited[a][b] and board[a][b] == word[p]:
                    res.append((i + hd, j + vd))
            for x, y in res:
                visited[x][y] = 1
                if look_for_next(x, y, p + 1, visited):
                    return True
                visited[x][y] = 0
            return False

        m = len(board)
        n = len(board[0])
        wl = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[0 for _ in range(n)] for _ in range(m)]
                    visited[i][j] = 1
                    if look_for_next(i, j, 1, visited):
                        return True
        return False
