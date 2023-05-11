from typing import List


class Solution:
    def exist_tle(self, board: List[List[str]], word: str) -> bool:
        def look_for_next(i, j, p, visited):
            res = []
            for hd, vd in [(1, 0), (-1, 0), (0 ,1), (0, -1)]:
                a = i + hd
                b = j + vd
                if m > a >= 0 and n > b >= 0 and (a, b) not in visited and board[a][b] == word[p]:
                    if p == wl - 1:
                        return True
                    res.append((i + hd, j + vd))
            for x, y in res:
                visited.append((x, y))
                if look_for_next(x, y, p + 1, list(visited)):
                    return True
                visited.pop()
            return False

        m = len(board)
        n = len(board[0])
        wl = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if wl == 1:
                        return True
                    if look_for_next(i, j, 1, [(i, j)]):
                        return True
        return False
