from _ast import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix:
                for row in matrix:
                    if row:
                        result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix:
                for row in matrix[::-1]:
                    if row:
                        result.append(row.pop(0))
        return result
