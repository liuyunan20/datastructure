from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        freq = {}
        for row in grid:
            row = tuple(row)
            freq.setdefault(row, 0)
            freq[row] += 1
        result = 0
        for j in range(n):
            col = tuple([grid[i][j] for i in range(n)])
            if col in freq:
                result += freq[col]
        return result
