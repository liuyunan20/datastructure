from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_line_0 = False
        first_col_0 = False
        for x in matrix[0]:
            if x == 0:
                first_line_0 = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_0 = True
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        if first_line_0:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_0:
            for i in range(m):
                matrix[i][0] = 0
