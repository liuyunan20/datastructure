from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i, j = 0, 0
        m = len(mat)
        n = len(mat[0])
        result = []
        down = True
        while not (i == m - 1 and j == n - 1):
            result.append(mat[i][j])
            if i == 0  and j % 2 == 0 and j + 1 < n:
                j += 1
                down = True
                continue
            if (m % 2 == 0 and i == m - 1 and j % 2 == 0) or (m % 2 == 1 and i == m - 1 and j % 2 == 1):
                j += 1
                down = False
                continue
            if j == 0 and i % 2 == 1 and i + 1 < m:
                i += 1
                down = False
                continue
            if (n % 2 == 0 and j == n - 1 and i % 2 == 1) or (n % 2 == 1 and j == n - 1 and i % 2 == 0):
                i += 1
                down = True
                continue
            if down:
                i += 1
                j -= 1
                continue
            if not down:
                i -= 1
                j += 1
                continue
        result.append(mat[m-1][n-1])
        return result
