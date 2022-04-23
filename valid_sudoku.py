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

    def isValidSudoku_hashmap(self, board: List[List[str]]) -> bool:
        digit_position = {}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    digit_position.setdefault(board[i][j], []).append((i, j))
        for digit in digit_position:
            j_set = set()
            i_set = set()
            for i, j in digit_position[digit]:
                i_set.add(i)
                j_set.add(j)
            if len(j_set) < len(digit_position[digit]) or len(i_set) < len(digit_position[digit]):
                return False
        block ={}
        for i in range(9):
            for x in range(3):
                for y in range(3):
                    block.setdefault(i, []).append((3 * (i // 3) + x, 3 * (i % 3) + y))
            for digit in digit_position:
                if len(set(digit_position[digit])&set(block[i])) > 1:
                    return False
        return True
