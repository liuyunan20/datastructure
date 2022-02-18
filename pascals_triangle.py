class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            pascal_triangle = [[1]]
        elif numRows == 2:
            pascal_triangle = [[1], [1, 1]]
        elif numRows > 2:
            pascal_triangle = [[1], [1, 1]]
            for i in range(2, numRows):
                el = []
                el.append(1)
                for j in range(i - 1):
                    el.append(pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j + 1])
                el.append(1)
                pascal_triangle.append(el)
        return pascal_triangle
