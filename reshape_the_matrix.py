class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) == r * c:
            mat_list = [x for row in mat for x in row]
            return [[mat_list[c * i + j] for j in range(c)] for i in range(r)]
        return mat
