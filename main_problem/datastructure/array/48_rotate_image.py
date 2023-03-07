from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp = []

        for j in range(n):
            col = []
            for i in range(n):
                col.append(matrix[i][j])
            temp.append(list(col))
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][n - j - 1]
