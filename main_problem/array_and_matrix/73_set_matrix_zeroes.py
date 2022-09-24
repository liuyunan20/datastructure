from _ast import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        for i in zero_rows:
            matrix[i] = [0 for _ in range(n)]
        for j in zero_columns:
            for i in range(m):
                matrix[i][j] = 0

    # the first value of every row and column to indicate
    # if there is zero in this row or column
    def setZeroes_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_col_0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in range(n)]
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            matrix[0] = [0 for _ in range(n)]
        if first_col_0:
            for i in range(m):
                matrix[i][0] = 0
