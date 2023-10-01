class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def sub_box(m, n):
            num = set()
            for i in range(3 * m, 3 * (m + 1)):
                for j in range(3 * n, 3 * (n + 1)):
                    if board[i][j]!= ".":
                        if board[i][j] in num:
                            return False
                        else:
                            num.add(board[i][j])
            return True

        for row in board:
            nums = set()
            for cell in row:
                if cell != ".":
                    if cell in nums:
                        return False
                    else:
                        nums.add(cell)
        for i in range(9):
            nums = set()
            for row in board:
                if row[i] != ".":
                    if row[i] in nums:
                        return False
                    else:
                        nums.add(row[i])
        for a in range(3):
            for b in range(3):
                if not sub_box(a, b):
                    return False
        return True
