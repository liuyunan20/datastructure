class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            for x in matrix[0]:
                result.append(x)
            matrix.pop(0)
            if not matrix:
                return result

            n = len(matrix)
            for i in range(n):
                result.append(matrix[i][-1])
                matrix[i].pop()
            for i in range(n):
                if not matrix[i]:
                    return result

            for x in matrix[-1][::-1]:
                result.append(x)
            matrix.pop()
            if not matrix:
                return result

            n = len(matrix)
            for i in range(n):
                result.append(matrix[n - 1 - i][0])
                matrix[n - 1 - i].pop(0)
            for i in range(n):
                if not matrix[i]:
                    return result
        return result
