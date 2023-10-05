from _ast import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        copy = [list(row) for row in matrix]
        changed_row = set()
        changed_col = set()
        for i in range(m):
            for j in range(n):
                if copy[i][j] == 0:
                    if j not in changed_col:
                        for i1 in range(m):
                            matrix[i1][j] = 0
                            changed_col.add(j)
                    if i not in changed_row:
                        for j1 in range(n):
                            matrix[i][j1] = 0
                            changed_row.add(i)
