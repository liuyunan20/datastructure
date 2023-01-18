from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = [board]
        queue = [board]
        step = 0
        if board == [[1,2,3],[4,5,0]]:
            return step
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                board = queue.pop(0)
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    board_c = [[0 for _ in range(3)] for _ in range(2)]
                    for m in range(2):
                        for n in range(3):
                            board_c[m][n] = board[m][n]
                            if board[m][n] == 0:
                                i, j = m, n
                    r = i + d[0]
                    c = j + d[1]
                    if 0 <= r < 2 and 0 <= c < 3:
                        board_c[i][j], board_c[r][c] = board_c[r][c], board_c[i][j]
                        if board_c == [[1,2,3],[4,5,0]]:
                            return step
                        if board_c not in visited:
                            queue.append(board_c)
                        visited.append(board_c)
        return -1
