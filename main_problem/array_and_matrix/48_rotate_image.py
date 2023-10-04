from _ast import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy = [list(row) for row in matrix]
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = copy[n - 1 - j][i]
