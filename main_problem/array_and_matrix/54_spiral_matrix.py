from _ast import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row = len(matrix)
        col = len(matrix[0])
        while len(result) <= row * col:
            result += matrix[0]
            matrix = matrix[1:]
            if len(result) == row * col:
                return result
            m = len(matrix)
            n = len(matrix[0])
            for i in range(m):
                result.append(matrix[i][n - 1])
                matrix[i] = matrix[i][:n - 1]
            if len(result) == row * col:
                return result
            result += matrix[m - 1][::-1]
            matrix = matrix[:m - 1]
            if len(result) == row * col:
                return result
            m = len(matrix)
            n = len(matrix[0])
            for i in range(m - 1, -1, -1):
                result.append(matrix[i][0])
                matrix[i] = matrix[i][1:]
        return result
