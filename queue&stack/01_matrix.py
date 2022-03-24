from typing import List


class Solution:
    # tle solution using dfs recursion
    def updateMatrix_tle(self, mat: List[List[int]]) -> List[List[int]]:

        def dfs(m, n, i, j, visited):
            if i < 0 or i == m or j < 0 or j == n:
                return float('inf')
            if mat[i][j] == 0:
                return 0
            if mat[i][j] > 1:
                return mat[i][j]

            if mat[i][j] == 1 and (i, j) not in visited:
                visited.append((i, j))
                visited_clone1 = [x for x in visited]
                visited_clone2 = [x for x in visited]
                visited_clone3 = [x for x in visited]
                visited_clone4 = [x for x in visited]
                step1 = 1 + dfs(m, n, i + 1, j, visited_clone1)
                if step1 == 1:
                    return 1
                step2 = 1 + dfs(m, n, i - 1, j, visited_clone2)
                if step2 == 1:
                    return 1
                step3 = 1 + dfs(m, n, i, j + 1, visited_clone3)
                if step3 == 1:
                    return 1
                step4 = 1 + dfs(m, n, i, j - 1, visited_clone4)
                if step4 == 1:
                    return 1
                return min(step1, step2, step3, step4)

            return float('inf')

        m = len(mat)
        n = len(mat[0])
        for x in range(m):
            for y in range(n):
                visited = []
                mat[x][y] = dfs(m, n, x, y, visited)
        return mat

    # another tle solution using bfs
    def updateMatrix_tle(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat_1 = [0 for x in range(m) for y in range(n)]
        positions_0 = []
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 1:
                    mat[x][y] = float('inf')
                else:
                    positions_0.append((x, y))
        for position in positions_0:
            current_round = [position]
            step = 0
            while current_round:
                step += 1
                next_round = []
                for p in current_round:
                    i, j = p
                    if i - 1 >= 0 and step < mat[i - 1][j]:
                        mat[i - 1][j] = step
                        next_round.append((i - 1, j))
                    if i + 1 < m and step < mat[i + 1][j]:
                        mat[i + 1][j] = step
                        next_round.append((i + 1, j))
                    if j - 1 >= 0 and step < mat[i][j - 1]:
                        mat[i][j - 1] = step
                        next_round.append((i, j - 1))
                    if j + 1 < n and step < mat[i][j + 1]:
                        mat[i][j + 1] = step
                        next_round.append((i, j + 1))
                current_round = next_round
        return mat

    # bfs solution
    # append all 0 first, find all 1 positions around 0
    # then find all 2 positions around 1, and so on
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat_1 = [0 for x in range(m) for y in range(n)]
        positions = []
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 1:
                    mat[x][y] = -1
                else:
                    positions.append((x, y))
        while positions:
            i, j = positions.pop(0)
            if i - 1 >= 0 and mat[i - 1][j] == -1:
                mat[i - 1][j] = mat[i][j] + 1
                positions.append((i - 1, j))
            if i + 1 < m and mat[i + 1][j] == -1:
                mat[i + 1][j] = mat[i][j] + 1
                positions.append((i + 1, j))
            if j - 1 >= 0 and mat[i][j - 1] == -1:
                mat[i][j - 1] = mat[i][j] + 1
                positions.append((i, j - 1))
            if j + 1 < n and mat[i][j + 1] == -1:
                mat[i][j + 1] = mat[i][j] + 1
                positions.append((i, j + 1))

        return mat
