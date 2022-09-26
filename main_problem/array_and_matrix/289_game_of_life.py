from _ast import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def count_1(row, column):
            m = len(board)
            n = len(board[0])
            count = 0
            for offset_row in range(-1, 2):
                for offset_col in range(-1, 2):
                    if not (offset_row == 0 and offset_col == 0):
                        if 0 <= row + offset_row < m and 0 <= column + offset_col < n \
                                and board[row + offset_row][column + offset_col] == 1:
                            count += 1
            return count

        to_one = []
        to_zero = []
        m = len(board)
        n = len(board[0])
        # find out the positions needing to change
        for i in range(m):
            for j in range(n):
                ones = count_1(i, j)
                if (ones < 2 or ones > 3) and board[i][j] == 1:
                    to_zero.append((i, j))
                if ones == 3 and board[i][j] == 0:
                    to_one.append((i, j))

        # change the positions found in the above step
        for i, j in to_one:
            board[i][j] = 1
        for i, j in to_zero:
            board[i][j] = 0
