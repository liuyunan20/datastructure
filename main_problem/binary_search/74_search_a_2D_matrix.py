class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        line_start = 0
        line_end = m - 1
        while line_start <= line_end:
            line = (line_start + line_end) // 2
            anchor0 = matrix[line][0]
            anchor1 = matrix[line][-1]
            if target == anchor0 or target == anchor1:
                return True
            if target < anchor0:
                line_end = line - 1
            if target > anchor1:
                line_start = line + 1
            if anchor0 < target < anchor1:
                break
        line = matrix[line]
        start = 0
        end = n - 1
        while start <= end:
            i = (start + end) // 2
            cur = line[i]
            if target == cur:
                return True
            if target < cur:
                end = i - 1
            if target > cur:
                start = i + 1
        return False
