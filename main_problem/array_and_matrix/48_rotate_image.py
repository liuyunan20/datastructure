class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        j = 0
        while n - 2 * j > 1:
            for i in range(n - 2 * j - 1):
                converter1 = matrix[j][j + i]
                matrix[j][j + i] = matrix[n - 1 - j - i][j]
                converter2 = matrix[j + i][n - 1 - j]
                matrix[j + i][n - 1 - j] = converter1
                converter1 = matrix[n - 1 - j][n - 1 - j - i]
                matrix[n - 1 - j][n - 1 - j - i] = converter2
                matrix[n - 1 - j - i][j] = converter1
                print(matrix)
            j += 1
