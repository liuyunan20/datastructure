from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            if matrix:
                for item in matrix:
                    if item:
                        result.append(item.pop())
                    else:
                        return result
            if matrix:
                result.extend(reversed(matrix.pop()))
            if matrix:
                for i in range(len(matrix) - 1, -1,  -1):
                    if matrix[i]:
                        result.append(matrix[i].pop(0))
        return result
