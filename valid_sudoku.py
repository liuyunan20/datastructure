from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ".", ".", ".", ".", ".", ".", ".", "."]
            for j in board[i]:
                if j in valid:
                    valid.remove(j)
                else:
                    return False

            for j in range(9):
                if board[j][i] in valid:
                    valid.remove(board[j][i])
                else:
                    return False

            for x in range(3):
                for y in range(3):
                    if board[3 * (i // 3) + x][3 * (i % 3) + y] in valid:
                        valid.remove(board[3 * (i // 3) + x][3 * (i % 3) + y])
                    else:
                        return False
        return True
